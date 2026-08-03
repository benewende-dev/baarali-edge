# Résumer · rédiger · analyser — q2b-iq4xs-baarali (2B)

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
| cr-chantier | résumer | BTP · Ouagadougou · fr | 7/7 | 7/7 | 7/7 |
| point-flotte | résumer | logistique · sans lieu · en | 7/7 | 7/7 | 7/7 |
| note-conges | résumer | RH · Dakar · fr | 6/6 | 6/6 | 6/6 |
| fil-client | résumer | commerce · Accra · en | 5/6 | 5/6 | 5/6 |
| rapport-sante | résumer | santé · Cotonou · fr | 6/7 | 6/7 | 6/7 |
| relance | rédiger | recouvrement · Abidjan · fr | 7/8 | 8/8 | 8/8 |
| annonce-poste | rédiger | RH · Bamako · en | 7/8 | 7/8 | 8/8 |
| note-coupure | rédiger | informatique · Lomé · fr | 7/7 | 7/7 | 7/7 |
| reponse-reclamation | rédiger | service client · sans lieu · en | 5/6 | 5/6 | 5/6 |
| avenant | rédiger | juridique · Douala · fr | 7/7 | 7/7 | 6/7 |
| manques-devis | analyser | achats · sans lieu · fr | 2/2 | 2/2 | 2/2 |
| risques-contrat | analyser | juridique · sans lieu · en | 2/2 | 2/2 | 2/2 |
| incoherence | analyser | gestion · sans lieu · fr | 1/2 | 1/2 | 1/2 |
| manques-decision | analyser | achats · sans lieu · en | 2/2 | 2/2 | 2/2 |
| priorisation | analyser | direction · Ouagadougou · fr | 4/4 | 4/4 | 4/4 |

| Total | | | pen 1.00 | pen 1.05 | pen 1.10 |
|---|---|---|---|---|---|
| **résumer** | 5 épreuves | | **31/33** (94 %) | **31/33** (94 %) | **31/33** (94 %) |
| **rédiger** | 5 épreuves | | **33/36** (92 %) | **34/36** (94 %) | **34/36** (94 %) |
| **analyser** | 5 épreuves | | **11/12** (92 %) | **11/12** (92 %) | **11/12** (92 %) |
| **ensemble** | 15 épreuves | | **75/81** (93 %) | **76/81** (94 %) | **76/81** (94 %) |
| **moyenne par épreuve** | à poids égal | | **92 %** | **93 %** | **93 %** |

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


#### pénalité 1.00 — 7/7, diversité 1.00, 3 s

- ✓ fait : 78
- ✓ fait : 9 jours / neuf jours
- ✓ fait : 41500000 / 41.500.000
- ✓ fait : 30 juin / juin
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
- Gros œuvre achevé à 78 % ; livraison de ciment retardée de 9 jours (invoquée rupture de stock à Lomé).
- Budget consommé : 41 500 000 FCFA sur 60 000 000 FCFA prévus.
- Client demande d'avancer la réception au 30 juin.
```


#### pénalité 1.05 — 7/7, diversité 1.00, 3 s

- ✓ fait : 78
- ✓ fait : 9 jours / neuf jours
- ✓ fait : 41500000 / 41.500.000
- ✓ fait : 30 juin / juin
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
- Gros œuvre achevé à 78 % ; livraison de ciment retardée de 9 jours (invoquée rupture de stock à Lomé).
- Budget consommé : 41 500 000 FCFA sur un budget prévu de 60 000 000 FCFA.
- Client demande d'avancer la réception au 30 juin.
```


#### pénalité 1.10 — 7/7, diversité 1.00, 3 s

- ✓ fait : 78
- ✓ fait : 9 jours / neuf jours
- ✓ fait : 41500000 / 41.500.000
- ✓ fait : 30 juin / juin
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
- Gros œuvre achevé à 78 % ; livraison de ciment retardée de 9 jours (invoquée rupture de stock à Lomé).
- Budget consommé : 41 500 000 FCFA sur un budget prévu de 60 000 000 FCFA.
- Client demande d'avancer la réception au 30 juin.
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
- ✓ ≤ 130 mots (vu : 42)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
The fleet currently stands at 14 vehicles, with three awaiting parts. On-time delivery has declined to 86% from 92% last quarter. Fuel costs increased by 17% following the withdrawal of a subsidy. Additionally, the new depot is scheduled to open in October.
```


#### pénalité 1.05 — 7/7, diversité 1.00, 3 s

- ✓ fait : 14 vehicles / 14 
- ✓ fait : 86
- ✓ fait : 17
- ✓ fait : october
- ✓ ≤ 130 mots (vu : 43)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
The fleet currently stands at 14 vehicles, with three awaiting parts. On-time delivery has declined to 86% from the previous quarter's 92%. Additionally, fuel costs increased by 17% following the withdrawal of a subsidy. The new depot is scheduled to open in October.
```


#### pénalité 1.10 — 7/7, diversité 1.00, 3 s

