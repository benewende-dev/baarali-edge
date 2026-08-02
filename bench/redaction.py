#!/usr/bin/env python3
"""Mesure le modèle sur ce que le jury va réellement lui demander.

Pourquoi ce script existe, et pourquoi il arrive tard. Le contrôle de
`penalite.py` juge dix-huit énoncés dont la bonne réponse est **un nombre** :
TVA, remises, pénalités, provisions. Il est solide, il est reproductible — et il
mesure la mauvaise chose. La définition officielle de notre domaine, relevée sur
la page du concours, tient en une ligne :

    corporate_enterprise — knowledge-work productivity: **summarization,
    drafting, and analysis** for small and medium enterprises.

Résumer. Rédiger. Analyser. Pas calculer. Et la justesse est « la moyenne
pondérée de la réponse du modèle, notée de 0 à 100 par un juge » : les deux
prompts cachés seront de ce genre-là, pas des exercices d'arithmétique.

On avait donc un thermomètre très soigné pour une fièvre qui n'est pas celle
qu'on nous prendra. Ce fichier construit l'autre.

## Comment on note sans avis humain

« La qualité d'un résumé » n'est pas un nombre — mais elle se décompose en
vérifications qui, elles, en sont. Chaque épreuve porte ses propres critères :

  · `contient`   les faits du document source qui doivent survivre au résumé
                 (un groupe = une variante orthographique acceptée) ;
  · `absent`     ce que la consigne interdit (une première relance courtoise ne
                 menace pas d'huissier) ;
  · `parmi`      au moins *k* éléments d'une liste — pour les analyses, où
                 plusieurs réponses sont également valables ;
  · `ordre`      un élément cité avant un autre — pour les priorisations ;
  · `puces`      le nombre de puces demandé, exactement ;
  · `max_mots`   / `max_lignes` : la consigne de longueur est-elle tenue ;
  · `langue`     la réponse est-elle dans la langue de la question ;
  · `sans_invention` aucun nombre d'au moins trois chiffres qui ne soit pas dans
                 la source. C'est le contrôle d'hallucination, et le plus
                 sévère : un résumé qui invente un montant est pire qu'un résumé
                 vide, parce qu'on le croit.

Le score d'une épreuve est la part de ses critères tenus. Rien n'est jugé « à
l'œil » — le tableau se refait à l'identique.

## Ce que le corpus couvre, et pourquoi si large

Le règlement génère deux prompts cachés dans notre domaine **pour détecter le
surapprentissage**. La parade n'est donc pas de deviner, c'est d'être large.
Quinze épreuves : cinq par genre, français et anglais, huit villes d'Afrique de
l'Ouest et du Centre plus des énoncés sans lieu, et des types d'écrits
délibérément différents — compte rendu de chantier, note RH, fil de courriels,
rapport sanitaire, relance de paiement, annonce d'emploi, note de service,
réponse à réclamation, avenant, devis, extrait de contrat, tableau de bord,
proposition d'achat, arbitrage de priorités. Un contrôle collé à une seule ville
ou à un seul secteur mesurerait exactement le défaut qu'on cherche à éviter.

## Ce qui est mesuré en même temps

La pénalité de répétition avait été arrêtée à 1,10 sur le contrôle arithmétique.
Cette décision avait donc été prise avec le mauvais thermomètre. Remise à
l'épreuve ici contre 1,00 — le défaut de la chaîne officielle — et contre 1,05,
elle est tombée : les trois valeurs sont indiscernables sur les quinze épreuves
(91 / 90 / 91 %), mais 1,10 rend **fausse** la réponse à `tp_001`, notre propre
prompt déclaré. Décision révisée : **1,05**. Le détail est dans
`bench/resultats.md`, étape 5.

Usage : .venv/bin/python bench/redaction.py [label]
"""
from __future__ import annotations

import json
import re
import sys
import time
import unicodedata

from mesurer import CANDIDATS, POIDS, RACINE

SORTIE = RACINE / "bench" / "copies" / "redaction.md"
LABEL_DEFAUT = "q2b-iq4xs"

# 1,00 = le défaut de la chaîne officielle. 1,10 = la décision de l'étape 3,
# prise sur le contrôle arithmétique. 1,05 s'est invitée en cours de route : elle
# est la seule à garder `tp_001` juste *et* à soigner la dégénérescence observée
# sur `manques-decision`. Les trois sont donc mises au même tableau.
PENALITES = [1.00, 1.05, 1.10]

