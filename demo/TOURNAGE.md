# Tournage de la vidéo de soumission

Deux minutes maximum, c'est un plafond du règlement. Tout est prêt pour tenir en
**25 secondes de démonstration**, ce qui laisse le reste pour dire pourquoi.

## Avant d'appuyer sur « enregistrer »

```bash
# 1. Répéter sans couper le Wi-Fi, pour vérifier que la machine est prête
.venv/bin/python demo/tournage.py --repetition

# 2. Fermer tout le reste. La machine a 8 Go et a déjà gelé pour moins que ça :
#    ni Docker/Colima, ni Ollama, ni serveur de développement, ni navigateur lourd.

# 3. Terminal en plein écran, police agrandie (⌘+ trois ou quatre fois).
#    Ce qui est illisible à l'écran est perdu.

# 4. Portable sur une surface dure. Le règlement retire 10 points au-delà de
#    85 °C, et un lit ou un canapé bouche les aérations.
```

## La prise

```bash
# Couper le Wi-Fi — à l'écran, pour que ça se voie
networksetup -setairportpower en0 off

# Lancer. Le script refuse de démarrer si le réseau répond encore.
.venv/bin/python demo/tournage.py

# Rétablir
networksetup -setairportpower en0 on
```

Le script enchaîne quatre actes dans un seul processus, donc les poids ne sont
chargés qu'une fois :

| Acte | Ce qu'on voit | Ce que ça prouve |
|---|---|---|
| 1 | `ping` sans réponse | la machine ne joint personne — vérifié, pas allégué |
| 2 | `tp_002` généré en flux, ~9 s | le modèle calcule ici, maintenant |
| 3 | session USSD complète, compteur de caractères | la portée sans forfait, à sa vraie limite |
| 4 | `commandes.json` local + chiffres du profileur | rien n'est sorti de la machine |

## Ce qu'il faut dire par-dessus

Le film montre que ça marche. La voix doit dire **pourquoi ça compte**, parce
que ça, l'écran ne le montre pas :

1. *« Le portable a une batterie. La box fibre, non. »* — 80,4 % des entreprises
   ivoiriennes déclarent des coupures ; l'assistant en nuage tombe précisément
   quand le travail est urgent.
2. *« Les documents ne sortent pas. »* — contrats, paie, fichiers clients : ce
   n'est pas une préférence, c'est souvent une impossibilité.
3. *« Chaque chiffre a été mesuré, y compris ceux qui nous dérangent. »* — le
   dépôt contient la variante qui nous bat sur la justesse, et la décision qu'on
   a dû retirer.

## Deux choix assumés, à ne pas cacher si on est interrogé

**Pas de numéro court filmé.** Un vrai `*384*...#` exige une convention
opérateur. Le mode `--serveur` est le même gestionnaire, branché sur le contrat
d'agrégateur réel ; on le dit, on ne le mime pas. Et l'avantage à ne pas gâcher :
notre démonstration entière tient **réseau coupé**, ce qu'une soumission branchée
sur un vrai code court ne peut pas montrer.

**L'acte 2 montre `tp_002`, pas `tp_001`.** D'abord parce que la définition
officielle du domaine est *summarization, drafting, and analysis* et que
`tp_002` est exactement cela. Ensuite parce que `tp_001` déroule 500 jetons de
calcul qui mangeraient la moitié du temps, et qu'il contient l'erreur d'arrondi
sur la « semaine entamée ». Cette erreur est écrite dans `REPORT.md` et sur la
fiche publique du modèle : ne pas la filmer n'est pas la cacher.

## Après

Le montage — voix off, gels et cartons de fin — est décrit dans
[`NARRATION.md`](NARRATION.md) et se rejoue en une commande :

```bash
bash demo/montage.sh demo/voix demo/prise-AAAAMMJJ-HHMMSS.mov video-soumission.mp4
```

Téléverser ensuite la vidéo (Devpost n'accepte qu'une **URL**, jamais un
fichier), puis remplir le brouillon — il ne demande que
`Project Report Public URL on Github`, les deux prompts de test, le domaine,
`Self Reported Sperf` et `Self Reported Seff`. Tout est dans `submission.json`
et dans <https://github.com/benewende-dev/baarali-edge>.
