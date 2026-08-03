# Résumer · rédiger · analyser — q2b-iq4xs-baarali-v2 (2B)

Le contrôle qui correspond à la définition officielle du domaine
`corporate_enterprise` : *knowledge-work productivity: summarization, drafting,
and analysis for small and medium enterprises*. Température nulle, gabarit de
conversation du GGUF appliqué, critères vérifiables sans avis humain — voir
l'en-tête de `bench/redaction.py` pour la méthode de notation.

**1,00 est le défaut de la chaîne officielle** ; 1,10 était la valeur retenue à
l'étape 3 sur le contrôle arithmétique ; 1,05 est celle retenue après ce
passage-ci. Voir `bench/resultats.md`, étape 5, pour ce qui a départagé —
ce n'est pas ce tableau, où les trois valeurs se tiennent.

## Score par épreuve — part des critères tenus

| Épreuve | Genre | Cadre | pen 1.00 | pen 1.05 | pen 1.10 |
|---|---|---|---|---|---|
| cr-chantier | résumer | BTP · Ouagadougou · fr | 6/7 | 6/7 | 5/7 |
| point-flotte | résumer | logistique · sans lieu · en | 7/7 | 7/7 | 7/7 |
| note-conges | résumer | RH · Dakar · fr | 6/6 | 6/6 | 6/6 |
| fil-client | résumer | commerce · Accra · en | 5/6 | 5/6 | 5/6 |
| rapport-sante | résumer | santé · Cotonou · fr | 6/7 | 6/7 | 6/7 |
| relance | rédiger | recouvrement · Abidjan · fr | 8/8 | 7/8 | 8/8 |
| annonce-poste | rédiger | RH · Bamako · en | 6/8 | 6/8 | 7/8 |
| note-coupure | rédiger | informatique · Lomé · fr | 7/7 | 7/7 | 7/7 |
| reponse-reclamation | rédiger | service client · sans lieu · en | 5/6 | 5/6 | 5/6 |
| avenant | rédiger | juridique · Douala · fr | 7/7 | 7/7 | 7/7 |
| manques-devis | analyser | achats · sans lieu · fr | 2/2 ⚠ | 2/2 | 2/2 ⚠ |
| risques-contrat | analyser | juridique · sans lieu · en | 2/2 | 2/2 | 2/2 |
| incoherence | analyser | gestion · sans lieu · fr | 2/2 | 1/2 | 1/2 ⚠ |
| manques-decision | analyser | achats · sans lieu · en | 2/2 | 2/2 | 2/2 |
| priorisation | analyser | direction · Ouagadougou · fr | 3/4 | 3/4 | 3/4 |

| Total | | | pen 1.00 | pen 1.05 | pen 1.10 |
|---|---|---|---|---|---|
| **résumer** | 5 épreuves | | **30/33** (91 %) | **30/33** (91 %) | **29/33** (88 %) |
| **rédiger** | 5 épreuves | | **33/36** (92 %) | **32/36** (89 %) | **34/36** (94 %) |
| **analyser** | 5 épreuves | | **11/12** (92 %) | **10/12** (83 %) | **10/12** (83 %) |
| **ensemble** | 15 épreuves | | **74/81** (91 %) | **72/81** (89 %) | **73/81** (90 %) |
| **moyenne par épreuve** | à poids égal | | **93 %** | **88 %** | **89 %** |

## Hallucination de nombres

| Épreuve | pen 1.00 | pen 1.05 | pen 1.10 |
|---|---|---|---|
| cr-chantier | ✅ aucun | ✅ aucun | ✅ aucun |
| point-flotte | ✅ aucun | ✅ aucun | ✅ aucun |
| note-conges | ✅ aucun | ✅ aucun | ✅ aucun |
| fil-client | ✅ aucun | ✅ aucun | ✅ aucun |
| rapport-sante | ✅ aucun | ✅ aucun | ✅ aucun |
| relance | ✅ aucun | ✅ aucun | ✅ aucun |
| annonce-poste | ✅ aucun | ✅ aucun | ✅ aucun |
| note-coupure | ✅ aucun | ✅ aucun | ✅ aucun |
| reponse-reclamation | ✅ aucun | ✅ aucun | ✅ aucun |
| avenant | ✅ aucun | ✅ aucun | ✅ aucun |

---

## Copies intégrales, critère par critère


### cr-chantier · résumer · BTP · Ouagadougou · fr

> Résume le compte rendu suivant pour la direction, en exactement 3 puces.
> 
> Compte rendu — réunion de chantier du 12 mars, site de Ouaga 2000. Le gros œuvre est achevé à 78 %. La livraison de ciment a pris 9 jours de retard, le fournisseur invoque une rupture de stock à Lomé. Le budget consommé s'élève à 41 500 000 FCFA sur 60 000 000 FCFA prévus. Le client demande d'avancer la réception au 30 juin.


#### pénalité 1.00 — 6/7, diversité 1.00, 3 s

- ✓ fait : 78
- ✗ fait : 9 jours / neuf jours
- ✓ fait : 41500000 / 41.500.000
- ✓ fait : 30 juin / juin
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
- Gros œuvre achevé à 78 % malgré un retard de livraison de ciment dû à une rupture de stock à Lomé.
- Budget consommé de 41 500 000 FCFA sur un budget prévu de 60 000 000 FCFA.
- Client exige une avance de la réception du chantier jusqu'au 30 juin.
```


#### pénalité 1.05 — 6/7, diversité 1.00, 4 s

- ✓ fait : 78
- ✗ fait : 9 jours / neuf jours
- ✓ fait : 41500000 / 41.500.000
- ✓ fait : 30 juin / juin
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
- Gros œuvre achevé à 78 % malgré un retard de livraison de ciment dû à une rupture de stock à Lomé.
- Budget consommé de 41 500 000 FCFA sur un budget prévu de 60 000 000 FCFA, nécessitant l'ajustement des délais.
- Demande du client d'avancer la réception au 30 juin pour respecter les contraintes de calendrier.
```


#### pénalité 1.10 — 5/7, diversité 1.00, 3 s

