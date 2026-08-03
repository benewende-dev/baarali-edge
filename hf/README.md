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
base models, from 0.75 B to 4.21 B measured parameters, were profiled; then **all seven**
quantisations of the winner. Full tables:
[`bench/resultats.md`](https://github.com/benewende-dev/baarali-edge/blob/main/bench/resultats.md).

Measured on an Apple M1 / 8 GB, CPU only (`-ngl 0`, enforced by the profiler). Throughput and peak
memory are the **median of three runs** — a single memory reading is worthless, and we have the
scar to prove it: one variant showed 1.47 GB on its first pass and 2.21 GB as its true median.
Accuracy is a **single deterministic run** (temperature 0, fixed seed, 200 `arc_easy` questions);
repeating it would return the same number. Absolute values differ from the reference i5 laptop; the
ranking between candidates does not.

| Quantisation | Accuracy | Throughput | Peak RAM | S_eff | Total @150 t/s |
|---|---|---|---|---|---|
| **IQ4_XS** *(shipped)* | 0.670 | **34.3 t/s** | **1.74 GB** | **75.2** | **55.4** |
| Q4_K_M | 0.675 | 31.6 t/s | 2.08 GB | 70.2 | 54.1 |
| UD-Q5_K_XL | **0.680** | 29.0 t/s | 2.11 GB | 69.8 | 53.8 |
| MTP-Q4_K_M | 0.675 | 31.1 t/s | 2.20 GB | 68.5 | 53.7 |
| Q5_K_M | 0.670 | 26.7 t/s | 2.01 GB | 71.3 | 53.1 |
| UD-Q4_K_XL | 0.650 | 29.4 t/s | 2.21 GB | 68.4 | 52.1 |
| Q3_K_M | 0.630 | 30.7 t/s | 1.93 GB | 72.4 | 52.1 |

The last column is not a measurement: it is the official scoring function
`0.50·accuracy + 0.30·S_perf + 0.20·S_eff` applied to the measured cells, under the assumption that
the fastest submission in the contest reaches 150 t/s. `S_perf` is scored relative to that
submission, so the assumption has to be stated rather than hidden.

**The variant that beats us is in the table on purpose.** UD-Q5_K_XL scores 0.680 against our
0.670 — the best accuracy of the seven. It still loses overall, and the arithmetic says by how
much: that extra point of accuracy is worth **0.5** of final score, while the 18 % throughput and
5.4 S_eff it gives up cost it **2.1** — a net 1.6 in our favour, which is exactly the 55.4 against
53.8 in the table. That is the whole argument for this track in one row, and hiding the row would
have made the argument weaker, not stronger.

IQ4_XS is also the fastest and the lightest, and its three runs sat within 1.72–1.77 GB — the
narrowest spread we recorded, which matters because it is the figure that has to survive an
independent re-measurement.

### The shipped file, measured as a package

The table above ranks candidates. The number that describes **this file as it is submitted** —
fetched by `download_model.sh`, three profiler runs, median — is **31.20 t/s and 1 544 MB peak**.
It is lower than the 34.3 t/s above and that is not a contradiction to explain away: it is
run-to-run and thermal variance on a fanless 8 GB laptop, measured weeks apart. The ranking table
is used only to **compare** variants measured back to back; the packaged figure is the one we
self-report.

## Recommended inference settings

```bash
llama-cli -m Qwen3.5-2B-IQ4_XS.gguf -ngl 0 --temp 0 --repeat-penalty 1.05
```

`--repeat-penalty 1.05` is not a preference. On inputs outside its competence this model does not
decline — it repeats one phrase until the token budget runs out, and llama.cpp applies **no
repetition penalty by default**.

The value was measured twice, and the second measurement overturned the first. An arithmetic
control of 18 items pointed at 1.10. A second control of 15 summarisation, drafting and analysis
tasks — the genre this model is actually for — showed what that had cost. On a contract-penalty
question, 1.00 and 1.05 both produce **270,000 FCFA**, a defensible amount; 1.10 produces
**63,450 FCFA** by inventing a formula, `(30 − 25) / 7`, that corresponds to nothing in the
contract. Reproducible at temperature 0.

To be precise about what "defensible" means here, because it is not the same as right: 270,000
follows if the ten-day threshold is read as a grace period, leaving 15 days — three weeks begun —
at 2 % each. The model does not reason that way. It divides 25 by 7, gets "3 weeks and 4 days", and
calls that three weeks begun, which rounds a begun week *down*. It reaches a defensible number by
an indefensible route. That rounding failure is listed under limitations below and it is not fixed
by any penalty value.

1.05 keeps the model on that route rather than the fabricated one, still removes the degeneration
(diversity 0.60 → 0.99 on the case that showed it), and costs one criterion out of 81 against no
penalty at all. Above 1.10 the collapse is not subtle: multi-step reasoning falls from 9/12 to 4/12
at 1.15.

Sweeps and full transcripts:
[`bench/copies/redaction.md`](https://github.com/benewende-dev/baarali-edge/blob/main/bench/copies/redaction.md),
[`bench/copies/penalite-repetition.md`](https://github.com/benewende-dev/baarali-edge/blob/main/bench/copies/penalite-repetition.md).

## Known limitations, measured

- **No African-language capability.** Probed and documented: asked to identify Dioula it answered
  "the language of Cameroon"; asked for Wolof, "the language of Tigré". `dyu` was consequently
  removed from the submission's `language_scope`. Working languages are French and English.
- **Rounding to a *week begun*** — a common clause in West African supply contracts — is wrong at
  every configuration we tested. It rounds down: 25 days becomes "three weeks begun".
- **It drops a fact to make room for a comment.** Told to summarise a clinic report in exactly
  three bullets, it sacrificed the 71 % bed-occupancy figure to write "requires immediate
  intervention". Summarising a client thread, it never quoted the order reference.
- **It ranks urgency badly.** Asked to order four tasks, it placed a public tender closing in three
  days last, as "low urgency" — it had restated the order of the question with justifications
  attached.
- **It confuses accounting definitions**, computing gross margin as revenue minus fixed costs.
- **It can derive numbers confidently and wrongly.** Analysing a purchasing proposal, it divided an
  annual spend by 1.08 to "recover" a pre-saving baseline, then built two further figures on that
  false start.

None of these depend on sampling settings; they are in the base model. The last four were found by
[`bench/redaction.py`](https://github.com/benewende-dev/baarali-edge/blob/main/bench/redaction.py),
a 15-task control scored without human judgement.

**2 B parameters is a deliberate trade, not a limitation we are apologising for.** Half of the
score is throughput and memory. Measured on the same machine at the Q4_K_M stage, Qwen3.5-4B is
6 accuracy points better — 0.735 against 0.675 — and still loses on total score, 52.6 against
56.5 in the same 150 t/s scenario, because it runs at 44 % of the speed and takes 1.4× the memory.

## Licence

Apache 2.0, inherited from Qwen3.5-2B. The submission repository is GPL v3, inherited from the
official ADTC template; the weights keep their own licence.
