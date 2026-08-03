#!/usr/bin/env python3
"""Fabrique le corpus de calibration de la matrice d'importance.

Pourquoi un corpus fabriqué plutôt que collecté. Une matrice d'importance se
calcule en faisant lire du texte au modèle et en relevant quels poids
s'activent ; ce qu'on lui donne à lire décide donc quels poids seront protégés
à la quantisation. La calibration héritée du fichier livré est de l'anglais
générique — 80 fragments, choisis par quelqu'un d'autre pour un usage qui n'est
pas le nôtre. Le registre de cette soumission est le document d'entreprise
francophone : contrats, comptes rendus, notes de service, relances, analyses.

Collecter ce registre pose deux problèmes qu'un dépôt public ne peut pas
résoudre : les vrais documents d'entreprise ne sont pas publiables, et les
corpus juridiques en ligne arrivent sans licence claire. On fabrique donc, à
partir de gabarits et d'un tirage à graine fixe : le corpus est intégralement
reproductible depuis ce fichier, ne contient aucune donnée réelle, et se lit.

Ce que ce corpus n'est pas : du texte authentique. Sa syntaxe est celle de ses
gabarits, et une matrice calibrée dessus protège les poids qu'active cette
syntaxe-là. C'est la limite de la méthode, et elle est mesurée en fin de script
— la diversité en 4-grammes est imprimée, pas supposée.

Usage : python imatrix/corpus.py > imatrix/corpus.txt
"""
from __future__ import annotations

import collections
import random
import sys

# Graine fixe : deux exécutions produisent le même corpus, octet pour octet.
GRAINE = 20260803

# Taille choisie par mesure, pas par confort. Le texte écrit à la main est une
# quantité fixe : allonger le corpus ne fait que le répéter, et une matrice
# estimée sur des répétitions sur-pondère les tournures répétées. Diversité en
# 4-grammes relevée sur trois tailles — 330 ko : 0,380 · 240 ko : 0,432 ·
# 180 ko : 0,489 — pour un nombre de fragments qui reste du même ordre que la
# calibration héritée (80). On garde donc la plus courte des trois.
CIBLE_OCTETS = 180_000

# ————————————————————————————————————————————————————————————————————————
# Entités. La dispersion géographique est délibérée : une matrice calibrée
# sur une seule ville protégerait les poids de cette ville.
# ————————————————————————————————————————————————————————————————————————

VILLES = [
    "Abidjan", "Ouagadougou", "Dakar", "Bamako", "Lomé", "Cotonou", "Accra",
    "Douala", "Yaoundé", "Niamey", "Conakry", "Bobo-Dioulasso", "Kumasi",
    "San-Pédro", "Thiès", "Korhogo", "Parakou", "Garoua",
]

SOCIETES = [
    "Sahel Distribution", "Kadi & Fils", "Ivoire Logistique", "Faso Matériaux",
    "Atlantique Négoce", "Zongo Transit", "Delta Agro", "Nord Équipements",
    "Sika Industries", "Wend-Panga BTP", "Baobab Services", "Lagune Froid",
    "Sourou Semences", "Kola Pharma", "Tanoé Emballages", "Mistral Marine",
    "Sahara Telecom", "Palmier Agroalimentaire", "Comoé Textiles",
    "Volta Énergie", "Bandama Câbles", "Karité Cosmétiques",
]

PERSONNES = [
    "M. Ouédraogo", "Mme Koné", "M. Diallo", "Mme Traoré", "M. Zongo",
    "Mme Sanogo", "M. Kouassi", "Mme Bamba", "M. Sawadogo", "Mme Nikiéma",
    "M. Compaoré", "Mme Yaméogo", "M. Doumbia", "Mme Cissé", "M. Tapsoba",
    "Mme Sy", "M. Anyanwu", "Mme Mensah", "M. Boadi", "Mme Owusu",
]

SERVICES = [
    "la direction commerciale", "le service achats", "la direction financière",
    "le service logistique", "la direction des ressources humaines",
    "le service qualité", "la direction technique", "le service juridique",
    "le contrôle de gestion", "le service après-vente",
]

PRODUITS = [
    "ciment CPJ 35", "tôles bac alu", "huile de palme raffinée", "engrais NPK",
    "câbles cuivre 2,5 mm²", "groupes électrogènes 15 kVA", "riz brisé 25 %",
    "emballages carton triple cannelure", "pneus poids lourd 315/80",
    "chambres froides 12 m³", "sacs polypropylène tissés", "tubes PVC ⌀110",
    "panneaux solaires 450 Wc", "batteries à décharge lente 200 Ah",
    "gasoil non routier", "semences de maïs certifiées",
]

GOODS = [
    "cement", "roofing sheets", "refined palm oil", "fertiliser", "copper cable",
    "15 kVA generator sets", "broken rice", "corrugated packaging",
    "heavy-goods tyres", "cold rooms", "woven polypropylene sacks",
    "PVC piping", "450 Wp solar panels", "deep-cycle batteries",
]

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

SECTEURS = [
    "la distribution", "le BTP", "l'agro-industrie", "la logistique",
    "le négoce de matériaux", "la transformation agroalimentaire",
    "les services aux entreprises", "l'importation d'équipements",
]


def tirer(alea: random.Random) -> dict:
    """Le décor d'un document : tiré une fois, réutilisé dans tous ses blocs."""
    montant = alea.randrange(750, 96_000) * 1000
    return {
        "ville": alea.choice(VILLES),
        "ville2": alea.choice(VILLES),
        "societe": alea.choice(SOCIETES),
        "societe2": alea.choice(SOCIETES),
        "personne": alea.choice(PERSONNES),
        "personne2": alea.choice(PERSONNES),
        "service": alea.choice(SERVICES),
        "produit": alea.choice(PRODUITS),
        "good": alea.choice(GOODS),
        "secteur": alea.choice(SECTEURS),
        "mois": alea.choice(MOIS),
        "mois2": alea.choice(MOIS),
        "month": alea.choice(MONTHS),
        "jour": alea.randrange(1, 29),
        "jour2": alea.randrange(1, 29),
        "annee": alea.choice([2024, 2025, 2026]),
        "montant": f"{montant:,}".replace(",", " "),
        "montant2": f"{alea.randrange(120, 9800) * 1000:,}".replace(",", " "),
        "amount": f"{alea.randrange(12, 940) * 1000:,}",
        "pct": alea.randrange(2, 48),
        "pct2": alea.randrange(2, 48),
        "delai": alea.choice([7, 10, 14, 15, 21, 30, 45, 60, 90]),
        "quantite": alea.randrange(12, 4800),
        "ref": f"{alea.choice('ABCDEFGHJKLMNPRSTV')}{alea.choice('ABCDEFGHJKLMNPRSTV')}"
               f"-{alea.randrange(1000, 9999)}",
        "ref2": f"{alea.randrange(2024, 2027)}-{alea.randrange(10, 99)}",
        "effectif": alea.randrange(6, 320),
        "unite": alea.choice(["tonnes", "palettes", "cartons", "unités", "sacs", "rouleaux"]),
        "unit": alea.choice(["tonnes", "pallets", "cartons", "units", "bags"]),
    }


# ————————————————————————————————————————————————————————————————————————
# Les gabarits. Un genre est une suite de blocs ; un bloc est une liste de
# formulations dont une seule est tirée. La combinatoire vient de là, et non
# d'une reformulation automatique — chaque phrase a été écrite.
# ————————————————————————————————————————————————————————————————————————

GENRES: dict[str, list[list[str]]] = {}

