# Résumer · rédiger · analyser — q2b-iq4xs-temoin (2B)

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
| cr-chantier | résumer | BTP · Ouagadougou · fr | 5/7 | 5/7 | 5/7 |
| point-flotte | résumer | logistique · sans lieu · en | 7/7 | 7/7 | 7/7 |
| note-conges | résumer | RH · Dakar · fr | 6/6 | 6/6 | 6/6 |
| fil-client | résumer | commerce · Accra · en | 5/6 | 5/6 | 5/6 |
| rapport-sante | résumer | santé · Cotonou · fr | 6/7 | 6/7 | 6/7 |
| relance | rédiger | recouvrement · Abidjan · fr | 8/8 | 8/8 | 8/8 |
| annonce-poste | rédiger | RH · Bamako · en | 6/8 | 6/8 | 6/8 |
| note-coupure | rédiger | informatique · Lomé · fr | 7/7 | 7/7 | 7/7 |
| reponse-reclamation | rédiger | service client · sans lieu · en | 5/6 | 5/6 | 5/6 |
| avenant | rédiger | juridique · Douala · fr | 7/7 | 7/7 | 7/7 |
| manques-devis | analyser | achats · sans lieu · fr | 2/2 ⚠ | 2/2 ⚠ | 2/2 ⚠ |
| risques-contrat | analyser | juridique · sans lieu · en | 2/2 | 2/2 | 2/2 |
| incoherence | analyser | gestion · sans lieu · fr | 2/2 | 2/2 ⚠ | 1/2 |
| manques-decision | analyser | achats · sans lieu · en | 2/2 | 1/2 | 1/2 |
| priorisation | analyser | direction · Ouagadougou · fr | 3/4 | 4/4 | 4/4 |

| Total | | | pen 1.00 | pen 1.05 | pen 1.10 |
|---|---|---|---|---|---|
| **résumer** | 5 épreuves | | **29/33** (88 %) | **29/33** (88 %) | **29/33** (88 %) |
| **rédiger** | 5 épreuves | | **33/36** (92 %) | **33/36** (92 %) | **33/36** (92 %) |
| **analyser** | 5 épreuves | | **11/12** (92 %) | **11/12** (92 %) | **10/12** (83 %) |
| **ensemble** | 15 épreuves | | **73/81** (90 %) | **73/81** (90 %) | **72/81** (89 %) |
| **moyenne par épreuve** | à poids égal | | **92 %** | **90 %** | **87 %** |

## Hallucination de nombres

| Épreuve | pen 1.00 | pen 1.05 | pen 1.10 |
|---|---|---|---|
| cr-chantier | ❌ 42000000, 52000000 | ❌ 42000000, 52000000 | ❌ 42000000, 53000000 |
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


#### pénalité 1.00 — 5/7, diversité 1.00, 3 s

- ✓ fait : 78
- ✓ fait : 9 jours / neuf jours
- ✗ fait : 41500000 / 41.500.000
- ✓ fait : 30 juin / juin
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✗ aucun nombre inventé (vu : 42000000, 52000000)

```
- Gros œuvre achevé à 78 % (42 000 000 FCFA dépensés sur 52 000 000 FCFA prévus).
- Livraison de ciment retardée de 9 jours due à une rupture de stock à Lomé.
- Client demande d'avancer la réception au 30 juin.
```


#### pénalité 1.05 — 5/7, diversité 1.00, 3 s

- ✓ fait : 78
- ✓ fait : 9 jours / neuf jours
- ✗ fait : 41500000 / 41.500.000
- ✓ fait : 30 juin / juin
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✗ aucun nombre inventé (vu : 42000000, 52000000)

```
- Gros œuvre achevé à 78 % (42 000 000 FCFA dépensés sur 52 000 000 FCFA prévus).
- Livraison de ciment retardée de 9 jours due à une rupture de stock à Lomé.
- Client demande d'avancer la réception au 30 juin.
```


#### pénalité 1.10 — 5/7, diversité 1.00, 3 s

- ✓ fait : 78
- ✓ fait : 9 jours / neuf jours
- ✗ fait : 41500000 / 41.500.000
- ✓ fait : 30 juin / juin
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✗ aucun nombre inventé (vu : 42000000, 53000000)

```
- Gros œuvre achevé à 78 % (42 000 000 FCFA dépensés sur 53 000 000 FCFA prévus).
- Livraison de ciment retardée de 9 jours due à une rupture de stock au fournisseur.
- Client demande d'avancer la réception jusqu'au 30 juin pour accélérer les délais.
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
- ✓ ≤ 130 mots (vu : 44)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
The fleet currently stands at 14 vehicles, with three awaiting parts off the road. On-time delivery dropped to 86% from 92% last quarter. Fuel costs increased by 17% following the withdrawal of a subsidy. Additionally, the new depot is scheduled to open in October.
```


#### pénalité 1.05 — 7/7, diversité 1.00, 3 s

- ✓ fait : 14 vehicles / 14 
- ✓ fait : 86
- ✓ fait : 17
- ✓ fait : october
- ✓ ≤ 130 mots (vu : 44)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
The fleet currently stands at 14 vehicles, with three awaiting parts off the road. On-time delivery dropped to 86% from 92% last quarter. Fuel costs increased by 17% following the withdrawal of a subsidy. Additionally, the new depot is scheduled to open in October.
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
The fleet currently stands at 14 vehicles, with three awaiting parts off the road. On-time delivery dropped to 86% from a previous quarter's 92%. Fuel costs increased by 17% following the withdrawal of a subsidy. Meanwhile, the new depot is scheduled for opening in October.
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
À compter du 1er septembre, les demandes de congé doivent être déposées au moins 15 jours à l'avance via le formulaire RH-04. Les demandes transmises par courriel ne seront plus acceptées, et le chef de service dispose de 5 jours ouvrés pour valider ou refuser chaque demande.
```


#### pénalité 1.05 — 6/6, diversité 1.00, 3 s

- ✓ fait : 15 jours / quinze jours
- ✓ fait : rh-04
- ✓ fait : septembre
- ✓ ≤ 90 mots (vu : 47)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
À compter du 1er septembre, les demandes de congé doivent être déposées au moins 15 jours à l'avance via le formulaire RH-04. Les demandes transmises par courriel ne seront plus acceptées et le chef de service dispose de 5 jours ouvrés pour valider ou refuser chaque demande.
```


