#!/usr/bin/env python3
"""Compose the EF Qatar Console artboards.

Artboards share nothing at runtime, so each .dc.html carries its own copy of
the shell. Composing them here rather than by hand is what keeps the sidebar,
top bar and tokens byte-identical across all four.

Palette and type are lifted from the EF Qatar brand guideline:
  maroon #4B1728 · green #4BB148 · pale #E9F1FA · rounded geometric wordmark.
"""
import math, pathlib

OUT = pathlib.Path(__file__).parent

# ---------------------------------------------------------------- brand mark
def _spiral(cx, cy, r0, r1, turns, n=180, start=196):
    pts, total = [], turns * 2 * math.pi
    for i in range(n + 1):
        t = i / n
        th = total * t + math.radians(start)
        r = r0 + (r1 - r0) * t
        pts.append((cx + r * math.cos(th), cy + r * math.sin(th)))
    return 'M %.2f %.2f' % pts[0] + ''.join(' L %.2f %.2f' % p for p in pts[1:])


def _arc(cx, cy, r, a0, a1):
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    return 'M %.2f %.2f A %.2f %.2f 0 %d %d %.2f %.2f' % (
        x0, y0, r, r, 1 if abs(a1 - a0) > 180 else 0, 1 if a1 > a0 else 0, x1, y1)


SWOOSH = ('M 22 78 C 37 94, 61 93, 80 74 C 91 63, 100 54, 113 46 '
          'C 98 53, 86 63, 74 72 C 57 85, 40 87, 22 78 Z')


def mark(size, stroke='#4B1728', swoosh='#4BB148'):
    """The EF roundel. Redrawn from the supplied logo — swap for EF's vector file."""
    return (
        f'<svg viewBox="0 0 120 120" width="{size}" height="{size}" '
        f'style="flex-shrink: 0;" aria-label="Engineers Forum Qatar">'
        f'<path d="{_arc(60, 60, 47, 34, 334)}" fill="none" stroke="{stroke}" '
        f'stroke-width="11" stroke-linecap="round"/>'
        f'<path d="{_spiral(60, 60, 9, 28, 0.72)}" fill="none" stroke="{stroke}" '
        f'stroke-width="11" stroke-linecap="round"/>'
        f'<path d="{SWOOSH}" fill="{swoosh}"/></svg>')


def lockup(reversed_=False):
    """Mark plus the two-line wordmark, set to match the logo's lowercase lockup."""
    a = '#FFFFFF' if reversed_ else '#4BB148'   # "engineers forum"
    b = '#4BB148' if reversed_ else '#4B1728'   # "qatar"
    m = mark(34, '#FFFFFF' if reversed_ else '#4B1728')
    return (
        f'<div style="display: flex; align-items: center; gap: 10px;">{m}'
        f'<div style="display: flex; flex-direction: column; line-height: 0.94;">'
        f'<span style="font-family: Quicksand, sans-serif; font-size: 17px; '
        f'font-weight: 700; color: {a}; letter-spacing: -0.01em;">engineers</span>'
        f'<span style="font-family: Quicksand, sans-serif; font-size: 17px; '
        f'font-weight: 700; letter-spacing: -0.01em;"><span style="color: {a};">forum</span>'
        f'<span style="color: {b};">qatar</span></span></div></div>')