GENRES["contrat_fr"] = [
    ["CONTRAT DE FOURNITURE N° {ref}\n\nEntre les soussignés : {societe}, société "
     "de droit ivoirien au capital de {montant2} FCFA, dont le siège social est "
     "situé à {ville}, ci-après dénommée « le Fournisseur », d'une part,",
     "CONTRAT DE PRESTATION DE SERVICES N° {ref}\n\nEntre : {societe}, dont le "
     "siège est établi à {ville}, représentée par {personne} agissant en qualité "
     "de directeur général, ci-après « le Prestataire », d'une part,",
     "MARCHÉ DE FOURNITURES N° {ref}\n\nLe présent marché est conclu entre "
     "{societe}, immatriculée au registre du commerce de {ville}, ci-après « le "
     "Titulaire », d'une part,"],
    ["et {societe2}, ayant son établissement principal à {ville2}, représentée "
     "par {personne2}, ci-après dénommée « le Client », d'autre part.",
     "et {societe2}, dont le siège est à {ville2}, dûment représentée aux "
     "présentes par {personne2}, ci-après « l'Acheteur », d'autre part.",
     "et {societe2}, établie à {ville2}, ci-après désignée « le Bénéficiaire », "
     "d'autre part. Les parties ont convenu ce qui suit."],
    ["\nArticle 1 — Objet\nLe présent contrat a pour objet la fourniture de "
     "{quantite} {unite} de {produit}, selon les spécifications techniques "
     "annexées, qui font partie intégrante du contrat.",
     "\nArticle 1 — Objet\nLe Fournisseur s'engage à livrer au Client "
     "{quantite} {unite} de {produit}, conformément au cahier des charges joint "
     "en annexe 1, dont les parties reconnaissent avoir pris connaissance.",
     "\nArticle 1 — Objet\nLe contrat porte sur la fourniture et la mise en "
     "service de {quantite} {unite} de {produit} sur le site du Client à "
     "{ville2}, à l'exclusion de toute autre prestation."],
    ["\nArticle 2 — Prix et modalités de règlement\nLe montant total du marché "
     "est fixé à {montant} FCFA hors taxes. Le règlement intervient à "
     "{delai} jours fin de mois à compter de la réception de la facture, par "
     "virement bancaire sur le compte désigné par le Fournisseur.",
     "\nArticle 2 — Prix\nLe prix global et forfaitaire s'établit à {montant} "
     "FCFA HT. Il est ferme et non révisable pendant toute la durée du contrat. "
     "Un acompte de {pct} % est versé à la commande, le solde à la livraison.",
     "\nArticle 2 — Conditions financières\nLe montant du contrat s'élève à "
     "{montant} FCFA hors taxes, payable en trois échéances : {pct} % à la "
     "signature, {pct2} % au démarrage, le solde après réception définitive."],
    ["\nArticle 3 — Délais\nLa livraison intervient au plus tard le {jour} "
     "{mois} {annee}. Tout retard supérieur à {delai} jours ouvre droit, au "
     "profit du Client, à une pénalité calculée par semaine entamée et plafonnée "
     "en valeur, sans que le Client ait à justifier d'un préjudice.",
     "\nArticle 3 — Délai d'exécution\nLe Prestataire dispose de {delai} jours "
     "calendaires à compter de la notification du présent contrat pour achever "
     "les prestations. Ce délai est suspendu en cas de force majeure dûment "
     "notifiée dans les quarante-huit heures.",
     "\nArticle 3 — Livraison\nLes marchandises sont livrées à {ville2}, rendues "
     "quai, au plus tard le {jour} {mois} {annee}. Le transfert des risques "
     "s'opère à la remise effective au Client ou à son transitaire."],
    ["\nArticle 4 — Garantie\nLe Fournisseur garantit les fournitures contre "
     "tout vice de fabrication pendant douze mois à compter de la réception. La "
     "garantie couvre le remplacement des pièces défectueuses, à l'exclusion des "
     "dommages résultant d'un défaut d'entretien.",
     "\nArticle 4 — Réception\nLa réception est prononcée contradictoirement en "
     "présence des deux parties. En cas de réserves, le Fournisseur dispose de "
     "{delai} jours pour y remédier. Passé ce délai, le Client peut faire "
     "exécuter les reprises aux frais du Fournisseur.",
     "\nArticle 4 — Conformité\nLe Client dispose de huit jours ouvrés à compter "
     "de la livraison pour formuler ses réserves. À défaut, les fournitures sont "
     "réputées acceptées sans réserve."],
    ["\nArticle 5 — Résiliation\nEn cas de manquement grave de l'une des "
     "parties à ses obligations, l'autre partie peut résilier le contrat de "
     "plein droit, quinze jours après une mise en demeure restée sans effet.",
     "\nArticle 5 — Confidentialité\nChaque partie s'interdit de divulguer les "
     "informations dont elle a connaissance à l'occasion de l'exécution du "
     "contrat, pendant sa durée et les trois années suivant son terme.",
     "\nArticle 5 — Sous-traitance\nLe Fournisseur ne peut sous-traiter tout ou "
     "partie des prestations sans l'accord écrit préalable du Client. "
     "L'agrément d'un sous-traitant ne décharge le Fournisseur d'aucune de ses "
     "obligations."],
    ["\nArticle 6 — Litiges\nTout différend relatif à l'interprétation ou à "
     "l'exécution du présent contrat est soumis, à défaut d'accord amiable dans "
     "un délai de trente jours, au tribunal de commerce de {ville}.\n\nFait à "
     "{ville}, le {jour2} {mois2} {annee}, en deux exemplaires originaux.",
     "\nArticle 6 — Droit applicable\nLe présent contrat est régi par les Actes "
     "uniformes de l'OHADA et, à titre supplétif, par le droit national du lieu "
     "d'exécution.\n\nFait à {ville}, le {jour2} {mois2} {annee}.",
     "\nArticle 6 — Élection de domicile\nLes parties élisent domicile aux "
     "adresses figurant en tête des présentes. Toute modification doit être "
     "notifiée par lettre recommandée.\n\nFait à {ville}, le {jour2} {mois2} "
     "{annee}, en deux exemplaires."],
]

GENRES["compte_rendu_fr"] = [
    ["COMPTE RENDU DE RÉUNION\n\nRéunion du comité de direction — {ville}, "
     "{jour} {mois} {annee}\nPrésents : {personne}, {personne2}, les "
     "responsables de {service}.\nAbsent excusé : le directeur technique.",
     "COMPTE RENDU\n\nRevue de projet {ref} — {ville}, le {jour} {mois} "
     "{annee}\nAnimateur : {personne}. Participants : sept personnes, dont les "
     "représentants de {service}.",
     "PROCÈS-VERBAL DE RÉUNION\n\nObjet : point mensuel d'activité — {ville}, "
     "{jour} {mois} {annee}\nLa séance est ouverte à neuf heures par "
     "{personne}."],
    ["\n1. Approbation du compte rendu précédent\nLe compte rendu de la séance "
     "du {jour2} {mois2} est approuvé sans modification.",
     "\n1. Suivi des décisions\nSur les six actions arrêtées lors de la séance "
     "précédente, quatre sont soldées, une est en cours et une est reportée "
     "faute de disponibilité budgétaire.",
     "\n1. Ouverture\n{personne} rappelle l'ordre du jour et précise que les "
     "arbitrages attendus portent sur trois points seulement."],
    ["\n2. Activité commerciale\nLe chiffre d'affaires du mois s'établit à "
     "{montant} FCFA, en progression de {pct} % par rapport au même mois de "
     "l'exercice précédent. La croissance provient principalement des ventes de "
     "{produit}, tandis que les autres lignes stagnent.",
     "\n2. Situation commerciale\nLes commandes enregistrées atteignent "
     "{montant} FCFA, soit {pct} % de l'objectif annuel. {personne2} signale que "
     "deux clients importants de {ville2} ont décalé leurs engagements au "
     "trimestre suivant.",
     "\n2. Ventes\nLe carnet de commandes représente {quantite} {unite} à "
     "livrer d'ici la fin du trimestre. Le taux de service ressort à {pct} %, "
     "en retrait par rapport au mois précédent."],
    ["\n3. Exploitation\nDeux ruptures de stock ont été constatées sur "
     "{produit}, chacune de {delai} jours. Le service logistique attribue la "
     "première à un retard portuaire et la seconde à une commande passée "
     "tardivement.",
     "\n3. Production\nLe taux d'utilisation des équipements s'établit à "
     "{pct} %. Une immobilisation de {delai} jours a été nécessaire pour la "
     "maintenance annuelle, opération planifiée mais dont la durée a dépassé la "
     "prévision de deux jours.",
     "\n3. Logistique\nSur {quantite} {unite} expédiées, {pct} % sont arrivées "
     "dans le délai contractuel. Les retards concernent essentiellement l'axe "
     "{ville} — {ville2}, où les contrôles routiers se sont multipliés."],
    ["\n4. Trésorerie\nL'encours client atteint {montant2} FCFA, dont une part "
     "significative à plus de {delai} jours. {personne} demande qu'une relance "
     "systématique soit engagée avant la fin du mois.",
     "\n4. Situation financière\nLe délai moyen de règlement clients s'établit "
     "à {delai} jours, contre 45 jours l'an dernier. La direction financière "
     "propose de conditionner les nouvelles livraisons au règlement des "
     "factures échues.",
     "\n4. Budget\nLes dépenses engagées représentent {pct} % du budget annuel "
     "à mi-exercice. L'écart favorable provient d'un report d'investissement et "
     "non d'une économie de fonctionnement."],
    ["\n5. Ressources humaines\nL'effectif s'établit à {effectif} personnes. "
     "Deux recrutements sont en cours pour {service}. La formation sécurité "
     "prévue en {mois2} concernera l'ensemble des opérateurs.",
     "\n5. Personnel\n{personne2} indique que le plan de formation a été "
     "consommé à {pct} %. Le comité valide le principe d'une session "
     "complémentaire à {ville2}.",
     "\n5. Organisation\nLe rattachement de {service} est modifié à compter du "
     "1er {mois2}. La note d'organisation correspondante sera diffusée dans la "
     "semaine."],
    ["\n6. Décisions\n— Relancer les clients dont les factures dépassent "
     "{delai} jours, avant le {jour2} {mois2}.\n— Constituer un stock de "
     "sécurité de {quantite} {unite} de {produit}.\n— Reporter l'arbitrage sur "
     "l'investissement au prochain comité.\n\nLa séance est levée à onze heures "
     "trente.",
     "\n6. Actions arrêtées\n— {personne} présentera un chiffrage détaillé du "
     "projet {ref} avant le {jour2} {mois2}.\n— {service} révisera les "
     "conditions générales de vente.\n— Une réponse écrite sera adressée au "
     "fournisseur de {ville2}.\n\nProchaine réunion le {jour2} {mois2}.",
     "\n6. Conclusions\nLe comité valide le principe d'un plan d'action en "
     "trois volets et charge {personne2} d'en assurer le suivi. Un point "
     "d'étape est fixé dans quinze jours.\n\nLa séance est levée."],
]