- ✓ fait : 14 vehicles / 14 
- ✓ fait : 86
- ✓ fait : 17
- ✓ fait : october
- ✓ ≤ 130 mots (vu : 43)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
The fleet currently stands at 14 vehicles, with three awaiting parts. On-time delivery has declined to 86% from the previous quarter's 92%. Additionally, fuel costs increased by 17% following the withdrawal of a subsidy. The new depot is scheduled for opening in October.
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
- ✓ ≤ 90 mots (vu : 47)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
À compter du 1er septembre, les demandes de congé doivent désormais être déposées au moins quinze jours à l'avance via le formulaire RH-04. Les demandes transmises par courriel sont désormais inacceptables, et le chef de service dispose de cinq jours ouvrés pour valider ou refuser chaque demande.
```


#### pénalité 1.10 — 6/6, diversité 1.00, 2 s

- ✓ fait : 15 jours / quinze jours
- ✓ fait : rh-04
- ✓ fait : septembre
- ✓ ≤ 90 mots (vu : 34)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
À compter du 1er septembre, les demandes de congé doivent désormais être déposées au moins quinze jours à l'avance via le formulaire RH-04. Les demandes transmises par courriel sont désormais inacceptables et seront refusées.
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
- ✓ ≤ 90 mots (vu : 45)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We have agreed to ship the 250 units immediately and to provide a firm delivery date for the remaining 150 units by Friday. We must now confirm the specific date for the rest of the order and initiate the shipment process for the 250 units.
```


#### pénalité 1.05 — 5/6, diversité 1.00, 2 s

- ✗ fait : gh-2291
- ✓ fait : 250
- ✓ fait : friday
- ✓ ≤ 90 mots (vu : 38)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We have agreed to ship the 250 units immediately and will provide a firm delivery date for the remaining 150 units by Friday. Next, we must confirm this specific date with the client before proceeding with the shipment.
```


#### pénalité 1.10 — 5/6, diversité 1.00, 2 s

- ✗ fait : gh-2291
- ✓ fait : 250
- ✓ fait : friday
- ✓ ≤ 90 mots (vu : 35)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We have agreed to ship the 250 units immediately and will provide a firm delivery date for the remaining 150 by Friday. Next, we must confirm this specific shipment date with you before proceeding further.
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
- Trois ruptures de stock de médicaments essentiels ont été identifiées et nécessitent une intervention immédiate.
- Le groupe électrogène est en panne depuis le 4 mai, impactant les services d'urgence et la continuité des soins.
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
- Trois ruptures de stock de médicaments essentiels ont été identifiées et nécessitent un réapprovisionnement immédiat.
- Le groupe électrogène est en panne depuis le 4 mai, compromettant l'approvisionnement en eau potable et la continuité des soins.
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
- 1240 consultations enregistrées avec une hausse de 8 % par rapport au mois précédent.
- Trois ruptures de stock de médicaments essentiels nécessitent un réapprovisionnement immédiat.
- Le groupe électrogène est en panne depuis le 4 mai, impactant la continuité des soins et l'éclairage du centre.
```


### relance · rédiger · recouvrement · Abidjan · fr

> Rédige une première relance de paiement, courtoise, adressée à la Pharmacie Riviera à Abidjan. Facture F-2026-118 d'un montant de 2 350 000 FCFA, échue depuis 22 jours. Demande un règlement sous huit jours et propose un rendez-vous téléphonique si un échéancier est nécessaire. Maximum 120 mots.


#### pénalité 1.00 — 7/8, diversité 1.00, 4 s

- ✓ fait : f-2026-118
- ✓ fait : 2350000 / 2.350.000
- ✓ fait : 22
- ✗ fait : echeancier
- ✓ registre : aucune menace
- ✓ ≤ 180 mots (vu : 59)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Madame, Monsieur,

Nous vous rappelons la facture F-2026-118, d'un montant de 2 350 000 FCFA, échue depuis 22 jours.

Pour faciliter le règlement, nous vous invitons à effectuer le paiement sous huit jours. Si votre situation l'exige, nous sommes à votre disposition pour un rendez-vous téléphonique.

Nous restons à votre entière disposition pour toute question.

Cordialement,
Le service commercial
```


#### pénalité 1.05 — 8/8, diversité 1.00, 4 s

- ✓ fait : f-2026-118
- ✓ fait : 2350000 / 2.350.000
- ✓ fait : 22
- ✓ fait : echeancier
- ✓ registre : aucune menace
- ✓ ≤ 180 mots (vu : 62)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Madame, Monsieur,

Nous vous rappelons la facture F-2026-118 (2 350 000 FCFA) échue depuis 22 jours.

Pour faciliter le règlement, nous vous invitons à régler ce montant sous huit jours. Si votre situation l'oblige, nous sommes à votre disposition pour un rendez-vous téléphonique afin de discuter d'un échéancier adapté.

Nous restons à votre entière disposition pour toute question.

Cordialement,
Le service commercial
```


#### pénalité 1.10 — 8/8, diversité 1.00, 4 s

- ✓ fait : f-2026-118
- ✓ fait : 2350000 / 2.350.000
- ✓ fait : 22
- ✓ fait : echeancier
- ✓ registre : aucune menace
- ✓ ≤ 180 mots (vu : 67)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Madame, Monsieur,

Nous vous rappelons la facture F-2026-118 (montant : 2 350 000 FCFA), échue depuis 22 jours.

Pour faciliter le règlement, nous vous invitons à régler ce montant sous huit jours. Si votre situation l'oblige, n'hésitez pas à nous contacter pour un rendez-vous téléphonique afin de discuter d'un échéancier adapté.

Nous restons à votre entière disposition et vous remercions de votre confiance.