# --------------------------------------------------------------------- icons
I = {
 'grid':   '<rect x="3" y="3" width="7.5" height="7.5" rx="1.6"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.6"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.6"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.6"/>',
 'people': '<circle cx="9" cy="8" r="3.3"/><path d="M2.6 19.6c.9-3.1 3.3-4.6 6.4-4.6s5.5 1.5 6.4 4.6"/><path d="M16.6 5.2a3.3 3.3 0 0 1 0 5.6M18.5 15.3c2 .7 3.3 2 3.9 4.3"/>',
 'check':  '<path d="M20.5 11.3V6.2a1.7 1.7 0 0 0-1.7-1.7H5.2a1.7 1.7 0 0 0-1.7 1.7v11.6a1.7 1.7 0 0 0 1.7 1.7h6"/><path d="M7.5 9h9M7.5 13h4"/><path d="m14.5 17.5 2.2 2.2 4.3-4.6"/>',
 'id':     '<rect x="2.5" y="5" width="19" height="14" rx="2.2"/><circle cx="8.6" cy="11" r="2.2"/><path d="M5.1 16.3c.7-1.4 2-2.1 3.5-2.1s2.8.7 3.5 2.1M15 10h4.2M15 13.6h4.2"/>',
 'doc':    '<path d="M14 2.6H7a2 2 0 0 0-2 2v14.8a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7.6Z"/><path d="M14 2.6v5h5M8.6 13h6.8M8.6 16.6h4.4"/>',
 'scale':  '<path d="M12 3.5v17M5 7.5h14"/><path d="M8.5 7.5 5.5 14h6ZM15.5 7.5 12.5 14h6Z"/>',
 'cal':    '<rect x="3" y="4.6" width="18" height="16" rx="2.2"/><path d="M3 9.6h18M8 2.6v4M16 2.6v4"/>',
 'mega':   '<path d="M3.5 10v4l3 .6 2.6 4.4 2.2-1.2-1.8-3.1 8.6 1.7V6.6L3.5 10Z"/><path d="M19.5 9.4a2.8 2.8 0 0 1 0 5.2"/>',
 'search': '<circle cx="10.5" cy="10.5" r="6.6"/><path d="m21 21-5.8-5.8"/>',
 'tag':    '<path d="M20.5 12.5 12.8 20.2a2 2 0 0 1-2.9 0l-6.4-6.4a2 2 0 0 1-.5-1.9l1.4-5.6a2 2 0 0 1 1.5-1.5l5.6-1.4a2 2 0 0 1 1.9.5l6.4 6.4a2 2 0 0 1 0 2.9Z"/><circle cx="8.6" cy="8.6" r="1.5"/>',
 'case':   '<rect x="2.5" y="7" width="19" height="13" rx="2.2"/><path d="M8.6 7V5.5a2 2 0 0 1 2-2h2.8a2 2 0 0 1 2 2V7M2.5 12h19"/>',
 'shield': '<path d="M12 2.6 3.6 6v6c0 5 3.6 8.4 8.4 9.4 4.8-1 8.4-4.4 8.4-9.4V6Z"/><path d="m9 12 2 2 4-4"/>',
 'clock':  '<circle cx="12" cy="12" r="9"/><path d="M12 7.2V12l3.2 2"/>',
 'bell':   '<path d="M18 8.6a6 6 0 1 0-12 0c0 6-2.5 7.5-2.5 7.5h17S18 14.6 18 8.6"/><path d="M13.7 20a2 2 0 0 1-3.4 0"/>',
 'dots':   '<circle cx="12" cy="5.5" r="1.6"/><circle cx="12" cy="12" r="1.6"/><circle cx="12" cy="18.5" r="1.6"/>',
 'chev':   '<path d="m9 6 6 6-6 6"/>',
 'down':   '<path d="m6 9 6 6 6-6"/>',
 'filter': '<path d="M3.5 5.5h17l-6.6 7.8v5.6l-3.8-2v-3.6Z"/>',
 'up':     '<path d="M12 19.5v-15M5.5 11 12 4.5 18.5 11"/>',
 'money':  '<rect x="2.5" y="5.5" width="19" height="13" rx="2.2"/><path d="M2.5 10h19"/>',
 'plus':   '<path d="M12 5v14M5 12h14"/>',
 'alert':  '<path d="M12 3.5 21 19.5H3Z"/><path d="M12 9.5v4M12 16.4v.1"/>',
 'x':      '<path d="M6 6l12 12M18 6 6 18"/>',
 'export': '<path d="M12 15.5V3.5M6.5 9 12 3.5 17.5 9"/><path d="M4 15.5v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/>',
}


def ic(name, size=18, stroke='currentColor', w=1.7):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="{stroke}" stroke-width="{w}" stroke-linecap="round" '
            f'stroke-linejoin="round" style="flex-shrink: 0;">{I[name]}</svg>')


