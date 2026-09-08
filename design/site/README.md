# EF Qatar — public home page

Designed as a learned society publishes, not as a product landing page.

| Artboard | Screen | Frame |
| --- | --- | --- |
| `Main.dc.html` | Home page, desktop | 1440 x 4420 |
| `HomeMobile.dc.html` | Home page, mobile | 390 x 6560 |

Static mockups for sign-off, not a clickable prototype.

## What the page does, in order

1. **Utility strip** — affiliation, contact, accessibility, member sign in
2. **Masthead** — lockup, site search, apply
3. **Navigation** — eight sections; the nav is itself the value on an
   institutional site, so it is populated rather than reduced to five items
4. **Lead story** — a notice, with a sidebar of four dated briefs
5. **Members' notice band** — the renewal window, stated once
6. **News** — three items, each with a kicker, a standfirst and a date
7. **Events** — a listing with date blocks, venue, category, capacity, booking
8. **Membership** — the categories with their dues, and the four steps of
   admission. Information, not persuasion.
9. **The register** — what it holds, who may search it, and a verification
   panel for partners and employers
10. **The committee** and **published documents** — offices with terms,
    documents with version numbers
11. **Footer** — a full sitemap

## Deliberately absent

The previous draft carried a centred value proposition with paired buttons,
a floating image collage, a statistics band, an icon trio of "pillars", a
member testimonial and a closing call-to-action banner. Those six blocks
are what made it read as marketing. They are gone and should not come back.

Hairline rules instead of shadowed cards. Square corners. A kicker and a
date on everything. Colour used structurally, not decoratively.

The genre was worked from first principles — royalsociety.org and
istructe.org are both blocked by the network's egress policy, and neither
society's design is reproduced here in any case.

## Type

Newsreader for editorial headlines, Public Sans for interface and reading
copy, Quicksand for the logo lockup alone. The serif is a **proposed
extension to the guideline** — see [`../brand/BRAND.md`](../brand/BRAND.md).

## Photographs — the one outstanding item

`images/` holds **seven generated placeholders**, not photographs:
defocused, desaturated compositions produced by `make-placeholders.py`, so
they read as photography rather than as brand-coloured panels. Each is
badged `placeholder` on the page.

Real imagery could not be reached from the build environment: EF's
Instagram is blocked by the network's egress policy, every open image host
is blocked too, and the Drive archive holds personal family snapshots
rather than EF events.

**Replacing one is a file swap.** Same filename, same rough crop, then
`python3 site.py`.

| File | Position | Crop |
| --- | --- | --- |
| `lead-agm.jpg` | Lead story | 16:9 |
| `brief-renewal.jpg` | Sidebar brief | square |
| `brief-seminar.jpg` | Sidebar brief | square |
| `brief-register.jpg` | Sidebar brief | square |
| `news-committee.jpg` | News, and the fourth brief | 3:2 |
| `news-tournament.jpg` | News | 3:2 |
| `news-arts.jpg` | News | 3:2 |

At least 1600px on the long edge. **Usage rights must be recorded against
every image** (BR-059).

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