Cordialement,
Le service commercial
```


### annonce-poste · rédiger · RH · Bamako · en

> Draft a short job advertisement, at most 8 lines, for a logistics coordinator based in Bamako. Requirements: at least 3 years of experience in freight or distribution, working French and English, a driving licence. The contract runs for 12 months, renewable. Applications close on 30 September.


#### pénalité 1.00 — 7/8, diversité 1.00, 4 s

- ✓ fait : bamako
- ✓ fait : 3 years / three years
- ✗ fait : 12 month
- ✓ fait : french
- ✓ fait : 30 september / september
- ✓ ≤ 12 lignes (vu : 9)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We are seeking a Logistics Coordinator in Bamako with at least 3 years of experience in freight or distribution.
You must be fluent in both French and English and hold a valid driving licence.
This 12-month contract is renewable upon successful completion.
Applications must be submitted by 30 September.
We look forward to meeting a dedicated professional who can optimize our supply chain.
Please send your CV and a cover letter to: [Insert Email Address]
For further details, contact our HR team at [Insert Phone Number].
We are committed to providing a competitive salary and professional growth opportunities.
Join our team today and contribute to Bamako's logistics excellence.
```


#### pénalité 1.05 — 7/8, diversité 1.00, 5 s

- ✓ fait : bamako
- ✓ fait : 3 years / three years
- ✗ fait : 12 month
- ✓ fait : french
- ✓ fait : 30 september / september
- ✓ ≤ 12 lignes (vu : 8)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We are seeking a Logistics Coordinator in Bamako with at least 3 years of experience in freight or distribution.
You must be fluent in both French and English, hold a valid driving licence, and demonstrate strong organizational skills.
This role offers a renewable 12-month contract starting immediately.
Applications should include your CV and a cover letter detailing your relevant logistics projects.
All applications will be reviewed by our team and contacted within two weeks.
Please submit your application to: logistics@company.com with the subject line "Logistics Coordinator - Bamako".
We look forward to welcoming your expertise to our growing distribution network in West Africa.
Deadline for submissions is 30 September.
```


#### pénalité 1.10 — 8/8, diversité 1.00, 3 s

- ✓ fait : bamako
- ✓ fait : 3 years / three years
- ✓ fait : 12 month
- ✓ fait : french
- ✓ fait : 30 september / september
- ✓ ≤ 12 lignes (vu : 4)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We are seeking a Logistics Coordinator in Bamako with at least 3 years of experience in freight or distribution.
You must be fluent in both French and English, hold a valid driving licence, and demonstrate strong organizational skills.
This role offers a renewable contract for 12 months, providing excellent opportunities for growth within our logistics network.
Applications are now closing on September 30th; please submit your CV and cover letter by this date to join us.
```


### note-coupure · rédiger · informatique · Lomé · fr

> Rédige une note de service annonçant au personnel une interruption du système informatique le samedi 14, de 8 h à 14 h, pour la sauvegarde annuelle. Indique que le service support reste joignable au poste 214. Maximum 100 mots.


#### pénalité 1.00 — 7/7, diversité 1.00, 4 s

- ✓ fait : samedi 14 / le 14
- ✓ fait : 8 h / 8h / huit heures
- ✓ fait : 214
- ✓ fait : sauvegarde
- ✓ ≤ 150 mots (vu : 65)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
**Note de Service : Interruption du Système Informatique**

Nous vous informons qu'une interruption du système informatique aura lieu le samedi 14, de 8 h à 14 h. Cette pause est nécessaire pour la sauvegarde annuelle des données.

Le service Support reste joignable au poste 214. Nous vous remercions de votre compréhension et vous invitons à nous contacter en cas de besoin.

Cordialement,  
Le Service Support
```


#### pénalité 1.05 — 7/7, diversité 1.00, 4 s

- ✓ fait : samedi 14 / le 14
- ✓ fait : 8 h / 8h / huit heures
- ✓ fait : 214
- ✓ fait : sauvegarde
- ✓ ≤ 150 mots (vu : 64)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
**Note de Service : Interruption du Système Informatique**

Nous vous informons qu'une interruption du système informatique aura lieu le samedi 14, de 8 h à 14 h. Cette pause est nécessaire pour la sauvegarde annuelle des données.

Le service Support reste joignable au poste 214. Nous vous remercions de votre compréhension et vous invitons à nous contacter en cas d'urgence.

Cordialement,  
Le Service Support
```


#### pénalité 1.10 — 7/7, diversité 1.00, 4 s

- ✓ fait : samedi 14 / le 14
- ✓ fait : 8 h / 8h / huit heures
- ✓ fait : 214
- ✓ fait : sauvegarde
- ✓ ≤ 150 mots (vu : 68)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
**Note de Service : Interruption du Système Informatique**

Nous vous informons qu'une interruption du système informatique aura lieu le samedi 14, entre **8 h et 14 h**. Cette pause est nécessaire pour la sauvegarde annuelle des données.

Le service Support restera joignable au poste **214** durant cette période. Nous vous remercions de votre compréhension et nous vous invitons à contacter le service en cas d'urgence.

Cordialement,  
Service Support
```


### reponse-reclamation · rédiger · service client · sans lieu · en

> Draft a reply to a customer who complains that their order arrived 6 days late. The cause was a customs hold on the shipment, which we could not control. Offer a 5% credit on their next order. Apologise once, at the beginning, and do not repeat the apology. Maximum 120 words.


#### pénalité 1.00 — 5/6, diversité 1.00, 3 s

- ✗ fait : 6 days / six days
- ✓ fait : customs
- ✓ fait : 5% / 5 %
- ✓ ≤ 180 mots (vu : 48)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We sincerely apologize for the delay in your order. Unfortunately, the shipment was held by customs, an issue beyond our control. We understand this caused significant inconvenience.

To make amends, we will issue a 5% credit toward your next purchase. We hope this gesture helps restore your trust.
```