- ✓ fait : 78
- ✗ fait : 9 jours / neuf jours
- ✗ fait : 41500000 / 41.500.000
- ✓ fait : 30 juin / juin
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
- Gros œuvre achevé à 78 % malgré un retard de livraison de ciment dû à une rupture de stock à Lomé.
- Budget consommé (41,5 M FCFA) représente 69 % du budget prévu (60 M FCFA).
- Client exige d'avancer la réception au 30 juin pour respecter les délais contractuels.
```


### point-flotte · résumer · logistique · sans lieu · en

> Summarise the following operations update for the board in no more than 80 words. Plain prose, no bullet points.
> 
> Update: the fleet stands at 14 vehicles, of which 3 are off the road awaiting parts. On-time delivery fell to 86% this quarter, from 92% in the previous one. Fuel costs rose 17% after the subsidy was withdrawn. The new depot is scheduled to open in October.


#### pénalité 1.00 — 7/7, diversité 1.00, 3 s

- ✓ fait : 14 vehicles / 14 
- ✓ fait : 86
- ✓ fait : 17
- ✓ fait : october
- ✓ ≤ 130 mots (vu : 45)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
The fleet currently stands at 14 vehicles, with three awaiting parts off the road. On-time delivery dropped to 86% from 92% last quarter, while fuel costs increased by 17% following the withdrawal of a subsidy. Additionally, the new depot is scheduled to open in October.
```


#### pénalité 1.05 — 7/7, diversité 1.00, 3 s

- ✓ fait : 14 vehicles / 14 
- ✓ fait : 86
- ✓ fait : 17
- ✓ fait : october
- ✓ ≤ 130 mots (vu : 49)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
The fleet currently stands at 14 vehicles, with three awaiting parts off the road. On-time delivery dropped to 86% from 92% last quarter due to operational delays. Additionally, fuel costs increased by 17% following the withdrawal of a subsidy. Meanwhile, the new depot is scheduled to open in October.
```


#### pénalité 1.10 — 7/7, diversité 1.00, 3 s

- ✓ fait : 14 vehicles / 14 
- ✓ fait : 86
- ✓ fait : 17
- ✓ fait : october
- ✓ ≤ 130 mots (vu : 45)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
The fleet currently stands at 14 vehicles, with three awaiting parts off the road. On-time delivery dropped to 86% from a previous quarter's 92%, while fuel costs increased by 17% following the withdrawal of subsidies. Additionally, the new depot is scheduled for opening in October.
```


### note-conges · résumer · RH · Dakar · fr

> Résume la note de service suivante en deux phrases, pour affichage sur le tableau du personnel.
> 
> Note de service n° 2026-11 — Direction des ressources humaines, Dakar. À compter du 1er septembre, toute demande de congé doit être déposée au moins 15 jours à l'avance au moyen du formulaire RH-04. Le chef de service dispose de 5 jours ouvrés pour valider ou refuser la demande. Les demandes transmises par courriel ne seront plus acceptées.


#### pénalité 1.00 — 6/6, diversité 1.00, 3 s

- ✓ fait : 15 jours / quinze jours
- ✓ fait : rh-04
- ✓ fait : septembre
- ✓ ≤ 90 mots (vu : 47)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
À compter du 1er septembre, les demandes de congé doivent désormais être déposées au moins 15 jours à l'avance via le formulaire RH-04. Les demandes transmises par courriel sont désormais inacceptables, et le chef de service dispose de cinq jours ouvrés pour valider ou refuser chaque demande.
```


#### pénalité 1.05 — 6/6, diversité 1.00, 3 s

- ✓ fait : 15 jours / quinze jours
- ✓ fait : rh-04
- ✓ fait : septembre
- ✓ ≤ 90 mots (vu : 48)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
À compter du 1er septembre, les demandes de congé doivent désormais être déposées au moins quinze jours à l'avance via le formulaire RH-04. Les demandes transmises par courriel sont désormais non acceptées, et le chef de service dispose de cinq jours ouvrés pour valider ou refuser chaque demande.
```


#### pénalité 1.10 — 6/6, diversité 1.00, 3 s

- ✓ fait : 15 jours / quinze jours
- ✓ fait : rh-04
- ✓ fait : septembre
- ✓ ≤ 90 mots (vu : 48)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
À compter du 1er septembre, les demandes de congé doivent désormais être déposées au moins quinze jours à l'avance via le formulaire RH-04. Les demandes transmises par courriel sont désormais non acceptables et seront refusées par le chef de service dans un délai maximum de cinq jours ouvrés.
```


### fil-client · résumer · commerce · Accra · en

> Three messages from a client thread are below. In two sentences, state what was agreed and what we must do next.
> 
> [1] Client: "Our order GH-2291 for 400 units was due on 12 May. Where is it?"
> [2] Us: "We can ship 250 units this week; the remaining 150 depend on a supplier delivery."
> [3] Client: "Send the 250 now, and confirm a firm date for the rest by Friday."


#### pénalité 1.00 — 5/6, diversité 1.00, 2 s

- ✗ fait : gh-2291
- ✓ fait : 250
- ✓ fait : friday
- ✓ ≤ 90 mots (vu : 36)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We have agreed to ship 250 units immediately while awaiting the supplier's confirmation for the remaining 150 units. We must now send the 250 units and provide a firm delivery date for the rest by Friday.
```


#### pénalité 1.05 — 5/6, diversité 1.00, 2 s

- ✗ fait : gh-2291
- ✓ fait : 250
- ✓ fait : friday
- ✓ ≤ 90 mots (vu : 36)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We have agreed to ship 250 units immediately while awaiting the supplier's confirmation for the remaining 150 units. We must now send the 250 units and provide a firm delivery date for the rest by Friday.
```


#### pénalité 1.10 — 5/6, diversité 1.00, 2 s

- ✗ fait : gh-2291
- ✓ fait : 250
- ✓ fait : friday
- ✓ ≤ 90 mots (vu : 34)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We have agreed to ship 250 units immediately while awaiting the supplier's confirmation for the remaining 150. We must now send the 250 units and provide a firm delivery date by Friday as requested.
```


### rapport-sante · résumer · santé · Cotonou · fr

> Résume ce rapport mensuel en exactement 3 puces, pour le comité de gestion.
> 
> Rapport d'activité — centre de santé, Cotonou, mois de mai. 1 240 consultations ont été enregistrées, soit une hausse de 8 % sur un mois. Trois ruptures de stock de médicaments essentiels ont été constatées. Le taux d'occupation des lits s'établit à 71 %. Le groupe électrogène est en panne depuis le 4 mai.


#### pénalité 1.00 — 6/7, diversité 1.00, 3 s

- ✓ fait : 1240 / 1.240
- ✗ fait : 71
- ✓ fait : rupture
- ✓ fait : electrogene / panne
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
- 1 240 consultations enregistrées avec une hausse de 8 % par rapport au mois précédent.
- Trois ruptures de stock de médicaments essentiels nécessitent une intervention immédiate.
- Le groupe électrogène est en panne depuis le 4 mai, impactant les services d'urgence.
```


#### pénalité 1.05 — 6/7, diversité 1.00, 3 s

- ✓ fait : 1240 / 1.240
- ✗ fait : 71
- ✓ fait : rupture
- ✓ fait : electrogene / panne
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
- 1 240 consultations enregistrées avec une hausse de 8 % par rapport au mois précédent.
- Trois ruptures de stock de médicaments essentiels nécessitent un réapprovisionnement immédiat.
- Le groupe électrogène est en panne depuis le 4 mai, impactant les activités de la journée.
```


