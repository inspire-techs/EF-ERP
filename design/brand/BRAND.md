# Brand tokens

Taken from EF's `BRAND GUIDELINE`, not invented.

## Colour

| Token | Value | Where |
| --- | --- | --- |
| Maroon | `#4B1728` | Sidebar, primary actions, headings, panels |
| Green | `#4BB148` | Accent, active state, positive status, figures band |
| Pale | `#E9F1FA` | Application and page ground |
| Ink | `#241017` | Headings — derived, warm near-black |
| Body | `#4A4045` | Reading copy |
| Muted | `#7D7278` · `#6E636A` | Secondary text |
| Line | `#DCE3EC` · `#D8E4F0` | Borders, cool to sit with the pale ground |
| Attention | `#7A4E12` on `#FBF2E2` | Overdue, expiring |
| Positive | `#2A6B27` on `#E4F4E3` | Cleared, paid, active |

Duotones for image slots are in `site.py` (`TONES`) — four of them, so no
two adjacent gallery panels share a colour.

## The green contrast problem

**White text on `#4BB148` is 2.6:1 and fails WCAG AA.** This is the one
constraint that shapes the whole system:

- Primary actions are **maroon with white text** — 13:1.
- Green is the **accent**: active states, positive chips, the figures band.
- Where a green action is right (`Approve membership`, `Apply to join`) it
  carries **dark text** — `#1E3319` or `#23361F` on green is 5.3:1.

Never put white text on the brand green.

Membership state always carries a text label, never colour alone.

## Type

The console and the public site diverge here, deliberately, and the
divergence needs EF's approval.

### Console

| Face | Role |
| --- | --- |
| Quicksand 500/600/700 | Brand voice — logo wordmark, headings, navigation, figures |
| Nunito Sans 400/600/700/800 | Interface and reading copy |
| IBM Plex Mono 400/500 | Member numbers, document references, amounts |

### Public site — a proposed extension

| Face | Role |
| --- | --- |
| Newsreader 400/500/600 | Editorial headlines |
| Public Sans 400/500/600/700 | Interface and reading copy |
| Quicksand 600/700 | **The logo lockup only** |

The guideline's rounded geometric is a friendly face. At headline size on
a public page it reads promotional, which is the wrong register for the
apex body of a profession — a serif is what gives an institution its
authority. Newsreader is an editorial serif built for news setting.

**This extends the guideline; it does not depart from the identity.** The
logo is untouched and Quicksand still sets it. If EF would rather hold
Quicksand across headlines too, that is a one-line change in
`site/site.py`.

All faces from Google Fonts.

**Measuring frames:** Quicksand is wider than most fallbacks. A sandbox
without Google Fonts access under-measures every frame — proxy the real
faces in before trusting a height. Doing so has caught 23px, 180px, 577px
and 933px of vertical overflow on this project.

## The mark

`mark.svg` (full) and `mark-small.svg` (fewer spiral turns, heavier
strokes, for sizes under about 40px) are redrawn from the supplied logo so
the roundel scales, recolours and reverses on maroon. They are a faithful
stand-in, **not EF's artwork** — drop the vector file in before build.

Reversed on maroon: ring and spiral white, swoosh green, wordmark white
with `qatar` in green (maroon would vanish on a maroon ground).
