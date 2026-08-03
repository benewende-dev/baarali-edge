#!/usr/bin/env python3
"""Compare deux modèles question par question, et non par leurs totaux.

Pourquoi ce script existe. Deux scores globaux — 0,670 contre 0,680 sur deux
cents questions — se comparent mal : l'erreur-type d'un score de 0,67 sur deux
cents tirages vaut 3,3 points, si bien qu'un écart d'un point ne prouve rien.
Mais les deux modèles répondent aux **mêmes** questions, et se trompent surtout
aux mêmes endroits. Ce qui porte l'information, ce n'est donc pas la différence
des totaux : ce sont les seules questions où les deux **divergent**.

C'est le test de McNemar. Sur les questions où l'un a juste et l'autre faux, si
la calibration n'a aucun effet, chaque sens est également probable — un tirage à
pile ou face répété. On calcule la probabilité exacte, sous cette hypothèse,
d'observer un déséquilibre au moins aussi marqué que celui qu'on voit.

L'évaluation elle-même reprend l'adaptateur du profileur officiel, `_make_lm` :
mêmes log-vraisemblances, même tokenisation, mêmes questions dans le même ordre.
Seule chose ajoutée, la trace par question, que `run_benchmark` agrège et jette.

Usage : .venv/bin/python bench/apparie.py <label-a> <label-b> [--limite=200]
"""
from __future__ import annotations

import json
import math
import sys

from mesurer import CANDIDATS, POIDS, RACINE

SORTIE = RACINE / "bench" / "raw"


def reponses(label: str, limite: int, tache: str, graine: int = 42) -> list[bool]:
    """Juste/faux pour chaque question, dans l'ordre du jeu."""
    import lm_eval
    from adtc_profiler.accuracy import _make_lm

    poids = POIDS / label / CANDIDATS[label]["fichier"]
    if not poids.exists():
        raise SystemExit(f"poids absents : {poids}")

    res = lm_eval.simple_evaluate(
        model=_make_lm(poids),
        tasks=[tache],
        limit=limite,
        random_seed=graine,
        numpy_random_seed=graine,
        fewshot_random_seed=graine,
        log_samples=True,
    )
    echantillons = res["samples"][tache]
    # `acc_norm` est la métrique que retient le profileur : bonne réponse = celle
    # dont la log-vraisemblance est la plus haute une fois normalisée par la
    # longueur. On relit la décision de lm-eval plutôt que de la recalculer.
    return [bool(e["acc_norm"]) for e in echantillons]


def mcnemar(a: list[bool], b: list[bool]) -> dict:
    """Probabilité exacte du déséquilibre observé, sous l'hypothèse nulle."""
    a_seul = sum(1 for x, y in zip(a, b) if x and not y)
    b_seul = sum(1 for x, y in zip(a, b) if y and not x)
    n = a_seul + b_seul
    k = min(a_seul, b_seul)
    # Test binomial bilatéral : P(au moins ce déséquilibre | pile ou face).
    p = 1.0 if n == 0 else min(
        1.0, 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n)
    return {"a_seul": a_seul, "b_seul": b_seul, "discordantes": n, "p": p}


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    limite = int(next((a.split("=")[1] for a in sys.argv[1:]
                       if a.startswith("--limite=")), 200))
    tache = next((a.split("=")[1] for a in sys.argv[1:]
                  if a.startswith("--tache=")), "arc_easy")
    if len(args) != 2:
        print(f"candidats : {', '.join(CANDIDATS)}", file=sys.stderr)
        return 1
    la, lb = args

    print(f"{tache}, {limite} questions, mêmes questions dans le même ordre\n")
    ra = reponses(la, limite, tache)
    rb = reponses(lb, limite, tache)
    if len(ra) != len(rb):
        raise SystemExit(f"jeux différents : {len(ra)} contre {len(rb)} questions")

    m = mcnemar(ra, rb)
    n = len(ra)
    print(f"  {la:<24} {sum(ra):>3}/{n}  ({sum(ra)/n:.3f})")
    print(f"  {lb:<24} {sum(rb):>3}/{n}  ({sum(rb)/n:.3f})")
    print(f"\n  identiques   {n - m['discordantes']:>3}/{n}  "
          f"({(n - m['discordantes'])/n:.0%} — les deux modèles sont d'accord)")
    print(f"  {la} seul juste : {m['a_seul']}")
    print(f"  {lb} seul juste : {m['b_seul']}")
    print(f"\n  p = {m['p']:.3f}", end="  ")
    if m["p"] < 0.05:
        print("→ l'écart ne s'explique pas par le hasard.")
    else:
        print("→ compatible avec le hasard : rien n'est démontré.")

    (SORTIE / f"apparie-{la}-vs-{lb}.json").write_text(json.dumps(
        {"tache": tache, "questions": n, la: sum(ra), lb: sum(rb), **m,
         "detail_a": ra, "detail_b": rb}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
