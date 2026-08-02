# Résultats de mesure — étape 1

Chaque ligne sort d'un `submission.json` produit par le profileur officiel, jamais d'une fiche de
modèle. Les fichiers bruts sont dans `bench/raw/`, un par mesure.

**Machine de mesure** (relevée automatiquement par le profileur) : Apple M1, 8 Go, graphique
intégré, macOS. Le profileur impose `-ngl 0` — **processeur seul, aucune accélération graphique**,
comme sur le portable de référence. Les valeurs absolues ne sont donc pas celles d'un i5, mais
tous les candidats subissent la même machine : la **comparaison entre eux est valide**, et c'est
elle qui décide.

Commande : `.venv/bin/python bench/mesurer.py --tous [--justesse --tache=… --limite=…]`

---

## Débit et mémoire (1er août 2026)

| Candidat | Params réels | Licence | Débit | Pic RAM | S_eff | Contexte |
|---|---|---|---|---|---|---|
| Qwen3.5-0.8B | 0,75 Md | Apache 2.0 | **64,0 t/s** | **1,16 Go** | **83,4** | 262 144 |
| Qwen3.5-2B | 1,88 Md | Apache 2.0 | 33,9 t/s | 2,33 Go | 66,7 | 262 144 |
| SmolLM3-3B | 3,08 Md | Apache 2.0 | 25,2 t/s | 2,66 Go | 62,0 | 65 536 |
| Phi-4-mini | 3,84 Md | MIT | 20,9 t/s | 3,35 Go | 52,1 | 131 072 |
| Qwen3.5-4B | 4,21 Md | Apache 2.0 | 15,4 t/s | 3,65 Go | 47,9 | 262 144 |

Tous en GGUF Q4_K_M. `S_eff = 100 × (7 Go − pic) ÷ 7 Go`, barème officiel.

**Deux conclusions immédiates :**

1. **Aucun risque de disqualification mémoire.** Le plus lourd laisse 3,35 Go de marge sous le
   plafond de 7 Go. La contrainte qui écartera d'autres candidats ne nous limite pas — on choisit
   sur la qualité, pas par peur du dépassement.
2. **Phi-4-mini est dominé par SmolLM3-3B sur les deux axes** — plus lent (20,9 contre 25,2) *et*
   plus lourd (3,35 contre 2,66 Go), pour 0,8 milliard de paramètres de plus. Il ne survit qu'en
   étant nettement plus juste.

---

## Le débit est noté relativement : ce que ça change

`S_perf = 100 × (notre débit ÷ débit de la meilleure soumission)`. Le dénominateur est fixé par
**les autres candidats**, pas par nous. L'écart entre un petit et un gros modèle sur la moitié de
la note qui ne dépend pas de la justesse en dépend entièrement :

| Si le plus rapide du concours fait… | Écart 0,8 Md vs 3 Md | Justesse que le 3 Md doit rattraper |
|---|---|---|
| 64 t/s | 22 points | +45 sur 100 — hors de portée |
| 150 t/s | 12 points | +24 — difficile |
| 300 t/s | 8 points | +16 — **atteignable** |

300 t/s n'est pas une hypothèse : **le modèle d'exemple fourni par les organisateurs** (135 M de
paramètres) tourne à **319 t/s sur cette machine**. Il suffit qu'un concurrent soumette quelque
chose de cet ordre pour écraser l'axe vitesse de tout le monde.

**D'où une conclusion contre-intuitive :** plus les concurrents courent après la vitesse avec des
modèles minuscules, moins la vitesse rapporte, et plus la justesse — 50 % de la note — décide
seule. Parier sur la petitesse revient à parier sur ce que font les autres ; parier sur la
justesse est robuste quoi qu'ils fassent. À budget mémoire tenu, **le plus gros modèle raisonnable
est le pari le plus sûr**.

---

## Justesse — les cinq candidats (`arc_easy`, 200 questions)

| Candidat | Justesse | Débit | Pic RAM | S_eff |
|---|---|---|---|---|
| Phi-4-mini | **0,765** | 20,6 t/s | 3,30 Go | 52,8 |
| Qwen3.5-4B | 0,735 | 14,9 t/s | 3,49 Go | 50,1 |
| SmolLM3-3B | 0,720 | 25,5 t/s | 3,02 Go | 56,9 |
| Qwen3.5-2B | 0,675 | 33,9 t/s | 2,52 Go | 64,1 |
| Qwen3.5-0.8B | 0,640 | 65,3 t/s | 1,21 Go | 82,7 |

