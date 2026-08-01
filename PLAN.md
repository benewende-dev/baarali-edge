# Plan — Africa Deep Tech Challenge 2026 (Laptop LLM)

**Échéance officielle : 24 août 2026, 23 h 45 PDT** = **25 août, 06 h 45 à Abidjan**.
Objectif interne : **tout bouclé le 15 août**, les 10 jours restants servent de marge.

Gate 2 (audit technique) : 8–29 septembre. Gate 3 (défense orale) : 17 octobre.

---

## Ce qui décide de la note (relu dans le code du profileur, pas dans la brochure)

```
S = 0,50 · Justesse + 0,30 · Débit + 0,20 · Légèreté − 10 (si > 85 °C)
```

| Axe | Comment c'est mesuré, réellement |
|---|---|
| Justesse (50 %) | `lm-evaluation-harness` sur le GGUF **quantifié**, `n_ctx = 2048`, via `llama-cpp-python`. Défaut de fumée : `arc_easy`, 50 questions. L'audit utilise un sous-ensemble de validation **caché**. |
| Débit (30 %) | `llama-bench -p 512 -n 128 -ngl 0`. **`-ngl 0` = carte graphique interdite, processeur seul.** Score = 100 × (t/s ÷ 15). |
| Légèreté (20 %) | Pic de RSS échantillonné toutes les 100 ms sur le processus **et ses enfants**. Score = 100 × (7 Go − pic) ÷ 7 Go. |
| Éliminatoire | Dépassement mémoire ou plantage pendant l'audit. |

**Conséquence stratégique** : 50 % de la note récompense la petitesse et la vitesse. Le point
d'équilibre est **1,5 à 4 milliards de paramètres**, pas 7. À vérifier par la mesure (étape 1),
pas à supposer.

**Bonus cumulables** : +10 % profil low-cost · +15 % langue africaine · jusqu'à +10 pts usage
africain réel. Prix séparés : meilleure intégration (3 000 $), meilleure localisation (1 500 $).

---

## Étape 0 — Inscriptions et outillage

**À faire par toi (humain, 20 min) :**
- [ ] S'inscrire sur [adtc-2026.devpost.com](https://adtc-2026.devpost.com) et sur le portail ADTF
- [ ] Récupérer le **`team_id`** → remplacer `TODO-REGISTER-ON-ADTF-PORTAL` dans `metadata.json`
- [ ] Renseigner le nom légal complet dans `metadata.json`
- [ ] Créer un compte Hugging Face (hébergement public des poids, gratuit)
- [ ] Lire les règles d'éligibilité complètes sur Devpost et confirmer la résidence (Abidjan = OK)

