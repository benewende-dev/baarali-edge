#!/usr/bin/env python3
"""Le canal USSD : la même réponse, atteignable sans forfait de données.

Ce que ce fichier démontre
--------------------------
Le modèle vit dans la mémoire du portable. L'ordinateur sert le bureau — mais
pas le chauffeur, ni le magasinier, ni l'agent de terrain, qui sont pourtant
ceux qui produisent les événements que le bureau doit connaître.

Le canal qui les atteint déjà, c'est **l'USSD** : les codes `*123#` qui
fonctionnent sur n'importe quel combiné, sans application, sans forfait de
données et sans navigateur. Ce n'est pas une hypothèse sur les usages : c'est
le rail financier de la sous-région — plus de 22 millions de comptes de monnaie
électronique actifs en Côte d'Ivoire en 2024. Voir `USE_CASE.md`.

Ce qui est réel ici, et ce qui ne l'est pas
-------------------------------------------
**Réel** : le contrat d'échange. `repondre()` implémente exactement le rappel
que publient les agrégateurs de la sous-région — quatre champs en entrée
(`sessionId`, `serviceCode`, `phoneNumber`, `text`, l'historique de la session
étant concaténé par des `*`), et une réponse en texte brut préfixée par `CON `
(la session continue) ou `END ` (elle se termine). Le même code répond donc à un
agrégateur sans être modifié.

**Réel aussi** : la contrainte d'écran. Un message USSD ne dépasse pas
**182 caractères**, préfixe compris. Ce n'est pas un détail de présentation :
c'est ce qui dicte la consigne donnée au modèle et le budget de jetons. Le
serveur *refuse* d'émettre un écran trop long plutôt que de laisser l'opérateur
le tronquer au hasard.

**Pas réel** : le numéro court. Un `*123#` en production exige une convention
avec un opérateur ivoirien — des semaines de démarches et un contrat commercial.
Nous ne prétendons donc à aucun code court en service. Le mode `--telephone`
rejoue une session en local, sur la machine, **réseau coupé** : c'est la
démonstration honnête de ce que nous pouvons montrer.

Usage
-----
    .venv/bin/python demo/ussd.py --telephone     # simulateur de combiné, hors ligne
    .venv/bin/python demo/ussd.py --serveur       # rappel HTTP compatible agrégateur
"""
from __future__ import annotations

import argparse
import json
import sys
import textwrap
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "bench"))

from mesurer import CANDIDATS, POIDS  # noqa: E402

LABEL = "q2b-iq4xs"
CODE_SERVICE = "*384*2273#"  # 2273 = « BARA » sur un clavier téléphonique

# Limite d'un écran USSD, préfixe « CON »/« END » compris. Contrainte du réseau,
# pas un choix de mise en page.
ECRAN_MAX = 182

# La pénalité de répétition retenue à l'issue de `bench/penalite.py`. Elle compte
# doublement ici : hors ligne et sans écran de secours, une boucle n'est pas une
# réponse laide, c'est une session perdue et du crédit dépensé pour rien.
PENALITE = 1.10

# Le modèle doit tenir dans un écran. On le lui dit, et on vérifie ensuite —
# une consigne n'est pas une garantie.
CONSIGNE = (
    "Tu es l'assistant d'une PME ivoirienne, joignable par USSD sur un téléphone. "
    "Réponds en français, en moins de 150 caractères, sans formatage, sans liste, "
    "sans emoji. Une seule phrase. Si tu ne sais pas, dis-le en une phrase."
)

# Les données de l'entreprise restent sur la machine : c'est tout l'argument.
# Un fichier plat suffit à le montrer, et se lit sans base de données.
COMMANDES = RACINE / "demo" / "commandes.json"


def _tronquer(texte: str, limite: int) -> str:
    """Coupe à la limite, sur une frontière de mot, sans jamais la dépasser.

    Les retours à la ligne sont **conservés** : sur un combiné, un menu USSD
    s'affiche une entrée par ligne, et les aplatir en un paragraphe donnerait
    une démonstration qui ne ressemble pas à ce que l'utilisateur voit.
    """
    texte = "\n".join(" ".join(l.split()) for l in texte.split("\n")).strip()
    if len(texte) <= limite:
        return texte
    coupe = texte[: limite - 1].rsplit(" ", 1)[0]
    return (coupe or texte[: limite - 1]) + "…"


def ecran(prefixe: str, corps: str) -> str:
    """Assemble un écran USSD valide. Émettre plus long serait mentir sur le canal."""
    assert prefixe in ("CON", "END")
    return f"{prefixe} " + _tronquer(corps, ECRAN_MAX - 4)


class Assistant:
    """Le modèle local. Chargé une fois, jamais interrogé à distance."""

    def __init__(self, label: str = LABEL) -> None:
        from llama_cpp import Llama

        poids = POIDS / label / CANDIDATS[label]["fichier"]
        if not poids.exists():
            raise SystemExit(f"poids absents : {poids}")
        # n_ctx modeste : c'est celui du profileur officiel, donc celui dans
        # lequel le modèle est jugé. On démontre ce qui est mesuré.
        self.llm = Llama(model_path=str(poids), n_ctx=2048, verbose=False)

    def repondre(self, question: str, contexte: str = "") -> str:
        invite = f"{contexte}\n\n{question}" if contexte else question
        out = self.llm.create_chat_completion(
            messages=[
                {"role": "system", "content": CONSIGNE},
                {"role": "user", "content": invite},
            ],
            max_tokens=96,  # 150 caractères tiennent largement dessous
            temperature=0.0,
            repeat_penalty=PENALITE,
        )
        return (out["choices"][0]["message"].get("content") or "").strip()