GENRES["note_service_fr"] = [
    ["NOTE DE SERVICE N° {ref2}\n\nDe : {service}\nÀ : l'ensemble du personnel\n"
     "Objet : procédure de demande de congés\n{ville}, le {jour} {mois} {annee}",
     "NOTE DE SERVICE N° {ref2}\n\nÉmetteur : la direction générale\n"
     "Destinataires : chefs de service et responsables d'équipe\nObjet : "
     "nouvelles modalités de validation des dépenses\n{ville}, le {jour} {mois} "
     "{annee}",
     "NOTE INTERNE N° {ref2}\n\nDe : {service}\nÀ : tous les sites\nObjet : "
     "consignes de sécurité applicables aux zones de stockage\n{ville}, le "
     "{jour} {mois} {annee}"],
    ["\nÀ compter du 1er {mois2} {annee}, toute demande doit être déposée au "
     "moyen du formulaire prévu à cet effet, au moins {delai} jours avant la "
     "date souhaitée. Les demandes transmises par un autre canal ne seront plus "
     "traitées.",
     "\nLa présente note annule et remplace toutes les dispositions antérieures "
     "portant sur le même objet. Elle prend effet le 1er {mois2} {annee} et "
     "s'applique à l'ensemble des établissements.",
     "\nLes dispositions ci-après entrent en vigueur le {jour2} {mois2} "
     "{annee}. Elles concernent l'ensemble des collaborateurs, quel que soit "
     "leur statut, y compris les intérimaires et les prestataires présents sur "
     "site."],
    # Formulation réécrite après une collision de huit mots avec l'épreuve
    # `note-conges` de bench/redaction.py, signalée par contamination.py — les
    # deux textes avaient été écrits par la même main dans le même registre.
    ["\nL'accord du supérieur direct intervient sous cinq jours ouvrés. En "
     "l'absence de réponse à l'expiration de ce délai, l'autorisation est "
     "acquise, sauf impératif d'exploitation notifié par écrit à l'intéressé.",
     "\nToute dépense supérieure à {montant2} FCFA requiert désormais une "
     "validation préalable de {service}. En dessous de ce seuil, l'engagement "
     "reste de la responsabilité du chef de service, dans la limite de son "
     "budget.",
     "\nLe port des équipements de protection individuelle est obligatoire dans "
     "l'ensemble des zones signalées. Les manquements constatés feront l'objet "
     "d'un rappel écrit, puis des sanctions prévues au règlement intérieur."],
    ["\nUne exception est prévue pour les situations d'urgence familiale, "
     "appréciées au cas par cas par {service}. Dans cette hypothèse, la demande "
     "peut être régularisée après coup, dans un délai de {delai} jours.",
     "\nLes cas particuliers non prévus par la présente note sont soumis à "
     "l'arbitrage de {personne}, dont la décision est notifiée par écrit à "
     "l'intéressé et à son responsable.",
     "\nUn registre des dérogations est tenu par {service} et présenté "
     "trimestriellement à la direction. Aucune dérogation verbale ne sera "
     "opposable."],
    ["\nLes chefs de service sont chargés de porter la présente note à la "
     "connaissance de leurs équipes et d'en assurer l'affichage sur les "
     "panneaux prévus à cet effet.\n\n{personne}\nDirecteur",
     "\nCette note sera affichée sur les tableaux d'information et diffusée par "
     "voie électronique. Un exemplaire est remis à chaque nouvel entrant lors de "
     "son accueil.\n\n{personne}\n{service}",
     "\nPour toute question relative à l'application de ces dispositions, les "
     "collaborateurs sont invités à s'adresser à leur responsable direct ou à "
     "{service}.\n\n{personne}"],
]

GENRES["courriel_fr"] = [
    ["Objet : relance — facture {ref} échue\n\nMadame, Monsieur,",
     "Objet : commande {ref} — confirmation et délai\n\nBonjour {personne2},",
     "Objet : réclamation sur la livraison du {jour} {mois}\n\nMadame, "
     "Monsieur,",
     "Objet : demande de cotation — {produit}\n\nBonjour,"],
    ["\nNous revenons vers vous au sujet de la facture n° {ref}, d'un montant "
     "de {montant2} FCFA, échue depuis {delai} jours. Sauf erreur de notre "
     "part, son règlement ne nous est pas parvenu à ce jour.",
     "\nNous accusons réception de votre commande n° {ref} portant sur "
     "{quantite} {unite} de {produit}, pour un montant total de {montant} FCFA "
     "hors taxes.",
     "\nLa livraison reçue le {jour} {mois} présente un écart de {pct} % par "
     "rapport au bon de commande n° {ref} : {quantite} {unite} ont été livrées "
     "au lieu de la quantité convenue.",
     "\nNotre société, implantée à {ville} et active dans {secteur}, souhaite "
     "recevoir une cotation pour {quantite} {unite} de {produit}, livrées à "
     "{ville2}."],
    ["\nNous vous serions reconnaissants de bien vouloir procéder au règlement "
     "sous {delai} jours. Si ce paiement a été effectué entre-temps, nous vous "
     "remercions de nous en communiquer la référence afin que nous puissions le "
     "rapprocher.",
     "\nNous confirmons une expédition depuis notre dépôt de {ville} au plus "
     "tard le {jour2} {mois2}. Le transport est assuré par nos soins, les "
     "marchandises voyageant aux risques du destinataire à compter de la remise "
     "au transporteur.",
     "\nNous vous demandons de bien vouloir procéder au complément dans les "
     "meilleurs délais, ou à défaut d'établir un avoir correspondant. Les "
     "marchandises manquantes conditionnent la poursuite de notre propre "
     "chantier à {ville2}.",
     "\nMerci de nous préciser le prix unitaire rendu, le délai de mise à "
     "disposition, ainsi que vos conditions de règlement. Une visite de vos "
     "installations serait envisageable si votre offre retient notre "
     "attention."],
    ["\nÀ défaut de régularisation dans le délai indiqué, nous serions "
     "contraints de suspendre les livraisons en cours, conformément à nos "
     "conditions générales de vente.",
     "\nUn accusé de réception vous parviendra dès le départ du camion, "
     "accompagné du bon de livraison et du certificat d'analyse.",
     "\nNous restons naturellement ouverts à toute solution amiable et "
     "souhaitons que cet incident ne remette pas en cause une relation "
     "commerciale qui donne par ailleurs satisfaction.",
     "\nNous vous remercions de bien vouloir nous répondre avant le {jour2} "
     "{mois2}, date à laquelle notre comité arrêtera son choix."],
    ["\nNous restons à votre disposition pour tout complément.\n\nCordialement,"
     "\n{personne}\n{societe} — {ville}",
     "\nDans l'attente de votre retour, nous vous prions d'agréer, Madame, "
     "Monsieur, l'expression de nos salutations distinguées.\n\n{personne}\n"
     "{service}, {societe}",
     "\nBien cordialement,\n{personne}\n{societe}, {ville}"],
]

