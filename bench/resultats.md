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

## Justesse

Mesure en cours (`arc_easy`, 200 questions, les cinq candidats). Premier relevé de calibrage :
Qwen3.5-0.8B — **0,700** sur 50 questions, 162 s pour la mesure complète.

⚠️ `arc_easy` est un test de raisonnement général, **pas** le domaine Entreprise/PME. Les
organisateurs annoncent fournir un jeu de validation par domaine : dès qu'on l'a, on re-mesure les
finalistes dessus. `arc_easy` sert ici à **classer**, pas à prédire la note du jury.
