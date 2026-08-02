# Résumer · rédiger · analyser — q2b-iq4xs (2B)

Le contrôle qui correspond à la définition officielle du domaine
`corporate_enterprise` : *knowledge-work productivity: summarization, drafting,
and analysis for small and medium enterprises*. Température nulle, gabarit de
conversation du GGUF appliqué, critères vérifiables sans avis humain — voir
l'en-tête de `bench/redaction.py` pour la méthode de notation.

**1,00 est le défaut de la chaîne officielle** ; 1,10 est la valeur retenue à
l'étape 3 sur le contrôle arithmétique, remise à l'épreuve ici sur le bon genre.

## Score par épreuve — part des critères tenus

| Épreuve | Genre | Cadre | pen 1.00 | pen 1.05 | pen 1.10 |
|---|---|---|---|---|---|
| cr-chantier | résumer | BTP · Ouagadougou · fr | 7/7 | 6/7 | 6/7 |
| point-flotte | résumer | logistique · sans lieu · en | 7/7 | 7/7 | 7/7 |
| note-conges | résumer | RH · Dakar · fr | 6/6 | 6/6 | 6/6 |
| fil-client | résumer | commerce · Accra · en | 5/6 | 5/6 | 5/6 |
| rapport-sante | résumer | santé · Cotonou · fr | 6/7 | 6/7 | 6/7 |
| relance | rédiger | recouvrement · Abidjan · fr | 8/8 | 8/8 | 8/8 |
| annonce-poste | rédiger | RH · Bamako · en | 7/8 | 7/8 | 8/8 |
| note-coupure | rédiger | informatique · Lomé · fr | 7/7 | 7/7 | 7/7 |
| reponse-reclamation | rédiger | service client · sans lieu · en | 5/6 | 5/6 | 5/6 |
| avenant | rédiger | juridique · Douala · fr | 7/7 | 7/7 | 7/7 |
| manques-devis | analyser | achats · sans lieu · fr | 2/2 ⚠ | 2/2 ⚠ | 2/2 ⚠ |
| risques-contrat | analyser | juridique · sans lieu · en | 2/2 | 2/2 | 2/2 |
| incoherence | analyser | gestion · sans lieu · fr | 2/2 | 1/2 | 1/2 |
| manques-decision | analyser | achats · sans lieu · en | 1/2 ⚠ | 2/2 | 2/2 |
| priorisation | analyser | direction · Ouagadougou · fr | 3/4 | 3/4 | 3/4 |

| Total | | | pen 1.00 | pen 1.05 | pen 1.10 |
|---|---|---|---|---|---|
| **résumer** | 5 épreuves | | **31/33** (94 %) | **30/33** (91 %) | **30/33** (91 %) |
| **rédiger** | 5 épreuves | | **34/36** (94 %) | **34/36** (94 %) | **35/36** (97 %) |
| **analyser** | 5 épreuves | | **10/12** (83 %) | **10/12** (83 %) | **10/12** (83 %) |
| **ensemble** | 15 épreuves | | **75/81** (93 %) | **74/81** (91 %) | **75/81** (93 %) |
| **moyenne par épreuve** | à poids égal | | **91 %** | **90 %** | **91 %** |

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


#### pénalité 1.00 — 7/7, diversité 1.00, 4 s

- ✓ fait : 78
- ✓ fait : 9 jours / neuf jours
- ✓ fait : 41500000 / 41.500.000
- ✓ fait : 30 juin / juin
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
- Gros œuvre achevé à 78 % avec un retard de livraison de ciment de 9 jours dû à une rupture de stock à Lomé.
- Budget consommé à 41 500 000 FCFA contre un budget prévu de 60 000 000 FCFA.
- Client demande d'avancer la réception au 30 juin.
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
- Gros œuvre achevé à 78 % avec un retard de livraison de ciment dû à une rupture de stock à Lomé.
- Budget consommé à 41 500 000 FCFA sur un montant prévu de 60 000 000 FCFA.
- Client exige l'avancement de la réception d'ici le 30 juin.
```


#### pénalité 1.10 — 6/7, diversité 1.00, 4 s

- ✓ fait : 78
- ✗ fait : 9 jours / neuf jours
- ✓ fait : 41500000 / 41.500.000
- ✓ fait : 30 juin / juin
- ✓ exactement 3 puces (vu : 3)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
- Gros œuvre achevé à 78 % avec un retard de livraison de ciment dû à une rupture de stock à Lomé.
- Budget consommé : 41 500 000 FCFA sur un budget prévu de 60 000 000 FCFA, nécessitant l'avancement du projet.
- Client demande d'anticiper la réception au 30 juin pour respecter les délais contractuels.
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
- ✓ ≤ 130 mots (vu : 47)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
The fleet currently stands at 14 vehicles, with three awaiting parts off the road. On-time delivery has declined to 86% from the previous quarter's 92%, while fuel costs increased by 17% following the withdrawal of a subsidy. Additionally, the new depot is scheduled to open in October.
```


#### pénalité 1.05 — 7/7, diversité 1.00, 3 s