GENRES["rapport_fr"] = [
    ["RAPPORT D'ACTIVITÉ — {mois} {annee}\n{societe}, {ville}\n\n1. Synthèse",
     "NOTE DE SYNTHÈSE TRIMESTRIELLE\n{societe} — site de {ville}\n\n1. Vue "
     "d'ensemble",
     "RAPPORT MENSUEL D'EXPLOITATION\n{service} — {ville}, {mois} {annee}\n\n"
     "1. Faits marquants"],
    ["\nL'activité du mois ressort à {montant} FCFA, soit {pct} % de l'objectif. "
     "La tendance reste orientée à la hausse, portée par {secteur}, mais elle "
     "masque des situations contrastées selon les lignes de produits.",
     "\nLe trimestre se solde par un chiffre d'affaires de {montant} FCFA, en "
     "progression de {pct} % sur un an. Cette progression est intégralement "
     "imputable au second mois ; les deux autres sont en léger retrait.",
     "\nL'exploitation a été marquée par deux événements : une rupture "
     "d'approvisionnement de {delai} jours sur {produit}, et l'ouverture du "
     "point de vente de {ville2}, effective depuis le {jour} {mois}."],
    ["\n2. Ventes\nLes volumes atteignent {quantite} {unite}, contre une "
     "prévision inférieure de {pct2} %. Le prix moyen de vente s'érode "
     "légèrement sous l'effet de la concurrence sur l'axe {ville} — {ville2}.",
     "\n2. Commercial\nLe nombre de clients actifs s'établit à {effectif}. Trois "
     "comptes représentent à eux seuls {pct} % du chiffre d'affaires, ce qui "
     "constitue une concentration à surveiller.",
     "\n2. Marché\nLa demande reste soutenue sur {produit}, dont les volumes "
     "progressent de {pct} %. Les autres références sont stables. Aucun nouvel "
     "entrant significatif n'a été identifié sur la période."],
    ["\n3. Achats et stocks\nLa valeur du stock s'établit à {montant2} FCFA, "
     "soit {delai} jours de couverture. Deux références sont en surstock et une "
     "en tension permanente depuis le début de l'exercice.",
     "\n3. Approvisionnements\nLe délai moyen fournisseur atteint {delai} jours, "
     "en dégradation. Le fournisseur historique de {ville2} n'a honoré que "
     "{pct} % des commandes dans le délai annoncé.",
     "\n3. Logistique\nLe coût de transport à la tonne progresse de {pct} %, "
     "sous l'effet du prix du carburant et de l'allongement des rotations."],
    ["\n4. Points de vigilance\n— La concentration du portefeuille clients.\n"
     "— L'encours à plus de {delai} jours, qui atteint {montant2} FCFA.\n"
     "— La dépendance à un fournisseur unique sur {produit}.",
     "\n4. Risques identifiés\n— Un litige commercial est en cours avec un "
     "client de {ville2} ; le montant en jeu est de {montant2} FCFA.\n"
     "— Le renouvellement du contrat de maintenance n'est pas engagé.\n"
     "— Deux postes clés de {service} restent vacants.",
     "\n4. Alertes\nL'écart entre le budget et le réalisé atteint {pct} % sur "
     "les charges externes. Cet écart n'est pas expliqué à ce stade et fait "
     "l'objet d'une analyse par le contrôle de gestion."],
    ["\n5. Perspectives\nLe mois de {mois2} devrait bénéficier de la "
     "saisonnalité favorable. Sous réserve de la levée des tensions "
     "d'approvisionnement, l'objectif annuel reste atteignable.\n\nRapport "
     "établi par {personne}, {service}.",
     "\n5. Actions engagées\nUne renégociation des conditions d'achat est "
     "ouverte. Le recrutement de deux collaborateurs est lancé. Un plan de "
     "réduction du stock dormant sera présenté au prochain comité.\n\n"
     "{personne}, {ville}, le {jour2} {mois2} {annee}.",
     "\n5. Recommandations\nIl est proposé de conditionner les livraisons des "
     "clients en dépassement d'encours, d'ouvrir une seconde source "
     "d'approvisionnement et de réviser la tarification avant la fin du "
     "trimestre.\n\n{personne}"],
]

GENRES["analyse_fr"] = [
    ["ANALYSE — écart budgétaire {mois} {annee}\n{service}, {societe}",
     "NOTE D'ANALYSE — rentabilité de la ligne {produit}\n{societe}, {ville}",
     "ÉTUDE PRÉALABLE — opportunité d'implantation à {ville2}\n{societe}"],
    ["\nLe budget de la période prévoyait {montant} FCFA de charges ; le réalisé "
     "s'établit à {montant2} FCFA. L'écart est défavorable et se concentre sur "
     "deux postes.",
     "\nLe chiffre d'affaires de la ligne atteint {montant} FCFA pour un coût "
     "d'achat de {montant2} FCFA. La marge brute qui en découle doit encore "
     "supporter les charges de distribution, ce que l'analyse ci-dessous "
     "détaille.",
     "\nL'implantation envisagée à {ville2} suppose un investissement initial "
     "de {montant} FCFA et des charges de structure annuelles estimées à "
     "{montant2} FCFA."],
    ["\nPremier poste : le transport, qui dépasse la prévision de {pct} %. "
     "L'analyse des factures montre que l'écart provient pour l'essentiel de "
     "trois rotations exceptionnelles vers {ville2}, décidées pour éviter une "
     "rupture chez un client important.",
     "\nLe coût de revient unitaire s'établit à un niveau supérieur de {pct} % "
     "à celui retenu lors de la construction du tarif. L'écart tient à la "
     "hausse du prix d'achat, non répercutée en aval.",
     "\nLe point mort est atteint pour un volume de {quantite} {unite} par an. "
     "Le marché local, estimé à partir des données disponibles, permettrait "
     "d'atteindre ce seuil au cours de la deuxième année."],
    ["\nSecond poste : les charges de personnel, en dépassement de {pct2} %. "
     "Le recours aux heures supplémentaires a compensé deux absences prolongées "
     "et n'a donc pas de caractère structurel.",
     "\nDeuxième facteur : la remise commerciale moyenne consentie atteint "
     "{pct2} %, contre un objectif inférieur. Cette dérive s'observe "
     "principalement sur les commandes traitées en fin de mois.",
     "\nLe principal facteur de sensibilité est le taux d'occupation. Une "
     "variation de dix points sur cette hypothèse déplace le point mort de "
     "près d'un an, ce qui rend la décision dépendante d'une donnée que nous "
     "ne maîtrisons pas."],
    ["\nLecture d'ensemble : sur l'écart total, une part est conjoncturelle et "
     "se résorbera d'elle-même ; le reste appelle une décision. Il serait "
     "prématuré d'en conclure à une dérive générale des charges.",
     "\nAu total, la ligne reste contributive, mais sa marge s'est réduite. La "
     "question posée n'est pas son maintien mais le niveau de prix auquel elle "
     "doit être vendue à compter de {mois2}.",
     "\nCes éléments ne permettent pas de trancher à eux seuls. Ils délimitent "
     "les conditions dans lesquelles le projet serait rentable, et celles dans "
     "lesquelles il ne le serait pas."],
    ["\nRecommandations\n1. Rétablir la validation préalable des transports "
     "exceptionnels.\n2. Ne pas modifier le budget de personnel avant la fin de "
     "l'exercice.\n3. Représenter une analyse actualisée au comité de {mois2}.",
     "\nRecommandations\n1. Réviser le tarif de {produit} à compter du 1er "
     "{mois2}.\n2. Encadrer la remise maximale accordée sans validation.\n"
     "3. Suivre mensuellement le coût de revient unitaire.",
     "\nSuite proposée\n1. Confirmer l'hypothèse de volume par une étude de "
     "terrain à {ville2}.\n2. Chiffrer une variante en location plutôt qu'en "
     "acquisition.\n3. Différer la décision au prochain exercice."],
]

GENRES["devis_fr"] = [
    ["DEVIS N° {ref}\n{societe} — {ville}\nÉtabli le {jour} {mois} {annee}, "
     "valable trente jours\n\nClient : {societe2}, {ville2}",
     "PROPOSITION COMMERCIALE N° {ref}\n{societe}, {ville}\nÀ l'attention de "
     "{personne2}, {societe2}\nDate : {jour} {mois} {annee}",
     "OFFRE DE PRIX N° {ref}\nÉmetteur : {societe}, {ville}\nDestinataire : "
     "{societe2}, {ville2}\nDate d'établissement : {jour} {mois} {annee}"],
    ["\nDésignation : {produit}\nQuantité : {quantite} {unite}\nPrix unitaire "
     "hors taxes : voir grille jointe\nMontant total hors taxes : {montant} "
     "FCFA",
     "\nObjet : fourniture de {quantite} {unite} de {produit}\nMontant hors "
     "taxes : {montant} FCFA\nTVA applicable selon la réglementation en "
     "vigueur\nMontant toutes taxes comprises : voir récapitulatif",
     "\nPrestation proposée : fourniture, transport et déchargement de "
     "{quantite} {unite} de {produit} sur le site de {ville2}.\nMontant global "
     "et forfaitaire : {montant} FCFA hors taxes."],
    ["\nConditions de livraison : rendu {ville2}, déchargement à la charge du "
     "client. Délai indicatif : {delai} jours à compter de la commande ferme, "
     "sous réserve de disponibilité au moment de la confirmation.",
     "\nDélai d'exécution : {delai} jours calendaires après réception de "
     "l'acompte. Livraison en une seule fois, sauf accord contraire des "
     "parties.",
     "\nModalités : la présente offre s'entend marchandises disponibles en "
     "dépôt à {ville}. Un enlèvement par les soins du client donnerait lieu à "
     "une remise de {pct} % sur le prix indiqué."],
    ["\nConditions de règlement : acompte de {pct} % à la commande, solde à "
     "{delai} jours date de facture. Tout retard de paiement entraîne "
     "l'application des pénalités prévues par la réglementation.",
     "\nRèglement : {pct} % à la commande, {pct2} % à la livraison, solde à "
     "trente jours. Aucun escompte n'est consenti pour paiement anticipé.",
     "\nPaiement par virement bancaire ou chèque certifié. Les marchandises "
     "restent la propriété du vendeur jusqu'au paiement intégral du prix."],
    ["\nLa présente offre est valable trente jours à compter de sa date "
     "d'émission. Passé ce délai, les prix sont susceptibles d'être révisés "
     "sans préavis.\n\n{personne}\n{service}",
     "\nCette proposition annule et remplace notre offre précédente. Elle est "
     "établie sur la base des informations transmises par le client et pourra "
     "être ajustée si celles-ci évoluent.\n\n{personne}",
     "\nNous restons à votre disposition pour adapter cette offre à vos "
     "contraintes de calendrier ou de conditionnement.\n\n{personne}, "
     "{societe}"],
]