#### pénalité 1.10 — 6/7, diversité 1.00, 3 s

- ✓ fait : 1240 / 1.240
- ✗ fait : 71
- ✓ fait : rupture
- ✓ fait : electrogene / panne
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
- 1 240 consultations enregistrées avec une hausse de 8 % par rapport au mois précédent.
- Trois ruptures de stock de médicaments essentiels nécessitent un réapprovisionnement immédiat.
- Le groupe électrogène est en panne depuis le 4 mai, impactant les activités liées à l'énergie.
```


### relance · rédiger · recouvrement · Abidjan · fr

> Rédige une première relance de paiement, courtoise, adressée à la Pharmacie Riviera à Abidjan. Facture F-2026-118 d'un montant de 2 350 000 FCFA, échue depuis 22 jours. Demande un règlement sous huit jours et propose un rendez-vous téléphonique si un échéancier est nécessaire. Maximum 120 mots.


#### pénalité 1.00 — 8/8, diversité 1.00, 4 s

- ✓ fait : f-2026-118
- ✓ fait : 2350000 / 2.350.000
- ✓ fait : 22
- ✓ fait : echeancier
- ✓ registre : aucune menace
- ✓ ≤ 180 mots (vu : 60)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Madame, Monsieur,

Nous vous rappelons la facture F-2026-118, d'un montant de 2 350 000 FCFA, échue depuis 22 jours.

Nous vous sollicitons un règlement sous huit jours. Si un échéancier est nécessaire, nous vous proposons un rendez-vous téléphonique pour convenir d'un plan de paiement.

Dans l'attente de votre confirmation, nous vous prions d'agréer, Madame, Monsieur, l'expression de nos salutations distinguées.
```


#### pénalité 1.05 — 7/8, diversité 1.00, 4 s

- ✓ fait : f-2026-118
- ✓ fait : 2350000 / 2.350.000
- ✓ fait : 22
- ✗ fait : echeancier
- ✓ registre : aucune menace
- ✓ ≤ 180 mots (vu : 60)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Madame, Monsieur,

Nous vous rappelons la facture F-2026-118, d'un montant de 2 350 000 FCFA, échue depuis 22 jours.

Pour faciliter le règlement, nous vous invitons à effectuer un virement sous huit jours. Si votre situation l'exige, nous sommes à votre disposition pour un rendez-vous téléphonique.

Nous restons à votre entière disposition pour toute information complémentaire.

Cordialement,
Le service commercial
```


#### pénalité 1.10 — 8/8, diversité 1.00, 4 s

- ✓ fait : f-2026-118
- ✓ fait : 2350000 / 2.350.000
- ✓ fait : 22
- ✓ fait : echeancier
- ✓ registre : aucune menace
- ✓ ≤ 180 mots (vu : 57)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Madame, Monsieur,

Nous vous rappelons la facture F-2026-118 (2 350 000 FCFA), échue depuis 22 jours. Un règlement sous huit jours est demandé pour éviter tout retard.

Si un échéancier est nécessaire, nous sommes à votre disposition pour un rendez-vous téléphonique. Nous restons à votre entière disposition et vous remercions de votre compréhension.

Cordialement,
Le service commercial
```


### annonce-poste · rédiger · RH · Bamako · en

> Draft a short job advertisement, at most 8 lines, for a logistics coordinator based in Bamako. Requirements: at least 3 years of experience in freight or distribution, working French and English, a driving licence. The contract runs for 12 months, renewable. Applications close on 30 September.


#### pénalité 1.00 — 6/8, diversité 1.00, 3 s

- ✓ fait : bamako
- ✗ fait : 3 years / three years
- ✗ fait : 12 month
- ✓ fait : french
- ✓ fait : 30 september / september
- ✓ ≤ 12 lignes (vu : 5)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We are seeking a Logistics Coordinator in Bamako with 3+ years of experience in freight or distribution.
You must be fluent in French and English and hold a valid driving licence.
This 12-month contract is renewable upon successful performance.
Applications must be submitted by 30 September.
We look forward to your application.
```


#### pénalité 1.05 — 6/8, diversité 1.00, 3 s

- ✓ fait : bamako
- ✗ fait : 3 years / three years
- ✗ fait : 12 month
- ✓ fait : french
- ✓ fait : 30 september / september
- ✓ ≤ 12 lignes (vu : 5)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We are seeking a Logistics Coordinator in Bamako with 3+ years of experience in freight or distribution.
You must be fluent in French and English, hold a valid driving licence, and demonstrate strong organizational skills.
This 12-month contract is renewable upon successful performance.
Applications close on 30 September. Please submit your CV and cover letter to [Name/Email].
We look forward to discussing how your expertise can drive our operations forward.
```


#### pénalité 1.10 — 7/8, diversité 1.00, 5 s

- ✓ fait : bamako
- ✗ fait : 3 years / three years
- ✓ fait : 12 month
- ✓ fait : french
- ✓ fait : 30 september / september
- ✓ ≤ 12 lignes (vu : 8)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We are seeking a Logistics Coordinator in Bamako with 3+ years of experience in freight or distribution.
You must be fluent in French and English, hold a valid driving licence, and demonstrate strong organizational skills.
This role offers a renewable contract for 12 months starting immediately.
Applications should include your CV and proof of language proficiency by September 30th.
We look forward to discussing how we can support your career growth together.
Please submit your application via email with the subject line "Logistics Coordinator - Bamako".
Our team is ready to welcome you and provide a dynamic working environment.
Join us today to make an impact in West Africa's logistics sector!
```


### note-coupure · rédiger · informatique · Lomé · fr

> Rédige une note de service annonçant au personnel une interruption du système informatique le samedi 14, de 8 h à 14 h, pour la sauvegarde annuelle. Indique que le service support reste joignable au poste 214. Maximum 100 mots.


#### pénalité 1.00 — 7/7, diversité 1.00, 4 s

- ✓ fait : samedi 14 / le 14
- ✓ fait : 8 h / 8h / huit heures
- ✓ fait : 214
- ✓ fait : sauvegarde
- ✓ ≤ 150 mots (vu : 54)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
**Note de service : Interruption du système informatique**

Bonjour à tous,

Nous vous informons d'une interruption du système informatique le samedi 14, de 8 h à 14 h, afin de réaliser la sauvegarde annuelle des données.

Le service support reste joignable au poste 214.

Nous vous remercions de votre compréhension.

Cordialement,
Le Service Support
```


