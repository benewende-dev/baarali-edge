#!/usr/bin/env python3
"""La démonstration de la vidéo de soumission, en une seule prise.

Pourquoi un script plutôt que des commandes tapées à l'écran. La vidéo est
plafonnée à **2 minutes** et le modèle met deux à quatre secondes à charger : le
recharger à chaque acte, c'est brûler un dixième du temps disponible à regarder
une barre de progression. Ici il est chargé **une fois** et les quatre actes
s'enchaînent dans le même processus.

Et surtout : rien n'est simulé. Le modèle tourne vraiment, hors ligne, sur les
poids que `download_model.sh` télécharge. Une démonstration truquée sur une
soumission dont l'argument est « chaque chiffre est mesuré » serait la seule
faute impossible à rattraper.

Ce qui est prouvé, acte par acte :

  1. **Hors ligne**   le réseau est injoignable, vérifié par `ping`, pas par une
                      icône barrée qu'on pourrait croire sur parole.
  2. **Le modèle**    `tp_002`, l'un des deux prompts déclarés, en flux — on voit
                      les jetons arriver, donc on voit que ça calcule ici.
  3. **Le canal**     une session USSD complète, à la vraie limite de
                      182 caractères, telle qu'un téléphone la recevrait.
  4. **La localité**  les documents lus sont sur le disque, et les chiffres du
                      profileur officiel sortent de `bench/raw/`.

**Tout ce qui s'affiche est en anglais**, comme le reste de ce que lira le jury.
Un écran qu'il faut traduire en le lisant est un écran qui coûte de l'attention.

Une seule chose reste en français, et c'est la plus intéressante : **les
documents de l'entreprise**. `commandes.json` est rédigé en français, la
question est posée en anglais, et le modèle répond en anglais à partir de la
pièce française. C'est exactement la situation d'une PME d'Abidjan dont les
documents sont en français et dont l'interlocuteur écrit en anglais — et ça
démontre le bilinguisme au lieu de le revendiquer.

Usage : .venv/bin/python demo/tournage.py [--repetition]

`--repetition` saute le contrôle réseau, pour préparer la prise sans couper le
Wi-Fi. **Ne jamais filmer dans ce mode** — l'acte 1 perdrait son sens.
"""
from __future__ import annotations

import json
import os
import pathlib
import subprocess
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

# Le canal USSD parle anglais **pour la caméra**, avant que `ussd` ne soit
# importé — ses libellés sont figés au chargement. Le français reste la langue
# de service par défaut du module ; ce qui change ici, c'est la langue du jury.
os.environ.setdefault("BAARALI_USSD_LANG", "en")

from ussd import (  # noqa: E402
    CODE_SERVICE,
    ECRAN_MAX,
    Assistant,
    _dessiner,
    charger_commandes,
    repondre,
)

RACINE = pathlib.Path(__file__).resolve().parent.parent

# Rythme de lecture à l'écran. Assez pour lire, pas assez pour s'ennuyer : la
# limite de deux minutes est dure, et un plan qui traîne coûte un plan qui manque.
POSE = 1.2

VERT, GRIS, GRAS, FIN = "\033[32m", "\033[90m", "\033[1m", "\033[0m"


def titre(n: int, texte: str) -> None:
    print(f"\n{GRAS}── {n}. {texte} {'─' * max(0, 58 - len(texte))}{FIN}\n")
    time.sleep(0.4)


def acte_hors_ligne(verifier: bool) -> None:
    titre(1, "The machine is offline")
    if not verifier:
        print(f"  {GRIS}(network check skipped: rehearsal mode){FIN}")
        time.sleep(POSE)
        return
    joignable = subprocess.run(
        ["ping", "-c", "1", "-t", "3", "1.1.1.1"],
        capture_output=True,
    ).returncode == 0
    if joignable:
        print("  ⚠️  Le réseau répond encore. Coupez le Wi-Fi avant de filmer.")
        sys.exit(1)
    print(f"  $ ping -c 1 1.1.1.1")
    print(f"  {VERT}No reply — this machine reaches nobody.{FIN}")
    time.sleep(POSE)