## Ce que le questionnaire à choix multiples ne voit pas

La justesse notée est « une combinaison de références automatisées **et de l'évaluation qualitative
des réponses par le jury** ». Les cinq candidats ont donc composé sur nos deux prompts réels
(copies intégrales dans `bench/copies/`, produites par `bench/repondre.py`).

**Question 1** — 25 jours de retard, 2 % par *semaine entamée*, plafond 10 % : la réponse juste est
6 % ou 8 % selon la lecture, **jamais le plafond**, et « entamée » impose d'arrondir au-dessus.

| Modèle | Réponse | Verdict |
|---|---|---|
| SmolLM3-3B | *aucune* | raisonne en anglais dans un bloc `<think>` et n'arrive jamais à conclure |
| Qwen3.5-0.8B | 450 000 | applique le plafond sans calculer, puis ajoute une note incohérente |
| Phi-4-mini | 450 000 | « 15 jours × 2 % = 30 % » : confond jours et semaines |
| Qwen3.5-2B | 270 000 | méthode juste, clause citée, plafond vérifié ; arrondit à la baisse |
| Qwen3.5-4B | 180 000 | meilleure lecture juridique, mais arrondit à la baisse **en l'assumant** |

**Question 2** — seuls les deux Qwen retiennent les quatre faits. Les trois autres oublient le
contrat non signé dans leur synthèse **et le réclament ensuite comme information manquante**, alors
que la note le dit.

⚠️ SmolLM3-3B est un modèle « raisonneur » : avec `/no_think` il répond enfin, mais calcule au
prorata (3,57 semaines) au lieu d'arrondir, ce que la clause interdit.

## Décision de l'étape 1 : **Qwen3.5-2B**

Score total au barème, justesse composée moitié mesure / moitié rédaction :

| Vitesse du meilleur concurrent | 0,8 Md | **2 Md** | SmolLM3 | Phi-4 | 4 Md |
|---|---|---|---|---|---|
| 65 t/s | 68,8 | 65,3 | 54,9 | 49,2 | 56,5 |
| 150 t/s | 51,9 | **56,5** | 48,2 | 43,8 | 52,6 |
| 319 t/s | 44,9 | **52,9** | 45,5 | 41,6 | 51,1 |

Il gagne deux scénarios sur trois et n'est jamais mauvais. Le 0,8 Md ne l'emporte que si personne,
parmi 1 340 inscrits, ne soumet un modèle rapide — un pari qui dépend des autres.

---

# Étape 2 — quantification du socle retenu

Sept variantes de Qwen3.5-2B, même protocole. La justesse est **déterministe** (température nulle,
graine fixée) ; le débit et la mémoire ne le sont pas, et ont donc été **repassés trois fois**.

| Variante | Justesse | Débit (méd. 3) | Pic RAM (méd. 3) | S_eff | S @150 t/s |
|---|---|---|---|---|---|
| **IQ4_XS** | 0,670 | **34,3 t/s** | **1,74 Go** | **75,2** | **55,4** |
| Q4_K_M | 0,675 | 31,6 t/s | 2,08 Go | 70,2 | 54,1 |
| MTP-Q4_K_M | 0,675 | 31,1 t/s | 2,20 Go | 68,5 | 53,7 |
| UD-Q4_K_XL | 0,650 | 29,4 t/s | 2,21 Go | 68,4 | 52,1 |
| UD-Q5_K_XL | 0,680 | 29,0 t/s | 2,11 Go | 69,8 | — |
| Q5_K_M | 0,670 | 26,7 t/s | 2,01 Go | 71,3 | — |
| Q3_K_M | 0,630 | 30,7 t/s | 1,93 Go | 72,4 | — |

**Décision : Qwen3.5-2B en IQ4_XS.** Le plus rapide *et* le plus léger, avec la plus faible
dispersion des quatre (1,72–1,77 Go) — donc celui dont le chiffre tiendra à l'audit.

### Quatre idées reçues tombées à la mesure

1. **Payer plus cher en Q5 n'achète pas de justesse** : 0,670, exactement comme IQ4_XS qui pèse 25 % de moins.
2. **La quantification « dynamique » n'a pas tenu sa promesse** : UD-Q4_K_XL sort à 0,650, *en dessous* du Q4_K_M ordinaire.
3. **La prédiction multi-jetons n'accélère rien ici** : 31,1 contre 31,6 t/s. Le profileur lance `llama-bench` sans réglage et ne l'exploite pas — la tête supplémentaire n'ajoute que du poids.
4. **Une mesure unique de mémoire ne vaut rien** : UD-Q4_K_XL avait affiché 1,47 Go au premier passage (le plus léger du lot) contre une médiane réelle de 2,21 Go (le plus lourd). Sans les trois passages, on choisissait sur du bruit.