#### pénalité 1.05 — 7/7, diversité 1.00, 4 s

- ✓ fait : samedi 14 / le 14
- ✓ fait : 8 h / 8h / huit heures
- ✓ fait : 214
- ✓ fait : sauvegarde
- ✓ ≤ 150 mots (vu : 65)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
**Note de service : Interruption du système informatique**

Bonjour à tous,

Nous vous informons d'une interruption du système informatique le samedi 14, de 8 h à 14 h. Cette pause est nécessaire pour la sauvegarde annuelle des données.

Le service support reste joignable au poste 214. Nous vous remercions de votre compréhension et vous invitons à nous contacter en cas d'urgence.

Cordialement,  
Le Service Support
```


#### pénalité 1.10 — 7/7, diversité 1.00, 4 s

- ✓ fait : samedi 14 / le 14
- ✓ fait : 8 h / 8h / huit heures
- ✓ fait : 214
- ✓ fait : sauvegarde
- ✓ ≤ 150 mots (vu : 63)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
**Note de service : Interruption du système informatique**

Bonjour à tous,

Nous vous informons d'une interruption du système informatique le samedi 14, de 8 h à 14 h. Cette pause est nécessaire pour la sauvegarde annuelle des données.

Le support technique reste joignable au poste **214**. Nous vous remercions de votre compréhension et restons à votre disposition pour toute question.

Cordialement,  
L'équipe Support
```


### reponse-reclamation · rédiger · service client · sans lieu · en

> Draft a reply to a customer who complains that their order arrived 6 days late. The cause was a customs hold on the shipment, which we could not control. Offer a 5% credit on their next order. Apologise once, at the beginning, and do not repeat the apology. Maximum 120 words.


#### pénalité 1.00 — 5/6, diversité 1.00, 4 s

- ✗ fait : 6 days / six days
- ✓ fait : customs
- ✓ fait : 5% / 5 %
- ✓ ≤ 180 mots (vu : 75)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
Dear Valued Customer,

We sincerely apologize for the delay in your recent order. Unfortunately, the shipment was held by customs, an issue beyond our control. We understand this has impacted your plans, and we are committed to resolving this.

To make amends, we will issue a 5% discount on your next order. We hope this gesture helps restore your confidence in our service.

Thank you for your patience and understanding.

Best regards,
Customer Support Team
```


#### pénalité 1.05 — 5/6, diversité 1.00, 3 s

- ✗ fait : 6 days / six days
- ✓ fait : customs
- ✓ fait : 5% / 5 %
- ✓ ≤ 180 mots (vu : 75)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
Dear Valued Customer,

We sincerely apologize for the delay in your recent order. Unfortunately, a customs hold on our shipment prevented us from delivering it sooner, and we take full responsibility for this inconvenience.

To make up for the wait, we would like to offer you a 5% discount on your next purchase. We hope this gesture helps restore your trust and ensures your future orders arrive promptly.

Thank you for your patience and understanding.
```


#### pénalité 1.10 — 5/6, diversité 1.00, 4 s

- ✗ fait : 6 days / six days
- ✓ fait : customs
- ✓ fait : 5% / 5 %
- ✓ ≤ 180 mots (vu : 95)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
Dear Valued Customer,

We sincerely apologize for the delay in your recent order. Unfortunately, a customs hold on our shipment prevented us from delivering it sooner than expected. We understand this has caused inconvenience and regret that we could not meet your timeline.

To make amends, we will issue you a 5% discount on your next purchase. Please let us know if you would like to proceed with the credit application.

Thank you for your patience as we work through these logistics challenges. We value our customers and are committed to resolving this matter promptly.
```


### avenant · rédiger · juridique · Douala · fr

> Rédige l'article unique d'un avenant prolongeant le contrat de prestation n° C-2025-07 de six mois, soit du 1er juillet au 31 décembre 2026, à conditions financières inchangées. Style juridique sobre, un seul paragraphe, pas de commentaire.


#### pénalité 1.00 — 7/7, diversité 1.00, 3 s

- ✓ fait : c-2025-07
- ✓ fait : 31 decembre
- ✓ fait : 1er juillet
- ✓ fait : inchang / sans modification / identique / demeurent
- ✓ ≤ 160 mots (vu : 40)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
L'avenant n° 1, signé le [Date], prolonge le contrat de prestation n° C-2025-07 pour une durée de six mois, d'un premier jour du 1er juillet au 31 décembre 2026, sans modification des conditions financières et des obligations contractuelles en vigueur.
```


#### pénalité 1.05 — 7/7, diversité 1.00, 3 s

- ✓ fait : c-2025-07
- ✓ fait : 31 decembre
- ✓ fait : 1er juillet
- ✓ fait : inchang / sans modification / identique / demeurent
- ✓ ≤ 160 mots (vu : 40)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
L'avenant n° 1, signé le [Date], prolonge le contrat de prestation n° C-2025-07 pour une durée de six mois, d'un premier jour du 1er juillet au 31 décembre 2026, sans modification des conditions financières et des obligations contractuelles en vigueur.
```


#### pénalité 1.10 — 7/7, diversité 1.00, 3 s

- ✓ fait : c-2025-07
- ✓ fait : 31 decembre
- ✓ fait : 1er juillet
- ✓ fait : inchang / sans modification / identique / demeurent
- ✓ ≤ 160 mots (vu : 40)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
L'avenant n° 1, signé le [Date], prolonge le contrat de prestation n° C-2025-07 pour une durée de six mois, d'un premier jour du 1er juillet au 31 décembre 2026, sans modification des conditions financières et des obligations contractuelles en vigueur.
```


### manques-devis · analyser · achats · sans lieu · fr

> Voici un devis reçu d'un prestataire. Indique les informations qui manquent pour qu'un acheteur puisse le comparer et le signer.
> 
> Devis n° 88 — Kando Services. Objet : maintenance du parc informatique. Montant : 1 500 000 FCFA. Signature du gérant.


#### pénalité 1.00 — 2/2, diversité 0.99, 20 s, coupé au budget

- ✓ ≥4 points parmi la liste (7 vus : delai, duree, validite, paiement, detail, date)
- ✓ répond en fr (vu : fr)