#### pénalité 1.05 — 5/6, diversité 1.00, 3 s

- ✗ fait : 6 days / six days
- ✓ fait : customs
- ✓ fait : 5% / 5 %
- ✓ ≤ 180 mots (vu : 54)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We sincerely apologize for the delay in your order. Unfortunately, a customs hold prevented us from shipping it sooner, and we take full responsibility for this inconvenience.

To make up for the wait, we would like to offer you a 5% discount on your next purchase. We hope this gesture helps restore your trust.
```


#### pénalité 1.10 — 5/6, diversité 1.00, 3 s

- ✗ fait : 6 days / six days
- ✓ fait : customs
- ✓ fait : 5% / 5 %
- ✓ ≤ 180 mots (vu : 71)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We sincerely apologize for the delay in your order. Unfortunately, a customs hold prevented us from shipping it sooner than expected. We understand this caused significant inconvenience and regret that we could not meet your timeline.

To make up for our mistake, we would like to offer you a 5% discount on your next purchase. Please let us know if you are interested in applying this credit toward your upcoming order.
```


### avenant · rédiger · juridique · Douala · fr

> Rédige l'article unique d'un avenant prolongeant le contrat de prestation n° C-2025-07 de six mois, soit du 1er juillet au 31 décembre 2026, à conditions financières inchangées. Style juridique sobre, un seul paragraphe, pas de commentaire.


#### pénalité 1.00 — 7/7, diversité 1.00, 3 s

- ✓ fait : c-2025-07
- ✓ fait : 31 decembre
- ✓ fait : 1er juillet
- ✓ fait : inchang / sans modification / identique / demeurent
- ✓ ≤ 160 mots (vu : 41)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
L'avenant n° C-2025-08, signé le [date], prolonge le contrat de prestation n° C-2025-07 pour une durée de six mois, d'un premier jour du 1er juillet 2026 au 31 décembre 2026, sans modification des conditions financières et des obligations contractuelles en vigueur.
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
L'avenant n° C-2025-08, signé le [date], prolonge le contrat de prestation n° C-2025-07 pour une durée de six mois, d'un premier jour du 1er juillet au 31 décembre 2026, sans modification des conditions financières et des obligations contractuelles en vigueur.
```


#### pénalité 1.10 — 6/7, diversité 1.00, 3 s

- ✓ fait : c-2025-07
- ✓ fait : 31 decembre
- ✗ fait : 1er juillet
- ✓ fait : inchang / sans modification / identique / demeurent
- ✓ ≤ 160 mots (vu : 34)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
L'avenant n° C-2025-XX, signé le [date], a pour objet de prolonger la durée du contrat de prestation n° C-2025-07 jusqu'au 31 décembre 2026, sans modification des conditions financières et des obligations contractuelles en vigueur.
```


### manques-devis · analyser · achats · sans lieu · fr

> Voici un devis reçu d'un prestataire. Indique les informations qui manquent pour qu'un acheteur puisse le comparer et le signer.
> 
> Devis n° 88 — Kando Services. Objet : maintenance du parc informatique. Montant : 1 500 000 FCFA. Signature du gérant.


#### pénalité 1.00 — 2/2, diversité 0.99, 19 s

- ✓ ≥4 points parmi la liste (5 vus : validite, paiement, detail, date, garantie)
- ✓ répond en fr (vu : fr)

```
Voici les informations essentielles qui manquent pour rendre ce devis professionnel, clair et prêt à être signé par un acheteur :

1.  **Le nom complet du prestataire** (au lieu de "Kando Services").
2.  **La date de validité du devis** (ex: "Valable du 01/01/2024 au 31/12/2024").
3.  **La liste détaillée des services** (ex: "Maintenance des serveurs", "Nettoyage des écrans", "Changement de cartes mères", etc.).
4.  **La liste des pièces jointes** (ex: "Liste des équipements à maintenir", "Historique des pannes", "Contrat de maintenance existant").
5.  **Les conditions de paiement** (ex: "Paiement à 50% à la signature, 50% à la réception des travaux").
6.  **La garantie** (ex: "Garantie de 1 an sur les travaux").
7.  **Le contact du responsable** (nom, téléphone, email) pour toute question.
8.  **La signature numérique** (signature électronique certifiée).

---

### Exemple de version corrigée et complète

Voici comment ce devis devrait apparaître pour être complet :

**Devis n° 88**
**Prestataire :** Kando Services
**Objet :** Maintenance du parc informatique
**Montant total :** 1 500 000 FCFA
**Date de validité :** Du 01/01/2024 au 31/12/2024

**Description des services :**
*   Nettoyage des écrans et des consoles de commande.
*   Vérification des systèmes de sécurité (caméras, alarmes).
*   Changement de cartes mères et de RAM.
*   Installation de logiciels de surveillance et de gestion.
*   *Liste des équipements à maintenir : (voir pièce jointe)*

**Conditions de paiement :**
*   50% (750 000 FCFA) à la signature de ce devis.
*   50% (750 000 FCFA) à la réception des travaux et remise des pièces jointes.

**Garantie :**
Garantie de 12 mois sur les travaux et les pièces fournies.

**Contact :**
Responsable : M. Kando
Téléphone : +223 00 00 00 00
Email : contact@kandoservices.com

**Signature électronique certifiée :**
*(Signature du gérant)*

---

### Pourquoi ces éléments sont cruciaux ?
*   **Clarté :** L'acheteur sait exactement quoi acheter avant de payer.
*   **Contrat :** Les conditions de paiement et la garantie sont des clauses contractuelles qui protègent l'acheteur.
*   **Authenticité :** La signature électronique certifiée prouve que le document a été signé par une personne autorisée.
```