### Le plancher

En Q3_K_M la justesse tombe à 0,630 sans compensation ailleurs : c'est la limite basse.

⚠️ `arc_easy` est un test de raisonnement général, **pas** le domaine Entreprise/PME. Les
organisateurs annoncent fournir un jeu de validation par domaine : dès qu'on l'a, on re-mesure les
finalistes dessus. `arc_easy` sert ici à **classer**, pas à prédire la note du jury.

---

# Étape 3 — robustesse : la pénalité de répétition

Commande : `.venv/bin/python bench/penalite.py` → `bench/copies/penalite-repetition.md`

## La panne

La sonde langues a mis au jour un mode d'échec franc : sur une entrée hors de sa compétence, le
modèle ne refuse pas, il **boucle** — une phrase répétée jusqu'à épuiser le budget de jetons.

Ce n'est pas cosmétique. Le jury ajoute **2 prompts cachés** ; une boucle sur l'un d'eux, c'est une
copie blanche sur un quart de l'épreuve qualitative. Et **la chaîne officielle ne protège de
rien** : relu dans `adtc_profiler/accuracy.py`, l'appel est
`create_completion(temperature=0.0)`, sans pénalité, et `llama-cpp-python` 0.3.34 a
`repeat_penalty = 1.0` par défaut. Ce que nous avons observé est donc **exactement** ce que verrait
un correcteur.

## Ce que la mesure a corrigé en route

Le premier passage comparait cinq pénalités sur un indicateur de **forme** — la proportion de
quadrigrammes distincts, qui détecte une boucle sans avis humain. Il concluait « 1,10 règle tout,
diversité 0,99 ». Sauf qu'à 1,10 la réponse à `tp_001` passait de 270 000 FCFA (juste) à
**63 450 FCFA** (absurde), avec une forme irréprochable. **La pénalité ne casse pas la citation :
elle dévie le raisonnement**, et un indicateur de forme est aveugle à ça.

D'où un second contrôle, sur le **fond** : dix-huit énoncés de gestion ordinaires — TVA ivoirienne,
remise, plafond contractuel, provision, escompte, marge, puis douze enchaînements à plusieurs
calculs — dont la bonne réponse est un **nombre** dont on vérifie la présence. Douze, et pas
quatre : au premier essai le niveau multi-étapes n'en comptait que quatre, dont un raté à toutes
les pénalités et un réussi à toutes. Deux énoncés discriminants ne décident de rien.

## Résultats

| Pénalité | Boucles réglées | Fond, 1 étape | Fond, n étapes |
|---|---|---|---|
| 1,00 *(défaut officiel)* | **0 / 3** | 6/6 | 9/12 |
| 1,05 | 2 / 3 | 6/6 | 9/12 |
| **1,10** | **3 / 3** | **6/6** | **9/12** |
| 1,15 | 3 / 3 | 6/6 | 4/12 |
| 1,20 | 3 / 3 | 5/6 | 4/12 |

## Décision : `repeat_penalty = 1.10`

C'est **la plus petite valeur qui supprime les trois boucles**, et elle le fait à **coût nul
mesuré** : 6/6 et 9/12, exactement comme sans pénalité. Au-delà, la falaise est brutale — 1,15 fait
tomber le raisonnement à plusieurs étapes de 9/12 à 4/12, soit plus de la moitié des énoncés
perdus, sans rien régler de plus.

L'anomalie de `tp_001` à 1,10 se lit maintenant pour ce qu'elle est : une trajectoire de
raisonnement déplacée sur **un** échantillon, pas une tendance. Sur dix-huit énoncés, 1,10 est
indiscernable de 1,00. Sans le second contrôle, on aurait écarté la bonne valeur sur un cas isolé.

### Deux limites à dire clairement

1. **Cette pénalité ne change pas notre note automatisée.** La justesse du profileur passe par des
   vraisemblances (`arc_easy` en QCM), où l'échantillonnage n'intervient pas. C'est un réglage
   **recommandé pour la génération** — documenté dans le `README.md` et appliqué dans `demo/` —
   pas un levier sur `S_acc`. Le prétendre serait faux.