- ✓ fait : 14 vehicles / 14 
- ✓ fait : 86
- ✓ fait : 17
- ✓ fait : october
- ✓ ≤ 130 mots (vu : 47)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
The fleet currently stands at 14 vehicles, with three awaiting parts off the road. On-time delivery has declined to 86% from the previous quarter's 92%, while fuel costs increased by 17% following the withdrawal of a subsidy. Additionally, the new depot is scheduled to open in October.
```


#### pénalité 1.10 — 7/7, diversité 1.00, 4 s

- ✓ fait : 14 vehicles / 14 
- ✓ fait : 86
- ✓ fait : 17
- ✓ fait : october
- ✓ ≤ 130 mots (vu : 46)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
The fleet currently stands at 14 vehicles, with three awaiting parts off the road. On-time delivery has declined to 86% from a previous quarter's 92%, while fuel costs increased by 17% following the withdrawal of subsidies. Additionally, the new depot is scheduled for opening in October.
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
- ✓ ≤ 90 mots (vu : 51)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
À compter du 1er septembre, les demandes de congé doivent être déposées au moins quinze jours à l'avance via le formulaire RH-04. Les demandes transmises par courriel ne seront plus acceptées et sont valables uniquement si elles sont traitées dans un délai de cinq jours ouvrés par le chef de service.
```


### fil-client · résumer · commerce · Accra · en

> Three messages from a client thread are below. In two sentences, state what was agreed and what we must do next.
> 
> [1] Client: "Our order GH-2291 for 400 units was due on 12 May. Where is it?"
> [2] Us: "We can ship 250 units this week; the remaining 150 depend on a supplier delivery."
> [3] Client: "Send the 250 now, and confirm a firm date for the rest by Friday."


#### pénalité 1.00 — 5/6, diversité 0.97, 3 s

- ✗ fait : gh-2291
- ✓ fait : 250
- ✓ fait : friday
- ✓ ≤ 90 mots (vu : 41)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We have agreed to ship 250 units immediately and to confirm a firm delivery date for the remaining 150 units by Friday. We must now proceed with shipping the 250 units and prepare the confirmation for the 150 units by Friday.
```


#### pénalité 1.05 — 5/6, diversité 1.00, 3 s

- ✗ fait : gh-2291
- ✓ fait : 250
- ✓ fait : friday
- ✓ ≤ 90 mots (vu : 43)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We have agreed to ship 250 units immediately and will confirm a firm delivery date for the remaining 150 units by Friday. Next, we must send the 250 units now and provide the confirmed date for the rest of the order by Friday.
```


#### pénalité 1.10 — 5/6, diversité 1.00, 3 s

- ✗ fait : gh-2291
- ✓ fait : 250
- ✓ fait : friday
- ✓ ≤ 90 mots (vu : 47)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We have agreed to ship 250 units immediately and will confirm a firm delivery date for the remaining 150 units by Friday. Next, we must send the 250 units now while simultaneously tracking the supplier's status to finalize the exact date for the rest of the order.
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
*   1 240 consultations enregistrées avec une hausse de 8 % par rapport au mois précédent.
*   Trois ruptures de stock de médicaments essentiels nécessitent une intervention immédiate.
*   Le groupe électrogène est en panne depuis le 4 mai, impactant les activités de santé.
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
*   1 240 consultations enregistrées avec une hausse de 8 % par rapport au mois précédent.
*   Trois ruptures de stock de médicaments essentiels nécessitent un réapprovisionnement immédiat.
*   Le groupe électrogène est en panne depuis le 4 mai, impactant les activités de la journée.
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
*   1 240 consultations enregistrées avec une hausse de 8 % par rapport au mois précédent.
*   Trois ruptures de stock de médicaments essentiels nécessitent un réapprovisionnement immédiat.
*   Le groupe électrogène est en panne depuis le 4 mai, impactant les activités du centre.
```


### relance · rédiger · recouvrement · Abidjan · fr

> Rédige une première relance de paiement, courtoise, adressée à la Pharmacie Riviera à Abidjan. Facture F-2026-118 d'un montant de 2 350 000 FCFA, échue depuis 22 jours. Demande un règlement sous huit jours et propose un rendez-vous téléphonique si un échéancier est nécessaire. Maximum 120 mots.


#### pénalité 1.00 — 8/8, diversité 1.00, 4 s

- ✓ fait : f-2026-118
- ✓ fait : 2350000 / 2.350.000
- ✓ fait : 22
- ✓ fait : echeancier
- ✓ registre : aucune menace
- ✓ ≤ 180 mots (vu : 65)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Madame, Monsieur,

Je vous adresse cette première relance concernant la facture F-2026-118, d'un montant de 2 350 000 FCFA, échue depuis 22 jours.

Nous vous sollicitons un règlement sous huit jours. Si un échéancier est nécessaire, nous vous proposons un rendez-vous téléphonique pour convenir d'un plan de paiement adapté.

Dans l'attente de votre retour, nous vous prions d'agréer, Madame, Monsieur, l'expression de nos salutations distinguées.
```


#### pénalité 1.05 — 8/8, diversité 1.00, 4 s

- ✓ fait : f-2026-118
- ✓ fait : 2350000 / 2.350.000
- ✓ fait : 22
- ✓ fait : echeancier
- ✓ registre : aucune menace
- ✓ ≤ 180 mots (vu : 70)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Madame, Monsieur,

Je vous adresse cette première relance concernant la facture F-2026-118, d'un montant de 2 350 000 FCFA. Ce paiement est en retard depuis 22 jours.

Nous vous demandons de régler ce solde sous huit jours. Si un échéancier est nécessaire, nous serions ravis de convenir d'un rendez-vous téléphonique pour discuter des modalités.

Dans l'attente de votre retour, nous vous prions d'agréer, Madame, Monsieur, l'expression de nos salutations distinguées.
```


#### pénalité 1.10 — 8/8, diversité 1.00, 5 s

- ✓ fait : f-2026-118
- ✓ fait : 2350000 / 2.350.000
- ✓ fait : 22
- ✓ fait : echeancier
- ✓ registre : aucune menace
- ✓ ≤ 180 mots (vu : 73)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Madame, Monsieur,

Je vous adresse cette première relance concernant la facture F-2026-118 (montant : 2 350 000 FCFA), échue depuis 22 jours.

Nous sollicitons un règlement sous huit jours pour éviter tout retard. Si votre paiement ne peut être effectué immédiatement, nous vous proposons de convenir d'un rendez-vous téléphonique pour discuter d'un échéancier adapté à votre situation.

Dans l'attente de votre confirmation, nous vous prions d'agréer, Madame, Monsieur, l'expression de nos salutations distinguées.
```


