#!/usr/bin/env python3
"""Sonde ce que le modèle retenu sait déjà faire en langues ouest-africaines.

Pourquoi cette sonde existe : `metadata.json` déclare des langues dans
`language_scope` et revendique le bonus « cas d'utilisation africain ». Une
revendication non tenue se voit à l'audit et coûte plus qu'elle ne rapporte.
Avant d'investir dans un affinage, il faut savoir ce que le socle sait **déjà**.

Deux langues, deux familles distinctes :
  · le **dioula** (jula, `dyu`) — continuum mandingue, parlé à Abidjan et dans
    tout le corridor Côte d'Ivoire / Mali / Burkina ;
  · le **wolof** (`wo`) — famille atlantique, Sénégal, Gambie, Mauritanie.
Les deux ensemble couvrent l'essentiel de l'Afrique de l'Ouest francophone,
et leur éloignement linguistique évite de conclure sur un seul cas.

On ne cherche pas une note : on cherche à distinguer trois comportements, qui
appellent trois décisions différentes — produire la langue, produire du
charabia, ou refuser honnêtement en français.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

from mesurer import CANDIDATS, POIDS, RACINE

SORTIE = RACINE / "bench" / "copies" / "sonde-langues.md"
MAX_TOKENS = 400
LABEL_DEFAUT = "q2b-iq4xs"

# Épreuves du plus simple (reconnaître) au plus exigeant (produire de l'utile).
EPREUVES = [
    ("dioula · reconnaissance",
     "De quelle langue s'agit-il, et que signifie cette phrase ? « I ni ce, i ka kene wa ? »"),
    ("dioula · français → dioula",
     "Traduis en dioula (jula), et donne uniquement la traduction : "
     "« Votre commande est prête. Merci de passer la retirer au magasin. »"),
    ("dioula · dioula → français",
     "Traduis en français : « N b'a fɛ ka feere kɛ bi. Wari bɛ n bolo. »"),
    ("dioula · usage métier",
     "Un commerçant d'Abidjan veut un message court en dioula pour prévenir ses "
     "clients que la boutique ouvre à 8 h. Écris ce message."),
    ("wolof · reconnaissance",
     "De quelle langue s'agit-il, et que signifie cette phrase ? « Na nga def, ana waa kër ga ? »"),
    ("wolof · français → wolof",
     "Traduis en wolof, et donne uniquement la traduction : "
     "« Votre commande est prête. Merci de passer la retirer au magasin. »"),
    ("wolof · wolof → français",
     "Traduis en français : « Damay dem marse bi tey ngoon. »"),
    ("wolof · usage métier",
     "Une boutique de Dakar veut un message court en wolof pour annoncer que "
     "la livraison est gratuite cette semaine. Écris ce message."),
    ("conscience de ses limites",
     "Réponds honnêtement en français, en deux phrases maximum : maîtrises-tu le "
     "dioula (jula) et le wolof ? Donne un niveau pour chacun."),
]


def main() -> int:
    from llama_cpp import Llama

    label = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in CANDIDATS else LABEL_DEFAUT
    poids = POIDS / label / CANDIDATS[label]["fichier"]
    if not poids.exists():
        print(f"poids absents : {poids}", file=sys.stderr)
        return 1

    llm = Llama(model_path=str(poids), n_ctx=2048, verbose=False)
    morceaux = [f"# Sonde langues ouest-africaines — {label} ({CANDIDATS[label]['params']})\n"]
    for nom, prompt in EPREUVES:
        debut = time.monotonic()
        out = llm.create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=MAX_TOKENS,
            temperature=0.0,
        )
        texte = (out["choices"][0]["message"].get("content") or "").strip()
        stop = out["choices"][0].get("finish_reason")
        alerte = "  ⚠️ **COUPÉ**" if stop == "length" else ""
        morceaux.append(
            f"\n## {nom} — {time.monotonic() - debut:.0f} s{alerte}\n\n"
            f"> {prompt}\n\n"
            + (texte or "_(réponse vide)_")
            + "\n"
        )
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text("\n".join(morceaux))
    print(f"→ {SORTIE.relative_to(RACINE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