# ---------------------------------------------------------------- the shell
NAV = [
    ('OVERVIEW',       [('Dashboard', 'grid')]),
    ('MEMBERSHIP',     [('Members', 'people'), ('Approvals', 'check'), ('Digital IDs', 'id')]),
    ('FINANCE',        [('Invoices and receipts', 'doc'), ('Reconciliation', 'scale')]),
    ('PROGRAMMES',     [('Events', 'cal'), ('Announcements', 'mega')]),
    ('COMMUNITY',      [('Directory', 'search'), ('Marketplace', 'tag'), ('Jobs', 'case')]),
    ('ADMINISTRATION', [('Roles and access', 'shield'), ('Audit log', 'clock')]),
]

CSS = """
    body { margin: 0; font-family: 'Nunito Sans', system-ui, sans-serif; background: #E9F1FA;
           color: #4A4045; -webkit-font-smoothing: antialiased; }
    * { box-sizing: border-box; }
    a { color: #4B1728; text-decoration: none; }
    a:hover { color: #6B3040; }
    h1, h2, h3 { font-family: Quicksand, system-ui, sans-serif; color: #241017; margin: 0;
                 font-weight: 600; letter-spacing: -0.01em; }
    p { margin: 0; }
    table { border-collapse: collapse; width: 100%; }
    .side-a { display: flex; align-items: center; gap: 12px; height: 42px; padding: 0 14px;
              margin: 0 12px; border-radius: 7px; color: #CFB9C1; font-size: 14px;
              font-family: Quicksand, sans-serif; font-weight: 600; }
    .side-a:hover { color: #FFFFFF; }
    .side-a.on { background: #FFFFFF; color: #4B1728; }
    .side-g { font-size: 10px; letter-spacing: 0.15em; color: #9A7883; font-weight: 700;
              padding: 0 26px 7px; margin-top: 20px; }
    .card { background: #FFFFFF; border: 1px solid #DCE3EC; border-radius: 10px; }
    .card-h { display: flex; align-items: center; justify-content: space-between; gap: 16px;
              padding: 17px 22px; border-bottom: 1px solid #EEF3F8; }
    .card-t { font-family: Quicksand, sans-serif; font-size: 15.5px; font-weight: 700; color: #241017; }
    .btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px;
           height: 38px; padding: 0 16px; border-radius: 7px; font-size: 14px; font-weight: 700;
           font-family: 'Nunito Sans', sans-serif; border: 1px solid transparent;
           white-space: nowrap; }
    .btn-p { background: #4B1728; color: #FFFFFF; }
    .btn-p:hover { background: #642034; color: #FFFFFF; }
    .btn-g { background: #4BB148; color: #23361F; }
    .btn-g:hover { background: #43A340; color: #23361F; }
    .btn-s { background: #FFFFFF; color: #4B1728; border-color: #D3DCE6; }
    .btn-s:hover { border-color: #4B1728; color: #4B1728; }
    .chip { display: inline-flex; align-items: center; gap: 6px; height: 25px; padding: 0 10px;
            border-radius: 100px; font-size: 12.5px; font-weight: 700; white-space: nowrap; }
    .th { font-size: 11px; letter-spacing: 0.07em; color: #7D7278; font-weight: 800;
          text-transform: uppercase; text-align: left; padding: 0 0 0 0; }
    .mono { font-family: 'IBM Plex Mono', monospace; font-variant-numeric: tabular-nums; }
    .av { border-radius: 50%; display: flex; align-items: center; justify-content: center;
          font-family: Quicksand, sans-serif; font-weight: 700; flex-shrink: 0; }
    .field { height: 38px; border: 1px solid #D3DCE6; border-radius: 7px; background: #FFFFFF;
             display: flex; align-items: center; gap: 9px; padding: 0 12px; font-size: 14px;
             color: #4A4045; white-space: nowrap; overflow: hidden; }
"""

CHIPS = {
    'active':    ('#E4F4E3', '#2A6B27', '#C4E6C2', 'Active'),
    'expiring':  ('#FBF2E2', '#7A4E12', '#EEDCBC', 'Expiring soon'),
    'lapsed':    ('#F3E3E8', '#4B1728', '#E3CBD3', 'Lapsed'),
    'pending':   ('#E9F1FA', '#2F5375', '#CBDCEE', 'Pending approval'),
    'suspended': ('#F1F1F3', '#554E52', '#E0DDE0', 'Suspended'),
}