### annonce-poste · rédiger · RH · Bamako · en

> Draft a short job advertisement, at most 8 lines, for a logistics coordinator based in Bamako. Requirements: at least 3 years of experience in freight or distribution, working French and English, a driving licence. The contract runs for 12 months, renewable. Applications close on 30 September.


#### pénalité 1.00 — 7/8, diversité 1.00, 4 s

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
You must be fluent in French and English and hold a valid driving licence.
This 12-month contract is renewable upon successful performance.
Applications must be submitted by 30 September.
We look forward to meeting your skills and experience.
Please contact us to discuss how you can contribute to our operations.
Your proactive approach will be valued in our growing logistics network.
Join us today and make a significant impact on our supply chain.
```


#### pénalité 1.05 — 7/8, diversité 1.00, 4 s

- ✓ fait : bamako
- ✓ fait : 3 years / three years
- ✗ fait : 12 month
- ✓ fait : french
- ✓ fait : 30 september / september
- ✓ ≤ 12 lignes (vu : 6)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We are seeking a Logistics Coordinator in Bamako with at least 3 years of experience in freight or distribution.
You must be fluent in French and English, hold a valid driving licence, and demonstrate strong organizational skills.
This role offers a renewable 12-month contract starting immediately.
Please apply by email to [Your Email] with your CV and proof of language proficiency.
Applications close on 30 September.
We look forward to discussing how we can support your career growth together.
```


#### pénalité 1.10 — 8/8, diversité 1.00, 4 s

- ✓ fait : bamako
- ✓ fait : 3 years / three years
- ✓ fait : 12 month
- ✓ fait : french
- ✓ fait : 30 september / september
- ✓ ≤ 12 lignes (vu : 5)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We are seeking a Logistics Coordinator in Bamako with at least 3 years of experience in freight or distribution.
You must be fluent in French and English, hold a valid driving licence, and demonstrate strong organizational skills.
This role offers a renewable contract for 12 months, providing excellent opportunities for growth within our logistics network.
Applications are invited to submit your CV and cover letter by 30 September.
We look forward to meeting qualified candidates who can drive efficiency in our operations.
```


### note-coupure · rédiger · informatique · Lomé · fr

> Rédige une note de service annonçant au personnel une interruption du système informatique le samedi 14, de 8 h à 14 h, pour la sauvegarde annuelle. Indique que le service support reste joignable au poste 214. Maximum 100 mots.


#### pénalité 1.00 — 7/7, diversité 1.00, 3 s

- ✓ fait : samedi 14 / le 14
- ✓ fait : 8 h / 8h / huit heures
- ✓ fait : 214
- ✓ fait : sauvegarde
- ✓ ≤ 150 mots (vu : 45)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
**Note de service : Interruption du système informatique**

Le système informatique est en maintenance du samedi 14, de 08h00 à 14h00. Cette interruption est nécessaire pour la sauvegarde annuelle des données.

Le service support reste joignable au poste 214.

Nous vous remercions de votre compréhension.
```


#### pénalité 1.05 — 7/7, diversité 1.00, 3 s

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

Le support technique reste joignable au poste 214.

Nous vous remercions de votre compréhension.
```


#### pénalité 1.10 — 7/7, diversité 1.00, 3 s

- ✓ fait : samedi 14 / le 14
- ✓ fait : 8 h / 8h / huit heures
- ✓ fait : 214
- ✓ fait : sauvegarde
- ✓ ≤ 150 mots (vu : 43)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
**Note de service : Interruption du système informatique**

Le samedi 14, de 08h00 à 14h00, le système informatique est hors service pour la sauvegarde annuelle.

Le support technique reste joignable au poste 214. Nous vous remercions d'avance et nous restons à votre disposition.
```


### reponse-reclamation · rédiger · service client · sans lieu · en

> Draft a reply to a customer who complains that their order arrived 6 days late. The cause was a customs hold on the shipment, which we could not control. Offer a 5% credit on their next order. Apologise once, at the beginning, and do not repeat the apology. Maximum 120 words.


#### pénalité 1.00 — 5/6, diversité 1.00, 3 s

- ✗ fait : 6 days / six days
- ✓ fait : customs
- ✓ fait : 5% / 5 %
- ✓ ≤ 180 mots (vu : 50)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We sincerely apologize for the delay in your order. Unfortunately, the shipment was held by customs, an issue we could not control. We understand this caused significant inconvenience.

To make up for this, we will issue a 5% credit on your next order. We hope this helps you move forward.
```


#### pénalité 1.05 — 5/6, diversité 1.00, 3 s

- ✗ fait : 6 days / six days
- ✓ fait : customs
- ✓ fait : 5% / 5 %
- ✓ ≤ 180 mots (vu : 45)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We sincerely apologize for the delay in your order. Unfortunately, a customs hold prevented us from shipping sooner, an issue we could not control.

To make this right, we will issue a 5% credit toward your next purchase. We hope this helps you move forward.
```


#### pénalité 1.10 — 5/6, diversité 1.00, 3 s

- ✗ fait : 6 days / six days
- ✓ fait : customs
- ✓ fait : 5% / 5 %
- ✓ ≤ 180 mots (vu : 56)
- ✓ répond en en (vu : en)
- ✓ aucun nombre inventé

