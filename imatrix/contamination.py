#!/usr/bin/env python3
"""Vérifie que le corpus de calibration ne contient rien des jeux qui le jugent.

Le risque, et il est sérieux. Une matrice d'importance calibrée sur un texte
protège les poids qu'active ce texte. Si le corpus contenait les énoncés des
épreuves — les deux prompts publiés dans `metadata.json`, les quinze tâches de
`bench/redaction.py` — la recalibration améliorerait ses propres notes sans
améliorer le modèle, et la mesure qui suit ne vaudrait rien. C'est exactement la
faute que le règlement cherche à détecter avec ses deux prompts cachés.

Un corpus fabriqué ne met pas à l'abri : ses gabarits ont été écrits par la même
main que les épreuves, dans le même registre, avec les mêmes villes. La
disjonction se vérifie, elle ne se suppose pas.

Méthode : on compare des n-grammes de mots normalisés. Huit mots consécutifs
identiques ne se produisent pas par hasard entre deux textes indépendants — même
registre, même vocabulaire. Le script imprime aussi la plus longue séquence
commune, parce qu'un compte de zéro collision à n=8 ne dit pas si on est passé
loin ou à un mot près.

Usage : python imatrix/contamination.py [imatrix/corpus.txt]
Sortie : 0 si le corpus est disjoint, 1 s'il faut le corriger.
"""
from __future__ import annotations

import ast
import json
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
N = 8            # longueur d'un n-gramme, en mots
SEUIL_ALERTE = 6  # au-delà, on affiche la séquence même si elle est tolérée

_NON_MOT = re.compile(r"[^\w\s]", re.UNICODE)
_ESPACES = re.compile(r"\s+")


def mots(texte: str) -> list[str]:
    """Minuscules, ponctuation retirée, espaces normalisés."""
    return _ESPACES.sub(" ", _NON_MOT.sub(" ", texte.lower())).split()


def grammes(suite: list[str], n: int) -> set[str]:
    if len(suite) < n:
        return set()
    return {" ".join(suite[i:i + n]) for i in range(len(suite) - n + 1)}


def epreuves() -> list[tuple[str, str]]:
    """Tous les textes qui serviront à juger la recalibration."""
    sources: list[tuple[str, str]] = []

    meta = json.loads((RACINE / "metadata.json").read_text())
    for p in meta["test_prompts"]:
        sources.append((f"metadata.json/{p['prompt_id']}", p["prompt"]))

    # `redaction.py` est lu, pas exécuté : il importe un module voisin et son
    # exécution ferait tourner le modèle. On extrait la liste `EPREUVES` de
    # l'arbre syntaxique, où les littéraux concaténés sont déjà fusionnés.
    arbre = ast.parse((RACINE / "bench" / "redaction.py").read_text())
    for noeud in arbre.body:
        cible = getattr(noeud, "target", None) or (getattr(noeud, "targets", [None])[0])
        if isinstance(cible, ast.Name) and cible.id == "EPREUVES":
            for ep in ast.literal_eval(noeud.value):
                sources.append((f"redaction.py/{ep['nom']}", ep["prompt"]))
            break
    else:
        raise SystemExit("EPREUVES introuvable dans bench/redaction.py")

    return sources


def plus_longue_commune(a: list[str], b: list[str], plafond: int = 40) -> tuple[int, str]:
    """Longueur de la plus longue suite de mots commune, et cette suite.

    Recherche par n croissant : on s'arrête dès qu'un n ne donne plus rien, ce
    qui évite la table quadratique sur un corpus de trente mille mots.
    """
    meilleure = (0, "")
    ensemble_b = None
    for n in range(1, plafond + 1):
        ensemble_b = grammes(b, n)
        if not ensemble_b:
            break
        commun = grammes(a, n) & ensemble_b
        if not commun:
            break
        meilleure = (n, sorted(commun)[0])
    return meilleure


def main() -> int:
    chemin = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else RACINE / "imatrix" / "corpus.txt")
    corpus = mots(chemin.read_text())
    corpus_grammes = grammes(corpus, N)

    print(f"corpus   : {chemin.name}, {len(corpus):,} mots, "
          f"{len(corpus_grammes):,} {N}-grammes distincts")

    sources = epreuves()
    print(f"épreuves : {len(sources)} énoncés "
          f"({sum(1 for n, _ in sources if n.startswith('metadata'))} publiés, "
          f"{sum(1 for n, _ in sources if n.startswith('redaction'))} de contrôle)\n")

    collisions = 0
    record = (0, "", "")
    for nom, texte in sources:
        suite = mots(texte)
        communs = grammes(suite, N) & corpus_grammes
        longueur, sequence = plus_longue_commune(suite, corpus)
        if longueur > record[0]:
            record = (longueur, sequence, nom)
        marque = "✗" if communs else ("·" if longueur < SEUIL_ALERTE else "!")
        detail = ""
        if communs:
            detail = f"  ← {len(communs)} collision(s) : « {sorted(communs)[0]} »"
            collisions += len(communs)
        elif longueur >= SEUIL_ALERTE:
            detail = f"  ← {longueur} mots communs : « {sequence} »"
        print(f"  {marque} {nom:<28} max {longueur:>2} mots{detail}")

    print(f"\nplus longue séquence commune, tous énoncés confondus : "
          f"{record[0]} mots ({record[2]})")
    if record[0]:
        print(f"  « {record[1]} »")

    if collisions:
        print(f"\n✗ {collisions} n-gramme(s) de {N} mots partagés entre le corpus "
              f"et les épreuves.\n  Le corpus doit être corrigé : une matrice "
              f"calibrée dessus s'auto-noterait.")
        return 1

    print(f"\n✓ aucun {N}-gramme partagé. Le corpus de calibration et les jeux "
          f"d'évaluation\n  sont disjoints : ce qui sera mesuré après "
          f"recalibration est un effet réel.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