#### pénalité 1.05 — 2/2, diversité 1.00, 14 s

- ✓ ≥4 points parmi la liste (6 vus : delai, validite, paiement, detail, date, garantie)
- ✓ répond en fr (vu : fr)

```
Voici les informations essentielles qui manquent pour rendre ce devis professionnel, clair et prêt à être signé par un acheteur :

1.  **Le nom complet du prestataire** (au lieu de "Kando Services").
2.  **La date d'émission** (pour vérifier la validité du délai de paiement).
3.  **La liste détaillée des services inclus** (ex: nettoyage, remplacement de pièces détachées, diagnostic, etc.). Un devis sans description précise ne permet pas à l'acheteur de savoir exactement ce qu'il paie.
4.  **Les conditions de paiement et de livraison** (date limite, mode de paiement, lieu de prestation).
5.  **La garantie ou la période d'essai** (si applicable).
6.  **Le contact principal** (téléphone, email, adresse physique) pour toute question.

Voici une version corrigée et complète du devis :

***

### Devis n° 88
**Prestataire :** Kando Services
**Date :** [Insérer la date]
**Objet :** Maintenance du parc informatique

**Montant total à payer :** **1 500 000 FCFA**

**Description des services inclus :**
*   Nettoyage et inspection des équipements.
*   Remplacement de pièces détachées usagées.
*   Diagnostic et réparation des logiciels et matériels.
*   [Ajouter ici les autres services si nécessaire].

**Conditions de paiement et de livraison :**
*   **Paiement :** À réception du bon de facturation (T/T) ou par virement bancaire.
*   **Date limite de paiement :** [Insérer la date, ex: 15 jours après la signature].
*   **Livraison :** Le prestataire s'engage à effectuer les travaux dans les délais convenus.

**Garantie :**
*   Garantie de [X] mois sur les réparations effectuées.

**Contact :**
*   Téléphone : [Numéro]
*   Email : [Adresse email]
*   Adresse physique : [Adresse complète du prestataire]

***

**Signature du gérant :**
*(Lieu et date)*
```


#### pénalité 1.10 — 2/2, diversité 1.00, 15 s

- ✓ ≥4 points parmi la liste (6 vus : duree, ttc, paiement, detail, date, garantie)
- ✓ répond en fr (vu : fr)

```
Voici les informations essentielles qui manquent pour rendre ce devis professionnel, clair et prêt à être signé par un acheteur :

1.  **Le nom complet du prestataire** (au lieu de "Kando Services").
2.  **La date d'émission exacte**.
3.  **L'adresse complète du prestataire**, y compris le numéro de téléphone, l'email et la ville/commune.
4.  **Les détails précis des services inclus** (ex: quel matériel est inclus ? quelle durée de garantie ? quels logiciels sont-ils ?).
5.  **La date limite pour paiement**.
6.  **Le mode de paiement accepté** (virement bancaire, chèque, etc.).
7.  **L'adresse du client** (pour que le devis soit adressé correctement).

---

### Exemple de version corrigée et complète

Voici comment ce devis devrait apparaître pour être parfaitement clair :

***

**Devis n° 88 — Kando Services**
**Objet :** Maintenance et réparation du parc informatique
**Montant total à payer : 1 500 000 FCFA**

**Informations du prestataire :**
*   **Nom de l'entreprise :** Kando Services (S.A.S.)
*   **Adresse :** Avenue de la République, Quartier des Jardins, Dakar.
*   **Téléphone :** +221 77 000 000
*   **Email :** contact@kandoservices.com

**Détails du devis :**
Ce devis concerne les services de maintenance et de réparation pour le parc informatique du client. Les prestations incluent :
*   Nettoyage des serveurs et vérification des composants.
*   Remplacement de pièces détachées (cartes mères, disques durs, etc.).
*   Installation et mise à jour des logiciels de sécurité.
*   Garantie incluse sur les travaux effectués (durée : 1 an).

**Conditions de paiement :**
*   **Date limite pour paiement :** Le 30 juin 2024.
*   **Mode de paiement :** Virement bancaire uniquement.
*   **Montant à verser :** 1 500 000 FCFA (TTC).

**Signature du gérant :**

*(Lieu et Date)*

_________________________
**[Nom du Gérant]**
Gérant de Kando Services
```


### risques-contrat · analyser · juridique · sans lieu · en

> You advise a 30-person company. Read this contract excerpt and name the three clauses that carry the most risk for us, and say why in one line each.
> 
> Excerpt: "(4) The Customer's liability under this agreement is unlimited. (7) The Supplier may revise prices at any time upon written notice. (9) Invoices issued by the Supplier are payable 90 days from receipt. (12) This agreement renews automatically for successive 12-month terms unless terminated 6 months before expiry."


