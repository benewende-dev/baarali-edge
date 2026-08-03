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

Usage : .venv/bin/python demo/tournage.py [--repetition]

`--repetition` saute le contrôle réseau, pour préparer la prise sans couper le
Wi-Fi. **Ne jamais filmer dans ce mode** — l'acte 1 perdrait son sens.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

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
    titre(1, "La machine est hors ligne")
    if not verifier:
        print(f"  {GRIS}(contrôle réseau sauté : mode répétition){FIN}")
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
    print(f"  {VERT}Aucune réponse — la machine ne joint personne.{FIN}")
    time.sleep(POSE)


def acte_modele(a: Assistant) -> None:
    titre(2, "Le modèle répond, sur cette machine")
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
    print(f"\n\n  {VERT}{jetons} jetons en {duree:.0f} s, processeur seul, sans réseau.{FIN}")
    time.sleep(POSE)


def acte_ussd(a: Assistant) -> None:
    titre(3, f"Le même modèle, joignable par USSD au {CODE_SERVICE}")
    saisies = ["", "3", "De combien de jours la commande CMD-1042 est-elle en retard ?"]
    texte = ""
    for i, saisie in enumerate(saisies):
        texte = saisie if not texte else f"{texte}*{saisie}"
        sortie = repondre("tournage", CODE_SERVICE, "+2250700000000", texte.lstrip("*"), a)
        _dessiner(sortie[4:])
        print(f"    {GRIS}{len(sortie)}/{ECRAN_MAX} caractères{FIN}")
        time.sleep(POSE if i < len(saisies) - 1 else 0.3)
    print(f"\n  {VERT}Aucun forfait data, aucune application, n'importe quel téléphone.{FIN}")
    time.sleep(POSE)


def acte_localite() -> None:
    titre(4, "Rien n'est sorti de la machine")
    cmd = charger_commandes()
    print(f"  Les documents lus sont ici : {GRAS}demo/commandes.json{FIN} "
          f"({len(cmd)} commandes, sur ce disque)\n")
    bruts = sorted((RACINE / "bench" / "raw").glob("final-iq4xs-*.json"))
    debits, pics = [], []
    for f in bruts:
        d = json.loads(f.read_text())
        debits.append(d["throughput"]["tokens_per_second_generation"])
        pics.append(d["memory"]["peak_rss_mb"])
    med = lambda v: sorted(v)[len(v) // 2]
    print(f"  Profileur officiel, médiane de {len(bruts)} passages sur ce fichier :")
    print(f"    débit      {GRAS}{med(debits):.2f} jetons/s{FIN}")
    print(f"    pic mémoire {GRAS}{med(pics):.0f} Mo{FIN}  (plafond du concours : 7 000 Mo)")
    print(f"\n  {VERT}Un modèle qui tient dans un portable à 8 Go, et qui n'appelle personne.{FIN}\n")


def main() -> int:
    repetition = "--repetition" in sys.argv
    depart = time.monotonic()
    acte_hors_ligne(verifier=not repetition)
    print(f"  {GRIS}chargement des poids…{FIN}")
    a = Assistant()
    acte_modele(a)
    acte_ussd(a)
    acte_localite()
    print(f"{GRIS}  [prise complète : {time.monotonic() - depart:.0f} s]{FIN}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
