#!/usr/bin/env python3
"""analyze-log-parser wordmark banner: desert observing camp in the last light before totality.
The name is written once only, in Cabin Sketch in dark pencil across the open ledger page in
the foreground. Crates carry packing marks that cannot be read as words."""
import random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(233)
V1 = "--v1" in sys.argv
V2 = "--v2" in sys.argv
W, H = 1200, 520
SLATE = (58, 68, 82); CREAM = (244, 236, 216); BRASS = (176, 141, 62); SAND = (200, 182, 142)
img = Image.new("RGB", (W, H), SLATE); d = ImageDraw.Draw(img, "RGBA")
for y in range(0, 372):
    t = y / 372
    warm = (226, 196, 152)
    col = tuple(int(warm[i] + (SLATE[i] - warm[i]) * (1 - t) ** 1.5) for i in range(3))
    d.line([(0, y), (W, y)], fill=col)
for _ in range(46):
    x, y = random.uniform(0, W), random.uniform(0, 110); r = random.uniform(.6, 1.6)
    d.ellipse([x - r, y - r, x + r, y + r], fill=(250, 248, 238, 130))
d.rectangle([0, 370, W, H], fill=SAND)
d.line([(0, 370), (W, 370)], fill=(74, 76, 80), width=3)
for _ in range(800):
    x, y = random.uniform(0, W), random.uniform(374, H)
    d.point((x, y), fill=random.choice([(180, 160, 118), (216, 200, 160)]))
def tent(x, base, w, h, col):
    d.polygon([(x, base), (x + w / 2, base - h), (x + w, base)], fill=col)
    d.polygon([(x + w / 2, base - h), (x + w, base), (x + w * .8, base)], fill=tuple(max(0, c - 24) for c in col))
tent(60, 376, 220, 112, (100, 112, 124)); tent(920, 376, 250, 122, (208, 192, 150))
# crates behind the instruments, stencilled only with marks that cannot be read as words
for (x, y, s) in [(770, 300, 72), (770, 372 - 72, 72), (846, 322, 52), (298, 322, 52)]:
    d.rectangle([x, y, x + s, y + s * .74], fill=(170, 140, 98), outline=(122, 98, 64), width=2)
    d.line([(x, y), (x + s, y + s * .74)], fill=(142, 114, 78), width=2)
    if V1:  # v1 flaw: the marks resolve into letter-like strokes, a second place that can be read
        for k in range(3):
            d.line([(x + 10 + k * 14, y + 16), (x + 10 + k * 14, y + 34)], fill=(70, 60, 48), width=3)
            d.line([(x + 10 + k * 14, y + 16), (x + 18 + k * 14, y + 16)], fill=(70, 60, 48), width=3)
    else:  # soft smudge marks only
        for k in range(4):
            d.line([(x + 9 + k * 11, y + 20), (x + 16 + k * 11, y + 24)], fill=(120, 100, 72), width=3)
# brass telescopes in a row on wooden tripods, tubes tipped toward the thinning sky
def telescope(x, base, scale):
    d.line([(x, base - 54 * scale), (x - 27 * scale, base)], fill=(110, 80, 48), width=4)
    d.line([(x, base - 54 * scale), (x + 27 * scale, base)], fill=(110, 80, 48), width=4)
    d.line([(x, base - 54 * scale), (x + 4 * scale, base)], fill=(96, 68, 40), width=4)
    x2, y2 = x + 66 * scale, base - 124 * scale
    d.line([(x - 15 * scale, base - 42 * scale), (x2, y2)], fill=BRASS, width=int(14 * scale))
    d.line([(x - 15 * scale, base - 42 * scale), (x2, y2)], fill=(216, 184, 106), width=int(4 * scale))
    d.ellipse([x2 - 8 * scale, y2 - 8 * scale, x2 + 8 * scale, y2 + 8 * scale], fill=(40, 46, 54), outline=BRASS, width=2)
for (x, s) in [(180, .86), (310, 1.0), (470, 1.0), (590, .86)]:
    telescope(x, 382, s)
# windsock on a pole at the camp edge, hanging nearly still
d.line([(1128, 252), (1128, 378)], fill=(74, 66, 58), width=4)
d.polygon([(1128, 256), (1164, 268), (1156, 306), (1128, 290)], fill=(206, 120, 62))
d.polygon([(1128, 256), (1164, 268), (1160, 280), (1128, 272)], fill=(238, 232, 216))
# foreground table with the open expedition ledger, a corona sketch half finished on its page
d.polygon([(240, 428), (960, 428), (1050, 520), (150, 520)], fill=(124, 94, 60))
d.polygon([(240, 428), (960, 428), (982, 446), (218, 446)], fill=(148, 114, 74))
lx0, ly0, lx1, ly1 = (372, 436, 828, 516) if not V1 else (430, 444, 770, 510)
d.polygon([(lx0, ly0), ((lx0 + lx1) // 2, ly0 - 4), ((lx0 + lx1) // 2, ly1), (lx0, ly1)], fill=(247, 241, 224))
d.polygon([((lx0 + lx1) // 2, ly0 - 4), (lx1, ly0), (lx1 + 8, ly1), ((lx0 + lx1) // 2, ly1)], fill=(241, 234, 213))
d.line([((lx0 + lx1) // 2, ly0 - 4), ((lx0 + lx1) // 2, ly1)], fill=(178, 168, 146), width=3)
for i in range(4):
    y = ly0 + 14 + i * 13
    d.line([(lx0 + 16, y), ((lx0 + lx1) // 2 - 14, y + 2)], fill=(198, 192, 174), width=1)
    d.line([((lx0 + lx1) // 2 + 14, y), (lx1 - 8, y + 2)], fill=(198, 192, 174), width=1)
# half finished corona sketch on the right page
ccx, ccy = lx1 - 64, ly0 + 22
d.ellipse([ccx - 12, ccy - 12, ccx + 12, ccy + 12], outline=(92, 96, 104), width=2)
for a in range(0, 360, 45):
    import math
    x2, y2 = ccx + math.cos(math.radians(a)) * 21, ccy + math.sin(math.radians(a)) * 21
    d.line([(ccx + math.cos(math.radians(a)) * 14, ccy + math.sin(math.radians(a)) * 14), (x2, y2)], fill=(150, 128, 74), width=2)
try:
    f = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/CabinSketch.ttf", 30 if V1 else 37)
except Exception:
    f = ImageFont.load_default()
# the one inscription in the scene: the name across the open ledger page, in dark pencil
# v2 flaw: the inscription rides high and crowds the corona sketch; the ship draft lowers it clear
ty = ly0 + 15 if V2 else ly0 + 62
d.text(((lx0 + lx1) // 2, ty), "analyze-log-parser", font=f, fill=(62, 60, 66), anchor="mm")
# pencils and a covered lens cap kept out of the dust
d.line([(lx0 - 52, 486), (lx0 + 6, 474)], fill=(226, 178, 84), width=4)
d.ellipse([872, 478, 920, 494], fill=(42, 48, 56), outline=BRASS, width=2)
img = img.filter(ImageFilter.GaussianBlur(0.4))
out = "scratch/banner-v1.png" if V1 else ("scratch/banner-v2.png" if V2 else "banner.png")
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)