def charger_commandes() -> dict[str, dict]:
    if COMMANDES.exists():
        return json.loads(COMMANDES.read_text())
    return {}


def repondre(
    session_id: str,
    service_code: str,
    phone_number: str,
    text: str,
    assistant: Assistant,
) -> str:
    """Le rappel USSD. Signature et format de retour d'un agrégateur standard.

    `text` porte tout l'historique de la session, les saisies séparées par `*` —
    c'est le protocole, et c'est aussi pourquoi il n'y a pas d'état à conserver
    côté serveur : la session **est** la chaîne reçue.
    """
    etapes = text.split("*") if text else [""]

    if etapes == [""]:
        return ecran(
            "CON",
            "Baarali Edge\n1. Etat d'une commande\n2. Signaler une livraison\n"
            "3. Poser une question",
        )

    choix = etapes[0]

    if choix == "1":
        if len(etapes) == 1:
            return ecran("CON", "Numero de commande :")
        cmd = charger_commandes().get(etapes[1].strip().upper())
        if not cmd:
            return ecran("END", f"Commande {etapes[1]} introuvable.")
        return ecran(
            "END",
            f"{cmd['client']} — {cmd['montant_fcfa']} FCFA HT. "
            f"Livraison prevue {cmd['echeance']}. Statut : {cmd['statut']}.",
        )

    if choix == "2":
        if len(etapes) == 1:
            return ecran("CON", "Numero de commande livree :")
        if len(etapes) == 2:
            return ecran("CON", "1. Livree complete\n2. Livree partielle\n3. Refusee")
        etat = {"1": "complete", "2": "partielle", "3": "refusee"}.get(etapes[2], "?")
        return ecran(
            "END",
            f"Livraison {etapes[1]} enregistree : {etat}. "
            f"Signale par {phone_number}. Le bureau est informe.",
        )

    if choix == "3":
        if len(etapes) == 1:
            return ecran("CON", "Votre question :")
        question = "*".join(etapes[1:]).strip()
        return ecran("END", assistant.repondre(question) or "Pas de reponse.")

    return ecran("END", "Choix invalide.")


# --------------------------------------------------------------------------
# Mode « téléphone » : une session rejouée en local, réseau coupé.
# --------------------------------------------------------------------------

CADRE = 30  # largeur de l'écran dessiné, en caractères


def _dessiner(contenu: str) -> None:
    print("\n    ┌" + "─" * CADRE + "┐")
    for ligne in contenu.split("\n"):
        for morceau in textwrap.wrap(ligne, CADRE - 2) or [""]:
            print(f"    │ {morceau.ljust(CADRE - 2)} │")
    print("    └" + "─" * CADRE + "┘")


def telephone(assistant: Assistant) -> int:
    session, numero, text = "sess-0001", "+2250700000000", ""
    print(f"\n  Composez {CODE_SERVICE} puis Appel.")
    print("  (Ctrl-C pour raccrocher)\n")
    while True:
        reponse = repondre(session, CODE_SERVICE, numero, text, assistant)
        prefixe, corps = reponse[:3], reponse[4:]
        _dessiner(corps)
        print(f"    {len(reponse)}/{ECRAN_MAX} caracteres")
        if prefixe == "END":
            print("\n  Session terminee.\n")
            return 0
        try:
            saisie = input("\n    Repondre : ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Raccroche.\n")
            return 0
        text = f"{text}*{saisie}" if text else saisie


# --------------------------------------------------------------------------
# Mode « serveur » : le rappel HTTP qu'un agrégateur appellerait.
# --------------------------------------------------------------------------


def serveur(assistant: Assistant, port: int = 8088) -> int:
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs

    class Rappel(BaseHTTPRequestHandler):
        def do_POST(self) -> None:  # noqa: N802 — nom imposé par la bibliothèque
            taille = int(self.headers.get("Content-Length", 0))
            champs = parse_qs(self.rfile.read(taille).decode())
            corps = repondre(
                champs.get("sessionId", [""])[0],
                champs.get("serviceCode", [CODE_SERVICE])[0],
                champs.get("phoneNumber", [""])[0],
                champs.get("text", [""])[0],
                assistant,
            ).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(corps)))
            self.end_headers()
            self.wfile.write(corps)

        def log_message(self, *_: object) -> None:
            pass  # le journal par défaut parasite la démonstration filmée

    print(f"  Rappel USSD sur http://127.0.0.1:{port}/  (Ctrl-C pour arrêter)")
    HTTPServer(("127.0.0.1", port), Rappel).serve_forever()
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--telephone", action="store_true", help="simulateur de combiné")
    ap.add_argument("--serveur", action="store_true", help="rappel HTTP")
    ap.add_argument("--port", type=int, default=8088)
    args = ap.parse_args()
    if not (args.telephone or args.serveur):
        ap.error("choisir --telephone ou --serveur")
    assistant = Assistant()
    return serveur(assistant, args.port) if args.serveur else telephone(assistant)


if __name__ == "__main__":
    raise SystemExit(main())
