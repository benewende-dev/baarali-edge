# Technical Report — Baarali Edge: an offline enterprise assistant for 8 GB laptops

**Team ID:** baarali-edge
**Domain:** corporate_enterprise
**Model:** baarali-edge-2b — Qwen3.5-2B, GGUF IQ4_XS, 1.88 B parameters, llama.cpp, CPU only

> Every number in this report is measured with the official `adtc-profiler` on the machine named
> below. No figure is estimated or copied from a model card.

---

## Problem

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

The detail that settles the architecture is smaller than any statistic: **the laptop has a
battery, the fibre box does not.** When the grid fails, a cloud assistant becomes a spinning wheel
at precisely the moment the work is urgent, while a model living in the laptop's own RAM keeps
answering. In the 2023 World Bank Enterprise Survey, 80.4 % of Ivorian firms reported electrical
outages, and affected firms put the loss at 2 % of annual sales. This is not a problem being
solved away: in February 2026 national demand rose 14 % year on year, and on 1 April 2026 the
government released 32 billion FCFA as an emergency measure.

Reach beyond the office is the second half of the problem. Coverage is not the bottleneck — 4G
reaches 93.7 % of the population — but roughly 60 % of Ivorians were still offline in 2024, and a
storekeeper checking an order does not open a laptop. The channel that already reaches them is
**USSD**: the short codes that carry more than 22 million active mobile-money accounts in Côte
d'Ivoire, on any handset, with no app and no data session. A working implementation against the
real aggregator contract, including the 182-character screen limit, is in [`demo/`](demo/) — with
an explicit statement of what it does not have, namely a live short code, which requires an
operator agreement.

Sources for every figure above, and a section stating what this submission does **not** claim, are
in [`USE_CASE.md`](USE_CASE.md).

---

## Design Decisions

Every choice below was made from a measurement, and each is reversible by re-running the script
named beside it. The full log, including the reasoning we later had to withdraw, is
[`bench/resultats.md`](bench/resultats.md).

### 1. Base model — Qwen3.5-2B, from five candidates profiled, not from reputation

Five open models between 0.75 B and 4.21 B measured parameters, all at GGUF Q4_K_M, same machine,
same profiler (`bench/mesurer.py`):

| Candidate | Parameters | Accuracy (`arc_easy`, 200 q) | Throughput | Peak RAM | S_eff |
|---|---|---|---|---|---|
| Phi-4-mini | 3.84 B | **0.765** | 20.6 t/s | 3.30 GB | 52.8 |
| Qwen3.5-4B | 4.21 B | 0.735 | 14.9 t/s | 3.49 GB | 50.1 |
| SmolLM3-3B | 3.08 B | 0.720 | 25.5 t/s | 3.02 GB | 56.9 |
| **Qwen3.5-2B** | **1.88 B** | 0.675 | 33.9 t/s | 2.52 GB | 64.1 |
| Qwen3.5-0.8B | 0.75 B | 0.640 | **65.3 t/s** | **1.21 GB** | **82.7** |

The most accurate model is not the best submission, because `S_perf` is scored **relative to the
fastest entry received**, not against a fixed bar. We do not control that denominator. Applying the
official function under three assumptions about it:

| If the fastest entry runs at… | 0.8 B | **2 B** | SmolLM3-3B | Phi-4-mini | 4 B |
|---|---|---|---|---|---|
| 65 t/s | **68.8** | 65.3 | 54.9 | 49.2 | 56.5 |
| 150 t/s | 51.9 | **56.5** | 48.2 | 43.8 | 52.6 |
| 319 t/s | 44.9 | **52.9** | 45.5 | 41.6 | 51.1 |

319 t/s is not a hypothesis: the 135 M-parameter example model shipped by the organisers reaches it
on this machine. Qwen3.5-2B wins two scenarios of three and is never poor in the third. The 0.8 B
wins only if nobody among the entrants submits a fast model — a bet on other people's choices
rather than on our own work.

The multiple-choice benchmark also misses what a judge will see, so all five candidates answered
our two real prompts (`bench/repondre.py`, transcripts in `bench/copies/`). Only the two Qwen
models retained all four facts of `tp_002`; the other three omitted the unsigned supplier contract
from their summary **and then requested it as missing information**, which the note had supplied.

### 2. Parameter count — 2 B is the trade, stated as arithmetic