#### pénalité 1.00 — 2/2, diversité 1.00, 4 s

- ✓ ≥4 points parmi la liste (7 vus : liabilit, unlimited, price, renew, automatic, terminat)
- ✓ répond en en (vu : en)

```
1. **Clause (4)** carries the most risk because it grants the Customer unlimited liability, which could expose the company to massive, unbounded financial losses if the Supplier fails to deliver or breaches other terms.
2. **Clause (7)** poses the highest risk for the Supplier's ability to recover costs, allowing them to unilaterally raise prices at any time without notice or justification, potentially rendering the contract unprofitable.
3. **Clause (12)** creates a dangerous renewal trap where the contract automatically extends indefinitely unless explicitly terminated 6 months in advance, leaving the company with no control over its long-term obligations.
```


#### pénalité 1.05 — 2/2, diversité 1.00, 4 s

- ✓ ≥4 points parmi la liste (7 vus : liabilit, unlimited, price, renew, automatic, terminat)
- ✓ répond en en (vu : en)

```
1. **Clause (4)** carries the most risk because it grants the Customer unlimited liability, which could expose them to massive financial losses if the Supplier fails to deliver or performs poorly.
2. **Clause (7)** poses a severe risk by allowing the Supplier to unilaterally change prices at any time without notice, destroying the customer's budgeting and planning capabilities.
3. **Clause (12)** creates a high risk of automatic renewal that can trap the Customer in an unfavorable contract indefinitely if they fail to terminate it 6 months before expiry.
```


#### pénalité 1.10 — 2/2, diversité 1.00, 5 s

- ✓ ≥4 points parmi la liste (8 vus : liabilit, unlimited, price, renew, automatic, terminat)
- ✓ répond en en (vu : en)

```
1. **Clause (4)** carries the most risk because it grants you unlimited liability, meaning you could be held responsible for all damages and losses without any cap or limit on your financial exposure.
2. **Clause (7)** poses a severe risk as it allows the Supplier to unilaterally change prices at any time upon notice, potentially rendering your fixed-price assumptions obsolete and causing significant cost overruns.
3. **Clause (12)** creates an indefinite renewal trap by automatically extending the contract for 12 months unless you terminate early, which could lock you into a long-term commitment without giving you adequate time to negotiate better terms or exit if conditions change.
```


### incoherence · analyser · gestion · sans lieu · fr

> Ce tableau de bord contient une incohérence. Trouve-la et donne le chiffre correct.
> 
> Tableau de bord — mois de juin. Chiffre d'affaires : 45 000 000 FCFA. Taux de marge annoncé : 30 %. Marge brute annoncée : 18 000 000 FCFA. Charges fixes : 9 000 000 FCFA.


#### pénalité 1.00 — 1/2, diversité 0.98, 6 s

- ✗ fait : 13500000 / 13.500.000 / 13,5 / 40 % / 40%
- ✓ répond en fr (vu : fr)

```
L'incohérence se situe dans la **Marge brute annoncée**.

Pour vérifier la cohérence, nous devons vérifier si la Marge brute est bien égale à la différence entre le Chiffre d'affaires et les Charges fixes :
*   Chiffre d'affaires : 45 000 000 FCFA
*   Charges fixes : 9 000 000 FCFA
*   Marge brute calculée : 45 000 000 - 9 000 000 = **36 000 000 FCFA**

Le tableau affiche une Marge brute annoncée de **18 000 000 FCFA**, ce qui est incorrect. Le chiffre correct est **36 000 000 FCFA**.
```


#### pénalité 1.05 — 1/2, diversité 0.98, 6 s

- ✗ fait : 13500000 / 13.500.000 / 13,5 / 40 % / 40%
- ✓ répond en fr (vu : fr)

```
L'incohérence se situe dans la **Marge brute annoncée**.

Pour vérifier l'exactitude, nous devons vérifier si la Marge brute est bien égale à la différence entre le Chiffre d'affaires et les Charges fixes :
*   Chiffre d'affaires = 45 000 000 FCFA
*   Charges fixes = 9 000 000 FCFA
*   Marge brute calculée = 45 000 000 - 9 000 000 = **36 000 000 FCFA**

Le tableau affiche une marge brute de **18 000 000 FCFA**, ce qui est incorrect. Le chiffre correct est donc **36 000 000 FCFA**.
```


#### pénalité 1.10 — 1/2, diversité 0.98, 8 s

- ✗ fait : 13500000 / 13.500.000 / 13,5 / 40 % / 40%
- ✓ répond en fr (vu : fr)

```
L'incohérence se situe dans la **Marge brute annoncée**.

Pour vérifier l'exactitude, nous devons additionner les charges fixes et le chiffre d'affaires pour obtenir la marge brute réelle :
*   Chiffre d'affaires : 45 000 000 FCFA
*   Charges fixes : 9 000 000 FCFA
*   **Marge brute calculée** = 45 000 000 - 9 000 000 = **36 000 000 FCFA**.

Le chiffre annoncé de **18 000 000 FCFA** est incorrect. Il semble qu'il y ait eu une erreur d'écriture ou d'interprétation dans le tableau (par exemple, si l'on a divisé par deux ou si la marge brute était mal calculée), car 36 millions ne correspondent pas à 18 millions.

Le chiffre correct pour la Marge brute annoncée est **36 000 000 FCFA**.
```


### manques-decision · analyser · achats · sans lieu · en

