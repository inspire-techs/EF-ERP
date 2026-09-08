# EF Qatar — public home page

The public front of the platform. Zones follow section 6.2 of the Design
Brief, visitor-not-signed-in state, with three programme pillars, a
gallery and a member quote added on top of it.

| Artboard | Screen | Frame |
| --- | --- | --- |
| `Main.dc.html` | Home page, desktop | 1440 x 5820 |
| `HomeMobile.dc.html` | Home page, mobile | 390 x 6120 |

Static mockups for sign-off, not a clickable prototype.

## Photographs — the one outstanding item

`images/` holds **eleven generated placeholders**, not photographs.
They are defocused compositions in the brand palette, produced by
`make-placeholders.py`, and each is labelled `placeholder` in the layout.

They exist because real imagery could not be reached from the build
environment: EF's Instagram is blocked by the network's egress policy,
every open image host is blocked too, and the Drive archive turned out to
hold personal family snapshots rather than EF events — nothing there
belongs on a public page.

**Replacing one is a file swap.** Same filename, same rough aspect, then:

    python3 make-placeholders.py    # only if regenerating placeholders
    python3 site.py                 # rewrites the artboards

| File | Position | Aspect |
| --- | --- | --- |
| `hero-cultural.jpg` | Hero collage, tall left tile | portrait 3:4 |
| `hero-cricket.jpg` | Hero collage, top right | square |
| `hero-seminar.jpg` | Hero collage, lower right | landscape ~10:9 |
| `pillar-engineering.jpg` | Engineering pillar | landscape ~2:1 |
| `pillar-sport.jpg` | Sport pillar | landscape ~2:1 |
| `pillar-arts.jpg` | Arts and culture pillar | landscape ~2:1 |
| `gallery-cultural.jpg` | Gallery, large tile | landscape 4:3 |
| `gallery-cricket.jpg` | Gallery, square | square-ish |
| `gallery-seminar.jpg` | Gallery, square | square-ish |
| `gallery-meeting.jpg` | Gallery, wide bottom tile | wide ~3:1 |
| `member-portrait.jpg` | The member quote | square |

At least 1600px on the long edge. **Usage rights must be recorded against
every image** (BR-059), and the member in the portrait has to have agreed
to appear.

Each slot keeps its brand duotone behind the photograph, so a missing
image degrades to a coloured panel rather than a broken box.

## Structure

`site.py` imports the mark, lockup and icon set from
`../console/build.py` rather than copying them, so the public site and the
committee console cannot drift apart.

    python3 site.py

Tokens and the green-contrast rule: [`../brand/BRAND.md`](../brand/BRAND.md).

## Composition

From EF's guideline: maroon panels carrying the mark oversized, a green
figures band lifted over the hero edge, green as the energetic accent, a
pale ground with white cards between. Four duotones drive the image slots
so no two adjacent gallery panels share a colour.

## Copy that needs confirming

The guideline states EF is "the apex body of Engineers of Kerala origin
who work in Qatar". The headline and the eligibility line both say so —
but **the Secretary must confirm the eligibility wording against the
admission criteria actually applied (BR-011)**, or applicants are
encouraged and then refused.

The member quote is left as instructions, not an invented testimonial.
Announcement, event and pillar copy is drafted and needs EF's content
owners (DQ-08, DQ-11). Dashed chips elsewhere are facts still outstanding:
three of the four figures (only the 800 members is known), venues, officer
names, the affiliation mark, contact details.

## Rebuilding the canvas

    node "<design skill base dir>/seed-canvas.mjs" \
      --template "<design skill base dir>/payload.template.html" \
      --out ef-qatar-home-page.html --title "EF Qatar Home Page" \
      --artboard Main.dc.html --artboard HomeMobile.dc.html \
      --canvas canvas.json $(for f in images/*.jpg; do echo --image $f; done)