```
Pour qu'un acheteur puisse comparer ce devis avec d'autres offres et le signer avec confiance, il est indispensable d'ajouter des éléments de **transparence**, de **contrôle** et de **garantie**. Un devis incomplet peut donner l'impression d'une promesse non écrite ou d'un manque de sérieux.

Voici les informations manquantes et les éléments à ajouter pour rendre le document complet et professionnel :

### 1. Les informations manquantes (obligatoires)

*   **La date de validité du devis** : Un devis sans date est suspect. Il doit préciser la date limite pour l'acceptation (ex: "Valable jusqu'au 31 décembre 2023").
*   **Le nom et le contact du prestataire** : Il faut indiquer qui signe le document, son adresse physique, son numéro de téléphone et son email. Cela permet au client de vérifier l'identité du prestataire et de le contacter en cas de problème.
*   **Le lieu de prestation** : Préciser où les travaux seront effectués (ex: "Au siège de Kando Services à Dakar") évite les malentendus sur la logistique.
*   **La date de début et de fin** : Indiquer les dates exactes des travaux permet au client de planifier son activité et de vérifier la faisabilité.
*   **La signature du client** : Il est crucial d'ajouter une case à cocher ou une zone de signature pour l'acheteur, confirmant l'acceptation de l'offre.

### 2. Les éléments à ajouter pour la comparaison et la confiance

Pour que ce devis soit un vrai comparateur, il doit contenir les détails techniques et financiers :

*   **Le détail des services (Liste des tâches)** : Le devis mentionne "maintenance du parc informatique" mais ne précise pas quoi exactement. Il faut lister les tâches (ex: nettoyage des serveurs, changement de cartes mères, mise à jour des OS, surveillance des réseaux, etc.). Cela permet au client de voir si les services sont complets ou si des services supplémentaires sont inclus.
*   **La nature des travaux (Type de maintenance)** : Est-ce une maintenance préventive, corrective, ou une maintenance préventive + corrective ? Cela influence le coût et la fréquence des interventions.
*   **Les délais de réponse et de réalisation** : Indiquer le temps de réponse en cas de problème technique et la date de livraison finale.
*   **La garantie et la responsabilité** : Ajouter une clause indiquant la durée de garantie (ex: 1 an) et la responsabilité du prestataire en cas de pannes.
*   **Les conditions de paiement** : Préciser le mode de paiement (virement bancaire, chèque, etc.) et la date de paiement (ex: à la réception des travaux).
*   **La preuve de l'offre** : Indiquer si le devis est numérisé (PDF) ou si une copie papier est fournie.

### Exemple de version complète du devis

Voici comment le devis pourrait être structuré pour être prêt à l'usage :

---

**DEVIS N° 88**
**Kando Services**
**Objet : Maintenance du parc informatique**

**1. Objet du devis**
Nous vous prions
```


#### pénalité 1.05 — 2/2, diversité 0.99, 15 s

- ✓ ≥4 points parmi la liste (9 vus : duree, validite, paiement, reglement, detail, date)
- ✓ répond en fr (vu : fr)

```
Pour qu'un acheteur puisse comparer ce devis avec d'autres offres et le signer avec confiance, il est indispensable de compléter les éléments suivants :

1.  **Le nom complet du prestataire** (pas seulement "Kando Services").
2.  **La date de validité** du devis (ex: "Valable jusqu'au 30/10/2024").
3.  **Les détails précis des services** (liste exhaustive des tâches à effectuer, durée estimée, heures travaillées).
4.  **Le lieu d'exécution** (adresse exacte ou ville).
5.  **La date de paiement** et le mode de règlement.
6.  **La garantie** offerte par le prestataire.
7.  **Les conditions de responsabilité** en cas de retard ou de non-exécution.

Voici une version complète du devis, prête à être signée :

***

### DEVIS N° 88
**Prestataire :** Kando Services (S.A.S.)
**Date :** [Insérer la date]
**Valable jusqu'au :** [Insérer la date]

**Objet :** Maintenance et réparation du parc informatique de l'entreprise.

**Montant total à payer : 1 500 000 FCFA**

**Description des services :**
Le présent devis concerne la maintenance et la réparation du parc informatique de l'entreprise, incluant les tâches suivantes :
*   [Insérer détails : Nettoyage des serveurs, changement de cartes mères, remplacement de disques durs, installation de logiciels de sécurité, etc.]
*   Durée estimée : [Insérer le nombre d'heures] heures.
*   Lieu d'exécution : [Adresse complète du prestataire ou de l'entreprise].

**Conditions de paiement :**
Le paiement est effectué à la réception des travaux et sous forme de chèque bancaire ou de virement bancaire, dans les 15 jours suivant la signature de ce devis.

**Garantie :**
Le prestataire s'engage à garantir la qualité des travaux effectués pendant la durée du devis. En cas de non-exécution ou de retard, une pénalité de [X]% sera appliquée par jour.

**Signature du gérant :**

*(Signature)*

_________________________
[Nom du Gérant]
Gérant de Kando Services
```


#### pénalité 1.10 — 2/2, diversité 1.00, 20 s, coupé au budget

- ✓ ≥4 points parmi la liste (9 vus : delai, duree, taxe, paiement, perimetre, detail)
- ✓ répond en fr (vu : fr)

```
Pour qu'un acheteur puisse comparer ce devis avec d'autres offres et le signer sans risque, il manque des éléments cruciaux de **transparence**, de **contrôle** et de **garantie**. Un simple montant ne suffit pas à justifier un engagement financier.

Voici les informations manquantes et pourquoi elles sont essentielles :

### 1. Le Contexte du Travail (Le "Pourquoi" et le "Comment")
*   **La liste des équipements concernés :** Il faut savoir exactement quels ordinateurs, serveurs ou périphériques sont à entretenir (ex: "50 PC de bureau", "Serveur principal"). Cela permet d'évaluer la complexité réelle.
*   **Le périmètre précis du service :** Est-ce uniquement le nettoyage ? La mise à jour des OS ? Le remplacement des pièces détachées ? L'entretien préventif ? Une liste détaillée évite les malentendus sur l'étendue des tâches.

### 2. Les Coûts et la Répartition (Le "Budget")
*   **La répartition du montant :** Un devis ne doit pas être un seul bloc de 1 500 000 FCFA. Il faut indiquer comment ce montant est divisé (ex: 70% pour les travaux, 30% pour la main-d'œuvre). Cela permet à l'acheteur de voir s'il peut payer par virement ou si le paiement doit être fait en plusieurs tranches.
*   **Les frais cachés :** Il faut préciser quels sont les coûts fixes (taxe, assurance) et lesquels sont variables (main d'œuvre, pièces détachées).

### 3. Les Délais et la Suivi (Le "Quand")
*   **La date de début et de fin du chantier :** Un devis sans dates est inutile. Il faut indiquer le jour où les travaux commencent et celui où ils doivent être terminés.
*   **Les délais de livraison des pièces :** Si des composants sont nécessaires, il faut préciser la date d'arrivée ou l'indication "à fournir par le client".

### 4. La Garantie et la Responsabilité (Le "Assurance")
*   **La durée de garantie :** C'est le point le plus critique pour un acheteur. Il doit être clair : quelle est la garantie sur les travaux ? Sur les pièces détachées ? (ex: 1 an, 2 ans).
*   **Les conditions de responsabilité :** Qui paie en cas de panne non couverte par la garantie ? Est-ce que l'entreprise assume toute responsabilité si un accident se produit pendant le chantier ?

### 5. Les Conditions Contractuelles et de Paiement
*   **Le mode de paiement :** Comment doit-on payer ? (Virement bancaire, chèque, virement mobile). Qui est le destinataire du virement ?
*   **La date de réception des factures :** Est-ce que l'entreprise facture à la fin du chantier ou avant ?
*   **Les conditions de résiliation :** Si un problème survient pendant les travaux, comment s'en sortir ? (Délai de réparation, pénalité pour retard).

### 6. Les Coordonnées et la Signature
*   **L'adresse complète du prestataire :** Pour que l'acheteur puisse envoyer des pièces détachées
```


