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
--repeat-penalty 1.05     (llama.cpp default is 1.0 — no penalty at all)
--temp 0
```

Not a preference: a measured fix, and one we got wrong before we got it right. On inputs outside
its competence the model degenerates into a repeated phrase until the token budget runs out, and
the evaluation chain applies no repetition penalty by default. An 18-item arithmetic control
pointed at 1.10. A later control built to match this track's actual definition — *summarization,
drafting and analysis* — showed that at 1.10 the model answers our own published test prompt
`tp_001` with **63,450 FCFA instead of 270,000**, inventing a formula to get there. Reproducible
at temperature 0.

**1.05 is the only value that holds both ends**: `tp_001` stays correct with the contract clause
quoted verbatim, the in-domain degeneracy disappears (diversity 0.60 → 0.99 on the case that
showed it), and it costs **one criterion out of 81** against no penalty at all — nothing
measurable. Above 1.10, multi-step reasoning collapses outright: 9/12 → 4/12 at 1.15.

Full sweeps: [`bench/resultats.md`](bench/resultats.md),
[`bench/copies/redaction.md`](bench/copies/redaction.md) (15 writing tasks, 3 penalties) and
[`bench/copies/penalite-repetition.md`](bench/copies/penalite-repetition.md) (23 probes, 5 values).

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
