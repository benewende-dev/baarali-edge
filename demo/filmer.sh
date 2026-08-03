#!/usr/bin/env bash
# Enregistre la démonstration de soumission, en une seule prise, sans intervention.
#
# Pourquoi un script et pas trois commandes tapées à la main : la démonstration
# exige que le Wi-Fi soit coupé, or couper le Wi-Fi coupe aussi l'outil qui
# taperait les commandes suivantes. Tout doit donc partir d'un seul appel, et le
# réseau doit revenir tout seul à la fin — y compris si quelque chose échoue.
#
# Usage :
#   bash demo/filmer.sh              # muet ; on ajoute la voix après
#   bash demo/filmer.sh --voix       # capte le micro pendant la prise
#   bash demo/filmer.sh --repetition # ne coupe pas le Wi-Fi, n'enregistre pas
#
# Sortie : demo/prise-AAAAMMJJ-HHMMSS.mov (ignoré par git — un .mov n'a rien à
# faire dans un dépôt de code ; il se téléverse sur Devpost).

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
SORTIE="$RACINE/demo/prise-$(date +%Y%m%d-%H%M%S).mov"
PID_CAPTURE=""

# Le filet. Quoi qu'il arrive — erreur, Ctrl-C, script tué — le Wi-Fi revient et
# l'enregistrement est refermé proprement. Sans ça, un échec au milieu laisse la
# machine hors ligne et le fichier .mov corrompu.
nettoyer() {
  if [[ -n "$PID_CAPTURE" ]] && kill -0 "$PID_CAPTURE" 2>/dev/null; then
    kill -INT "$PID_CAPTURE" 2>/dev/null   # SIGINT : screencapture ferme le fichier
    wait "$PID_CAPTURE" 2>/dev/null
  fi
  if [[ $REPETITION -eq 0 ]]; then
    networksetup -setairportpower "$INTERFACE" on >/dev/null 2>&1
    echo "  réseau rétabli sur $INTERFACE"
  fi
}
trap nettoyer EXIT INT TERM

echo "── Préparation ────────────────────────────────────────────────"
if [[ ! -f model/Qwen3.5-2B-IQ4_XS.gguf ]]; then
  echo "  ✗ les poids sont absents. Lancer d'abord : bash download_model.sh" >&2
  exit 1
fi
echo "  poids présents"

# Ce qui tourne en trop se verra à l'écran et se paiera en vitesse : la machine a
# 8 Go et pas de ventilateur. On avertit, on ne tue rien à la place de l'humain.
for p in Docker colima ollama node; do
  if pgrep -qx "$p" 2>/dev/null; then
    echo "  ⚠️  « $p » tourne. Le fermer avant de filmer : il mange la RAM et la vitesse."
  fi
done

if [[ $REPETITION -eq 1 ]]; then
  echo "  mode répétition : ni coupure réseau, ni enregistrement"
  echo
  exec .venv/bin/python demo/tournage.py --repetition
fi

echo "  coupure du Wi-Fi sur $INTERFACE…"
networksetup -setairportpower "$INTERFACE" off || {
  echo "  ✗ impossible de couper $INTERFACE (essayer INTERFACE=en1 bash demo/filmer.sh)" >&2
  exit 1
}
sleep 2

echo
echo "── Enregistrement dans 3 secondes ─────────────────────────────"
[[ $VOIX -eq 1 ]] && echo "  micro actif : parle par-dessus, la prise est unique."
for n in 3 2 1; do printf "  %d…\n" "$n"; sleep 1; done

# -m : écran principal seulement. -k : montre les clics. -V : garde-fou de durée,
# la prise dure ~30 s et le règlement plafonne à 2 minutes.
ARGS=(-v -m -k -V 180)
[[ $VOIX -eq 1 ]] && ARGS+=(-g)
screencapture "${ARGS[@]}" "$SORTIE" &
PID_CAPTURE=$!
sleep 2   # laisser la capture démarrer avant que quoi que ce soit s'affiche

clear
.venv/bin/python demo/tournage.py
CODE=$?

sleep 2   # ne pas couper sur le dernier caractère
kill -INT "$PID_CAPTURE" 2>/dev/null
wait "$PID_CAPTURE" 2>/dev/null
PID_CAPTURE=""

echo
if [[ -s "$SORTIE" ]]; then
  echo "── Prise enregistrée ──────────────────────────────────────────"
  echo "  $SORTIE"
  command -v ffprobe >/dev/null && ffprobe -v error \
    -show_entries format=duration,size -of default=nw=1 "$SORTIE" | sed 's/^/  /'
else
  echo "  ✗ aucun fichier produit. Vérifier l'autorisation « Enregistrement de" >&2
  echo "    l'écran » du terminal dans Réglages Système › Confidentialité." >&2
  CODE=1
fi

exit $CODE
