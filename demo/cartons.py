#!/usr/bin/env python3
"""Deux cartons de fin, au format et aux couleurs exacts du terminal filmé.

Pourquoi des cartons plutôt qu'une image figée : la voix off dure ~84 s quand la
prise en dure 32, et le règlement réclame le *development journey*, qui ne se
filme pas. Tenir la dernière image pendant les 27 dernières secondes serait mou ;
ces deux écrans disent ce que la voix raconte, dans la même typographie, donc
sans rupture visuelle.

Tout est en Menlo **Regular** : le Bold du même fichier n'a pas le glyphe de
trait horizontal (U+2500) et le remplace par un carré vide — mesuré, pas supposé.
Le gras du titre est refait à la main par un second tracé décalé d'un pixel.
"""
from PIL import Image, ImageDraw, ImageFont

FOND = (29, 35, 45)  # relevé au pixel sur la prise, pas choisi
BLANC, GRIS, VERT, VIF = (220, 223, 228), (120, 130, 142), (152, 195, 121), (245, 246, 248)
L, H = 2880, 1800
CORPS = 46
MARGE_X, INTERLIGNE = 200, 76

police = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", CORPS, index=0)


def carton(lignes, sortie):
    im = Image.new("RGB", (L, H), FOND)
    d = ImageDraw.Draw(im)
    y = (H - len(lignes) * INTERLIGNE) // 2  # bloc centré, pas collé en haut
    for texte, couleur, gras in lignes:
        d.text((MARGE_X, y), texte, font=police, fill=couleur)
        if gras:
            d.text((MARGE_X + 2, y), texte, font=police, fill=couleur)
        y += INTERLIGNE
    im.save(sortie)
    print(f"  ✓ {sortie}")


carton([
    ("── 5. How we got here " + "─" * 36, VIF, True),
    ("", BLANC, False),
    ("   5  open base models profiled       0.75 B  →  4.21 B", BLANC, False),
    ("   7  quantisations of the winner     Q2_K    →  Q8_0", BLANC, False),
    ("   1  published decision reversed     after a second control", BLANC, False),
    ("", BLANC, False),
    ("  The first control was rigorous, documented, and off-topic:", GRIS, False),
    ("  it measured arithmetic, and our domain is summarisation,", GRIS, False),
    ("  drafting and analysis. We measured again, and reversed.", GRIS, False),
    ("", BLANC, False),
    ("  A measured number is only worth the question you asked it.", VERT, False),
], "carton5.png")

carton([
    ("── Baarali Edge " + "─" * 42, VIF, True),
    ("", BLANC, False),
    ("  Qwen3.5-2B  ·  IQ4_XS  ·  1.88 B parameters", BLANC, False),
    ("  corporate_enterprise  ·  French and English  ·  offline", BLANC, False),
    ("", BLANC, False),
    ("  github.com/benewende-dev/baarali-edge", BLANC, False),
    ("  huggingface.co/Benewende-dev/baarali-edge-2b", BLANC, False),
    ("", BLANC, False),
    ("  Every number in the report is measured, including the", GRIS, False),
    ("  ones that do not flatter us: the report names the", GRIS, False),
    ("  quantisation that beats ours on accuracy.", GRIS, False),
    ("", BLANC, False),
    ("  A model that fits an 8 GB laptop, and calls nobody.", VERT, False),
], "carton6.png")