#### pénalité 1.10 — 6/6, diversité 1.00, 3 s

- ✓ fait : 15 jours / quinze jours
- ✓ fait : rh-04
- ✓ fait : septembre
- ✓ ≤ 90 mots (vu : 47)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
À compter du 1er septembre, les demandes de congé doivent être déposées au moins quinze jours à l'avance via le formulaire RH-04. Les demandes transmises par courriel ne seront plus acceptées et le chef de service dispose de cinq jours ouvrés pour valider ou refuser chaque demande.
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
- ✓ ≤ 90 mots (vu : 43)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We have agreed to ship the 250 units immediately and to provide a firm delivery date for the remaining 150 units by Friday. We must now confirm the specific shipping date for the 250 units and finalize the schedule for the 150 units.
```


#### pénalité 1.05 — 5/6, diversité 1.00, 2 s

- ✗ fait : gh-2291
- ✓ fait : 250
- ✓ fait : friday
- ✓ ≤ 90 mots (vu : 46)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We have agreed to ship the 250 units immediately and will provide a firm delivery date for the remaining 150 units by Friday. Next, we must confirm the specific shipping date for the 250 units and await your confirmation of that date before proceeding with shipment.
```


#### pénalité 1.10 — 5/6, diversité 1.00, 2 s

- ✗ fait : gh-2291
- ✓ fait : 250
- ✓ fait : friday
- ✓ ≤ 90 mots (vu : 36)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We have agreed to ship the 250 units immediately and will provide a firm delivery date for the remaining 150 units by Friday. Next, we must confirm that specific dates with you before proceeding with shipment.
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
- 1 240 consultations enregistrées (+8 % par rapport au mois précédent).
- Trois ruptures de stock de médicaments essentiels nécessitent une intervention immédiate.
- Le groupe électrogène est en panne depuis le 4 mai, impactant l'approvisionnement en énergie.
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
- 1 240 consultations enregistrées (+8 % par rapport au mois précédent).
- Trois ruptures de stock de médicaments essentiels nécessitent une intervention immédiate.
- Le groupe électrogène est en panne depuis le 4 mai, impactant l'approvisionnement en énergie.
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
- 1240 consultations enregistrées (+8 % par rapport au mois précédent).
- Trois ruptures de stock de médicaments essentiels nécessitent une intervention immédiate.
- Le groupe électrogène est en panne depuis le 4 mai, impactant l'approvisionnement en énergie.
```


### relance · rédiger · recouvrement · Abidjan · fr

> Rédige une première relance de paiement, courtoise, adressée à la Pharmacie Riviera à Abidjan. Facture F-2026-118 d'un montant de 2 350 000 FCFA, échue depuis 22 jours. Demande un règlement sous huit jours et propose un rendez-vous téléphonique si un échéancier est nécessaire. Maximum 120 mots.


#### pénalité 1.00 — 8/8, diversité 1.00, 3 s

- ✓ fait : f-2026-118
- ✓ fait : 2350000 / 2.350.000
- ✓ fait : 22
- ✓ fait : echeancier
- ✓ registre : aucune menace
- ✓ ≤ 180 mots (vu : 51)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Madame, Monsieur,

Nous vous rappelons la facture F-2026-118 (2 350 000 FCFA) échue depuis 22 jours.

Pour faciliter le règlement, nous vous invitons à nous contacter sous huit jours. Un rendez-vous téléphonique est proposé si un échéancier est nécessaire.

Nous restons à votre disposition pour toute question.

Cordialement,
Le service commercial
```


#### pénalité 1.05 — 8/8, diversité 1.00, 3 s

- ✓ fait : f-2026-118
- ✓ fait : 2350000 / 2.350.000
- ✓ fait : 22
- ✓ fait : echeancier
- ✓ registre : aucune menace
- ✓ ≤ 180 mots (vu : 43)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Madame, Monsieur,

Nous vous rappelons la facture F-2026-118 (2 350 000 FCFA) échue depuis 22 jours. Un règlement sous huit jours est demandé.

Si un échéancier est nécessaire, nous vous proposons un rendez-vous téléphonique.

Dans l'attente de votre confirmation,

Cordialement,
Le service commercial
```


#### pénalité 1.10 — 8/8, diversité 1.00, 4 s

- ✓ fait : f-2026-118
- ✓ fait : 2350000 / 2.350.000
- ✓ fait : 22
- ✓ fait : echeancier
- ✓ registre : aucune menace
- ✓ ≤ 180 mots (vu : 55)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Madame, Monsieur,

Nous vous rappelons la facture F-2026-118 (montant : 2 350 000 FCFA), échue depuis 22 jours. Un règlement sous huit jours est demandé pour éviter tout retard.

Si un échéancier s'impose, nous sommes à votre disposition pour un rendez-vous téléphonique. Nous restons à votre entière disposition pour toute question.

Cordialement,
Le service commercial
```


### annonce-poste · rédiger · RH · Bamako · en

> Draft a short job advertisement, at most 8 lines, for a logistics coordinator based in Bamako. Requirements: at least 3 years of experience in freight or distribution, working French and English, a driving licence. The contract runs for 12 months, renewable. Applications close on 30 September.


#### pénalité 1.00 — 6/8, diversité 1.00, 4 s

