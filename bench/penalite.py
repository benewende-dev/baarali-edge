#!/usr/bin/env python3
"""Mesure ce que coûte et ce que rapporte une pénalité de répétition.

Pourquoi ce script existe. La sonde langues a fait apparaître une panne franche :
sur une entrée que le modèle ne sait pas traiter, il n'échoue pas, il **boucle** —
la même phrase répétée jusqu'à épuisement du budget de jetons. Ce n'est pas un
détail cosmétique :

  · le jury ajoute **2 prompts cachés** que nous ne verrons jamais avant l'audit ;
  · une boucle sur l'un d'eux, c'est une copie blanche sur un quart de l'épreuve
    qualitative ;
  · et la chaîne officielle ne protège de rien — relu dans le code du profileur,
    `accuracy.py` appelle `create_completion(temperature=0.0)` sans pénalité, et
    `llama-cpp-python` 0.3.34 a `repeat_penalty = 1.0` par défaut, c'est-à-dire
    **aucune pénalité**. Les boucles observées sont donc exactement ce que le
    jury verrait.

Le remède évident est une pénalité de répétition. Mais il n'est évident que tant
qu'on ne l'a pas mesuré : dans llama.cpp la pénalité s'applique aux
`repeat_last_n` derniers jetons **du contexte, prompt compris**. Or notre premier
prompt de test demande de **citer une clause de contrat mot pour mot**. Une
pénalité trop forte pénalise précisément les jetons qu'il faut recopier.

Ce script mesure donc les trois côtés de la balance sur la même échelle :
  1. la panne guérit-elle ? (prompts hors-domaine qui bouclaient)
  2. la citation survit-elle ? (nos deux prompts de test réels)
  3. **le fond tient-il ?** (un contrôle chiffré, vérifiable sans avis humain)

Le point 3 n'était pas prévu : il a été ajouté après un premier passage, parce
que celui-ci a montré une chose qu'on n'aurait pas devinée. À pénalité 1,10, la
boucle disparaît et l'indicateur de dégénérescence est excellent (0,99) —
pendant que la réponse au premier prompt de test passe de 270 000 FCFA (juste) à
63 450 FCFA (absurde). La pénalité ne casse pas la citation, elle **dévie le
raisonnement**. Un indicateur de forme ne peut donc pas décider seul.

Mesure de la dégénérescence : la proportion de quadrigrammes de mots distincts.
Un texte français sain tourne au-dessus de 0,90 ; une boucle tombe sous 0,10.
Ce n'est pas un jugement de qualité, c'est un détecteur de panne — et il se
calcule sans avis humain, donc il est reproductible.

Mesure du fond : six énoncés de gestion courants — TVA ivoirienne, remise,
plafond contractuel, provision, escompte, marge — dont la bonne réponse est **un
nombre**. On vérifie sa présence dans la copie. Six échantillons ne font pas une
référence, mais ils suffisent à distinguer une déviation isolée d'une déviation
systématique, ce qu'un seul prompt ne permettait pas.

Usage : .venv/bin/python bench/penalite.py [label]
"""
from __future__ import annotations

import json
import sys
import time

from mesurer import CANDIDATS, POIDS, RACINE

SORTIE = RACINE / "bench" / "copies" / "penalite-repetition.md"
LABEL_DEFAUT = "q2b-iq4xs"

# 1,0 = pas de pénalité, c'est le défaut de la chaîne officielle : c'est notre
# point de comparaison, pas une valeur candidate.
PENALITES = [1.0, 1.05, 1.10, 1.15, 1.20]

# Fenêtre sur laquelle la pénalité s'applique. Valeur par défaut de llama.cpp,
# gardée telle quelle : on fait varier une seule chose à la fois.
FENETRE = 64

SEUIL_PANNE = 0.30  # en dessous, la sortie est dégénérée, pas seulement répétitive