SEUIL_PANNE = 0.30  # sous ce seuil de diversité, la sortie est dégénérée

# Nombres légitimes partout : millésimes courants et les pourcentages ronds que
# n'importe quelle rédaction peut produire sans rien inventer.
CHIFFRES_LIBRES = ["2025", "2026", "2027", "100"]

# ————————————————————————————————————————————————————————————————————————
# Les épreuves
# ————————————————————————————————————————————————————————————————————————

EPREUVES: list[dict] = [
    # ————————————————————————— résumer —————————————————————————
    {
        "nom": "cr-chantier",
        "genre": "résumer",
        "cadre": "BTP · Ouagadougou · fr",
        "budget": 512,
        "prompt":
            "Résume le compte rendu suivant pour la direction, en exactement 3 puces.\n\n"
            "Compte rendu — réunion de chantier du 12 mars, site de Ouaga 2000. Le gros "
            "œuvre est achevé à 78 %. La livraison de ciment a pris 9 jours de retard, le "
            "fournisseur invoque une rupture de stock à Lomé. Le budget consommé s'élève à "
            "41 500 000 FCFA sur 60 000 000 FCFA prévus. Le client demande d'avancer la "
            "réception au 30 juin.",
        "criteres": {
            "contient": [["78"], ["9 jours", "neuf jours"], ["41500000", "41.500.000"],
                         ["30 juin", "juin"]],
            "puces": 3,
            "langue": "fr",
            "sans_invention": True,
        },
    },
    {
        "nom": "point-flotte",
        "genre": "résumer",
        "cadre": "logistique · sans lieu · en",
        "budget": 512,
        "prompt":
            "Summarise the following operations update for the board in no more than 80 "
            "words. Plain prose, no bullet points.\n\n"
            "Update: the fleet stands at 14 vehicles, of which 3 are off the road awaiting "
            "parts. On-time delivery fell to 86% this quarter, from 92% in the previous "
            "one. Fuel costs rose 17% after the subsidy was withdrawn. The new depot is "
            "scheduled to open in October.",
        "criteres": {
            "contient": [["14 vehicles", "14 "], ["86"], ["17"], ["october"]],
            "max_mots": 130,
            "langue": "en",
            "sans_invention": True,
        },
    },
    {
        "nom": "note-conges",
        "genre": "résumer",
        "cadre": "RH · Dakar · fr",
        "budget": 512,
        "prompt":
            "Résume la note de service suivante en deux phrases, pour affichage sur le "
            "tableau du personnel.\n\n"
            "Note de service n° 2026-11 — Direction des ressources humaines, Dakar. À "
            "compter du 1er septembre, toute demande de congé doit être déposée au moins "
            "15 jours à l'avance au moyen du formulaire RH-04. Le chef de service dispose "
            "de 5 jours ouvrés pour valider ou refuser la demande. Les demandes transmises "
            "par courriel ne seront plus acceptées.",
        "criteres": {
            "contient": [["15 jours", "quinze jours"], ["rh-04"], ["septembre"]],
            "max_mots": 90,
            "langue": "fr",
            "sans_invention": True,
        },
    },
    {
        "nom": "fil-client",
        "genre": "résumer",
        "cadre": "commerce · Accra · en",
        "budget": 512,
        "prompt":
            "Three messages from a client thread are below. In two sentences, state what "
            "was agreed and what we must do next.\n\n"
            "[1] Client: \"Our order GH-2291 for 400 units was due on 12 May. Where is "
            "it?\"\n"
            "[2] Us: \"We can ship 250 units this week; the remaining 150 depend on a "
            "supplier delivery.\"\n"
            "[3] Client: \"Send the 250 now, and confirm a firm date for the rest by "
            "Friday.\"",
        "criteres": {
            "contient": [["gh-2291"], ["250"], ["friday"]],
            "max_mots": 90,
            "langue": "en",
            "sans_invention": True,
        },
    },
    {
        "nom": "rapport-sante",
        "genre": "résumer",
        "cadre": "santé · Cotonou · fr",
        "budget": 512,
        "prompt":
            "Résume ce rapport mensuel en exactement 3 puces, pour le comité de gestion.\n\n"
            "Rapport d'activité — centre de santé, Cotonou, mois de mai. 1 240 "
            "consultations ont été enregistrées, soit une hausse de 8 % sur un mois. Trois "
            "ruptures de stock de médicaments essentiels ont été constatées. Le taux "
            "d'occupation des lits s'établit à 71 %. Le groupe électrogène est en panne "
            "depuis le 4 mai.",
        "criteres": {
            "contient": [["1240", "1.240"], ["71"], ["rupture"], ["electrogene", "panne"]],
            "puces": 3,
            "langue": "fr",
            "sans_invention": True,
        },
    },

    # ————————————————————————— rédiger —————————————————————————
    {
        "nom": "relance",
        "genre": "rédiger",
        "cadre": "recouvrement · Abidjan · fr",
        "budget": 512,
        "prompt":
            "Rédige une première relance de paiement, courtoise, adressée à la Pharmacie "
            "Riviera à Abidjan. Facture F-2026-118 d'un montant de 2 350 000 FCFA, échue "
            "depuis 22 jours. Demande un règlement sous huit jours et propose un rendez-vous "
            "téléphonique si un échéancier est nécessaire. Maximum 120 mots.",
        "criteres": {
            "contient": [["f-2026-118"], ["2350000", "2.350.000"], ["22"], ["echeancier"]],
            # Une *première* relance courtoise ne menace pas. Ces mots-là sont le
            # signe que le modèle a suivi le contenu et perdu le registre.
            "absent": ["huissier", "avocat", "poursuite", "contentieux", "mise en demeure"],
            "max_mots": 180,
            "langue": "fr",
            "sans_invention": True,
        },
    },
    {
        "nom": "annonce-poste",
        "genre": "rédiger",
        "cadre": "RH · Bamako · en",
        "budget": 512,
        "prompt":
            "Draft a short job advertisement, at most 8 lines, for a logistics coordinator "
            "based in Bamako. Requirements: at least 3 years of experience in freight or "
            "distribution, working French and English, a driving licence. The contract runs "
            "for 12 months, renewable. Applications close on 30 September.",
        "criteres": {
            "contient": [["bamako"], ["3 years", "three years"], ["12 month"],
                         ["french"], ["30 september", "september"]],
            "max_lignes": 12,
            "langue": "en",
            "sans_invention": True,
        },
    },
    {
        "nom": "note-coupure",
        "genre": "rédiger",
        "cadre": "informatique · Lomé · fr",
        "budget": 512,
        "prompt":
            "Rédige une note de service annonçant au personnel une interruption du système "
            "informatique le samedi 14, de 8 h à 14 h, pour la sauvegarde annuelle. Indique "
            "que le service support reste joignable au poste 214. Maximum 100 mots.",
        "criteres": {
            "contient": [["samedi 14", "le 14"], ["8 h", "8h", "huit heures"], ["214"],
                         ["sauvegarde"]],
            "max_mots": 150,
            "langue": "fr",
            "sans_invention": True,
        },
    },
    {
        "nom": "reponse-reclamation",
        "genre": "rédiger",
        "cadre": "service client · sans lieu · en",
        "budget": 512,
        "prompt":
            "Draft a reply to a customer who complains that their order arrived 6 days "
            "late. The cause was a customs hold on the shipment, which we could not "
            "control. Offer a 5% credit on their next order. Apologise once, at the "
            "beginning, and do not repeat the apology. Maximum 120 words.",
        "criteres": {
            "contient": [["6 days", "six days"], ["customs"], ["5%", "5 %"]],
            "max_mots": 180,
            "langue": "en",
            "sans_invention": True,
        },
    },
    {
        "nom": "avenant",
        "genre": "rédiger",
        "cadre": "juridique · Douala · fr",
        "budget": 512,
        "prompt":
            "Rédige l'article unique d'un avenant prolongeant le contrat de prestation "
            "n° C-2025-07 de six mois, soit du 1er juillet au 31 décembre 2026, à conditions "
            "financières inchangées. Style juridique sobre, un seul paragraphe, pas de "
            "commentaire.",
        "criteres": {
            "contient": [["c-2025-07"], ["31 decembre"], ["1er juillet"],
                         ["inchang", "sans modification", "identique", "demeurent"]],
            "max_mots": 160,
            "langue": "fr",
            "sans_invention": True,
        },
    },

    # ————————————————————————— analyser —————————————————————————
    {
        "nom": "manques-devis",
        "genre": "analyser",
        "cadre": "achats · sans lieu · fr",
        "budget": 700,
        "prompt":
            "Voici un devis reçu d'un prestataire. Indique les informations qui manquent "
            "pour qu'un acheteur puisse le comparer et le signer.\n\n"
            "Devis n° 88 — Kando Services. Objet : maintenance du parc informatique. "
            "Montant : 1 500 000 FCFA. Signature du gérant.",
        "criteres": {
            "parmi": ([
                "delai", "duree", "planning", "calendrier", "validite", "tva", "taxe",
                "hors taxe", "ht", "ttc", "paiement", "reglement", "perimetre", "detail",
                "date", "garantie", "nombre", "penalite", "reference",
            ], 4),
            "langue": "fr",
        },
    },
    {
        "nom": "risques-contrat",
        "genre": "analyser",
        "cadre": "juridique · sans lieu · en",
        "budget": 700,
        "prompt":
            "You advise a 30-person company. Read this contract excerpt and name the three "
            "clauses that carry the most risk for us, and say why in one line each.\n\n"
            "Excerpt: \"(4) The Customer's liability under this agreement is unlimited. "
            "(7) The Supplier may revise prices at any time upon written notice. "
            "(9) Invoices issued by the Supplier are payable 90 days from receipt. "
            "(12) This agreement renews automatically for successive 12-month terms unless "
            "terminated 6 months before expiry.\"",
        "criteres": {
            "parmi": ([
                "liabilit", "unlimited", "price", "revis", "90 day", "payment",
                "renew", "automatic", "terminat", "notice", "lock",
            ], 4),
            "langue": "en",
        },
    },
    {
        "nom": "incoherence",
        "genre": "analyser",
        "cadre": "gestion · sans lieu · fr",
        "budget": 700,
        "prompt":
            "Ce tableau de bord contient une incohérence. Trouve-la et donne le chiffre "
            "correct.\n\n"
            "Tableau de bord — mois de juin. Chiffre d'affaires : 45 000 000 FCFA. Taux de "
            "marge annoncé : 30 %. Marge brute annoncée : 18 000 000 FCFA. Charges fixes : "
            "9 000 000 FCFA.",
        # Deux raisonnements sont également justes : soit la marge devrait valoir
        # 13 500 000 FCFA au taux annoncé, soit le taux réel est de 40 %.
        "criteres": {
            "contient": [["13500000", "13.500.000", "13,5", "40 %", "40%"]],
            "langue": "fr",
        },
        "chiffres_extra": ["13500000", "135", "40", "1350"],
    },
    {
        "nom": "manques-decision",
        "genre": "analyser",
        "cadre": "achats · sans lieu · en",
        "budget": 700,
        "prompt":
            "An operations manager sends the note below. List what the note does not tell "
            "you but that you would need before approving it.\n\n"
            "Note: \"I propose we consolidate our 5 stationery and cleaning suppliers into "
            "a single one. The quotes I collected show an 8% saving on our current annual "
            "spend of 24,000,000 XOF. I recommend we sign this month.\"",
        "criteres": {
            "parmi": ([
                "risk", "depend", "single point", "lead time", "delivery", "quality",
                "exit", "terminat", "contract", "reference", "transition", "which supplier",
                "who", "service level", "price increase", "lock", "negotiat",
                # Familles de manques tout aussi valables, relevées par le modèle
                # lui-même au premier passage — les exclure aurait noté ma
                # réponse, pas la sienne.
                "scope", "what is included", "breakdown", "validity", "valid for",
                "baseline", "current cost", "per supplier", "individual",
            ], 4),
            "langue": "en",
        },
    },
    {
        "nom": "priorisation",
        "genre": "analyser",
        "cadre": "direction · Ouagadougou · fr",
        "budget": 700,
        "prompt":
            "Tu assistes le gérant d'une PME de 25 personnes à Ouagadougou. Classe les "
            "quatre actions suivantes de la plus urgente à la moins urgente, avec une "
            "justification d'une ligne chacune.\n\n"
            "a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités "
            "de retard.\n"
            "b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.\n"
            "c) Recruter un stagiaire pour la rentrée de septembre.\n"
            "d) Répondre à un appel d'offres public qui ferme dans 3 jours.\n",
        # Une échéance à 3 jours et une facture qui court passent avant un
        # recrutement de rentrée : c'est l'ordre, pas le classement exact, qui se
        # vérifie sans avis humain.
        "criteres": {
            "ordre": [("appel d'offres", "stagiaire"), ("facture", "stagiaire")],
            "parmi": (["3 jours", "penalite", "40 jours", "expire"], 2),
            "langue": "fr",
        },
    },
]

