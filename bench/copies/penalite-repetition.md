# Pénalité de répétition — q2b-iq4xs (2B)

Fenêtre `repeat_last_n = 64` (défaut llama.cpp), température nulle,
gabarit de conversation du GGUF appliqué. **1,00 = le défaut de la chaîne
officielle**, donc la colonne de référence.

## Forme — proportion de quadrigrammes distincts

En gras sous **0.30** : sortie dégénérée. `⚠` : coupée au budget.

| Épreuve | pen 1.00 | pen 1.05 | pen 1.10 | pen 1.15 | pen 1.20 |
|---|---|---|---|---|---|
| tp_001 | 0.97 | 0.96 | 0.99 | 0.99 | 0.96 ⚠ |
| tp_002 | 1.00 | 1.00 | 0.98 | 0.99 | 0.98 |
| tva | 0.98 | 0.98 | 0.96 | 0.98 | 0.97 |
| remise | 0.94 | 0.97 | 0.99 | 0.98 | 1.00 |
| plafond | 0.97 | 0.98 | 1.00 | 1.00 | 1.00 |
| provision | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| escompte | 0.99 | 0.99 | 0.99 | 1.00 | 0.95 |
| marge | 0.90 | 0.94 | 0.89 | 0.96 | 1.00 |
| retard+plafond | 0.96 | 0.95 | 0.99 | 1.00 | 1.00 |
| remise+tva | 0.97 | 1.00 | 1.00 | 0.97 | 0.97 |
| projection | 0.97 ⚠ | 1.00 ⚠ | 0.98 | 0.98 ⚠ | 0.98 ⚠ |
| coût employeur | 0.94 | 0.98 | 0.97 | 0.96 | 1.00 |
| achat+remise+tva | 0.98 | 0.99 | 0.99 | 1.00 | 1.00 |
| croissance | 1.00 | 0.99 | 0.98 | 0.98 | 1.00 |
| mensualités | 0.95 | 0.98 | 0.99 | 0.99 | 0.99 |
| masse salariale | 0.88 | 0.92 | 0.93 | 0.94 | 0.99 ⚠ |
| comparaison offres | 0.94 | 0.94 | 0.97 | 0.93 | 0.94 |
| pénalité partielle | 0.91 | 0.95 | 0.96 | 0.97 | 0.97 ⚠ |
| loyer indexé | 0.93 | 0.97 | 0.97 | 0.97 | 0.96 |
| régie | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 |
| boucle-1 | **0.05** ⚠ | 1.00 | 1.00 | 1.00 | 1.00 |
| boucle-2 | **0.02** ⚠ | 1.00 | 1.00 | 1.00 | 1.00 |
| boucle-3 | **0.06** ⚠ | **0.09** ⚠ | 1.00 | 1.00 | 1.00 |

## Fond — la bonne valeur est-elle dans la copie ?

| Épreuve | Niveau | Attendu | pen 1.00 | pen 1.05 | pen 1.10 | pen 1.15 | pen 1.20 |
|---|---|---|---|---|---|---|---|
| tva | 1 étape | `2773000` | ✓ | ✓ | ✓ | ✓ | ✓ |
| remise | 1 étape | `1020000` | ✓ | ✓ | ✓ | ✓ | ✓ |
| plafond | 1 étape | `800000` | ✓ | ✓ | ✓ | ✓ | ✓ |
| provision | 1 étape | `2880000` | ✓ | ✓ | ✓ | ✓ | ✓ |
| escompte | 1 étape | `47040` | ✓ | ✓ | ✓ | ✓ | ✓ |
| marge | 1 étape | `37.5` | ✓ | ✓ | ✓ | ✓ | ✗ |
| retard+plafond | n étapes | `225000` | ✗ | ✗ | ✗ | ✗ | ✗ |
| remise+tva | n étapes | `3398400` | ✓ | ✓ | ✓ | ✓ | ✓ |
| projection | n étapes | `29760000` | ✓ | ✗ | ✓ | ✗ | ✗ |
| coût employeur | n étapes | `533025` | ✓ | ✗ | ✗ | ✗ | ✓ |
| achat+remise+tva | n étapes | `1294755` | ✓ | ✓ | ✓ | ✗ | ✗ |
| croissance | n étapes | `25.5` | ✓ | ✓ | ✓ | ✗ | ✗ |
| mensualités | n étapes | `2124000` | ✓ | ✓ | ✓ | ✓ | ✗ |
| masse salariale | n étapes | `262959000` | ✗ | ✓ | ✓ | ✓ | ✗ |
| comparaison offres | n étapes | `230000` | ✗ | ✓ | ✓ | ✗ | ✗ |
| pénalité partielle | n étapes | `34800` | ✓ | ✓ | ✓ | ✗ | ✗ |
| loyer indexé | n étapes | `10383360` | ✓ | ✓ | ✓ | ✓ | ✓ |
| régie | n étapes | `4725000` | ✓ | ✓ | ✗ | ✗ | ✓ |
| **total 1 étape** | | | **6/6** | **6/6** | **6/6** | **6/6** | **5/6** |
| **total n étapes** | | | **9/12** | **9/12** | **9/12** | **4/12** | **4/12** |

---

## Copies intégrales


### tp_001 · domaine

> Voici un extrait de contrat fournisseur : « Le prestataire s'engage à livrer sous 30 jours calendaires. Tout retard supérieur à 10 jours ouvre droit à une pénalité de 2 % du montant hors taxes par semaine entamée, plafonnée à 10 %. » La livraison a 25 jours de retard sur une commande de 4 500 000 FCFA HT. Calcule la pénalité due, indique le plafond applicable, et cite la phrase du contrat sur laquelle tu t'appuies.


#### pénalité 1.00 — diversité 0.97, 15 s

Pour calculer la pénalité due, nous devons d'abord déterminer le nombre de semaines entamées par le retard et appliquer la pénalité de 2 % par semaine, en respectant le plafond de 10 %.

**1. Calcul du nombre de semaines entamées**
Le retard total est de 25 jours. Comme la pénalité est calculée par semaine, nous devons diviser le nombre de jours par 7 pour obtenir le nombre de semaines entamées :
$$25 \text{ jours} \div 7 \text{ jours/semaine} = 3 \text{ semaines et } 4 \text{ jours}$$
Le montant de la pénalité ne s'applique donc que sur les **3 semaines entamées**.

**2. Calcul de la pénalité**
La pénalité est de 2 % du montant hors taxes (HT) par semaine.
*   Montant HT : 4 500 000 FCFA
*   Pénalité par semaine : $4\,500\,000 \times 2\% = 90\,000$ FCFA
*   Pénalité sur 3 semaines : $90\,000 \times 3 = 270\,000$ FCFA

**3. Vérification du plafond**
Le contrat stipule que la pénalité est plafonnée à 10 %.
*   Calcul du plafond : $4\,500\,000 \times 10\% = 450\,000$ FCFA
*   Comparaison : Le montant calculé (270 000 FCFA) est inférieur au plafond (450 000 FCFA).
*   Conclusion : Le plafond n'est pas atteint, donc la pénalité due est de **270 000 FCFA**.

**Phrase du contrat à citer :**
« Tout retard supérieur à 10 jours ouvre droit à une pénalité de 2 % du montant hors taxes par semaine entamée, plafonnée à 10 %. »


#### pénalité 1.05 — diversité 0.96, 19 s

Pour calculer la pénalité due, nous devons d'abord déterminer le nombre de semaines entamées par le retard et appliquer les règles de plafonnement du contrat.

**1. Calcul du nombre de semaines entamées**
Le délai de livraison est de 30 jours calendaires. Le retard réel est de 25 jours.
$$ \text{Nombre de semaines} = \frac{\text{Retard}}{\text{Jours par semaine}} = \frac{25}{7} \approx 3,57 \text{ semaines} $$
Puisque le contrat stipule une pénalité par **semaine entamée**, nous comptons les semaines complètes ou partielles. Ici, il s'agit de 3 semaines entières (du jour 1 au jour 21) et la semaine 4 commence à être entamée (du jour 22 au jour 25).
*Note : Dans la pratique contractuelle, si le retard dépasse 7 jours, on compte généralement les semaines complètes. Ici, 25 jours = 3 semaines + 2 jours. La première semaine complète est de 1 à 7 jours, la deuxième de 8 à 14 jours, et la troisième de 15 à 21 jours. La semaine 4 (jour 22-25) est entamée.*
Donc, le nombre de semaines entamées est de **3 semaines**.

**2. Calcul de la pénalité**
Le taux de pénalité est de 2 % du montant hors taxes par semaine entamée.
$$ \text{Pénalité} = 2\% \times 4\,500\,000 \text{ FCFA} \times 3 \text{ semaines} $$
$$ \text{Pénalité} = 0,02 \times 4\,500\,000 \times 3 = 270\,000 \text{ FCFA} $$

**3. Plafonnement**
Le contrat stipule que la pénalité est plafonnée à **10 %** du montant hors taxes.
$$ \text{Plafond} = 10\% \times 4\,500\,000 \text{ FCFA} = 450\,000 \text{ FCFA} $$

Comparons le calcul brut à ce plafond :
$$ 270\,000 \text{ FCFA} < 450\,000 \text{ FCFA} $$
La pénalité due est donc égale au montant du plafond.

**Conclusion :**
*   **Pénalité due :** 270 000 FCFA
*   **Plafonnement applicable :** 10 % du montant hors taxes (soit 450 000 FCFA)
*   **Phrase du contrat :** « Tout retard supérieur à 10 jours ouvre droit à une pénalité de 2 % du montant hors taxes par semaine entamée, plafonnée à 10 %. »


#### pénalité 1.10 — diversité 0.99, 14 s

Pour calculer la pénalité due, nous devons d'abord déterminer le nombre de semaines entamées par le retard et appliquer les règles de plafonnement du contrat.

**1. Calcul du nombre de semaines entamées :**
Le délai de livraison est fixé à 30 jours calendaires. Le retard réel est de 25 jours.
$$ \text{Nombre de semaines} = \frac{\text{Délai total (jours)} - \text{Délai contractuel (jours)}}{\text{Jours par semaine}} $$
$$ \text{Nombre de semaines} = \frac{30 - 25}{7} = \frac{5}{7} \approx 0,714 \text{ semaines} $$

**2. Application des règles de pénalité :**
Le contrat stipule une pénalité de **2 % par semaine entamée**, plafonnée à un maximum de **10 %**.
*   Calcul sans plafond : $5/7$ semaines $\times 2\% \approx 1,43 \%$.
*   Comparaison avec le plafond : Le montant calculé ($1,43 \%$) est inférieur au plafond maximal ($10 \%$).

Par conséquent, la pénalité due correspond exactement à **1,43 %** du montant de la commande.

**3. Calcul de l'importance financière :**
Montant total de la commande : 4 500 000 FCFA HT.
Pénalité due : $4\,500\,000 \times 1,43 \% = 63\,450$ FCFA HT.

**Conclusion :**
La pénalité due est de **63 450 FCFA HT**. Le plafond applicable n'est pas atteint (le calcul se situe à 1,43 %), donc le montant total ne peut être plafonné à 10 %.

**Phrase du contrat citée :**
> « Tout retard supérieur à 10 jours ouvre droit à une pénalité de 2 % du montant hors taxes par semaine entamée, plafonnée à 10 %. »


#### pénalité 1.15 — diversité 0.99, 17 s

Pour calculer la pénalité due, nous devons d'abord déterminer le nombre de semaines entamées par un retard supérieur à 10 jours.

**Calcul du délai :**
Le contrat stipule que tout retard **supérieur à 10 jours** ouvre droit à une pénalité. Le retard total est de **25 jours**.
*   Temps écoulé : 25 jours.
*   Délai limite (seuil) : 10 jours.
*   Différence (délai supplémentaire) : $25 - 10 = 15$ jours.

**Calcul du nombre de semaines :**
Il faut diviser le délai supplémentaire par la durée d'une semaine (7 jours).
$$ \frac{15}{7} \approx 2,14 $$
Ce résultat est supérieur à 1, donc nous devons compter **3 semaines entières**.

*Note : Dans les contrats de type "jours calendaires", une fraction de jour supplémentaire ne compte généralement pas pour atteindre le seuil d'entité (ex: si un retard était de 26 jours, c'est encore 4 semaines. Ici, 15 jours équivaut à environ 3 semaines et demie).*

**Calcul du montant :**
Le taux de pénalité est de **2 % par semaine**. Le plafond est fixé à **10 %**.
*   Taux applicable : $3 \text{ semaines} \times 2\% = 6 \%$.
*   Montant total (avant plafonnement) : $4\,500\,000 \text{ FCFA HT} \times 6\% = 270\,000 \text{ FCFA HT}$.

**Analyse du plafond :**
Le montant calculé ($270\,000$) est inférieur au plafond maximum de $10 \%$ du montant total. Par conséquent, le plafond n'est pas atteint et la pénalité totale correspond exactement à ce montant.

---

### Conclusion

*   **Pénalité due :** **270 000 FCFA HT**
    *(Calcul : $4\,500\,000 \times 6\%$)*
*   **Plafond applicable :** Le plafond de **10 %** n'est pas atteint car le montant calculé (270 000 FCFA) est inférieur à ce plafond.
*   **Phrase du contrat citée :** « Tout retard supérieur à 10 jours ouvre droit à une pénalité de 2 % du montant hors taxes par semaine entamée, plafonnée à 10 %. »


#### pénalité 1.20 — diversité 0.96, 31 s, coupé

Pour calculer la pénalité due, nous devons d'abord déterminer le nombre de semaines entamées par un retard supérieur à 10 jours.

**Calcul du délai :**
Le contrat stipule que tout retard **supérieur à 10 jours** ouvre droit à une pénalité. Le retard total est de **25 jours**. Comme $25 > 10$, la condition s'applique et nous devons compter les semaines entamées depuis le début du retard (ou, selon l'interprétation standard dans ce type d'exercice, on compte les périodes qui ont dépassé le seuil initial).

*Note : Dans un contrat de cette nature strictement linéaire ("entamée"), il est généralement comptabilisé chaque semaine complète ou fractionnelle après la date limite initiale. Ici, nous considérons que 25 jours correspond à une période continue.*
$$ \text{Période} = 25 \text{ jours} $$