- ✓ fait : bamako
- ✗ fait : 3 years / three years
- ✗ fait : 12 month
- ✓ fait : french
- ✓ fait : 30 september / september
- ✓ ≤ 12 lignes (vu : 8)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We are seeking a Logistics Coordinator in Bamako with 3+ years of experience in freight or distribution.
You must be bilingual (French and English) and hold a valid driving licence.
This 12-month contract is renewable upon successful performance.
Applications must close on 30 September.
Please submit your CV and a cover letter to [Email Address].
We look forward to discussing how your skills can benefit our team.
Join us in Bamako and drive our logistics operations forward.
Contact us today to apply for this exciting opportunity.
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
You must be bilingual (French and English) and hold a valid driving licence.
This role offers a 12-month contract, renewable upon performance.
Applications are invited to submit your CV and cover letter by 30 September.
We look forward to discussing how your skills can drive our operations forward.
```


#### pénalité 1.10 — 6/8, diversité 1.00, 3 s

- ✓ fait : bamako
- ✗ fait : 3 years / three years
- ✗ fait : 12 month
- ✓ fait : french
- ✓ fait : 30 september / september
- ✓ ≤ 12 lignes (vu : 4)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We are seeking a Logistics Coordinator in Bamako with 3+ years of experience in freight or distribution.
You must be bilingual (French and English) and hold a valid driving licence.
This role offers a flexible 12-month contract, renewable upon performance.
Apply now to join our team! Applications close on 30 September.
```


### note-coupure · rédiger · informatique · Lomé · fr

> Rédige une note de service annonçant au personnel une interruption du système informatique le samedi 14, de 8 h à 14 h, pour la sauvegarde annuelle. Indique que le service support reste joignable au poste 214. Maximum 100 mots.


#### pénalité 1.00 — 7/7, diversité 1.00, 3 s

- ✓ fait : samedi 14 / le 14
- ✓ fait : 8 h / 8h / huit heures
- ✓ fait : 214
- ✓ fait : sauvegarde
- ✓ ≤ 150 mots (vu : 39)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
**Note de service : Interruption du système informatique**

Le samedi 14, de 08h00 à 14h00, le système informatique est hors service pour la sauvegarde annuelle.

Le service support reste joignable au poste 214.

Nous vous remercions de votre compréhension.
```


#### pénalité 1.05 — 7/7, diversité 1.00, 3 s

- ✓ fait : samedi 14 / le 14
- ✓ fait : 8 h / 8h / huit heures
- ✓ fait : 214
- ✓ fait : sauvegarde
- ✓ ≤ 150 mots (vu : 48)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
**Note de service : Interruption du système informatique**

Le samedi 14, de 08h00 à 14h00, le système informatique est hors service pour la sauvegarde annuelle.

Le service support reste joignable au poste 214.

Nous vous remercions de votre compréhension et vous invitons à nous contacter en cas d'urgence.
```


#### pénalité 1.10 — 7/7, diversité 1.00, 3 s

- ✓ fait : samedi 14 / le 14
- ✓ fait : 8 h / 8h / huit heures
- ✓ fait : 214
- ✓ fait : sauvegarde
- ✓ ≤ 150 mots (vu : 49)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
**Note de service : Interruption du système informatique**

Le samedi 14, de 08h00 à 14h00, le système informatique est hors service pour la sauvegarde annuelle.

Pour toute urgence ou question technique, veuillez contacter le service support au poste **214**.

Nous vous remercions de votre compréhension et restons en contact.
```


### reponse-reclamation · rédiger · service client · sans lieu · en

> Draft a reply to a customer who complains that their order arrived 6 days late. The cause was a customs hold on the shipment, which we could not control. Offer a 5% credit on their next order. Apologise once, at the beginning, and do not repeat the apology. Maximum 120 words.


#### pénalité 1.00 — 5/6, diversité 1.00, 2 s

- ✗ fait : 6 days / six days
- ✓ fait : customs
- ✓ fait : 5% / 5 %
- ✓ ≤ 180 mots (vu : 49)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We sincerely apologize for the delay in your order. Unfortunately, the shipment was held by customs, an issue we could not control. We understand this caused significant inconvenience.

To make this right, we will issue a 5% credit toward your next order. We hope this helps you move forward.
```


#### pénalité 1.05 — 5/6, diversité 1.00, 2 s

- ✗ fait : 6 days / six days
- ✓ fait : customs
- ✓ fait : 5% / 5 %
- ✓ ≤ 180 mots (vu : 45)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We sincerely apologize for the delay in your order. Unfortunately, a customs hold prevented us from shipping sooner, an issue we could not control.

To make this right, we will apply a 5% credit to your next order. We hope this helps you move forward.
```


#### pénalité 1.10 — 5/6, diversité 1.00, 3 s

- ✗ fait : 6 days / six days
- ✓ fait : customs
- ✓ fait : 5% / 5 %
- ✓ ≤ 180 mots (vu : 60)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We sincerely apologize for the delay in your order. Unfortunately, a customs hold prevented us from shipping sooner than expected. We understand this caused significant inconvenience and regret that we could not meet your timeline.

To make amends, please accept a 5% discount on your next purchase. We value your business and hope to restore your trust with future orders.
```


### avenant · rédiger · juridique · Douala · fr

> Rédige l'article unique d'un avenant prolongeant le contrat de prestation n° C-2025-07 de six mois, soit du 1er juillet au 31 décembre 2026, à conditions financières inchangées. Style juridique sobre, un seul paragraphe, pas de commentaire.


#### pénalité 1.00 — 7/7, diversité 1.00, 3 s

- ✓ fait : c-2025-07
- ✓ fait : 31 decembre
- ✓ fait : 1er juillet
- ✓ fait : inchang / sans modification / identique / demeurent
- ✓ ≤ 160 mots (vu : 36)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Avenant n° C-2025-08, signé le [Date], prolonge le contrat de prestation n° C-2025-07 pour une durée de six mois, d'un 1er juillet 2026 au 31 décembre 2026, sans modification des conditions financières et des obligations contractuelles.
```


#### pénalité 1.05 — 7/7, diversité 1.00, 3 s

- ✓ fait : c-2025-07
- ✓ fait : 31 decembre
- ✓ fait : 1er juillet
- ✓ fait : inchang / sans modification / identique / demeurent
- ✓ ≤ 160 mots (vu : 35)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Avenant n° C-2025-08, signé le [Date], prolonge le contrat de prestation n° C-2025-07 pour une durée de six mois, d'un 1er juillet au 31 décembre 2026, sans modification des conditions financières et des obligations contractuelles.
```


#### pénalité 1.10 — 7/7, diversité 1.00, 4 s