```
We sincerely apologize for the delay in your order. Unfortunately, a customs hold prevented us from shipping sooner than expected. We understand this caused significant inconvenience and will offer you a 5% discount on your next purchase as a gesture of goodwill. Please let us know if you would like to proceed with the credit application.
```


### avenant · rédiger · juridique · Douala · fr

> Rédige l'article unique d'un avenant prolongeant le contrat de prestation n° C-2025-07 de six mois, soit du 1er juillet au 31 décembre 2026, à conditions financières inchangées. Style juridique sobre, un seul paragraphe, pas de commentaire.


#### pénalité 1.00 — 7/7, diversité 1.00, 3 s

- ✓ fait : c-2025-07
- ✓ fait : 31 decembre
- ✓ fait : 1er juillet
- ✓ fait : inchang / sans modification / identique / demeurent
- ✓ ≤ 160 mots (vu : 49)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Avenant n° 1 au contrat de prestation n° C-2025-07, par lequel le présent avenant est signé le [Date], prolonge la durée du contrat pour une période de six mois, soit du 1er juillet 2026 au 31 décembre 2026, sans modification des conditions financières et des obligations contractuelles en vigueur.
```


#### pénalité 1.05 — 7/7, diversité 1.00, 3 s

- ✓ fait : c-2025-07
- ✓ fait : 31 decembre
- ✓ fait : 1er juillet
- ✓ fait : inchang / sans modification / identique / demeurent
- ✓ ≤ 160 mots (vu : 49)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Avenant n° 1 au contrat de prestation n° C-2025-07, par lequel le présent avenant est signé le [Date], prolonge la durée du contrat pour une période de six mois, soit du 1er juillet 2026 au 31 décembre 2026, sans modification des conditions financières et des obligations contractuelles en vigueur.
```


#### pénalité 1.10 — 7/7, diversité 1.00, 4 s

- ✓ fait : c-2025-07
- ✓ fait : 31 decembre
- ✓ fait : 1er juillet
- ✓ fait : inchang / sans modification / identique / demeurent
- ✓ ≤ 160 mots (vu : 46)
- ✓ répond en fr (vu : fr)
- ✓ aucun nombre inventé

```
Avenant n° 1 au contrat de prestation n° C-2025-07, par lequel le présent avenant est signé et reçu à l'effet d'étendre la durée du contrat pour une période de six mois, soit du 1er juillet 2026 au 31 décembre 2026, sans modification des conditions financières applicables.
```


### manques-devis · analyser · achats · sans lieu · fr

> Voici un devis reçu d'un prestataire. Indique les informations qui manquent pour qu'un acheteur puisse le comparer et le signer.
> 
> Devis n° 88 — Kando Services. Objet : maintenance du parc informatique. Montant : 1 500 000 FCFA. Signature du gérant.


#### pénalité 1.00 — 2/2, diversité 1.00, 22 s, coupé au budget

- ✓ ≥4 points parmi la liste (8 vus : delai, duree, taxe, paiement, reglement, detail)
- ✓ répond en fr (vu : fr)

```
Pour qu'un acheteur puisse comparer ce devis avec d'autres offres et le signer avec confiance, il est impératif d'ajouter des **informations techniques, financières et contractuelles**. Le devis actuel est trop vague pour être jugé.

Voici les éléments manquants et les conseils pour les compléter :

### 1. Les informations techniques (Le "Comment" et le "Quoi")
L'acheteur ne doit pas savoir *qui* fait le travail, mais *comment* il le fait.
*   **Liste des équipements à maintenir :** Quel est le matériel spécifique (ordinateurs, serveurs, imprimantes, réseaux) ?
*   **Type de maintenance :** Est-ce une maintenance préventive (planification), corrective (réparation d'un bug) ou une maintenance préventive + corrective ?
*   **Durée estimée :** Combien de jours ou de heures est prévu pour la prestation ?
*   **Horaires de travail :** Les prestataires sont-ils disponibles 24h/24 ou seulement 8h/12h ?
*   **Contraintes de sécurité :** Le prestataire a-t-il des certifications (ISO, sécurité informatique, etc.) ?

### 2. Les informations financières et de paiement (Le "Coût")
C'est souvent le point de friction principal.
*   **Détail du montant :** Le devis affiche un total de 1 500 000 FCFA. Est-ce le prix total final ou un prix de départ ? S'il y a des frais cachés (taxe, frais de dossier, assurance), ils doivent être listés.
*   **Modalités de paiement :** Comment le paiement sera-t-il effectué ? (Virement bancaire, chèque, paiement à la réception, acompte ?)
*   **Date de paiement :** À quel moment le client doit-il payer ?
*   **Taux de change :** Si le devis est en FCFA mais les factures sont en Euro, mentionnez le taux de change applicable.

### 3. Les informations contractuelles et légales (Le "Règlement")
Ces éléments sont cruciaux pour éviter les litiges.
*   **Durée du contrat :** Combien de temps la prestation dure-t-elle ? (Ex: 3 mois, 6 mois, 1 an).
*   **Clause de résiliation :** Comment peut le client annuler le contrat ? (Délai de préavis, pénalité de rupture).
*   **Confidentialité :** Le prestataire a-t-il des accords de confidentialité avec le client ?
*   **Assurance :** Le prestataire est-il couvert par une assurance responsabilité civile ou professionnelle ?
*   **Gestion des incidents :** Que se passe-t-il si un équipement tombe en panne pendant la période de maintenance ? (Délai de réparation, coût de la réparation).

### 4. Les informations de contact et de signature
*   **Coordonnées du prestataire :** Adresse physique, email, téléphone, site web.
*   **Signature :** Il faut une signature manuscrite ou numérique valide.
*   **Date et lieu de signature :** Indispensables pour la traçabilité.

---

### Exemple de version améliorée du devis

Voici comment votre devis actuel pourrait être structuré pour être professionnel
```