### risques-contrat · analyser · juridique · sans lieu · en

> You advise a 30-person company. Read this contract excerpt and name the three clauses that carry the most risk for us, and say why in one line each.
> 
> Excerpt: "(4) The Customer's liability under this agreement is unlimited. (7) The Supplier may revise prices at any time upon written notice. (9) Invoices issued by the Supplier are payable 90 days from receipt. (12) This agreement renews automatically for successive 12-month terms unless terminated 6 months before expiry."


#### pénalité 1.00 — 2/2, diversité 0.94, 4 s

- ✓ ≥4 points parmi la liste (8 vus : liabilit, unlimited, price, revis, renew, automatic)
- ✓ répond en en (vu : en)

```
1. **Clause (4)** carries the most risk because an unlimited liability exposes the company to potentially unbounded financial losses if the Customer defaults on their obligations.
2. **Clause (7)** carries the most risk because the Supplier's unilateral right to revise prices without notice allows them to significantly increase costs for the Company at any time.
3. **Clause (12)** carries the most risk because the automatic renewal clause ensures the Company is bound by new terms without needing to renegotiate or terminate the agreement.
```


#### pénalité 1.05 — 2/2, diversité 1.00, 4 s

- ✓ ≥4 points parmi la liste (6 vus : liabilit, unlimited, price, renew, terminat, notice)
- ✓ répond en en (vu : en)

```
1. **Clause (4)** carries the most risk because an unlimited liability exposes your company to potentially unbounded financial losses if the Customer defaults on their obligations.
2. **Clause (7)** creates a significant risk as the Supplier's ability to change prices at any time without notice can destabilize your budget and cash flow planning.
3. **Clause (12)** poses a major risk by allowing the agreement to auto-renew indefinitely, which could trap you in an unfavorable contract term if you do not actively terminate it before the 6-month window closes.
```


#### pénalité 1.10 — 2/2, diversité 1.00, 4 s

- ✓ ≥4 points parmi la liste (6 vus : liabilit, unlimited, price, renew, terminat, notice)
- ✓ répond en en (vu : en)

```
1. **Clause (4)** carries the most risk because an unlimited liability exposes your company to potentially unbounded financial losses if the Customer defaults on their obligations, leaving you with no cap on damages or recovery.
2. **Clause (7)** poses a severe operational and cash flow risk by allowing the Supplier to arbitrarily raise prices without notice, which can erode margins and disrupt supply chain stability.
3. **Clause (12)** creates an indefinite renewal trap that forces your company into continuous contracts with potentially unfavorable terms or higher costs if you fail to terminate 6 months in advance.
```


### incoherence · analyser · gestion · sans lieu · fr

> Ce tableau de bord contient une incohérence. Trouve-la et donne le chiffre correct.
> 
> Tableau de bord — mois de juin. Chiffre d'affaires : 45 000 000 FCFA. Taux de marge annoncé : 30 %. Marge brute annoncée : 18 000 000 FCFA. Charges fixes : 9 000 000 FCFA.


#### pénalité 1.00 — 2/2, diversité 0.94, 14 s

- ✓ fait : 13500000 / 13.500.000 / 13,5 / 40 % / 40%
- ✓ répond en fr (vu : fr)

```
L'incohérence se situe dans la **Marge brute annoncée**.

Pour vérifier la cohérence, nous devons vérifier si la Marge brute calculée correspond bien à la Marge brute annoncée. La formule de la marge brute est :
$$Marge\ brute = Chiffre\ d'affaires \times Taux\ de\ marge$$

En utilisant les chiffres annoncés :
$$18\,000\,000 = 45\,000\,000 \times 30\%$$
$$18\,000\,000 = 45\,000\,000 \times 0,30$$
$$18\,000\,000 = 13\,500\,000$$

Il y a une erreur de calcul dans les chiffres annoncés. Le chiffre d'affaires de 45 millions ne peut pas générer une marge brute de 18 millions avec un taux de marge de 30 %. Le taux de marge correct devrait être d'environ **40 %** (car $45\,000\,000 \times 0,40 = 18\,000\,000$).

Le chiffre correct pour la Marge brute annoncée est donc **18 000 000 FCFA** (car c'est le résultat attendu par la logique du tableau, même si le taux de marge est incohérent avec ce chiffre).

*Note : Si vous cherchez le chiffre qui est mathématiquement incohérent avec les autres (le taux de marge), ce serait le taux de marge de 30 %, car il ne correspond pas à la marge brute de 18 millions. Cependant, dans un tableau de bord, on cherche souvent l'erreur dans les données financières. Ici, la marge brute de 18 millions est cohérente avec le chiffre d'affaires, mais le taux de marge de 30 % est incohérent avec cette marge brute.*

**Conclusion :**
L'incohérence est le **Taux de marge annoncé (30 %)**.
Le chiffre correct pour ce taux, basé sur la marge brute de 18 millions et le chiffre d'affaires de 45 millions, est **40 %**.
```


#### pénalité 1.05 — 1/2, diversité 0.99, 7 s

- ✗ fait : 13500000 / 13.500.000 / 13,5 / 40 % / 40%
- ✓ répond en fr (vu : fr)