Half the score is throughput and memory. Qwen3.5-4B is 6 accuracy points better than our choice —
0.735 against 0.675 — and still loses on total score, 52.6 against 56.5 in the middle scenario,
because it runs at 44 % of the speed and takes 1.4× the memory. Accuracy has to buy a great deal
before it pays for that, and at this scale it does not.

Peak memory is 1 544 MB against a 7 GB ceiling. We are not near the disqualification line, so the
model size was chosen on score, never out of fear of an overrun.

### 3. Quantisation — IQ4_XS, from all seven variants of the winner

| Variant | Accuracy | Throughput | Peak RAM | S_eff | Total @150 t/s |
|---|---|---|---|---|---|
| **IQ4_XS** *(shipped)* | 0.670 | **34.3 t/s** | **1.74 GB** | **75.2** | **55.4** |
| Q4_K_M | 0.675 | 31.6 t/s | 2.08 GB | 70.2 | 54.1 |
| UD-Q5_K_XL | **0.680** | 29.0 t/s | 2.11 GB | 69.8 | 53.8 |
| MTP-Q4_K_M | 0.675 | 31.1 t/s | 2.20 GB | 68.5 | 53.7 |
| Q5_K_M | 0.670 | 26.7 t/s | 2.01 GB | 71.3 | 53.1 |
| UD-Q4_K_XL | 0.650 | 29.4 t/s | 2.21 GB | 68.4 | 52.1 |
| Q3_K_M | 0.630 | 30.7 t/s | 1.93 GB | 72.4 | 52.1 |

Accuracy here is a single deterministic run (temperature 0, fixed seed); throughput and memory are
medians of three, because one variant read 1.47 GB on its first pass against a true median of
2.21 GB — a single memory sample would have chosen the wrong model.

**UD-Q5_K_XL is the variant that beats us on accuracy**, 0.680 to 0.670, and it is in this table
for that reason. It loses by 1.6 points overall: its extra accuracy point is worth 0.5 of final
score, while the 18 % throughput and 5.4 S_eff it gives up cost 2.1. Three further assumptions
also failed the measurement — Q5 bought no accuracy at all over IQ4_XS for 25 % more weight;
"dynamic" UD-Q4_K_XL came out *below* ordinary Q4_K_M at 0.650; and multi-token prediction
accelerated nothing, because the profiler drives `llama-bench` without the settings that would use
it, so the extra head is pure weight.

### 4. Importance-matrix calibration — inherited, not ours, and we say so

The shipped file is an importance-matrix quantisation. Read from its own metadata:

```
quantize.imatrix.file      Qwen3.5-2B-GGUF/imatrix_unsloth.gguf
quantize.imatrix.dataset   unsloth_calibration_Qwen3.5-2B.txt
quantize.imatrix.entries_count  186
quantize.imatrix.chunks_count   80
```

That calibration set is Unsloth's, and it is **generic English**. Recalibrating it on francophone
enterprise text — the register this submission is actually for — was the one lever we had
identified and not pulled. **We have now pulled it, and it does not move.**

A 176 kB calibration corpus of enterprise documents, 55 % French, was built
([`imatrix/corpus.py`](imatrix/corpus.py), fixed seed, fully reproducible), its length chosen by
measuring 4-gram diversity at three sizes rather than by preference, and checked against every
question that would judge it: [`imatrix/contamination.py`](imatrix/contamination.py) found an
eight-word overlap between one template and one of our own control tasks — written by the same
hand, in the same register — which was rewritten before anything was computed. A corpus containing
its own exam marks its own paper.

The result had to be compared against the right thing. Our first rebuild came out **23 MB heavier**
than the shipped file, and a tensor-by-tensor check showed why: not the calibration, but the type
map. So we rebuilt twice more — a control with the *inherited* calibration and the default map, and
a candidate replaying the shipped file's map exactly
([`imatrix/types-unsloth.txt`](imatrix/types-unsloth.txt)). The latter lands **32 bytes** from the
shipped file, with an identical peak RSS across three runs, which makes any remaining difference
attributable to calibration alone.

It is not measurable. Throughput and memory: unchanged, the gap smaller than the spread between
three runs of the same file. Accuracy: 0.670 against 0.680 on 200 `arc_easy` questions — and since
two totals four questions apart prove nothing, we compared them **question by question**
([`bench/apparie.py`](bench/apparie.py), McNemar):

```
identical answers   196/200  (98 %)
shipped only right    1
recalibrated only     3        p = 0.625
```

