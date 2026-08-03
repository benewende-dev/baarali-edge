#!/usr/bin/env python3
"""Fabrique les sous-titres anglais de la vidéo, à partir du texte réellement dit.

Pourquoi ne pas laisser les sous-titres automatiques faire le travail : ils
transcrivent ce qu'ils croient entendre. « IQ4_XS », « Qwen », « USSD » et
« adtc-profiler » n'ont aucune chance, et un jury qui lit « I Q four X S » sur
une soumission dont l'argument est la précision, c'est un mauvais moment.

Ici la source n'est pas une transcription : ce sont les fichiers `segN.txt` qui
ont été envoyés au moteur de synthèse. Le texte est donc exact par construction.

Chaque segment est découpé en phrases, et la durée du segment répartie entre
elles au prorata de leur longueur — approximation assumée : la diction est
régulière, et un décalage de quelques dixièmes sur un sous-titre ne se voit pas.

Usage : python demo/sous-titres.py demo/voix > demo/sous-titres.srt
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

# Instant où commence chaque segment dans la vidéo montée = cumul des durées de
# plan calculées par `montage.sh`. À régénérer si la narration change.
DEPARTS = [0.0, 8.4, 22.7, 38.4, 57.0, 72.9]


def duree(f: pathlib.Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(f)],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


def horodatage(t: float) -> str:
    h, reste = divmod(t, 3600)
    m, s = divmod(reste, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}".replace(".", ",")


def main() -> int:
    dossier = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "demo/voix")
    n = 0
    for i, depart in enumerate(DEPARTS, 1):
        texte = (dossier / f"seg{i}.txt").read_text().strip()
        total = duree(dossier / f"seg{i}.mp3")

        # Découpe sur la ponctuation forte, en la gardant collée à la phrase.
        phrases = [p.strip() for p in re.split(r"(?<=[.:;?!])\s+", texte) if p.strip()]
        longueur = sum(len(p) for p in phrases)

        t = depart
        for p in phrases:
            d = total * len(p) / longueur
            n += 1
            print(n)
            print(f"{horodatage(t)} --> {horodatage(t + d)}")
            print(p)
            print()
            t += d
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