#### pénalité 1.05 — 2/2, diversité 0.99, 22 s, coupé au budget

- ✓ ≥4 points parmi la liste (8 vus : duree, tva, taxe, paiement, detail, date)
- ✓ répond en fr (vu : fr)

```
Pour qu'un acheteur puisse comparer ce devis avec d'autres offres et le signer avec confiance, il est impératif de compléter les **informations manquantes** suivantes :

### 1. Les détails du prestataire (Kando Services)
*   **L'adresse physique complète** (pas seulement "à la maison" ou "à l'entreprise").
*   **Le numéro de téléphone et l'email professionnel**.
*   **La nature exacte de l'entreprise** (si c'est une société, un particulier, une agence, etc.).
*   **L'expérience antérieure** : Nombre d'années d'existence, nombre de projets similaires réalisés pour ce type de maintenance.

### 2. La liste détaillée des services (Le "Scope")
Le devis mentionne "maintenance du parc informatique" mais ne précise pas **quoi** exactement est inclus. Il faut savoir si le client doit :
*   Acheter les équipements (ordinateurs, serveurs, imprimantes).
*   Les louer ou les sous-louer.
*   Les entretenir (nettoyage, changement de batteries, mise à jour du système d'exploitation).
*   Les remplacer en cas de panne.
*   **La durée du contrat** : Est-ce un devis pour 1 an, 3 ans ou une durée indéterminée ?

### 3. La liste détaillée des prestations (Le "Scope")
Il faut savoir si le prestataire s'engage à :
*   Effectuer les tâches quotidiennes (maintenance courante).
*   Réparer les pannes spécifiques.
*   Fournir une assistance technique en cas de problème.
*   **Les heures de disponibilité** : Le client peut-il contacter le prestataire 24h/7 ou seulement entre 8h et 18h ?

### 4. Les conditions financières et contractuelles
*   **Le montant total** : Il est déjà indiqué (1 500 000 FCFA), mais il faut vérifier s'il y a des frais cachés (taxe, TVA, frais de déplacement, frais de signature).
*   **La date de début et de fin** du contrat.
*   **Le mode de paiement** : Est-ce à la réception du devis, à la signature, ou à la fin du contrat ?
*   **Les conditions de résiliation** : Peut-on annuler le contrat facilement ?

### 5. Les garanties et assurances
*   **Garantie de performance** : Si l'équipement tombe en panne après 1 an, est-ce couvert ?
*   **Assurance responsabilité civile** : Le prestataire est-il couvert par une assurance qui protège le client en cas de dégâts causés par son matériel ?

### 6. Les conditions de paiement et de livraison
*   **Lors de la livraison** : Est-ce que le client doit payer avant que le matériel ne soit livré, ou après ?
*   **Le mode de paiement** : Virement bancaire, chèque, paiement à la réception (net) ?

### 7. Les clauses de confidentialité et de propriété intellectuelle
*   Le client souhaite-t-il que les données de son parc informatique soient traitées en toute confidentialité ?
*   Qui possède les logiciels ou les équipements fournis ? (Le
```


#### pénalité 1.10 — 2/2, diversité 1.00, 22 s, coupé au budget

- ✓ ≥4 points parmi la liste (5 vus : duree, paiement, detail, date, garantie)
- ✓ répond en fr (vu : fr)

```
Pour qu'un acheteur puisse comparer ce devis avec d'autres offres et le signer avec confiance, il est impératif de compléter les **informations manquantes** suivantes :

### 1. Les détails du prestataire (Kando Services)
*   **L'adresse physique complète :** Où se trouve l'équipe ? (Région, ville, code postal). Cela permet d'identifier le site et de vérifier la légitimité de l'entreprise.
*   **Le numéro de téléphone et l'email officiel :** Pour une communication rapide en cas de problème technique ou pour confirmer les disponibilités.
*   **La nature exacte du contrat (Optionnel mais recommandé) :** Est-ce un devis à durée déterminée, une maintenance annuelle, ou une prestation ponctuelle ? Cela influence le montant final et la responsabilité du prestataire.

### 2. Les détails techniques de l'offre (Maintenance du parc informatique)
*   **La liste des équipements concernés :** Le devis mentionne "parc informatique" mais ne précise pas quels ordinateurs, serveurs, imprimantes ou périphériques sont inclus dans les 1 500 000 FCFA.
    *   *Exemple :* "Inclus : PC de bureau (20), Serveur d'exploitation (1), Impressionneuse laser (1)".
*   **La période de couverture :** La maintenance dure-t-elle un an, deux ans ou une durée spécifique ?
*   **Les heures de fonctionnement :** Est-ce 7j/7 et 24h/24, ou seulement les jours ouvrés ?
*   **Le type d'intervention :** Est-ce uniquement la réparation (maintenance corrective) ou aussi la prévention (maintenance préventive) ?

### 3. Les conditions financières et contractuelles
*   **La date de paiement :** Le devis ne précise pas quand l'argent sera payé (avant, à la réception des travaux, à la fin du contrat).
*   **Le mode de paiement :** Est-ce en espèces, par virement bancaire, ou via un système de facturation électronique ?
*   **Les conditions de garantie et de rétractation :** Si le client ne satisfait pas les exigences (ex: 30 jours), quel est le montant à payer pour annuler l'offre ?

### 4. Les informations légales et de sécurité
*   **Le numéro d'immatriculation fiscale du prestataire :** Indispensable pour la fiscalité et la vérification de l'identité de Kando Services.
*   **La signature numérique ou le sceau officiel :** Le devis doit être signé par une personne habilitée (le gérant) avec un sceau de l'entreprise, pas seulement une signature manuscrite sur du papier blanc.

---

### Exemple de version complète à signer

Voici comment votre devis actuel devrait apparaître pour être complet et professionnel :

> **DEVIS N° 88**
> **Prestataire :** Kando Services
> **Objet :** Maintenance du parc informatique (20 PC, 1 Serveur)
> **Montant total :** 1 500 000 FCFA
>
> **Détails de l'offre :**
> *   Période : 12 mois à compter de la signature.
```


