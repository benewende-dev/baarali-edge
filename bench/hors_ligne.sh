#!/usr/bin/env bash
# Prouve que l'inférence ne parle à personne.
#
# Le règlement interdit tout appel réseau pendant le profilage, et `CLAUDE.md`
# impose de le **vérifier** plutôt que de le déduire en lisant le code. Deux
# épreuves, de la moins à la plus convaincante :
#
#   1. `--sockets` : lance une inférence et surveille les connexions ouvertes du
#      processus. Non intrusif — se lance à tout moment, y compris pendant
#      qu'autre chose tourne.
#   2. `--sans-wifi` : coupe le Wi-Fi, refait l'inférence, remet le Wi-Fi. C'est
#      la preuve que le jury attend. Le Wi-Fi est rétabli même en cas d'erreur
#      ou d'interruption (trap), parce qu'un script qui laisse la machine hors
#      ligne après un plantage est un piège.
#
# Usage : bash bench/hors_ligne.sh --sockets | --sans-wifi

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODELE="$HERE/model/Qwen3.5-2B-IQ4_XS.gguf"
INVITE="Resume en une phrase : la commande CMD-1042 est en retard de 25 jours."

[[ -f "$MODELE" ]] || { echo "poids absents : $MODELE — lancer download_model.sh" >&2; exit 1; }
command -v llama-cli > /dev/null || { echo "llama-cli absent : brew install llama.cpp" >&2; exit 1; }

# `-st` est indispensable : sans lui, `-no-cnv` génère puis **attend un second
# tour**, et le processus ne rend jamais la main. Constaté à la mesure — un run
# resté 17 minutes en vie pour 48 jetons.
ARGS=(-ngl 0 --temp 0 --repeat-penalty 1.10 -n 48 -no-cnv -st --no-warmup)

inference() {
  llama-cli -m "$MODELE" "${ARGS[@]}" -p "$INVITE" > /dev/null 2>&1 &
  echo $!
}

# Ce qui compte n'est pas « une socket existe » mais « une socket sort de la
# machine ». Mesuré : `llama-cli` ouvre systématiquement une paire de sockets en
# **boucle locale** (127.0.0.1 qui se connecte à lui-même), un réveil de threads
# interne. Un contrôle naïf « toute socket = échec » nous recalerait à tort, et
# recalerait aussi toute autre soumission llama.cpp. Le critère juste est
# l'absence d'adresse **non locale**.
LOCALES='127\.0\.0\.1|\[::1\]|localhost'

epreuve_sockets() {
  echo "→ inférence sous surveillance des sockets…"
  local pid; pid="$(inference)"
  local externes=0 locales=0 n=0 vues dehors
  while kill -0 "$pid" 2> /dev/null; do
    # -i : sockets réseau uniquement. -nP : pas de résolution DNS ni de noms de
    # services — sans ça `lsof` met plusieurs secondes par appel et le sondage
    # coûte plus cher que l'inférence qu'il observe.
    # `|| true` : lsof sort en erreur quand il ne trouve **rien**, c'est-à-dire
    # précisément dans le cas favorable. Sans ça, `set -e` tue le script au
    # premier relevé propre — le test échouait quand tout allait bien.
    vues="$(lsof -nP -i -a -p "$pid" 2> /dev/null | tail -n +2 || true)"
    if [[ -n "$vues" ]]; then
      locales=$((locales + 1))
      dehors="$(grep -Ev "$LOCALES" <<< "$vues" || true)"
      if [[ -n "$dehors" ]]; then
        echo "  ⚠️  socket NON locale :"
        sed 's/^/     /' <<< "$dehors"
        externes=$((externes + 1))
      fi
    fi
    n=$((n + 1))
    sleep 0.5
  done
  wait "$pid" 2> /dev/null || true
  echo "  $n relevés, dont $locales avec des sockets ouvertes (toutes examinées)."
  if [[ "$externes" -eq 0 ]]; then
    echo "  ✅ aucune socket vers une adresse extérieure à la machine."
    [[ "$locales" -gt 0 ]] && echo "     (des sockets en boucle locale existent : réveil de threads interne à llama.cpp)"
  else
    echo "  ❌ $externes relevés avec une socket non locale." >&2
    return 1
  fi
}

# `interface` est **volontairement globale**. La première version la déclarait
# `local` à la fonction : le `trap EXIT` s'exécutant *après* la sortie de la
# fonction, la variable n'existait plus au moment précis où le filet devait
# servir, et le Wi-Fi restait coupé. Un garde-fou qui ne tient pas au moment de
# l'accident n'est pas un garde-fou. Constaté en vrai, sur cette machine.
interface=""

retablir_wifi() {
  [[ -n "$interface" ]] || return 0
  echo "→ rétablissement du Wi-Fi (${interface})…"
  networksetup -setairportpower "$interface" on
  # Vérifier, pas espérer : si la remise en route a échoué, il faut le voir.
  sleep 2
  networksetup -getairportpower "$interface"
}

epreuve_sans_wifi() {
  interface="$(networksetup -listallhardwareports \
    | awk '/Wi-Fi|AirPort/{getline; print $2; exit}')"
  [[ -n "$interface" ]] || { echo "interface Wi-Fi introuvable" >&2; exit 1; }

  # Le Wi-Fi revient quoi qu'il arrive : succès, échec, ou Ctrl-C.
  trap retablir_wifi EXIT INT TERM

  # Accolades obligatoires : sans elles, bash agrège le caractère « … » qui suit
  # au nom de la variable et échoue sur « interface… : unbound variable ».
  echo "→ coupure du Wi-Fi sur ${interface}…"
  networksetup -setairportpower "$interface" off
  sleep 2

  if ping -c 1 -t 3 1.1.1.1 > /dev/null 2>&1; then
    echo "  ⚠️  la machine répond encore au réseau (Ethernet ? partage de connexion ?)" >&2
    echo "     L'épreuve n'est pas concluante dans cet état." >&2
    return 1
  fi
  echo "  réseau injoignable, confirmé par ping."

  echo "→ inférence hors ligne…"
  local debut; debut="$(date +%s)"
  llama-cli -m "$MODELE" "${ARGS[@]}" -p "$INVITE" 2> /dev/null | tail -6
  echo "  ✅ réponse produite en $(( $(date +%s) - debut )) s, sans réseau."
}

case "${1:-}" in
  --sockets)   epreuve_sockets ;;
  --sans-wifi) epreuve_sans_wifi ;;
  *) echo "usage: bash bench/hors_ligne.sh --sockets | --sans-wifi" >&2; exit 2 ;;
esac
