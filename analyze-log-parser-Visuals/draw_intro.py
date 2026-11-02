#!/usr/bin/env python3
"""analyze-log-parser intro: eclipse expedition camp before totality, no readable mark anywhere.
Foreground observing table with a blank ruled ledger and a pencil in its gutter, a row of brass
telescopes in the midground, tents, unmarked crates, a slack windsock, first stars overhead."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter
random.seed(410)
V1 = "--v1" in sys.argv
W, H = 1200, 520
SLATE = (52, 63, 76); CREAM = (242, 234, 214); BRASS = (176, 141, 62); SAND = (198, 180, 140)
img = Image.new("RGB", (W, H), SLATE); d = ImageDraw.Draw(img, "RGBA")
# sky deepening from cloud cream near the ground to slate overhead
for y in range(0, 386):
    t = y / 386
    col = tuple(int(CREAM[i] + (SLATE[i] - CREAM[i]) * (1 - t) ** 1.6) for i in range(3))
    d.line([(0, y), (W, y)], fill=col)
# first stars in the upper slate
for _ in range(90):
    x, y = random.uniform(0, W), random.uniform(0, 150); r = random.uniform(.6, 1.8)
    d.ellipse([x - r, y - r, x + r, y + r], fill=(250, 248, 238, random.randint(90, 200)))
# flat desert to a low dark horizon
d.rectangle([0, 384, W, H], fill=SAND)
d.line([(0, 384), (W, 384)], fill=(70, 74, 78), width=3)
for _ in range(1100):
    x, y = random.uniform(0, W), random.uniform(388, H)
    d.point((x, y), fill=random.choice([(178, 158, 116), (214, 198, 158), (160, 142, 104)]))
# canvas tents closing the middle ground, slate and sand tones
def tent(x, base, w, h, col):
    d.polygon([(x, base), (x + w / 2, base - h), (x + w, base)], fill=col)
    d.polygon([(x + w / 2, base - h), (x + w, base), (x + w * .82, base)], fill=tuple(max(0, c - 26) for c in col))
    d.line([(x + w / 2, base - h), (x + w / 2, base)], fill=(60, 58, 52), width=2)
tent(96, 388, 210, 104, (96, 108, 120)); tent(872, 388, 240, 116, (206, 190, 148)); tent(700, 386, 150, 76, (120, 128, 138))
# stacked crates shown from their unmarked sides
for (x, y, s) in [(408, 330, 58), (408, 386 - 58, 58), (470, 344, 44)]:
    d.rectangle([x, y, x + s, y + s * .72], fill=(168, 138, 96), outline=(120, 96, 62), width=2)
    d.line([(x, y), (x + s, y + s * .72)], fill=(140, 112, 76), width=2)
# the row of mounted telescopes, every tube tipped to the same point in the darkening sky
def telescope(x, base, scale):
    tube_col = BRASS if not V1 else (150, 128, 84)
    lw = 7 if not V1 else 3
    # wooden tripod
    d.line([(x, base - 52 * scale), (x - 26 * scale, base)], fill=(110, 80, 48), width=4)
    d.line([(x, base - 52 * scale), (x + 26 * scale, base)], fill=(110, 80, 48), width=4)
    d.line([(x, base - 52 * scale), (x + 4 * scale, base)], fill=(96, 68, 40), width=4)
    # brass tube aimed up and to the right
    x2, y2 = x + 62 * scale, base - 118 * scale
    d.line([(x - 14 * scale, base - 40 * scale), (x2, y2)], fill=tube_col, width=int(13 * scale))
    d.line([(x - 14 * scale, base - 40 * scale), (x2, y2)], fill=(214, 182, 104), width=int(4 * scale))
    d.ellipse([x2 - 8 * scale, y2 - 8 * scale, x2 + 8 * scale, y2 + 8 * scale], fill=(40, 46, 54), outline=BRASS, width=2)
    d.line([(x - 22 * scale, base - 30 * scale), (x - 34 * scale, base - 16 * scale)], fill=tube_col, width=lw)
for (x, s) in [(210, .8), (330, .92), (560, .92), (660, .8)]:
    telescope(x, 392, s)
# windsock pole at the camp edge, the sock hanging nearly still
d.line([(1078, 268), (1078, 392)], fill=(74, 66, 58), width=4)
d.polygon([(1078, 272), (1116, 284), (1108, 322), (1078, 306)], fill=(206, 120, 62))
d.polygon([(1078, 272), (1116, 284), (1112, 296), (1078, 288)], fill=(238, 232, 216))
# foreground: the observing table at close range
d.polygon([(180, 452), (1020, 452), (1120, 520), (80, 520)], fill=(122, 92, 58))
d.polygon([(180, 452), (1020, 452), (1046, 470), (154, 470)], fill=(146, 112, 72))
# brass telescope foot and its long shadow at the left of the table
d.ellipse([196, 470, 268, 492], fill=(60, 54, 44, 120))
d.polygon([(214, 446), (246, 446), (258, 478), (202, 478)], fill=BRASS)
d.ellipse([200, 472, 260, 484], fill=(140, 110, 52))
# blank open ledger: ruled lines only, a pencil resting in the gutter
d.polygon([(430, 458), (598, 458), (606, 512), (424, 512)], fill=(246, 240, 222))
d.polygon([(598, 458), (772, 458), (786, 512), (606, 512)], fill=(240, 233, 212))
d.line([(598, 458), (606, 512)], fill=(178, 168, 146), width=3)
rule_col = (90, 96, 108) if V1 else (196, 190, 172)
rule_w = 2 if V1 else 1
for i in range(5):
    y = 470 + i * 9
    d.line([(442, y), (588, y + 2)], fill=rule_col, width=rule_w)
    d.line([(616, y), (762, y + 2)], fill=rule_col, width=rule_w)
d.line([(596, 466), (610, 504)], fill=(226, 178, 84), width=4)  # pencil in the gutter
d.polygon([(610, 504), (613, 512), (606, 508)], fill=(70, 62, 54))
# lens caps kept out of the dust
for (x, y, r) in [(842, 486, 17), (884, 494, 13)]:
    d.ellipse([x - r, y - r * .4, x + r, y + r * .4], fill=(42, 48, 56), outline=BRASS, width=2)
img = img.filter(ImageFilter.GaussianBlur(0.4))
out = "scratch/intro-v1.png" if V1 else "intro-banner.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)