### risques-contrat · analyser · juridique · sans lieu · en

> You advise a 30-person company. Read this contract excerpt and name the three clauses that carry the most risk for us, and say why in one line each.
> 
> Excerpt: "(4) The Customer's liability under this agreement is unlimited. (7) The Supplier may revise prices at any time upon written notice. (9) Invoices issued by the Supplier are payable 90 days from receipt. (12) This agreement renews automatically for successive 12-month terms unless terminated 6 months before expiry."


#### pénalité 1.00 — 2/2, diversité 0.95, 4 s

- ✓ ≥4 points parmi la liste (7 vus : liabilit, unlimited, price, renew, automatic, terminat)
- ✓ répond en en (vu : en)

```
1. **Clause (4)** carries the most risk because an unlimited liability clause removes any cap on damages, allowing the Supplier to potentially recover the entire value of the goods or services if the Customer defaults, which could bankrupt the Company.
2. **Clause (7)** carries the most risk because the Supplier's unilateral right to change prices without notice gives them the power to inflate costs and pass those increases entirely to the Company.
3. **Clause (12)** carries the most risk because the automatic renewal clause ensures the Company is bound by the same unfavorable terms indefinitely without needing to renegotiate or terminate the contract.
```


#### pénalité 1.05 — 2/2, diversité 1.00, 4 s

- ✓ ≥4 points parmi la liste (6 vus : liabilit, unlimited, renew, automatic, terminat, lock)
- ✓ répond en en (vu : en)

```
1. **Clause (4)** carries the most risk because an unlimited liability clause removes any cap on damages, allowing the Supplier to potentially recover costs far exceeding the actual value of the goods or services provided.
2. **Clause (7)** poses significant risk as it grants the Supplier unilateral pricing power without a review mechanism, making it difficult for you to negotiate fair market rates in the future.
3. **Clause (12)** creates an indefinite renewal trap where the contract automatically extends indefinitely unless explicitly terminated 6 months before expiry, effectively locking you into the agreement forever.
```


#### pénalité 1.10 — 2/2, diversité 1.00, 5 s

- ✓ ≥4 points parmi la liste (7 vus : liabilit, unlimited, price, renew, automatic, terminat)
- ✓ répond en en (vu : en)

```
1. **Clause (4)** carries the most risk because an unlimited liability clause removes any cap on damages, allowing you to be held responsible for losses that could theoretically exceed your company's assets or cash flow.
2. **Clause (7)** poses a severe financial threat as it grants the Supplier unilateral power to change prices at any time without notice, potentially eroding margins and forcing immediate price hikes if market conditions worsen.
3. **Clause (12)** creates an indefinite renewal trap where the contract automatically extends for 12 months unless you explicitly terminate six months in advance, making it nearly impossible to exit the agreement or renegotiate terms later.
```


### incoherence · analyser · gestion · sans lieu · fr

> Ce tableau de bord contient une incohérence. Trouve-la et donne le chiffre correct.
> 
> Tableau de bord — mois de juin. Chiffre d'affaires : 45 000 000 FCFA. Taux de marge annoncé : 30 %. Marge brute annoncée : 18 000 000 FCFA. Charges fixes : 9 000 000 FCFA.


#### pénalité 1.00 — 2/2, diversité 0.94, 14 s

- ✓ fait : 13500000 / 13.500.000 / 13,5 / 40 % / 40%
- ✓ répond en fr (vu : fr)

```
Il y a une **incohérence** dans les chiffres de la marge brute annoncée.

Pour vérifier la cohérence, nous devons comparer la **marge brute** avec la **marge nette** (le résultat final après avoir déduit les charges fixes).

1.  **Calcul de la marge nette annoncée** :
    $$ \text{Marge nette} = \text{Marge brute} - \text{Charges fixes} $$
    $$ \text{Marge nette} = 18\,000\,000 - 9\,000\,000 = 9\,000\,000 \text{ FCFA} $$

2.  **Vérification avec le chiffre d'affaires** :
    Le chiffre d'affaires annoncé est de 45 000 000 FCFA.
    Le taux de marge annoncé est de 30 %.
    $$ 45\,000\,000 \times 0,30 = 13\,500\,000 \text{ FCFA} $$

**Analyse de l'incohérence :**
Il y a une contradiction entre le taux de marge (30 %) et la marge brute annoncée (18 000 000 FCFA).
*   Si le taux de marge est bien de 30 %, la marge brute devrait être de **13 500 000 FCFA**.
*   Si la marge brute est bien de 18 000 000 FCFA, le taux de marge réel serait de environ **40 %** ($18M / 45M$).

Le tableau de bord contient une erreur dans la **marge brute annoncée**.

**Chiffre correct :**
Le chiffre correct pour la marge brute, si le taux de marge est bien de 30 %, est de **13 500 000 FCFA**.
```


#### pénalité 1.05 — 1/2, diversité 0.99, 8 s

- ✗ fait : 13500000 / 13.500.000 / 13,5 / 40 % / 40%
- ✓ répond en fr (vu : fr)