# ————————————————————————————————————————————————————————————————————————
# Vues normalisées du texte
# ————————————————————————————————————————————————————————————————————————

# Séparateurs de milliers et espaceurs LaTeX : tout ce qui coupe un nombre sans
# le changer.
_BRUIT_NOMBRE = [" ", " ", " ", " ", "\\,", "\\;", "\\ ", ",", "_", "'", "’"]


def vue_nombre(texte: str) -> str:
    """Texte débarrassé de tout ce qui coupe un nombre : « 2 350 000 » → « 2350000 »."""
    for c in _BRUIT_NOMBRE:
        texte = texte.replace(c, "")
    return texte


def vue_mot(texte: str) -> str:
    """Minuscules, accents retirés, apostrophes uniformisées.

    Les accents partent des deux côtés de la comparaison : « délai » et « delai »
    doivent compter pareil, sans quoi on noterait l'orthographe du modèle plutôt
    que sa compréhension.
    """
    texte = texte.replace("’", "'").replace(" ", " ").replace(" ", " ")
    decompose = unicodedata.normalize("NFD", texte.lower())
    return "".join(c for c in decompose if unicodedata.category(c) != "Mn")


_EST_NOMBRE = re.compile(r"^[\d.,\s%]+$")


def present(attendu: str, nombres: str, mots: str) -> bool:
    """Cherche `attendu` dans la vue qui convient à sa nature."""
    if _EST_NOMBRE.match(attendu):
        return vue_nombre(attendu) in nombres
    return vue_mot(attendu) in mots


