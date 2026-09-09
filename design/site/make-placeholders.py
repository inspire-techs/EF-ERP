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
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageChops

OUT = pathlib.Path(__file__).parent / 'images'
OUT.mkdir(exist_ok=True)

# palettes keyed to what each photograph will eventually show
PALETTES = {
    'cultural': [(120, 54, 74), (196, 132, 96), (242, 206, 158), (255, 244, 228),
                 (38, 20, 26), (86, 62, 70)],
    'cricket':  [(96, 168, 88), (58, 116, 52), (206, 224, 176), (248, 246, 226),
                 (34, 44, 32), (150, 140, 116)],
    'seminar':  [(154, 128, 132), (98, 78, 84), (216, 200, 194), (250, 246, 240),
                 (40, 32, 36), (120, 112, 118)],
    'meeting':  [(112, 128, 108), (64, 76, 62), (198, 202, 188), (248, 248, 240),
                 (34, 38, 32), (140, 122, 100)],
    'portrait': [(150, 104, 104), (104, 66, 70), (222, 198, 190), (252, 246, 242),
                 (44, 30, 34), (128, 106, 104)],
}

# scene: (bands, blobs, horizon) — bands give outdoor scenes a ground/sky split
SCENES = {
    'cultural': dict(blobs=44, horizon=None, glow=True,  figures=14, blur=0.026),
    'cricket':  dict(blobs=32, horizon=0.62, glow=False, figures=11, blur=0.022),
    'seminar':  dict(blobs=34, horizon=0.72, glow=False, figures=18, blur=0.024),
    'meeting':  dict(blobs=36, horizon=0.66, glow=False, figures=22, blur=0.022),
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


def make(kind, w, h, seed, desat=0.58):
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
    # pull most of the saturation out and warm what is left, so these read as
    # photographs rather than as brand-coloured panels
    img = Image.blend(img, img.convert('L').convert('RGB'), desat)
    warm = Image.new('RGB', img.size, (214, 200, 190))
    img = Image.blend(img, ImageChops.multiply(img, warm), 0.45)
    img = vignette(img, 0.26)
    img = grain(img)
    img = ImageEnhance.Contrast(img).enhance(1.34)
    img = ImageEnhance.Brightness(img).enhance(1.18)
    return img


# named for the position each fills, with the crop that position wants.
# Hero slides keep more colour — they carry the whole top of the page.
SPEC = [
    ('hero-onam',    'cultural', 1600, 900, 210, 0.20),
    ('hero-cricket', 'cricket',  1600, 900, 220, 0.20),
    ('hero-seminar', 'seminar',  1600, 900, 230, 0.20),
    ('hero-agm',     'meeting',  1600, 900, 240, 0.20),
    ('news-lead',    'meeting',  1040, 694, 110, 0.58),
    ('news-1',       'cricket',   560, 374,  88, 0.58),
    ('news-2',       'cultural',  560, 374,  66, 0.58),
    ('news-3',       'seminar',   560, 374,  44, 0.58),
]

if __name__ == '__main__':
    total = 0
    for name, kind, w, h, seed, desat in SPEC:
        p = OUT / f'{name}.jpg'
        make(kind, w, h, seed, desat).save(p, 'JPEG', quality=76, optimize=True,
                                           progressive=True)
        kb = p.stat().st_size / 1024
        total += kb
        print(f'{name}.jpg  {w}x{h}  {kb:.0f} KB')
    print(f'total {total:.0f} KB')
