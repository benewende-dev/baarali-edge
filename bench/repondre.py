#!/usr/bin/env python3
"""Fait répondre chaque candidat à nos deux prompts de test, et range les copies.

Pourquoi ce script existe : `arc_easy` mesure si un modèle sait **cocher la bonne
case**. La moitié « justesse » de la note est explicitement une combinaison de
références automatisées *et* de l'évaluation qualitative des réponses par le
jury — or nos deux prompts demandent de calculer, de citer et de rédiger en
français. Un questionnaire à choix multiples n'en dit rien.

On passe par `llama-cpp-python` et `create_chat_completion` pour que le **gabarit
de conversation embarqué dans le GGUF** soit appliqué : interroger un modèle
d'instruction sans son gabarit donne une sortie qui ne ressemble pas à ce que le
jury verra.

Usage : python bench/repondre.py [label…]   (défaut : tous)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

from mesurer import CANDIDATS, POIDS, RACINE

COPIES = RACINE / "bench" / "copies"

# Borné, toujours — mais assez large. À 512 tokens, trois copies sur cinq
# étaient coupées avant la conclusion : on ne compare pas des réponses
# tronquées. 1024 couvre la plus longue réponse complète observée (~450) avec
# de la marge pour les modèles qui raisonnent avant d'écrire.
MAX_TOKENS = 1024

# Certains modèles réfléchissent à voix haute avant de répondre et épuisent leur
# budget en hésitations. Les condamner là-dessus serait les juger sur un réglage
# et non sur leurs capacités : on leur donne la consigne qui coupe ce mode,
# quand elle existe. SmolLM3 reconnaît `/no_think`.
SYSTEME: dict[str, str] = {
    "smollm3-3b": "/no_think",
}


def repondre(label: str, prompts: list[dict]) -> str:
    from llama_cpp import Llama

    poids = POIDS / label / CANDIDATS[label]["fichier"]
    if not poids.exists():
        return f"# {label}\n\n_poids absents — lancer d'abord `bench/mesurer.py {label}`_\n"

    # n_ctx modeste : c'est celui que le profileur officiel utilise (2048), donc
    # celui dans lequel le modèle sera jugé.
    llm = Llama(model_path=str(poids), n_ctx=2048, verbose=False)
    systeme = SYSTEME.get(label)
    entete = f"# {label} — {CANDIDATS[label]['params']}, {CANDIDATS[label]['licence']}"
    if systeme:
        entete += f"\n\n_consigne système : `{systeme}`_"
    morceaux = [entete + "\n"]
    for p in prompts:
        messages = ([{"role": "system", "content": systeme}] if systeme else []) + [
            {"role": "user", "content": p["prompt"]}
        ]
        debut = time.monotonic()
        out = llm.create_chat_completion(
            messages=messages,
            max_tokens=MAX_TOKENS,
            temperature=0.0,  # déterministe : deux lectures doivent donner la même copie
        )
        texte = (out["choices"][0]["message"].get("content") or "").strip()
        stop = out["choices"][0].get("finish_reason")
        # « length » veut dire coupé : la copie ne vaut alors rien pour juger la
        # rédaction, et il faut le voir d'un coup d'œil plutôt que de le déduire.
        alerte = "  ⚠️ **COUPÉ**" if stop == "length" else ""
        morceaux.append(
            f"\n## {p['prompt_id']} — {time.monotonic() - debut:.0f} s, arrêt : {stop}{alerte}\n\n"
            + (texte or "_(réponse vide — le modèle n'a rien produit)_")
            + "\n"
        )
    return "\n".join(morceaux)


def main() -> int:
    prompts = json.loads((RACINE / "metadata.json").read_text())["test_prompts"]
    labels = [a for a in sys.argv[1:] if a in CANDIDATS] or list(CANDIDATS)
    COPIES.mkdir(parents=True, exist_ok=True)
    for label in labels:
        print(f"=== {label} ===", flush=True)
        copie = COPIES / f"{label}.md"
        copie.write_text(repondre(label, prompts))
        print(f"  → {copie.relative_to(RACINE)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