**Four questions out of two hundred separate the two files.** We kept the shipped weights. What
this step produces is not a better model but an answer to a question our own report had left open,
and the answer is negative — obtained with the control, the contamination check and the paired test
that were needed for it to be worth anything. Full protocol and figures:
[`bench/resultats.md`](bench/resultats.md), step 6.

What this does **not** show is that importance-matrix calibration is pointless in general. One
corpus, one model, one format, 200 questions. A format more aggressive than IQ4_XS — where fewer
bits remain to allocate, so more is at stake in allocating them well — could well behave otherwise.

### 5. Sampling — `repeat_penalty = 1.05`, and how we got it wrong first

On input outside its competence the model does not decline, it loops — one phrase repeated until
the token budget is exhausted — and the official chain applies no repetition penalty by default
(`accuracy.py` calls `create_completion(temperature=0.0)`; `llama-cpp-python` defaults to
`repeat_penalty = 1.0`). So the loops we observed are exactly what a grader would see.

An 18-item arithmetic control settled on 1.10. That control was rigorous and off-topic: this domain
is summarising, drafting and analysis, not arithmetic. Re-measured on a control built for the right
genre, 1.00, 1.05 and 1.10 are indistinguishable (91 / 90 / 91 %) — but at 1.10 the model answers
our own published `tp_001` with 63,450 FCFA, from a formula `(30 − 25) / 7` that corresponds to
nothing in the contract. 1.05 keeps it on the defensible route, removes the in-domain degeneration
we found (diversity 0.60 → 0.99), and costs one criterion out of 81.

The wrong conclusion is kept in the log with the reasoning that produced it, because a decision
process that only records its successes cannot be audited.

### 6. Alternatives considered and rejected, each for a measured reason

| Rejected | Measured reason |
|---|---|
| Phi-4-mini | Dominated by SmolLM3-3B on both axes — slower (20.6 vs 25.5 t/s) *and* heavier (3.30 vs 3.02 GB). On `tp_001` it read "15 days × 2 % = 30 %", confusing days with weeks. |
| SmolLM3-3B | A reasoning model: it thinks in English inside a `<think>` block and never concludes. With `/no_think` it finally answers, but prorates 3.57 weeks instead of rounding up, which the clause forbids. |
| Qwen3.5-4B | The best legal reading of the contract of the five, and still 3.9 points behind on total score at 150 t/s. Accuracy did not pay for 44 % of the speed. |
| Qwen3.5-0.8B | Wins only in the scenario where no competitor submits a fast model. Choosing it means betting on 1,340 other entrants' choices. |
| Q3_K_M | The accuracy floor: 0.630, with no compensating gain elsewhere. |
| Ivorian-language support | Probed and refuted. Asked to identify Dioula it answered "the language of Cameroon"; asked for Wolof, "the language of Tigré". `dyu` was **removed** from `language_scope` rather than left in as an unbacked claim. |
| Fine-tuning the base model | Out of reach on the hardware available, and it would have consumed the time that went into measurement instead. We would rather be able to defend every number than own a model we could not evaluate. |

---

## Constraints

- Target: 8 GB RAM, integrated graphics, Ubuntu 22.04, no discrete GPU.
- Pure CPU inference through llama.cpp (`-ngl 0`); 7 GB peak memory budget.
- No network of any kind at inference time.
- Development constraint, worth stating: this submission was itself built on an 8 GB machine.
  The memory ceiling was not a specification to read — it was a daily condition.

---

## Benchmarks

Measured with the official `adtc-profiler` on the **packaged submission** — the same file
`download_model.sh` fetches, at the path `_runtime.model_path` declares. Three runs, **median**
reported; the raw JSON of each is in [`bench/raw/final-iq4xs-{1,2,3}.json`](bench/raw/).

| Metric | Value (median of 3) | Individual runs |
|---|---|---|
| Machine | Apple M1, 8 GB, integrated graphics, macOS | — |
| Peak RSS | **1 544 MB** | 1 615 / 1 544 / 1 526 |
| Generation speed | **31.20 tok/s** | 32.23 / 28.25 / 31.20 |
| Time to first token | 3 398 ms | 3 351 / 4 643 / 3 398 |
| CPU p99 | 97.3 % | 97.5 / 97.3 / 87.0 |
| Thermal throttling | **none** | no core-temp sensor exposed on this machine |
| Accuracy (`arc_easy`) | 0.68 acc_norm, 50 samples | 0.670 at 200 samples (étape 2) |
| Parameter count | 1 881 825 088 — profiler reports `params_match: true` | — |

