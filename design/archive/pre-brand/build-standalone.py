#!/usr/bin/env python3
"""Turn the .dc.html artboards into plain, self-contained HTML pages.

Produces standalone/<page>.html (one file per screen, opens on its own)
and standalone/ef-qatar-screens.html (all three behind tabs, one file to send).
No build step, no assets, no network beyond the Google Fonts stylesheet.
"""
import re, pathlib

SRC = pathlib.Path('.')
OUT = SRC / 'standalone'
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=IBM+Plex+Sans:wght@400;450;500;600&family=IBM+Plex+Mono:wght@400;500'
         '&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap">')

SCREENS = [
    dict(src='Main.dc.html',        slug='01-home',           kind='desktop',
         title='EF Qatar — Home page',
         tab='Home', note='Visitor, not signed in · 1440'),
    dict(src='MyEF.dc.html',        slug='02-my-ef-desktop',  kind='desktop',
         title='EF Qatar — My EF, desktop',
         tab='My EF — desktop', note='Member page, expiring soon · 1440'),
    dict(src='MyEFMobile.dc.html',  slug='03-my-ef-mobile',   kind='mobile',
         title='EF Qatar — My EF, mobile',
         tab='My EF — mobile', note='Member page, expiring soon · 390'),
]


def parts(path):
    """Pull the stylesheet and the markup out of a Design Component file."""
    s = path.read_text(encoding='utf-8')
    css = re.search(r'<helmet>[\s\S]*?<style>([\s\S]*?)</style>[\s\S]*?</helmet>', s).group(1)
    markup = re.search(r'</helmet>([\s\S]*?)</x-dc>', s).group(1).strip()
    return css, markup


def scope(css, sel):
    """Prefix every rule in a stylesheet so screens can share one document.

    `body` maps onto the screen wrapper itself; everything else nests under it.
    Without this the two `.sect-h` rules (19px desktop, 17px mobile) collide.
    """
    out = []
    for block in re.findall(r'([^{}]+)\{([^{}]*)\}', css):
        selectors, body = block[0].strip(), block[1].strip()
        scoped = []
        for one in selectors.split(','):
            one = one.strip()
            if not one:
                continue
            scoped.append(sel if one == 'body' else f'{sel} {one}')
        out.append('%s { %s }' % (', '.join(scoped), body))
    return '\n    '.join(out)


CHROME = """
    :root { color-scheme: light; }
    html, body { margin: 0; }
    body { background: #EDE7E8; font-family: 'IBM Plex Sans', system-ui, sans-serif; }
    .frame-note { max-width: 1200px; margin: 0 auto; padding: 14px 40px; font-size: 12.5px;
                  color: #7C7076; display: flex; gap: 10px; align-items: baseline; }
    .frame-note strong { color: #1B1417; font-weight: 500; }
"""

# ---- one file per screen -------------------------------------------------
built = []
for sc in SCREENS:
    css, markup = parts(SRC / sc['src'])
    if sc['kind'] == 'desktop':
        # the artboard is a fixed 1440 column; let it fill the window instead
        markup = markup.replace('<div style="width: 1440px; background: #FBF9F8;">',
                                '<div style="width: 100%; min-width: 1280px; background: #FBF9F8;">', 1)
        shell = 'body { margin: 0; }'
    else:
        # keep the phone column at 390 and centre it on a darker surround
        markup = markup.replace('<div style="width: 390px; background: #FBF9F8;">',
                                '<div style="width: 390px; margin: 0 auto; min-height: 100vh; '
                                'border-left: 1px solid #E1D9DB; border-right: 1px solid #E1D9DB; '
                                'background: #FBF9F8;">', 1)
        shell = 'body { margin: 0; background: #EDE7E8; }'

    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{sc['title']}</title>
{FONTS}
<style>
{css.strip()}
    {shell}