def diversite(texte: str, n: int = 4) -> float:
    """Proportion de quadrigrammes de mots distincts. 1,0 = aucune répétition."""
    m = texte.split()
    if len(m) < n + 1:
        return 1.0
    g = [tuple(m[i : i + n]) for i in range(len(m) - n + 1)]
    return len(set(g)) / len(g)


_PUCE = re.compile(r"^\s*(?:[-*•–—]|\d+[.)])\s+")


def compter_puces(texte: str) -> int:
    return sum(1 for l in texte.split("\n") if _PUCE.match(l))


_MARQUEURS = {
    "fr": ["le", "la", "les", "des", "une", "est", "pour", "dans", "avec", "sur",
           "que", "qui", "aux", "du", "vous", "nous", "par", "ce", "cette"],
    "en": ["the", "and", "is", "are", "for", "with", "that", "this", "of", "to",
           "we", "you", "our", "your", "will", "from", "as", "in"],
}


def langue_dominante(mots: str) -> str:
    jetons = re.findall(r"[a-z]+", mots)
    if not jetons:
        return "?"
    poids = {
        code: sum(1 for j in jetons if j in liste) for code, liste in _MARQUEURS.items()
    }
    return max(poids, key=poids.get) if any(poids.values()) else "?"


_RUN = re.compile(r"\d{3,}")