```
Il y a une **incohérence** dans les chiffres de la marge brute annoncée.

Pour vérifier l'exactitude, nous devons appliquer la formule de base :
$$Marge Brute = Chiffre d'affaires - Charges fixes$$

En utilisant les valeurs fournies dans le tableau :
*   Chiffre d'affaires : 45 000 000 FCFA
*   Charges fixes : 9 000 000 FCFA

Le calcul donne :
$$45\,000\,000 - 9\,000\,000 = 36\,000\,000 \text{ FCFA}$$

Le chiffre de la marge brute annoncé dans le tableau (18 000 000 FCFA) est donc **faux**. Il semble qu'il y ait une erreur de transcription ou d'écriture dans le document original (probablement un oubli d'un chiffre 3 devant les 6 millions).

**Chiffre correct :**
La marge brute annoncée doit être **36 000 000 FCFA**.
```


#### pénalité 1.10 — 1/2, diversité 1.00, 9 s

- ✗ fait : 13500000 / 13.500.000 / 13,5 / 40 % / 40%
- ✓ répond en fr (vu : fr)

```
Il y a une **incohérence** dans les chiffres de la marge brute annoncée.

Pour vérifier l'exactitude, nous devons appliquer la formule de base :
$$Marge Brute = Chiffre d'affaires - Charges fixes$$

En utilisant les valeurs fournies dans le tableau :
*   Chiffre d'affaires : 45 000 000 FCFA
*   Charges fixes : 9 000 000 FCFA

Le calcul donne une marge brute réelle de **36 000 000 FCFA**.

Cependant, le tableau affiche un chiffre d'affaires qui est **18 000 000 FCFA** (ce qui correspond à la valeur affichée pour la marge brute). Cela crée une contradiction :
*   Si on prend le chiffre d'affaires réel (45 M) et les charges fixes (9 M), la marge brute réelle est de **36 M**.
*   Le tableau affiche une marge brute fictive de **18 M**, ce qui serait impossible si l'on partait du chiffre d'affaires réel.

**Le chiffre correct pour la marge brute annoncée est :**
**36 000 000 FCFA**
```


### manques-decision · analyser · achats · sans lieu · en

> An operations manager sends the note below. List what the note does not tell you but that you would need before approving it.
> 
> Note: "I propose we consolidate our 5 stationery and cleaning suppliers into a single one. The quotes I collected show an 8% saving on our current annual spend of 24,000,000 XOF. I recommend we sign this month."


#### pénalité 1.00 — 1/2, diversité 0.60, 22 s, coupé au budget

- ✗ ≥4 points parmi la liste (1 vus : baseline)
- ✓ répond en en (vu : en)

```
Before approving this proposal, you would need to gather the following critical information:

1.  **The specific cost of the 5 current suppliers**
    *   *Why:* To calculate the actual dollar amount of the 24,000,000 XOF figure. You cannot verify if an 8% saving is real without knowing the baseline cost.
    *   *Calculation:* $24,000,000 \div 1.08 \approx 22,222,222$ XOF (Current Total Spend).

2.  **The specific cost of the consolidated supplier**
    *   *Why:* To determine the true savings. The note claims an 8% saving, but you need to know the exact price of the new supplier to see if the math holds up.
    *   *Calculation:* $22,222,222 \times 0.08 \approx 1,777,777$ XOF (Expected Savings).

3.  **The price of the consolidated supplier**
    *   *Why:* To verify the 8% saving claim. If the new supplier is significantly cheaper than the average of the 5 current suppliers, the "saving" might be overstated, or the 8% might be an error.
    *   *Calculation:* $22,222,222 \times 0.08 = 1,777,777$ XOF.

4.  **The price of the 5 current suppliers**
    *   *Why:* To ensure the 8% saving is accurate. If the current suppliers are already very cheap, the 8% saving might be negligible or incorrect.
    *   *Calculation:* Sum of the 5 supplier prices.

5.  **The price of the consolidated supplier**
    *   *Why:* To verify the 8% saving claim.
    *   *Calculation:* Sum of the 5 supplier prices.

6.  **The price of the consolidated supplier**
    *   *Why:* To verify the 8% saving claim.
    *   *Calculation:* Sum of the 5 supplier prices.

7.  **The price of the consolidated supplier**
    *   *Why:* To verify the 8% saving claim.
    *   *Calculation:* Sum of the 5 supplier prices.

8.  **The price of the consolidated supplier**
    *   *Why:* To verify the 8% saving claim.
    *   *Calculation:* Sum of the 5 supplier prices.

9.  **The price of the consolidated supplier**
    *   *Why:* To verify the 8% saving claim.
    *   *Calculation:* Sum of the 5 supplier prices.

10. **The price of the consolidated supplier**
    *   *Why:* To verify the 8% saving claim.
    *   *Calculation:* Sum of the 5 supplier prices.

11. **The price of the consolidated supplier**
    *   *Why:* To verify the 8% saving claim.
    *   *Calculation:* Sum of the
```


#### pénalité 1.05 — 2/2, diversité 0.99, 9 s

- ✓ ≥4 points parmi la liste (6 vus : risk, terminat, contract, transition, breakdown, individual)
- ✓ répond en en (vu : en)

```
Before approving this proposal, you would need to gather the following critical information:

1.  **The specific cost of each individual supplier** (to calculate the exact total spend before consolidation).
2.  **The current contract terms and renewal dates** for all five suppliers (to ensure the savings are not lost if a new contract is signed immediately).
3.  **The financial impact on cash flow**, specifically whether the consolidated payment schedule will be more or less favorable than the current staggered payments.
4.  **A detailed breakdown of the "8% saving"** to verify that it applies to the *total* spend or if it is a per-item discount, and to confirm the calculation method (e.g., is it based on volume, price, or a mix of both?).
5.  **The specific timeline for the new consolidated contract** (to ensure the savings are realized within the "sign this month" timeframe).
6.  **Potential risks associated with consolidation**, such as loss of competitive pricing power if the new supplier is less flexible than the current ones, or potential service degradation due to reduced competition.
7.  **The cost of switching suppliers** (e.g., transition fees, contract termination penalties, or the cost of retraining staff).
```