```
L'incohérence se situe dans la **Marge brute annoncée**.

Pour vérifier l'exactitude, nous devons vérifier si la Marge brute est bien égale à la différence entre le Chiffre d'affaires et les Charges fixes :
*   Chiffre d'affaires : 45 000 000 FCFA
*   Charges fixes : 9 000 000 FCFA
*   Marge brute calculée = 45 000 000 - 9 000 000 = **36 000 000 FCFA**

Le chiffre annoncé de **18 000 000 FCFA** est incorrect. Il semble qu'il y ait une erreur de calcul dans le tableau (probablement un double comptage ou une erreur de lecture des chiffres).

**Chiffre correct :** 36 000 000 FCFA
```


#### pénalité 1.10 — 1/2, diversité 0.99, 20 s, coupé au budget

- ✗ fait : 13500000 / 13.500.000 / 13,5 / 40 % / 40%
- ✓ répond en fr (vu : fr)

```
L'incohérence se situe dans la **Marge brute annoncée**.

Pour vérifier l'exactitude, nous devons appliquer la formule de base :
$$\text{Marge Brute} = \text{Chiffre d'affaires} - \text{Coûts Variables}$$

Dans ce tableau, on ne donne que les charges fixes (9 000 000 FCFA). Il est donc impossible de calculer la marge brute réelle sans connaître les coûts variables. Cependant, si nous supposons que le chiffre d'affaires annoncé (45 000 000 FCFA) soit correct et que l'annonce de la marge brute soit une erreur de calcul ou de formulation, nous pouvons déduire ce qui est probablement faux en comparant avec les chiffres annoncés.

Analysons la logique :
1. Si le chiffre d'affaires est de **45 000 000 FCFA**.
2. La marge brute annoncée est de **18 000 000 FCFA**.
3. Cela impliquerait que les coûts variables seraient de $45 - 18 = 27$ millions, ce qui est très élevé par rapport aux charges fixes de 9 millions (ce qui ferait une marge nette négative).

Cependant, l'incohérence la plus évidente ici réside dans le fait qu'une **Marge brute annoncée** ne peut pas être calculée ou affichée correctement si les coûts variables sont ignorés. Mais si nous regardons les chiffres comme des données d'entrée pour une erreur de calcul :

Si on prend le chiffre d'affaires (45 000 000) et on soustrait les charges fixes (9 000 000), on obtient un résultat de **36 000 000 FCFA**. C'est ce montant qui devrait être la marge brute *réelle* si l'on ignorait les coûts variables.

L'annonce de **18 000 000 FCFA** est donc incorrecte car elle ne correspond pas à une logique simple de soustraction des charges fixes du chiffre d'affaires, ni même à une marge brute réaliste pour ces chiffres (qui donneraient un taux de marge bien supérieur au 30 % annoncé).

Le chiffre correct pour la Marge brute (basé sur l'erreur de calcul apparente entre les chiffres donnés) est :
$$45\,000\,000 - 9\,000\,000 = \mathbf{36\,000\,000} \text{ FCFA}$$

*(Note : Si l'on considère que le taux de marge annoncé de 30 % est correct, la marge brute réelle devrait être $45M \times 0.30 = 13.5M$. Dans ce cas, les chiffres annoncés (18M) seraient également incorrects. Mais dans un exercice d'identification d'incohérence simple basé sur les nombres donnés, l'erreur de calcul entre le chiffre d'affaires et les charges fixes est la plus directe).*

**Réponse :**
L'incohérence réside dans la **
```


### manques-decision · analyser · achats · sans lieu · en

> An operations manager sends the note below. List what the note does not tell you but that you would need before approving it.
> 
> Note: "I propose we consolidate our 5 stationery and cleaning suppliers into a single one. The quotes I collected show an 8% saving on our current annual spend of 24,000,000 XOF. I recommend we sign this month."


#### pénalité 1.00 — 2/2, diversité 0.99, 12 s

- ✓ ≥4 points parmi la liste (4 vus : risk, depend, contract, service level)
- ✓ répond en en (vu : en)

```
Based on the note provided, here are the critical pieces of information you would need to gather before approving this proposal:

1.  **The Cost of Consolidation (Implementation Costs):** The note mentions an 8% saving on *quotes*, but it does not state the actual cost to merge the five suppliers into one. You need to know if the administrative, legal, and operational costs of consolidating five vendors into one will exceed or significantly reduce the 8% savings.
2.  **The Nature of the Savings (Quote vs. Actual Spend):** The note claims an 8% saving based on "quotes collected." You need to verify whether these are actual historical quotes or just hypothetical estimates. If the quotes were hypothetical, the projected savings may be inaccurate.
3.  **The Specific Suppliers and Their Current Status:** You need the names and contact details of the five separate suppliers to understand their current capabilities, pricing structures, and whether they can realistically be integrated into a single contract.
4.  **The Timeline for Implementation:** The note recommends signing the agreement "this month," but it does not specify the timeline for the actual consolidation process. You need to know if the consolidation can realistically happen within the next month or if it will take longer.
5.  **The Total Annual Spend:** While the note mentions the spend, you need the exact figures for each of the five suppliers to calculate the precise total annual spend and verify the 8% figure mathematically.
6.  **Risk of Vendor Consolidation:** You need to understand the potential risks of consolidating five different suppliers into one, such as loss of competitive pricing, reduced service levels, or increased dependency on a single vendor.
7.  **The "XOF" Context:** The note uses "XOF" (West African CFA francs), which implies a specific geographic location. You need to confirm that the consolidation will not negatively impact the operational efficiency or compliance of the operations manager's specific region.
```


#### pénalité 1.05 — 2/2, diversité 1.00, 10 s

- ✓ ≥4 points parmi la liste (8 vus : risk, lead time, delivery, contract, transition, service level)
- ✓ répond en en (vu : en)

```
Based on the note provided, here are the critical pieces of information you would need to gather before approving this proposal:

1.  **The Cost of Consolidation (Implementation Costs):** The note mentions an 8% saving but does not state the total cost to merge the five suppliers into one. You must verify if the savings outweigh the administrative and logistical expenses of consolidation.
2.  **Supplier Reliability and Risk:** Consolidating five different vendors into a single entity introduces new risks regarding payment terms, delivery lead times, and potential points of failure. You need assurance that the new single supplier has the same track record and reliability as the current ones.
3.  **Contractual Terms and Payment Cycles:** The note mentions "quotes" but not the actual contract terms. You need to know if the new consolidated agreement will have different payment cycles, penalties for late delivery, or specific service level agreements (SLAs) compared to the individual contracts.
4.  **Scope of Services:** The note lists "stationery and cleaning" as the two categories. You need clarification on whether these are separate departments or distinct business units, as consolidating them might require significant changes to internal workflows and reporting structures.
5.  **The Specific Value Proposition:** While an 8% saving is mentioned, you need to understand *why* the current five suppliers are inefficient (e.g., lack of bargaining power, poor coordination) versus why a single consolidated entity would be more efficient. This helps validate the manager's claim.
6.  **Budget Approval for the New Structure:** The note recommends signing "this month," but you need to confirm that the company has sufficient budget allocated to absorb any potential costs associated with the new structure or the transition period.
```