def inventions(texte: str, autorise: str) -> list[str]:
    """Nombres d'au moins trois chiffres présents dans la copie, absents de la source.

    Trois chiffres, pas moins : « 3 points », « 2 phrases », « article 4 » sont du
    langage ordinaire et n'ont rien à voir avec une hallucination. Ce sont les
    montants, les références et les quantités qu'on surveille.
    """
    permis = vue_nombre(autorise)
    return sorted({n for n in _RUN.findall(vue_nombre(texte)) if n not in permis})


# ————————————————————————————————————————————————————————————————————————
# Notation
# ————————————————————————————————————————————————————————————————————————


def noter(ep: dict, texte: str) -> tuple[list[tuple[str, bool]], list[str]]:
    """Rend la liste (libellé du critère, tenu ?) et les nombres inventés."""
    nombres, mots = vue_nombre(texte), vue_mot(texte)
    c = ep["criteres"]
    detail: list[tuple[str, bool]] = []

    for groupe in c.get("contient", []):
        detail.append((
            "fait : " + " / ".join(groupe),
            any(present(a, nombres, mots) for a in groupe),
        ))

    if "absent" in c:
        trouves = [m for m in c["absent"] if vue_mot(m) in mots]
        detail.append(("registre : aucune menace" + (f" (vu : {', '.join(trouves)})" if trouves else ""),
                       not trouves))

    if "parmi" in c:
        liste, k = c["parmi"]
        vus = [m for m in liste if vue_mot(m) in mots]
        detail.append((f"≥{k} points parmi la liste ({len(vus)} vus : {', '.join(vus[:6]) or '—'})",
                       len(vus) >= k))

    for avant, apres in c.get("ordre", []):
        ia, ib = mots.find(vue_mot(avant)), mots.find(vue_mot(apres))
        detail.append((f"« {avant} » avant « {apres} »", ia != -1 and (ib == -1 or ia < ib)))

    if "puces" in c:
        n = compter_puces(texte)
        detail.append((f"exactement {c['puces']} puces (vu : {n})", n == c["puces"]))

    if "max_mots" in c:
        n = len(texte.split())
        detail.append((f"≤ {c['max_mots']} mots (vu : {n})", n <= c["max_mots"]))

    if "max_lignes" in c:
        n = sum(1 for l in texte.split("\n") if l.strip())
        detail.append((f"≤ {c['max_lignes']} lignes (vu : {n})", n <= c["max_lignes"]))

    if "langue" in c:
        vue = langue_dominante(mots)
        detail.append((f"répond en {c['langue']} (vu : {vue})", vue == c["langue"]))

    inventes: list[str] = []
    if c.get("sans_invention"):
        autorise = ep["prompt"] + " " + " ".join(
            CHIFFRES_LIBRES + ep.get("chiffres_extra", [])
        )
        inventes = inventions(texte, autorise)
        detail.append((
            "aucun nombre inventé" + (f" (vu : {', '.join(inventes)})" if inventes else ""),
            not inventes,
        ))

    return detail, inventes


