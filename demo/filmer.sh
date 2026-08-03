#!/usr/bin/env bash
# Enregistre la démonstration de soumission, en une seule prise, sans intervention.
#
# Deux obstacles, deux parades — c'est tout ce que fait ce script.
#
# 1. La démonstration exige que le Wi-Fi soit coupé, or couper le Wi-Fi coupe
#    aussi l'outil qui taperait les commandes suivantes. Tout part donc d'un seul
#    appel, et le réseau revient tout seul à la fin, y compris en cas d'échec.
#
# 2. Un script lancé depuis un agent écrit dans un tuyau, pas sur l'écran : la
#    capture n'aurait filmé qu'un fond d'écran. La démonstration est donc jouée
#    dans une **vraie fenêtre Terminal**, mise au premier plan, police 20, plein
#    écran — c'est elle que la caméra voit.
#
# Usage :
#   bash demo/filmer.sh              # la prise, muette (la voix se pose au montage)
#   bash demo/filmer.sh --voix       # capte le micro pendant la prise
#   bash demo/filmer.sh --repetition # ne coupe rien, n'enregistre pas, vérifie la machine
#
# Sortie : demo/prise-AAAAMMJJ-HHMMSS.mov (ignoré par git ; il se téléverse sur Devpost)

set -uo pipefail

RACINE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RACINE"

VOIX=0
REPETITION=0
for a in "$@"; do
  case "$a" in
    --voix)       VOIX=1 ;;
    --repetition) REPETITION=1 ;;
    *) echo "option inconnue : $a" >&2; exit 2 ;;
  esac
done

INTERFACE="${INTERFACE:-en0}"
POLICE="${POLICE:-20}"
SORTIE="$RACINE/demo/prise-$(date +%Y%m%d-%H%M%S).mov"
ATELIER="$(mktemp -d)"
FEU_VERT="$ATELIER/go"      # le joueur attend ce fichier : la capture démarre avant lui
FINI="$ATELIER/fini"        # le joueur pose ce fichier : la capture peut s'arrêter
PID_CAPTURE=""
ID_FENETRE=""

# Le filet. Quoi qu'il arrive — erreur, Ctrl-C, script tué — le réseau revient,
# l'enregistrement est refermé proprement et la fenêtre est rangée. Sans ça, un
# échec au milieu laisse la machine hors ligne et le .mov corrompu.
nettoyer() {
  if [[ -n "$PID_CAPTURE" ]] && kill -0 "$PID_CAPTURE" 2>/dev/null; then
    kill -INT "$PID_CAPTURE" 2>/dev/null   # SIGINT : screencapture referme le fichier
    wait "$PID_CAPTURE" 2>/dev/null
  fi
  [[ -n "$ID_FENETRE" ]] && osascript -e "tell application \"Terminal\" to close (every window whose id is $ID_FENETRE)" >/dev/null 2>&1
  if [[ $REPETITION -eq 0 ]]; then
    networksetup -setairportpower "$INTERFACE" on >/dev/null 2>&1
    echo "  réseau rétabli sur $INTERFACE"
  fi
  rm -rf "$ATELIER"
}
trap nettoyer EXIT INT TERM

echo "── Préparation ────────────────────────────────────────────────"
if [[ ! -f model/Qwen3.5-2B-IQ4_XS.gguf ]]; then
  echo "  ✗ les poids sont absents. Lancer d'abord : bash download_model.sh" >&2
  exit 1
fi
echo "  poids présents"

# Ce qui tourne en trop se verra à l'écran et se paiera en vitesse : la machine a
# 8 Go et pas de ventilateur. On avertit, on ne ferme rien à la place de l'humain.
for p in Docker colima ollama node; do
  pgrep -qx "$p" 2>/dev/null && echo "  ⚠️  « $p » tourne : il mange la RAM et la vitesse."
done

if [[ $REPETITION -eq 1 ]]; then
  echo "  mode répétition : ni coupure réseau, ni enregistrement"
  echo
  exec .venv/bin/python demo/tournage.py --repetition
fi

# Le joueur : ce que la fenêtre visible exécutera. Il attend le feu vert pour que
# la capture soit déjà lancée quand le premier caractère s'affiche.
cat > "$ATELIER/jouer.sh" <<JOUEUR
cd "$RACINE"
clear
while [ ! -f "$FEU_VERT" ]; do sleep 0.2; done
clear
.venv/bin/python demo/tournage.py
echo
touch "$FINI"
sleep 2
JOUEUR