**Outillage machine :**
- [ ] `brew install llama.cpp` → fournit `llama-bench`, exigé par le profileur
- [ ] Environnement Python **3.11 ou 3.12** (le poste est en 3.14 ; `llama-cpp-python` compile
      depuis les sources et n'a pas forcément de roue pour 3.14) — via `uv venv --python 3.12`
- [ ] `pip install "git+https://github.com/Africa-Deep-Tech-Foundation/adtc-profiler.git"`
- [ ] Un premier run du profileur sur le modèle d'exemple, pour prouver que la chaîne tourne

⚠️ **Mémoire** : la machine a 8 Go et a déjà gelé une fois. Pendant les mesures : **rien d'autre
ne tourne** — ni Docker/Colima, ni Ollama, ni serveur Next.js. Un pic parasite fausse la note.

---

## Étape 1 — Mesurer avant de choisir *(le cœur du travail)*

On ne choisit pas le modèle de départ par réputation : on le **note** avec le profileur officiel.

- [ ] Sélectionner 5 socles ouverts, licence permissive, dans la fourchette 1,5–4 Md de paramètres
- [ ] Pour chacun : télécharger le GGUF Q4_K_M, lancer le profileur **complet** (justesse comprise)
- [ ] Consigner dans `bench/resultats.md` : justesse, t/s, pic RAM, température, **score total calculé**
- [ ] **Décision documentée** : le socle retenu, et pourquoi les autres sont écartés

*Sortie : un tableau de scores réels. C'est aussi la moitié du `REPORT.md`, écrite d'avance.*

---

## Étape 2 — Compresser intelligemment

- [ ] Comparer Q4_K_M / Q5_K_M / IQ4_XS sur le socle retenu (l'IQ4 pèse moins pour une qualité voisine)
- [ ] Essayer une quantification guidée par **matrice d'importance** (*imatrix*) calibrée sur du
      texte d'entreprise francophone — même taille, meilleure justesse. C'est une contribution
      technique défendable devant le jury.
- [ ] Retenir le meilleur score total mesuré, pas le meilleur ressenti

---

## Étape 3 — Le dioula *(bonus +15 %, et le prix « meilleure localisation »)*

**Garde-fou avant de promettre quoi que ce soit :**
- [ ] Vérifier **ce qui existe réellement** comme données ouvertes en dioula/bambara. Si la
      réponse est « rien d'exploitable en deux semaines », on retire la revendication du
      `metadata.json` plutôt que de la revendiquer à vide — une revendication non tenue se voit
      à l'audit et coûte plus qu'elle ne rapporte.
- [ ] Affinage LoRA **additif** (louer un GPU quelques heures, ~10 à 30 $ — la machine locale ne
      peut pas entraîner)
- [ ] **Barrière de sécurité** : re-mesurer la justesse en anglais **avant/après**. Le bonus vaut
      +15 % ; s'il coûte plus de 15 % de justesse, il fait perdre des points. On garde l'affinage
      **seulement si** la mesure le valide.

---

## Étape 4 — Publier et éprouver le paquet

- [ ] Pousser les poids `.gguf` sur Hugging Face (dépôt public, sans identifiants)
- [ ] Écrire `download_model.sh` : idempotent, URL publique, chemin identique à `_runtime.model_path`
- [ ] Effacer `model/`, lancer `bash download_model.sh` **depuis zéro** : ça doit marcher seul
- [ ] Run complet du profileur → `submission.json` avec `"measured_on": "participant_laptop"`
- [ ] Couper le Wi-Fi et refaire tourner une inférence : **zéro appel réseau**, prouvé, pas supposé

---

## Étape 5 — Le rapport et la vidéo

- [ ] `REPORT.md` : problème, décisions de conception, contraintes, **chiffres mesurés** (pas d'estimations)
- [ ] Vidéo de **2 minutes maximum** : le modèle tourne hors ligne sur le portable, puis la démo
      Baarali (lecture de documents, réponse **citée**, canal USSD depuis un téléphone à touches)
- [ ] Relire les 2 `test_prompts` : le jury en ajoute 2 cachés dans le même domaine — nos prompts
      doivent être représentatifs, pas taillés sur mesure (l'anti-surapprentissage est explicite)

---

## Étape 6 — Soumettre

- [ ] Dépôt **public** sur GitHub
- [ ] Passer la liste de contrôle du gabarit officiel, ligne par ligne
- [ ] Soumettre l'URL sur Devpost **avant le 24 août 23 h 45 PDT**

---

## Ce qu'on ne fait pas

- **Baarali-v1 n'est pas ouvert.** C'est le produit commercial ; il apparaît en démonstration
  dans la vidéo, son code reste privé. Ce dépôt-ci est autonome.
- **Pas d'entraînement depuis zéro.** Deux semaines, 8 Go de RAM, aucun GPU : on part d'un socle
  ouvert, on le compresse et on l'adapte. C'est ce que le règlement autorise explicitement.
- **Aucun chiffre non mesuré dans le rapport.** Le jury re-mesure tout à l'étape 2 ; un écart
  entre nos chiffres et les leurs est le plus court chemin vers l'élimination.
