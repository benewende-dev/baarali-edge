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

Cinq images prêtes, au format 3:2 recommandé, bien sous les 5 Mo. **Téléverser
`00-carte.png` en premier** : Devpost fait de la première image la vignette du
projet, et l'acte 1 — un écran presque vide, c'est tout son propos — ferait une
mauvaise vignette.

| Fichier | Ce qu'elle montre |
|---|---|
| `demo/captures/00-carte.png` | la carte d'identité : modèle, domaine, liens |
| `demo/captures/01.png` | le `ping` sans réponse — le hors-ligne, vérifié |
| `demo/captures/02.png` | le modèle qui répond à `tp_002`, en cours de génération |
| `demo/captures/03.png` | la session USSD complète, au compteur de caractères |
| `demo/captures/04.png` | les fichiers locaux et les chiffres du profileur |

Les légendes (`Caption`, 140 caractères maximum), dans le même ordre :

```
Qwen3.5-2B in IQ4_XS: 31.20 tokens/s and 1,544 MB peak RSS on an 8 GB laptop, CPU only, no network. Every figure measured, not estimated.

The network is off and verified, not claimed: ping gets no reply. Everything that follows runs with no connection of any kind.

One of our two declared test prompts, generated live on the CPU: an internal note summarised for management. No GPU, no cloud fallback.

The same model over USSD from any feature phone: no data plan, no app, 182 characters per screen, offline. The reach the office model lacks.

The English answer above came from a French order record on this disk. Official profiler, median of 3 runs: 31.20 tokens/s, 1,544 MB peak.
```

### `Video demo link` *(obligatoire)*

⚠️ **Devpost ne prend pas le fichier : il veut une URL** YouTube, Vimeo,
Facebook Video ou Youku. Il faut donc téléverser d'abord.

La vidéo est montée : **`demo/video-soumission.mp4`**, 82 s, 3200×1800 (16:9), 8,0 Mo,
voix off comprise (méthode dans `demo/NARRATION.md`).

1. Téléverser sur YouTube. **Non répertoriée** — pas *privée* : une vidéo privée
   est invisible pour le jury.
2. Titre : `Baarali Edge — offline enterprise assistant on an 8 GB laptop (ADTC 2026)`.
3. Coller l'URL ici.

#### Les réglages YouTube qui comptent

| Champ | Valeur | Pourquoi |
|---|---|---|
| Langue de la vidéo | **Anglais** | déclenche les sous-titres automatiques ; la narration est en anglais |
| Audience | *pas conçue pour les enfants* | obligatoire, sinon la mise en ligne bloque |
| Utilisation de l'IA | **Non** | aucun des trois cas listés : pas de personne réelle à qui l'on fait dire quelque chose, pas d'image d'un lieu réel modifiée, pas de scène réaliste fabriquée. La voix de synthèse est déclarée dans `demo/NARRATION.md` |
| Catégorie | *Science et technologie* | |
| Miniature | `demo/captures/miniature-youtube.png` | 1280×720, sous les 2 Mo imposés |
| Commentaires | désactivés | c'est une pièce de dossier, pas une publication |
| Autoriser l'intégration | coché | permet au jury de lire la vidéo depuis sa propre page |

Description (les horodatages créent des chapitres cliquables ; YouTube exige au
moins trois chapitres d'au moins dix secondes, d'où le regroupement des deux
premiers plans) :

```
Baarali Edge is an offline enterprise assistant built for the Africa Deep Tech
Challenge 2026 — Laptop LLM track, corporate_enterprise domain.

Qwen3.5-2B quantised to IQ4_XS, 1.88 B parameters, running under llama.cpp on an
8 GB laptop, CPU only, with the Wi-Fi physically switched off. Measured with the
official adtc-profiler, median of three runs: 31.20 tokens/s and 1,544 MB peak
RSS against a 7,000 MB ceiling.

Everything in this video runs on the machine. Nothing is simulated.

0:00  The machine is offline, and the model answers anyway
0:22  The same model over USSD, from any feature phone
0:38  The documents stay on the disk — and the measured figures
0:57  How we got here

On the throughput shown on screen: the live demo reports about 27 tokens/s,
because recording the screen costs CPU. The 31.20 figure comes from the official
profiler on an otherwise idle machine. Both numbers are in the repository.

Code and full report: https://github.com/benewende-dev/baarali-edge
Model weights: https://huggingface.co/Benewende-dev/baarali-edge-2b

The voice-over is synthetic. The screen recording is not.
```

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