# Contrôle du fond. Des situations de gestion ordinaires du domaine déclaré —
# pas des variantes de nos prompts de test, sans quoi on ne mesurerait que du
# surapprentissage sur nos propres énoncés. Chaque réponse attendue est un
# nombre : sa présence dans la copie se vérifie sans jugement.
#
# Deux niveaux, parce que le premier passage a montré qu'ils ne disent pas la
# même chose : les énoncés à **une étape** sont réussis à toutes les pénalités
# et ne départagent donc rien. La déviation observée portait sur un
# enchaînement de calculs — c'est là qu'il faut regarder.
CONTROLE = [
    # — une étape —
    ("tva",
     "Une facture s'élève à 2 350 000 FCFA hors taxes. La TVA applicable en Côte "
     "d'Ivoire est de 18 %. Donne le montant toutes taxes comprises.",
     ["2773000"]),
    ("remise",
     "Un devis de 1 200 000 FCFA HT bénéficie d'une remise commerciale de 15 %. "
     "Quel est le montant HT après remise ?",
     ["1020000"]),
    ("plafond",
     "Le calcul brut d'une pénalité de retard donne 12 % du montant de la commande, "
     "mais le contrat plafonne les pénalités à 10 %. La commande vaut 8 000 000 FCFA HT. "
     "Quel montant de pénalité est réellement dû ?",
     ["800000"]),
    ("provision",
     "Une entreprise doit provisionner 3 % de sa masse salariale annuelle pour la "
     "formation. La masse salariale est de 96 000 000 FCFA. Quel montant provisionner ?",
     ["2880000"]),
    ("escompte",
     "An invoice of 48,000 USD carries payment terms of 2/10 net 30. The customer pays "
     "on day 8. What amount do they pay?",
     ["47040"]),
    ("marge",
     "A product costs 12,500 XOF to buy and sells for 20,000 XOF. What is the gross "
     "margin as a percentage of the selling price?",
     ["37.5", "375"]),  # « 37,5 % » perd sa virgule à la normalisation

    # — plusieurs étapes : c'est ce niveau qui départage —
    ("retard+plafond",
     "Un fournisseur devait livrer sous 20 jours. Il livre avec 16 jours de retard. "
     "Le contrat prévoit une pénalité de 1,5 % du montant hors taxes par semaine "
     "entamée, plafonnée à 8 %. La commande vaut 5 000 000 FCFA HT. Quel est le "
     "montant de la pénalité due ?",
     ["225000"]),           # 16 j → 3 semaines entamées → 4,5 % → plafond non atteint
    ("remise+tva",
     "Une facture de 3 200 000 FCFA HT bénéficie d'une remise de 10 %, puis la TVA "
     "de 18 % s'applique sur le montant remisé. Quel est le montant TTC à payer ?",
     ["3398400"]),
    ("projection",
     "A 90-day project has spent 62% of a 24,000,000 XOF budget after 45 days. If the "
     "daily spending rate stays the same, what will the total spend be on day 90?",
     ["29760000"]),
    ("coût employeur",
     "Un salarié perçoit 450 000 FCFA de salaire brut. Les cotisations salariales "
     "retenues sont de 6,3 %, et l'employeur verse en plus 18,45 % de charges "
     "patronales calculées sur le brut. Quel est le coût total pour l'employeur ?",
     ["533025"]),
    ("achat+remise+tva",
     "Une entreprise achète 3 imprimantes à 385 000 FCFA HT l'unité. Le fournisseur "
     "accorde 5 % de remise sur le total, puis la TVA de 18 % s'applique sur le "
     "montant remisé. Quel est le montant TTC ?",
     ["1294755"]),
    ("croissance",
     "Le chiffre d'affaires est passé de 145 000 000 FCFA à 182 000 000 FCFA. Quel "
     "est le taux de croissance en pourcentage, arrondi à une décimale ?",
     ["25.5", "255%"]),
    ("mensualités",
     "Une facture de 5 400 000 FCFA HT est réglée en 3 mensualités égales, TVA de "
     "18 % comprise. Quel est le montant de chaque mensualité TTC ?",
     ["2124000"]),
    ("masse salariale",
     "A company's monthly gross payroll is 18,500,000 XOF. Employer social "
     "contributions add 18.45% on top of the gross. What is the total annual "
     "employer payroll cost?",
     ["262959000"]),
    ("comparaison offres",
     "Deux fournisseurs sont en concurrence : A propose 12 000 FCFA l'unité avec 8 % "
     "de remise, B propose 11 500 FCFA l'unité sans remise. Pour une commande de 500 "
     "unités, quel est l'écart de prix total entre les deux offres ?",
     ["230000"]),
    ("pénalité partielle",
     "An order of 320 units at 7,250 XOF each is shipped in four batches. The first "
     "two batches, which together represent half the order, arrive late and incur a "
     "3% penalty on their value. What is the penalty amount?",
     ["34800"]),
    ("loyer indexé",
     "Le loyer annuel d'un bureau est de 9 600 000 FCFA. Quel sera-t-il après deux "
     "augmentations annuelles successives de 4 % ?",
     ["10383360"]),
    ("régie",
     "Une équipe facture 45 000 FCFA de l'heure, toutes personnes confondues. Un "
     "projet demande 3 semaines à 35 heures par semaine. Quel est le montant HT ?",
     ["4725000"]),
]

