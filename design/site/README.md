# EF Qatar — public home page

| Artboard | Screen | Frame |
| --- | --- | --- |
| `Main.dc.html` | Home page, desktop | 1440 x 4420 |
| `HomeMobile.dc.html` | Home page, mobile | 390 x 6560 |

Static mockups for sign-off, not a clickable prototype.

## What the page does, in order

1. **Utility strip** — affiliation, contact, accessibility, member sign in
2. **Masthead and navigation** — lockup, site search, apply; eight nav sections
3. **Hero** — full-bleed slideshow, four slides crossfading on an 8-second beat,
   heading and kicker over them, progress bars on the same timing. CSS
   keyframes, no script, so it runs live.
4. **Four routes** — apply, register of members, marketplace, activities, in
   the maroon band immediately under the hero
5. **Notice strip** — the live notice, stated once
6. **News** — a lead story with three beside it
7. **March at EF** — the month calendar and the monthly programme, side by side
8. **How to apply** — four numbered steps, then categories and dues, then
   registration
9. **Notices** — the formal ones, dated
10. **The register** — what it holds, who may search it, partner verification
11. **The committee** and **published documents**
12. **Footer** — a full sitemap

### The hero

Four `.slide` layers, each `animation: shot 32s linear infinite` with an
8-second delay step, plus a slow `drift` scale on each image. The progress
bars run the same 32s cycle with matching delays, so they stay in step
without any script.

**Swapping in video** replaces the four slide layers with one `<video>` and
keeps the scrim and overlay untouched. Everything else on the page is
unaffected.

### The calendar

Generated from the real month with Python's `calendar` module, so 1 March
2027 falls on a Monday because it does. `CAL_EVENTS` maps day numbers to
categories, `CAL_KINDS` maps categories to their dot colour, and `CAL_TODAY`
marks the current day. Change the month by changing `CAL_YEAR`/`CAL_MONTH`.

## Type

Newsreader for editorial headlines, Public Sans for interface and reading
copy, Quicksand for the logo lockup alone. The serif is a **proposed
extension to the guideline** — see [`../brand/BRAND.md`](../brand/BRAND.md).

## Photographs — the ceiling on this page

`images/` holds **eight generated placeholders**, not photographs.
`make-placeholders.py` composes defocused scenes with standing figures,
stage light and a full tonal range, which is as close to photography as
synthetic imagery gets. Each is badged `placeholder` on the page.

Real imagery cannot be reached from the build environment: EF's Instagram is
blocked by the network's egress policy, every open image host is blocked too,
and the Drive archive holds personal family snapshots rather than EF events.

**On a full-bleed hero this gap shows more than anywhere else on the page.**
Four real hero photographs would do more for it than any further design
change.

**Replacing one is a file swap.** Same filename, same rough crop, then
`python3 site.py`.

| File | Position | Crop |
| --- | --- | --- |
| `hero-onam.jpg` | Hero slide 1 — arts and culture | 16:9, 1600px+ |
| `hero-cricket.jpg` | Hero slide 2 — sport | 16:9, 1600px+ |
| `hero-seminar.jpg` | Hero slide 3 — learning | 16:9, 1600px+ |
| `hero-agm.jpg` | Hero slide 4 — governance | 16:9, 1600px+ |
| `news-lead.jpg` | News lead story | 3:2 |
| `news-1.jpg` | News, secondary | 3:2 |
| `news-2.jpg` | News, secondary | 3:2 |
| `news-3.jpg` | News, secondary | 3:2 |

Hero slides carry the whole top of the page, so they keep more colour than
the news images — `make-placeholders.py` takes a per-image desaturation
figure for that reason.

**Usage rights must be recorded against every image** (BR-059).

## Structure

`site.py` imports the logo lockup from `../console/build.py` rather than
copying it, so the public site and the committee console cannot drift apart.

    python3 site.py

## Copy that needs confirming

The guideline states EF is "the apex body of Engineers of Kerala origin who
work in Qatar", and the membership section says so. **The Secretary must
confirm the eligibility wording against the criteria actually applied
(BR-011)**, or applicants are encouraged and then refused.

Dashed chips are facts still outstanding: three of the four membership dues,
venues, officer names, adoption dates for the bylaws and policies, the
annual report year, and the contact details. News, briefs and event copy is
drafted and needs EF's content owners (DQ-08, DQ-11).

## Rebuilding the canvas

    node "<design skill base dir>/seed-canvas.mjs" \
      --template "<design skill base dir>/payload.template.html" \
      --out ef-qatar-home-page.html --title "EF Qatar Home Page" \
      --artboard Main.dc.html --artboard HomeMobile.dc.html \
      --canvas canvas.json $(for f in images/*.jpg; do echo --image $f; done)

Measure frames against the real Google Fonts faces before publishing — the
sandbox browser cannot fetch them and under-measures. That caught 928px of
overflow on the mobile frame in this redesign.
