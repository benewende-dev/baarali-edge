# Plan — Africa Deep Tech Challenge 2026 (Laptop LLM)

**Échéance officielle : 25 août 2026 à 6 h 45 GMT** — Abidjan **est** en GMT, donc 6 h 45 du matin
ici. La dernière nuit utile est celle du 24 au 25 ; ne pas compter dessus.
Objectif interne : **tout bouclé le 15 août**, les 10 jours restants servent de marge.

Gate 2 (audit technique) : 8–29 septembre. Gate 3 (défense orale) : 17 octobre.

---

## Ce qui décide de la note

*(relu dans le règlement officiel Devpost et dans le code du profileur — pas dans la presse, qui
se trompe sur trois points : voir « Ce qui n'existe pas » plus bas)*

```
S = 0,50 · Justesse + 0,30 · Débit + 0,20 · Légèreté − 10 (si > 85 °C)
    + jusqu'à 10 points de bonus « cas d'utilisation africain »
```

| Axe | Comment c'est mesuré, réellement |
|---|---|
| Justesse (50 %) | Mélange de **références automatisées** (`lm-evaluation-harness` sur le GGUF quantifié, `n_ctx = 2048`, jeu de validation caché) **et d'une évaluation qualitative par le jury** — qui inclut explicitement **la qualité de la documentation**. Le `REPORT.md` est donc *dans* les 50 %. |
| Débit (30 %) | `llama-bench -p 512 -n 128 -ngl 0` (**carte graphique interdite, processeur seul**). Score = 100 × (t/s ÷ **t/s de la meilleure soumission**) — barème **relatif**, pas une référence fixe. |
| Légèreté (20 %) | Pic de RSS échantillonné toutes les 100 ms sur le processus **et ses enfants**. Score = 100 × (7 Go − pic) ÷ 7 Go. |
| Bonus africain | Jusqu'à **+10 points** au score total, selon l'applicabilité à un cas d'usage africain réel. |
| Éliminatoire | Dépassement mémoire (OOM) ou plantage pendant l'audit. |

**Prix** : 8 000 / 4 000 / 3 000 $ **au classement**, plus 1 500 $ « meilleure étude de cas
africaine », plus des bourses en crédits GPU (10 finalistes × 250 $, 20 demi-finalistes × 50 $).
Total en espèces affiché : 16 500 $.

### Ce qui n'existe pas (et que la presse annonçait)

- **Aucun multiplicateur** « +15 % langue africaine » ni « +10 % portable low-cost ». Le seul
  bonus du règlement est celui, en points, du cas d'utilisation africain.
- **Aucun prix « meilleure intégration »**. La 3ᵉ place vaut 3 000 $, c'est tout.
- **Aucune référence fixe de 15 t/s** : le débit est noté par rapport à la meilleure soumission.

---

## La stratégie, en une phrase

**On vise le classement**, pas un prix latéral. On gagne les axes gagnables (débit, légèreté,
bonus africain), on reste honorable sur celui qui ne l'est pas (justesse brute).

### L'arithmétique qui décide de la taille du modèle

En supposant que la meilleure soumission tourne autour de 40 t/s sur le portable de référence :

| | 7 Md | 3 Md | 1,5 Md |
|---|---|---|---|
| Débit (30 %) | ~11 | ~25 | ~50 |
| Légèreté (20 %) | 29 | 63 | 77 |
| **Écart cumulé vs 7 Md** | — | **+11 pts** | **+21 pts** |

Pour rattraper, un 7 Md devrait être **22 points plus juste sur 100**. Il ne l'est pas.
Entre **3 et 1,5 milliard, c'est trop serré pour trancher sur le papier** : c'est l'objet de
l'étape 1, qui n'est donc pas une précaution mais **la décision elle-même**.

### Où sont les 10 points les moins chers du plateau

Gagner 10 points par la justesse demanderait +20 points de justesse (poids 0,50) ; par le débit,
il faudrait tripler la vitesse. Par le **bonus africain**, il suffit de prouver un usage réel —
canal USSD déjà en service, documents de PME francophones, contexte de coupures et de data
comptée. C'est ce que la plupart des concurrents, qui optimisent des modèles sans terrain, ne
pourront pas produire.

---

## Étape 0 — Inscriptions et outillage

**À faire par toi (humain) :**
- [x] Profil Devpost complet (spécialité, compétences, admissibilité, bio)
- [ ] S'inscrire au challenge (« Participez au hackathon » → formulaire *Registre*)
- [ ] **`team_id`** — vérifié le 1er août : **aucun champ `team_id` n'existe**, ni à l'inscription,
      ni dans « Additional info », et le « portail ADTF » dont parle le gabarit n'existe pas. On
      pose donc `baarali-edge` et on demande confirmation sur le Discord. Ne pas laisser la valeur
      d'exemple : leur liste de contrôle refuse les valeurs par défaut.
- [ ] **Demander les 5 heures de crédits GPU offertes par Udutech** — c'est gratuit, ça met du
      temps à être accordé, et c'est ce qui rendra un affinage possible sans dépenser un franc
- [ ] Récupérer le **jeu de validation du domaine Entreprise/PME** (onglet Ressources) — les
      organisateurs en fournissent un par domaine : on mesurera dessus, pas sur un test générique
- [x] Compte Hugging Face : **huggingface.co/Benewende-dev** — c'est là que seront publiés les
      poids `.gguf` (dépôt public, gratuit, accessible sans identifiants comme l'exige le gabarit)

**Outillage machine :**
- [ ] `brew install llama.cpp` → fournit `llama-bench`, exigé par le profileur
- [ ] Environnement Python **3.11 ou 3.12** (le poste est en 3.14 ; `llama-cpp-python` compile
      depuis les sources et n'a pas forcément de roue pour 3.14) — via `uv venv --python 3.12`
- [ ] `pip install "git+https://github.com/Africa-Deep-Tech-Foundation/adtc-profiler.git"`
- [ ] Un premier run du profileur sur le modèle d'exemple, pour prouver que la chaîne tourne

⚠️ **Mémoire** : la machine a 8 Go et a déjà gelé une fois. Pendant les mesures : **rien d'autre
ne tourne** — ni Docker/Colima, ni Ollama, ni serveur Next.js. Un pic parasite fausse la note.

---

## Étape 1 — Mesurer avant de choisir *(le cœur du travail, et la décision principale)*

On ne choisit pas le modèle de départ par réputation : on le **note** avec le profileur officiel.

- [ ] Sélectionner 5 socles ouverts, licence permissive, couvrant **1 Md à 4 Md** de paramètres
- [ ] Pour chacun : GGUF Q4_K_M, profileur **complet** (justesse comprise), 3 exécutions, médiane
- [ ] Consigner dans `bench/resultats.md` : justesse, t/s, pic RAM, température, **score total**
- [ ] **Décision documentée** : le socle retenu, et pourquoi chaque autre est écarté

*Sortie : un tableau de scores réels — et la moitié du `REPORT.md`, écrite d'avance.*

---

## Étape 2 — Compresser intelligemment

- [ ] Comparer Q4_K_M / Q5_K_M / IQ4_XS sur le socle retenu (l'IQ4 pèse moins pour une qualité voisine)
- [ ] Essayer une quantification guidée par **matrice d'importance** (*imatrix*) calibrée sur du
      texte d'entreprise francophone — même taille, meilleure justesse. Contribution technique
      défendable devant le jury, et elle joue sur les deux axes à la fois.
- [ ] Retenir le meilleur score total mesuré, pas le meilleur ressenti

---

## Étape 3 — Le cas d'usage africain *(jusqu'à 10 points, et 1 500 $)*

Ce n'est pas une décoration : c'est l'équivalent de 20 points de justesse, pour bien moins d'effort.

- [ ] Écrire l'étude de cas **à partir du réel** : PME abidjanaise, coupures, data comptée,
      documents qui ne peuvent pas sortir de l'entreprise. Chiffres et situations vraies.
- [ ] Démontrer la **portée sans forfait** : le canal USSD, filmé depuis un téléphone à touches
- [ ] **Dioula — sous condition.** Vérifier d'abord ce qui existe comme données ouvertes
      exploitables. Ça n'apporte plus de multiplicateur (il n'existe pas) : ça nourrit le bonus
      des 10 points. Donc on n'y consacre du temps **que si** l'affinage ne coûte pas de justesse
      ailleurs — mesure avant/après obligatoire, avec les crédits GPU d'Udutech.
- [ ] Si la mesure ne suit pas : retirer `dyu` de `language_scope`. Une revendication non tenue
      se voit à l'audit et coûte plus qu'elle ne rapporte.

---

## Étape 4 — Publier et éprouver le paquet

- [ ] Pousser les poids `.gguf` sur Hugging Face (dépôt public, sans identifiants)
- [ ] Écrire `download_model.sh` : idempotent, URL publique, chemin identique à `_runtime.model_path`
- [ ] Effacer `model/`, lancer `bash download_model.sh` **depuis zéro** : ça doit marcher seul
- [ ] Run complet du profileur → `submission.json` avec `"measured_on": "participant_laptop"`
- [ ] Couper le Wi-Fi et refaire tourner une inférence : **zéro appel réseau**, prouvé, pas supposé

---

## Étape 5 — Le rapport et la vidéo

*Rappel : la qualité de la documentation est comptée dans les 50 % de justesse. Ce n'est pas
l'emballage du travail, c'en est une partie notée.*

- [ ] `REPORT.md` : problème, décisions de conception, contraintes, **chiffres mesurés**
- [ ] Vidéo de **2 minutes maximum** : le modèle tourne hors ligne sur le portable, puis la
      démonstration (lecture de documents, réponse **citée**, USSD depuis un téléphone à touches)
- [ ] Relire les 2 `test_prompts` : le jury en ajoute 2 cachés dans le même domaine — nos prompts
      doivent être **représentatifs**, pas taillés sur mesure (l'anti-surapprentissage est explicite)

---

## Étape 6 — Soumettre

Le formulaire Devpost (« Additional info », relevé le 1er août) demande exactement :
`Project Report Public URL on Github` · `Test Prompt 1` · `Test Prompt 2` · `Problem Domain` ·
`Self Reported Sperf` · `Self Reported Seff`. **Rien d'autre** — la justesse, ce sont eux qui la
mesurent. Donc toute la page se remplit avec un seul `submission.json` et l'URL du dépôt public.

⚠️ Les deux prompts sont saisis **deux fois** (Devpost + `metadata.json`) : ils doivent être
rigoureusement identiques, sans quoi l'audit compare deux choses différentes.

- [ ] Dépôt **public** sur GitHub (`baarali-edge` seul — jamais Baarali-v1)
- [ ] Passer la liste de contrôle du gabarit officiel, ligne par ligne
- [ ] Étapes 3, 4 et 5 du brouillon Devpost remplies (histoire, vidéo, scores)
- [ ] Soumettre **avant le 25 août 6 h 45 GMT**

---

## Ce qu'on ne fait pas

- **Baarali-v1 n'est pas ouvert.** C'est le produit privé ; il sert de banc de démonstration dans
  la vidéo, son code reste privé et ce dépôt-ci est autonome.
- **Pas d'entraînement depuis zéro.** On part d'un socle ouvert, on le compresse et on l'adapte.
- **Aucun chiffre non mesuré dans le rapport.** Le jury re-mesure tout à l'audit : un écart entre
  nos chiffres et les leurs est le plus court chemin vers l'élimination.