# Où s'arrête le niveau « une étape » dans la liste ci-dessus.
CHARNIERE = 6

# Séparateurs de milliers et espaceurs LaTeX : tout ce qui coupe un nombre sans
# le changer. La virgule décimale française disparaît aussi, d'où les deux
# formes acceptées pour « marge ».
_BRUIT = [" ", " ", " ", " ", "\\,", "\\;", "\\ ", ",", "_", "'"]


def normaliser(texte: str) -> str:
    for c in _BRUIT:
        texte = texte.replace(c, "")
    return texte


def diversite(texte: str, n: int = 4) -> float:
    """Proportion de quadrigrammes de mots distincts. 1,0 = aucune répétition."""
    mots = texte.split()
    if len(mots) < n + 1:
        return 1.0
    grammes = [tuple(mots[i : i + n]) for i in range(len(mots) - n + 1)]
    return len(set(grammes)) / len(grammes)


def epreuves() -> list[tuple[str, str, str, int, list[str] | None]]:
    """(famille, nom, prompt, budget de jetons, réponses acceptées)."""
    meta = json.loads((RACINE / "metadata.json").read_text())
    reels = [
        ("domaine", p["prompt_id"], p["prompt"], 1024, None)
        for p in meta["test_prompts"]
    ]
    controle = [
        ("1 étape" if i < CHARNIERE else "n étapes", nom, p, 700, att)
        for i, (nom, p, att) in enumerate(CONTROLE)
    ]
    # Les trois entrées qui ont bouclé à la sonde langues. On ne revendique plus
    # ces langues — on garde les prompts parce qu'ils sont le **déclencheur
    # reproductible** de la panne, et qu'un correctif se prouve sur ce qui casse.
    hors_domaine = [
        ("hors-domaine", "boucle-1",
         "Traduis en dioula (jula), et donne uniquement la traduction : "
         "« Votre commande est prête. Merci de passer la retirer au magasin. »",
         400, None),
        ("hors-domaine", "boucle-2",
         "Un commerçant d'Abidjan veut un message court en dioula pour prévenir "
         "ses clients que la boutique ouvre à 8 h. Écris ce message.",
         400, None),
        ("hors-domaine", "boucle-3",
         "Une boutique de Dakar veut un message court en wolof pour annoncer que "
         "la livraison est gratuite cette semaine. Écris ce message.",
         400, None),
    ]
    return reels + controle + hors_domaine


