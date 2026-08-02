# African use case — why this model belongs on a laptop in Abidjan

This is the claim behind `"african_alpha_claim": true` in `metadata.json`.

It is written to be checked. Every figure below carries a source, and the section
**[What we do not claim](#what-we-do-not-claim)** exists because a use case that only lists
advantages is a brochure, not evidence.

---

## 1. Who this is for

Côte d'Ivoire counts **more than 82 000 formal enterprises**, of which **over 98 % are SMEs**,
and **72,3 % of them sit in Abidjan** [1]. Together they produce about **20 % of GDP** [1] —
a small share for so many firms, which is precisely the productivity gap this work addresses.

The concrete profile we design for: a **40-person distribution company in Abidjan**. It has a
handful of laptops, an accountant, a warehouse, and a filing cabinet's worth of documents that
decide money — supplier contracts with penalty clauses, invoices in FCFA, HR policies, meeting
notes. Nobody in the company is a machine-learning engineer. The laptop is a refurbished i5 with
8 GB of RAM, which is exactly the ADTC Standard Laptop profile.

---

## 2. What actually breaks

### The grid

In the World Bank Enterprise Survey of 2023, **80,4 % of Ivorian firms reported experiencing
electrical outages**, and affected firms put the resulting loss at **2 % of annual sales** [2][3].
This is not a legacy problem being solved away: in **February 2026 national demand rose 14 %**
year on year, roughly 22 communes saw recurring and longer cuts, and on **1 April 2026 the
government released 32 billion FCFA** as an emergency measure to stabilise the network [4][5].

There is a detail that decides the architecture, and anyone who has worked through an Abidjan
outage knows it:

> **The laptop has a battery. The fibre box does not.**

When the power goes, the screen stays on and the internet does not. Every cloud assistant on that
laptop becomes a spinning wheel at the exact moment the work is urgent. A model that lives in the
laptop's own RAM keeps answering for as long as the battery lasts. This is the single strongest
argument for on-device inference in this market, and it costs nothing to verify — it happens
several times a month.

### The connection, when the power is on

Mobile coverage is not the bottleneck: **4G reaches 93,7 % of the population**, yet roughly
**60 % of Ivorians were still offline in 2024** [6]. Coverage without use is a device and
affordability problem, not a network problem — which means solutions that assume a permanent
broadband session exclude most of the country by construction.

### The documents

A signed supplier contract, a payroll file, a client list. Sending these to a foreign provider is
a decision an Ivorian SME is rarely in a position to take — sometimes by regulation, more often by
plain prudence, and almost always without a legal department to advise on it. **Local inference
turns that decision into a non-question:** the file never leaves the disk it is already on.

---

## 3. What the model does there, concretely

The two prompts in `metadata.json` are not illustrations chosen to flatter the model. They are the
job:

- **`tp_001`** — a supplier delivered 25 days late on a 4 500 000 FCFA order; the contract says
  2 % per *week begun*, capped at 10 %. Compute the penalty, state the cap, and **quote the clause
  you relied on.** This is a real argument between a buyer and a supplier, and the citation matters
  more than the arithmetic: it is what makes the answer usable in a negotiation.
- **`tp_002`** — turn an internal note into three bullet points for a management committee, then
  **list what the note does not say** that a decision-maker would need. Naming the missing
  information is the part a spreadsheet cannot do.

Both are in FCFA, both are in the register of West African business French, and both are answerable
with the company's own documents and no network.

---

## 4. Reach without a data plan: USSD

An offline laptop serves the office. It does not serve the delivery driver, the warehouse keeper,
or the field agent — and those are the people who generate the events the office needs to know
about.

The channel that already reaches them is **USSD**: the `*123#` short codes that work on any
handset, with no app, no data plan, and no browser. This is not a hypothesis about what West
Africans might adopt. It is what the region's financial system already runs on:

- **more than 22 million active mobile-money accounts in Côte d'Ivoire** in 2024 [7];
- **11 billion transactions across the UEMOA** the same year, worth **160 415 billion FCFA** [8].

Every one of those interactions is a menu on a phone screen. USSD is, in practice, the most widely
used human-computer interface in the country — and it is text-only, session-based, and capped at
182 characters per screen, which happens to be a shape a small language model handles well.

In our architecture the laptop holds the model and the documents; the USSD gateway is a thin front
door onto the same core, so a driver can report a delivery or query an order status from a handset
with no credit for data. The model does not change; only the surface does.

---

## 5. What the measurements say about robustness here

Offline changes what a failure costs. Online, a bad answer is followed by a retry, a second
opinion, a search. Offline, on a laptop in a warehouse, **the model's answer is the only answer**.
Robustness under unexpected input is therefore a use-case requirement, not a polish item.

We found a hard failure mode and measured it rather than assuming it away: on inputs outside its
competence, the model does not decline — it **loops**, repeating one phrase until it exhausts the
token budget. The default configuration of the official evaluation chain applies **no repetition
penalty at all** (`repeat_penalty = 1.0`), so this is exactly what a grader would see.
`bench/copies/penalite-repetition.md` records the full sweep, the fix, and — importantly — the
cost of the fix on multi-step reasoning. See `bench/resultats.md` for the decision.

---

## 6. What we do not claim

A claim that survives an audit is worth more than a claim that reads well.

- **We do not claim the model speaks any Ivorian language.** We tested it. Asked to identify
  Dioula, it answered "the language of Cameroon"; asked to identify Wolof, "the language of Tigré,
  an official language of the Republic of Tigré in southern Rwanda"; asked to translate, it looped.
  Asked directly, it answered honestly: *"Non, je ne maîtrise ni le dioula (jula) ni le wolof."*
  The probe is `bench/sonder_langues.py`, the transcript is `bench/copies/sonde-langues.md`, and
  the consequence is recorded in git: `dyu` was **removed** from `language_scope`. The working
  languages are French and English, which is what the target office actually writes in.
- **We do not claim mobile data is unaffordable in Côte d'Ivoire.** By the ITU's benchmark — the
  cheapest 2 GB plan costing 2 % or less of monthly GNI per capita — Côte d'Ivoire is one of only
  three West African countries that **meet** the affordability threshold [9]. Our argument is
  availability and confidentiality, not price per gigabyte.
- **We do not claim feature phones dominate.** Ivorian national statistics report **89 % of
  households using a smartphone** [10]. USSD is in this design because it needs no data session
  and no app — not because handsets are primitive.
- **We do not claim the model is a lawyer or an accountant.** It reads documents, computes, cites,
  and flags what is missing. Our own measurements show where it still fails — notably rounding to
  a *week begun*, which it gets wrong at every configuration we tested.

---

## Sources

1. Africa24 / ANSTAT — *Côte d'Ivoire : 98 % du secteur privé dominé par les PME*, and the 2024
   *Répertoire national des entreprises de Côte d'Ivoire* (ANSTAT):
   <https://africa24tv.com/cote-divoire-98-du-secteur-prive-domine-par-les-pme/> ·
   <https://www.anstat.ci/assets/publications/files/File_val_indicateur1746807354.pdf>
2. World Bank, *Firms experiencing electrical outages (% of firms)*, Côte d'Ivoire — **80,35 %
   (2023)**, Enterprise Surveys:
   <https://data.worldbank.org/indicator/IC.ELC.OUTG.ZS>
3. World Bank, *Value lost due to electrical outages (% of sales for affected firms)*, Côte
   d'Ivoire — **2 % (2023)**:
   <https://data.worldbank.org/indicator/IC.FRM.OUTG.ZS>
4. Africa24 — *Côte d'Ivoire : 32 milliards FCFA pour stabiliser le réseau électrique* (1 April
   2026): <https://africa24tv.com/cote-divoire-32-milliards-fcfa-pour-stabiliser-le-reseau-le-electrique/>
