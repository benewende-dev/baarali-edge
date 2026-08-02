---
license: apache-2.0
base_model: Qwen/Qwen3.5-2B
tags:
  - gguf
  - llama.cpp
  - on-device
  - offline
  - cpu
  - africa
  - adtc-2026
language:
  - fr
  - en
pipeline_tag: text-generation
library_name: llama.cpp
---

# baarali-edge-2b

The weights for **[Baarali Edge](https://github.com/benewende-dev/baarali-edge)**, a submission to
the **Africa Deep Tech Challenge 2026 — Laptop LLM track**, domain `corporate_enterprise`.

An offline enterprise assistant for the laptops West Africa actually owns: 8 GB of RAM, integrated
graphics, no network. It reads a company's own documents — supplier contracts, invoices, HR
policies, meeting notes — and answers with citations, on the machine, in French and English.

## What this file is, exactly

This repository hosts **`Qwen3.5-2B-IQ4_XS.gguf`, an unmodified copy** of the IQ4_XS build
published by [unsloth/Qwen3.5-2B-GGUF](https://huggingface.co/unsloth/Qwen3.5-2B-GGUF), itself
quantised from [Qwen/Qwen3.5-2B](https://huggingface.co/Qwen/Qwen3.5-2B). Credit for the base model
goes to Qwen; credit for this quantisation goes to Unsloth. It is republished here so that the
submission's `download_model.sh` points at a URL under our control and keeps working unchanged
through the audit window — not because we claim authorship of the weights.

```
sha256  3639f34b5ca22aa1c51f3616566eae8c355111554f6924ad97ee2652ed11c1cd
size    1 172 996 352 bytes (1.09 GiB)
```

Our contribution is the **selection, measurement and packaging**: which base model, which
quantisation, which sampling settings, and the evidence for each. That evidence lives in the
GitHub repository, not in a claim on this page.

## Why this model, and why this quantisation

Both decisions were measured with the official `adtc-profiler`, never chosen by reputation. Five
base models between 0.8 B and 4.2 B parameters were profiled, then seven quantisations of the
winner. Full tables: [`bench/resultats.md`](https://github.com/benewende-dev/baarali-edge/blob/main/bench/resultats.md).

Measured on an Apple M1 / 8 GB, CPU only (`-ngl 0`, enforced by the profiler), median of three
runs. Absolute figures differ from the reference i5 laptop; the comparison between candidates does
not.

| Quantisation | Accuracy (`arc_easy`) | Throughput | Peak RAM |
|---|---|---|---|
| **IQ4_XS** *(shipped)* | 0.670 | **34.3 t/s** | **1.74 GB** |
| Q4_K_M | 0.675 | 31.6 t/s | 2.08 GB |
| Q5_K_M | 0.670 | 26.7 t/s | 2.01 GB |
| UD-Q4_K_XL | 0.650 | 29.4 t/s | 2.21 GB |
| Q3_K_M | 0.630 | 30.7 t/s | 1.93 GB |

IQ4_XS is the fastest *and* the lightest, with the tightest run-to-run spread (1.72–1.77 GB).
Paying for Q5 bought no accuracy at all — 0.670, identical, for 25 % more weight.

## Recommended inference settings

```bash
llama-cli -m Qwen3.5-2B-IQ4_XS.gguf -ngl 0 --temp 0 --repeat-penalty 1.05
```

`--repeat-penalty 1.05` is not a preference. On inputs outside its competence this model does not
decline — it repeats one phrase until the token budget runs out, and llama.cpp applies **no
repetition penalty by default**.

The value was measured twice, and the second measurement overturned the first. An arithmetic
control of 18 items pointed at 1.10. A second control of 15 summarisation, drafting and analysis
tasks — the genre this model is actually for — showed that 1.10 makes it answer a contract-penalty
question with **63,450 FCFA instead of 270,000**, inventing a formula to get there. Reproducible at
temperature 0.

1.05 keeps that answer correct, still removes the degeneration (diversity 0.60 → 0.99 on the case
that showed it), and costs one criterion out of 81 against no penalty at all. Above 1.10 the
collapse is not subtle: multi-step reasoning falls from 9/12 to 4/12 at 1.15.

Sweeps and full transcripts:
[`bench/copies/redaction.md`](https://github.com/benewende-dev/baarali-edge/blob/main/bench/copies/redaction.md),
[`bench/copies/penalite-repetition.md`](https://github.com/benewende-dev/baarali-edge/blob/main/bench/copies/penalite-repetition.md).

## Known limitations, measured

- **No African-language capability.** Probed and documented: asked to identify Dioula it answered
  "the language of Cameroon"; asked for Wolof, "the language of Tigré". `dyu` was consequently
  removed from the submission's `language_scope`. Working languages are French and English.
- **Rounding to a *week begun*** — a common clause in West African supply contracts — is wrong at
  every configuration we tested.
- **It drops a fact to make room for a comment.** Told to summarise a clinic report in exactly
  three bullets, it sacrificed the 71 % bed-occupancy figure to write "requires immediate
  intervention". Summarising a client thread, it never quoted the order reference.
- **It ranks urgency badly.** Asked to order four tasks, it placed a public tender closing in three
  days last, as "low urgency" — it had restated the order of the question with justifications
  attached.
- **It confuses accounting definitions**, computing gross margin as revenue minus fixed costs.

None of these depend on sampling settings; they are in the base model. All three were found by
[`bench/redaction.py`](https://github.com/benewende-dev/baarali-edge/blob/main/bench/redaction.py),
a 15-task control scored without human judgement.
- 2 B parameters is a deliberate trade. The scoring function puts 50 % of its weight on throughput
  and memory; a larger model would have to be ~22 accuracy points better to break even, and it is
  not.

## Licence

Apache 2.0, inherited from Qwen3.5-2B. The submission repository is GPL v3, inherited from the
official ADTC template; the weights keep their own licence.