def chip(kind, label=None):
    bg, fg, bd, dflt = CHIPS[kind]
    return (f'<span class="chip" style="background: {bg}; color: {fg}; border: 1px solid {bd};">'
            f'{label or dflt}</span>')


def avatar(initials, size=36, bg='#F3E3E8', fg='#4B1728', fs=None):
    return (f'<div class="av" style="width: {size}px; height: {size}px; background: {bg}; '
            f'color: {fg}; font-size: {fs or round(size * 0.38, 1)}px;">{initials}</div>')


def sidebar(active):
    groups = []
    for label, items in NAV:
        links = ''.join(
            f'<a href="#" class="side-a{" on" if name == active else ""}">'
            f'{ic(icon, 17, "#4B1728" if name == active else "#B79AA4")}'
            f'<span>{name}</span></a>' for name, icon in items)
        groups.append(f'<div class="side-g">{label}</div>'
                      f'<div style="display: flex; flex-direction: column; gap: 2px;">{links}</div>')
    return f"""<div style="background: #4B1728; display: flex; flex-direction: column;">
      <div style="padding: 22px 24px 4px;">{lockup(reversed_=True)}</div>
      <div style="flex-grow: 1; padding-bottom: 20px;">{''.join(groups)}</div>
      <div style="border-top: 1px solid #642A3C; padding: 14px 20px; display: flex;
                  align-items: center; gap: 11px;">
        {avatar('RM', 36, '#642A3C', '#FFFFFF')}
        <div style="display: flex; flex-direction: column; gap: 2px; flex-grow: 1; min-width: 0;">
          <span style="font-size: 13.5px; font-weight: 700; color: #FFFFFF;">Rajesh Menon</span>
          <span style="font-size: 11.5px; color: #B79AA4;">Technical Secretary</span>
        </div>
        {ic('dots', 16, '#B79AA4')}
      </div>
    </div>"""


def topbar(title, crumb=None, actions=''):
    head = (f'<div style="display: flex; flex-direction: column; gap: 3px;">'
            f'<span style="font-size: 11.5px; color: #7D7278; font-weight: 600;">{crumb}</span>'
            f'<h1 style="font-size: 19px;">{title}</h1></div>'
            if crumb else f'<h1 style="font-size: 20px;">{title}</h1>')
    return f"""<div style="height: 68px; background: #FFFFFF; border-bottom: 1px solid #DCE3EC;
                display: flex; align-items: center; gap: 24px; padding: 0 30px; flex-shrink: 0;">
      {head}
      <div style="flex-grow: 1;"></div>
      <div class="field" style="width: 232px; color: #7D7278;">{ic('search', 17, '#9A9096')}
        <span>Search members</span></div>
      <a href="#" style="position: relative; display: flex;">{ic('bell', 20, '#4A4045')}
        <span style="position: absolute; top: -2px; right: -2px; width: 8px; height: 8px;
              border-radius: 50%; background: #4BB148; border: 1.5px solid #FFFFFF;"></span></a>
      {actions}
    </div>"""


def page(body, active, title, crumb=None, actions='', h=1040):
    """Wrap a screen's content in the app shell and the Design Component envelope."""
    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700;6..12,800&family=IBM+Plex+Mono:wght@400;500&display=swap">
  <style>{CSS}  </style>
</helmet>

<div style="width: 1440px; height: {h}px; display: grid; grid-template-columns: 252px minmax(0, 1fr); background: #E9F1FA; overflow: hidden;">
  {sidebar(active)}
  <div style="display: flex; flex-direction: column; min-width: 0;">
    {topbar(title, crumb, actions)}
    <div style="flex-grow: 1; overflow: hidden; padding: 26px 30px;">
{body}
    </div>
  </div>
</div>
</x-dc>
<script data-dc-script data-props='{{"$preview":{{"width":1440,"height":{h}}}}}'>
class Component extends DCLogic {{}}
</script>
</body>
</html>
"""
