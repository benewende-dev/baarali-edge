# Recalibrer la matrice d'importance — et mesurer que ça ne sert à rien

*Document de travail. Le résultat publié est dans [`../REPORT.md`](../REPORT.md), section 4 ; le
protocole complet et les chiffres dans [`../bench/resultats.md`](../bench/resultats.md), étape 6.*

## Ce que ce dossier contient

| Fichier | Rôle |
|---|---|
| `corpus.py` | fabrique le corpus de calibration, graine fixe |
| `corpus.txt` | le corpus produit — versionné pour qu'on puisse le **lire**, pas seulement le refaire |
| `contamination.py` | vérifie que le corpus ne contient rien des épreuves qui le jugent |
| `recalibrer.sh` | enchaîne contrôle → matrice → quantisation |
| `types-unsloth.txt` | le découpage des types du fichier livré, relevé tenseur par tenseur |

## Le raccourci qu'on n'a pas pris, et ce qu'il aurait coûté

Le calcul part du **BF16** (3,8 Go), jamais du fichier IQ4_XS déjà quantifié : requantiser un
fichier quantifié empile deux arrondis et mesure cette erreur-là plutôt que la calibration.

Le prix se paie en temps. Sur une machine à 8 Go, 3,8 Go ne tiennent pas en cache : chaque fragment
relit le modèle depuis le disque. Mesuré, `llama-imatrix` tourne à **12 % de processeur** — il
n'attend pas le calcul, il attend le SSD — soit 12,6 s par fragment et 18 minutes pour 88 fragments.

Partir du **Q8_0** (2 Go, qui tient en RAM) coûterait un arrondi supplémentaire mais irait sans
doute trois à quatre fois plus vite. Sur cette machine, le vrai coût n'est pas la précision, c'est
la pagination. À refaire, c'est la première chose à essayer.

## Les deux pièges, dont un qui a mordu

**Le corpus qui contient ses propres épreuves.** Une matrice calibrée sur un texte protège les
poids qu'active ce texte. Si le corpus contient les énoncés qui serviront à le juger, la
recalibration améliore ses propres notes sans améliorer le modèle. Fabriquer le corpus ne met pas à
l'abri : ses gabarits ont été écrits par la même main que les épreuves, dans le même registre, avec
les mêmes villes. `contamination.py` a effectivement trouvé huit mots consécutifs communs entre le
gabarit « note de service » et l'épreuve `note-conges`. Le gabarit a été réécrit.

**Le témoin manquant.** Le premier fichier produit pesait 23 Mo de plus que le livré, et il aurait
été tentant d'attribuer l'écart de justesse à la calibration. Vérification faite, l'écart de poids
venait du découpage des types, différent chez le producteur du fichier livré. Sans témoin, deux
causes se seraient confondues dans un seul chiffre — et aucune mesure ultérieure n'aurait pu les
séparer.

## Refaire la manipulation

```bash
python3 imatrix/corpus.py > imatrix/corpus.txt     # 184 documents, graine fixe
python3 imatrix/contamination.py                   # doit sortir 0
bash imatrix/recalibrer.sh                         # ~19 min sur M1 8 Go

# le témoin : même chose, matrice héritée
llama-quantize --imatrix bench/models/recalibre/imatrix_unsloth.gguf \
  bench/models/qwen35-2b-bf16/Qwen3.5-2B-BF16.gguf sortie-temoin.gguf IQ4_XS

# le candidat comparable au livré : notre matrice, son découpage
llama-quantize --imatrix bench/models/recalibre/baarali-entreprise.imatrix.gguf \
  --tensor-type-file imatrix/types-unsloth.txt \
  bench/models/qwen35-2b-bf16/Qwen3.5-2B-BF16.gguf sortie-v2.gguf IQ4_XS
```

Puis les mesures :

```bash
.venv/bin/python bench/mesurer.py q2b-iq4xs-baarali-v2 --justesse
.venv/bin/python bench/redaction.py q2b-iq4xs-baarali-v2
.venv/bin/python bench/apparie.py q2b-iq4xs q2b-iq4xs-baarali-v2
```

## Le résultat, en une ligne

196 réponses identiques sur 200. Le levier est plat sur ce fichier.
