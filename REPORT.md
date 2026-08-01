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

TODO — the claim behind `african_alpha_claim: true`: francophone enterprise documents, Dioula
language support (kept only if measured to cost less accuracy than the bonus it earns), and
reachability from a feature phone over USSD, with no data plan.