def main() -> int:
    from llama_cpp import Llama

    label = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in CANDIDATS else LABEL_DEFAUT
    poids = POIDS / label / CANDIDATS[label]["fichier"]
    if not poids.exists():
        print(f"poids absents : {poids}", file=sys.stderr)
        return 1

    llm = Llama(model_path=str(poids), n_ctx=2048, verbose=False)

    resultats: dict[tuple[str, float], dict] = {}
    ordre: list[tuple[str, str]] = []  # (famille, nom), dans l'ordre d'apparition
    for famille, nom, prompt, budget, attendu in epreuves():
        ordre.append((famille, nom))
        for pen in PENALITES:
            debut = time.monotonic()
            out = llm.create_chat_completion(
                messages=[{"role": "user", "content": prompt}],
                max_tokens=budget,
                temperature=0.0,  # déterministe : la pénalité est la seule variable
                repeat_penalty=pen,
            )
            choix = out["choices"][0]
            texte = (choix["message"].get("content") or "").strip()
            juste = None
            if attendu:
                brut = normaliser(texte)
                juste = any(a in brut for a in attendu)
            resultats[(nom, pen)] = {
                "famille": famille,
                "prompt": prompt,
                "attendu": attendu,
                "texte": texte,
                "div": diversite(texte),
                "juste": juste,
                "coupe": choix.get("finish_reason") == "length",
                "duree": time.monotonic() - debut,
            }
            marque = "" if juste is None else ("  ✓" if juste else "  ✗")
            print(
                f"{nom:10s} pen={pen:.2f}  div={resultats[(nom, pen)]['div']:.2f}"
                f"  {resultats[(nom, pen)]['duree']:.0f}s{marque}",
                flush=True,
            )

    entete_pen = " | ".join(f"pen {p:.2f}" for p in PENALITES)
    lignes = [
        f"# Pénalité de répétition — {label} ({CANDIDATS[label]['params']})\n",
        f"Fenêtre `repeat_last_n = {FENETRE}` (défaut llama.cpp), température nulle,",
        "gabarit de conversation du GGUF appliqué. **1,00 = le défaut de la chaîne",
        "officielle**, donc la colonne de référence.\n",
        "## Forme — proportion de quadrigrammes distincts\n",
        f"En gras sous **{SEUIL_PANNE:.2f}** : sortie dégénérée. `⚠` : coupée au budget.\n",
        f"| Épreuve | {entete_pen} |",
        "|---|" + "---|" * len(PENALITES),
    ]
    for famille, nom in ordre:
        cases = []
        for pen in PENALITES:
            r = resultats[(nom, pen)]
            gras = "**" if r["div"] < SEUIL_PANNE else ""
            cases.append(f"{gras}{r['div']:.2f}{gras}" + (" ⚠" if r["coupe"] else ""))
        lignes.append(f"| {nom} | " + " | ".join(cases) + " |")

    lignes += [
        "\n## Fond — la bonne valeur est-elle dans la copie ?\n",
        f"| Épreuve | Niveau | Attendu | {entete_pen} |",
        "|---|---|---|" + "---|" * len(PENALITES),
    ]
    scores = {niv: {p: 0 for p in PENALITES} for niv in ("1 étape", "n étapes")}
    effectif = {niv: 0 for niv in scores}
    for famille, nom in ordre:
        if famille not in scores:
            continue
        effectif[famille] += 1
        cases = []
        for pen in PENALITES:
            r = resultats[(nom, pen)]
            scores[famille][pen] += int(bool(r["juste"]))
            cases.append("✓" if r["juste"] else "✗")
        attendu = resultats[(nom, PENALITES[0])]["attendu"][0]
        lignes.append(f"| {nom} | {famille} | `{attendu}` | " + " | ".join(cases) + " |")
    for niv in scores:
        lignes.append(
            f"| **total {niv}** | | | "
            + " | ".join(f"**{scores[niv][p]}/{effectif[niv]}**" for p in PENALITES)
            + " |"
        )

    lignes.append("\n---\n\n## Copies intégrales\n")
    for famille, nom in ordre:
        lignes.append(
            f"\n### {nom} · {famille}\n\n> {resultats[(nom, PENALITES[0])]['prompt']}\n"
        )
        for pen in PENALITES:
            r = resultats[(nom, pen)]
            extrait = r["texte"]
            # Une boucle n'a pas besoin d'être lue en entier pour être vue.
            if r["div"] < SEUIL_PANNE and len(extrait) > 600:
                extrait = (
                    extrait[:600]
                    + f"\n\n_(…coupé ici : {len(r['texte'])} caractères de boucle)_"
                )
            verdict = "" if r["juste"] is None else (", **juste**" if r["juste"] else ", **faux**")
            lignes.append(
                f"\n#### pénalité {pen:.2f} — diversité {r['div']:.2f}, "
                f"{r['duree']:.0f} s{verdict}{', coupé' if r['coupe'] else ''}\n\n"
                + (extrait or "_(réponse vide)_")
                + "\n"
            )

    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text("\n".join(lignes))
    print(f"→ {SORTIE.relative_to(RACINE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
