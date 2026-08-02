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
