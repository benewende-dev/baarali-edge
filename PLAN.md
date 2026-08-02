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

## Étape 3 — Le cas d'usage africain *(jusqu'à 10 points, et 1 500 $)* ✅

Ce n'est pas une décoration : c'est l'équivalent de 20 points de justesse, pour bien moins d'effort.

- [x] **Robustesse d'abord.** La sonde langues avait mis au jour une boucle dégénérée sur entrée
      inconnue, et la chaîne officielle n'applique aucune pénalité de répétition. Mesuré sur 23
      épreuves × 5 valeurs : `repeat_penalty = 1.10` supprime les 3 boucles à coût nul sur le fond
      (6/6 et 9/12, comme sans pénalité) ; à 1,15 le multi-étapes s'effondre à 4/12.
      → `bench/resultats.md`, `bench/copies/penalite-repetition.md`
      **⚠ Décision revue à l'étape 5 → `repeat_penalty = 1.05`.** Ce contrôle-ci était
      arithmétique, or le domaine est rédactionnel : à 1,10 le modèle répond **faux** à `tp_001`.
      Le raisonnement complet est dans `bench/resultats.md`, étape 5.
- [x] Écrire l'étude de cas **à partir du réel** → `USE_CASE.md`, chaque chiffre sourcé, plus une
      section « What we do not claim » qui retire d'avance les revendications qui ne tiendraient
      pas à l'audit.
- [x] Démontrer la **portée sans forfait** → `demo/ussd.py`. Le vrai contrat d'agrégateur, la vraie
      limite de 182 caractères, les commandes lues sur le disque. **Pas de numéro court** : il
      exige une convention opérateur, on ne le prétend pas.
- [x] **Dioula — écarté par la mesure.** La sonde (`bench/sonder_langues.py`) a donné « langue du
      Cameroun » pour le dioula, « langue du Tigré » pour le wolof, et des boucles en traduction.
      `dyu` retiré de `language_scope`. Les crédits GPU d'Udutech, s'ils arrivent, iront à
      l'affinage entreprise francophone — pas à enseigner une langue depuis zéro en 3 semaines.

---

## Étape 4 — Publier et éprouver le paquet ✅

- [x] Poids publiés : <https://huggingface.co/Benewende-dev/baarali-edge-2b> (public, sans identifiants)
- [x] `download_model.sh` : URL publique, empreinte SHA-256 vérifiée, taille contrôlée, reprise
      d'un transfert interrompu. Testé en corrompant volontairement le fichier — détecté.
- [x] `model/` vidé, téléchargement depuis zéro : **7 min 46 s**, empreinte identique, `curl` seul
- [x] Profileur complet ×3 → médiane **31,20 t/s**, **1 544 Mo**, aucun bridage, `params_match: true`
- [x] Hors ligne prouvé deux fois : aucune socket non locale sur 15 relevés, et une inférence
      complète **Wi-Fi coupé** (7 s). Trois pièges de mesure notés dans `bench/resultats.md`.

---

## Étape 5 — Le rapport et la vidéo

*Rappel : la qualité de la documentation est comptée dans les 50 % de justesse. Ce n'est pas
l'emballage du travail, c'en est une partie notée.*

- [ ] `REPORT.md` : problème, décisions de conception, contraintes, **chiffres mesurés**
- [ ] Vidéo de **2 minutes maximum**. Plan de tournage arrêté à l'étape 3, avec ce qu'on a :

      | Durée | Plan | Ce que ça prouve |
      |---|---|---|
      | 0:00–0:15 | Wi-Fi coupé à l'écran, `airport -I` ou l'icône barrée | le hors-ligne, montré |
      | 0:15–0:50 | `bench/repondre.py` ou llama-cli sur `tp_001` | l'objet noté, en marche |
      | 0:50–1:30 | `demo/ussd.py --telephone`, session complète | le canal, à sa vraie limite |
      | 1:30–2:00 | `commandes.json` ouvert sur le disque, puis le chiffre du profileur | rien ne sort de la machine |

      **Pas de numéro court filmé** : il exige une convention opérateur. Le mode `--serveur` est le
      même handler ; on le dit, on ne le mime pas. Avantage à ne pas gâcher : notre démonstration
      entière tient **réseau coupé**, ce qu'un concurrent branché sur un vrai code court ne peut
      pas montrer.
- [x] **Savoir ce qu'on nous demandera.** Le jeu de validation ne sera pas distribué aux
      participants — `adtc_profiler/accuracy.py` dit « the full hidden 30 % validation subset
      distributed by **judges** », et l'onglet Ressources du Devpost renvoie 404. Ce qu'on a, c'est
      la définition du domaine : *summarization, drafting, and analysis for small and medium
      enterprises*. La parade n'est donc pas de deviner, c'est d'être large.
- [x] **Contrôle bâti sur cette définition** → `bench/redaction.py`, 15 épreuves (5 résumer,
      5 rédiger, 5 analyser), FR + EN, huit villes plus des énoncés sans lieu, notées sans avis
      humain — dont un détecteur d'invention de nombres. Résultat : **91 % à poids égal, zéro
      nombre inventé sur 45 rédactions**, et trois limites du socle nommées (il sacrifie un fait
      pour placer un commentaire, il classe mal l'urgence, il confond marge brute et résultat).
      → `bench/copies/redaction.md`
- [x] **Relecture des 2 `test_prompts`** : gardés tels quels. `tp_002` est du résumé + analyse de
      manques, exactement la définition du domaine ; `tp_001` est de l'analyse contractuelle avec
      citation, et il est **juste** à 1,00 comme à 1,05 — c'est seulement à 1,10, la valeur qu'on
      avait retenue à tort, qu'il devenait faux. Aucun des deux n'est taillé sur mesure : ce sont
      des tâches ordinaires du domaine, ce que l'anti-surapprentissage exige.
- [ ] `REPORT.md` : rédiger la prose des *Design Decisions* (tous les chiffres sont déjà mesurés)

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