GENRES["contract_en"] = [
    ["SUPPLY AGREEMENT No. {ref}\n\nThis agreement is made between {societe}, a "
     "company having its registered office in {ville} (\"the Supplier\"), and "
     "{societe2}, having its principal place of business in {ville2} (\"the "
     "Buyer\").",
     "SERVICE AGREEMENT No. {ref}\n\nBetween {societe}, of {ville}, represented "
     "by {personne} (\"the Provider\"), and {societe2}, of {ville2}, "
     "represented by {personne2} (\"the Client\").",
     "FRAMEWORK PURCHASE AGREEMENT No. {ref}\n\nEntered into on {jour} {month} "
     "{annee} between {societe} (\"the Seller\") and {societe2} (\"the "
     "Purchaser\")."],
    ["\n1. Scope\nThe Supplier shall deliver {quantite} {unit} of {good} in "
     "accordance with the technical specification set out in Schedule 1, which "
     "forms part of this agreement.",
     "\n1. Subject matter\nThe Provider shall supply and commission {quantite} "
     "{unit} of {good} at the Client's premises in {ville2}. No other service "
     "is included unless separately agreed in writing.",
     "\n1. Purpose\nThis agreement governs the supply of {good} by the Seller "
     "to the Purchaser over a period of twelve months, in quantities to be "
     "specified in individual purchase orders."],
    ["\n2. Price and payment\nThe total contract value is {amount} FCFA "
     "excluding tax. Payment falls due {delai} days from the date of invoice, "
     "by bank transfer to the account nominated by the Supplier.",
     "\n2. Consideration\nThe firm lump-sum price is {amount} FCFA net of tax "
     "and is not subject to revision during the term. A deposit of {pct} % is "
     "payable on order, the balance on delivery.",
     "\n2. Payment terms\nInvoices are payable within {delai} days. Late "
     "payment accrues interest at the statutory rate without further notice."],
    ["\n3. Delivery\nDelivery shall be completed no later than {jour} {month} "
     "{annee}. Any delay exceeding {delai} days entitles the Buyer to "
     "liquidated damages calculated per week commenced, subject to an overall "
     "cap.",
     "\n3. Time for performance\nThe Provider has {delai} calendar days from "
     "notification of this agreement to complete the works. Time is of the "
     "essence.",
     "\n3. Delivery and risk\nGoods are delivered to {ville2}, carriage paid. "
     "Risk passes on physical delivery to the Purchaser or its nominated "
     "carrier; title passes only on payment in full."],
    ["\n4. Acceptance\nThe Purchaser has eight working days from delivery to "
     "notify defects. Failing such notice, the goods are deemed accepted "
     "without reservation.",
     "\n4. Warranty\nThe Supplier warrants the goods against manufacturing "
     "defects for twelve months from delivery. The warranty is limited to "
     "replacement of defective parts and excludes damage arising from misuse.",
     "\n4. Inspection\nAcceptance is pronounced jointly by both parties. Where "
     "reservations are recorded, the Supplier has {delai} days to remedy them "
     "at its own cost."],
    ["\n5. Termination\nEither party may terminate this agreement for material "
     "breach, fifteen days after written notice has remained without effect.\n\n"
     "Signed at {ville} on {jour2} {month} {annee}, in two originals.",
     "\n5. Confidentiality\nEach party shall keep confidential all information "
     "received in the course of performance, for the term of this agreement and "
     "three years thereafter.\n\nSigned at {ville} on {jour2} {month} {annee}.",
     "\n5. Governing law\nThis agreement is governed by the OHADA Uniform Acts "
     "and, subsidiarily, by the national law of the place of performance. "
     "Disputes shall be referred to the commercial court of {ville}.\n\nSigned "
     "in duplicate at {ville}."],
]

GENRES["minutes_en"] = [
    ["MINUTES OF MEETING\n\nManagement committee — {ville}, {jour} {month} "
     "{annee}\nPresent: {personne}, {personne2} and the heads of department.\n"
     "Apologies: the technical director.",
     "MINUTES\n\nProject review {ref} — {ville}, {jour} {month} {annee}\n"
     "Chair: {personne}. Seven participants.",
     "RECORD OF MEETING\n\nMonthly operations review — {ville}, {jour} {month} "
     "{annee}\nThe meeting opened at nine o'clock."],
    ["\n1. Previous minutes\nThe minutes of the meeting held on {jour2} "
     "{month} were approved without amendment.",
     "\n1. Matters arising\nOf the six actions agreed at the previous meeting, "
     "four are closed, one is in progress and one is deferred for lack of "
     "budget.",
     "\n1. Opening\n{personne} set out the agenda and noted that only three "
     "items required a decision."],
    ["\n2. Commercial performance\nRevenue for the month stands at {amount} "
     "FCFA, up {pct} % year on year. Growth came principally from {good}; other "
     "lines were flat.",
     "\n2. Sales\nOrders booked reached {amount} FCFA, or {pct} % of the annual "
     "target. {personne2} reported that two significant customers in {ville2} "
     "had deferred their commitments to the following quarter.",
     "\n2. Order book\nThe order book represents {quantite} {unit} for "
     "delivery before quarter end. Service level stands at {pct} %, down on the "
     "previous month."],
    ["\n3. Operations\nTwo stock-outs were recorded on {good}, each lasting "
     "{delai} days. Logistics attributed the first to a port delay and the "
     "second to a late purchase order.",
     "\n3. Production\nEquipment utilisation stands at {pct} %. Annual "
     "maintenance required {delai} days of downtime — planned, but two days "
     "longer than forecast.",
     "\n3. Distribution\nOf {quantite} {unit} despatched, {pct} % arrived "
     "within the contractual window. Delays were concentrated on the {ville} to "
     "{ville2} route."],
    ["\n4. Cash position\nTrade receivables stand at {amount} FCFA, a "
     "significant portion of which is more than {delai} days overdue. "
     "{personne} asked for systematic chasing before month end.",
     "\n4. Finance\nAverage customer payment days stand at {delai}. Finance "
     "proposed making further deliveries conditional on settlement of overdue "
     "invoices.",
     "\n4. Budget\nCommitted expenditure represents {pct} % of the annual "
     "budget at the half-year. The favourable variance reflects deferred "
     "investment rather than a saving in running costs."],
    ["\n5. Decisions\n— Chase all invoices more than {delai} days overdue "
     "before {jour2} {month}.\n— Build a safety stock of {quantite} {unit} of "
     "{good}.\n— Defer the investment decision to the next committee.\n\nThe "
     "meeting closed at half past eleven.",
     "\n5. Actions\n— {personne} to present a detailed costing of project "
     "{ref} before {jour2} {month}.\n— Terms of sale to be revised.\n— A "
     "written reply to be sent to the supplier in {ville2}.\n\nNext meeting: "
     "{jour2} {month}.",
     "\n5. Conclusions\nThe committee approved a three-part action plan and "
     "asked {personne2} to monitor it. A progress review was set for two weeks' "
     "time.\n\nThe meeting closed."],
]

GENRES["memo_en"] = [
    ["INTERNAL MEMORANDUM No. {ref2}\n\nFrom: the finance department\nTo: all "
     "department heads\nSubject: revised expenditure approval limits\n{ville}, "
     "{jour} {month} {annee}",
     "MEMORANDUM No. {ref2}\n\nFrom: human resources\nTo: all staff\nSubject: "
     "leave request procedure\n{ville}, {jour} {month} {annee}",
     "NOTICE No. {ref2}\n\nFrom: the operations director\nTo: all sites\n"
     "Subject: safety rules in storage areas\n{ville}, {jour} {month} {annee}"],
    ["\nWith effect from 1 {month} {annee}, any expenditure above {amount} FCFA "
     "requires prior approval. Below that threshold, commitment remains the "
     "responsibility of the department head, within the approved budget.",
     "\nWith effect from {jour2} {month} {annee}, requests must be submitted on "
     "the prescribed form at least {delai} days before the date requested. "
     "Requests sent by any other route will no longer be processed.",
     "\nThe following provisions take effect on 1 {month} {annee} and apply to "
     "all sites, including contractors and temporary staff working on our "
     "premises."],
    ["\nLine managers have five working days to approve or refuse a request. "
     "After that period the request is deemed approved, unless operational "
     "necessity is stated in writing.",
     "\nThis memorandum supersedes all previous instructions on the same "
     "subject. Exceptions are decided case by case by {personne} and confirmed "
     "in writing.",
     "\nPersonal protective equipment must be worn in all marked areas. "
     "Breaches will be recorded in writing and, if repeated, dealt with under "
     "the staff rules."],
    ["\nDepartment heads are asked to bring this memorandum to the attention of "
     "their teams and to display it on the notice boards provided.\n\n"
     "{personne}",
     "\nA register of exceptions is kept and reported quarterly to the board. "
     "No verbal exception is valid.\n\n{personne}",
     "\nQuestions on the application of these rules should be addressed to your "
     "line manager in the first instance.\n\n{personne}"],
]