def acte_modele(a: Assistant) -> None:
    titre(2, "The model answers, on this machine")
    # `tp_002` et pas `tp_001`, pour deux raisons dites franchement. La première
    # est de fond : « summarization, drafting, and analysis » est la définition
    # officielle du domaine, et `tp_002` est exactement cela, quand `tp_001` est
    # d'abord un calcul. La seconde est de forme : `tp_001` déroule un
    # raisonnement de 500 jetons qui, filmé, mange la moitié des deux minutes —
    # et il contient l'erreur d'arrondi que le rapport documente comme limite.
    # Ce n'est pas la cacher que de ne pas la filmer : elle est écrite noir sur
    # blanc dans `REPORT.md` et sur la fiche du modèle.
    prompt = json.loads((RACINE / "metadata.json").read_text())["test_prompts"][1]["prompt"]
    print(f"  {GRIS}{prompt[:150]}…{FIN}\n")
    debut = time.monotonic()
    jetons = 0
    for morceau in a.llm.create_chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=700,
        temperature=0.0,
        repeat_penalty=1.05,
        stream=True,  # en flux : on voit que ça calcule, on ne le lit pas d'un fichier
    ):
        bout = morceau["choices"][0].get("delta", {}).get("content") or ""
        sys.stdout.write(bout)
        sys.stdout.flush()
        jetons += 1
    duree = time.monotonic() - debut
    print(f"\n\n  {VERT}{jetons} tokens in {duree:.0f} s, CPU only, no network.{FIN}")
    time.sleep(POSE)


def acte_ussd(a: Assistant) -> None:
    titre(3, f"The same model, reachable by USSD on {CODE_SERVICE}")
    saisies = ["", "3", "How many days late is order CMD-1042?"]
    texte = ""
    for i, saisie in enumerate(saisies):
        texte = saisie if not texte else f"{texte}*{saisie}"
        sortie = repondre("tournage", CODE_SERVICE, "+2250700000000", texte.lstrip("*"), a)
        _dessiner(sortie[4:])
        print(f"    {GRIS}{len(sortie)}/{ECRAN_MAX} characters{FIN}")
        time.sleep(POSE if i < len(saisies) - 1 else 0.3)
    print(f"\n  {VERT}No data plan, no app, any phone.{FIN}")
    time.sleep(POSE)


def acte_localite() -> None:
    titre(4, "Nothing left the machine")
    cmd = charger_commandes()
    print(f"  The documents it read are here: {GRAS}demo/commandes.json{FIN} "
          f"({len(cmd)} orders, on this disk)\n")
    bruts = sorted((RACINE / "bench" / "raw").glob("final-iq4xs-*.json"))
    debits, pics = [], []
    for f in bruts:
        d = json.loads(f.read_text())
        debits.append(d["throughput"]["tokens_per_second_generation"])
        pics.append(d["memory"]["peak_rss_mb"])
    med = lambda v: sorted(v)[len(v) // 2]
    print(f"  Official profiler, median of {len(bruts)} runs on this file:")
    print(f"    throughput  {GRAS}{med(debits):.2f} tokens/s{FIN}")
    print(f"    peak memory {GRAS}{med(pics):.0f} MB{FIN}  (contest ceiling: 7,000 MB)")
    print(f"\n  {VERT}A model that fits an 8 GB laptop, and calls nobody.{FIN}\n")


def main() -> int:
    repetition = "--repetition" in sys.argv
    depart = time.monotonic()
    acte_hors_ligne(verifier=not repetition)
    print(f"  {GRIS}loading weights…{FIN}")
    a = Assistant()
    acte_modele(a)
    acte_ussd(a)
    acte_localite()
    print(f"{GRIS}  [full take: {time.monotonic() - depart:.0f} s]{FIN}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