def main() -> int:
    from llama_cpp import Llama

    label = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in CANDIDATS else LABEL_DEFAUT
    poids = POIDS / label / CANDIDATS[label]["fichier"]
    if not poids.exists():
        print(f"poids absents : {poids}", file=sys.stderr)
        return 1

    llm = Llama(model_path=str(poids), n_ctx=2048, verbose=False)

    res: dict[tuple[str, float], dict] = {}
    for ep in EPREUVES:
        for pen in PENALITES:
            debut = time.monotonic()
            out = llm.create_chat_completion(
                messages=[{"role": "user", "content": ep["prompt"]}],
                max_tokens=ep["budget"],
                temperature=0.0,  # déterministe : la pénalité est la seule variable
                repeat_penalty=pen,
            )
            choix = out["choices"][0]
            texte = (choix["message"].get("content") or "").strip()
            detail, inventes = noter(ep, texte)
            tenus = sum(1 for _, ok in detail if ok)
            res[(ep["nom"], pen)] = {
                "texte": texte,
                "detail": detail,
                "tenus": tenus,
                "total": len(detail),
                "score": tenus / len(detail) if detail else 0.0,
                "div": diversite(texte),
                "inventes": inventes,
                "coupe": choix.get("finish_reason") == "length",
                "duree": time.monotonic() - debut,
            }
            r = res[(ep["nom"], pen)]
            print(
                f"{ep['nom']:20s} pen={pen:.2f}  {tenus}/{len(detail)}"
                f"  div={r['div']:.2f}  {r['duree']:.0f}s",
                flush=True,
            )

    entete = " | ".join(f"pen {p:.2f}" for p in PENALITES)
    L = [
        f"# Résumer · rédiger · analyser — {label} ({CANDIDATS[label]['params']})\n",
        "Le contrôle qui correspond à la définition officielle du domaine",
        "`corporate_enterprise` : *knowledge-work productivity: summarization, drafting,",
        "and analysis for small and medium enterprises*. Température nulle, gabarit de",
        "conversation du GGUF appliqué, critères vérifiables sans avis humain — voir",
        "l'en-tête de `bench/redaction.py` pour la méthode de notation.\n",
        "**1,00 est le défaut de la chaîne officielle** ; 1,10 était la valeur retenue à",
        "l'étape 3 sur le contrôle arithmétique ; 1,05 est celle retenue après ce",
        "passage-ci. Voir `bench/resultats.md`, étape 5, pour ce qui a départagé —",
        "ce n'est pas ce tableau, où les trois valeurs se tiennent.\n",
        "## Score par épreuve — part des critères tenus\n",
        f"| Épreuve | Genre | Cadre | {entete} |",
        "|---|---|---|" + "---|" * len(PENALITES),
    ]
    for ep in EPREUVES:
        cases = []
        for pen in PENALITES:
            r = res[(ep["nom"], pen)]
            gras = "**" if r["div"] < SEUIL_PANNE else ""
            cases.append(
                f"{gras}{r['tenus']}/{r['total']}{gras}" + (" ⚠" if r["coupe"] else "")
            )
        L.append(f"| {ep['nom']} | {ep['genre']} | {ep['cadre']} | " + " | ".join(cases) + " |")

    genres = ["résumer", "rédiger", "analyser"]
    L.append("")
    L.append(f"| Total | | | {entete} |")
    L.append("|---|---|---|" + "---|" * len(PENALITES))
    for g in genres:
        lot = [ep for ep in EPREUVES if ep["genre"] == g]
        cases = []
        for pen in PENALITES:
            t = sum(res[(ep["nom"], pen)]["tenus"] for ep in lot)
            n = sum(res[(ep["nom"], pen)]["total"] for ep in lot)
            cases.append(f"**{t}/{n}** ({100 * t / n:.0f} %)")
        L.append(f"| **{g}** | {len(lot)} épreuves | | " + " | ".join(cases) + " |")
    cases = []
    for pen in PENALITES:
        t = sum(res[(ep["nom"], pen)]["tenus"] for ep in EPREUVES)
        n = sum(res[(ep["nom"], pen)]["total"] for ep in EPREUVES)
        cases.append(f"**{t}/{n}** ({100 * t / n:.0f} %)")
    L.append(f"| **ensemble** | {len(EPREUVES)} épreuves | | " + " | ".join(cases) + " |")
    # Le total ci-dessus compte les critères, or les analyses en portent deux et
    # les rédactions huit : il pencherait vers la rédaction sans qu'on l'ait
    # décidé. Cette seconde ligne donne à chaque épreuve le même poids.
    cases = [
        f"**{100 * sum(res[(ep['nom'], pen)]['score'] for ep in EPREUVES) / len(EPREUVES):.0f} %**"
        for pen in PENALITES
    ]
    L.append("| **moyenne par épreuve** | à poids égal | | " + " | ".join(cases) + " |")

    # Le contrôle d'hallucination mérite sa propre ligne : c'est le défaut le
    # plus coûteux à l'usage, et celui qu'un score agrégé dilue.
    L += ["\n## Hallucination de nombres\n",
          f"| Épreuve | {entete} |", "|---|" + "---|" * len(PENALITES)]
    for ep in EPREUVES:
        if not ep["criteres"].get("sans_invention"):
            continue
        cases = []
        for pen in PENALITES:
            inv = res[(ep["nom"], pen)]["inventes"]
            cases.append("✅ aucun" if not inv else "❌ " + ", ".join(inv))
        L.append(f"| {ep['nom']} | " + " | ".join(cases) + " |")

    L.append("\n---\n\n## Copies intégrales, critère par critère\n")
    for ep in EPREUVES:
        L.append(f"\n### {ep['nom']} · {ep['genre']} · {ep['cadre']}\n")
        L.append("> " + ep["prompt"].replace("\n", "\n> ") + "\n")
        for pen in PENALITES:
            r = res[(ep["nom"], pen)]
            extrait = r["texte"]
            if r["div"] < SEUIL_PANNE and len(extrait) > 600:
                extrait = extrait[:600] + f"\n\n_(…coupé : {len(r['texte'])} caractères de boucle)_"
            L.append(
                f"\n#### pénalité {pen:.2f} — {r['tenus']}/{r['total']}, "
                f"diversité {r['div']:.2f}, {r['duree']:.0f} s"
                + (", coupé au budget" if r["coupe"] else "") + "\n"
            )
            for libelle, ok in r["detail"]:
                L.append(f"- {'✓' if ok else '✗'} {libelle}")
            L.append("\n```\n" + (extrait or "(réponse vide)") + "\n```\n")

    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text("\n".join(L))
    print(f"→ {SORTIE.relative_to(RACINE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