GENRES["email_en"] = [
    ["Subject: overdue invoice {ref}\n\nDear Sir or Madam,",
     "Subject: order {ref} — confirmation and lead time\n\nDear {personne2},",
     "Subject: short delivery on {jour} {month}\n\nDear Sir or Madam,",
     "Subject: request for quotation — {good}\n\nHello,"],
    ["\nWe write regarding invoice {ref} for {amount} FCFA, which fell due "
     "{delai} days ago. Unless we are mistaken, payment has not reached us.",
     "\nWe acknowledge your order {ref} for {quantite} {unit} of {good}, "
     "totalling {amount} FCFA excluding tax.",
     "\nThe delivery received on {jour} {month} was short by {pct} % against "
     "purchase order {ref}: {quantite} {unit} were delivered instead of the "
     "agreed quantity.",
     "\nOur company, based in {ville}, would like a quotation for {quantite} "
     "{unit} of {good}, delivered to {ville2}."],
    ["\nWe would be grateful if you could arrange settlement within {delai} "
     "days. If payment has been made in the meantime, please send us the "
     "reference so that we can reconcile it.",
     "\nWe confirm despatch from our {ville} warehouse no later than {jour2} "
     "{month}. Transport is arranged by us; goods travel at the consignee's "
     "risk from handover to the carrier.",
     "\nPlease arrange the balance as soon as possible, or issue a credit note. "
     "The missing goods are holding up our own site works in {ville2}.",
     "\nPlease confirm your unit price delivered, lead time and payment terms. "
     "We would welcome a visit to your facilities if your offer is "
     "competitive."],
    ["\nFailing settlement within that period, we would be obliged to suspend "
     "current deliveries in accordance with our terms of sale.",
     "\nAn acknowledgement will follow when the vehicle leaves, together with "
     "the delivery note.",
     "\nWe remain open to an amicable solution and hope this incident will not "
     "affect a relationship that is otherwise satisfactory.",
     "\nPlease reply before {jour2} {month}, when our committee will make its "
     "decision."],
    ["\nWe remain at your disposal for any further information.\n\nKind "
     "regards,\n{personne}\n{societe} — {ville}",
     "\nYours faithfully,\n{personne}\n{societe}, {ville}",
     "\nBest regards,\n{personne}\n{societe}"],
]

GENRES["report_en"] = [
    ["MONTHLY ACTIVITY REPORT — {month} {annee}\n{societe}, {ville}\n\n"
     "1. Summary",
     "QUARTERLY REVIEW\n{societe} — {ville} site\n\n1. Overview",
     "OPERATIONS REPORT — {ville}, {month} {annee}\n\n1. Highlights"],
    ["\nActivity for the month was {amount} FCFA, or {pct} % of target. The "
     "trend remains positive but masks contrasting situations between product "
     "lines.",
     "\nThe quarter closed at {amount} FCFA, up {pct} % year on year. The whole "
     "of that increase is attributable to the second month; the other two were "
     "slightly down.",
     "\nTwo events shaped the period: a {delai}-day supply interruption on "
     "{good}, and the opening of the {ville2} outlet on {jour} {month}."],
    ["\n2. Sales\nVolumes reached {quantite} {unit}, {pct2} % above forecast. "
     "Average selling price eased slightly under competitive pressure on the "
     "{ville} to {ville2} corridor.",
     "\n2. Customers\nActive customers number {effectif}. Three accounts "
     "represent {pct} % of revenue between them, a concentration that bears "
     "watching.",
     "\n2. Market\nDemand for {good} remains firm, with volumes up {pct} %. "
     "Other references were stable and no significant new entrant was "
     "identified."],
    ["\n3. Stock and purchasing\nStock value stands at {amount} FCFA, or "
     "{delai} days of cover. Two references are overstocked and one has been "
     "under continuous tension since the start of the year.",
     "\n3. Supply\nAverage supplier lead time reached {delai} days and is "
     "deteriorating. The long-standing supplier in {ville2} met only {pct} % of "
     "its stated delivery dates.",
     "\n3. Logistics\nTransport cost per tonne rose {pct} %, driven by fuel "
     "prices and longer round trips."],
    ["\n4. Watch list\n— Customer portfolio concentration.\n— Receivables over "
     "{delai} days, now {amount} FCFA.\n— Single-source dependency on {good}.",
     "\n4. Risks\n— A commercial dispute with a customer in {ville2}, {amount} "
     "FCFA at stake.\n— The maintenance contract renewal has not been started.\n"
     "— Two key posts remain vacant.",
     "\n4. Alerts\nThe variance between budget and actual on external charges "
     "reached {pct} %. It is not yet explained and is being analysed."],
    ["\n5. Outlook\n{month} should benefit from favourable seasonality. Subject "
     "to supply tensions easing, the annual target remains reachable.\n\n"
     "Prepared by {personne}.",
     "\n5. Actions under way\nPurchase terms are being renegotiated, two "
     "recruitments have been launched, and a plan to reduce dormant stock will "
     "be presented at the next committee.\n\n{personne}, {ville}.",
     "\n5. Recommendations\nMake deliveries to customers over their credit "
     "limit conditional on payment, open a second source of supply, and review "
     "pricing before quarter end.\n\n{personne}"],
]

GENRES["analysis_en"] = [
    ["ANALYSIS — budget variance, {month} {annee}\n{societe}",
     "NOTE — profitability of the {good} line\n{societe}, {ville}",
     "FEASIBILITY NOTE — opening a depot in {ville2}\n{societe}"],
    ["\nThe budget provided for {amount} FCFA of costs; the actual outturn is "
     "higher. The variance is unfavourable and concentrated on two headings.",
     "\nRevenue on the line is {amount} FCFA against a purchase cost that "
     "leaves a gross margin which must still absorb distribution costs.",
     "\nThe proposed depot requires an initial investment of {amount} FCFA and "
     "annual fixed costs that the analysis below sets out."],
    ["\nFirst heading: transport, {pct} % above budget. Invoice analysis shows "
     "the variance comes largely from three exceptional runs to {ville2}, "
     "authorised to avoid a stock-out at a major customer.",
     "\nUnit cost is {pct} % higher than the figure used to build the price "
     "list, because a purchase price increase was not passed on.",
     "\nBreak-even is reached at {quantite} {unit} a year. On the demand "
     "estimates available, that level would be reached during the second year."],
    ["\nSecond heading: payroll, {pct2} % over budget. Overtime covered two "
     "extended absences and is therefore not structural.",
     "\nSecond factor: average discount granted reached {pct2} %, above target, "
     "mostly on orders processed at month end.",
     "\nThe main sensitivity is the utilisation rate. A ten-point change in "
     "that assumption moves break-even by close to a year, which makes the "
     "decision dependent on a figure we do not control."],
    ["\nRead as a whole, part of the variance is cyclical and will correct "
     "itself; the remainder requires a decision. It would be premature to read "
     "it as a general drift in costs.",
     "\nOverall the line still contributes, but its margin has narrowed. The "
     "question is not whether to keep it but at what price it should be sold "
     "from {month} onwards.",
     "\nThese figures do not settle the matter on their own. They set out the "
     "conditions under which the project would be viable, and those under which "
     "it would not."],
    ["\nRecommendations\n1. Restore prior approval for exceptional transport.\n"
     "2. Leave the payroll budget unchanged until year end.\n3. Bring an "
     "updated analysis to the {month} committee.",
     "\nRecommendations\n1. Revise the price of {good} from 1 {month}.\n"
     "2. Cap the discount that may be granted without approval.\n3. Track unit "
     "cost monthly.",
     "\nNext steps\n1. Confirm the volume assumption with field research in "
     "{ville2}.\n2. Cost a leasing variant.\n3. Defer the decision to the next "
     "financial year."],
]