</style>
</head>
<body>
{markup}
</body>
</html>
"""
    (OUT / f"{sc['slug']}.html").write_text(page, encoding='utf-8')
    built.append((sc, css, markup))

# ---- all three in one file, behind tabs ----------------------------------
styles, panels, tabs = [], [], []
for i, (sc, css, markup) in enumerate(built):
    sel = f'#screen-{i}'
    styles.append(scope(css, sel))
    body = markup
    if sc['kind'] == 'desktop':
        body = body.replace('min-width: 1280px', 'min-width: 1280px')
    tabs.append(
        f'<button type="button" class="tab{" is-on" if i == 0 else ""}" data-i="{i}">'
        f'{sc["tab"]}</button>')
    panels.append(
        f'<div class="panel{" is-on" if i == 0 else ""}" id="panel-{i}">'
        f'<div class="frame-note"><strong>{sc["tab"]}</strong><span>{sc["note"]}</span></div>'
        f'<div class="screen" id="screen-{i}">{body}</div></div>')

combined = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EF Qatar Platform Screens</title>
{FONTS}
<style>
{CHROME}
    .bar {{ position: sticky; top: 0; z-index: 10; background: #1B1417; }}
    .bar-in {{ max-width: 1200px; margin: 0 auto; padding: 14px 40px; display: flex;
               align-items: center; gap: 28px; }}
    .lockup {{ display: flex; align-items: center; gap: 10px; }}
    .lockup .mark {{ width: 32px; height: 32px; border-radius: 4px; background: #FFFFFF;
                     display: flex; align-items: center; justify-content: center;
                     font-family: 'Source Serif 4', Georgia, serif; font-weight: 700;
                     font-size: 14px; color: #4B1527; }}
    .lockup .name {{ font-family: 'Source Serif 4', Georgia, serif; font-size: 14.5px;
                     font-weight: 600; color: #FFFFFF; }}
    .tabs {{ display: flex; gap: 6px; }}
    .tab {{ font-family: inherit; font-size: 13.5px; color: #B7ABB0; background: transparent;
            border: 1px solid #3A3135; border-radius: 4px; padding: 8px 16px; cursor: pointer; }}
    .tab:hover {{ color: #FFFFFF; }}
    .tab.is-on {{ color: #1B1417; background: #FFFFFF; border-color: #FFFFFF; }}
    .panel {{ display: none; }}
    .panel.is-on {{ display: block; }}
    .screen {{ background: #FBF9F8; }}
    #screen-2 {{ background: #EDE7E8; padding-bottom: 40px; }}
{chr(10).join('    ' + s for s in styles)}
</style>
</head>
<body>
<div class="bar"><div class="bar-in">
  <div class="lockup"><div class="mark">EF</div><div class="name">Engineers Forum Qatar</div></div>
  <div class="tabs">{''.join(tabs)}</div>
</div></div>
{''.join(panels)}
<script>
document.querySelectorAll('.tab').forEach(function (t) {{
  t.addEventListener('click', function () {{
    var i = t.dataset.i;
    document.querySelectorAll('.tab').forEach(function (x) {{ x.classList.toggle('is-on', x === t); }});
    document.querySelectorAll('.panel').forEach(function (p) {{
      p.classList.toggle('is-on', p.id === 'panel-' + i);
    }});
    window.scrollTo(0, 0);
  }});
}});
</script>
</body>
</html>
"""
(OUT / 'ef-qatar-screens.html').write_text(combined, encoding='utf-8')

# The Artifact host supplies its own doctype/html/head/body, so publish a variant
# carrying only the title, styles and markup.
inner = combined.split('<head>', 1)[1]
inner = inner.replace('</head>', '', 1).replace('<body>', '', 1)
inner = inner.rsplit('</body>', 1)[0]
inner = '\n'.join(l for l in inner.splitlines()
                  if '<meta charset' not in l and 'name="viewport"' not in l)
(OUT / 'ef-qatar-screens.artifact.html').write_text(inner.strip() + '\n', encoding='utf-8')

print('wrote:', ', '.join(sorted(p.name for p in OUT.glob('*.html'))))
