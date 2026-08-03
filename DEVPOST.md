# Devpost — ce qu'il faut coller, champ par champ

*Document de travail. La page Devpost est publique, ce texte le sera donc aussi.
Chaque chiffre cité vient de `bench/resultats.md` ou du profileur officiel.*

---

## Étape 3 — Project details

### `About the project` *(obligatoire, Markdown)*

```markdown
## Inspiration

A laptop has a battery. A fibre box does not. In Côte d'Ivoire, 80.4% of firms
report power cuts, and the cloud assistant goes down at exactly the moment the
work becomes urgent — a quote to send, a contract clause to check, a report due.

There is a second reason, and it is the one companies say out loud: supplier
contracts, payroll and client files cannot be sent to a cloud provider at all.
Not for cost, for confidentiality. An assistant that requires uploading those
documents is not a cheaper option. It is not an option.

So we built for the machine those companies already own: 8 GB of RAM,
integrated graphics, no network.

## What it does

Baarali Edge is an offline enterprise assistant for the `corporate_enterprise`
domain — knowledge-work productivity for small and medium businesses:
summarising, drafting and analysing a company's own documents, on the machine,
in French and English, with no network at any point.

The same reasoning core is reachable over **USSD** from a feature phone, at the
real 182-character screen limit, with no data plan and no app.

## How we built it

By measuring, not by choosing. Every decision below was made with the official
`adtc-profiler` on an 8 GB laptop, CPU only (`-ngl 0`), median of three runs.

- **Base model.** Five open models profiled, from 0.75 B to 4.21 B measured
  parameters. Qwen3.5-2B won on total score, not on accuracy.
- **Quantisation.** All seven quantisations of the winner, profiled end to end.
  IQ4_XS won: **31.20 tokens/s, 1 544 MB peak RSS** against the contest's 7 GB
  ceiling, giving **S_eff 77.9**, and 0.67 on 200 `arc_easy` questions.
- **Sampling.** `repeat_penalty = 1.05`, because llama.cpp applies none by
  default and this model loops on inputs outside its competence.
- **Verification.** Offline proven twice: no non-local socket across 15 samples
  during profiling, and a full inference with the Wi-Fi physically off. The
  weights are fetched by `download_model.sh` with a SHA-256 check.

## Challenges we ran into

**We published a decision, then had to reverse it.** An 18-item arithmetic
control pointed at `repeat_penalty = 1.10`. It was rigorous, documented — and
off-topic, because our domain is *summarisation, drafting and analysis*, not
arithmetic. So we built a second control on the official domain definition: 15
tasks, French and English, scored without human judgement, with a detector for
invented numbers. It showed that at 1.10 the model answers our own published
test prompt by **fabricating a formula**. We reversed to 1.05 and wrote down why.
A measured number is only worth as much as the question you asked it.

**The hidden validation set is not distributed to participants.** The profiler
source says the judges hold it. There is nothing to train against, so the only
defence against the two hidden prompts is breadth — which is what those 15 tasks
are for.

## Accomplishments that we're proud of

Not a score — a discipline. **No number enters our report unless it comes out of
a measurement**, and the report contains the ones that do not flatter us: the
quantisation that beats ours on accuracy is in the table, with the arithmetic
showing why it still loses. The 4 B model that is 6 accuracy points better is
there too, with the reason it loses on total score.

We also removed a claim rather than defend it. We had declared Dioula in our
language scope. We probed it: the model answered that Dioula is "the language of
Cameroon". We deleted `dyu` from the submission.

## What we learned

That half of this contest is won by *not* being big. Throughput and memory carry
50% of the score, throughput is graded relative to the fastest submission, and
the accuracy a larger model buys is rarely worth what it costs in both.

And that documentation is scored, not decorative — it sits inside the 50%.

## What's next

One lever identified and not pulled: the importance matrix. Our file is already
an imatrix quantisation, but the calibration is inherited — generic English, 80
chunks, computed by someone else. Recalibrating it on francophone enterprise
text would protect the weights that matter for our actual workload at identical
size, speed and memory. We have the instrument to judge the result; we did not
have the compute in time. We say so rather than imply otherwise.
```

### `Built with` *(obligatoire, max 25 étiquettes)*

```
llama.cpp, gguf, qwen3.5, quantization, imatrix, iq4-xs, cpu-inference,
offline-first, on-device-ai, edge-ai, python, llama-cpp-python,
lm-evaluation-harness, ussd, hugging-face, bash
```

### `"Try it out" links`

```
https://github.com/benewende-dev/baarali-edge
https://huggingface.co/Benewende-dev/baarali-edge-2b
```

**Deux liens, pas un.** Le dépôt contient la méthode ; les poids sont sur
Hugging Face et c'est ce que le jury exécute. Et **sans le suffixe `.git`** :
c'est l'URL de clonage, elle ne fait que rediriger (301 vérifié) vers la page.

### `Image gallery`

Quatre captures prêtes, tirées de la vidéo, au format 3:2 recommandé, bien sous
les 5 Mo :

| Fichier | Ce qu'elle montre |
|---|---|
| `demo/captures/01.png` | le `ping` sans réponse — le hors-ligne, vérifié |
| `demo/captures/02.png` | le modèle qui répond à `tp_002`, en cours de génération |
| `demo/captures/03.png` | la session USSD complète, au compteur de caractères |
| `demo/captures/04.png` | les fichiers locaux et les chiffres du profileur |

### `Video demo link` *(obligatoire)*

⚠️ **Devpost ne prend pas le fichier : il veut une URL** YouTube, Vimeo,
Facebook Video ou Youku. Il faut donc téléverser d'abord.

La vidéo est montée : **`demo/video-soumission.mp4`**, 87 s, 2880×1800, 7,8 Mo,
voix off comprise (méthode dans `demo/NARRATION.md`).

1. Téléverser sur YouTube. **Non répertoriée** — pas *privée* : une vidéo privée
   est invisible pour le jury.
2. Titre suggéré : `Baarali Edge — offline enterprise assistant on an 8 GB laptop`.
3. Coller l'URL ici.

---

## Étape 4 — Additional info

| Champ | Valeur |
|---|---|
| `Project Report Public URL on Github` | `https://github.com/benewende-dev/baarali-edge/blob/main/REPORT.md` |
| `Problem Domain` | `corporate_enterprise` |
| `Self Reported Sperf` | `20.8` |
| `Self Reported Seff` | `77.9` |
| `Test Prompt 1` | copier **à l'identique** depuis `metadata.json` → `test_prompts[0].prompt` |
| `Test Prompt 2` | copier **à l'identique** depuis `metadata.json` → `test_prompts[1].prompt` |

⚠️ Les deux prompts sont saisis deux fois — ici et dans `metadata.json`. Au
caractère près, sans quoi l'audit compare deux choses différentes. Les extraire
proprement plutôt que les retaper :

```bash
python3 -c "import json;[print(p['prompt'],end='\n\n---\n\n') for p in json.load(open('metadata.json'))['test_prompts']]"
```