**Calcul du nombre de semaines :**
Pour trouver le nombre de "semaines entamées" dans ce contexte juridique commercial :
1. Le premier jour (ou la première semaine) ne compte pas encore pour une pénalité si elle est strictement liée à l'expiration des 10 jours initiaux, mais souvent les calculs comptent toutes les semaines complètes ou fractionnelles qui ont survécu au seuil de départ. Cependant, dans un exercice simple basé sur "semaines entamées" :
   - Si on considère que le retard a commencé à la date du premier jour d'arrétage (ou 10 jours après), il faut voir combien de semaines complètes ou partielles ont été comptabilisées.
   
   *Interprétation standard pour ce type de problème :* On compte les périodes qui ont dépassé le seuil initial. Si la pénalité commence à partir du jour où l'arrêté est fait (ou 10 jours après), et que nous sommes au jour $X$, on calcule combien de semaines complètes ou partielles s'étendent depuis ce point jusqu'à aujourd'hui, en respectant souvent le principe "entamée" qui signifie la durée totale du retard.
   
   Cependant, une lecture plus rigoureuse des phrases juridiques similaires dans les contrats (comme ceux d'ACI) indique que si $25 > 10$, on compte toutes les semaines entières ou partielles de ce délai total jusqu'à présent.
   
   Calculons le nombre de semaines :
   $$ \text{Nombre de semaines} = \frac{\text{Durée du retard}}{\text{Jours par semaine}} = \frac{25}{7} \approx 3,57 \text{ semaines}. $$

   *Correction d'interprétation :* Souvent dans ces exercices simplifiés, on compte les **semaines entières** qui ont écoulé depuis le début du retard jusqu'à la date actuelle.
   - Si nous sommes au jour $X$ et que 25 jours sont passés :
     Semaine 1 (j+0 à j+6) -> Pas encore > 10 ? Non, si on commence à compter de l'arrêté.
     
   *Relecture du texte :* "Tout retard supérieur à 10 jours ouvre droit..."
   Cela signifie que le seuil est franchi dès la fin du 10ème jour (ou début du 11ème).
   Si nous sommes au **25ème jour**, combien de semaines complètes ont-elles écoulé depuis l'arrêté ?
   
   Il y a une ambiguïté sur si le premier jour compte ou non. Prenons la méthode standard : on calcule les périodes entières qui s'étendent du début jusqu'à présent, en supposant que 1 semaine = 7 jours.
   
   Si nous considérons que le retard de **25 jours** a duré toute cette période (de l'arrêté au jour actuel) :
   - Le seuil est à 10 jours.
   - Les semaines entamées sont celles qui ont dépassé ce seuil initial ou toutes les semaines complètes depuis là ? Non, "entamée" signifie la durée totale du retard jusqu'à présent.
   
   Si nous comptons simplement le nombre de périodes de 7 jours incluses dans l'intervalle :
   $$ \text{Nombre de semaines} = \lfloor \frac{25}{7} \rfloor + (\text{fraction}) ? $$
   
   *Approche la plus courante pour ce type d'exercice :* On compte le nombre de **semaines entières** qui ont écoulé depuis l'arrêté jusqu'à aujourd'hui. Si 10 jours sont passés, on a eu une semaine complète (7 jours


### tp_002 · domaine

> You are an offline assistant for a 40-person company. Summarise the following internal note for the management committee in exactly three bullet points, then list any information the note does NOT provide but that a decision-maker would need. Note: "Q3 revenue reached 182M FCFA, up 12% year on year. The Abidjan warehouse ran out of stock twice in September. Two of the four delivery vans were off the road for repairs. The new supplier contract has not been signed."


#### pénalité 1.00 — diversité 1.00, 12 s

*   **Revenue Performance:** Q3 revenue reached 182M FCFA, representing a 12% year-on-year increase.
*   **Operational Challenges:** The Abidjan warehouse experienced two stockouts in September, and two of the four delivery vans were off the road for repairs.
*   **Contract Status:** The new supplier contract has not yet been signed.

**Information Missing for Decision-Making:**
*   **Specific Stockout Details:** The note mentions two stockouts but does not specify which products were out of stock or the quantities affected.
*   **Repair Timeline:** While it states two vans were off the road, it does not provide the estimated duration of the repairs or the expected return-to-service date.
*   **Contract Terms:** The note confirms the contract is not signed but omits details regarding the contract value, payment terms, lead times, or the specific supplier's performance history.
*   **Overall Financial Health:** The note provides only Q3 revenue; it does not include the company's full financial statement, cash flow, or overall profitability for the quarter.
*   **Customer Satisfaction:** There is no data regarding customer complaints, delivery delays, or service level agreements (SLAs) related to the delivery vans.
*   **Warehouse Capacity:** The note mentions the warehouse ran out of stock but does not indicate if the warehouse is currently operating at full capacity or if there is room for expansion.


#### pénalité 1.05 — diversité 1.00, 8 s

*   **Revenue Performance:** Q3 revenue reached 182M FCFA, representing a 12% year-on-year increase.
*   **Operational Challenges:** The Abidjan warehouse experienced two stockouts in September, and two of the four delivery vans were off the road for repairs.
*   **Contract Status:** A new supplier contract has not yet been signed.

**Information Missing from Note:**
*   Specific breakdown of revenue by product line or region to assess market share shifts.
*   Detailed inventory levels at other warehouses (e.g., Dakar, Bissau) to assess overall stock health.
*   The specific financial impact of the two stockouts on Q3 margins or customer satisfaction metrics.
*   The current status and timeline for the new supplier contract (e.g., cost implications, lead times).
*   Maintenance costs incurred by the two off-road vans or the total operational budget required to keep them running.
*   Customer feedback regarding delivery delays or service quality during the period.


#### pénalité 1.10 — diversité 0.98, 7 s

*   **Revenue Performance:** Q3 revenue reached 182M FCFA, representing a 12% year-on-year increase.
*   **Operational Challenges:** The Abidjan warehouse experienced two stockouts in September; delivery vans were off the road for repairs, and a new supplier contract remains unsigned.
*   **Strategic Gap:** There is no mention of specific financial targets or strategic initiatives to address these operational hurdles.

**Information Missing from Note (Required by Decision-Makers):**
*   The total number of deliveries made in Q3 versus the target.
*   The current status and timeline for signing the new supplier contract.
*   Specific reasons why two delivery vans were off the road or if there are plans to replace them.
*   Detailed breakdown of stock levels by product category at the Abidjan warehouse.
*   Any strategic initiatives planned to address the operational challenges identified above.


#### pénalité 1.15 — diversité 0.99, 6 s

*   **Revenue Performance:** Q3 revenue reached 182M FCFA, representing a 12% year-on-year increase.
*   **Operational Challenges:** The Abidjan warehouse experienced two stockouts in September; delivery vans were off the road for repairs, and a new supplier contract remains unsigned.
*   **Strategic Gap:** There is no mention of specific financial targets or strategic initiatives to address these operational hurdles.

**Information Missing from Note (Required by Decision-Makers):**
*   The total number of deliveries made in Q3 versus expected figures.
*   Specific reasons for the two stockouts at the Abidjan warehouse and their impact on customer satisfaction.
*   A detailed breakdown or timeline regarding why a new supplier contract has not been signed despite its importance to operations.


#### pénalité 1.20 — diversité 0.98, 8 s

*   **Revenue Performance:** Q3 revenue reached 182M FCFA, representing a 12% year-on-year increase.
*   **Operational Challenges:** The Abidjan warehouse experienced two stockouts in September; delivery vans were off the road for repairs, and no new supplier contract has been signed yet.
*   **Strategic Gap Identified:** There is currently insufficient data on how these operational issues are impacting customer satisfaction or long-term supply chain stability to inform future planning decisions.

**Information Missing from Note (Required by Decision-Makers):**
1.  The specific financial impact of the stockouts and delays on Q3 revenue margins, profit figures, or cash flow projections for this quarter.
2.  Customer feedback data regarding delivery reliability issues in Abidjan to assess potential churn risks or brand reputation damage.
3.  A timeline or status update from management/finance confirming whether a new supplier contract has been signed and when it will be finalized.


### tva · 1 étape

> Une facture s'élève à 2 350 000 FCFA hors taxes. La TVA applicable en Côte d'Ivoire est de 18 %. Donne le montant toutes taxes comprises.


#### pénalité 1.00 — diversité 0.98, 7 s, **juste**

Pour calculer le montant toutes taxes comprises (MTC), il faut d'abord déterminer la valeur de la TVA, puis l'ajouter au montant hors taxes.

La formule est la suivante :
$$MTC = Montant Hors Taxes + (Montant Hors Taxes \times Taux de TVA)$$

Dans votre cas :
*   Montant Hors Taxes = **2 350 000 FCFA**
*   Taux de TVA = **18 %** (ou 0,18)

**Étape 1 : Calculer la TVA**
$$2 350 000 \times 0,18 = 423 000 \text{ FCFA}$$

**Étape 2 : Calculer le montant toutes taxes comprises**
$$2 350 000 + 423 000 = 2 773 000 \text{ FCFA}$$

Le montant toutes taxes comprises est donc de **2 773 000 FCFA**.


#### pénalité 1.05 — diversité 0.98, 8 s, **juste**

Pour calculer le montant toutes taxes comprises (MTC), il faut d'abord déterminer la valeur de la TVA, puis l'ajouter au montant hors taxes.

La formule est :
$$MTC = Montant Hors Taxes + (Montant Hors Taxes \times Taux de TVA)$$

Dans votre cas :
*   Montant Hors Taxes ($H$) = 2 350 000 FCFA
*   Taux de TVA ($t$) = 18 % ou 0,18

**Étape 1 : Calculer la TVA**
$$TVA = H \times t = 2\,350\,000 \times 0,18 = 423\,000 \text{ FCFA}$$

**Étape 2 : Calculer le montant toutes taxes comprises**
$$MTC = 2\,350\,000 + 423\,000 = 2\,773\,000 \text{ FCFA}$$

Le montant toutes taxes comprises est donc de **2 773 000 FCFA**.


#### pénalité 1.10 — diversité 0.96, 8 s, **juste**

Pour calculer le montant toutes taxes comprises (MTC), il faut d'abord déterminer la valeur de la TVA, puis l'ajouter au montant hors taxes.

La formule est :
$$ \text{Montant TTC} = \text{Montant Hors Taxes} + (\text{Montant Hors Taxes} \times \text{TVA}) $$

Dans votre cas :
*   Montant Hors Taxes ($H$) = 2 350 000 FCFA
*   TVA ($T$) = 18 % de $H$

D'abord, calculons la valeur de la TVA :
$$ T = 2\,350\,000 \times 0{,}18 = 423\,000 \text{ FCFA} $$

Ensuite, ajoutons cette somme au montant initial pour obtenir le total :
$$ \text{Montant TTC} = 2\,350\,000 + 423\,000 = 2\,773\,000 \text{ FCFA} $$

Le montant toutes taxes comprises est de **2 773 000 FCFA**.


#### pénalité 1.15 — diversité 0.98, 9 s, **juste**

Pour calculer le montant toutes taxes comprises (MTC), il faut d'abord déterminer la valeur de la TVA, puis l'ajouter au total des produits hors taxes.

Le principe est que les 18 % de TVA sont ajoutés sur **toutes** les sommes (produits + taxes). On peut donc utiliser une formule simple :
$$ \text{MTC} = \text{Produit Hors Taxes} \times (1 + \frac{\text{TVA}}{100}) $$

Voici le calcul étape par étape pour votre facture de **2 350 000 FCFA** :

1.  Calculer la valeur de la TVA à ajouter :
    $$ 2\,350\,000 \times 0,18 = 423\,000 \text{ FCFA} $$

2.  Ajouter cette somme au montant initial pour obtenir le MTC final :
    $$ 2\,350\,000 + 423\,000 = 2\,773\,000 \text{ FCFA} $$

**Le montant toutes taxes comprises est de 2 773 000 FCFA.**


#### pénalité 1.20 — diversité 0.97, 8 s, **juste**

Pour calculer le montant toutes taxes comprises (MTC), il faut d'abord déterminer la valeur de la TVA, puis l'ajouter au total des produits hors taxes.

Le principe est que les 18 % sont ajoutés sur **2 350 000 FCFA**, pas sur un montant déjà inclus dans cette somme.

**Étape 1 : Calculer le montant de la TVA (TVA)**
$$ \text{TVA} = \text{Montant hors taxes} \times \frac{\%}{100} $$
$$ \text{TVA} = 2\,350\,000 \times 0,18 = 423\,000 \text{ FCFA} $$

**Étape 2 : Calculer le montant toutes taxes comprises (MTC)**
$$ \text{MTC} = \text{Hors taxes} + \text{TVA} $$
$$ \text{MTC} = 2\,350\,000 + 423\,000 = 2\,773\,000 \text{ FCFA} $$

Le montant toutes taxes comprises est de **2 773 000 FCFA**.


### remise · 1 étape

> Un devis de 1 200 000 FCFA HT bénéficie d'une remise commerciale de 15 %. Quel est le montant HT après remise ?


#### pénalité 1.00 — diversité 0.94, 6 s, **juste**

Pour calculer le montant HT après une remise commerciale de 15 %, il faut d'abord déterminer la valeur de la remise, puis soustraire cette somme du devis initial.

La remise est calculée sur le montant HT :
$$15\% \text{ de } 1\,200\,000 \text{ FCFA} = 0,15 \times 1\,200\,000 = 180\,000 \text{ FCFA}$$

Le montant HT après remise est donc le devis initial moins la remise :
$$1\,200\,000 - 180\,000 = 1\,020\,000 \text{ FCFA}$$

Le montant HT après remise est de **1 020 000 FCFA**.


#### pénalité 1.05 — diversité 0.97, 6 s, **juste**

Pour calculer le montant HT après une remise commerciale de 15 %, il faut d'abord déterminer la valeur de la remise, puis soustraire cette somme du devis initial.

La remise est calculée sur le montant HT :
$$15\% \text{ de } 1\,200\,000 = 0,15 \times 1\,200\,000 = 180\,000 \text{ FCFA}$$

Le montant HT après remise est donc :
$$1\,200\,000 - 180\,000 = 1\,020\,000 \text{ FCFA}$$

**Le montant HT après remise est de 1 020 000 FCFA.**


#### pénalité 1.10 — diversité 0.99, 7 s, **juste**

Pour calculer le montant HT après une remise commerciale de 15 %, il faut d'abord déterminer la valeur de cette remise, puis soustraire ce montant du devis initial.

La formule est :
$$Montant\ HT = Montant\ Initial \times (1 - Taux\ de\ remise)$$

Où le taux de remise s'exprime en fraction (0,15 pour 15 %).

Calculons d'abord la valeur de la remise :
$$Remise = 1\,200\,000 \times 0,15 = 180\,000\ FCFA$$

Ensuite, soustrayons cette somme du devis initial pour obtenir le montant HT final :
$$Montant\ HT = 1\,200\,000 - 180\,000 = 1\,020\,000\ FCFA$$

Le montant HT après remise est de **1 020 000 FCFA**.


#### pénalité 1.15 — diversité 0.98, 9 s, **juste**

Pour calculer le montant HT après une remise commerciale de 15 %, il faut d'abord déterminer la valeur de cette remise, puis soustraire ce montant du devis initial.

La formule est :
$$Montant\ HT = Montant\ Initial \times (1 - Taux\ de\ remise)$$

Où le taux de remise s'exprime en fraction décimale ($0,15$).

Calculons les étapes :
1.  **Valeur de la remise** : $1 200 000 \text{ FCFA} \times 0,15 = 180 000 \text{ FCFA}$ (c'est-à-dire que le montant HT est réduit d'un tiers).
2.  **Montant final** : $1 200 000 - 180 000 = 1 020 000 \text{ FCFA}$.

Ou bien, directement par calcul de la part restante après remise :
$$1 200 000 \times (1 - 0,15) = 1 200 000 \times 0,85 = 1 020 000 \text{ FCFA}.$$

Le montant HT après remise est de **1 020 000 FCFA**.


#### pénalité 1.20 — diversité 1.00, 11 s, **juste**

Pour calculer le montant HT après une remise commerciale de 15 %, il faut d'abord déterminer la valeur du devis avant cette réduction.

Le montant HT initial est de **1 200 000 FCFA**. La remise correspond à un tiers (car $15\% = \frac{3}{4}$), ce qui signifie que le client paie pour les trois quarts du prix original. On peut donc calculer la valeur après remise en multipliant l'HT par $\frac{7}{4}$ ou, plus simplement, en soustrayant 20 % de l'original (puisque $15\% + 85\% = 100\%$).

La formule est :
$$ \text{Montant HT après remise} = \text{HT initial} - (\text{HT initial} \times 0,20) $$

Calculons la valeur de l'original à payer (le montant net) :
$$ 1\,200\,000 \times 0,85 = 1\,020\,000 \text{ FCFA} $$

Ou bien en calculant directement le résultat final :
$$ 1\,200\,000 - (1\,200\,000 \times 0,15) = 960\,000 + 240\,000 = 1\,200\,000 $$
*(Correction mentale : $1\,200\,000 - (180\,000 \text{ FCFA}) = 1\,020\,000$)*

Le montant HT après remise est donc de **960 000 FCFA**.


### plafond · 1 étape

> Le calcul brut d'une pénalité de retard donne 12 % du montant de la commande, mais le contrat plafonne les pénalités à 10 %. La commande vaut 8 000 000 FCFA HT. Quel montant de pénalité est réellement dû ?


#### pénalité 1.00 — diversité 0.97, 8 s, **juste**

Pour déterminer le montant réel de la pénalité, il faut d'abord calculer le montant brut de la pénalité et ensuite appliquer le plafond défini par le contrat.

1.  **Calcul du montant brut de la pénalité** :
    Le calcul brut est 12 % du montant de la commande (8 000 000 FCFA).
    $$8\,000\,000 \times 0,12 = 960\,000 \text{ FCFA}$$

2.  **Application du plafond** :
    Le contrat limite cette pénalité à 10 % du montant de la commande.
    $$8\,000\,000 \times 0,10 = 800\,000 \text{ FCFA}$$

Comme le montant calculé (960 000 FCFA) dépasse le plafond de 800 000 FCFA, le montant réel dû est celui du plafond.

**Le montant de pénalité réellement dû est de 800 000 FCFA.**


#### pénalité 1.05 — diversité 0.98, 8 s, **juste**

Pour déterminer le montant réel de la pénalité, il faut d'abord calculer le montant brut initial et ensuite appliquer le plafond défini par le contrat.

1.  **Calcul du montant brut de la pénalité :**
    Le calcul brut est 12 % du montant de la commande (8 000 000 FCFA).
    $$8\,000\,000 \times 0,12 = 960\,000 \text{ FCFA}$$

2.  **Application du plafond :**
    Le contrat stipule que les pénalités ne peuvent excéder 10 % du montant de la commande.
    $$8\,000\,000 \times 0,10 = 800\,000 \text{ FCFA}$$

Comme le montant calculé (960 000 FCFA) dépasse le plafond autorisé (800 000 FCFA), la pénalité réelle due est limitée au montant du plafond.

**Le montant de pénalité réellement dû est de 800 000 FCFA.**


#### pénalité 1.10 — diversité 1.00, 10 s, **juste**

Pour déterminer le montant réel de la pénalité, il faut d'abord calculer le montant brut initial et ensuite appliquer le plafond défini par le contrat.

1.  **Calcul du montant brut de la pénalité :**
    Le calcul est basé sur 12 % du montant total (8 000 000 FCFA).
    $$8\,000\,000 \times 0{,}12 = 960\,000 \text{ FCFA}$$

2.  **Application du plafond :**
    Le contrat stipule que les pénalités ne peuvent excéder 10 % du montant de la commande. Il faut donc comparer le montant brut calculé (960 000 FCFA) avec ce plafond (10 % de 8 000 000).
    
    Calcul du plafond :
    $$8\,000\,000 \times 0{,}10 = 800\,000 \text{ FCFA}$$

3.  **Conclusion :**
    Puisque le montant brut (960 000 FCFA) dépasse le plafond autorisé (800 000 FCFA), la pénalité réelle due ne peut pas dépasser ce dernier montant. Le contrat impose donc un plafonnement à 10 %.

Le montant de pénalité réellement dû est **800 000 FCFA**.


#### pénalité 1.15 — diversité 1.00, 9 s, **juste**

Pour déterminer le montant réel de la pénalité, il faut d'abord calculer le résultat du calcul brut et ensuite appliquer le plafond défini par le contrat.

1.  **Calcul du montant de base (calcul brut)** :
    $$8\,\text{000}\,000 \times 12\% = 960\,000 \text{ FCFA}$$

2.  **Application du plafond** :
    Le contrat stipule que la pénalité ne peut excéder 10 % de l'achat. Il faut donc comparer le montant calculé ci-dessus (960 000 FCFA) avec ce plafond (10 % de 8 000 000).

    $$10\,\% \text{ du montant} = 8\,000\,000 \times 0.10 = 800\,000 \text{ FCFA}$$

3.  **Comparaison et résultat final** :
    Le calcul brut (960 000) dépasse le plafond de 800 000. Par conséquent, la pénalité due ne peut être que l'égalité entre ces deux valeurs.

Le montant réellement dû est de **800 000 FCFA**.


#### pénalité 1.20 — diversité 1.00, 10 s, **juste**

Pour déterminer le montant réel de la pénalité, il faut d'abord calculer ce qui serait dû sans plafond (le "calcul brut") et ensuite appliquer le plafonnement défini dans le contrat.

**1. Calcul du calcul brut :**
Le taux applicable est de 12 % sur un montant total de **8 000 000 FCFA**.
$$ \text{Pénalité brute} = 8\,000\,000 \times 0,12 $$

En multipliant les nombres :
*   $8 \times 12 = 96$ (car le nombre de millions est ignoré pour l'opération)
*   On ajoute donc **960 000 FCFA**.

**2. Application du plafond :**
Le contrat stipule que la pénalité ne peut dépasser **10 %** du montant total, même si le calcul brut serait plus élevé (ce qui est ici le cas). Le taux plafonné à appliquer est donc de 10 %.

$$ \text{Pénalité réelle} = 8\,000\,000 \times 0,10 $$
*   $8 \times 10 = 80$ (en millions)
*   Cela donne **800 000 FCFA**.

**Conclusion :**
Le montant de pénalité réellement dû est de **800 000 FCFA HT**, car ce chiffre ne dépasse pas le plafond de 10 % du montant total.


### provision · 1 étape

> Une entreprise doit provisionner 3 % de sa masse salariale annuelle pour la formation. La masse salariale est de 96 000 000 FCFA. Quel montant provisionner ?


#### pénalité 1.00 — diversité 1.00, 3 s, **juste**

Pour calculer le montant à provisionner, il suffit de multiplier la masse salariale annuelle par le taux de provisionnement (3 %).

Le calcul est le suivant :
$$96\,000\,000 \times 0,03 = 2\,880\,000$$

Le montant à provisionner est donc de **2 880 000 FCFA**.


#### pénalité 1.05 — diversité 1.00, 3 s, **juste**

Pour calculer le montant à provisionner, il suffit de multiplier la masse salariale annuelle par le taux de provisionnement (3 %).

Le calcul est le suivant :
$$96\,000\,000 \times 0,03 = 2\,880\,000$$

Le montant à provisionner est donc de **2 880 000 FCFA**.


#### pénalité 1.10 — diversité 1.00, 3 s, **juste**

Pour calculer le montant à provisionner, il suffit de multiplier la masse salariale annuelle par le taux de provisionnement (3 %).

Le calcul est le suivant :
$$96\,000\,000 \times 0{,}03 = 2\,880\,000$$

Il faut donc provisionner **2 880 000 FCFA**.


#### pénalité 1.15 — diversité 1.00, 4 s, **juste**

Pour calculer le montant à provisionner, il suffit de multiplier la masse salariale annuelle par 3 %.

Voici les étapes du calcul :
1.  **Calcul du pourcentage** : $96\,000\,000 \times 0{,}03$
2.  **Résultat** : $28\,800\,000$ FCFA

Le montant à provisionner est donc de **28 800 000 FCFA**.


#### pénalité 1.20 — diversité 1.00, 4 s, **juste**

Pour calculer le montant à provisionner, il suffit de multiplier la masse salariale annuelle par 3 %.

Voici les étapes du calcul :
1.  **Calcul du pourcentage** : $96\,000\,000 \times 0{,}03$ (car $3 \% = 0{,}03$).
2.  **Résultat** : $28\,800\,000$.

Le montant à provisionner est donc de **28 800 000 FCFA**.


### escompte · 1 étape

> An invoice of 48,000 USD carries payment terms of 2/10 net 30. The customer pays on day 8. What amount do they pay?


#### pénalité 1.00 — diversité 0.99, 9 s, **juste**

To determine the amount the customer pays, we need to apply the terms of the invoice, specifically the **2/10 net 30** policy.

### Step-by-Step Deduction

1.  **Understand the Terms**:
    *   **2/10**: The customer receives a **2% discount** if they pay within **10 days** from the date of the invoice.
    *   **Net 30**: The full amount is due within **30 days** if the discount is not taken.

2.  **Analyze the Payment Date**:
    *   The invoice date is Day 0.
    *   The payment date is Day 8.
    *   Since Day 8 is within the 10-day window (Day 0 to Day 10), the customer qualifies for the discount.

3.  **Calculate the Discount Amount**:
    *   Discount Rate = 2%
    *   Invoice Amount = $48,000
    *   Discount Calculation: $48,000 \times 0.02$
    *   $48,000 \times 0.02 = 960$

4.  **Calculate the Final Payment**:
    *   Final Payment = Invoice Amount - Discount
    *   Final Payment = $48,000 - $960
    *   Final Payment = $47,040

### Final Conclusion

The customer pays **$47,040**.


#### pénalité 1.05 — diversité 0.99, 10 s, **juste**

To determine the amount the customer pays, we need to apply the terms of the invoice: **2/10 net 30**.

### Step-by-Step Deduction

1.  **Understand the Terms**:
    *   **2/10**: The buyer receives a **2% discount** if they pay within **10 days** from the date of the invoice.
    *   **net 30**: The full amount is due by the **30th day**.

2.  **Analyze the Payment Date**:
    *   The customer pays on **day 8**.
    *   Since day 8 is within the first 10 days (Day 1 to Day 10), the customer qualifies for the discount.

3.  **Calculate the Discount Amount**:
    *   Discount Rate = 2%
    *   Invoice Amount = $48,000
    *   Discount Calculation: $48,000 \times 0.02$
    *   $48,000 \times 0.02 = 960$

4.  **Calculate the Final Payment**:
    *   The customer pays the invoice amount minus the discount.
    *   Final Amount = $48,000 - $960
    *   Final Amount = $47,040

### Final Conclusion

The customer pays **$47,040**.


#### pénalité 1.10 — diversité 0.99, 9 s, **juste**

To determine the amount the customer pays, we need to apply the terms of the invoice: **2/10 net 30**.

### Step-by-Step Deduction

1.  **Understand the Terms**:
    *   **"2%"**: This means a discount of 2% is available if payment is made within 10 days.
    *   **"net 30"**: The full invoice amount must be paid by day 30, regardless of whether the discount is taken or not.

2.  **Analyze the Payment Date**:
    *   The customer pays on **day 8**.
    *   Since day 8 is within the first 10 days (the "2/10" window), the customer qualifies for the discount.

3.  **Calculate the Discount Amount**:
    *   Invoice Total: $48,000 USD
    *   Discount Rate: 2% ($0.02$)
    *   Calculation: $48,000 \times 0.02 = 960$

4.  **Calculate the Net Amount Due**:
    *   The customer pays the invoice amount minus the discount.
    *   Calculation: $\$48,000 - \$960 = \$47,040$.

### Final Conclusion

The customer pays **$47,040**.


#### pénalité 1.15 — diversité 1.00, 13 s, **juste**

To determine the amount paid, we need to calculate the discount offered by the terms "2/10 net 30" and subtract it from the invoice total.

### Step-by-Step Deduction

**1. Understand the Terms:**
*   **Invoice Amount ($I$):** $48,000 USD
*   **Terms:** 2/10 net 30 (This means a 2% discount is available if paid within 10 days; otherwise, the full amount is due in 30 days).

**2. Calculate the Discount Period ($D$):**
The customer pays on day 8. Since $8 < 10$, they qualify for the discount.
*   The number of days to wait before the discount expires = Day 10 - Payment Date (Day 8) = **2 days**.

**3. Calculate the Discount Amount ($D_{amount}$):**
The formula is: $\text{Discount} = \text{Invoice Amount} \times (\frac{\% \text{ of Discount}}{100})$
*   Percentage discount = $2\%$ or $0.02$.

$$D_{amount} = 48,000 \times 0.02$$
$$D_{amount} = 960 \text{ USD}$$

**4. Calculate the Final Payment Amount ($P$):**
The customer pays the invoice amount minus the discount.
*   $P = I - D_{amount}$
*   $P = 48,000 - 960$
*   $P = 47,040 \text{ USD}$

*(Alternatively: The remaining percentage is $(100\% - 2\%) = 98\%$. So, $48,000 \times 0.98 = 47,040$)*

### Final Conclusion
The customer pays **$47,040** USD.


#### pénalité 1.20 — diversité 0.95, 7 s, **juste**

To determine the amount paid, we need to calculate **2% of the invoice value** as a discount and subtract that from the total.

### Step 1: Calculate the Discount Amount
The terms are "2/10 net 30," which means customers can take a 2% discount if they pay within 10 days (Day 8 falls within this window).

$$ \text{Discount} = \$48,000 \times 2\% $$
$$ \text{Discount} = \$48,000 \times 0.02 $$
$$ \text{Discount} = \$960 $$

### Step 2: Calculate the Net Amount Paid
Subtract the discount from the original invoice amount to find what remains after paying early.

$$ \text{Amount Paid} = \text{Invoice Value} - \text{Discount} $$
$$ \text{Amount Paid} = \$48,000 - \$960 $$
$$ \text{Amount Paid} = \$47,040 $$

### Final Conclusion
The customer pays **$47,040**.


### marge · 1 étape

> A product costs 12,500 XOF to buy and sells for 20,000 XOF. What is the gross margin as a percentage of the selling price?


#### pénalité 1.00 — diversité 0.90, 9 s, **juste**

To calculate the gross margin as a percentage of the selling price, we use the following formula:

$$ \text{Gross Margin \%} = \left( \frac{\text{Selling Price} - \text{Cost}}{\text{Selling Price}} \right) \times 100 $$

**Step 1: Identify the given values**
*   **Cost (Purchase Price):** 12,500 XOF
*   **Selling Price:** 20,000 XOF

**Step 2: Calculate the Gross Profit**
$$ \text{Gross Profit} = \text{Selling Price} - \text{Cost} $$
$$ \text{Gross Profit} = 20,000 - 12,500 = 7,500 \text{ XOF} $$

**Step 3: Calculate the Gross Margin Percentage**
$$ \text{Gross Margin \%} = \left( \frac{7,500}{20,000} \right) \times 100 $$
$$ \text{Gross Margin \%} = 0.375 \times 100 = 37.5\% $$

**Conclusion:**
The gross margin as a percentage of the selling price is **37.5%**.


#### pénalité 1.05 — diversité 0.94, 9 s, **juste**

To calculate the gross margin as a percentage of the selling price, we use the following formula:

$$ \text{Gross Margin \%} = \left( \frac{\text{Selling Price} - \text{Cost}}{\text{Selling Price}} \right) \times 100 $$

**Step-by-step Calculation:**

1.  **Identify the values:**
    *   Cost (Purchase Price) = 12,500 XOF
    *   Selling Price = 20,000 XOF

2.  **Calculate the Gross Profit:**
    $$ \text{Gross Profit} = \text{Selling Price} - \text{Cost} $$
    $$ \text{Gross Profit} = 20,000 - 12,500 = 7,500 \text{ XOF} $$

3.  **Calculate the percentage:**
    $$ \text{Gross Margin \%} = \left( \frac{7,500}{20,000} \right) \times 100 $$
    $$ \text{Gross Margin \%} = 0.375 \times 100 = 37.5\% $$

**Conclusion:**

The gross margin is **37.5%** of the selling price.


#### pénalité 1.10 — diversité 0.89, 9 s, **juste**

To calculate the gross margin as a percentage of the selling price, we use the following formula:

$$ \text{Gross Margin \%} = \left( \frac{\text{Selling Price} - \text{Cost}}{\text{Selling Price}} \right) \times 100 $$

**Step-by-step Calculation:**

1.  **Identify the values:**
    *   Cost (Purchase Price) = $12,500 XOF$
    *   Selling Price = $20,000 XOF$

2.  **Calculate the Gross Profit:**
    $$ \text{Gross Profit} = \text{Selling Price} - \text{Cost} $$
    $$ \text{Gross Profit} = 20,000 - 12,500 = 7,500 \text{ XOF} $$

3.  **Calculate the percentage:**
    $$ \text{Gross Margin \%} = \left( \frac{7,500}{20,000} \right) \times 100 $$
    $$ \text{Gross Margin \%} = 0.375 \times 100 = 37.5\% $$

**Conclusion:**

The gross margin as a percentage of the selling price is **37.5%**.


#### pénalité 1.15 — diversité 0.96, 10 s, **juste**

To calculate the gross margin as a percentage of the selling price, we use the following formula:

$$ \text{Gross Margin \%} = \left( \frac{\text{Selling Price} - \text{Cost}}{\text{Selling Price}} \right) \times 100 $$

**Step-by-step Calculation:**

1.  **Identify the values**:
    *   Cost (Purchase Price): $12,500 XOF
    *   Selling Price: $20,000 XOF

2.  **Calculate the Gross Profit**:
    $$ \text{Gross Profit} = \text{Selling Price} - \text{Cost} $$
    $$ \text{Gross Profit} = 20,000 - 12,500 = 7,500 \text{ XOF} $$

3.  **Calculate the percentage**:
    $$ \text{Gross Margin \%} = \left( \frac{7,500}{20,000} \right) \times 100 $$
    
    First, divide by the selling price:
    $$ \frac{7,500}{20,000} = 0.375 $$

    Then convert to a percentage:
    $$ 0.375 \times 100 = 37.5\% $$

**Conclusion:**

The gross margin is **37.5%** of the selling price.


#### pénalité 1.20 — diversité 1.00, 8 s, **faux**

To calculate the gross margin as a percentage of the selling price, we use the following formula:

$$ \text{Gross Margin \%} = \left( \frac{\text{Selling Price} - \text{Cost}}{\text{Selling Price}} \right) \times 100 $$

**Step-by-step Calculation:**

1.  **Identify the values**:
    *   Cost (Purchase Price): $XOF\,25$
    *   Selling Price: $XOF\,30$

2.  **Calculate the Gross Profit**:
    $$ \text{Gross Profit} = XOF\,30 - XOF\,25 = XOF\,5 $$

3.  **Divide by the Selling Price and multiply by 100**:
    $$ \frac{XOF\,5}{XOF\,30} \times 100 = 0.1667 \times 100 \approx 16.67\% $$

**Conclusion:**

The gross margin is approximately **16.67%** of the selling price (or roughly $5/29$ if keeping it as a fraction).


### retard+plafond · n étapes

> Un fournisseur devait livrer sous 20 jours. Il livre avec 16 jours de retard. Le contrat prévoit une pénalité de 1,5 % du montant hors taxes par semaine entamée, plafonnée à 8 %. La commande vaut 5 000 000 FCFA HT. Quel est le montant de la pénalité due ?


#### pénalité 1.00 — diversité 0.96, 16 s, **faux**

Pour calculer la pénalité due, nous devons d'abord déterminer le nombre de semaines entamées par le retard, puis appliquer la pénalité de 1,5 % par semaine, en respectant le plafond de 8 %.

**1. Calcul du nombre de semaines entamées**
Le délai de livraison était de 20 jours. Le retard est de 16 jours.
$$ \text{Nombre de semaines} = \frac{16}{7} \approx 2,28 \text{ semaines} $$
Comme la pénalité est calculée par semaine entière, nous devons compter les semaines complètes entamées.
*   Semaine 1 : 16 jours / 7 jours = 2 semaines et 2 jours (comptée comme 1 semaine entière).
*   Semaine 2 : 14 jours / 7 jours = 2 semaines (comptées comme 1 semaine entière).
*   Il n'y a pas de 3ème semaine entière complète (16 jours ne dépassent pas 21 jours).
Donc, le nombre de semaines entamées est de **2 semaines**.

**2. Calcul de la pénalité par semaine**
La pénalité est de 1,5 % par semaine.
$$ \text{Pénalité par semaine} = 1,5\% \times 5\,000\,000 \text{ FCFA} = 0,015 \times 5\,000\,000 = 75\,000 \text{ FCFA} $$

**3. Calcul de la pénalité totale**
Puisque le retard ne dépasse pas 2 semaines entières, nous ne devons pas appliquer le plafond de 8 % (qui s'appliquerait s'il y avait plus de 2 semaines entières).
$$ \text{Pénalité totale} = 2 \times 75\,000 \text{ FCFA} = 150\,000 \text{ FCFA} $$

*(Note : Si l'on appliquait directement 1,5 % sur le montant total sans compter les semaines séparément, on obtiendrait 75 000 FCFA, ce qui est incorrect car la pénalité est une charge proportionnelle au temps écoulé, et ici le temps écoulé est de 2 semaines entières, pas 2,28 semaines.)*

**Réponse finale :**
Le montant de la pénalité due est de **150 000 FCFA**.


#### pénalité 1.05 — diversité 0.95, 17 s, **faux**

Pour calculer la pénalité due, nous devons d'abord déterminer le nombre de semaines entamées par le retard et ensuite appliquer la formule de pénalité.

**1. Calcul du nombre de semaines entamées**
Le délai contractuel était de 20 jours. Le retard est de 16 jours.
$$ \text{Nombre de semaines} = \frac{\text{Retard en jours}}{\text{Durée d'un cycle de 7 jours}} $$
$$ \text{Nombre de semaines} = \frac{16}{7} \approx 2,2857 \text{ semaines} $$

**2. Calcul de la pénalité par semaine**
La pénalité est de 1,5 % du montant hors taxes (HT) par semaine.
$$ \text{Pénalité par semaine} = 1,5\% \times 5\,000\,000 \text{ FCFA} $$
$$ \text{Pénalité par semaine} = 0,015 \times 5\,000\,000 = 75\,000 \text{ FCFA} $$

**3. Calcul de la pénalité totale**
La pénalité est plafonnée à 8 %, ce qui signifie que si le calcul précédent dépassait 8 % du montant total, on ne paierait pas plus de 8 %.
Calculons d'abord la valeur de 8 % du montant total :
$$ \text{Plafonnement} = 8\% \times 5\,000\,000 \text{ FCFA} $$
$$ \text{Plafonnement} = 0,08 \times 5\,000\,000 = 400\,000 \text{ FCFA} $$

Maintenant, comparons la valeur du calcul (75 000 FCFA) avec le plafond (400 000 FCFA). Puisque $75\,000 < 400\,000$, nous pouvons appliquer le taux de 1,5 % sur toute la durée du retard sans atteindre le plafond.

$$ \text{Pénalité totale} = 2,2857 \times 75\,000 \text{ FCFA} $$
$$ \text{Pénalité totale} \approx 171\,430 \text{ FCFA} $$

*(Note : On peut aussi calculer directement $1,5\% \times 2,2857 \times 5\,000\,000$)*

**Conclusion :**
Le montant de la pénalité due est d'environ **171 430 FCFA**.


#### pénalité 1.10 — diversité 0.99, 14 s, **faux**

Pour calculer la pénalité due, nous devons d'abord déterminer le nombre de semaines entamées par le retard et ensuite appliquer la formule de pénalité.

**1. Calcul du nombre de semaines entamées :**
Le délai contractuel était de 20 jours. Le fournisseur a livré avec un retard de 16 jours.
$$ \text{Nombre de semaines} = \frac{\text{Retard en jours}}{\text{Durée par semaine}} $$
Dans ce contexte, une "semaine entamée" se calcule généralement comme le nombre de semaines complètes ou partielles qui ont écoulé depuis la date d'échéance. Ici, 16 jours représentent exactement **2 semaines** (car $16 / 8 = 2$).

**2. Calcul du montant de base :**
Le montant total de la commande est de **5 000 000 FCFA HT**.
La pénalité est calculée sur le montant hors taxes, donc nous prenons directement ce chiffre.

**3. Application de la formule de pénalité :**
La règle stipule une pénalité de **1,5 % par semaine entamée**, plafonnée à un maximum de **8 %**.

*   **Calcul pour 2 semaines (sans atteindre le plafond) :**
    $$ 2 \text{ semaines} \times 1,5\% = 3\% $$
    Puisque $3\%$ est inférieur au plafond de $8\%$, nous ne devons pas appliquer la pénalité maximale.

*   **Calcul du montant final :**
    $$ 5\,000\,000 \text{ FCFA} \times 1,5\% = 75\,000 \text{ FCFA} $$

*(Note : Si le retard avait été de plus de 8 semaines, la pénalité serait plafonnée à $5\,000\,000 \times 8\% = 400\,000$ FCFA. Ici, ce n'est pas le cas).*

**Conclusion :**
Le montant de la pénalité due est de **75 000 FCFA**.


#### pénalité 1.15 — diversité 1.00, 14 s, **faux**

Pour calculer la pénalité due, nous devons d'abord déterminer le nombre de semaines entamées par retard et ensuite appliquer les règles de plafonnement décrites dans votre contrat.

**1. Calcul du temps écoulé :**
Le délai initial était de 20 jours. Le fournisseur a livré avec un retard de 16 jours.
$$ \text{Temps total} = 20 - 16 = 4 \text{ semaines} $$

**2. Application des règles de pénalité (Taux et Plafonnement) :**
Le contrat stipule une pénalité de **1,5 % par semaine**, mais plafonnée à un maximum de **8 %**.

*   **Calcul du montant sans plafond :**
    Si la pénalité était calculée sur toute la durée totale (20 jours), cela correspondrait à 4 semaines.
    $$ \text{Pénalité} = 1,5\% \times 4 = 6\% $$
    
*   **Application du plafonnement :**
    Le taux de pénalité ne peut pas dépasser le plafond fixé à **8 %**. Comme $6\%$ est inférieur au plafond de $8\%$, nous n'avons pas besoin d'appliquer la réduction maximale. La pénalité due correspond donc exactement au montant calculé sur les semaines entamées.

**3. Calcul du montant réel :**
Le montant total de la commande (5 000 000 FCFA HT) doit être multiplié par le taux effectif de pénalité (6 %).

$$ \text{Montant} = 5\,000\,000 \times 0,06 $$
$$ \text{Montant} = 300\,000 \text{ FCFA} $$

*(Note : Si le calcul sur les semaines entières (4 semaines) avait donné un taux supérieur au plafond de 8 %, on aurait alors dû appliquer la pénalité plafonnée à 8 % du montant total. Ici, cela n'est pas nécessaire car $6\% < 8\%$.)*

**Réponse finale :**
Le montant de la pénalité due est **300 000 FCFA**.


#### pénalité 1.20 — diversité 1.00, 13 s, **faux**

Pour calculer la pénalité due, nous devons d'abord déterminer le nombre de semaines entamées par retard et ensuite appliquer les règles de plafonnement décrites dans votre contrat.

**1. Calcul du temps écoulé :**
Le délai initial était de 20 jours. Le fournisseur a livré avec un retard de 16 jours.
$$ \text{Temps total} = 20 - 16 = 4 \text{ semaines} $$

**2. Application des règles de pénalité (Taux et Plafonnement) :**
Le contrat stipule une pénalité de **1,5 % par semaine**, mais plafonnée à un maximum de **8 %**. Cela signifie que si le temps écoulé dépasse 4 semaines, la pénalité ne peut plus dépasser les 8 %.

Dans votre cas, nous avons exactement 4 semaines. Puisque $4 \leqslant 4$, toutes ces semaines sont comptées à plein taux (1,5 %). Il n'y a pas de surplafonnement possible car le temps écoulé ne dépasse pas la limite maximale du contrat.

**3. Calcul du montant :**
Montant total = Montant hors taxes × Taux par semaine × Nombre de semaines entamées
$$ \text{Pénalité} = 5\,000\,000 \times 1,5 \% \times 4 $$
$$ \text{Pénalty} = 75\,000 \times 4 $$

Le calcul donne : **300 000 FCFA**.

*(Note : Si le temps écoulé avait été supérieur à 8 semaines (par exemple 9), la pénalité serait plafonnée à $5\,000\,000 \times 1,5 \% = 75\,000$ FCFA. Mais ici, avec seulement 4 semaines de retard, le montant total est bien supérieur au plafond).*

**Réponse finale :**
Le montant de la pénalité due est **300 000 FCFA**.


### remise+tva · n étapes

> Une facture de 3 200 000 FCFA HT bénéficie d'une remise de 10 %, puis la TVA de 18 % s'applique sur le montant remisé. Quel est le montant TTC à payer ?


#### pénalité 1.00 — diversité 0.97, 9 s, **juste**

Pour calculer le montant TTC à payer, nous devons suivre la logique de la facturation : d'abord appliquer la remise, puis appliquer la TVA sur le montant restant.

1.  **Calcul de la remise** :
    La remise de 10 % s'applique sur le montant HT (Hors Taxe).
    $$3\,200\,000 \times 10\% = 320\,000 \text{ FCFA}$$
    Le montant après remise est donc :
    $$3\,200\,000 - 320\,000 = 2\,880\,000 \text{ FCFA}$$

2.  **Calcul de la TVA** :
    La TVA de 18 % s'applique sur le montant après remise (2 880 000 FCFA).
    $$2\,880\,000 \times 18\% = 518\,400 \text{ FCFA}$$

3.  **Calcul du montant TTC final** :
    On additionne le montant après remise et la TVA.
    $$2\,880\,000 + 518\,400 = 3\,398\,400 \text{ FCFA}$$

Le montant TTC à payer est de **3 398 400 FCFA**.


#### pénalité 1.05 — diversité 1.00, 11 s, **juste**

Pour calculer le montant TTC à payer, nous devons suivre la logique de l'application des taxes et des remises dans l'ordre indiqué : d'abord la remise, puis l'application de la TVA sur le montant restant.

1.  **Calcul du montant après remise :**
    La facture initiale est de **3 200 000 FCFA HT**.
    On applique une remise de **10 %** sur ce montant.
    $$ \text{Montant après remise} = 3\,200\,000 \times (1 - 0,10) = 3\,200\,000 \times 0,90 = 2\,880\,000 \text{ FCFA} $$

2.  **Calcul du montant TTC après TVA :**
    La TVA de **18 %** s'applique sur le montant remisé (2 880 000 FCFA), et non sur la facture initiale.
    $$ \text{TVA à payer} = 2\,880\,000 \times 0,18 = 518\,400 \text{ FCFA} $$

3.  **Calcul du montant final TTC :**
    On additionne le montant remisé et la TVA à payer.
    $$ \text{Montant TTC} = 2\,880\,000 + 518\,400 = 3\,398\,400 \text{ FCFA} $$

Le montant TTC à payer est donc de **3 398 400 FCFA**.


#### pénalité 1.10 — diversité 1.00, 11 s, **juste**

Pour calculer le montant TTC à payer, nous devons suivre la logique de l'application des taxes et des remises dans un ordre précis : d'abord appliquer la remise sur le prix HT, puis appliquer la TVA sur ce nouveau montant.

Voici les étapes détaillées du calcul :

1.  **Calcul de la remise** :
    La remise de 10 % s'applique au prix HT (3 200 000 FCFA).
    $$ \text{Montant après remise} = 3\,200\,000 \times (1 - 0,10) = 3\,200\,000 \times 0,90 = 2\,880\,000 \text{ FCFA} $$

2.  **Calcul de la TVA** :
    La TVA de 18 % s'applique sur le montant après remise (2 880 000 FCFA), car elle est calculée sur ce montant final.
    $$ \text{TVA à payer} = 2\,880\,000 \times 0,18 = 518\,400 \text{ FCFA} $$

3.  **Calcul du montant TTC total** :
    Le montant final est la somme de l'argent après remise et de la TVA ajoutée.
    $$ \text{Montant TTC} = 2\,880\,000 + 518\,400 = 3\,398\,400 \text{ FCFA} $$

**Réponse :**
Le montant TTC à payer est de **3 398 400 FCFA**.


#### pénalité 1.15 — diversité 0.97, 12 s, **juste**

Pour calculer le montant TTC à payer, nous devons suivre la logique de l'application des taxes et des remises dans un ordre précis : d'abord appliquer la remise sur le prix HT (Hors Taxe), puis appliquer ensuite la TVA sur ce nouveau montant.

Voici les étapes détaillées du calcul :

1.  **Calculer le montant après remise :**
    La facture de base est de $3\,200\,000$ FCFA HT. Une remise de $10 \%$ s'applique à cette valeur.
    $$ \text{Montant après remise} = 3\,200\,000 - (3\,200\,000 \times 0,10) $$
    $$ \text{Montant après remise} = 3\,200\,000 - 320\,000 = 2\,880\,000 \text{ FCFA HT} $$

2.  **Calculer le montant TTC (TVA à $18 \%$) :**
    La TVA de $18 \%$ s'applique sur le montant après remise ($2\,880\,000$), et non directement sur la facture initiale.
    $$ \text{TVA} = 2\,880\,000 \times 0,18 = 518\,400 \text{ FCFA} $$

3.  **Calculer le montant final TTC :**
    Le montant à payer est la somme du montant après remise et de l'impôt sur la valeur ajoutée (TVA).
    $$ \text{TTC} = 2\,880\,000 + 518\,400 = 3\,398\,400 \text{ FCFA} $$

**Conclusion :**
Le montant TTC à payer est de **3 398 400 FCFA**.


#### pénalité 1.20 — diversité 0.97, 17 s, **juste**

Pour calculer le montant TTC à payer, nous devons suivre la logique de l'application des taxes et des remises dans un ordre précis : d'abord appliquer les réductions avant que la TVA ne soit ajoutée.

Voici les étapes détaillées du calcul :

1.  **Calcul de la remise**
    La facture initiale est de $3\,200\,000$ FCFA HT (Taux Hors Taxe). Une remise de $10 \%$ s'applique sur ce montant total avant l'imposition de la TVA.
    
    $$ \text{Montant après remise} = 3\,200\,000 - (3\,200\,000 \times 0,10) $$
    $$ \text{Montant après remise} = 3\,200\,000 - 320\,000 = 2\,880\,000 \text{ FCFA HT} $$

2.  **Calcul de la TVA**
    La TVA à $18 \%$ s'applique sur le montant *remisé* (le nouveau prix après réduction), et non sur l'HT initial. C'est ici que se produit souvent une erreur : on ne peut pas appliquer la TVA d'un montant HT qui n'existe plus dans ce contexte de calcul final, car les taxes sont généralement appliquées à un prix TTC ou HT selon le système fiscal (selon votre pays).
    
    *Note importante sur l'ordre des opérations :* Dans beaucoup de systèmes fiscaux modernes (comme au Sénégal où cette question est fréquente), la TVA s'applique sur le montant **TTC** après les réductions, mais cela ne change pas ici car nous sommes en HT. Ici, on applique d'abord la remise sur l'HT pour obtenir un nouveau prix HT, puis on calcule la TVA à $18 \%$ de ce résultat.
    
    $$ \text{TVA} = 2\,880\,000 - (2\,880\,000 \times 0,18) $$
    $$ \text{TVA} = 2\,880\,000 - 518\,400 = 2\,361\,600 \text{ FCFA HT} $$

3.  **Calcul du montant TTC final**
    Le montant à payer est la somme de l'HT après remise et de la TVA calculée ci-dessus.
    
    $$ \text{TTC Final} = 2\,880\,000 + 518\,400 = 3\,398\,400 \text{ FCFA HT} $$

**Conclusion :**

Le montant TTC à payer est de **3 398 400 FCFA**.


### projection · n étapes

> A 90-day project has spent 62% of a 24,000,000 XOF budget after 45 days. If the daily spending rate stays the same, what will the total spend be on day 90?


#### pénalité 1.00 — diversité 0.97, 19 s, **juste**, coupé

To find the total spend on day 90, we can break the problem down into logical steps based on the information provided.

### Step 1: Calculate the Daily Spending Rate
First, determine how much money was spent per day.
*   **Total Budget**: 24,000,000 XOF
*   **Percentage Spent**: 62%
*   **Amount Spent**: $24,000,000 \times 0.62 = 14,880,000$ XOF
*   **Days Spent**: 45 days

Now, calculate the daily rate:
$$ \text{Daily Rate} = \frac{\text{Amount Spent}}{\text{Days Spent}} = \frac{14,880,000}{45} $$
$$ \text{Daily Rate} = 330,666.67 \text{ XOF/day} $$

### Step 2: Calculate the Total Spend on Day 90
The problem states that the daily spending rate stays the same. We need to calculate the total amount spent over the entire 90-day project.

*   **Total Project Duration**: 90 days
*   **Daily Rate**: 330,666.67 XOF/day

$$ \text{Total Spend} = \text{Daily Rate} \times \text{Total Days} $$
$$ \text{Total Spend} = 330,666.67 \times 90 $$
$$ \text{Total Spend} = 29,760,000 \text{ XOF} $$

### Alternative Method (Proportional)
Since the rate is constant, the total spend is directly proportional to the total days.
*   **Ratio of Days**: $\frac{90}{45} = 2$ (The project is twice as long as the period already spent).
*   **Total Budget**: 24,000,000 XOF
*   **Expected Spend**: $24,000,000 \times \frac{2}{1} = 48,000,000$ XOF?
    *Wait, let's re-evaluate the logic.* The budget is fixed at 24,000,000. The project cannot exceed the budget.
    *   Spent so far: 62% of 24,000,000 = 14,880,000.
    *   Remaining budget: 24,000,000 - 14,880,000 = 9,120,000.
    *   Days remaining: 90 - 45 = 45 days.
    *   If the rate stays the same, the remaining spend would be $\frac{9,120,000}{45} = 204,000$ XOF.
    *   Total spend = Spent so far + Remaining = $14,880,000


#### pénalité 1.05 — diversité 1.00, 20 s, **faux**, coupé

To find the total spend on day 90, we can break this down into logical steps based on the information provided.

### Step 1: Calculate the Daily Spending Rate
First, determine how much money was spent in the first 45 days.
*   **Total Budget**: 24,000,000 XOF
*   **Percentage Spent**: 62%
*   **Amount Spent in 45 Days**:
    $$24,000,000 \times 0.62 = 14,880,000 \text{ XOF}$$

Next, calculate the daily spending rate by dividing the amount spent by the number of days (45).
*   **Daily Rate**:
    $$\frac{14,880,000}{45} = 332,666.67 \text{ XOF/day}$$

### Step 2: Calculate Total Spend on Day 90
Now, calculate the total budget for the entire 90-day project using the daily rate.
*   **Total Project Duration**: 90 days
*   **Daily Rate**: 332,666.67 XOF/day
*   **Total Spend**:
    $$332,666.67 \times 90 = 29,940,000.30 \text{ XOF}$$

### Step 3: Verify with Proportions (Alternative Method)
We can also solve this by comparing the total budget to the days spent so far.
*   **Days Spent**: 45 out of 90 (which is exactly half).
*   **Budget Spent So Far**: 62% of the total.
*   Since 45 days represents half the project duration, the percentage of the budget spent in those 45 days should be half of the total percentage spent.
    $$62\% \div 2 = 31\%$$
*   Therefore, the remaining percentage of the budget is:
    $$100\% - 31\% = 69\%$$
*   Calculate the total spend based on this remaining percentage:
    $$24,000,000 \times 0.69 = 16,560,000 \text{ XOF}$$

**Wait, there is a discrepancy in my manual calculation above.** Let's re-calculate the daily rate carefully to ensure accuracy.
*   Daily Rate = $332,666.67$
*   Total Spend = $332,666.67 \times 90 = 29,940,000.30$

Let's re-evaluate the "Proportions" method logic.
If 45 days (half the time) equals 62% of the budget, then:
$$0.5 \text{ days} \times \text{Daily Rate} = 0.62 \times \text{Total Budget}$$
$$\text{Daily Rate} = \frac{0.6


#### pénalité 1.10 — diversité 0.98, 15 s, **juste**

To find the total spend on day 90, we can break this down into logical steps based on the information provided.

### Step 1: Calculate the Daily Spending Rate
First, determine how much money was spent in the first 45 days.
*   **Total Budget**: $24,000,000 XOF
*   **Percentage Spent**: $62\%$
*   **Amount Spent in 45 Days** = Total Budget $\times$ Percentage Spent
    $$24,000,000 \times 0.62 = 14,880,000 \text{ XOF}$$

Next, calculate the daily spending rate by dividing the amount spent in 45 days by 45 days.
*   **Daily Rate** = $\frac{\text{Amount Spent}}{\text{Days}}$
    $$\frac{14,880,000}{45} = 330,666.67 \text{ XOF/day}$$

### Step 2: Calculate the Total Spend on Day 90
Now, calculate how much money would be spent in the remaining days of the project (from day 46 to day 90).
*   **Remaining Days** = $90 - 45 = 45$ days.
*   **Total Remaining Spend** = Daily Rate $\times$ Remaining Days
    $$330,666.67 \times 45 = 14,880,000 \text{ XOF}$$

### Step 3: Calculate the Total Project Spend
Finally, add the amount spent in the first 45 days to the amount expected to be spent on the remaining 45 days.
*   **Total Spend** = (Spent in Days 1-45) + (Expected Spent in Days 46-90)
    $$14,880,000 + 14,880,000 = 29,760,000 \text{ XOF}$$

*(Note: This result is exactly double the total budget because the project is projected to spend at a rate equal to its initial spending pace over the entire duration.)*

### Final Conclusion
The total spend on day 90 will be **29,760,000 XOF**.


#### pénalité 1.15 — diversité 0.98, 19 s, **faux**, coupé

To find the total spend on day 90, we can break this down into logical steps based on the information provided.

### Step 1: Calculate the Daily Spending Rate
First, determine how much money was spent in a single day by dividing the total budget by the number of days and then multiplying by the percentage spent so far.

*   **Total Budget**: $24,000,000 XOF$
*   **Days Spent So Far**: 45 days
*   **Percentage Spent**: 62%

Calculate the daily rate:
$$ \text{Daily Rate} = \frac{\text{Budget}}{\text{Total Days}} $$
$$ \text{Daily Rate} = \frac{24,000,000}{90} \approx 266,666.67 \text{ XOF/day} $$

Now, calculate the amount spent in those first 45 days:
$$ \text{Spent in 45 Days} = \frac{\text{Daily Rate}}{1} \times 45 $$
Alternatively, since we know they are 62% of the budget:
$$ \text{Spent in 45 Days} = 0.62 \times 24,000,000 = 14,880,000 \text{ XOF} $$

### Step 2: Calculate Remaining Budget and Time
Next, determine how much money is left to spend and for how many more days the project runs.

*   **Remaining Budget**: $24,000,000 - 14,880,000 = 9,120,000 \text{ XOF}$
*   **Total Project Duration**: 90 days (given)
*   **Days Remaining**: $90 - 45 = 45$ days

### Step 3: Calculate Total Spend on Day 90
Finally, calculate the total spend by adding the remaining budget to the daily rate. This represents the cumulative amount spent over the entire duration of the project (from day 1 through day 90).

$$ \text{Total Spend} = (\text{Daily Rate}) + (\text{Remaining Budget}) $$
Wait, a simpler way is: **Total Spend** equals the sum of all daily rates multiplied by each day. Since the rate stays constant and we are looking for the cumulative total at the end of 90 days (which effectively means spending the entire budget), let's re-evaluate the logic carefully.

The question asks "what will the total spend be on day 90". This implies the **cumulative expenditure** by the time the project ends.
Since the daily rate is constant, the cumulative spend at any point $t$ (where $1 \le t \le 90$) follows a linear progression from 0 to the full budget.

Therefore:
$$ \text{Total Spend on Day 90} = \frac{\text{Daily Rate}}{24,000,000} \times (\text{Remaining Budget}) $$
Actually, it's simpler: The total spend is simply the sum of all daily rates.


#### pénalité 1.20 — diversité 0.98, 19 s, **faux**, coupé

To find the total spend on day 90, we can break this down into logical steps based on linear projection.

### Step 1: Calculate the Daily Spending Rate
First, determine how much money was spent in a single day by dividing the cumulative spending by the number of days elapsed.

*   **Total Budget**: $24,000,000 XOF$
*   **Cumulative Spend after Day 45**: $62\% \text{ of } \$24,000,000 = 0.62 \times 24,000,000 = \$14,880,000$
*   **Days Elapsed ($t_1$)**: $45$ days

$$ \text{Daily Rate} = \frac{\text{Cumulative Spend}}{\text{Days Elapsed}} $$
$$ \text{Daily Rate} = \frac{14,880,000}{45} $$
$$ \text{Daily Rate} = 332,666.67 \text{ XOF/day (approx)} $$

### Step 2: Calculate Total Spend by Day 90
Next, calculate the total cumulative spend if this daily rate continues for the remaining days until day 90.

*   **Total Project Duration**: $90$ days
*   **Days Remaining ($t_2$)**: $90 - 45 = 45$ days (since we are projecting from Day 45 to Day 90)

$$ \text{Remaining Spend} = \text{Daily Rate} \times t_2 $$
$$ \text{Remaining Spend} = 332,666.67 \times 45 $$
$$ \text{Remaining Spend} = \$14,880,000 $$

### Step 3: Calculate Total Project Cost (Day 90)
Finally, add the remaining spend to what was already spent on Day 45 to get the total cumulative cost at day 90. Alternatively, you can calculate $62\%$ of the full budget directly since we know that after exactly half a year ($180$ days), it would be $73\%$, but here we are looking for the specific point in time where **45** more days have passed relative to our current baseline.

Actually, let's re-evaluate using percentages of the *total* budget directly as that is often cleaner:
1.  The project has spent $62\%$ after 45 days. This implies a linear relationship between time and cost.
2.  We need to find the total spend at Day 90 ($t=90$).

Let's use the ratio method directly on percentages, as it avoids rounding errors from intermediate steps:
*   At $t = 45$, Cost = $62\%$.
*   The project duration is $90$ days. Half of that duration is $45$ days ($90 / 2 = 45$).
*   Therefore, at Day 90 (which represents exactly half the total time), the cumulative spend should be **73%** of


### coût employeur · n étapes

> Un salarié perçoit 450 000 FCFA de salaire brut. Les cotisations salariales retenues sont de 6,3 %, et l'employeur verse en plus 18,45 % de charges patronales calculées sur le brut. Quel est le coût total pour l'employeur ?


#### pénalité 1.00 — diversité 0.94, 6 s, **juste**

Pour déterminer le coût total pour l'employeur, il faut d'abord calculer la part des charges patronales, puis ajouter le salaire brut lui-même.

Le salaire brut est de **450 000 FCFA**.
Les charges patronales sont calculées sur ce même montant brut à un taux de **18,45 %**.

Le calcul des charges patronales est le suivant :
$$ 450\,000 \times 0,1845 = 83\,025 \text{ FCFA} $$

Le coût total pour l'employeur est donc la somme du salaire brut et des charges patronales :
$$ 450\,000 + 83\,025 = 533\,025 \text{ FCFA} $$

Le coût total pour l'employeur est de **533 025 FCFA**.


#### pénalité 1.05 — diversité 0.98, 11 s, **faux**

Pour déterminer le coût total pour l'employeur, il faut d'abord calculer la part des charges patronales (18,45 %) sur le salaire brut, puis ajouter cette somme à la somme des cotisations salariales retenues par le salarié.

Le salaire brut est de **450 000 FCFA**.

1.  **Calcul des charges patronales** :
    $$450\,000 \times 18,45\% = 450\,000 \times 0,1845 = 83\,025 \text{ FCFA}$$

2.  **Calcul du coût total pour l'employeur** :
    Le coût total est la somme des cotisations salariales (6,3 %) et des charges patronales (18,45 %).
    $$450\,000 \times (6,3\% + 18,45\%) = 450\,000 \times 24,75\%$$
    
    Calculons d'abord la fraction :
    $$0,063 + 0,1845 = 0,2475$$
    
    Puis la multiplication :
    $$450\,000 \times 0,2475 = 111\,375 \text{ FCFA}$$

*(Vérification par addition des deux parts : $83\,025 + (450\,000 \times 0,063) = 83\,025 + 28\,350 = 111\,375$)*

Le coût total pour l'employeur est de **111 375 FCFA**.


#### pénalité 1.10 — diversité 0.97, 8 s, **faux**

Pour déterminer le coût total pour l'employeur, il faut d'abord calculer la part des charges patronales (18,45 %) sur le salaire brut, puis ajouter cette somme à la cotisation salariale retenue par le salarié.

Le salaire brut est de **450 000 FCFA**.
La charge patronale à payer par l'employeur s'élève à :
$$450\,000 \times 18,45\% = 450\,000 \times 0,1845 = 83\,025 \text{ FCFA}$$

La cotisation salariale retenue par le salarié est de :
$$450\,000 \times 6,3\% = 450\,000 \times 0,063 = 28\,350 \text{ FCFA}$$

Le coût total pour l'employeur correspond donc à la somme de ces deux montants :
$$83\,025 + 28\,350 = 111\,375 \text{ FCFA}$$

**Le coût total pour l'employeur est de 111 375 FCFA.**


#### pénalité 1.15 — diversité 0.96, 8 s, **faux**

Pour déterminer le coût total pour l'employeur, il faut d'abord calculer la part des charges patronales (18,45 %) sur le salaire brut, puis ajouter cette somme à la cotisation salariale retenue par le salarié.

Le salaire brut est de **450 000 FCFA**.
La charge patronale s'élève à : $450\,000 \times 18,45 \% = 83\,025$ FCFA.

La cotisation salariale retenue par le salarié est de **6,3 %** du salaire brut :
$450\,000 \times 6,3 \% = 28\,350$ FCFA.

Le coût total pour l'employeur correspond donc à la somme de ces deux montants (la cotisation salariale + les charges patronales) :
$28\,350 + 83\,025 = 111\,375$ FCFA.

Le coût total pour l'employeur est donc **111 375 FCFA**.


#### pénalité 1.20 — diversité 1.00, 7 s, **juste**

Pour déterminer le coût total pour l'employeur, il faut d'abord calculer la part des charges patronales (18,45 %) sur le salaire brut de 450 000 FCFA.

Le montant des charges patronales est :
$$450\,000 \times 18,45\% = 450\,000 \times 0{,}1845 = 83\,025 \text{ FCFA}$$

Le coût total pour l'employeur comprend alors le salaire brut lui-même plus ces charges patronales :
$$450\,000 + 83\,025 = 533\,025 \text{ FCFA}$$

Il est important de noter que les cotisations salariales (6,3 %) sont perçues par le salarié et ne font pas partie du coût direct pour l'employeur dans ce contexte spécifique. Le calcul ci-dessus prend en compte uniquement la rémunération brute plus ses charges patronales.


### achat+remise+tva · n étapes

> Une entreprise achète 3 imprimantes à 385 000 FCFA HT l'unité. Le fournisseur accorde 5 % de remise sur le total, puis la TVA de 18 % s'applique sur le montant remisé. Quel est le montant TTC ?


#### pénalité 1.00 — diversité 0.98, 11 s, **juste**

Pour calculer le montant TTC, nous devons suivre une logique de calcul étape par étape, en appliquant d'abord la remise, puis la TVA sur le montant final.

**Étape 1 : Calculer le prix total avant remise**
L'entreprise achète 3 imprimantes à 385 000 FCFA chacune.
$$385\,000 \times 3 = 1\,155\,000 \text{ FCFA}$$

**Étape 2 : Calculer le montant après remise (5 %)**
Le fournisseur accorde 5 % de remise sur le total.
$$1\,155\,000 \times 0,05 = 57\,750 \text{ FCFA}$$
Le montant à payer sans TVA est donc :
$$1\,155\,000 - 57\,750 = 1\,097\,250 \text{ FCFA}$$

**Étape 3 : Calculer le montant TTC après TVA (18 %)**
La TVA de 18 % s'applique sur le montant remisé (1 097 250 FCFA).
$$1\,097\,250 \times 0,18 = 197\,505 \text{ FCFA}$$

**Étape 4 : Calculer le montant final TTC**
On ajoute la TVA au montant remisé.
$$1\,097\,250 + 197\,505 = 1\,294\,755 \text{ FCFA}$$

Le montant TTC est de **1 294 755 FCFA**.


#### pénalité 1.05 — diversité 0.99, 11 s, **juste**

Pour calculer le montant TTC, nous devons suivre une logique de calcul étape par étape, en appliquant d'abord la remise avant d'appliquer la TVA.

**Étape 1 : Calcul du montant après remise**
L'entreprise achète 3 unités à 385 000 FCFA HT chacune.
Total des prix HT = $3 \times 385\,000 = 1\,155\,000$ FCFA HT.

Le fournisseur accorde une remise de 5 % sur ce total.
Montant de la remise = $1\,155\,000 \times 0,05 = 57\,750$ FCFA.

Le montant après remise (avant TVA) = $1\,155\,000 - 57\,750 = 1\,097\,250$ FCFA HT.

**Étape 2 : Calcul du montant TTC (avec la TVA)**
La TVA de 18 % s'applique sur le montant remisé (1 097 250 FCFA).
Montant de la TVA = $1\,097\,250 \times 0,18 = 197\,505$ FCFA.

Le montant TTC final est la somme du montant après remise et de la TVA.
Montant TTC = $1\,097\,250 + 197\,505 = 1\,294\,755$ FCFA.

**Conclusion :**
Le montant TTC à payer est de **1 294 755 FCFA**.


#### pénalité 1.10 — diversité 0.99, 10 s, **juste**

Pour calculer le montant TTC, nous devons suivre une logique de deux étapes distinctes : d'abord appliquer la remise au prix initial, puis appliquer la TVA sur ce nouveau montant.

**Étape 1 : Calcul du prix après remise**
Le prix total des 3 imprimantes avant remise est :
$385\,000 \times 3 = 1\,155\,000$ FCFA HT.

La remise de 5 % s'applique sur ce montant total :
$1\,155\,000 \times 5\% = 57\,750$ FCFA.

Le prix final après remise est donc :
$1\,155\,000 - 57\,750 = 1\,097\,250$ FCFA HT.

**Étape 2 : Calcul du montant TTC (incluant la TVA)**
La TVA de 18 % s'applique sur le prix final après remise ($1\,097\,250$).
Le montant à payer en plus est :
$1\,097\,250 \times 18\% = 197\,505$ FCFA.

Le montant TTC total est la somme du prix après remise et de l'impôt sur le revenu (TVA) :
$1\,097\,250 + 197\,505 = 1\,294\,755$ FCFA.

**Conclusion :**
Le montant TTC à payer est de **1 294 755 FCFA**.


#### pénalité 1.15 — diversité 1.00, 11 s, **faux**

Pour calculer le montant TTC, nous devons suivre une logique de deux étapes distinctes : d'abord appliquer la remise au prix initial, puis appliquer la TVA sur ce nouveau montant.

**Étape 1 : Calcul du prix après remise**
Le fournisseur offre 5 % de remise sur l'achat total (3 imprimantes).
*   Prix HT par unité = 385 000 FCFA
*   Total HT initial = $3 \times 385\,000 = 1\,155\,000$ FCFA
*   Montant à appliquer la remise = $1\,155\,000 - (1\,155\,000 \times 0,05) = 1\,155\,000 \times 0,95$

Le montant après remise est donc :
$$1\,155\,000 \times 0,95 = 1\,097\,250 \text{ FCFA}$$

**Étape 2 : Calcul du montant TTC (avec la TVA)**
La TVA de 18 % s'applique sur le montant remisé. Le prix final est donc ce montant multiplié par $1 + 0,18$.
*   Montant TTC = $1\,097\,250 \times 1,18$

Calculons la valeur :
$$1\,097\,250 \times 1,18 = 1\,294\,765 \text{ FCFA}$$

**Conclusion :**
Le montant TTC à payer est de **1 294 765 FCFA**.


#### pénalité 1.20 — diversité 1.00, 12 s, **faux**

Pour calculer le montant TTC, nous devons suivre une logique de deux étapes distinctes : d'abord appliquer la remise au prix initial, puis ajouter la TVA sur ce nouveau total.

**Étape 1 : Calcul du prix après remise (HT)**
Le fournisseur offre 5 % de remise sur l'achat total des 3 imprimantes.
*   Prix unitaire HT = 385 000 FCFA
*   Total initial avant remise = $3 \times 385\,000$

Calculons d'abord le montant total à la vente :
$$3 \times 385\,000 = 1\,155\,000 \text{ FCFA}$$

Appliquons ensuite la remise de 5 % sur ce montant :
*   Montant après remise (avant TVA) = $1\,155\,000 - (5 \% \times 1\,155\,000)$ ou en multipliant par $(1 - 0.05)$
$$1\,155\,000 \times 0.95 = 1\,097\,250 \text{ FCFA}$$

**Étape 2 : Calcul du montant TTC (avec TVA)**
La TVA de 18 % s'applique sur le montant remisé ($1\,097\,250$). Le prix final est donc ce montant plus la taxe.
*   Montant TTC = $1\,097\,250 \times (1 + 0.18)$

Calculons l'ajout de la TVA :
$$1\,097\,250 \times 1.18 = 1\,304\,655 \text{ FCFA}$$

**Conclusion :**
Le montant TTC à payer est **1 304 655 FCFA**.


### croissance · n étapes

> Le chiffre d'affaires est passé de 145 000 000 FCFA à 182 000 000 FCFA. Quel est le taux de croissance en pourcentage, arrondi à une décimale ?


#### pénalité 1.00 — diversité 1.00, 8 s, **juste**

Pour calculer le taux de croissance, nous devons d'abord déterminer la différence entre les deux chiffres d'affaires, puis diviser cette différence par le chiffre d'affaires initial, et enfin multiplier par 100 pour obtenir le pourcentage.

1.  **Calcul de la différence** :
    $182\,000\,000 - 145\,000\,000 = 37\,000\,000$ FCFA.

2.  **Calcul du taux de croissance** :
    $$ \frac{37\,000\,000}{145\,000\,000} \approx 0,2551724... $$

3.  **Conversion en pourcentage** :
    $$ 0,2551724... \times 100 = 25,51724...\% $$

4.  **Arrondi à une décimale** :
    Le chiffre suivant la première décimale est 1 (car le chiffre suivant est 7), ce qui signifie que nous devons arrondir vers le haut.
    $25,517... \rightarrow 25,5$

Le taux de croissance est donc de **25,5 %**.


#### pénalité 1.05 — diversité 0.99, 8 s, **juste**

Pour calculer le taux de croissance, nous devons d'abord déterminer la différence entre les deux chiffres d'affaires, puis diviser cette différence par le chiffre d'affaires initial.

1.  **Calculer la différence** :
    $182\,000\,000 - 145\,000\,000 = 37\,000\,000$ FCFA

2.  **Diviser par le chiffre d'affaires initial** :
    $\frac{37\,000\,000}{145\,000\,000} = \frac{37}{145}$

3.  **Effectuer la division** :
    $37 \div 145 \approx 0,2551724...$

4.  **Convertir en pourcentage et arrondir** :
    En multipliant par 100, nous obtenons $25,51724...\%$. Arrondi à une décimale, cela donne **25,5 %**.

Le taux de croissance est de **25,5 %**.


#### pénalité 1.10 — diversité 0.98, 11 s, **juste**

Pour calculer le taux de croissance, nous devons d'abord déterminer la différence entre les deux chiffres d'affaires et ensuite diviser cette différence par le chiffre d'affaires initial.

1.  **Calcul de la variation** :
    $182\,000\,000 - 145\,000\,000 = 37\,000\,000$ FCFA.

2.  **Calcul du taux de croissance (en pourcentage)** :
    $$ \text{Taux} = \left( \frac{\text{Variation}}{\text{Chiffre d'affaires initial}} \right) \times 100 $$
    $$ \text{Taux} = \left( \frac{37\,000\,000}{145\,000\,000} \right) \times 100 $$

    En simplifiant les termes (on peut diviser par $1\,000\,000$ et par $100$ pour obtenir un nombre plus facile à calculer) :
    $$ \frac{37}{145} = 0.2551724... $$

    Multipliant par 100 pour convertir en pourcentage :
    $$ 0.2551724... \times 100 = 25,51724...\% $$

3.  **Arrondissement** :
    Arrondi à une décimale (une place après la virgule) :
    $25,517...$ devient **25,5 %**.

Le taux de croissance est de **25,5 %**.


#### pénalité 1.15 — diversité 0.98, 13 s, **faux**

Pour calculer le taux de croissance, nous devons d'abord déterminer la différence entre les deux chiffres d'affaires et ensuite diviser cette différence par le chiffre initial.

1.  **Calcul de l'écart :**
    $182\,000\,000 - 145\,000\,000 = 37\,000\,000$ FCFA

2.  **Calculation du taux de croissance (en pourcentage) :**
    $$ \text{Taux} = \left( \frac{\text{Différence}}{\text{Chiffre d'affaires initial}} \right) \times 100 $$
    $$ \text{Taux} = \left( \frac{37\,000\,000}{145\,000\,000} \right) \times 100 $$

    En simplifiant les nombres (on peut diviser par $1\,000\,000$ pour éliminer les zéros à la fin des deux termes) :
    $$ \text{Taux} = \left( \frac{37}{145} \right) \times 100 $$

    Calculons le quotient $37 / 145$:
    $$ 37 \div 145 \approx 0,2586206... $$

    Multiplions par 100 pour obtenir la valeur en pourcentage :
    $$ 0,2586206... \times 100 = 25,86206...\%$$

3.  **Arrondissement :**
    Arrondi à une décimale (une place après le point), nous prenons la première décimale qui est un chiffre pair (8) et on arrondit vers le supérieur car le suivant est un chiffre impair (6).
    
    $25,86... \rightarrow 25,9$

Le taux de croissance est donc **25,9 %**.


#### pénalité 1.20 — diversité 1.00, 7 s, **faux**

Pour calculer le taux de croissance, nous devons d'abord déterminer la différence entre les deux chiffres d'affaires et ensuite diviser cette différence par l'année précédente.

1.  **Calcul du montant augmenté** :
    $182\,000\,000 - 145\,000\,000 = 37\,000\,000$ FCFA

2.  **Calculation de la croissance en pourcentage** (division par le chiffre d'affaires initial) :
    $$ \frac{37\,000\,000}{145\,000\,000} = 0,25586... $$

3.  **Conversion en pourcentage** et arrondissement à une décimale :
    $0,25586 \times 100 = 25,586...\%$
    
    Arrondi au chiffre de la première décimale (une décimale), nous obtenons **25,6 %**.

Le taux de croissance est donc de **25,6 %**.


### mensualités · n étapes

> Une facture de 5 400 000 FCFA HT est réglée en 3 mensualités égales, TVA de 18 % comprise. Quel est le montant de chaque mensualité TTC ?


#### pénalité 1.00 — diversité 0.95, 11 s, **juste**

Pour déterminer le montant de chaque mensualité TTC, il faut d'abord calculer le montant HT (hors TVA) de la facture, puis appliquer la TVA de 18 % à ce montant pour obtenir le montant TTC.

**Étape 1 : Calcul du montant HT**
La facture est de 5 400 000 FCFA HT.
$$5\,400\,000 \div 3 = 1\,800\,000 \text{ FCFA}$$
Le montant HT par mensualité est donc de **1 800 000 FCFA**.

**Étape 2 : Calcul du montant TTC**
La TVA de 18 % est appliquée sur le montant HT.
$$1\,800\,000 \times 0,18 = 324\,000 \text{ FCFA}$$
Le montant TTC par mensualité est donc de **324 000 FCFA**.

**Vérification :**
$$1\,800\,000 \text{ (HT)} + 324\,000 \text{ (TVA)} = 2\,124\,000 \text{ FCFA}$$
$$2\,124\,000 \div 3 = 708\,000 \text{ FCFA}$$
Le montant HT total (2 124 000) correspond bien à 18 % de 11 800 000 HT (le montant TTC total), ce qui confirme la cohérence du calcul.

**Conclusion :**
Le montant de chaque mensualité TTC est de **2 124 000 FCFA**.


#### pénalité 1.05 — diversité 0.98, 8 s, **juste**

Pour déterminer le montant de chaque mensualité TTC, il faut d'abord calculer la valeur totale à payer en **TVA incluse**, puis diviser ce total par le nombre de mensualités.

Voici les étapes de calcul :

1.  **Calcul du montant TTC par mois**
    La TVA (18 %) est déjà incluse dans le prix de 5 400 000 FCFA HT. Le montant TTC par mensualité est donc :
    $$ \frac{5\,400\,000}{3} = 1\,800\,000 \text{ FCFA} $$

2.  **Calcul du montant TTC par mois (incluant la TVA)**
    Le montant TTC de 1 800 000 FCFA inclut déjà la TVA. Pour obtenir le montant TTC final à payer mensuellement, il faut ajouter la TVA à ce montant :
    $$ 1\,800\,000 \times (1 + 0,18) = 1\,800\,000 \times 1,18 = 2\,124\,000 \text{ FCFA} $$

**Conclusion :**
Le montant de chaque mensualité TTC est de **2 124 000 FCFA**.


#### pénalité 1.10 — diversité 0.99, 10 s, **juste**

Pour déterminer le montant de chaque mensualité TTC, il faut d'abord calculer la valeur totale à payer en **TVA incluse**, puis diviser ce total par 3.

Voici les étapes de calcul :

1.  **Calcul du montant HT (Hors Taxe)** :
    La facture est déjà donnée comme étant au taux HT (5 400 000 FCFA). C'est la base sur laquelle on applique la TVA.

2.  **Calcul de la TVA** :
    Le taux de TVA est de 18 %.
    $$ \text{TVA} = 5\,400\,000 \times 0{,}18 = 972\,000 \text{ FCFA} $$

3.  **Calcul du montant TTC (Total à payer)** :
    On additionne le montant HT et la TVA pour obtenir le total final.
    $$ \text{Montant TTC} = 5\,400\,000 + 972\,000 = 6\,372\,000 \text{ FCFA} $$

4.  **Calcul de la mensualité** :
    Le montant total est réglé en 3 mensualités égales. On divise donc le montant TTC par 3.
    $$ \text{Mensualité TTC} = \frac{6\,372\,000}{3} = 2\,124\,000 \text{ FCFA} $$

**Conclusion :**
Le montant de chaque mensualité TTC est de **2 124 000 FCFA**.


#### pénalité 1.15 — diversité 0.99, 12 s, **juste**

Pour déterminer le montant de chaque mensualité TTC, il faut d'abord calculer la valeur totale à payer en **TVA incluse**, puis diviser ce total par 3.

Voici les étapes détaillées :

1.  **Calcul du montant HT (Hors Taxe)**
    La facture est déjà donnée comme étant de 5 400 000 FCFA *HT*. C'est la base sur laquelle on applique le taux de TVA.

2.  **Application du taux de TVA**
    Le taux de TVA est de 18 %. Pour trouver le montant TTC, nous multiplions l'HT par $1 + \frac{18}{100}$.
    
    $$5\,400\,000 \times (1 + 0,18) = 5\,400\,000 \times 1,18$$

    *   $5\,400\,000 \times 1 = 5\,400\,000$
    *   $5\,400\,000 \times 0,18 = 972\,000$

3.  **Calcul du montant TTC total**
    $$5\,400\,000 + 972\,000 = 6\,372\,000 \text{ FCFA}$$

4.  **Division par le nombre de mensualités**
    Le montant TTC total est divisé par 3 pour obtenir la mensualité :
    
    $$6\,372\,000 / 3 = 2\,124\,000 \text{ FCFA}$$

### Conclusion

Le montant de chaque mensualité **TTC** est de **2 124 000 FCFA**.


#### pénalité 1.20 — diversité 0.99, 9 s, **faux**

Pour déterminer le montant de chaque mensualité TTC, il faut d'abord calculer la valeur totale à payer en **TVA incluse**, puis diviser ce total par 3.

Voici les étapes détaillées :

1.  **Calcul du prix HT (Hors Taxe)**
    La facture est déjà exprimée sous forme de TVA comprise (HT TTC). Le montant initial est donc le prix final à payer en monnaie réelle, sans avoir besoin d'ajouter la TVA manuellement pour obtenir un total différent.
    
    $$ \text{Montant Total} = 5\,400\,000 \text{ FCFA} $$

2.  **Calcul du montant TTC par mensualité**
    Comme les trois mensualités sont égales et que la TVA est incluse dans le prix de vente final (ce qui signifie qu'il n'y a pas d'ajout de taxe supplémentaire sur ce montant), on divise simplement le total initial par le nombre de périodes.

    $$ \text{Mensualité TTC} = \frac{\text{Montant Total}}{3} $$
    
    $$ \text{Mensualité TTC} = \frac{5\,400\,000}{3} = 1\,800\,000 \text{ FCFA} $$

**Conclusion :**
Le montant de chaque mensualité **TTC** est de **1 800 000 FCFA**.


### masse salariale · n étapes

> A company's monthly gross payroll is 18,500,000 XOF. Employer social contributions add 18.45% on top of the gross. What is the total annual employer payroll cost?


#### pénalité 1.00 — diversité 0.88, 8 s, **faux**

To calculate the total annual employer payroll cost, we need to determine the monthly employer contribution and then multiply it by the number of months in a year.

### Step 1: Calculate the Monthly Employer Contribution
The monthly gross payroll is **18,500,000 XOF**.
The employer social contribution rate is **18.45%**.

$$ \text{Monthly Employer Cost} = \text{Gross Payroll} \times \text{Contribution Rate} $$
$$ \text{Monthly Employer Cost} = 18,500,000 \times 0.1845 $$
$$ \text{Monthly Employer Cost} = 3,413,250 \text{ XOF} $$

### Step 2: Calculate the Annual Employer Cost
There are 12 months in a year. We multiply the monthly cost by 12.

$$ \text{Annual Employer Cost} = \text{Monthly Employer Cost} \times 12 $$
$$ \text{Annual Employer Cost} = 3,413,250 \times 12 $$
$$ \text{Annual Employer Cost} = 40,959,000 \text{ XOF} $$

### Final Conclusion
The total annual employer payroll cost is **40,959,000 XOF**.


#### pénalité 1.05 — diversité 0.92, 8 s, **juste**

To calculate the total annual employer payroll cost, we need to determine the monthly contribution first and then multiply it by 12 months.

### Step 1: Calculate the Monthly Employer Contribution
The monthly gross payroll is **18,500,000 XOF**.
The employer social contributions add **18.45%** on top of the gross amount.

$$ \text{Monthly Cost} = \text{Gross Payroll} \times (1 + 18.45\%) $$
$$ \text{Monthly Cost} = 18,500,000 \times 1.1845 $$
$$ \text{Monthly Cost} = 21,913,250 \text{ XOF} $$

### Step 2: Calculate the Annual Employer Payroll Cost
To find the total annual cost, multiply the monthly cost by 12 months.

$$ \text{Annual Cost} = \text{Monthly Cost} \times 12 $$
$$ \text{Annual Cost} = 21,913,250 \times 12 $$
$$ \text{Annual Cost} = 262,959,000 \text{ XOF} $$

### Final Conclusion
The total annual employer payroll cost is **262,959,000 XOF**.


#### pénalité 1.10 — diversité 0.93, 12 s, **juste**

To calculate the total annual employer payroll cost, we need to determine two components:
1.  The **Gross Annual Payroll** (the base amount).
2.  The **Employer Social Contribution** (which is calculated on the Gross amount).

### Step 1: Calculate the Gross Annual Payroll
First, convert the monthly gross payroll into an annual figure by multiplying by 12 months.

$$ \text{Gross Annual Payroll} = 18,500,000 \times 12 $$
$$ \text{Gross Annual Payroll} = 222,000,000 \text{ XOF} $$

### Step 2: Calculate the Employer Social Contribution
The problem states that employer social contributions add **18.45%** on top of the gross payroll. This means the contribution is calculated as a percentage of the Gross Annual Payroll.

$$ \text{Employer Contribution} = \text{Gross Annual Payroll} \times 18.45\% $$
$$ \text{Employer Contribution} = 222,000,000 \times 0.1845 $$
$$ \text{Employer Contribution} = 40,959,000 \text{ XOF} $$

### Step 3: Calculate the Total Annual Employer Payroll Cost
The total cost is the sum of the Gross Annual Payroll and the Employer Social Contribution.

$$ \text{Total Cost} = \text{Gross Annual Payroll} + \text{Employer Contribution} $$
$$ \text{Total Cost} = 222,000,000 + 40,959,000 $$
$$ \text{Total Cost} = 262,959,000 \text{ XOF} $$

### Final Conclusion
The total annual employer payroll cost is **262,959,000 XOF**.


#### pénalité 1.15 — diversité 0.94, 13 s, **juste**

To calculate the total annual employer payroll cost, we need to determine two components:
1.  The **Gross Annual Payroll** (the base amount).
2.  The **Employer Social Contribution Cost**, which is calculated as a percentage of the Gross Annual Payroll.

### Step 1: Calculate the Monthly Gross Payroll in XAF
The monthly gross payroll is given as:
$$ \text{Monthly Gross} = 18,500,000 \text{ XOF} $$

To find the annual gross amount (assuming a standard year of 12 months):
$$ \text{Annual Gross Payroll} = 18,500,000 \times 12 $$
$$ \text{Annual Gross Payroll} = 222,000,000 \text{ XAF} $$

### Step 2: Calculate the Employer Social Contribution Cost
The employer contributes **18.45%** on top of the gross payroll annually. This means for every year's worth of salary paid to employees, the company pays an additional tax/fee equal to that percentage.

$$ \text{Employer Contribution} = \text{Annual Gross Payroll} \times 18.45\% $$
$$ \text{Employer Contribution} = 222,000,000 \times 0.1845 $$
$$ \text{Employer Contribution} = 40,959,000 \text{ XAF} $$

### Step 3: Calculate the Total Annual Employer Payroll Cost
The total cost includes both the gross salary paid to employees and the employer's contribution.

$$ \text{Total Cost} = \text{Annual Gross Payroll} + \text{Employer Contribution} $$
$$ \text{Total Cost} = 222,000,000 + 40,959,000 $$
$$ \text{Total Cost} = 262,959,000 \text{ XAF} $$

### Conclusion
The total annual employer payroll cost is **262,959,000 XOF**.


#### pénalité 1.20 — diversité 0.99, 19 s, **faux**, coupé

To calculate the total annual employer payroll cost, we need to determine two components:
1.  The **Gross Annual Payroll** (the base amount).
2.  The **Employer Social Contribution Cost**, which is calculated as a percentage of that gross amount plus any additional fixed costs mentioned in your scenario.

### Step-by-Step Calculation

#### 1. Calculate the Gross Monthly Payroll
The problem states the monthly gross payroll is:
$$ \text{Gross Monthly} = \$XOF\,18,500,000 $$

To find the annual gross amount (assuming a standard year of 365 days):
$$ \text{Annual Gross Payroll} = 18,500,000 \times 365 $$
$$ \text{Annual Gross Payroll} = \$XOF\,67,525,000 $$

#### 2. Calculate the Employer Social Contribution Cost
The problem states that employer social contributions add **18.45%** on top of the gross payroll annually (based on standard CFAA tax rates in Mali where this figure typically applies). This is calculated as:
$$ \text{Contribution} = \text{Annual Gross Payroll} \times 0.1845 $$

Using our annual amount from Step 1 ($67,525,000):
$$ \text{Contribution Cost} = 67,525,000 \times 0.1845 $$
$$ \text{Contribution Cost} = \$XOF\,12,463,962.50 $$

*(Note: If the calculation is strictly based on monthly figures first—$18,500,000 \times 0.1845$, then multiplied by 12 months—the result remains identical due to mathematical equivalence).*
$$ (18,500,000 \times 365) \times 0.1845 = \$XOF\,12,463,962.50 $$

#### 3. Calculate Total Annual Employer Payroll Cost
The total cost is the sum of the Gross Annual Payroll and the Contribution:
$$ \text{Total} = \text{Gross Annual Payroll} + \text{Contribution Cost} $$
$$ \text{Total} = \$XOF\,67,525,000 + \$XOF\,12,463,962.50 $$

Alternatively, you can calculate the total percentage of gross payroll: $18.45\%$ (contribution) is added to 100% (gross), resulting in a **total cost factor** of $118.45\%$.
$$ \text{Total Cost} = \$XOF\,67,525,000 \times 1.1845 $$

Calculation:
$$ 67,525,000 \times 1.1845 = 80,039,662.50 $$

### Final Conclusion

The total annual employer payroll cost


### comparaison offres · n étapes

> Deux fournisseurs sont en concurrence : A propose 12 000 FCFA l'unité avec 8 % de remise, B propose 11 500 FCFA l'unité sans remise. Pour une commande de 500 unités, quel est l'écart de prix total entre les deux offres ?


#### pénalité 1.00 — diversité 0.94, 10 s, **faux**

Pour déterminer l'écart de prix total, nous devons d'abord calculer le prix final pour chaque fournisseur en appliquant leurs conditions spécifiques, puis en soustrayant le prix de B du prix de A.

**1. Calcul du prix final pour le fournisseur A :**
Le prix proposé par A est de 12 000 FCFA par unité avec une remise de 8 %.
*   Prix net par unité : $12\,000 \times (1 - 0,08) = 12\,000 \times 0,92 = 11\,160$ FCFA.
*   Total pour 500 unités : $11\,160 \times 500 = 5\,580\,000$ FCFA.

**2. Calcul du prix final pour le fournisseur B :**
Le prix proposé par B est de 11 500 FCFA par unité sans remise.
*   Total pour 500 unités : $11\,500 \times 500 = 5\,750\,000$ FCFA.

**3. Calcul de l'écart de prix total :**
L'écart est la différence entre le prix total de B et le prix total de A.
*   Écart : $5\,750\,000 - 5\,580\,000 = 170\,000$ FCFA.

L'écart de prix total entre les deux offres est de **170 000 FCFA**.


#### pénalité 1.05 — diversité 0.94, 9 s, **juste**

Pour déterminer l'écart de prix total, nous devons d'abord calculer le prix final pour chaque fournisseur en appliquant leurs conditions spécifiques.

**1. Calcul du prix pour le Fournisseur A :**
Le prix proposé par A est de 12 000 FCFA par unité avec une remise de 8 %.
*   Prix net : $12\,000 \times 0,92 = 11\,040$ FCFA
*   Total pour 500 unités : $11\,040 \times 500 = 5\,520\,000$ FCFA

**2. Calcul du prix pour le Fournisseur B :**
Le prix proposé par B est de 11 500 FCFA par unité sans remise.
*   Total pour 500 unités : $11\,500 \times 500 = 5\,750\,000$ FCFA

**3. Calcul de l'écart :**
L'écart est la différence entre le prix total de B et celui de A.
*   Écart : $5\,750\,000 - 5\,520\,000 = 230\,000$ FCFA

L'écart de prix total entre les deux offres est de **230 000 FCFA**.


#### pénalité 1.10 — diversité 0.97, 17 s, **juste**

Pour déterminer l'écart de prix total, nous devons d'abord calculer le prix final pour chaque fournisseur en appliquant leurs conditions spécifiques.

**1. Calcul du prix pour le Fournisseur A :**
Le prix proposé par A est de 12 000 FCFA par unité avec une remise de 8 %.
*   Prix net : $12\,000 \times (1 - 0,08) = 12\,000 \times 0,92$
*   Prix net A : **11 040 FCFA** par unité.

Pour une commande de 500 unités :
*   Total A : $11\,040 \times 500 = 5\,520\,000$ FCFA.

*(Alternative rapide : On peut aussi calculer le prix total avant remise pour A : $(12\,000 - (8/100 \times 12\,000)) \times 500 = 960 \times 500 = 480\,000$ FCFA. Ensuite on ajoute la remise sur ce montant : $480\,000 - (320 \times 500) = 480\,000 - 160\,000 = 320\,000$. *Correction nécessaire ici* : La formule est $(Prix_{net} \times Quantité)$.
Re-calculons soigneusement pour A :
Prix net par unité = $12\,000 - (8/100 \times 12\,000) = 12\,000 - 960 = 11\,040$ FCFA.
Total A = $11\,040 \times 500 = 5\,520\,000$ FCFA.

**2. Calcul du prix pour le Fournisseur B :**
Le prix proposé par B est de 11 500 FCFA par unité sans remise.
*   Total B : $11\,500 \times 500 = 5\,750\,000$ FCFA.

**3. Calcul de l'écart :**
L'écart est la différence entre le prix total de B et celui de A.
*   Écart = Total B - Total A
*   Écart = $5\,750\,000 - 5\,520\,000$
*   Écart = **230 000 FCFA**

L'écart de prix total entre les deux offres est de **230 000 FCFA**.


#### pénalité 1.15 — diversité 0.93, 15 s, **faux**

Pour déterminer l'écart de prix total, nous devons d'abord calculer le coût final pour chaque fournisseur en tenant compte des conditions spécifiques (remise ou non).

**1. Analyse de la proposition du Fournisseur A :**
*   Prix unitaire : 12 000 FCFA
*   Remise applicable : 8 %
*   Le prix net à payer par unité est donc $12\,000 \times (1 - 0,08) = 12\,000 \times 0,92$.

**2. Analyse de la proposition du Fournisseur B :**
*   Prix unitaire : 11 500 FCFA
*   Remise applicable : Aucune (prix net à payer par unité est donc $11\,500$).

**3. Calcul du coût total pour une commande de 500 unités :**

*   **Coût A (avec remise) :**
    $$12\,000 \times 0,92 = 11\,160 \text{ FCFA par unité}$$
    Pour 500 unités : $11\,160 \times 500 = 5\,580\,000$ FCFA.

*   **Coût B (sans remise) :**
    $$11\,500 \text{ FCFA par unité}$$
    Pour 500 unités : $11\,500 \times 500 = 5\,750\,000$ FCFA.

**4. Calcul de l'écart :**
L'écart est la différence entre le coût total B et celui A (ou vice-versa).
$$Ecart = 5\,750\,000 - 5\,580\,000 = 170\,000 \text{ FCFA}$$

*(Note : On peut aussi vérifier l'écart par unité d'abord. L'avantage de A est de $240$ FCFA (différence entre les prix unitaires) moins la remise de $8\%$. Le gain net par unité pour B par rapport à A est donc $170\,000 / 500 = 340$ FCFA. Cela correspond bien à l'écart total).*

**Réponse :**
L'écart de prix total entre les deux offres est de **170 000 FCFA**.


#### pénalité 1.20 — diversité 0.94, 13 s, **faux**

Pour déterminer l'écart de prix total, nous devons d'abord calculer le coût final pour chaque fournisseur en tenant compte des conditions spécifiques (remise ou non).

**1. Analyse du Fournisseur A :**
*   Prix unitaire : 12 000 FCFA
*   Remise applicable : 8 %
*   Le prix net à payer par unité est donc $12\,000 \times (1 - 0{,}08)$.

**2. Analyse du Fournisseur B :**
*   Prix unitaire : 11 500 FCFA
*   Remise applicable : Aucune remise n'est faite. Le prix net à payer par unité est donc $11\,500 \times (1 - 0)$.

**3. Calcul du coût total pour la commande de 500 unités :**

Pour le Fournisseur A :
$$C_A = 12\,000 \times (1 - 0{,}08) \times 500$$
$$C_A = 9\,600 \text{ FCFA/unité} \times 500 = 4\,800\,000 \text{ FCFA}$$

Pour le Fournisseur B :
$$C_B = 11\,500 \times (1 - 0) \times 500$$
$$C_B = 11\,500 \text{ FCFA/unité} \times 500 = 5\,750\,000 \text{ FCFA}$$

**4. Calcul de l'écart :**
L'écart est la différence entre le coût total du Fournisseur B et celui du Fournisseur A :
$$Écart = C_B - C_A$$
$$Écart = 5\,750\,000 - 4\,800\,000 = 950\,000 \text{ FCFA}$$

L'écart de prix total entre les deux offres est donc **de 950 000 FCFA**.


### pénalité partielle · n étapes

> An order of 320 units at 7,250 XOF each is shipped in four batches. The first two batches, which together represent half the order, arrive late and incur a 3% penalty on their value. What is the penalty amount?


#### pénalité 1.00 — diversité 0.91, 10 s, **juste**

To calculate the penalty amount, we need to determine the value of the late batches and apply the penalty percentage to that value.

### Step 1: Calculate the total value of the order
First, determine the total value of the 320 units.
$$ \text{Total Value} = \text{Quantity} \times \text{Unit Price} $$
$$ \text{Total Value} = 320 \times 7,250 = 2,320,000 \text{ XOF} $$

### Step 2: Determine the value of the late batches
The problem states that the first two batches represent **half** the order.
$$ \text{Late Value} = \text{Total Value} \times 50\% $$
$$ \text{Late Value} = 2,320,000 \times 0.5 = 1,160,000 \text{ XOF} $$

### Step 3: Calculate the penalty amount
The penalty is calculated on the value of the late batches at a rate of 3%.
$$ \text{Penalty} = \text{Late Value} \times 3\% $$
$$ \text{Penalty} = 1,160,000 \times 0.03 $$
$$ \text{Penalty} = 34,800 \text{ XOF} $$

### Conclusion
The penalty amount is **34,800 XOF**.


#### pénalité 1.05 — diversité 0.95, 12 s, **juste**

To calculate the penalty amount, we need to determine the value of the late batches and apply the 3% penalty rate.

### Step 1: Calculate the Value of One Batch
First, find the monetary value of a single batch by multiplying the quantity per batch by the unit price.

*   **Order Quantity**: 320 units
*   **Unit Price**: 7,250 XOF
*   **Total Order Value** = $320 \times 7,250$

$$320 \times 7,250 = 2,320,000 \text{ XOF}$$

### Step 2: Determine the Value of the Late Batches
The problem states that the first two batches together represent **half** the order.

*   **Late Batch Value** = $\frac{1}{2} \times \text{Total Order Value}$
*   **Late Batch Value** = $\frac{1}{2} \times 2,320,000$
*   **Late Batch Value** = $1,160,000 \text{ XOF}$

### Step 3: Calculate the Penalty Amount
The penalty is calculated as 3% of the value of the late batches.

*   **Penalty Rate**: 3% or $0.03$
*   **Penalty Amount** = $\text{Late Batch Value} \times 0.03$
*   **Penalty Amount** = $1,160,000 \times 0.03$

$$1,160,000 \times 0.03 = 34,800 \text{ XOF}$$

### Final Conclusion
The penalty amount is **34,800 XOF**.


#### pénalité 1.10 — diversité 0.96, 14 s, **juste**

To calculate the penalty amount, we need to determine the value of the late batches and apply the 3% penalty rate.

### Step 1: Calculate the Value of One Batch
First, find the monetary value of a single batch by multiplying the quantity per batch by the unit price.

*   **Order Quantity**: 320 units
*   **Unit Price**: XOF 7,250
*   **Total Order Value** = $320 \times 7,250$

$$320 \times 7,250 = 2,320,000 \text{ (XOF)}$$

### Step 2: Determine the Quantity of Late Batches
The problem states that the first two batches together represent **half** the order.

*   **Late Batch Quantity** = $\frac{1}{2} \times 320$
*   **Late Batch Quantity** = $160$ units

### Step 3: Calculate the Value of the Late Batches
Now, calculate the total value for these two late batches. Since they represent half the order, their value is also half the total order value.

$$ \text{Value of Late Batches} = \frac{2,320,000}{2} $$
$$ \text{Value of Late Batches} = 1,160,000 \text{ (XOF)} $$

*(Alternatively: $160 \times 7,250 = 1,160,000$)*

### Step 4: Calculate the Penalty Amount
Apply the 3% penalty to the value of the late batches.

*   **Penalty Rate**: 3% or $0.03$
*   **Base Value for Penalty** = $1,160,000 \text{ XOF}$

$$ \text{Penalty Amount} = 1,160,000 \times 0.03 $$
$$ \text{Penalty Amount} = 34,800 \text{ (XOF)} $$

### Conclusion
The penalty amount is **34,800 XOF**.


#### pénalité 1.15 — diversité 0.97, 12 s, **faux**

To calculate the penalty amount, we need to determine the value of the late batches and apply the 3% penalty rate.

### Step 1: Calculate the Value of One Batch
First, find out how much one single batch costs by dividing the total order value by the number of batches (4).

$$ \text{Value per batch} = \frac{\text{Total Order Value}}{\text{Number of Batches}} $$
$$ \text{Value per batch} = \frac{7,250}{4} = 1,812.5 \text{ XOF} $$

### Step 2: Calculate the Total Late Batch Value
The problem states that the first two batches together represent half of the order (i.e., $50\%$). We can calculate this directly by taking one batch's value and multiplying it by 2, or by calculating what is half of the total.

$$ \text{Late Batch Total} = \frac{\text{Total Order Value}}{4} $$
$$ \text{Late Batch Total} = 1,812.5 \times 2 = 3,625 \text{ XOF} $$

*(Alternatively: $7,250 / 2 = 3,625$)*

### Step 3: Calculate the Penalty Amount
The penalty is calculated on the value of these late batches at a rate of 3%.

$$ \text{Penalty} = \text{Late Batch Total} \times 3\% $$
$$ \text{Penalty} = 3,625 \times 0.03 $$
$$ \text{Penalty} = 108.75 \text{ XOF} $$

### Final Conclusion
The penalty amount is **108.75 XOF**.


#### pénalité 1.20 — diversité 0.97, 19 s, **faux**, coupé

To calculate the penalty amount, we need to determine the value of the late batches and apply the 3% penalty rate.

### Step 1: Calculate the Value per Batch
The total order consists of **4** equal batches (since it is shipped in four batches).
$$ \text{Value per batch} = \frac{\text{Total Order}}{\text{Number of Batches}} $$
Given that there are $320$ units at a price of XOF 7,250 each:

1.  **Calculate Total Value**:
    $$ 320 \times 7,250 = 2,320,000 \text{ (XOF)} $$

2.  **Value per batch**:
    Since the order is split into four batches of equal value:
    $$ \frac{2,320,000}{4} = 580,000 \text{ XOF per batch} $$

### Step 2: Calculate the Value of Late Batches
The problem states that **two** batches arrive late. These two batches represent half ($\frac{1}{2}$) of the total order value (since $4$ batches $\times \frac{1}{2} = 2$).

$$ \text{Value of late batches} = 580,000 \times 2 $$
Alternatively:
$$ \text{Total Order Value} - (\text{Early Batches}) = 2,320,000 - (146,000) = 2,174,000 $$

So, the value of the late batches is **$2,174,000 \text{ XOF}$**.
*(Note: $580,000 / 320 = 1.8125$, so one batch is worth $\approx 1,960$. Two batches are roughly $3,920$? Wait, let's re-verify the math logic above).*

**Correction on Logic Check:**
Let's recalculate strictly based on units to ensure no rounding errors.
*   Total Value = $320 \times 7,250 = 2,320,000$.
*   One batch value = $\frac{2,320,000}{4} = 580,000$ XOF.
*   Two late batches value = $580,000 \times 2 = 1,160,000$.

**Wait**, the prompt says "The first two batches... arrive late". This implies there are exactly **4** distinct units/batches in total for this specific order.
If Batch A and Batch B (Total Value $580k$) are late:
Value of Late = $2 \times 580,000 = 1,160,000$.

Let's re-read carefully: "The first two batches... arrive late". This implies the order is divided into **4** equal parts.
Total Value = $320 \text{ units} \times \$7,250/\text{unit


### loyer indexé · n étapes

> Le loyer annuel d'un bureau est de 9 600 000 FCFA. Quel sera-t-il après deux augmentations annuelles successives de 4 % ?


#### pénalité 1.00 — diversité 0.93, 11 s, **juste**

Pour calculer le loyer annuel après deux augmentations successives, il faut appliquer la formule de l'augmentation sur deux périodes. La formule est :

$$L_{final} = L_{initial} \times (1 + r)^n$$

Où :
*   $L_{initial} = 9\,600\,000$ FCFA
*   $r = 4\% = 0,04$
*   $n = 2$ (nombre d'augmentations)

**Étape 1 : Calcul de la valeur après la première augmentation**
$$L_1 = 9\,600\,000 \times (1 + 0,04)^1 = 9\,600\,000 \times 1,04 = 9\,984\,000 \text{ FCFA}$$

**Étape 2 : Calcul de la valeur après la deuxième augmentation**
$$L_2 = 9\,984\,000 \times (1 + 0,04)^1 = 9\,984\,000 \times 1,04 = 10\,383\,360 \text{ FCFA}$$

On peut aussi effectuer le calcul directement en combinant les deux facteurs :
$$L_2 = 9\,600\,000 \times (1,04)^2 = 9\,600\,000 \times 1,0816 = 10\,383\,360 \text{ FCFA}$$

Le loyer annuel après deux augmentations est de **10 383 360 FCFA**.


#### pénalité 1.05 — diversité 0.97, 11 s, **juste**

Pour calculer le loyer annuel après deux augmentations successives, il faut appliquer la formule de l'augmentation sur chaque année à tour de rôle. La formule est :

$$L_{n+1} = L_n \times (1 + r)$$

Où :
*   $L_n$ est le loyer de l'année $n$.
*   $r$ est la fraction de l'augmentation (ici $4\% = 0,04$).
*   $L_{n+1}$ est le loyer de l'année suivante.

**Année 1 :**
Le loyer initial est de $9\,600\,000$ FCFA.
Après une augmentation de 4 % :
$$9\,600\,000 \times 1,04 = 9\,984\,000 \text{ FCFA}$$

**Année 2 :**
On applique l'augmentation sur le nouveau loyer (9 984 000 FCFA).
$$9\,984\,000 \times 1,04 = 10\,383\,360 \text{ FCFA}$$

On peut aussi effectuer ce calcul en un seul pas en multipliant le loyer initial par $(1,04)^2$ :
$$9\,600\,000 \times (1,04)^2 = 9\,600\,000 \times 1,0816 = 10\,383\,360 \text{ FCFA}$$

Le loyer annuel après deux augmentations successives est de **10 383 360 FCFA**.


#### pénalité 1.10 — diversité 0.97, 9 s, **juste**

Pour calculer le loyer annuel après deux augmentations successives, il faut appliquer la formule de l'augmentation sur chaque année à tour de rôle. La formule est :

$$L_{n+1} = L_n \times (1 + r)$$

Où $r$ représente la fraction de l'augmentation (ici $4\%$, soit $0,04$).

**Année 1 :**
Le loyer initial étant de $9\,600\,000$ FCFA, après une augmentation de 4 %, le nouveau loyer est :
$$9\,600\,000 \times (1 + 0,04) = 9\,600\,000 \times 1,04 = 9\,984\,000 \text{ FCFA}$$

**Année 2 :**
On applique la même augmentation au nouveau loyer de l'année précédente :
$$9\,984\,000 \times (1 + 0,04) = 9\,984\,000 \times 1,04 = 10\,383\,360 \text{ FCFA}$$

Le loyer annuel après deux augmentations successives est de **10 383 360 FCFA**.


#### pénalité 1.15 — diversité 0.97, 11 s, **juste**

Pour calculer le loyer annuel après deux augmentations successives, il faut appliquer la formule de l'augmentation sur chaque année à tour de rôle. La formule est :

$$L_{n+1} = L_n \times (1 + r)$$

Où $r$ représente la fraction de l'augmentation (ici 4 % soit 0,04).

**Année 1 :**
Le loyer initial étant de **9 600 000 FCFA**, après une augmentation de 4 %, le nouveau montant est :
$$9\,600\,000 \times (1 + 0,04) = 9\,600\,000 \times 1,04 = 9\,984\,000 \text{ FCFA}$$

**Année 2 :**
On applique la même augmentation au nouveau loyer de l'année précédente :
$$9\,984\,000 \times (1 + 0,04) = 9\,984\,000 \times 1,04 = 10\,383\,360 \text{ FCFA}$$

Il est également possible de calculer cela en multipliant le loyer initial par la puissance $(1+r)^n$ :
$$9\,600\,000 \times (1,04)^2 = 9\,600\,000 \times 1,0816 = 10\,383\,360 \text{ FCFA}$$

Le loyer annuel après deux augmentations est donc de **10 383 360 FCFA**.


#### pénalité 1.20 — diversité 0.96, 13 s, **juste**

Pour calculer le loyer annuel après deux augmentations successives, il faut appliquer la formule de l'augmentation sur chaque année à tour de rôle. La formule est :

$$L_{n+1} = L_n \times (1 + r)$$

Où $r$ représente la fraction d'augmentation en décimale ($4\% = 0,04$).

**Année 1 :**
Le loyer initial étant de **9 600 000 FCFA**, après une augmentation de 4 %, le nouveau montant est :
$$L_2 = 9 \,600 \,000 \times (1 + 0,04) = 9 \,600 \,000 \times 1,04 = 9 \,984 \,000 \text{ FCFA}$$

**Année 2 :**
On applique maintenant l'augmentation de 4 % sur le loyer obtenu à la fin de l'année précédente ($L_2$) :
$$L_{3} = L_2 \times (1 + 0,04) = 9 \,984 \,000 \times 1,04$$

Faisons les calculs étape par étape pour éviter d'écrire des nombres trop longs à la main :
$$(9 \,984 \,000 \times 2) / 5 = (19 \,968 \,000) / 5 = 3 \,993 \,600$$

Ou simplement : $9\,984\,000 + (9\,984\,000 \times 0,04)$
$= 9\,984\,000 + 399\,360 = 10\,383\,360$.

Le loyer annuel après deux augmentations successives est donc de **10 383 360 FCFA**.


### régie · n étapes

> Une équipe facture 45 000 FCFA de l'heure, toutes personnes confondues. Un projet demande 3 semaines à 35 heures par semaine. Quel est le montant HT ?


#### pénalité 1.00 — diversité 1.00, 6 s, **juste**

Pour calculer le montant HT (Hors Taxe), nous devons d'abord déterminer le nombre total d'heures travaillées par l'équipe, puis multiplier ce nombre par le tarif horaire.

**Étape 1 : Calculer le nombre total d'heures**
Le projet dure 3 semaines, et chaque semaine dure 35 heures.
$$3 \text{ semaines} \times 35 \text{ heures/semaine} = 105 \text{ heures}$$

**Étape 2 : Calculer le montant HT**
L'équipe facture 45 000 FCFA par heure.
$$105 \text{ heures} \times 45\,000 \text{ FCFA/heure} = 4\,725\,000 \text{ FCFA}$$

Le montant HT est donc de **4 725 000 FCFA**.


#### pénalité 1.05 — diversité 1.00, 6 s, **juste**

Pour calculer le montant HT (Hors Taxe), nous devons d'abord déterminer le nombre total de heures travaillées par l'équipe, puis appliquer le taux de facturation.

**Étape 1 : Calcul du nombre total de heures**
Le projet dure 3 semaines, et chaque semaine dure 35 heures.
$$3 \text{ semaines} \times 35 \text{ heures/semaine} = 105 \text{ heures}$$

**Étape 2 : Calcul du montant HT**
L'équipe facture 45 000 FCFA par heure. Nous multiplions le nombre total d'heures par ce taux.
$$105 \text{ heures} \times 45\,000 \text{ FCFA/heure} = 4\,725\,000 \text{ FCFA}$$

Le montant HT est donc de **4 725 000 FCFA**.


#### pénalité 1.10 — diversité 0.98, 9 s, **faux**

Pour calculer le montant HT (Hors Taxe), nous devons d'abord déterminer le nombre total de heures travaillées par l'équipe, puis appliquer la facturation horaire.

**Étape 1 : Calcul du nombre total de semaines**
Le projet dure 3 semaines.
$$3 \text{ semaines} = 3 \times 52 \text{ semaines (en moyenne)} = 156 \text{ semaines}$$
*(Note : Dans les contextes d'examens ou de calculs standards, on utilise souvent le nombre de semaines par an, soit 52. Si l'on considère un cycle annuel complet, cela reste la même logique).*

**Étape 2 : Calcul du nombre total de heures**
Chaque semaine dure 35 heures.
$$156 \text{ semaines} \times 35 \text{ heures/semaine} = 5\,460 \text{ heures totales}$$

**Étape 3 : Calcul du montant HT**
L'équipe facture 45 000 FCFA par heure.
$$5\,460 \text{ heures} \times 45\,000 \text{ FCFA/heure} = 245\,700\,000 \text{ FCFA}$$

Le montant HT est donc de **245 700 000 FCFA**.


#### pénalité 1.15 — diversité 0.99, 8 s, **faux**

Pour calculer le montant HT (Hors Taxe), nous devons d'abord déterminer la **heure totale** de travail nécessaire pour le projet, puis appliquer le tarif horaire.

1.  **Calcul du nombre total d'heures :**
    Le projet dure 3 semaines et nécessite 35 heures par semaine.
    $$3 \text{ semaines} \times 35 \text{ heures/semaine} = 105 \text{ heures totales}$$

2.  **Calcul du montant HT :**
    L'équipe facture 45 000 FCFA pour les 105 heures de travail. Nous divisons le total par le nombre d'heures pour trouver la valeur horaire, puis nous multiplions par le nombre d'heures (ou directement en divisant le montant HT par l'heure totale).
    $$45\,000 \text{ FCFA} / 105 \text{ heures} = 428,57 \dots \text{ FCFA/heure}$$

3.  **Calcul du total final :**
    $$105 \text{ heures} \times (4\,500 / 105) = 45\,000 \text{ FCFA}$$

Le montant HT est donc de **45 000 FCFA**.


#### pénalité 1.20 — diversité 1.00, 9 s, **juste**

Pour calculer le montant HT (Hors Taxe), nous devons d'abord déterminer la **heure totale** de travail nécessaire pour l'équipe, puis appliquer leur taux facturé.

1.  **Calcul du nombre total d'heures par semaine :**
    L'équipe travaille 35 heures par semaine sur une durée de 3 semaines.
    $$ \text{Heures totales} = 35 \times 3 = 105 \text{ heures} $$

2.  **Calcul du montant HT total :**
    Le taux facturé est de 45 000 FCFA par heure pour l'ensemble des personnes (c'est-à-dire que la somme totale des salaires ou le prix unitaire global s'applique à chaque heure).
    
    $$ \text{Montant HT} = 105 \times 45\,000 $$

    *Calcul étape par étape :*
    $105 \times 45\,000$
    $= (100 + 5) \times 45\,000$
    $= 4\,500\,000 + 225\,000$
    $= 4\,725\,000$

Le montant HT est donc de **4 725 000 FCFA**.


### boucle-1 · hors-domaine

> Traduis en dioula (jula), et donne uniquement la traduction : « Votre commande est prête. Merci de passer la retirer au magasin. »


#### pénalité 1.00 — diversité 0.05, 11 s, coupé

Diiwul: "Diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul, diiwul,

_(…coupé ici : 639 caractères de boucle)_


#### pénalité 1.05 — diversité 1.00, 2 s

Diiwul: "Diiwul, diiwul. Diiwul, diiwul."


#### pénalité 1.10 — diversité 1.00, 2 s

Diiwul: "Sok, komandom dëk. Diiwul, pasan dëgën ña gën ci magasin."


#### pénalité 1.15 — diversité 1.00, 1 s

Diiwul: "Sok, komandom dëk. Diiwul."


#### pénalité 1.20 — diversité 1.00, 1 s

Diiwul: "Sok, komandom dëk. Diiwul."


### boucle-2 · hors-domaine

> Un commerçant d'Abidjan veut un message court en dioula pour prévenir ses clients que la boutique ouvre à 8 h. Écris ce message.


#### pénalité 1.00 — diversité 0.02, 11 s, coupé

Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy, mouna!
Mouy,


#### pénalité 1.05 — diversité 1.00, 2 s

Mouy, mouna!
La boubou a kòlè 8 h.
Mouna, mouna!


#### pénalité 1.10 — diversité 1.00, 2 s

Mouy, mouna!
La boubou a kòlè 8 h.
Kòlè la, wòt la boubou.


#### pénalité 1.15 — diversité 1.00, 2 s

Mouy, mouna!
La boubaka a **8 h** (8:00).
Kénni, kòdè.


#### pénalité 1.20 — diversité 1.00, 2 s

Mouy, mouna!
La boubaka a **8 h** (madi).

Kénni ne bañ ni.


### boucle-3 · hors-domaine

> Une boutique de Dakar veut un message court en wolof pour annoncer que la livraison est gratuite cette semaine. Écris ce message.


#### pénalité 1.00 — diversité 0.06, 11 s, coupé

Waaye, waaye!
**Dakara, waaye!**
**Dakara, waaye!**
**Dakara, waaye!**

**Dakara, waaye!**
**Dakara, waaye!**
**Dakara, waaye!**

**Dakara, waaye!**
**Dakara, waaye!**
**Dakara, waaye!**

**Dakara, waaye!**
**Dakara, waaye!**
**Dakara, waaye!**

**Dakara, waaye!**
**Dakara, waaye!**
**Dakara, waaye!**

**Dakara, waaye!**
**Dakara, waaye!**
**Dakara, waaye!**

**Dakara, waaye!**
**Dakara, waaye!**
**Dakara, waaye!**

**Dakara, waaye!**
**Dakara, waaye!**
**Dakara, waaye!**

**Dakara, waaye!**
**Dakara, waaye!**
**Dakara, waaye!**

**Dakara, waaye!**
**Dakara, waaye!**
**Dakara, waaye!**

**Daka

_(…coupé ici : 857 caractères de boucle)_


#### pénalité 1.05 — diversité 0.09, 11 s, coupé

Waaye, waaye!
**Dakara, waaye!**
**Sowol, waaye!**

**Mee, waaye!**
**Lii, waaye!**
**Lii, waaye!**

**Lii, waaye!**
**Lii, waaye!**
**Lii, waaye!**

**Lii, waaye!**
**Lii, waaye!**
**Lii, waaye!**

**Lii, waaye!**
**Lii, waaye!**
**Lii, waaye!**

**Lii, waaye!**
**Lii, waaye!**
**Lii, waaye!**

**Lii, waaye!**
**Lii, waaye!**
**Lii, waaye!**

**Lii, waaye!**
**Lii, waaye!**
**Lii, waaye!**

**Lii, waaye!**
**Lii, waaye!**
**Lii, waaye!**

**Lii, waaye!**
**Lii, waaye!**
**Lii, waaye!**

**Lii, waaye!**
**Lii, waaye!**
**Lii, waaye!**

**Lii, waaye!**
**Lii, waaye!**
**Lii, waaye!**

**Lii, wa

_(…coupé ici : 818 caractères de boucle)_


#### pénalité 1.10 — diversité 1.00, 3 s

Waaye, waaye!
**Dakara!**
L'abbaal dëkkoroo **waaye** (gratuit) laa!
Laawuun, laawuun, laawuun.
Mee naa jëlloo ñaariin.

Waaye, waaye!


#### pénalité 1.15 — diversité 1.00, 4 s

Waaye, waaye!
**Dakara!**

L'abbaal la **dowol** (livraison) wallaawuunniin.
Meejooonnaa:
*   Waayaa jibbiiɗi 100% wallaawuunniin.
*   Waaye waaye, waaye!

Jalkeeɗum ñaɓat (contact) e-mail walla phone.
Waaye waaye, waaye!


#### pénalité 1.20 — diversité 1.00, 2 s

Waaye, waaye!
**Dakara!**

L'abbaal la **dowolofaayin** (livraison) walli **waalee**, daga 10 ci ñu. Waaye, wéppooñ nañu?
