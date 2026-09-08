# EF Qatar Console — committee-side application

Four screens, designed for sign-off against the brand guideline and the
BRD. Static mockups, not a clickable prototype.

| Artboard | Screen | Frame |
| --- | --- | --- |
| `Main.dc.html` | Dashboard | 1440 x 1120 |
| `Members.dc.html` | Members list | 1440 x 1120 |
| `MemberRecord.dc.html` | One member's record | 1440 x 1200 |
| `Approvals.dc.html` | Approvals queue | 1440 x 1120 |

The member record is taller than one viewport on purpose — records
scroll.

## Structure

`build.py` holds the app shell, the tokens, the icon set and the EF mark.
`screens.py` holds the four screens. Artboards share nothing at runtime,
so each `.dc.html` carries its own copy of the shell; composing them from
one source is what keeps the sidebar and top bar byte-identical.

    python3 screens.py

Tokens and the green-contrast rule: [`../brand/BRAND.md`](../brand/BRAND.md).

## What the screens follow

Structure and content come from the BRD: one approvals queue with time
limits and escalation, sequential invoices, receipts and credit notes, a
tamper-evident record of privileged action, and per-section profile
visibility enforced on every route. Dashboard figures track EF's own
objectives — 70% self-service renewal (OBJ-02) and 80% of dues collected
electronically (OBJ-03).

Member names, employers, numbers, dates and amounts are sample data.

## Rebuilding the canvas

    node "<design skill base dir>/seed-canvas.mjs" \
      --template "<design skill base dir>/payload.template.html" \
      --out ef-qatar-console.html --title "EF Qatar Console" \
      --artboard Main.dc.html --artboard Members.dc.html \
      --artboard MemberRecord.dc.html --artboard Approvals.dc.html \
      --canvas canvas.json

Check frames against the real Google Fonts faces before publishing — see
the note in `../brand/BRAND.md`.
