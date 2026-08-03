#!/usr/bin/env bash
# Monte la vidéo de soumission : la prise muette + les six segments de voix off.
#
# Le problème que ce script résout. La prise dure 32 s, la narration 84 s, et le
# règlement réclame *« explaining your solution and development journey »* — or
# le parcours ne se filme pas. On ne peut donc ni accélérer la voix ni tenir la
# dernière image trente secondes. La solution est un montage à durées imposées :
# **chaque plan dure exactement le temps de la phrase qui le commente**, allongé
# si besoin par un gel de sa dernière image, et les deux derniers segments
# tombent sur des cartons de texte (`cartons.py`) au lieu d'une image figée.
#
# Usage : bash demo/montage.sh <dossier-voix> <prise.mov> <sortie.mp4>
#   <dossier-voix> contient seg1.mp3 … seg6.mp3 et carton5.png, carton6.png.
set -euo pipefail

# La machine est en locale française : sans cela `printf %f` refuse « 8.4 » et
# attend « 8,4 », alors que ffmpeg et bc ne parlent que le point décimal.
export LC_NUMERIC=C

VOIX="${1:?dossier des segments de voix}"
PRISE="${2:?prise vidéo muette}"
SORTIE="${3:?fichier de sortie}"
TRAVAIL="$(mktemp -d)"
trap 'rm -rf "$TRAVAIL"' EXIT

# Frontières des quatre actes dans la prise, relevées image par image sur une
# planche-contact à 1 image/s — pas estimées. Chaque valeur tombe juste AVANT
# l'apparition du titre suivant, pour que le titre apparaisse à l'écran pendant
# la première seconde de sa narration plutôt que dans le plan précédent.
DEBUTS=(0 8.4 17.4 28.4)
FINS=(8.4 17.4 28.4 32.0)

# Blanc laissé après chaque phrase. Sans lui, la phrase suivante enchaîne sans
# respiration et le plan change au milieu d'un mot.
BLANC=0.5
BLANC_FIN=1.2

duree() { ffprobe -v error -show_entries format=duration -of csv=p=0 "$1"; }

MORCEAUX=()
AUDIOS=()

for i in 1 2 3 4; do
  A="$VOIX/seg$i.mp3"
  [[ -f "$A" ]] || { echo "manque $A" >&2; exit 1; }
  D_AUDIO="$(duree "$A")"
  D_PLAN="$(echo "${FINS[$((i-1))]} - ${DEBUTS[$((i-1))]}" | bc -l)"
  # La durée du plan est le **maximum** des deux : jamais on ne coupe du film
  # pour rattraper une phrase courte — ça produirait un saut d'image — et jamais
  # on ne laisse une phrase déborder sur le plan suivant. Quand la voix est plus
  # courte que le film, c'est le silence qui s'allonge, pas l'image qui se coupe.
  CIBLE="$(echo "if ($D_AUDIO + $BLANC > $D_PLAN) $D_AUDIO + $BLANC else $D_PLAN" | bc -l)"
  # `printf` et non la sortie brute de bc : sous 1 seconde, bc écrit « .61 » sans
  # le zéro de tête, et ffmpeg refuse cette écriture comme durée.
  CIBLE="$(printf '%.3f' "$CIBLE")"
  GEL="$(printf '%.3f' "$(echo "$CIBLE - $D_PLAN" | bc -l)")"

  printf "  plan %d : %5.1f s de film + %5.1f s de gel = %5.1f s (voix %5.1f s)\n" \
    "$i" "$D_PLAN" "$GEL" "$CIBLE" "$D_AUDIO"

  # `tpad` clone la dernière image : le gel est une image fixe, pas un ralenti.
  # `-t` et non `-to` : après un `-ss` placé avant `-i`, `-to` se compte depuis
  # le début du fichier selon les versions de ffmpeg, `-t` jamais.
  ffmpeg -v error -ss "${DEBUTS[$((i-1))]}" -t "$D_PLAN" -i "$PRISE" \
    -vf "tpad=stop_mode=clone:stop_duration=$GEL,fps=30" -an \
    -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p "$TRAVAIL/v$i.mp4" -y
  MORCEAUX+=("$TRAVAIL/v$i.mp4")

  # La piste son du plan : la phrase, puis du silence jusqu'à la fin du plan.
  ffmpeg -v error -i "$A" -af "apad=whole_dur=$CIBLE" -c:a aac -b:a 192k \
    "$TRAVAIL/a$i.m4a" -y
  AUDIOS+=("$TRAVAIL/a$i.m4a")
done

for i in 5 6; do
  A="$VOIX/seg$i.mp3"
  IMG="$VOIX/carton$i.png"
  [[ -f "$A" && -f "$IMG" ]] || { echo "manque $A ou $IMG" >&2; exit 1; }
  D_AUDIO="$(duree "$A")"
  CIBLE="$(echo "$D_AUDIO + $([[ $i -eq 6 ]] && echo "$BLANC_FIN" || echo "$BLANC")" | bc -l)"
  printf "  carton %d : %5.1f s (voix %5.1f s)\n" "$i" "$CIBLE" "$D_AUDIO"

  ffmpeg -v error -loop 1 -t "$CIBLE" -i "$IMG" -vf "fps=30" \
    -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p "$TRAVAIL/v$i.mp4" -y
  MORCEAUX+=("$TRAVAIL/v$i.mp4")

  ffmpeg -v error -i "$A" -af "apad=whole_dur=$CIBLE" -c:a aac -b:a 192k \
    "$TRAVAIL/a$i.m4a" -y
  AUDIOS+=("$TRAVAIL/a$i.m4a")
done

# Concaténation. Le démuxeur `concat` recopie les flux sans les ré-encoder :
# les six morceaux ont déjà les mêmes paramètres, imposés ci-dessus.
: > "$TRAVAIL/liste-v.txt"; for f in "${MORCEAUX[@]}"; do echo "file '$f'" >> "$TRAVAIL/liste-v.txt"; done
: > "$TRAVAIL/liste-a.txt"; for f in "${AUDIOS[@]}";  do echo "file '$f'" >> "$TRAVAIL/liste-a.txt"; done

ffmpeg -v error -f concat -safe 0 -i "$TRAVAIL/liste-v.txt" -c copy "$TRAVAIL/video.mp4" -y
ffmpeg -v error -f concat -safe 0 -i "$TRAVAIL/liste-a.txt" -c copy "$TRAVAIL/audio.m4a" -y

# `loudnorm` amène la bande son à -16 LUFS, la cible des plateformes web. Sans
# elle, une voix grave sort autour de -19 dB et le jury doit monter le volume —
# on ne lui laisse pas ce geste à faire.
ffmpeg -v error -i "$TRAVAIL/video.mp4" -i "$TRAVAIL/audio.m4a" \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11" \
  -c:v copy -c:a aac -b:a 192k -movflags +faststart "$SORTIE" -y

# Contrôle final : la durée réelle du fichier, et le plafond du règlement.
D="$(duree "$SORTIE")"
printf "\n  ✓ %s — %.1f s, %s\n" "$SORTIE" "$D" "$(du -h "$SORTIE" | cut -f1)"
if [[ "$(echo "$D > 120" | bc -l)" == 1 ]]; then
  echo "  ✗ DÉPASSE les 2 minutes du règlement — raccourcir la narration." >&2
  exit 1
fi
