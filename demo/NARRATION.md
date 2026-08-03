# Voix off — texte à poser sur la prise muette

La prise brute (`bash demo/filmer.sh`) dure ~32 s et n'a pas de son. Ce texte se
pose dessus au montage. **181 mots, soit ~72 s** à un débit posé de 150 mots par
minute — sous le plafond de 2 minutes du règlement, qui dit *« a short video
(max 2 minutes) »* : c'est un plafond, pas une durée à remplir.

⚠️ **La voix est plus longue que l'image** (72 s contre 32 s), et c'est voulu :
le règlement demande *« explaining your solution **and development journey** »*,
or le parcours ne se filme pas. Au montage, tenir la dernière image pendant les
segments 5 et 6, ou poser un carton noir avec le lien du dépôt.

**En anglais.** Tous nos fichiers publics le sont, et c'est la langue du jury.
Le français avec sous-titres anglais serait défendable, mais on ne prend pas ce
pari pour rien.

L'écran montre **que** ça marche. La voix ne doit dire que **pourquoi ça
compte** — c'est là que sont les 10 points du cas d'usage africain, et l'écran
ne les montrera jamais tout seul.

---

## Le texte

### 1 — sur l'acte 1, le `ping` sans réponse *(~8 s, 20 mots)*

> Eight gigabytes of RAM. Integrated graphics. No network — the ping proves it.
> Everything you see runs on this machine.

### 2 — sur l'acte 2, le modèle qui génère *(~14 s, 34 mots)*

> Eighty percent of Ivorian firms report power cuts. A laptop has a battery; a
> fibre box does not. So the assistant answers here — one of our two declared
> prompts, generated now, on the CPU.

### 3 — sur l'acte 3, la session USSD *(~10 s, 25 mots)*

> The same model, reachable by USSD from any phone. No data plan, no app, one
> hundred and eighty-two characters per screen — the real limit.

### 4 — sur l'acte 4, les fichiers locaux et les chiffres *(~14 s, 33 mots)*

> The documents stay on the disk. Measured with the official profiler, CPU only,
> median of three runs: thirty-one tokens per second, one point five gigabytes
> peak, against a seven gigabyte ceiling.

### 5 — le parcours, sur la dernière image tenue *(~18 s, 44 mots)*

*C'est le segment que le règlement réclame et que l'écran ne peut pas montrer.*

> Getting here was measurement, not intuition. We profiled five open base models,
> then all seven quantisations of the winner. One decision we had already
> published, we later reversed — a second control showed the first had measured
> the wrong thing.

### 6 — carton de fin *(~10 s, 24 mots)*

> Every number in our report is measured, including the ones that do not flatter
> us. The repository names the variant that beats us on accuracy.

---

## Trois précautions

**Les chiffres se disent en toutes lettres**, pas en chiffres : une voix
synthétique lit « 31.20 » de travers une fois sur deux. Le texte ci-dessus est
déjà écrit ainsi.

**Ne pas lire un chiffre que la prise contredit.** L'acte 2 affiche un compte de
jetons mesuré pendant l'enregistrement, or capturer l'écran en 60 images par
seconde coûte du processeur : il sortira sous nos 31,20. La voix parle du
**profileur officiel, médiane de trois passages** — ce n'est pas la même mesure,
et le dire ainsi est exact. Si le montage laisse les deux chiffres à l'image en
même temps, ajouter un sous-titre `llama-bench, median of 3`.

**Ne rien promettre que le dépôt ne tienne.** Pas de langue africaine : le modèle
n'en parle aucune et c'est écrit noir sur blanc dans les limites.

---

## Coller la voix sur l'image

```bash
# voix.m4a : la bande son, montée à la longueur de la prise
ffmpeg -i demo/prise-AAAAMMJJ-HHMMSS.mov -i voix.m4a \
       -c:v copy -c:a aac -b:a 192k -shortest video-soumission.mp4
```

`-c:v copy` recopie l'image sans la ré-encoder : aucune perte de netteté sur le
texte du terminal, qui est le seul contenu à lire à l'écran.

Vérifier avant de téléverser :

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1 video-soumission.mp4
```
