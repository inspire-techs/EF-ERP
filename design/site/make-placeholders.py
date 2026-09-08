#!/usr/bin/env python3
"""Generate the placeholder photographs for the home page.

Every image host is blocked from this environment and EF has not supplied
photographs yet, so these are generated: heavily defocused compositions in the
brand palette, which read as out-of-focus event photography rather than as grey
boxes. Each is labelled "placeholder" in the layout.

Replacing one is a file swap — same filename, same aspect, done.
Run:  python3 make-placeholders.py
"""
import math, random, pathlib
from PIL import Image, ImageDraw, ImageFilter, ImageChops

OUT = pathlib.Path(__file__).parent / 'images'
OUT.mkdir(exist_ok=True)

# palettes keyed to what each photograph will eventually show
PALETTES = {
    'cultural': [(94, 32, 54), (140, 52, 80), (201, 120, 148), (247, 214, 224), (58, 16, 31)],
    'cricket':  [(74, 174, 70), (37, 105, 31), (168, 214, 152), (226, 240, 210), (21, 63, 18)],
    'seminar':  [(150, 112, 126), (92, 56, 68), (206, 176, 186), (240, 226, 231), (61, 34, 44)],
    'meeting':  [(46, 122, 43), (21, 63, 18), (150, 190, 132), (233, 241, 250), (30, 51, 25)],
    'portrait': [(140, 52, 80), (94, 32, 54), (206, 176, 186), (247, 240, 242), (58, 16, 31)],
}

# scene: (bands, blobs, horizon) — bands give outdoor scenes a ground/sky split
SCENES = {
    'cultural': dict(blobs=34, horizon=None, glow=True,  figures=9,  blur=0.040),
    'cricket':  dict(blobs=24, horizon=0.62, glow=False, figures=7,  blur=0.034),
    'seminar':  dict(blobs=26, horizon=0.72, glow=False, figures=12, blur=0.036),
    'meeting':  dict(blobs=28, horizon=0.66, glow=False, figures=14, blur=0.034),
    'portrait': dict(blobs=16, horizon=None, glow=True,  figures=1,  blur=0.046),
}


def grain(img, amount=7):
    n = Image.effect_noise(img.size, amount).convert('L').convert('RGB')
    return ImageChops.overlay(img, n) if False else Image.blend(img, n, 0.055)


def vignette(img, strength=0.42):
    w, h = img.size
    mask = Image.new('L', (w, h), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse([-w * 0.22, -h * 0.22, w * 1.22, h * 1.22], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(min(w, h) * 0.22))
    dark = Image.new('RGB', (w, h), (16, 6, 10))
    return Image.composite(img, Image.blend(img, dark, strength), mask)


def make(kind, w, h, seed):
    rnd = random.Random(seed)
    pal = PALETTES[kind]
    cfg = SCENES[kind]
    img = Image.new('RGB', (w, h), pal[1])
    d = ImageDraw.Draw(img, 'RGBA')

    # a soft vertical gradient base
    for y in range(h):
        t = y / max(1, h - 1)
        a, b = pal[1], pal[0]
        d.line([(0, y), (w, y)], fill=(int(a[0] + (b[0] - a[0]) * t),
                                       int(a[1] + (b[1] - a[1]) * t),
                                       int(a[2] + (b[2] - a[2]) * t)))

    # ground plane for the outdoor and interior scenes
    if cfg['horizon']:
        hy = int(h * cfg['horizon'])
        d.rectangle([0, hy, w, h], fill=pal[1] + (235,))
        d.rectangle([0, hy - int(h * 0.02), w, hy + int(h * 0.02)], fill=pal[2] + (90,))

    # defocused highlights — the bokeh that makes it read as a photograph
    for _ in range(cfg['blobs']):
        r = rnd.uniform(0.05, 0.26) * min(w, h)
        cx = rnd.uniform(-0.1, 1.1) * w
        cy = rnd.uniform(-0.05, 1.05) * h
        col = pal[rnd.randrange(len(pal))]
        d.ellipse([cx - r, cy - r, cx + r, cy + r],
                  fill=col + (rnd.randrange(46, 132),))

    # soft standing figures, so a crowd scene reads as a crowd
    fy = cfg['horizon'] or 0.74
    for _ in range(cfg['figures']):
        fh = rnd.uniform(0.16, 0.34) * h
        fw = fh * rnd.uniform(0.24, 0.36)
        cx = rnd.uniform(0.02, 0.98) * w
        base = fy * h + rnd.uniform(-0.03, 0.05) * h
        col = pal[rnd.randrange(len(pal))]
        alpha = rnd.randrange(60, 150)
        d.rounded_rectangle([cx - fw / 2, base - fh, cx + fw / 2, base],
                            radius=fw / 2, fill=col + (alpha,))
        hr = fw * 0.42
        d.ellipse([cx - hr, base - fh - hr * 1.7, cx + hr, base - fh + hr * 0.3],
                  fill=col + (alpha,))

    # a warm stage glow for the indoor celebratory scenes
    if cfg['glow']:
        gx, gy = rnd.uniform(0.25, 0.75) * w, rnd.uniform(0.15, 0.45) * h
        gr = min(w, h) * 0.55
        d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=pal[3] + (72,))

    img = img.filter(ImageFilter.GaussianBlur(min(w, h) * cfg['blur']))
    img = vignette(img)
    img = grain(img)
    return img


SPEC = [
    ('hero-cultural',      'cultural', 720, 940,  11),
    ('hero-cricket',       'cricket',  620, 620,  22),
    ('hero-seminar',       'seminar',  740, 660,  33),
    ('pillar-engineering', 'seminar',  860, 400,  44),
    ('pillar-sport',       'cricket',  860, 400,  55),
    ('pillar-arts',        'cultural', 860, 400,  66),
    ('gallery-cultural',   'cultural', 940, 700,  77),
    ('gallery-cricket',    'cricket',  640, 470,  88),
    ('gallery-seminar',    'seminar',  640, 470,  99),
    ('gallery-meeting',    'meeting', 1040, 380, 110),
    ('member-portrait',    'portrait', 440, 440, 121),
]

if __name__ == '__main__':
    total = 0
    for name, kind, w, h, seed in SPEC:
        p = OUT / f'{name}.jpg'
        make(kind, w, h, seed).save(p, 'JPEG', quality=78, optimize=True, progressive=True)
        kb = p.stat().st_size / 1024
        total += kb
        print(f'{name}.jpg  {w}x{h}  {kb:.0f} KB')
    print(f'total {total:.0f} KB')
