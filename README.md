# Baarali Edge — an offline enterprise assistant for the laptops West Africa actually owns

Submission to the **Africa Deep Tech Challenge 2026 — Laptop LLM track**, domain
`corporate_enterprise`.

A quantised language model that runs entirely on a commodity laptop — 8 GB of RAM, integrated
graphics, no network — and serves as the reasoning core of an offline assistant for small
companies and public bodies: read the organisation's own documents, answer with citations, keep
every byte on the machine.

> **Status: work in progress.** Numbers appear in this repository only once they have been
> measured with the official `adtc-profiler`. Nothing here is estimated.

---

## Why offline is the requirement, not a feature

In the 2023 World Bank Enterprise Survey, **80,4 % of Ivorian firms reported electrical outages**,
and affected firms put the loss at **2 % of annual sales**. The detail that decides the
architecture is simpler than any statistic: **the laptop has a battery, the fibre box does not.**
When the power goes, a cloud assistant becomes a spinning wheel at the exact moment the work is
urgent — while a model living in the laptop's own RAM keeps answering. Add to that the documents
that cannot leave the company, and on-device inference stops being a feature and becomes the
requirement.

The full argument, with sources and with an explicit list of what we **do not** claim, is in
[`USE_CASE.md`](USE_CASE.md).

---

## Target profile

The ADTC Standard Laptop — Intel Core i5 (10th–12th gen) or Ryzen 5, **8 GB DDR4**, integrated
graphics only, 256 GB SSD, Ubuntu 22.04. Representative price: $150–$250 refurbished.

Peak memory budget: **7 GB**. Runtime: **llama.cpp**, GGUF weights, CPU only (`-ngl 0`).

---

## Repository layout

```
metadata.json         Team, model and test-prompt metadata (ADTC format)
download_model.sh     Fetches the GGUF weights from a public URL
REPORT.md             Technical report: problem, design, constraints, benchmarks
USE_CASE.md           The African use case, sourced — and what we do not claim
model/                Weights land here at download time — never committed
bench/                Our own measurement runs and the reasoning behind each choice
PLAN.md               Working plan (French)
```

---

## Recommended inference settings

```
--repeat-penalty 1.10     (llama.cpp default is 1.0 — no penalty at all)
--temp 0
```

Not a preference: a measured fix. On inputs outside its competence the model degenerates into a
repeated phrase until the token budget runs out, and the default configuration of the evaluation
chain applies no repetition penalty. **1.10 is the smallest value that eliminates the failure on
every trigger we found, at zero measured cost** on an 18-item domain control (6/6 single-step and
9/12 multi-step, identical to no penalty). At 1.15 multi-step reasoning collapses to 4/12.

Full sweep and reasoning: [`bench/resultats.md`](bench/resultats.md) and
[`bench/copies/penalite-repetition.md`](bench/copies/penalite-repetition.md).

## Reproducing our measurements

```bash
brew install llama.cpp          # provides llama-bench, required by the profiler
pip install "git+https://github.com/Africa-Deep-Tech-Foundation/adtc-profiler.git"

bash download_model.sh
adtc-profiler run --submission . --mode participant --output submission.json
```

---

## Licence

GPL v3, inherited from the official ADTC 2026 submission template.