#### pénalité 1.10 — 2/2, diversité 1.00, 10 s

- ✓ ≥4 points parmi la liste (8 vus : contract, transition, negotiat, what is included, breakdown, validity)
- ✓ répond en en (vu : en)

```
Before approving this proposal, you would need to gather the following critical information:

1.  **The specific cost of each individual supplier** (to calculate the exact total spend before consolidation).
2.  **A detailed breakdown of what is included in "stationery and cleaning"** for each of the five suppliers (e.g., are they separate categories, or does one supplier provide both?). This ensures you aren't double-counting costs if the consolidated quote bundles services differently than your current setup.
3.  **The validity period of the quotes** provided by the new single supplier. Are these valid for a specific duration? If not, how long will they remain valid to ensure the savings are realized without needing to renegotiate immediately?
4.  **A clear definition of "consolidate"** (e.g., does this mean one physical location, one contract with one vendor, or simply combining their billing cycles?). Ambiguity here can lead to unexpected administrative costs or service disruptions.
5.  **The specific items included in the quotes** versus what is currently being purchased separately. You need to know if the new supplier offers any services your current five suppliers do not (which could be a hidden benefit) or if they are strictly replacing existing ones without adding value.
6.  **A timeline for implementation**. When will the consolidation actually happen? Is there a transition period where you might still pay both old and new rates, which would negate the projected savings?
```


### priorisation · analyser · direction · Ouagadougou · fr

> Tu assistes le gérant d'une PME de 25 personnes à Ouagadougou. Classe les quatre actions suivantes de la plus urgente à la moins urgente, avec une justification d'une ligne chacune.
> 
> a) Une facture fournisseur est échue depuis 40 jours et génère des pénalités de retard.
> b) L'abonnement antivirus du parc informatique a expiré la semaine dernière.
> c) Recruter un stagiaire pour la rentrée de septembre.
> d) Répondre à un appel d'offres public qui ferme dans 3 jours.
> 


#### pénalité 1.00 — 3/4, diversité 1.00, 7 s

- ✓ ≥2 points parmi la liste (4 vus : 3 jours, penalite, 40 jours, expire)
- ✗ « appel d'offres » avant « stagiaire »
- ✓ « facture » avant « stagiaire »
- ✓ répond en fr (vu : fr)

```
a) **Facture échue (40 jours)** : Urgence maximale. Une dette de 40 jours génère des pénalités lourdes et pose un risque de litige ou de faillite, nécessitant une action immédiate pour rétablir la trésorerie.
b) **Abonnement antivirus expiré** : Urgence très élevée. L'absence de protection informatique expose les 25 employés à des cyber-risques critiques, ce qui compromet la continuité des opérations et la sécurité des données.
c) **Recrutement stagiaire** : Urgence modérée. Bien que nécessaire pour la rentrée de septembre, ce processus prend du temps et ne compromet pas l'activité immédiate de l'entreprise.
d) **Appel d'offres public** : Urgence faible. Avec 3 jours de délai, ce projet est à la limite de l'urgence mais reste prioritaire par rapport aux risques financiers et de sécurité (a et b).
```


#### pénalité 1.05 — 3/4, diversité 1.00, 7 s

- ✓ ≥2 points parmi la liste (3 vus : penalite, 40 jours, expire)
- ✗ « appel d'offres » avant « stagiaire »
- ✓ « facture » avant « stagiaire »
- ✓ répond en fr (vu : fr)

```
a) **Facture échue (40 jours)** : Urgence maximale. Une dette de 40 jours génère des pénalités lourdes et pose un risque de litige ou d'insolvabilité financière immédiate pour la PME.
b) **Abonnement antivirus expiré** : Urgence très élevée. L'absence de protection informatique expose les données sensibles à des cyberattaques, ce qui compromet la continuité des opérations et la réputation de l'entreprise.
c) **Recrutement stagiaire** : Urgence faible. Bien que nécessaire pour le personnel, ce processus est lent et ne pose pas de risque immédiat si un poste est déjà disponible ou si une offre alternative existe.
d) **Appel d'offres public** : Urgence modérée. C'est une obligation légale à respecter dans les délais, mais la marge de manœuvre reste suffisante pour préparer le dossier sans compromettre l'activité principale.
```


#### pénalité 1.10 — 3/4, diversité 1.00, 8 s

- ✓ ≥2 points parmi la liste (4 vus : 3 jours, penalite, 40 jours, expire)
- ✗ « appel d'offres » avant « stagiaire »
- ✓ « facture » avant « stagiaire »
- ✓ répond en fr (vu : fr)

```
a) **Facture échue (40 jours)** : Urgence maximale. Une dette de 40 jours génère des pénalités lourdes et pose un risque de litige ou d'insolvabilité financière immédiate pour la PME.
b) **Abonnement antivirus expiré** : Urgence très élevée. L'informatique est critique pour les opérations quotidiennes ; sans protection, le risque de perte de données ou de piratage est immédiat et coûteux à réparer.
c) **Recrutement stagiaire** : Urgence faible (à moyen terme). Bien que nécessaire pour la rentrée, ce n'est pas une urgence financière ou opérationnelle immédiate comparée aux autres points.
d) **Appel d'offres public** : Urgence modérée à élevée (court terme). Il faut agir rapidement pour ne pas manquer l'appel, mais le délai de 3 jours est généralement suffisant pour la préparation et la soumission sans risque majeur.
```
