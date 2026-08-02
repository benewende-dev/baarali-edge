#!/usr/bin/env python3
"""Banc d'essai — passe un GGUF au profileur officiel et range le résultat.

Pourquoi un script plutôt que des commandes à la main : le profileur exige un
dossier de soumission complet (metadata.json valide + poids au chemin déclaré).
En fabriquer un par candidat à la main, c'est cinq occasions de se tromper d'un
champ et de comparer deux choses différentes. Ici, seuls le modèle et son
chemin changent — tout le reste est copié de notre `metadata.json` réel.

Usage :
    python bench/mesurer.py <label>            # débit + mémoire (quelques secondes)
    python bench/mesurer.py <label> --justesse # ajoute la justesse (long)
    python bench/mesurer.py --tous             # tous les candidats, sans justesse
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
POIDS = RACINE / "bench" / "models"
BRUT = RACINE / "bench" / "raw"
PYTHON = RACINE / ".venv" / "bin" / "python"
PROFILEUR = RACINE / ".venv" / "bin" / "adtc-profiler"

# Les cinq candidats de l'étape 1. Licences relevées sur l'API Hugging Face le
# 1er août 2026 : quatre Apache 2.0, un MIT — aucune restriction d'usage, ce qui
# est exigé par un dépôt public et par nos ambitions derrière.
CANDIDATS: dict[str, dict[str, str]] = {
    "smollm3-3b": {
        "repo": "ggml-org/SmolLM3-3B-GGUF",
        "fichier": "SmolLM3-Q4_K_M.gguf",
        "params": "3B",
        "licence": "apache-2.0",
    },
    "qwen35-0.8b": {
        "repo": "unsloth/Qwen3.5-0.8B-GGUF",
        "fichier": "Qwen3.5-0.8B-Q4_K_M.gguf",
        "params": "0.8B",
        "licence": "apache-2.0",
    },
    "qwen35-2b": {
        "repo": "unsloth/Qwen3.5-2B-GGUF",
        "fichier": "Qwen3.5-2B-Q4_K_M.gguf",
        "params": "2B",
        "licence": "apache-2.0",
    },
    "qwen35-4b": {
        "repo": "unsloth/Qwen3.5-4B-GGUF",
        "fichier": "Qwen3.5-4B-Q4_K_M.gguf",
        "params": "4B",
        "licence": "apache-2.0",
    },
    "phi4-mini": {
        "repo": "unsloth/Phi-4-mini-instruct-GGUF",
        "fichier": "Phi-4-mini-instruct-Q4_K_M.gguf",
        "params": "3.8B",
        "licence": "mit",
    },
    # ── Étape 2 : quantifications du socle retenu (Qwen3.5-2B) ────────────────
    # Le barème récompense la légèreté (20 %) et le débit (30 %) : descendre en
    # quantification gagne sur ces deux axes et perd sur la justesse (50 %).
    # L'équilibre ne se devine pas, il se mesure. Les variantes `UD-` sont des
    # quantifications guidées par matrice d'importance : à taille égale, elles
    # préservent mieux les poids qui comptent.
    "q2b-iq4xs": {
        "repo": "unsloth/Qwen3.5-2B-GGUF",
        "fichier": "Qwen3.5-2B-IQ4_XS.gguf",
        "params": "2B",
        "licence": "apache-2.0",
    },
    "q2b-ud-q4": {
        "repo": "unsloth/Qwen3.5-2B-GGUF",
        "fichier": "Qwen3.5-2B-UD-Q4_K_XL.gguf",
        "params": "2B",
        "licence": "apache-2.0",
    },
    "q2b-q5km": {
        "repo": "unsloth/Qwen3.5-2B-GGUF",
        "fichier": "Qwen3.5-2B-Q5_K_M.gguf",
        "params": "2B",
        "licence": "apache-2.0",
    },
    "q2b-ud-q5": {
        "repo": "unsloth/Qwen3.5-2B-GGUF",
        "fichier": "Qwen3.5-2B-UD-Q5_K_XL.gguf",
        "params": "2B",
        "licence": "apache-2.0",
    },
    "q2b-q3km": {
        "repo": "unsloth/Qwen3.5-2B-GGUF",
        "fichier": "Qwen3.5-2B-Q3_K_M.gguf",
        "params": "2B",
        "licence": "apache-2.0",
    },
    # Prédiction multi-jetons : même modèle, même quantification, tête
    # supplémentaire. Sert à savoir si `llama-bench` — que le profileur lance
    # sans réglage — en tire quoi que ce soit. Si non, la tête n'ajoute que du
    # poids, ce qui coûterait sur l'axe mémoire.
    "q2b-mtp-q4": {
        "repo": "unsloth/Qwen3.5-2B-MTP-GGUF",
        "fichier": "Qwen3.5-2B-Q4_K_M.gguf",
        "params": "2B",
        "licence": "apache-2.0",
    },
}


DELAI_S = 60      # une socket muette plus longtemps que ça est morte
ESSAIS_MAX = 20   # reprises successives avant d'abandonner


def telecharger(label: str) -> Path:
    """Récupère les poids si absents, en reprenant là où on s'est arrêté.

    Deux garde-fous, appris à nos dépens : un `urlopen` **sans délai** attend
    indéfiniment quand la connexion tombe (mesuré : 18 heures de blocage
    silencieux sur un portable qui s'était endormi). Et sans reprise par
    plage d'octets, chaque coupure recommence des gigaoctets depuis zéro — ce
    qui, sur une connexion comptée, n'est pas une gêne mais un coût.

    Le fichier n'est renommé qu'au succès : un `.gguf` tronqué se chargerait
    comme s'il était complet et fausserait la mesure sans rien signaler.
    """
    c = CANDIDATS[label]
    # Un dossier par candidat, jamais un espace de noms plat : deux dépôts
    # différents publient le MÊME nom de fichier (`Qwen3.5-2B-Q4_K_M.gguf`
    # existe dans le dépôt normal et dans le dépôt MTP). À plat, le second
    # serait tenu pour déjà téléchargé et on mesurerait deux fois le premier,
    # sans erreur et sans s'en apercevoir.
    cible = POIDS / label / c["fichier"]
    if cible.exists():
        return cible
    cible.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://huggingface.co/{c['repo']}/resolve/main/{c['fichier']}"
    partiel = cible.with_suffix(".gguf.partial")
    print(f"  téléchargement de {c['fichier']}…", flush=True)

    for essai in range(1, ESSAIS_MAX + 1):
        deja = partiel.stat().st_size if partiel.exists() else 0
        requete = urllib.request.Request(url)
        if deja:
            requete.add_header("Range", f"bytes={deja}-")
            print(f"    reprise à {deja >> 20} Mo (essai {essai})", flush=True)
        try:
            with urllib.request.urlopen(requete, timeout=DELAI_S) as r:
                # 206 = la plage a été honorée ; 200 = le serveur renvoie tout
                # depuis le début, il faut alors repartir de zéro sous peine de
                # concaténer deux fois le même début de fichier.
                reprise = r.status == 206
                total = int(r.headers.get("content-length", 0)) + (deja if reprise else 0)
                mode = "ab" if reprise else "wb"
                lus = deja if reprise else 0
                jalon = 100 * lus // total + 10 if total else 0
                with partiel.open(mode) as f:
                    while bloc := r.read(1 << 20):
                        f.write(bloc)
                        lus += len(bloc)
                        # Un point tous les 10 % : sur 2,5 Go, une ligne par
                        # mégaoctet noie la sortie du profileur.
                        if total and (pct := 100 * lus // total) >= jalon:
                            print(f"    {pct} %  ({lus >> 20} Mo)", flush=True)
                            jalon = pct + 10
        except (TimeoutError, OSError) as e:
            print(f"    coupure ({e}) — on reprend", flush=True)
            continue
        if total and partiel.stat().st_size < total:
            continue  # le serveur a fermé avant la fin : reprendre
        partiel.rename(cible)
        return cible

    raise RuntimeError(f"{c['fichier']} : {ESSAIS_MAX} reprises sans succès")


def soumission_temporaire(label: str, poids: Path, dossier: Path) -> None:
    """Fabrique un dossier de soumission valide pointant sur ces poids."""
    meta = json.loads((RACINE / "metadata.json").read_text())
    c = CANDIDATS[label]
    meta["model"] = {
        "name": poids.stem,
        "runtime": "llama.cpp",
        "quantization": "GGUF Q4_K_M",
        "parameters_estimate": c["params"],
        "packaging": "binary_bundle",
    }
    meta["_runtime"] = {"model_path": f"model/{poids.name}"}
    (dossier / "model").mkdir(parents=True)
    (dossier / "metadata.json").write_text(json.dumps(meta, indent=2))
    # Lien symbolique : recopier 2,5 Go par mesure serait absurde.
    (dossier / "model" / poids.name).symlink_to(poids)


def mesurer(label: str, justesse: bool, tache: str, limite: int) -> dict:
    poids = telecharger(label)
    BRUT.mkdir(parents=True, exist_ok=True)
    # Le nom du fichier porte la tâche et le nombre de questions : deux mesures
    # de justesse sur des jeux différents ne sont pas comparables, les ranger
    # sous le même nom reviendrait à écraser l'une par l'autre sans le voir.
    suffixe = f"-{tache}-{limite}" if justesse else ""
    sortie = BRUT / f"{label}{suffixe}.json"
    with tempfile.TemporaryDirectory() as tmp:
        dossier = Path(tmp) / "soumission"
        dossier.mkdir()
        soumission_temporaire(label, poids, dossier)
        cmd = [
            str(PROFILEUR), "run",
            "--submission", str(dossier),
            "--mode", "participant",
            "--output", str(sortie),
        ]
        if justesse:
            cmd += ["--accuracy-task", tache, "--accuracy-limit", str(limite)]
        else:
            cmd.append("--skip-accuracy")
        subprocess.run(cmd, check=True)
    return json.loads(sortie.read_text())


def resumer(label: str, rapport: dict) -> str:
    t = rapport["throughput"]["tokens_per_second_generation"]
    ram = rapport["memory"]["peak_rss_mb"] / 1024
    # Barème officiel : S_eff = 100 × (7 Go − pic) ÷ 7 Go. Le débit, lui, est
    # noté par rapport à la MEILLEURE soumission du concours — inconnue ici,
    # donc on garde le brut et on comparera entre nous.
    eff = 100 * (7 - ram) / 7
    acc = rapport.get("accuracy") or []
    note = f" | justesse {acc[0]['score']:.3f} ({acc[0]['benchmark']})" if acc else ""
    return f"{label:14s} {t:7.1f} t/s | pic {ram:4.2f} Go | S_eff {eff:5.1f}{note}"


def main() -> int:
    if not PROFILEUR.exists():
        print("profileur absent — voir PLAN.md, étape 0", file=sys.stderr)
        return 1
    if shutil.which("llama-bench") is None:
        print("llama-bench absent du PATH (brew install llama.cpp)", file=sys.stderr)
        return 1

    args = sys.argv[1:]
    justesse = "--justesse" in args
    tache = next((a.split("=", 1)[1] for a in args if a.startswith("--tache=")), "arc_easy")
    limite = int(next((a.split("=", 1)[1] for a in args if a.startswith("--limite=")), 200))
    labels = list(CANDIDATS) if "--tous" in args else [a for a in args if a in CANDIDATS]
    if not labels:
        print(f"candidats : {', '.join(CANDIDATS)}", file=sys.stderr)
        return 1

    lignes = []
    for label in labels:
        print(f"\n=== {label} ===", flush=True)
        debut = time.monotonic()
        rapport = mesurer(label, justesse, tache, limite)
        lignes.append(f"{resumer(label, rapport)} | {time.monotonic() - debut:.0f} s")
    print("\n" + "\n".join(lignes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