2. **`retard+plafond` échoue à toutes les pénalités.** Arrondir à la *semaine entamée* reste hors
   de portée du modèle, exactement comme à l'étape 1. C'est une limite du socle, et elle est écrite
   telle quelle dans `USE_CASE.md` plutôt que passée sous silence.

---

# Étape 4 — le paquet, mesuré tel qu'il sera soumis

Trois passages du profileur officiel sur `model/Qwen3.5-2B-IQ4_XS.gguf`, c'est-à-dire sur le
fichier que `download_model.sh` télécharge, au chemin que `_runtime.model_path` déclare.
Bruts : `bench/raw/final-iq4xs-{1,2,3}.json`.

| | Run 1 | Run 2 | Run 3 | **Médiane** |
|---|---|---|---|---|
| Débit | 32,23 t/s | 28,25 t/s | 31,20 t/s | **31,20 t/s** |
| Pic RSS | 1 615 Mo | 1 544 Mo | 1 526 Mo | **1 544 Mo** |
| Premier jeton | 3 351 ms | 4 643 ms | 3 398 ms | 3 398 ms |
| CPU p99 | 97,5 % | 97,3 % | 87,0 % | 97,3 % |

Bridage thermique : **aucun**. Justesse `arc_easy` : **0,68** (50 questions, défaut du profileur).
`params_match: true` — le profileur a compté 1 881 825 088 paramètres et validé « 1.88B ».

**S_eff = 77,9** sur 7 Go décimaux (78,5 sur 7 Gio). On retient le plus bas : un chiffre
sous-estimé ne peut pas être contredit à l'audit.

## L'écart avec l'étape 2, dit avant qu'on nous le demande

L'étape 2 relevait 34,3 t/s et 1,74 Go pour ce même fichier. Même machine, même commande. C'est de
la variance entre passages et de l'état thermique d'un portable sans ventilateur. D'où la règle
déjà appliquée : **médiane de trois**, et le tableau de l'étape 2 ne sert qu'à **classer** des
candidats mesurés coup sur coup, jamais à revendiquer une valeur absolue.

## Zéro appel réseau : mesuré, pas déduit

`bash bench/hors_ligne.sh --sockets` — 15 relevés pendant une inférence complète.

Le résultat corrige une idée fausse qu'on allait écrire : **`llama-cli` ouvre bel et bien des
sockets**, systématiquement, une paire en boucle locale (`127.0.0.1` qui se connecte à lui-même)
qui sert de réveil de threads. Un contrôle naïf « une socket ⇒ échec » nous aurait recalés — et
recalerait n'importe quelle soumission llama.cpp. Le critère juste est l'absence d'adresse **non
locale**, et sur ce critère : **aucune, sur les 15 relevés**.

Deux pièges de mesure rencontrés en chemin, notés parce qu'ils coûtent du temps :

- `llama-cli -no-cnv` **sans `-st`** génère puis attend un second tour : un run est resté 17
  minutes en vie pour 48 jetons.
- `lsof` sort en **code d'erreur quand il ne trouve rien**. Sous `set -e`, le script mourait
  exactement dans le cas favorable.

## L'épreuve Wi-Fi coupé

`bash bench/hors_ligne.sh --sans-wifi` — Wi-Fi éteint, injoignabilité confirmée par `ping`,
inférence complète en **7 s**, 33,5 t/s en génération, puis Wi-Fi rétabli et vérifié.

Un troisième piège, et le plus instructif des trois. La première version déclarait l'interface
réseau en variable **locale** à la fonction. Or un `trap EXIT` s'exécute **après** la sortie de la
fonction : au moment exact où le filet devait rétablir le Wi-Fi, la variable n'existait plus. La
machine est restée hors ligne, et il a fallu rallumer à la main.

Un garde-fou qui ne tient pas au moment de l'accident n'est pas un garde-fou. La variable est
maintenant globale, le rétablissement est une fonction nommée, et il **vérifie** l'état de
l'interface au lieu de l'espérer.

## Le paquet, de bout en bout

`model/` vidé, puis `bash download_model.sh` : **7 min 46 s**, empreinte
`3639f34b5ca22aa1c51f3616566eae8c355111554f6924ad97ee2652ed11c1cd` identique à l'attendue.
`curl` seul, URL publique, aucun jeton — exactement ce dont dispose un évaluateur.

Poids publiés : <https://huggingface.co/Benewende-dev/baarali-edge-2b>
