# Design

Screen designs for the EF Qatar platform, built against the brand
guideline and the BRD. Static mockups for sign-off — not prototypes, and
not implementation.

| Folder | Deliverable | Screens |
| --- | --- | --- |
| [`console/`](console/) | Committee-side application | Dashboard · Members · Member record · Approvals queue |
| [`site/`](site/) | Public home page, designed as a learned society publishes | Desktop · Mobile |
| [`brand/`](brand/) | The mark and the design tokens | — |
| [`archive/pre-brand/`](archive/pre-brand/) | Superseded first drafts | Home · My EF (desktop and mobile) |

## How these are built

Each screen is a `.dc.html` artboard. A Python script composes the
artboards from shared parts, because artboards share nothing at runtime
and each file needs its own copy of the chrome — composing them is what
keeps the chrome identical across screens.

    cd console && python3 screens.py        # rewrites the 4 console artboards
    cd site    && python3 site.py           # rewrites the 2 home page artboards

`site.py` imports the mark, lockup and icon set from `console/build.py`
rather than copying them, so the public site and the console cannot drift
apart. Run the console build first if you have changed the shared parts.

The seeded canvases (`ef-qatar-*.html`) are gitignored — they are large
generated payloads. Rebuild them with the command in each folder's README.

## Two things every screen depends on

**The mark is a stand-in.** `brand/mark.svg` is redrawn in SVG from the
supplied logo so it scales and reverses. EF's own vector artwork has to
replace it before build.

**White on the brand green fails.** `#4BB148` against white is 2.6:1.
Maroon carries the primary actions instead (13:1), green stays the
accent, and where a green action is right it carries dark text at 5.3:1.
See [`brand/BRAND.md`](brand/BRAND.md).

**The public site sets headlines in a serif.** Newsreader, with Quicksand
held back for the logo lockup alone. That is a proposed extension to the
guideline and needs EF's approval — the reasoning is in
[`brand/BRAND.md`](brand/BRAND.md).

## Still to do

- The member-facing **My EF** page in this brand. The version in
  `archive/pre-brand/` predates the guideline.
- Remaining console areas: finance, events, marketplace, directory, jobs,
  roles and access.
- Real photographs for the home page — see [`site/README.md`](site/README.md).