GENRES["reception_fr"] = [
    ["PROCÈS-VERBAL DE RÉCEPTION N° {ref}\nChantier : {ville2}\nMaître "
     "d'ouvrage : {societe2}\nEntreprise : {societe}\nDate : {jour} {mois} "
     "{annee}",
     "PROCÈS-VERBAL DE RÉCEPTION DES TRAVAUX\nOpération n° {ref} — {ville2}\n"
     "Établi contradictoirement le {jour} {mois} {annee}",
     "PV DE LIVRAISON ET DE MISE EN SERVICE N° {ref}\nSite : {ville2}\n"
     "Fournisseur : {societe}\nDate d'intervention : {jour} {mois} {annee}"],
    ["\nLes opérations de réception se sont déroulées en présence de "
     "{personne}, représentant le maître d'ouvrage, et de {personne2} pour "
     "l'entreprise. Les essais prévus au cahier des charges ont été conduits en "
     "totalité.",
     "\nLa vérification a porté sur la conformité aux spécifications, le bon "
     "fonctionnement des équipements en charge, et la remise des documents "
     "d'exploitation. Chaque point a été contrôlé contradictoirement.",
     "\nOnt participé aux opérations : {personne} pour {societe2}, {personne2} "
     "pour {societe}, ainsi que le bureau de contrôle. Les mesures relevées "
     "figurent en annexe au présent procès-verbal."],
    ["\nÉtat des lieux : {quantite} {unite} de {produit} ont été livrées et "
     "vérifiées. Le comptage contradictoire n'a fait apparaître aucun écart "
     "avec le bon de livraison.",
     "\nConstatations : sur {quantite} {unite} contrôlées, {pct} % sont "
     "conformes sans réserve. Le solde présente des défauts d'aspect sans "
     "incidence sur l'usage.",
     "\nLes essais de fonctionnement ont été satisfaisants. Le rendement mesuré "
     "est conforme à la valeur garantie, avec un écart inférieur à celui admis "
     "par le marché."],
    ["\nRéserves formulées :\n1. Reprise de la signalisation sur la zone de "
     "manœuvre.\n2. Remise du dossier des ouvrages exécutés, non fourni à ce "
     "jour.\n3. Réglage complémentaire à effectuer avant la fin du mois.\n"
     "L'entreprise dispose de {delai} jours pour y remédier.",
     "\nAucune réserve n'est formulée. La réception est prononcée sans réserve "
     "à compter de ce jour, et le délai de garantie court à partir de cette "
     "date.",
     "\nRéserves : le dossier technique reste à compléter et deux points de "
     "finition sont à reprendre. Ces réserves ne font pas obstacle à la mise en "
     "exploitation immédiate."],
    ["\nEn conséquence, la réception est prononcée avec effet au {jour2} "
     "{mois2} {annee}. La retenue de garantie sera libérée après levée des "
     "réserves et à l'expiration du délai contractuel.\n\nSignatures des "
     "parties.",
     "\nLa réception est prononcée sous réserve de la levée des points "
     "ci-dessus. Une visite de contrôle est fixée au {jour2} {mois2}.\n\nFait à "
     "{ville2}, en trois exemplaires.",
     "\nLe présent procès-verbal vaut point de départ des garanties "
     "contractuelles. Il est établi en trois exemplaires, dont un remis à "
     "l'entreprise.\n\n{personne} — {personne2}"],
]

GENRES["appel_offres_fr"] = [
    ["AVIS D'APPEL D'OFFRES N° {ref}\n{societe2}, {ville}\nObjet : fourniture "
     "de {produit}",
     "DOSSIER DE CONSULTATION N° {ref}\nMaître d'ouvrage : {societe2}, {ville}\n"
     "Objet : marché de fournitures et services associés",
     "CONSULTATION RESTREINTE N° {ref}\nAcheteur : {societe2}\nLieu "
     "d'exécution : {ville2}"],
    ["\n1. Objet de la consultation\nLa présente consultation porte sur la "
     "fourniture de {quantite} {unite} de {produit}, livrées à {ville2} selon "
     "un calendrier échelonné sur douze mois.",
     "\n1. Objet\nLe marché a pour objet la fourniture, le transport et la mise "
     "en service de {produit} sur le site de {ville2}. Les prestations de "
     "maintenance associées font l'objet d'un lot séparé.",
     "\n1. Consistance des prestations\nLe titulaire assurera la fourniture de "
     "{quantite} {unite} de {produit}, la formation des utilisateurs et "
     "l'assistance technique pendant la première année."],
    ["\n2. Conditions de participation\nLes candidats devront justifier d'une "
     "expérience d'au moins trois marchés comparables au cours des cinq "
     "dernières années, ainsi que d'une capacité financière suffisante "
     "appréciée au vu des trois derniers exercices.",
     "\n2. Capacités exigées\nLe candidat produira son attestation de "
     "régularité fiscale, son attestation sociale et les références de "
     "prestations similaires exécutées dans la sous-région.",
     "\n2. Recevabilité\nLes offres émanant de groupements sont admises, sous "
     "réserve de désigner un mandataire solidaire. Les candidatures incomplètes "
     "seront écartées sans examen au fond."],
    ["\n3. Critères de jugement\nLes offres seront classées selon la valeur "
     "technique pour {pct} %, le prix pour {pct2} % et le délai de livraison "
     "pour le solde. Une note éliminatoire est prévue sur la conformité "
     "technique.",
     "\n3. Jugement des offres\nLe classement retiendra le prix et la valeur "
     "technique, appréciée au vu du mémoire remis. Toute offre anormalement "
     "basse fera l'objet d'une demande de justification écrite.",
     "\n3. Attribution\nLe marché sera attribué à l'offre économiquement la "
     "plus avantageuse, appréciée sur l'ensemble des critères pondérés annoncés "
     "au règlement de consultation."],
    ["\n4. Remise des offres\nLes plis devront parvenir au plus tard le {jour} "
     "{mois} {annee} à seize heures, à l'adresse indiquée ci-dessus. Les "
     "offres remises hors délai seront retournées sans être ouvertes.",
     "\n4. Dépôt\nLa date limite de remise est fixée au {jour} {mois} {annee}. "
     "Les offres resteront valables {delai} jours à compter de cette date.",
     "\n4. Calendrier\nRemise des offres : {jour} {mois} {annee}. Ouverture des "
     "plis en séance publique le lendemain. Notification prévue dans le mois "
     "suivant."],
    ["\n5. Renseignements\nToute demande de précision est adressée par écrit à "
     "{service}, au plus tard {delai} jours avant la date limite. Les réponses "
     "sont communiquées à l'ensemble des candidats.\n\n{personne}",
     "\n5. Variantes\nLes variantes sont autorisées à condition qu'une offre "
     "de base conforme soit également remise. Aucune négociation n'est prévue "
     "après l'ouverture.\n\n{personne}, {societe2}",
     "\n5. Dispositions diverses\nL'acheteur se réserve le droit de ne pas "
     "donner suite à la consultation, sans que les candidats puissent prétendre "
     "à indemnité.\n\n{personne}"],
]

GENRES["rh_fr"] = [
    ["FICHE DE POSTE\nIntitulé : responsable {service}\nRattachement : "
     "direction générale\nLieu : {ville}\nRéférence : {ref}",
     "OFFRE D'EMPLOI\n{societe} recrute pour son site de {ville}\nPoste : "
     "chargé de mission, {service}\nRéférence : {ref}",
     "DESCRIPTIF DE FONCTION\nEntité : {societe}, {ville}\nFonction : "
     "coordinateur d'exploitation\nRéférence : {ref}"],
    ["\nContexte\n{societe} exerce dans {secteur} et emploie {effectif} "
     "personnes réparties sur deux sites. Le poste est créé pour accompagner la "
     "croissance de l'activité et structurer les procédures internes.",
     "\nEnvironnement\nL'entreprise, présente à {ville} et {ville2}, compte "
     "{effectif} collaborateurs. Le titulaire du poste travaillera en lien "
     "étroit avec {service} et les responsables de site.",
     "\nPrésentation\nAvec {effectif} salariés et une implantation à {ville}, "
     "la société intervient principalement dans {secteur}. Le poste est "
     "rattaché directement à la direction."],
    ["\nMissions principales\n— Piloter l'activité quotidienne et le suivi des "
     "indicateurs.\n— Encadrer une équipe de six personnes.\n— Préparer les "
     "budgets et suivre leur exécution.\n— Représenter l'entreprise auprès des "
     "partenaires locaux.",
     "\nResponsabilités\n— Organiser les approvisionnements et les stocks.\n"
     "— Négocier les conditions d'achat avec les fournisseurs.\n— Garantir le "
     "respect des procédures de sécurité.\n— Rendre compte mensuellement à la "
     "direction.",
     "\nAttributions\n— Assurer le suivi des dossiers clients et des "
     "règlements.\n— Établir les reportings d'activité.\n— Proposer les actions "
     "correctives nécessaires.\n— Participer aux réunions de direction."],
    ["\nProfil recherché\nFormation supérieure en gestion ou équivalent, "
     "assortie d'une expérience d'au moins cinq ans dans une fonction "
     "comparable. La maîtrise du français est indispensable, celle de l'anglais "
     "appréciée.",
     "\nCompétences attendues\nRigueur, capacité d'analyse et sens de "
     "l'organisation. Une expérience du secteur et la pratique des outils de "
     "gestion sont exigées. Le permis de conduire est nécessaire.",
     "\nQualités requises\nAutonomie, aptitude à l'encadrement et goût du "
     "terrain. Une connaissance de la réglementation applicable dans la "
     "sous-région constitue un atout."],
    ["\nConditions\nContrat à durée indéterminée, période d'essai de trois "
     "mois renouvelable une fois. Rémunération selon profil et expérience. "
     "Prise de fonction souhaitée au 1er {mois2} {annee}.",
     "\nModalités\nPoste basé à {ville}, avec des déplacements réguliers vers "
     "{ville2}. Rémunération à négocier. Les candidatures sont reçues jusqu'au "
     "{jour} {mois}.",
     "\nDispositions\nLe poste comporte des astreintes ponctuelles. La prise de "
     "fonction est prévue le {jour} {mois} {annee}. Les dossiers de candidature "
     "sont adressés à {service}."],
]