5. Jeune Afrique — *Électricité : la croissance d'Abidjan met le réseau ivoirien sous tension*:
   <https://www.jeuneafrique.com/1783185/economie-entreprises/electricite-la-croissance-dabidjan-met-le-reseau-ivoirien-sous-tension/>
6. Ecofin Agency — *Côte d'Ivoire targets rural smartphone adoption to narrow digital divide*
   (4G coverage 93,7 %; ~60 % of the population offline in 2024):
   <https://www.ecofinagency.com/news-digital/1806-56575-cote-divoire-targets-rural-smartphone-adoption-to-narrow-digital-divide>
7. 7info — *Monnaie électronique : la Côte d'Ivoire deuxième pays utilisateur de l'UEMOA en 2024*:
   <https://www.7info.ci/monnaie-electronique-la-cote-divoire-2e-pays-utilisateur-en-2024-dans-luemoa/>
8. BCEAO — *Rapport annuel sur les services financiers numériques dans l'UEMOA, 2024*:
   <https://www.bceao.int/fr/publications/rapport-annuel-sur-les-services-financiers-numeriques-dans-luemoa-2024>
9. ITU / Alliance for Affordable Internet affordability threshold, via Agence Ecofin's ranking of
   African countries by mobile-broadband cost:
   <https://www.agenceecofin.com/mobile/0705-65908-classement-des-pays-africains-par-cout-du-gb-en-haut-debit-mobile>
10. Institut National de la Statistique (INS), household survey — 89 % of households use a
    smartphone: <https://afriksoir.net/cote-divoire-menages-smartphones-enquetes-ins/>