> An operations manager sends the note below. List what the note does not tell you but that you would need before approving it.
> 
> Note: "I propose we consolidate our 5 stationery and cleaning suppliers into a single one. The quotes I collected show an 8% saving on our current annual spend of 24,000,000 XOF. I recommend we sign this month."


#### pénalité 1.00 — 2/2, diversité 0.97, 14 s

- ✓ ≥4 points parmi la liste (8 vus : risk, depend, single point, lead time, contract, who)
- ✓ répond en en (vu : en)

```
Before approving this proposal, the operations manager would need to clarify the following critical details:

*   **The specific cost of the consolidated supplier:** The note mentions an 8% saving but does not state the **total annual cost** of the consolidated supplier. Without knowing the base price, you cannot calculate the exact dollar amount of the savings or verify if the 8% figure is accurate.
*   **The current cost of each individual supplier:** To verify the 8% saving, you need to know the **current price per stationery item and cleaning product** for each of the five separate suppliers. This allows you to calculate the total current spend and confirm the math.
*   **The timeline for the consolidated supplier:** The note states the manager "collects quotes" but does not specify **when the consolidated supplier will be available** or when the contract will be signed. You need to know if the supplier is ready to start operations immediately or if there is a lead time involved.
*   **The contract duration and renewal terms:** The note mentions signing "this month," but it does not specify the **duration of the contract** or the **renewal terms** (e.g., does the new supplier have a long-term commitment, or will they be replaced in six months?).
*   **The source of the quotes:** The note mentions "quotes I collected," but it does not specify **where these quotes came from** (e.g., direct from the supplier, a third-party vendor, or internal estimates). This affects the reliability of the data.
*   **The nature of the "consolidation":** The note implies a simple merger of five suppliers into one. It does not clarify **how the inventory will be managed** (e.g., will the consolidated supplier handle all items, or will they be split into different product lines?) or if the consolidated entity will have its own dedicated staff.
*   **The financial impact on the department:** While the note mentions an 8% saving, it does not specify **who bears the cost** (the department, the company, or the suppliers) or if the consolidated supplier will require additional capital investment to set up.
*   **The risk of dependency:** Consolidating five suppliers into one creates a single point of failure. The note does not address **risk mitigation strategies** if the consolidated supplier fails or goes out of business.
```


#### pénalité 1.05 — 2/2, diversité 0.98, 15 s

- ✓ ≥4 points parmi la liste (8 vus : lead time, delivery, contract, transition, negotiat, scope)
- ✓ répond en en (vu : en)

```
Before approving this proposal, the operations manager would need to clarify the following critical details:

*   **The specific cost of each supplier:** The note mentions a 24,000,000 XOF annual spend but does not list the individual prices for the five current suppliers. Without these figures, it is impossible to calculate the exact total savings or verify if the 8% figure is accurate.
*   **The cost of the consolidated supplier:** The note states a saving of 8%, but it does not provide the price of the single new supplier. You need this figure to determine the actual dollar amount saved and whether the new price is competitive with current market rates.
*   **The timeline for implementation:** The manager recommends signing the agreement "this month." However, there is no information regarding the lead time required to procure the new supplier or the duration of the transition period. You would need to know if the new supplier can be onboarded immediately or if there are delays that could disrupt operations.
*   **The scope of consolidation:** The note mentions "5 stationery and cleaning suppliers." It does not specify whether these are currently active, inactive, or if some have already been cancelled. You need to know the current status of these five vendors to ensure the consolidation is feasible without losing existing relationships.
*   **The definition of "consolidate":** The note implies a merger of the five suppliers into one entity. It does not clarify if this involves a change in legal entity, a shift from direct procurement to a vendor-managed service (VMS), or a simple price negotiation. You need to understand the operational implications of this structural change.
*   **The source and validity of the quotes:** The note claims "quotes I collected." It does not specify if these are current market quotes, historical data, or internal estimates. Furthermore, it does not mention whether these quotes have been verified by an external third party or audited for accuracy.
*   **Contractual terms and payment terms:** The proposal involves a new supplier. You would need to know the payment terms (e.g., net 30, net 60), delivery lead times, warranty periods, and any penalties for non-performance before making a final decision.
*   **The impact on existing vendors:** Consolidating five suppliers into one might affect how the company currently manages its relationships with them. You would need to understand if this change could negatively impact customer service or supply chain reliability.
```


#### pénalité 1.10 — 2/2, diversité 1.00, 10 s

- ✓ ≥4 points parmi la liste (8 vus : risk, delivery, quality, terminat, contract, service level)
- ✓ répond en en (vu : en)

```
Before approving this proposal, the operations manager would need to clarify several critical points regarding **cost savings**, **risk mitigation**, and **operational feasibility**. Specifically:

*   **Source of Savings:** The note claims an 8% saving on a spend of 24 million XOF. Does this figure represent a reduction in *total annual cost*, or is it based on the current year's spending? If the company has spent less than 24 million XOF last year, the math doesn't add up (an 8% drop would be roughly 1.92 million XOF saved, not 2 million).
*   **Validity of Quotes:** The manager states they have "collected quotes." Have these been verified by an external third party or a qualified supplier? Are there any hidden fees, minimum order quantities (MOQs), or volume discounts that might negate the claimed savings?
*   **Supplier Reliability and Quality:** Consolidating suppliers often leads to supply chain disruptions. Has the manager assessed whether consolidating 5 distinct entities into one will maintain product quality, delivery timelines, and service levels?
*   **Contractual Obligations:** Are there existing contracts with any of these five suppliers that cannot be terminated immediately without penalty or notice periods?
*   **Implementation Timeline:** The note suggests signing the deal "this month." Does this timeline allow for the necessary due diligence, contract negotiation, legal review, and procurement processes required to execute such a significant change?
*   **Risk Assessment:** What are the potential risks of consolidating these suppliers (e.g., loss of competitive pricing power, reduced bargaining leverage)? Is there a contingency plan if the new supplier fails to meet quality standards or delivery commitments?
```


