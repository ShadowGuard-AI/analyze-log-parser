#!/usr/bin/env python3
"""analyze-log-parser logo: a hand drawn corona at totality on a faint ledger rule, slate disc,
uneven rays of cloud cream and brass, the name lettered in Cabin Sketch in slate below."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(97)
V1 = "--v1" in sys.argv
W, H = 900, 560
CREAM = (243, 236, 218); SLATE = (52, 63, 76); BRASS = (176, 141, 62)
img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img, "RGBA")
# faint ledger rules across the paper
for y in range(36, H, 34):
    d.line([(24, y), (W - 24, y)], fill=(206, 198, 176), width=1)
cx, cy, R = 450, 238, 104
# corona rays first, so the disc sits over their roots; no ray repeated
lengths = [168, 132, 190, 118, 156, 200, 126, 172, 140, 186, 122, 160, 196, 134, 148, 178, 116, 166, 142, 188, 128, 154, 174, 120]
for i, ang in enumerate(range(0, 360, 15)):
    a = math.radians(ang + random.uniform(-3, 3))
    ln = 150 if V1 else lengths[i % len(lengths)]  # v1 flaw: every ray the same length, a tidy sun icon
    col = (250, 246, 230) if i % 3 else BRASS
    wdt = 7 if i % 3 else 4
    x2, y2 = cx + math.cos(a) * ln, cy + math.sin(a) * ln
    x1, y1 = cx + math.cos(a) * (R - 8), cy + math.sin(a) * (R - 8)
    d.line([(x1, y1), (x2, y2)], fill=col, width=wdt)
    d.line([(x1, y1), (cx + math.cos(a) * (ln * .55), cy + math.sin(a) * (ln * .55))], fill=(250, 246, 230), width=3)
# the occulted sun: a solid slate disc, slightly off a perfect circle as a three minute sketch would be
pts = []
for ang in range(0, 360, 6):
    a = math.radians(ang); rr = R + math.sin(ang * 2.7) * 3 + random.uniform(-1.6, 1.6)
    pts.append((cx + math.cos(a) * rr, cy + math.sin(a) * rr))
d.polygon(pts, fill=SLATE)
d.arc([cx - R + 10, cy - R + 12, cx + R - 14, cy + R - 10], 200, 330, fill=(84, 96, 110), width=3)
try:
    f = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/CabinSketch-Bold.ttf", 47)
except Exception:
    f = ImageFont.load_default()
d.text((450, 462), "analyze-log-parser", font=f, fill=SLATE, anchor="mm")
img = img.filter(ImageFilter.GaussianBlur(0.3))
out = "scratch/logo-v1.png" if V1 else "logo.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out)
if not V1:
    img.resize((64, 64)).save(__file__.rsplit("/", 1)[0] + "/scratch/logo64-ship.png")
print("saved", out)