GENRES["procedure_en"] = [
    ["PROCEDURE {ref2} — purchase order approval\nOwner: finance\nIssue "
     "{annee}.{jour}\nApplies to: all sites",
     "STANDARD OPERATING PROCEDURE {ref2} — goods receipt\nOwner: logistics\n"
     "Effective {jour} {month} {annee}",
     "QUALITY PROCEDURE {ref2} — handling customer complaints\nOwner: "
     "{service}\nRevision {annee}.{jour2}"],
    ["\n1. Purpose\nThis procedure defines how purchase requests are raised, "
     "approved and recorded, so that commitments are visible before they are "
     "made rather than after the invoice arrives.",
     "\n1. Purpose\nThis procedure sets out how incoming goods are checked "
     "against the order and the delivery note, and how discrepancies are "
     "recorded.",
     "\n1. Purpose\nThis procedure describes how customer complaints are "
     "received, investigated and closed, and the records to be kept at each "
     "stage."],
    ["\n2. Scope\nIt applies to all expenditure above {amount} FCFA, at every "
     "site, including purchases made by contractors on the company's behalf. "
     "Emergency purchases are covered by section 6.",
     "\n2. Scope\nIt applies to every delivery received at the {ville} and "
     "{ville2} warehouses, whatever the value, and to direct deliveries to "
     "customer sites.",
     "\n2. Scope\nIt covers complaints received by any channel — letter, "
     "e-mail, telephone or in person — and applies to all staff who deal with "
     "customers."],
    ["\n3. Responsibilities\nThe requester completes the form and states the "
     "budget line. The department head checks the budget. Finance verifies the "
     "supplier is approved. No order leaves the company without both "
     "signatures.",
     "\n3. Responsibilities\nThe storekeeper performs the physical count. The "
     "logistics supervisor authorises acceptance. Any discrepancy above {pct} % "
     "is escalated to {service} the same day.",
     "\n3. Responsibilities\nThe person receiving the complaint records it "
     "within one working day. {service} investigates and proposes a response. "
     "The department head approves any commercial gesture."],
    ["\n4. Steps\n4.1 Raise the request, stating quantity, specification and "
     "required date.\n4.2 Obtain budget approval.\n4.3 Obtain at least two "
     "quotations above {amount} FCFA.\n4.4 Issue the order and file the "
     "acknowledgement.\n4.5 Match invoice, order and delivery note before "
     "payment.",
     "\n4. Steps\n4.1 Check the vehicle seal and the delivery note against the "
     "order.\n4.2 Count and inspect the goods.\n4.3 Record quantities received "
     "and any damage.\n4.4 Sign the note, keeping one copy.\n4.5 Enter the "
     "receipt in the stock record the same day.",
     "\n4. Steps\n4.1 Record the complaint with date, customer and order "
     "reference.\n4.2 Acknowledge receipt within {delai} days.\n4.3 "
     "Investigate and establish the facts.\n4.4 Reply in writing.\n4.5 Close "
     "the file, recording the root cause."],
    ["\n5. Records\nApproved requests, quotations and orders are kept for five "
     "years. The register is reviewed quarterly by {service}, and exceptions "
     "are reported to the board.\n\nApproved: {personne}",
     "\n5. Records\nSigned delivery notes and discrepancy reports are filed for "
     "five years. A monthly summary of discrepancies is produced for {service}."
     "\n\nApproved: {personne}",
     "\n5. Records and review\nThe complaints register is reviewed monthly. "
     "Recurring causes are reported to management with a proposed corrective "
     "action.\n\nApproved: {personne}"],
]

GENRES["policy_en"] = [
    ["INFORMATION SECURITY POLICY {ref2}\n{societe} — {ville}\nApproved by the "
     "board on {jour} {month} {annee}",
     "DATA PROTECTION POLICY {ref2}\n{societe}\nEffective {jour} {month} "
     "{annee}",
     "TRAVEL AND EXPENSES POLICY {ref2}\n{societe}, {ville}\nIssued {jour} "
     "{month} {annee}"],
    ["\n1. Principles\nCompany information is an asset. It is classified as "
     "public, internal or confidential, and handled accordingly. Where a "
     "classification is unclear, the more restrictive treatment applies.",
     "\n1. Principles\nPersonal data is collected only for a stated purpose, "
     "kept only as long as that purpose requires, and disclosed only to those "
     "who need it to do their work.",
     "\n1. Principles\nExpenditure on travel must be necessary, reasonable and "
     "supported by receipts. Where a cheaper option was available and not "
     "taken, the reason is recorded."],
    ["\n2. Access\nAccess rights follow the role, not the person, and are "
     "reviewed when someone changes duties or leaves. Shared accounts are not "
     "permitted. Passwords are not written down or exchanged by e-mail.",
     "\n2. Lawful basis\nPersonal data is processed on the basis of contract, "
     "legal obligation or consent. Consent, where relied on, is recorded and "
     "can be withdrawn.",
     "\n2. Authorisation\nAll travel is authorised in advance by the department "
     "head. Journeys between {ville} and {ville2} follow the standard schedule "
     "of allowances."],
    ["\n3. Devices and premises\nLaptops leaving the premises are encrypted. "
     "Documents classified as confidential are not left on desks overnight or "
     "printed on shared devices without collection.",
     "\n3. Retention\nRecords are retained for the periods set out in the "
     "retention schedule and then destroyed securely. Deletion requests are "
     "handled within {delai} days.",
     "\n3. Limits\nAccommodation is reimbursed up to the ceiling set annually. "
     "Expenditure above {amount} FCFA requires prior written approval, whatever "
     "the category."],
    ["\n4. Incidents\nAny suspected loss or disclosure is reported to "
     "{service} immediately, and in any event within twenty-four hours. Reports "
     "made in good faith carry no sanction, whatever the outcome.",
     "\n4. Breaches\nA breach is reported to {service} without delay and, where "
     "required, to the supervisory authority. A register of breaches is "
     "maintained.",
     "\n4. Claims\nClaims are submitted within {delai} days of return, with "
     "receipts. Late claims may be refused. Claims without receipts are settled "
     "only in exceptional circumstances, on written justification."],
    ["\n5. Compliance\nThis policy applies to employees, contractors and "
     "temporary staff. It is reviewed annually and after any significant "
     "incident.\n\n{personne}, on behalf of the board",
     "\n5. Responsibility\nEvery member of staff is responsible for applying "
     "this policy. {service} monitors compliance and reports annually to the "
     "board.\n\n{personne}",
     "\n5. Review\nThis policy is reviewed each year. Questions on its "
     "application are addressed to {service}.\n\n{personne}"],
]


def document(alea: random.Random, genre: str) -> str:
    """Un document : un décor tiré, puis une formulation tirée par bloc."""
    decor = tirer(alea)
    blocs = GENRES[genre]
    return "\n".join(alea.choice(bloc).format(**decor) for bloc in blocs)


def diversite(texte: str, n: int = 4) -> float:
    """Part de n-grammes distincts. Mesurée, pas supposée : c'est le seul
    garde-fou contre un corpus qui se répéterait sous ses propres gabarits."""
    mots = texte.split()
    if len(mots) <= n:
        return 1.0
    grammes = [" ".join(mots[i:i + n]) for i in range(len(mots) - n + 1)]
    return len(set(grammes)) / len(grammes)


def main() -> int:
    alea = random.Random(GRAINE)
    genres = list(GENRES)
    morceaux: list[str] = []
    octets = 0
    compte: collections.Counter = collections.Counter()

    # Tirage sans remise sur un cycle complet des genres : sur 160 documents,
    # un tirage libre laisserait un genre à 6 exemplaires et un autre à 22.
    while octets < CIBLE_OCTETS:
        tour = genres[:]
        alea.shuffle(tour)
        for genre in tour:
            texte = document(alea, genre)
            morceaux.append(texte)
            compte[genre] += 1
            octets += len(texte.encode("utf-8")) + 2
            if octets >= CIBLE_OCTETS:
                break

    corpus = "\n\n".join(morceaux) + "\n"
    sys.stdout.write(corpus)

    mots = corpus.split()
    print(f"  {len(morceaux)} documents, {len(corpus):,} octets, {len(mots):,} mots",
          file=sys.stderr)
    for genre in sorted(compte):
        print(f"    {genre:<18} {compte[genre]:>3}", file=sys.stderr)
    print(f"  diversité 4-grammes : {diversite(corpus):.3f}", file=sys.stderr)
    fr = sum(v for g, v in compte.items() if g.endswith("_fr"))
    print(f"  français {fr}/{len(morceaux)} documents "
          f"({100 * fr / len(morceaux):.0f} %)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
