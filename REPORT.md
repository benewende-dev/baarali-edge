# Technical Report — Baarali Edge: an offline enterprise assistant for 8 GB laptops

**Team ID:** TODO
**Domain:** corporate_enterprise
**Model:** TODO

> Every number in this report is measured with the official `adtc-profiler` on the machine named
> below. No figure is estimated or copied from a model card.

---

## Problem

<!-- À remplir à l'étape 5. Matière déjà arrêtée : -->

Small and mid-sized organisations in West Africa — a 40-person distributor in Abidjan, a
municipal office, a clinic — hold the documents that would make an assistant genuinely useful:
supplier contracts, invoices, HR policies, meeting notes. Cloud assistants cannot serve them, for
three reasons that hold simultaneously:

- **Cost.** Data is metered. A per-query cost that is negligible in Europe is a line item here.
- **Availability.** Connectivity and grid power both fail, and they fail during working hours.
- **Confidentiality.** Sending a signed contract or a payroll file to a foreign provider is a
  decision most organisations are not in a position to take — sometimes by regulation, often by
  plain prudence.

An assistant that runs on the laptop answers all three at once. The target user is an office
worker with a refurbished i5 and 8 GB of RAM, working through an outage.

TODO — expand: field context, the USSD channel as the zero-data reach for non-smartphone users.

---

## Design Decisions

<!-- À remplir à l'étape 1 et 2, à partir de bench/resultats.md -->

- **Base model:** TODO — chosen from a measured comparison of N candidates, not by reputation.
- **Parameter range:** TODO — the scoring function assigns 50 % of the weight to throughput and
  memory, which favours a smaller model than intuition suggests. State the arithmetic.
- **Quantization:** TODO — Q4_K_M / Q5_K_M / IQ4_XS compared on measured total score.
- **Importance-matrix calibration:** TODO — calibrated on francophone enterprise text.
- **Alternatives considered and rejected:** TODO — with the measured reason for each rejection.

---

## Constraints

- Target: 8 GB RAM, integrated graphics, Ubuntu 22.04, no discrete GPU.
- Pure CPU inference through llama.cpp (`-ngl 0`); 7 GB peak memory budget.
- No network of any kind at inference time.
- Development constraint, worth stating: this submission was itself built on an 8 GB machine.
  The memory ceiling was not a specification to read — it was a daily condition.

---

## Benchmarks

<!-- Remplacer chaque TODO par la sortie de submission.json. Aucun chiffre à la main. -->

| Metric | Value |
|---|---|
| Machine | TODO |
| RAM at peak | TODO |
| Time to first token | TODO |
| Generation speed | TODO |
| Thermal throttling | TODO |
| Accuracy (lm-eval task, samples) | TODO |

These are self-reported development benchmarks. Official scores are measured by the ADTC
profiler on the standard evaluation machine.

---

## African use case

The claim behind `african_alpha_claim: true` is set out in full, with sources, in
**[`USE_CASE.md`](USE_CASE.md)**. In one paragraph:

80,4 % of Ivorian firms reported electrical outages in the 2023 World Bank Enterprise Survey, and
affected firms lose 2 % of annual sales to them. When the power fails, the laptop's battery keeps
the screen on and the fibre box goes dark — so a cloud assistant is unavailable precisely when the
work is urgent, while a model in the laptop's own RAM is not. Add the documents that cannot leave
the company (contracts, payroll, client lists), and on-device inference becomes the requirement
rather than the feature. Reach beyond the office is provided over **USSD**, the text-only channel
that already carries 22 million active mobile-money accounts in Côte d'Ivoire — no app, no data
plan, any handset.

`USE_CASE.md` also states what this submission **does not** claim: no Ivorian-language capability
(measured, and `dyu` was consequently removed from `language_scope`), no claim that mobile data is
unaffordable in Côte d'Ivoire (by the ITU threshold it is not), and no claim that feature phones
dominate the market (they do not).
