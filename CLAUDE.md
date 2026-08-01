# Baarali Edge — consignes de travail

## Ce que c'est

Soumission au **Africa Deep Tech Challenge 2026**, piste *Laptop LLM*, domaine
`corporate_enterprise`. L'objet noté est **un modèle GGUF tournant sous llama.cpp** sur un
portable à 8 Go sans carte graphique, hors ligne. Voir `PLAN.md` pour le plan et les échéances.

**Dépôt public** (exigence du règlement), licence GPL v3 héritée du gabarit officiel.

## Ce dépôt n'est pas Baarali-v1

`~/baarali-v1` est le **produit commercial privé** et le reste. Il sert de démonstration dans la
vidéo de soumission ; son code ne migre pas ici, et rien de confidentiel (clés, clients,
architecture interne) n'apparaît dans ce dépôt public.

## Méthode de travail

1. **Un pas à la fois, proprement** — une étape se termine mesurée, écrite, committée.
2. **Revue avant d'enchaîner.**
3. **Aucun chiffre non mesuré.** Le jury re-mesure tout à l'audit (Gate 2, 8–29 sept.) : un écart
   entre nos chiffres et les leurs est le plus court chemin vers l'élimination. Un chiffre entre
   dans `REPORT.md` uniquement s'il sort de `submission.json`.
4. **Une revendication non tenue coûte plus qu'elle ne rapporte** — `african_alpha_claim` et le
   dioula ne restent dans `metadata.json` que si la mesure les soutient.
5. **Répondre en français.** Les fichiers publics (`README.md`, `REPORT.md`, `metadata.json`)
   sont en **anglais** : c'est la langue du jury.

## Commandes

```bash
brew install llama.cpp                       # fournit llama-bench, exigé par le profileur
uv venv --python 3.12 && source .venv/bin/activate
pip install "git+https://github.com/Africa-Deep-Tech-Foundation/adtc-profiler.git"

bash download_model.sh                       # récupère les poids
adtc-profiler run --submission . --mode participant --output submission.json
adtc-profiler run --submission . --mode participant --output submission.json --skip-accuracy
```

## Conditions de mesure — non négociables

- **Rien d'autre ne tourne** : ni Docker/Colima, ni Ollama, ni serveur de développement, ni
  navigateur lourd. La machine a 8 Go et a déjà gelé le 1er août 2026 pour cette raison exacte.
- **Processeur seul.** Le profileur impose `-ngl 0` ; ne jamais publier un chiffre obtenu avec
  accélération graphique.
- Trois exécutions pour tout chiffre retenu, et on note la **médiane** — une mesure unique sur un
  portable thermiquement contraint ne veut rien dire.

## Pièges du règlement (relus dans le code du profileur, pas dans la brochure)

| Piège | À faire |
|---|---|
| Choisir un gros modèle « pour la justesse » | 50 % de la note va au débit et à la mémoire : l'optimum est vers 1,5–4 Md de paramètres. **Le mesurer.** |
| Poids commités dans git | `*.gguf` est dans `.gitignore` ; l'évaluateur télécharge via `download_model.sh` |
| `download_model.sh` qui demande des identifiants | URL publique obligatoire, et chemin **identique** à `_runtime.model_path` |
| Nombre de prompts de test | **exactement 2**, dans le domaine déclaré ; le jury en ajoute 2 cachés pour détecter le surapprentissage |
| Prompts taillés sur mesure | les 2 cachés sont dans le même domaine : des prompts trop spécifiques font chuter la note, pas monter |
| Un appel réseau résiduel à l'inférence | zéro requête sortante pendant le profilage. Le vérifier **Wi-Fi coupé**, pas en lisant le code |
| Dépassement mémoire pendant l'audit | **disqualification automatique** — garder de la marge sous les 7 Go, pas frôler |
| Chauffe > 85 °C | −10 points. Mesurer sur une machine posée sur une surface dure, pas sur un lit |
| `llama-cpp-python` sur Python 3.14 | compile depuis les sources ; utiliser un environnement **3.11/3.12** |
| Bonus langue africaine pris sans mesure | +15 % ne compense pas une chute de justesse plus grande. Mesurer **avant/après** l'affinage |
