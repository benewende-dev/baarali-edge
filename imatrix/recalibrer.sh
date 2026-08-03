#!/usr/bin/env bash
# Recalibre la matrice d'importance sur le corpus d'entreprise, puis requantise.
#
# Ce que fait ce script, et ce qu'il ne fait pas. Il ne réentraîne rien : les
# poids du modèle de base sont ceux de Qwen, inchangés. Ce qui change, c'est la
# manière dont ils sont *arrondis* à 4 bits. Une quantisation à matrice
# d'importance mesure d'abord quels poids s'activent le plus sur un texte de
# référence, puis dépense sa précision sur ceux-là. Le fichier livré hérite
# d'une référence en anglais générique ; on recalcule la mesure sur le registre
# de cette soumission.
#
# Départ obligatoire du BF16, jamais du fichier IQ4_XS déjà livré : requantiser
# un fichier déjà quantisé empilerait deux arrondis et mesurerait cette erreur
# plutôt que la recalibration.
#
# Conditions de mesure : rien d'autre ne tourne. La machine a 8 Go et le BF16
# en pèse 3,8 à lui seul.
#
# Usage : bash imatrix/recalibrer.sh [dossier-de-travail]
set -euo pipefail

# La machine est en locale française : sans cela `printf %f` refuse « 1.96 » et
# attend « 1,96 ». Même piège que dans demo/montage.sh.
export LC_NUMERIC=C

RACINE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TRAVAIL="${1:-$RACINE/bench/models/recalibre}"
SOURCE="$RACINE/bench/models/qwen35-2b-bf16/Qwen3.5-2B-BF16.gguf"
CORPUS="$RACINE/imatrix/corpus.txt"
MATRICE="$TRAVAIL/baarali-entreprise.imatrix.gguf"
SORTIE="$TRAVAIL/Qwen3.5-2B-IQ4_XS-baarali.gguf"

mkdir -p "$TRAVAIL"

for f in "$SOURCE" "$CORPUS"; do
  [[ -f "$f" ]] || { echo "manque $f" >&2; exit 1; }
done

# Garde-fou : le corpus ne doit rien partager avec les jeux qui jugeront le
# résultat. Sans ce contrôle, la recalibration s'auto-noterait.
echo "── contrôle de contamination"
python3 "$RACINE/imatrix/contamination.py" "$CORPUS" | tail -3

echo
echo "── calcul de la matrice d'importance"
# -c 512 : la taille de fragment de la calibration héritée, pour que les deux
# matrices soient comparables. -ngl 0 : processeur seul, comme le concours.
# --no-ppl : la perplexité sur ce corpus ne nous apprendrait rien et coûte du
# temps de calcul sur une machine qui n'en a pas à perdre.
/usr/bin/time -l llama-imatrix \
  -m "$SOURCE" -f "$CORPUS" -o "$MATRICE" \
  -c 512 -b 512 -ngl 0 --no-ppl --output-format gguf \
  2> >(tee "$TRAVAIL/imatrix.log" >&2)

echo
echo "── quantisation IQ4_XS avec la nouvelle matrice"
llama-quantize --imatrix "$MATRICE" "$SOURCE" "$SORTIE" IQ4_XS \
  2> >(tee "$TRAVAIL/quantize.log" >&2)

echo
echo "── résultat"
ls -la "$MATRICE" "$SORTIE"
# La taille doit tomber à quelques kilo-octets près sur celle du fichier livré :
# IQ4_XS est un format à débit fixe, la matrice change la répartition de la
# précision, pas le nombre de bits. Un écart notable signalerait une erreur.
LIVRE="$RACINE/model/Qwen3.5-2B-IQ4_XS.gguf"
if [[ -f "$LIVRE" ]]; then
  A="$(stat -f %z "$LIVRE")"; B="$(stat -f %z "$SORTIE")"
  printf "\n  livré     %'d octets\n  recalibré %'d octets\n  écart     %+d octets (%.3f %%)\n" \
    "$A" "$B" "$((B - A))" "$(echo "scale=6; 100 * ($B - $A) / $A" | bc -l)"
fi