- ✓ fait : c-2025-07
- ✓ fait : 31 decembre
- ✓ fait : 1er juillet
- ✓ fait : inchang / sans modification / identique / demeurent
- ✓ ≤ 160 mots (vu : 55)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Avenant n° C-2025-XX, signé le [Date], par lequel l'entreprise [Nom de la société] et le prestataire [Nom du prestataire] concluent un avenant prolongeant le contrat de prestation n° C-2025-07 pour une durée de six mois, soit du 1er juillet 2026 au 31 décembre 2026, sans modification des conditions financières et des obligations contractuelles en vigueur.
```


### manques-devis · analyser · achats · sans lieu · fr

> Voici un devis reçu d'un prestataire. Indique les informations qui manquent pour qu'un acheteur puisse le comparer et le signer.
> 
> Devis n° 88 — Kando Services. Objet : maintenance du parc informatique. Montant : 1 500 000 FCFA. Signature du gérant.


#### pénalité 1.00 — 2/2, diversité 0.99, 20 s, coupé au budget

- ✓ ≥4 points parmi la liste (9 vus : duree, tva, ht, ttc, paiement, detail)
- ✓ répond en fr (vu : fr)

```
Pour qu'un acheteur puisse comparer ce devis avec d'autres offres et le signer avec confiance, il est impératif d'ajouter des éléments de **transparence**, de **contrôle** et de **garantie**. Le devis actuel est trop générique et manque de détails techniques et financiers.

Voici les informations manquantes et les éléments à ajouter pour rendre le document complet :