#### pénalité 1.10 — 2/2, diversité 0.99, 13 s

- ✓ ≥4 points parmi la liste (8 vus : lead time, terminat, contract, price increase, scope, breakdown)
- ✓ répond en en (vu : en)

```
Based on the note provided, here are several critical pieces of information you would need to gather before approving this proposal:

1.  **The Specific Cost Breakdown**
    The note mentions an "8% saving" but does not specify *which* suppliers are being consolidated or what their individual costs were. You cannot verify if the savings are real without knowing the current price of each supplier (e.g., stationery vs. cleaning supplies) to ensure no hidden fees or overlapping services exist.

2.  **The Validity and Scope of the Quotes**
    The note states "quotes I collected," but it does not specify:
    *   Are these quotes for a single year?
    *   Do they include all necessary items (e.g., paper, ink, cleaning chemicals)?
    *   Is there a contract already in place with any of the current suppliers that might be affected by this change?

3.  **The Current Annual Spend**
    While the note mentions "24,000,000 XOF," it does not confirm if this figure is accurate for the specific fiscal year being quoted or if there are recurring costs (like annual cleaning fees) that might be missed in a consolidated package.

4.  **The Timeline and Contract Terms**
    The note recommends signing "this month." You would need to know:
    *   What is the lead time required for procurement?
    *   Are there any existing contracts with these suppliers that have early termination clauses or penalties if they are cancelled mid-year?

5.  **The Supplier's Response**
    The note claims the quotes were "collected," but it does not state whether those quotes have been received, accepted by the relevant departments (e.g., IT for stationery, Facilities for cleaning), or even if they exist yet. Approval cannot happen until these suppliers formally agree to the consolidation.

6.  **The Financial Impact on Other Departments**
    Consolidating five suppliers into one might change how costs are allocated internally. You would need to know how this affects departmental budgets and whether there is a mechanism for reallocating the cost savings if any single supplier's price increases unexpectedly.
```


### priorisation · analyser · direction · Ouagadougou · fr

> Tu assistes le gérant d'une PME de 25 personnes à Ouagadougou. Classe les quatre actions suivantes de la plus urgente à la moins urgente, avec une justification d'une ligne chacune.
> 
> a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.
> b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.
> c) Recruter un stagiaire pour la rentrée de septembre.
> d) Répondre à un appel d'offres public qui ferme dans 3 jours.
> 


#### pénalité 1.00 — 3/4, diversité 0.99, 8 s

- ✓ ≥2 points parmi la liste (4 vus : 3 jours, penalite, 40 jours, expire)
- ✗ « appel d'offres » avant « stagiaire »
- ✓ « facture » avant « stagiaire »
- ✓ répond en fr (vu : fr)

```
a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.
C'est l'urgence absolue car l'absence de paiement entraîne des pénalités financières immédiates et potentiellement des poursuites judiciaires, menaçant directement la trésorerie de la PME.

b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.
C'est l'urgence secondaire car l'absence de protection informatique expose les données et les équipements à des cyberattaques, ce qui compromet la continuité des opérations et la sécurité des clients.

c) Recruter un stagiaire pour la rentrée de septembre.
C'est l'urgence faible car, bien que nécessaire pour l'avenir, ce poste est à long terme et ne pose pas de risque immédiat de perte de revenus ou de sécurité.

d) Répondre à un appel d'offres public qui ferme dans 3 jours.
C'est l'urgence la plus faible car, bien que le délai soit court, la réponse à un appel d'offres est généralement une obligation administrative et commerciale, mais elle ne met pas en danger la survie immédiate de l'entreprise.
```


#### pénalité 1.05 — 3/4, diversité 0.98, 8 s

- ✓ ≥2 points parmi la liste (4 vus : 3 jours, penalite, 40 jours, expire)
- ✗ « appel d'offres » avant « stagiaire »
- ✓ « facture » avant « stagiaire »
- ✓ répond en fr (vu : fr)

```
a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.
C'est l'urgence absolue car la non-paiement entraîne des pénalités financières immédiates, des risques de litige et une perte potentielle de revenus, ce qui compromet directement la trésorerie de la PME.

b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.
C'est l'urgence très élevée car sans protection, les données sensibles des 25 employés risquent d'être compromises par des cyberattaques, ce qui expose la PME à des pertes de données et à des coûts de réparation majeurs.

c) Recruter un stagiaire pour la rentrée de septembre.
C'est l'urgence faible car bien que nécessaire pour le développement à long terme, cette action ne pose pas de risque immédiat ni de perte financière, et elle peut être différée sans affecter la survie immédiate de l'entreprise.

d) Répondre à un appel d'offres public qui ferme dans 3 jours.
C'est l'urgence faible car bien que le délai soit court, il ne présente pas de risque financier ou de perte de données immédiat, et les processus administratifs peuvent être optimisés pour répondre plus tard sans compromettre la situation actuelle.
```


#### pénalité 1.10 — 3/4, diversité 0.98, 8 s

- ✓ ≥2 points parmi la liste (4 vus : 3 jours, penalite, 40 jours, expire)
- ✗ « appel d'offres » avant « stagiaire »
- ✓ « facture » avant « stagiaire »
- ✓ répond en fr (vu : fr)

```
a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.
C'est l'urgence absolue car la non-paiement entraîne immédiatement des pénalités financières, un risque de litige juridique et une perte potentielle de clients en raison d'un manque de solvabilité perçue.

b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.
C'est l'urgence critique car sans ce service, les équipements informatiques risquent de devenir inopérables ou vulnérables à des cyberattaques graves, compromettant la continuité des activités et la sécurité des données.

c) Recruter un stagiaire pour la rentrée de septembre.
C'est l'urgence secondaire car bien que nécessaire pour le développement du personnel, elle ne pose pas de risque immédiat ou de perte financière si les ressources sont déjà en place, contrairement aux autres points listés.

d) Répondre à un appel d'offres public qui ferme dans 3 jours.
C'est l'urgence la moins urgente car, bien que nécessaire pour la croissance, elle ne présente pas de risque immédiat de perte financière ou de sécurité opérationnelle si le dossier est manqué, contrairement aux autres points listés.
```