# Accolades obligatoires : bash 3.2 (celui de macOS) rattache le « … » multi-octets
# au nom de la variable et échoue sous `set -u`.
echo "  coupure du Wi-Fi sur ${INTERFACE}…"
networksetup -setairportpower "$INTERFACE" off || {
  echo "  ✗ impossible de couper $INTERFACE (essayer : INTERFACE=en1 bash demo/filmer.sh)" >&2
  exit 1
}
sleep 2

echo "  ouverture de la fenêtre de scène…"
ID_FENETRE=$(osascript <<AS
tell application "Terminal"
  activate
  do script "bash '$ATELIER/jouer.sh'"
  delay 0.6
  set font size of current settings of front window to $POLICE
  set bounds of front window to {0, 0, 1440, 900}
  return id of front window
end tell
AS
) || { echo "  ✗ impossible d'ouvrir la fenêtre Terminal" >&2; exit 1; }
sleep 1.5

echo "── Enregistrement ─────────────────────────────────────────────"
echo "  ⚠️  NE PLUS TOUCHER À LA MACHINE pendant ~40 s : tout ce qui passe à"
echo "     l'écran est filmé, y compris un navigateur ou une messagerie."
[[ $VOIX -eq 1 ]] && echo "  micro actif."

# -m écran principal · -k montre les clics · -V garde-fou de durée.
#
# ⚠️ Mesuré le 2 août : screencapture **n'obéit pas** au SIGINT envoyé depuis un
# script. Il tourne jusqu'à son plafond -V, et pendant ce rab il filme tout ce
# qui passe à l'écran — la première prise a ainsi capté un navigateur ouvert sur
# un compte personnel. Deux conséquences, toutes deux appliquées plus bas :
# le plafond est court, et le film est **recoupé à la fin réelle de la scène**.
ARGS=(-v -m -k -V 75)
[[ $VOIX -eq 1 ]] && ARGS+=(-g)
BRUT="${SORTIE%.mov}-brut.mov"
screencapture "${ARGS[@]}" "$BRUT" &
PID_CAPTURE=$!
sleep 2

DEBUT=$(date +%s)
touch "$FEU_VERT"   # la scène commence

# Attendre la fin du jeu, sans jamais bloquer indéfiniment.
for _ in $(seq 1 900); do   # 900 × 0,2 s = 180 s
  [[ -f "$FINI" ]] && break
  sleep 0.2
done
if [[ ! -f "$FINI" ]]; then
  echo "  ✗ la démonstration n'a pas rendu la main en 180 s." >&2
  exit 1
fi

sleep 2   # ne pas couper sur le dernier caractère
UTILE=$(( $(date +%s) - DEBUT + 2 ))   # durée réelle de la scène, plus le battement

# On ne tue pas screencapture, on le laisse atteindre son plafond -V.
# Mesuré le 2 août, dans cet ordre : SIGINT est ignoré (il filme jusqu'au bout),
# et SIGKILL le tue avant qu'il n'ait refermé le conteneur — zéro fichier. Le
# laisser finir est donc la seule voie qui produise un .mov valide.
#
# La fenêtre de scène reste ouverte pendant cette attente, volontairement : ce
# que la caméra filme alors, c'est une démonstration terminée, jamais ce qu'il y
# a derrière. Puis la coupe ffmpeg efface ce rab.
echo "  scène terminée en $((UTILE - 2)) s — la capture se referme, patiente…"
wait "$PID_CAPTURE" 2>/dev/null
PID_CAPTURE=""

osascript -e "tell application \"Terminal\" to close (every window whose id is $ID_FENETRE)" >/dev/null 2>&1
ID_FENETRE=""

echo
if [[ ! -s "$BRUT" ]]; then
  echo "  ✗ aucun fichier produit. Vérifier l'autorisation « Enregistrement de" >&2
  echo "    l'écran » du terminal dans Réglages Système › Confidentialité." >&2
  exit 1
fi

# Le recadrage temporel. `-c copy` ne ré-encode rien : coupe instantanée et texte
# de terminal intact, or le texte est le seul contenu à lire à l'image.
if command -v ffmpeg >/dev/null; then
  ffmpeg -v error -i "$BRUT" -t "$UTILE" -c copy "$SORTIE" -y && rm -f "$BRUT"
else
  mv "$BRUT" "$SORTIE"
  echo "  ⚠️  ffmpeg absent : le film n'a pas été recoupé, vérifie sa fin à la main."
fi

echo "── Prise enregistrée ──────────────────────────────────────────"
echo "  $SORTIE"
command -v ffprobe >/dev/null && ffprobe -v error \
  -show_entries format=duration,size -of default=nw=1 "$SORTIE" | sed 's/^/  /'
echo "  Voix off à poser au montage : demo/NARRATION.md"