### 1. Les informations techniques (Le "quoi" et le "comment")
Le devis mentionne "maintenance du parc informatique" mais ne précise pas ce qui est inclus.
*   **Type de maintenance :** Est-ce une maintenance préventive (planification), corrective (réparation d'un bug) ou une maintenance préventive + corrective ?
*   **Période de couverture :** La maintenance couvre-t-elle 1 an, 3 ans ou 5 ans ?
*   **Horaires de service :** Les interventions sont-elles en journée, en soirée, ou en week-end ?
*   **Contrat de maintenance :** Est-ce un contrat à durée limitée (ex: 1 an) ou une maintenance à vie (ex: 3 ans) ?
*   **Outils et équipements :** Les outils de diagnostic sont-ils fournis par le prestataire ou par l'acheteur ?

### 2. Les informations financières et contractuelles (Le "prix" et "durée")
Le montant est donné, mais le contexte financier est flou.
*   **Montant total :** Le devis est-il facturé à l'avance (1 500 000 FCFA) ou à la fin du contrat ?
*   **Taux de TVA :** Le montant est-il TTC ou HT ? (En FCFA, la TVA est souvent incluse, mais il faut le préciser).
*   **Paiement :** Les modalités de paiement sont-elles claires (dépôt à la signature, paiement à la fin, etc.) ?
*   **Durée du contrat :** La durée du contrat de maintenance est-elle définie ?
*   **Clause de résiliation :** Si le contrat est rompu, quelle est la procédure et les pénalités ?

### 3. Les informations sur le prestataire (Le "qui")
*   **Nom complet du prestataire :** "Kando Services" est un nom générique. Il faut le nom de l'entreprise (ex: Kando Services S.A. à Dakar).
*   **Adresse physique :** L'adresse de l'entreprise est-elle indiquée ?
*   **Téléphone et Email :** Les coordonnées de contact sont-elles fournies ?
*   **Certification :** Le prestataire est-il certifié (ex: ISO 9001, ISO 27001) ?
*   **Historique :** Le prestataire a-t-il des références clients dans le secteur ?

### 4. Les informations de protection (Le "protection")
*   **Garantie de résultat :** Si le contrat est rompu, est-ce que le prestataire doit rembourser le montant ?
*   **Assurance :** Le prestataire est-il assuré pour les dommages causés par ses agents ou ses outils ?
*   **Confidentialité :** Les données des clients sont-elles protégées ?

---

### Exemple de version amélior
```


#### pénalité 1.05 — 2/2, diversité 1.00, 21 s, coupé au budget

- ✓ ≥4 points parmi la liste (5 vus : delai, paiement, detail, date, garantie)
- ✓ répond en fr (vu : fr)

```
Pour qu'un acheteur puisse comparer ce devis avec d'autres offres et le signer avec confiance, il est impératif de compléter les éléments suivants :

### 1. Les détails du prestataire (Kando Services)
*   **Adresse physique complète** (pour vérifier la légitimité de l'entreprise).
*   **Téléphone et numéro WhatsApp** (pour un contact rapide en cas de problème technique).
*   **Email professionnel** (pour les échanges formels).
*   **Numéro de SIRET** (si disponible) pour vérifier leur statut juridique.

### 2. La liste détaillée des services (Le cœur du devis)
Le montant global est un indicateur, mais l'acheteur doit savoir exactement **quoi** est inclus dans les 1 500 000 FCFA. Il faut une liste claire :
*   **Type de maintenance** : Est-ce uniquement la maintenance préventive (nettoyage, changement de batteries) ou inclut-il aussi la maintenance corrective (réparations après panne) ?
*   **Période d'intervention** : Combien de jours ou de heures sont inclus dans ce devis ?
*   **Horaires d'ouverture** : Les techniciens travaillent-t-ils uniquement le jour et l'heure indiqués, ou y a-t-il des heures de repos ?
*   **Délais de réponse** : En cas de panne, combien de temps (heures/jours) le prestataire met-il à jour le client ?

### 3. Les conditions contractuelles et financières
*   **Garantie** : Combien de temps s'applique la garantie (ex: 1 an) ? Est-elle incluse dans ce montant ?
*   **Paiement** : Le devis est-il payable à l'avance, à la livraison des services ou à la fin du contrat ?
*   **Taux de change** : Si le devis est en FCFA mais les factures sont en Euro, quel taux de conversion est utilisé ?
*   **Délais de paiement** : Combien de temps après la réception des services doit-on payer ?

### 4. Les clauses de responsabilité et exclusions
*   **Exclusions** : Y a-t-il des éléments de service non inclus (ex: maintenance de matériel hors d'âge, logiciels obsolètes) ?
*   **Responsabilité** : Qui paie en cas de panne due à un défaut de fabrication ou à une erreur humaine du prestataire ?

### 5. Les informations de contact et de signature
*   **Signature du gérant** (comme mentionnée dans votre texte) : Elle doit être signée par une personne autorisée, avec son nom complet, sa fonction et son signature manuscrite.
*   **Date de réception** : La date à laquelle le devis a été reçu.
*   **Méthode de paiement** : Mentionner clairement les modalités de paiement (virement bancaire, chèque, etc.).

---

### Exemple de version complète du devis à signer

Voici comment votre devis actuel devrait être structuré pour être complet et professionnel :

> **DEVIS N° 88**
> **Prestataire :** Kando Services
> **Objet :** Maintenance du parc informatique
> **Montant total :** 1
```


#### pénalité 1.10 — 2/2, diversité 1.00, 20 s, coupé au budget

- ✓ ≥4 points parmi la liste (5 vus : duree, paiement, detail, date, garantie)
- ✓ répond en fr (vu : fr)

```
Pour qu'un acheteur puisse comparer ce devis avec d'autres offres et le signer sans risque, il manque des éléments cruciaux de **transparence**, de **contrôle** et de **garantie**.

Voici les informations manquantes classées par ordre d'importance :

### 1. Les détails techniques (Le "Comment" et le "Quoi")
*   **La liste exhaustive du matériel :** Le devis mentionne "parc informatique", mais ne précise pas quels ordinateurs, serveurs, imprimantes ou périphériques sont inclus dans ce montant de 1 500 000 FCFA. Est-ce un remplacement complet ?
*   **Les services spécifiques :** La maintenance est-elle purement préventive (nettoyage, changement de batteries) ou corrective (remplacement de pièces)?
    *   *Question :* Y a-t-il des frais de déplacement pour les techniciens ?
    *   *Question :* Le devis inclut-il la formation du personnel ?

### 2. Les conditions contractuelles et financières
*   **La date d'exécution :** À partir de quel jour le travail sera-il commencé ?
*   **Le mode de paiement :**
    *   Est-ce un paiement unique à la signature ou en plusieurs tranches (ex: 50% avant, 50% après)?
    *   Qui doit payer les frais de transport et d'installation ?
*   **La garantie :** Quelle est la durée de garantie (ex: 1 an) ? Si une pièce casse, qui paie le coût du remplacement ?

### 3. Les clauses de responsabilité et exclusions
*   **Les exclusions :** Le devis ne mentionne-t-il pas les éléments suivants ?
    *   Les dommages causés par l'utilisateur ou des facteurs externes (foudre, incendie).
    *   L'usure normale du matériel (qui est-elle incluse dans le prix ?).
    *   La perte de données (sauvegarde incluse ?).
*   **La responsabilité :** Si un technicien fait une erreur grave, qui paie la réparation ?

### 4. Les informations légales et de contact
*   **L'adresse physique du prestataire :** L'acheteur doit savoir où le technicien peut être contacté en cas d'urgence (ex: "Le technicien est basé à Dakar").
*   **La signature numérique ou électronique :** Le devis doit être signé électroniquement par un système sécurisé pour être juridiquement valide.
*   **L'adresse de l'émetteur :** Qui est le destinataire du devis ?

### 5. Les éléments manquants dans votre exemple
Votre texte mentionne "Signature du gérant", ce qui est une bonne pratique, mais il manque :
*   La signature numérique (pour la sécurité).
*   L'adresse de l'émetteur (Kando Services) à côté du nom du gérant.

---

### Exemple d'une version complète et signable

Pour que le devis soit prêt à être signé par un acheteur, voici ce qu'il devrait contenir :

> **DEVIS N° 88**
> **Prestataire :** Kando Services
> **Objet :** Maintenance du parc informatique (Remplacement de matériel + Services)
> **Montant total :** 1 5
```


### risques-contrat · analyser · juridique · sans lieu · en

> You advise a 30-person company. Read this contract excerpt and name the three clauses that carry the most risk for us, and say why in one line each.
> 
> Excerpt: "(4) The Customer's liability under this agreement is unlimited. (7) The Supplier may revise prices at any time upon written notice. (9) Invoices issued by the Supplier are payable 90 days from receipt. (12) This agreement renews automatically for successive 12-month terms unless terminated 6 months before expiry."


#### pénalité 1.00 — 2/2, diversité 0.94, 5 s

- ✓ ≥4 points parmi la liste (7 vus : liabilit, unlimited, price, revis, renew, automatic)
- ✓ répond en en (vu : en)

```
1. **Clause (4)** carries the most risk because it grants the Customer **unlimited liability**, which could expose the company to massive, undefined financial losses if the Supplier fails to deliver or breaches other terms.
2. **Clause (7)** carries the most risk because it allows the Supplier to **unilaterally revise prices at any time**, potentially eroding the company's margins and forcing it to pay significantly higher costs without negotiation.
3. **Clause (12)** carries the most risk because it creates an **automatic renewal trap**, binding the company to a new 12-month term unless it actively terminates 6 months in advance, leaving no time to renegotiate unfavorable terms.
```


#### pénalité 1.05 — 2/2, diversité 1.00, 5 s

- ✓ ≥4 points parmi la liste (7 vus : liabilit, unlimited, price, renew, automatic, terminat)
- ✓ répond en en (vu : en)

```
1. **Clause (4)** carries the most risk because it grants the Customer unlimited liability, which can lead to catastrophic financial exposure if the Supplier fails to deliver goods or services as promised.
2. **Clause (7)** poses a severe risk by allowing the Supplier to unilaterally change prices at any time without notice, effectively stripping the Customer of budget control and forcing them to pay for increased costs immediately.
3. **Clause (12)** creates a high risk of indefinite, uncontrolled cost escalation because the contract renews automatically every 12 months unless explicitly terminated early, preventing the Company from renegotiating terms or setting a cap on future prices.
```


#### pénalité 1.10 — 2/2, diversité 1.00, 4 s

- ✓ ≥4 points parmi la liste (8 vus : liabilit, unlimited, price, renew, automatic, terminat)
- ✓ répond en en (vu : en)

```
1. **Clause (4)** carries the most risk because it grants you unlimited liability, meaning you could be held responsible for damages far exceeding your actual financial loss or the contract's stated value.
2. **Clause (7)** poses a severe operational risk as it allows the Supplier to change prices at any time without notice, potentially rendering your fixed budget and planning obsolete immediately.
3. **Clause (12)** creates an indefinite renewal trap where you are automatically locked into new terms for 12 months unless you actively terminate 6 months in advance, preventing you from ending the contract when it is no longer needed.
```


### incoherence · analyser · gestion · sans lieu · fr

> Ce tableau de bord contient une incohérence. Trouve-la et donne le chiffre correct.
> 
> Tableau de bord — mois de juin. Chiffre d'affaires : 45 000 000 FCFA. Taux de marge annoncé : 30 %. Marge brute annoncée : 18 000 000 FCFA. Charges fixes : 9 000 000 FCFA.


#### pénalité 1.00 — 2/2, diversité 0.97, 7 s

- ✓ fait : 13500000 / 13.500.000 / 13,5 / 40 % / 40%
- ✓ répond en fr (vu : fr)

```
Il y a une **incohérence** dans les chiffres de la marge brute annoncée.

Analysons les données fournies :
*   Chiffre d'affaires (CA) : **45 000 000 FCFA**
*   Marge brute annoncée : **18 000 000 FCFA**
*   Taux de marge annoncé : **30 %**

La marge brute est calculée en multipliant le chiffre d'affaires par le taux de marge.
Calcul : $45\,000\,000 \times 0,30 = 13\,500\,000$ FCFA.

Le chiffre annoncé de **18 000 000 FCFA** est donc incorrect. Il est probablement une erreur de frappe (confusion avec le chiffre d'affaires de 18 millions ou une erreur de calcul).

**Le chiffre correct de la marge brute annoncée est : 13 500 000 FCFA.**
```


#### pénalité 1.05 — 2/2, diversité 0.96, 20 s, coupé au budget

- ✓ fait : 13500000 / 13.500.000 / 13,5 / 40 % / 40%
- ✓ répond en fr (vu : fr)

```
Il y a une **incohérence** dans les chiffres de la marge brute annoncée.

Analysons les données fournies :
*   Chiffre d'affaires (CA) = 45 000 000 FCFA
*   Marge brute annoncée = 18 000 000 FCFA
*   Taux de marge annoncé = 30 %

La formule de la marge brute est :
$$Marge Brute = \frac{CA}{100} - Charges Fixes$$

Si nous appliquons les chiffres annoncés :
$$18\,000\,000 = \frac{45\,000\,000}{100} - 9\,000\,000$$
$$18\,000\,000 = 450\,000 - 9\,000\,000$$
$$18\,000\,000 = -8\,550\,000$$

Le résultat est négatif, ce qui est impossible pour une marge brute. Il y a donc une erreur dans l'un des chiffres. En regardant les autres données (le CA de 45 millions et le taux de 30 %), on peut déduire que la **marge brute annoncée** est probablement celle qui contient l'erreur, car elle ne correspond pas à la réalité mathématique des autres valeurs.

Si nous calculons la marge brute correcte en utilisant le CA (45 000 000) et le taux de marge (30 %) :
$$Marge Brute = 45\,000\,000 \times 30\% = 13\,500\,000 \text{ FCFA}$$

Vérifions ensuite si cette marge brute est cohérente avec les charges fixes :
$$Charges Fixes = CA - Marge Brute = 45\,000\,000 - 13\,500\,000 = 31\,500\,000 \text{ FCFA}$$

Cependant, le tableau indique que les charges fixes sont de **9 000 000 FCFA**. Cela signifie que la charge fixe annoncée est également incorrecte (elle devrait être de 31 500 000 FCFA pour être cohérente avec le CA et le taux).

Si nous supposons que les charges fixes sont correctes (9 000 000 FCFA) et que le CA est correct (45 000 000 FCFA), alors la marge brute réelle serait :
$$Marge Brute = 45\,000\,000 - 9\,000\,000 = 36\,000\,000 \text{ FCFA}$$

Dans ce cas, le taux de marge réel serait :
$$Taux = \frac{36\,000\,0
```


#### pénalité 1.10 — 1/2, diversité 0.96, 14 s

- ✗ fait : 13500000 / 13.500.000 / 13,5 / 40 % / 40%
- ✓ répond en fr (vu : fr)

```
Il y a une **incohérence** dans les chiffres de la marge brute annoncée.

Analysons les données fournies :
*   Chiffre d'affaires (CA) = 45 000 000 FCFA
*   Marge brute annoncée = 18 000 000 FCFA
*   Taux de marge annoncé = 30 %

La formule pour calculer la marge brute est :
$$Marge Brute = \frac{CA}{1 + (Taux de marge)}$$

Si nous appliquons le taux de 30 % sur le chiffre d'affaires :
$$45\,000\,000 \times (1 - 0,30) = 45\,000\,000 \times 0,70 = 31\,500\,000 \text{ FCFA}$$

Le chiffre d'affaires réel (45 millions) ne correspond pas à une marge brute de 18 millions. Le taux de 30 % est donc inexact par rapport au CA donné.

**Chiffre correct :**
Si le taux de marge est bien de **30 %**, la marge brute réelle doit être :
$$45\,000\,000 \times 70\% = \mathbf{31\,500\,000} \text{ FCFA}$$

Si le chiffre d'affaires de 45 millions est correct et que la marge brute annoncée (18 millions) est l'erreur, alors le taux de marge réel serait :
$$18\,000\,000 / 45\,000\,000 = 40\%$$

**Conclusion :**
Le tableau contient une incohérence car **le chiffre d'affaires (45 millions) ne correspond pas au taux de marge annoncé (30 %)**. Le taux de 30 % est incorrect par rapport aux chiffres affichés.
```


### manques-decision · analyser · achats · sans lieu · en

> An operations manager sends the note below. List what the note does not tell you but that you would need before approving it.
> 
> Note: "I propose we consolidate our 5 stationery and cleaning suppliers into a single one. The quotes I collected show an 8% saving on our current annual spend of 24,000,000 XOF. I recommend we sign this month."


#### pénalité 1.00 — 2/2, diversité 0.96, 18 s

- ✓ ≥4 points parmi la liste (7 vus : risk, delivery, contract, who, validity, baseline)
- ✓ répond en en (vu : en)

```
Before approving this proposal, you would need the following information to verify its validity and ensure it is in the company's best interest:

1.  **The specific cost of each individual supplier**
    *   *Why:* To calculate the actual **total annual spend** (which you mentioned as 24,000,000 XOF) and verify that the "8% saving" is mathematically accurate. If the current spend is actually 24 million, the 8% saving is 1.92 million. If the current spend is different, the math changes. You need to know the baseline to confirm the savings figure is correct.

2.  **The specific cost of the consolidated supplier**
    *   *Why:* To determine the **true cost of the new single supplier**. You cannot approve a consolidation unless you know the price of the new vendor. If the new supplier is significantly more expensive than the current average, the 8% saving might be an illusion or a result of a one-time discount that won't last.

3.  **The duration of the contract**
    *   *Why:* The note mentions "annual spend," but it does not specify the **contract length** (e.g., 1 year, 3 years, 5 years). Consolidating suppliers often involves long-term contracts. You need to know if the savings will persist for the full duration of the new contract or if it is a short-term deal that might expire quickly.

4.  **The specific items included in the consolidation**
    *   *Why:* The note says "5 stationery and cleaning suppliers." You need to know exactly **what** is being consolidated (e.g., pens, paper, cleaning supplies, janitorial services). Consolidating unrelated items (like office supplies and janitorial services) might not yield the same savings as consolidating two related items (like two different cleaning companies).

5.  **The source of the quotes**
    *   *Why:* The note states "The quotes I collected show..." You need to know **who** provided these quotes (internal team, external vendors, third-party research) and **when** they were collected. If the quotes are outdated or from a different market, the savings calculation is invalid.

6.  **The risk of disruption**
    *   *Why:* Consolidating suppliers often involves changing vendors. You need to know if this will cause **service disruption** or delays in delivery, which could be more expensive than the 8% saving.

7.  **The current status of the 5 suppliers**
    *   *Why:* You need to know if these 5 suppliers are currently **active, incurring costs, and capable of being replaced**. If they are dormant or have already been replaced, the savings calculation is moot.
```


#### pénalité 1.05 — 1/2, diversité 0.96, 16 s

- ✗ ≥4 points parmi la liste (3 vus : validity, baseline, individual)
- ✓ répond en en (vu : en)

```
Before approving this proposal, you would need the following information to verify its validity and ensure it is in your best interest:

1.  **The Cost of Each Individual Supplier**
    *   You need the specific price list or quote for each of the five separate suppliers to calculate the **true total cost** before consolidation.
    *   *Why:* The note claims an "8% saving," but without knowing the baseline cost per item, you cannot determine if the 8% is a real savings or simply a reduction in the number of vendors (which might actually increase costs due to higher unit prices).

2.  **The Cost Per Item**
    *   You need to know how much each stationery and cleaning item costs individually.
    *   *Why:* To calculate the "8% saving," you must compare the sum of the five separate costs against the single consolidated cost. If the items are expensive, a consolidation might actually be more expensive than the 8% savings claimed.

3.  **The Current Annual Spend**
    *   You need to confirm that the current spend is indeed **24,000,000 XOF**.
    *   *Why:* The note states this figure as a fact ("our current annual spend of..."). If your internal records show a different amount (e.g., 25,000,000), the math for the 8% saving will be incorrect.

4.  **The Specific Cost of the Consolidated Supplier**
    *   You need to know the price offered by the single new supplier.
    *   *Why:* The note mentions "quotes I collected," implying they exist, but it doesn't state what those quotes are. You must verify that the consolidated price is actually lower than the sum of the five separate prices.

5.  **The Cost Per Item (Reiterated)**
    *   To ensure the math holds up, you need to know the unit cost of the items being purchased so you can calculate the exact dollar amount of the savings.
    *   *Why:* This is crucial for validating the "8% saving" figure mentioned in the text.

**Summary:**
The note relies on a percentage calculation that cannot be verified without knowing the **unit costs** of the individual items and the **actual consolidated price**. Without this data, you cannot determine if the consolidation will save money or simply reduce the number of vendors.
```


#### pénalité 1.10 — 1/2, diversité 0.99, 12 s

- ✗ ≥4 points parmi la liste (3 vus : validity, per supplier, individual)
- ✓ répond en en (vu : en)

```
Before approving this proposal, you would need the following information to verify its validity and ensure it is in your best interest:

1.  **The Cost of Each Individual Supplier**
    *   You cannot calculate the "8% saving" without knowing the price per stationery item or cleaning service for each of the five separate suppliers. Without this data, you cannot determine if the savings are real or if they were based on volume discounts that will disappear once consolidation occurs.

2.  **The Total Annual Spend (Current vs. Proposed)**
    *   While the note mentions a "current annual spend" of 24,000,000 XOF, it does not explicitly state what this figure represents: is it the sum of all five suppliers? Is it an average per supplier? Or is it a different metric entirely? You need to know if consolidating these specific items will actually increase or decrease that total spend.

3.  **The Specific Cost Structure (Unit Price)**
    *   To calculate the "8% saving," you must know the unit price of the stationery and cleaning services for each of the five suppliers. If one supplier is selling at a massive discount compared to the others, consolidating might actually result in higher costs if those high-cost items are replaced by cheaper ones elsewhere.

4.  **The Timeline for Implementation**
    *   The note says "sign this month," but it does not specify when the consolidation will be completed or how long it takes to switch suppliers. You need a timeline to assess operational disruption, potential delays in receiving goods/services, and whether the savings materialize within that timeframe.

5.  **The Source of the Quotes**
    *   The note claims "quotes I collected," but does not specify if these quotes are from internal vendors, external market research, or third-party aggregators. You need to know where these quotes came from to verify their accuracy and reliability.
```


### priorisation · analyser · direction · Ouagadougou · fr

> Tu assistes le gérant d'une PME de 25 personnes à Ouagadougou. Classe les quatre actions suivantes de la plus urgente à la moins urgente, avec une justification d'une ligne chacune.
> 
> a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.
> b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.
> c) Recruter un stagiaire pour la rentrée de septembre.
> d) Répondre à un appel d'offres public qui ferme dans 3 jours.
> 


#### pénalité 1.00 — 3/4, diversité 0.96, 9 s

- ✓ ≥2 points parmi la liste (4 vus : 3 jours, penalite, 40 jours, expire)
- ✗ « appel d'offres » avant « stagiaire »
- ✓ « facture » avant « stagiaire »
- ✓ répond en fr (vu : fr)

```
Voici l'analyse des quatre actions classées de la plus urgente à la moins urgente pour un gestionnaire d'une PME à Ouagadougou :

**a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.**
C'est l'action la plus urgente car l'absence de paiement entraîne des pénalités financières immédiates et potentiellement des poursuites judiciaires, ce qui compromet directement la trésorerie de l'entreprise.

**b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.**
C'est la deuxième action la plus urgente car l'absence de protection informatique expose les données sensibles de 25 personnes à des cyberattaques, risquant de causer des pertes de données et des dommages réels à l'image de l'entreprise.

**c) Recruter un stagiaire pour la rentrée de septembre.**
C'est l'action la moins urgente car, bien que nécessaire pour l'avenir, elle ne pose pas de risque immédiat et ne compromet pas la survie de l'entreprise dans les semaines à venir.

**d) Répondre à un appel d'offres public qui ferme dans 3 jours.**
C'est l'action la moins urgente car, bien que critique pour la croissance future, elle ne présente pas de danger immédiat et ne nécessite pas d'intervention d'urgence pour la pérennité de l'entreprise.
```


#### pénalité 1.05 — 4/4, diversité 0.99, 12 s

- ✓ ≥2 points parmi la liste (4 vus : 3 jours, penalite, 40 jours, expire)
- ✓ « appel d'offres » avant « stagiaire »
- ✓ « facture » avant « stagiaire »
- ✓ répond en fr (vu : fr)

```
Voici l'analyse des quatre actions classées de la plus urgente à la moins urgente pour un gestionnaire d'une PME à Ouagadougou :

**a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.**
C'est l'action la plus urgente car elle compromet directement la trésorerie de l'entreprise. Les pénalités financières s'accumulent rapidement, menaçant le paiement des salaires et des achats d'inventaire, ce qui peut entraîner une faillite immédiate si les fonds ne sont pas rétablis dans un délai très court.

**d) Répondre à un appel d'offres public qui ferme dans 3 jours.**
C'est la deuxième priorité car elle représente une opportunité commerciale majeure et un engagement contractuel. Le risque de perte de l'appel d'offres est immédiat, mais il ne compromet pas la survie financière de l'entreprise à court terme comme le fait une facture échue.

**b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.**
C'est l'action la moins urgente parmi les quatre. Bien que cela pose des risques de sécurité et de perte de données, ce n'est pas une urgence financière ou contractuelle immédiate. Les systèmes peuvent être mis en place à nouveau rapidement si le problème est résolu, sans compromettre la survie de l'entreprise.

**c) Recruter un stagiaire pour la rentrée de septembre.**
C'est l'action la moins urgente car elle relève du développement à moyen terme. Bien que nécessaire pour l'avenir de l'entreprise, elle ne présente pas d'urgence critique immédiate et n'a pas encore d'impact financier ou opérationnel immédiat sur le fonctionnement courant de l'entreprise.
```


#### pénalité 1.10 — 4/4, diversité 1.00, 15 s

- ✓ ≥2 points parmi la liste (4 vus : 3 jours, penalite, 40 jours, expire)
- ✓ « appel d'offres » avant « stagiaire »
- ✓ « facture » avant « stagiaire »
- ✓ répond en fr (vu : fr)

```
Voici l'analyse des quatre actions classées de la plus urgente à la moins urgente pour un gestionnaire d'une PME à Ouagadougou :

**a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.**
C'est l'action **la plus urgente**. L'échéance de 40 jours dépasse largement le seuil critique (généralement 30-60 jours selon les contrats), entraînant des pénalités financières immédiates qui peuvent éroder la trésorerie. À Ouagadougou, où l'infrastructure bancaire peut être complexe à gérer localement, un retard de paiement prolongé expose directement le solvabilité de l'entreprise et compromet sa capacité d'échange avec les partenaires commerciaux.

**d) Répondre à un appel d'offres public qui ferme dans 3 jours.**
C'est la **deuxième action la plus urgente**. La perte d'un appel d'offre public représente une opportunité commerciale directe (nouvelles sources de revenus). Dans un contexte où les marchés locaux et internationaux sont dynamiques, manquer cette fenêtre de trois jours peut entraîner des pertes financières immédiates et l'échec d'une stratégie de croissance.

**b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.**
C'est la **troisième action urgente**. Bien que cela ne soit pas une perte financière immédiate, c'est un risque opérationnel critique. Sans protection anti-virus, les données sensibles des 25 employés et leurs clients risquent d'être compromises par des cyberattaques. À Ouagadougou, où le ciblage informatique est fréquent, cette faille technique peut causer une perte de données ou des pertes de revenus en cas de piratage, nécessitant un traitement immédiat pour rétablir la sécurité du parc.

**c) Recruter un stagiaire pour la rentrée de septembre.**
C'est l'action **la moins urgente**. Bien que nécessaire pour le développement à long terme et la succession des compétences, recruter un stagiaire ne pose pas de risque financier ou opérationnel immédiat. L'entreprise a probablement déjà des ressources humaines (employés permanents) qui peuvent prendre en charge ce poste dès qu'il sera disponible, rendant cette action secondaire par rapport aux impératifs financiers et sécuritaires actuels.
```
