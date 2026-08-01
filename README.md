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

For an SME in Abidjan, cloud AI fails on three counts at once: metered data makes every query a
cost, outages make it unavailable exactly when work is urgent, and sending contracts, payroll or
client files to a foreign provider is a confidentiality decision most organisations cannot make.
An assistant that lives on the laptop removes all three at the same time.

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
model/                Weights land here at download time — never committed
bench/                Our own measurement runs and the reasoning behind each choice
PLAN.md               Working plan (French)
```

---

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
