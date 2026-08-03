# Voix off et montage de la vidéo de soumission

La prise brute (`bash demo/filmer.sh`) dure 32 s et n'a pas de son. La vidéo
finale en dure **82 s**, sous le plafond du règlement — *« a short video
(max 2 minutes) »* : c'est un plafond, pas une durée à remplir.

L'écart entre les deux est voulu. Le règlement demande *« explaining your
solution **and development journey** »*, or le parcours ne se filme pas : il se
raconte. Le montage donne donc à chaque plan la durée exacte de la phrase qui le
commente, et pose les deux derniers segments sur des cartons de texte plutôt que
sur une image figée.

**En anglais.** Tous nos fichiers publics le sont, et c'est la langue du jury.

L'écran montre **que** ça marche. La voix ne dit que **pourquoi ça compte** —
c'est là que sont les 10 points du cas d'usage africain, et l'écran ne les
montrera jamais tout seul.

---

## Refaire la vidéo en une commande

```bash
bash demo/montage.sh demo/voix demo/prise-AAAAMMJJ-HHMMSS.mov video-soumission.mp4
```

`demo/voix/` contient les six segments (`seg1.mp3` … `seg6.mp3`), leur texte
source (`seg1.txt` …) et les deux cartons de fin. Le script refuse de rendre un
fichier au-delà de deux minutes.

Pour refaire les cartons après une correction de texte :

```bash
python demo/cartons.py    # nécessite Pillow ; les PNG produits sont versionnés
```

## Le texte, tel qu'il a été dit

| Segment | Sur quoi | Durée mesurée |
|---|---|---|
| 1 | acte 1, le `ping` sans réponse | 7,2 s |
| 2 | acte 2, le modèle qui génère | 13,8 s |
| 3 | acte 3, la session USSD | 15,2 s |
| 4 | acte 4, les fichiers locaux et les chiffres | 18,1 s |
| 5 | carton « How we got here » | 15,4 s |
| 6 | carton de fin | 8,2 s |

Le texte exact de chaque segment est dans `demo/voix/segN.txt` — ce sont les
fichiers réellement passés au moteur, pas une transcription approchée.

**La voix est synthétique** (ElevenLabs v3 via une passerelle commerciale, voix « Liam »). Rien
dans le règlement ne l'interdit, et c'est la seule façon d'obtenir une diction
anglaise nette sans studio.

## Trois précautions, dont une qui a changé le texte

**Les chiffres se disent en toutes lettres**, pas en chiffres : un moteur de
synthèse lit « 31.20 » de travers une fois sur deux. Les fichiers `.txt` sont
déjà écrits ainsi.

**Le chiffre à l'écran contredit le chiffre officiel — on le dit à voix haute.**
L'acte 2 affiche *« 214 tokens in 8 s »*, soit 26,8 jetons/s, quand le rapport
annonce 31,20 : enregistrer l'écran à 60 images par seconde coûte du processeur.
Taire l'écart aurait laissé un jury faire la division tout seul. Le segment 4
l'énonce donc : *« On screen you just saw about twenty-seven tokens per second,
because recording the screen costs CPU. Measured clean with the official
profiler, median of three runs: thirty-one point two… »*. Sur une soumission
dont l'argument est que chaque chiffre est mesuré, c'est la seule version
tenable.

**Ne rien promettre que le dépôt ne tienne.** Pas de langue africaine : le
modèle n'en parle aucune et c'est écrit noir sur blanc dans les limites.

## Comment le montage tient les 82 secondes

Les frontières des quatre actes ont été relevées **image par image** sur une
planche-contact à une image par seconde, pas estimées : 0 / 8,4 / 17,4 / 28,4 s.
Chaque plan dure ensuite le **maximum** de deux choses : la longueur du film et
la longueur de sa phrase. Quand la phrase est plus longue, un gel de la dernière
image comble — une image fixe, jamais un ralenti, un terminal ralenti se voit
immédiatement. Quand la phrase est plus courte, c'est le silence qui s'allonge :
raccourcir le film à la place produirait un saut d'image, et décalerait toute la
suite du montage.

Conséquence utile : l'acte 4, qui ne dure que 3,6 s dans la prise, reste 19 s à
l'écran. C'est le plan le plus dense — la fiche source en français, la réponse
anglaise au-dessus, les deux chiffres du profileur — et c'était le seul qu'on
n'avait pas le temps de lire.