### priorisation · analyser · direction · Ouagadougou · fr

> Tu assistes le gérant d'une PME de 25 personnes à Ouagadougou. Classe les quatre actions suivantes de la plus urgente à la moins urgente, avec une justification d'une ligne chacune.
> 
> a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.
> b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.
> c) Recruter un stagiaire pour la rentrée de septembre.
> d) Répondre à un appel d'offres public qui ferme dans 3 jours.
> 


#### pénalité 1.00 — 4/4, diversité 0.95, 9 s

- ✓ ≥2 points parmi la liste (4 vus : 3 jours, penalite, 40 jours, expire)
- ✓ « appel d'offres » avant « stagiaire »
- ✓ « facture » avant « stagiaire »
- ✓ répond en fr (vu : fr)

```
Voici la classification des actions, de la plus urgente à la moins urgente, avec une justification par ligne :

**a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.**
C'est l'action la plus urgente car l'absence de paiement entraîne des pénalités financières immédiates et potentiellement des poursuites judiciaires, ce qui compromet la trésorerie de l'entreprise.

**d) Répondre à un appel d'offres public qui ferme dans 3 jours.**
C'est l'action la plus urgente car elle nécessite une réponse immédiate pour garantir la participation à un appel d'offres critique qui se termine très bientôt, évitant ainsi un risque de perte de projet.

**b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.**
C'est l'action la plus urgente car l'absence de protection informatique expose les données de l'entreprise à des cyberattaques, ce qui peut causer des pertes de données et des dommages réels à l'activité.

**c) Recruter un stagiaire pour la rentrée de septembre.**
C'est l'action la moins urgente car, bien que nécessaire pour l'avenir, elle ne pose pas de risque immédiat et ne compromet pas la survie de l'entreprise dans les semaines à venir.
```


#### pénalité 1.05 — 4/4, diversité 0.97, 11 s

- ✓ ≥2 points parmi la liste (4 vus : 3 jours, penalite, 40 jours, expire)
- ✓ « appel d'offres » avant « stagiaire »
- ✓ « facture » avant « stagiaire »
- ✓ répond en fr (vu : fr)

```
Voici la classification des actions, de la plus urgente à la moins urgente, avec une justification par ligne :

**a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.**
C'est l'action la plus urgente car elle compromet directement la trésorerie de l'entreprise. L'échéance d'une facture de 40 jours en retard expose le gérant à des pénalités financières immédiates et potentiellement irréversibles, ce qui peut mettre en danger la survie de la PME.

**d) Répondre à un appel d'offres public qui ferme dans 3 jours.**
C'est l'action la plus urgente car elle garantit une source de revenus future et sécurise des contrats. Une perte de cette opportunité de 3 jours pourrait entraîner des pertes financières immédiates, tandis que les pénalités de retard (action a) sont déjà en cours ou vont se multiplier.

**b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.**
C'est l'action la plus urgente car elle pose un risque critique de sécurité pour les 25 employés. Un système non protégé expose les données sensibles à des cyberattaques, ce qui peut causer des pertes de données, des interruptions d'activité et une perte de confiance des clients, tout comme le retard financier (action a).

**c) Recruter un stagiaire pour la rentrée de septembre.**
C'est l'action la moins urgente car elle relève de la stratégie à moyen terme. Bien que nécessaire pour l'avenir de l'entreprise, recruter un stagiaire ne pose pas de risque immédiat financier ou opérationnel, et son impact sur les résultats financiers se fera attendre jusqu'à la rentrée de septembre.
```


#### pénalité 1.10 — 4/4, diversité 0.97, 8 s

- ✓ ≥2 points parmi la liste (4 vus : 3 jours, penalite, 40 jours, expire)
- ✓ « appel d'offres » avant « stagiaire »
- ✓ « facture » avant « stagiaire »
- ✓ répond en fr (vu : fr)

```
Voici la classification des actions, de l'urgence la plus forte à la plus faible :

**a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.**
*Justification :* C'est une urgence critique car le non-paiement entraîne immédiatement des pénalités financières et potentiellement un arrêt de service ou l'arrêt du paiement, ce qui compromet la trésorerie immédiate.

**d) Répondre à un appel d'offres public qui ferme dans 3 jours.**
*Justification :* C'est une urgence opérationnelle vitale pour maintenir les contrats existants et sécuriser des nouveaux revenus futurs, car le délai de réponse est très court (3 jours).

**b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.**
*Justification :* C'est une urgence technique importante qui risque d'empêcher l'accès aux données ou au réseau, mais elle ne compromet pas directement les finances ou la production à long terme.

**c) Recruter un stagiaire pour la rentrée de septembre.**
*Justification :* C'est une action stratégique à moyen terme qui vise à renforcer le capital humain et préparer l'avenir, bien que nécessaire, elle n'exige pas d'intervention immédiate.
```