**Self-reported S_eff = 77.9** — `100 × (7000 − 1544) ÷ 7000`. Computed against 7 **decimal** GB
rather than 7 GiB, which is the more conservative of the two readings (7 GiB would give 78.5). An
understated claim cannot be contradicted by the audit.

**S_perf is deliberately not self-reported as a score.** The rule computes it relative to the
fastest submission received, a denominator we do not have. The measured figure is 31.20 tok/s.

Two honest notes on these numbers:

- The measuring machine is an Apple M1, not the reference i5. The profiler enforces `-ngl 0`, so
  this is CPU-only inference in both cases, but the absolute values will differ on the evaluation
  hardware. What transfers is the **relative** ranking that produced every design decision here.
- Étape 2 recorded 34.3 tok/s and 1.74 GB for this same file. The spread between that and 31.20 /
  1.54 is run-to-run and thermal variance on a fanless 8 GB laptop — which is precisely why every
  figure in this table is a median of three, and why the étape 2 table is used only to **rank**
  candidates measured back to back, never as an absolute claim.

---

## Domain fit — measured against what this track actually asks

`arc_easy` is an English general-knowledge quiz. It is what the profiler scores, and we report it
above, but it is not what this domain is. The official definition of `corporate_enterprise` is
*knowledge-work productivity: **summarization, drafting, and analysis** for small and medium
enterprises* — and half of `S_acc` is a judge reading answers, not a benchmark.

So we built a second control for that, [`bench/redaction.py`](bench/redaction.py): 15 tasks, five
per genre, French and English, spread across eight West and Central African cities plus tasks with
no location at all — a site-meeting record from Ouagadougou, an HR notice from Dakar, a client
email thread from Accra, a clinic report from Cotonou, a payment reminder from Abidjan, a job
advert for Bamako, a service notice from Lomé, a contract amendment from Douala, a quotation, a
contract excerpt, a dashboard, a priority call. Breadth is deliberate: the rules generate the two
hidden prompts specifically to detect overfitting, so a control tied to one city would measure the
very fault it is meant to guard against.

Scoring uses no human judgement. Each task carries its own checks — do the source facts survive
the summary, is the imposed register kept, is the bullet count and word limit respected, is the
answer in the language of the question, and above all **is any number invented**. A hand-written
ideal answer scores 100 % on all 15, so the ceiling is reachable and every gap below it belongs to
the model.

| | penalty 1.00 *(chain default)* | 1.05 *(shipped)* | 1.10 |
|---|---|---|---|
| Summarising, 5 tasks | 31/33 | 30/33 | 30/33 |
| Drafting, 5 tasks | 34/36 | 34/36 | 35/36 |
| Analysis, 5 tasks | 10/12 | 10/12 | 10/12 |
| **Mean per task** | **91 %** | **90 %** | **91 %** |
| **Invented numbers** | **0/10** | **0/10** | **0/10** |

Zero fabricated figures across 30 pieces of writing is the result we would most want to be true,
and it is the one we checked hardest: every number of three digits or more was matched against its
source text.

The check covers the 10 summarising and drafting tasks, where the set of legitimate figures is
closed. It is **not** applied to the 5 analysis tasks, where the model is expected to derive new
numbers — and we should say what that exclusion hides: on one of them it produced a confident but
wrong derivation, dividing an annual spend by 1.08 to "recover" a pre-saving baseline. Bad
arithmetic inside an analysis is a real failure mode; it is simply not one an automatic
source-matching check can separate from correct arithmetic.

What the control found that the benchmark could not:

- **It drops a fact to make room for a comment.** Held to exactly three bullets on a clinic
  report, it discarded the 71 % bed-occupancy figure in favour of "requires immediate
  intervention". Summarising a client thread, it never quoted the order reference.
- **It ranks urgency badly.** Given four tasks to order, it placed a public tender closing in
  three days last, labelled "low urgency", having essentially restated the order of the question.
- **It confuses accounting definitions**, computing gross margin as revenue minus fixed costs.

These are limits of the base model, not of the sampling settings, and they are stated here rather
than left for the audit to find. Full transcripts, criterion by criterion:
[`bench/copies/redaction.md`](bench/copies/redaction.md).

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
