#!/usr/bin/env python3
"""EF Qatar public home page — desktop and mobile artboards.

Built to a brief from EF: a full-bleed slideshow hero with the heading over it,
then news, a month calendar, the monthly programme, how to apply, notices, and
direct routes to registration, the register, the marketplace and activities.

The hero cycles four slides on CSS keyframes — no script — with the progress
bars driven off the same timing, so it runs live in the canvas and in any
browser. Swapping the slideshow for a video is a later change: replace the four
slide layers with one <video>, keep the scrim and the overlay.

The calendar is generated from the real March 2027 month, so the weekday
alignment is correct rather than drawn.

Type: Newsreader carries headlines, Public Sans the interface and reading copy,
Quicksand the logo lockup alone — a proposed extension to the guideline, see
README. The eight photographs are generated placeholders, also see README.
"""
import calendar
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str((HERE / '..' / 'console').resolve()))
from build import lockup  # noqa: E402

MAROON = '#4B1728'
MAROON_D = '#2E0C19'
GREEN = '#4BB148'
GREEN_T = '#2A7F26'        # the brand green darkened until type on white clears 5:1
INK = '#191013'
BODY = '#3F383B'
MUTED = '#6E6569'
RULE = '#D7DCE3'
HAIR = '#E7EBF0'
BAND = '#F2F5F8'

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&'
         'family=Public+Sans:wght@400;500;600;700&'
         'family=Quicksand:wght@600;700&display=swap">')

CSS = """
    body { margin: 0; font-family: 'Public Sans', system-ui, sans-serif; background: #FFFFFF;
           color: #3F383B; -webkit-font-smoothing: antialiased; }
    * { box-sizing: border-box; }
    a { color: #2A7F26; text-decoration: none; }
    a:hover { color: #1F6019; text-decoration: underline; }
    h1, h2, h3, h4 { font-family: Newsreader, Georgia, serif; color: #191013; margin: 0;
                     font-weight: 500; letter-spacing: -0.005em; }
    p { margin: 0; }
    img { display: block; }
    .wrap { max-width: 1240px; margin: 0 auto; padding: 0 40px; }
    .kick { font-family: 'Public Sans', sans-serif; font-size: 11px; font-weight: 700;
            letter-spacing: 0.14em; color: #4B1728; text-transform: uppercase; }
    .kick-g { color: #2A7F26; }
    .kick-w { color: #7FCB7C; }
    .date { font-size: 12.5px; color: #6E6569; font-variant-numeric: tabular-nums; }
    .std { font-size: 15px; line-height: 1.62; color: #3F383B; }
    .sec { border-top: 3px solid #4B1728; padding-top: 14px; display: flex;
           align-items: baseline; justify-content: space-between; gap: 24px;
           margin-bottom: 26px; }
    .sec h2 { font-size: 28px; }
    .more { font-size: 14px; font-weight: 600; white-space: nowrap; }
    .btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px;
           height: 46px; padding: 0 24px; font-size: 15px; font-weight: 600;
           font-family: 'Public Sans', sans-serif; border: 1px solid transparent;
           white-space: nowrap; }
    .btn-m { background: #4B1728; color: #FFFFFF; }
    .btn-m:hover { background: #63203A; color: #FFFFFF; text-decoration: none; }
    .btn-g { background: #4BB148; color: #16290F; }
    .btn-g:hover { background: #43A340; color: #16290F; text-decoration: none; }
    .btn-o { background: #FFFFFF; color: #4B1728; border-color: #B9A3AC; }
    .btn-o:hover { border-color: #4B1728; color: #4B1728; text-decoration: none; }
    .btn-w { background: transparent; color: #FFFFFF; border-color: rgba(255,255,255,0.55); }
    .btn-w:hover { background: rgba(255,255,255,0.12); color: #FFFFFF;
                   border-color: #FFFFFF; text-decoration: none; }
    .nav-a { font-size: 14.5px; font-weight: 600; color: #191013; padding: 15px 0;
             border-bottom: 3px solid transparent; }
    .nav-a:hover { color: #4B1728; border-bottom-color: #4BB148; text-decoration: none; }
    .field { height: 42px; border: 1px solid #C3CAD3; background: #FFFFFF; display: flex;
             align-items: center; gap: 9px; padding: 0 13px; font-size: 14px; color: #6E6569;
             white-space: nowrap; overflow: hidden; }
    .tbc { font-family: 'Public Sans', sans-serif; font-size: 12px; font-weight: 600;
           color: #7C7378; border: 1px dashed #C3CAD3; padding: 3px 7px; white-space: nowrap; }
    .ph { position: absolute; right: 8px; bottom: 8px; font-family: 'Public Sans', sans-serif;
          font-size: 9.5px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;
          color: #FFFFFF; background: rgba(25, 16, 19, 0.72); padding: 3px 6px; }

    /* the hero slideshow: four layers crossfading on one 32s cycle, no script */
    .slide { position: absolute; inset: 0; opacity: 0; animation: shot 32s linear infinite; }
    @keyframes shot { 0% { opacity: 0; } 2% { opacity: 1; } 23% { opacity: 1; }
                      27% { opacity: 0; } 100% { opacity: 0; } }
    .slide-img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;
                 animation: drift 32s linear infinite; }
    @keyframes drift { 0% { transform: scale(1.06); } 27% { transform: scale(1.12); }
                       100% { transform: scale(1.12); } }
    /* the progress bars share the slides' timing */
    .bar { position: relative; width: 54px; height: 3px; background: rgba(255,255,255,0.32);
           overflow: hidden; }
    .bar span { position: absolute; inset: 0; background: #FFFFFF; transform-origin: left;
                transform: scaleX(0); animation: fill 32s linear infinite; }
    @keyframes fill { 0% { transform: scaleX(0); } 25% { transform: scaleX(1); }
                      25.6% { transform: scaleX(0); } 100% { transform: scaleX(0); } }
    /* the four routes below the hero */
    .route { display: flex; flex-direction: column; gap: 9px; padding: 26px 28px;
             border-left: 1px solid rgba(255,255,255,0.16); }
    .route:hover { background: rgba(255,255,255,0.07); text-decoration: none; }
    .route-t { font-family: Newsreader, serif; font-size: 20px; color: #FFFFFF; }
    .route-s { font-size: 13px; color: #C9B2BB; line-height: 1.45; }
    /* calendar */
    .cal-h { font-size: 11px; font-weight: 700; letter-spacing: 0.1em; color: #6E6569;
             text-transform: uppercase; text-align: center; padding-bottom: 8px; }
    .cal-d { aspect-ratio: 1 / 1; border: 1px solid #E7EBF0; display: flex;
             flex-direction: column; align-items: center; justify-content: center; gap: 5px;
             font-size: 14px; color: #3F383B; font-variant-numeric: tabular-nums; }
    .cal-dot { width: 6px; height: 6px; border-radius: 50%; }
"""

NAV = ['About EF', 'Membership', 'Register of members', 'Events', 'Learning',
       'Publications', 'Governance', 'Jobs']

# hero slides: image, kicker, heading, one supporting line
SLIDES = [
    ('hero-onam.jpg', 'Arts and culture',
     'The evenings that make a register into a community',
     'Music, performance and the festivals the community keeps — families welcome.'),
    ('hero-cricket.jpg', 'Sport',
     'Twelve teams, one season, every fixture recorded',
     'Tournaments through the year, with squads, waivers and emergency contacts held for '
     'every player.'),
    ('hero-seminar.jpg', 'Learning',
     'Seminars run by members, for members',
     'Technical sessions across the disciplines, recorded against your professional profile.'),
    ('hero-agm.jpg', 'Governance',
     'Eight hundred engineers, one elected committee',
     'Every approval, every payment and every decision recorded against the officer who '
     'made it.'),
]

ROUTES = [
    ('Apply for membership', 'Open to qualified engineers of Kerala origin in Qatar'),
    ('Register of members', 'Search 800 engineers by name, employer or discipline'),
    ('Marketplace', 'Partner offers and member-to-member listings'),
    ('Activities', 'Seminars, sport, arts and the annual programme'),
]

NEWS_LEAD = ('News', 'news-lead.jpg', 'Committee elected for the 2027 term',
             'The officers returned at the general meeting, and the portfolio each of them '
             'holds for the year. The Treasurer has published the accounts alongside the '
             'result.', '28 January 2027')

NEWS = [
    ('Sport', 'news-1.jpg', 'Cricket tournament returns on 27 March', '22 January 2027'),
    ('Arts', 'news-2.jpg', 'Arts evening to be held on 10 April', '18 January 2027'),
    ('Learning', 'news-3.jpg', 'Workshop programme set for the second quarter',
     '11 January 2027'),
]

# March 2027 — the calendar is generated, so the weekday alignment is real
CAL_YEAR, CAL_MONTH, CAL_TODAY = 2027, 3, 9
CAL_KINDS = {'Seminar': GREEN_T, 'Sport': '#B0762A', 'Arts': '#8A3A5A', 'Committee': MAROON}
CAL_EVENTS = {5: 'Committee', 14: 'Seminar', 20: 'Seminar', 27: 'Sport', 31: 'Committee'}

PROGRAMME = [
    ('5', 'Committee meeting', 'Committee', '19:30', 'Officers only'),
    ('14', 'Structural engineering seminar', 'Seminar', '18:30',
     '182 registered · 18 waiting'),
    ('20', 'Workshop: reinforced concrete detailing', 'Seminar', '18:00',
     'Places limited to 40'),
    ('27', 'EF cricket tournament 2027', 'Sport', '07:00', '12 teams entered'),
    ('31', 'Renewal window closes', 'Committee', '23:59', 'Dues QAR 500'),
]

NOTICES = [
    ('Notice of the Annual General Meeting', '12 February 2027',
     'Agenda, the Treasurer\'s statement and the papers for the meeting. Nominations for the '
     '2027 committee close on 28 February.'),
    ('Renewal of membership for 2027', '5 February 2027',
     'The renewal window is open until 31 March. Dues are QAR 500 for the year and a receipt '
     'is issued on payment.'),
    ('Amendment to the bylaws, clause 7', '21 January 2027',
     'Adopted at the general meeting. The consolidated bylaws are republished at v4.1.'),
]

FEES = [
    ('Ordinary Member', 'Qualified engineers of Kerala origin resident in Qatar',
     'QAR 500 a year', True),
    ('Associate Member', 'Engineering professionals in related disciplines',
     'Dues — EF to confirm', False),
    ('Student Member', 'Engineering students enrolled in Qatar', 'Dues — EF to confirm', False),
    ('Life Member', 'By resolution of the committee, for long-standing members',
     'One-off — EF to confirm', False),
]

STEPS = [
    ('Apply', 'Your qualification, your employment and a proposer in good standing.'),
    ('Verification', 'EF checks your documents against the originals.'),
    ('Decision', 'The committee decides within five business days, and records it.'),
    ('Your Digital ID', 'Pay your dues, and the credential is issued the same day.'),
]

OFFICERS = ['President', 'Secretary', 'Treasurer', 'Technical Secretary',
            'Marcoms Secretary', 'Sports Secretary', 'Arts Secretary']

DOCS = [
    ('Bylaws of Engineers Forum Qatar', 'v4.1'),
    ('Code of conduct and committee policies', 'v2.0'),
    ('Privacy notice', 'v2.0'),
    ('Register of past officers', '—'),
    ('Annual report and accounts', '—'),
]

FOOT = [
    ('About EF', ['What EF is', 'Governance', 'Officers and terms', 'Affiliation', 'Contact EF']),
    ('Membership', ['Who may join', 'Categories and dues', 'Apply', 'Renew',
                    'Member Digital ID']),
    ('Activities', ['Events calendar', 'Learning', 'Publications', 'Sport', 'Arts']),
    ('Community', ['Register of members', 'Jobs', 'Marketplace', 'Partner offers']),
    ('Legal', ['Bylaws', 'Policies', 'Privacy notice', 'Accessibility']),
]


def arrow(c=GREEN_T, s=13, w=2.6):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" '
            f'stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" '
            f'style="flex-shrink: 0;"><path d="M4 12h15M13 6l6 6-6 6"/></svg>')


def search_ico(c='#8A8288', s=15):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" '
            f'stroke-width="2" stroke-linecap="round" style="flex-shrink: 0;">'
            f'<circle cx="10.5" cy="10.5" r="6.6"/><path d="m21 21-5.8-5.8"/></svg>')


def tbc(t):
    return f'<span class="tbc">{t}</span>'


def photo(src, ratio, badge=True):
    tag = '<span class="ph">placeholder</span>' if badge else ''
    return (f'<div style="position: relative; background: {BAND};">'
            f'<img src="{src}" alt="" style="width: 100%; aspect-ratio: {ratio}; '
            f'object-fit: cover;">{tag}</div>')


def more(label):
    return (f'<a href="#" class="more" style="display: inline-flex; align-items: center; '
            f'gap: 7px;">{label} {arrow()}</a>')


def hero(h, title_px, lede_px, pad, mobile=False):
    """Four crossfading slide layers plus the progress bars, all on one 32s cycle."""
    layers = ''
    for k, (img, kick, head, line) in enumerate(SLIDES):
        d = f'animation-delay: {k * 8}s;'
        lede = ('' if mobile else
                f'<p style="font-size: {lede_px}px; line-height: 1.6; color: #E6D8DD; '
                f'max-width: 46ch;">{line}</p>')
        layers += f"""<div class="slide" style="{d}">
          <img class="slide-img" src="{img}" alt="" style="{d}">
          <div style="position: absolute; inset: 0; background:
               linear-gradient(180deg, rgba(24,10,16,0.34) 0%, rgba(24,10,16,0.04) 34%,
               rgba(24,10,16,0.10) 52%, rgba(24,10,16,0.78) 100%);"></div>
          <div style="position: absolute; inset: 0; background:
               linear-gradient(96deg, rgba(24,10,16,0.70) 0%, rgba(24,10,16,0.34) 40%,
               rgba(24,10,16,0) 66%);"></div>
          <div style="position: absolute; inset: 0; display: flex; flex-direction: column;
               justify-content: flex-end;">
            <div class="wrap" style="width: 100%; padding-bottom: {pad}px; display: flex;
                 flex-direction: column; gap: 14px;">
              <span class="kick kick-w">{kick}</span>
              <h1 style="font-size: {title_px}px; line-height: 1.1; color: #FFFFFF;
                   max-width: 20ch;">{head}</h1>
              {lede}
            </div>
          </div>
        </div>"""

    bars = ''.join(f'<div class="bar"><span style="animation-delay: {k * 8}s;"></span></div>'
                   for k in range(len(SLIDES)))

    return f"""<div style="position: relative; height: {h}px; overflow: hidden;
         background: {MAROON_D};">
      {layers}
      <span class="ph" style="right: 16px; top: 16px; bottom: auto;">placeholder</span>
      <div style="position: absolute; left: 0; right: 0; bottom: {pad - 26}px;">
        <div class="wrap" style="display: flex; align-items: center; gap: 9px;">{bars}</div>
      </div>
    </div>"""


def routes_band(mobile=False):
    """The four things people come to the site to do, immediately under the hero."""
    cells = ''.join(f"""<a href="#" class="route"
         style="{'border-left: none; border-top: 1px solid rgba(255,255,255,0.16);' if mobile else ''}">
      <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px;">
        <span class="route-t">{t}</span>{arrow('#7FCB7C', 15, 2.4)}
      </div>
      <span class="route-s">{s}</span>
    </a>""" for t, s in ROUTES)
    cols = ('1fr' if mobile else 'repeat(4, minmax(0, 1fr))')
    return f"""<div style="background: {MAROON};">
      <div class="wrap" style="padding: 0 40px; display: grid; grid-template-columns: {cols};">
        {cells}
      </div>
    </div>"""


def calendar_grid(cell_font=14):
    weeks = calendar.Calendar(firstweekday=0).monthdayscalendar(CAL_YEAR, CAL_MONTH)
    heads = ''.join(f'<div class="cal-h">{d}</div>'
                    for d in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    cells = ''
    for wk in weeks:
        for d in wk:
            if d == 0:
                cells += f'<div class="cal-d" style="border-color: transparent;"></div>'
                continue
            kind = CAL_EVENTS.get(d)
            dot = (f'<span class="cal-dot" style="background: {CAL_KINDS[kind]};"></span>'
                   if kind else '<span style="width: 6px; height: 6px;"></span>')
            today = d == CAL_TODAY
            style = (f'background: {MAROON}; border-color: {MAROON}; color: #FFFFFF; '
                     f'font-weight: 700;' if today else
                     (f'background: #FFFFFF; font-weight: 600; color: {INK};' if kind
                      else 'background: #FFFFFF;'))
            cells += (f'<div class="cal-d" style="{style} font-size: {cell_font}px;">'
                      f'<span>{d}</span>{dot}</div>')
    legend = ''.join(f"""<span style="display: inline-flex; align-items: center; gap: 6px;
         font-size: 12.5px; color: {MUTED};">
      <span class="cal-dot" style="background: {c};"></span>{k}</span>"""
                     for k, c in CAL_KINDS.items())
    return f"""<div style="display: flex; flex-direction: column; gap: 14px;">
      <div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 0;">
        {heads}
      </div>
      <div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 0;
           margin-top: -8px;">{cells}</div>
      <div style="display: flex; flex-wrap: wrap; gap: 10px 18px; padding-top: 4px;">
        {legend}</div>
    </div>"""


def programme_rows(compact=False):
    return ''.join(f"""<div style="display: grid;
         grid-template-columns: 34px minmax(0, 1fr) {'' if compact else '150px '}104px;
         gap: {14 if compact else 20}px; align-items: center; padding: {13 if compact else 15}px 0;
         border-top: 1px solid {HAIR};">
      <span style="font-family: Newsreader, serif; font-size: 20px; color: {INK};
            font-variant-numeric: tabular-nums;">{d}</span>
      <div style="display: flex; flex-direction: column; gap: 4px; min-width: 0;">
        <span style="font-size: 15px; font-weight: 600; color: {INK}; line-height: 1.35;">{t}</span>
        <span style="font-size: 12.5px; color: {MUTED};">{time} · {tbc('Venue')}
          <span style="display: inline-flex; align-items: center; gap: 5px; padding-left: 4px;">
            <span class="cal-dot" style="background: {CAL_KINDS[kind]};"></span>{kind}</span></span>
      </div>
      {'' if compact else f'<span style="font-size: 13px; color: {MUTED};">{note}</span>'}
      <a href="#" class="btn btn-o" style="height: 36px; padding: 0 16px; font-size: 13px;">
        Details</a>
    </div>""" for d, t, kind, time, note in PROGRAMME)


# ======================================================================= desktop
def home():
    nav = ''.join(f'<a href="#" class="nav-a">{n}</a>' for n in NAV)

    utility = f"""<div style="background: {MAROON_D};">
      <div class="wrap" style="height: 36px; display: flex; align-items: center;
           justify-content: space-between; gap: 24px; font-size: 12.5px;">
        <span style="color: #C9B2BB;">Affiliated to the Indian Business and Professional
          Council, under the Embassy of India in Qatar</span>
        <div style="display: flex; align-items: center; gap: 22px;">
          <a href="#" style="color: #C9B2BB;">Contact EF</a>
          <a href="#" style="color: #C9B2BB;">Accessibility</a>
          <a href="#" style="color: #FFFFFF; font-weight: 600;">Member sign in</a>
        </div>
      </div>
    </div>"""

    masthead = f"""<div class="wrap" style="height: 96px; display: flex; align-items: center;
         justify-content: space-between; gap: 40px;">
      {lockup()}
      <div style="display: flex; align-items: center; gap: 14px;">
        <div class="field" style="width: 244px;">{search_ico()}<span>Search this site</span></div>
        <a href="#" class="btn btn-m">Apply for membership</a>
      </div>
    </div>
    <div style="border-top: 1px solid {RULE};">
      <div class="wrap" style="display: flex; align-items: center; gap: 30px;">{nav}</div>
    </div>"""

    notice_bar = f"""<div style="background: {BAND}; border-bottom: 1px solid {RULE};">
      <div class="wrap" style="padding: 17px 40px; display: flex; align-items: center;
           justify-content: space-between; gap: 28px;">
        <div style="display: flex; align-items: center; gap: 14px;">
          <span class="kick kick-g">Notice</span>
          <span style="width: 1px; height: 16px; background: {RULE};"></span>
          <span style="font-size: 15px; color: {INK};">Renewal for 2027 is open until
            <strong style="font-weight: 600;">31 March</strong>. Nominations for the committee
            close on 28 February.</span>
        </div>
        {more('All notices')}
      </div>
    </div>"""

    kick, img, title, std, date = NEWS_LEAD
    small = ''.join(f"""<a href="#" style="display: grid;
         grid-template-columns: 118px minmax(0, 1fr); gap: 16px; padding: 16px 0;
         border-top: 1px solid {HAIR}; align-items: start;">
      {photo(i, '3 / 2', badge=False)}
      <div style="display: flex; flex-direction: column; gap: 6px;">
        <span class="kick">{k}</span>
        <h4 style="font-size: 17px; line-height: 1.3;">{t}</h4>
        <span class="date">{d}</span>
      </div>
    </a>""" for k, i, t, d in NEWS)

    news_sec = f"""<div class="wrap" style="padding-top: 58px;">
      <div class="sec"><h2>News</h2>{more('All news')}</div>
      <div style="display: grid; grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr);
           gap: 44px;">
        <a href="#" style="display: flex; flex-direction: column; gap: 15px;">
          {photo(img, '3 / 2')}
          <span class="kick">{kick}</span>
          <h3 style="font-size: 30px; line-height: 1.18;">{title}</h3>
          <p class="std" style="font-size: 16px;">{std}</p>
          <span class="date">{date}</span>
        </a>
        <div style="display: flex; flex-direction: column;">{small}</div>
      </div>
    </div>"""

    cal_sec = f"""<div style="background: {BAND}; border-top: 1px solid {RULE};
         margin-top: 60px;">
      <div class="wrap" style="padding-top: 52px; padding-bottom: 56px;">
        <div class="sec"><h2>March at EF</h2>{more('The full calendar')}</div>
        <div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.28fr);
             gap: 52px; align-items: start;">
          <div style="display: flex; flex-direction: column; gap: 16px;">
            <div style="display: flex; align-items: baseline; justify-content: space-between;">
              <h3 style="font-size: 21px;">March 2027</h3>
              <div style="display: flex; align-items: center; gap: 8px;">
                <a href="#" class="btn btn-o" style="height: 32px; width: 32px; padding: 0;">
                  &lsaquo;</a>
                <a href="#" class="btn btn-o" style="height: 32px; width: 32px; padding: 0;">
                  &rsaquo;</a>
              </div>
            </div>
            {calendar_grid()}
          </div>
          <div style="display: flex; flex-direction: column; gap: 14px;">
            <h3 style="font-size: 21px;">This month's programme</h3>
            <div style="border-bottom: 1px solid {HAIR};">{programme_rows()}</div>
            <div style="display: flex; align-items: center; gap: 16px; padding-top: 4px;">
              <a href="#" class="btn btn-m">Book a place</a>
              {more('Add the calendar to your diary')}
            </div>
          </div>
        </div>
      </div>
    </div>"""

    fee_rows = ''.join(f"""<div style="display: grid;
         grid-template-columns: 168px minmax(0, 1fr) 158px; gap: 20px; padding: 14px 0;
         border-top: 1px solid {RULE}; align-items: baseline;">
      <span style="font-size: 14.5px; font-weight: 600; color: {INK};">{cat}</span>
      <span style="font-size: 14px; color: {BODY}; line-height: 1.5;">{who}</span>
      {f'<span style="font-size: 14.5px; font-weight: 600; color: {INK};">{dues}</span>'
         if known else tbc(dues)}
    </div>""" for cat, who, dues, known in FEES)

    step_cells = ''.join(f"""<div style="display: flex; flex-direction: column; gap: 8px;
         padding: 22px 20px; border-left: 1px solid rgba(255,255,255,0.16);">
      <span style="font-family: Newsreader, serif; font-size: 27px; color: {GREEN};
            line-height: 1;">{k + 1}</span>
      <span style="font-size: 15px; font-weight: 600; color: #FFFFFF;">{t}</span>
      <span style="font-size: 13px; line-height: 1.5; color: #C9B2BB;">{d}</span>
    </div>""" for k, (t, d) in enumerate(STEPS))

    apply_sec = f"""<div class="wrap" style="padding-top: 60px;">
      <div class="sec"><h2>How to apply</h2>{more('Membership in full')}</div>
      <div style="background: {MAROON}; display: grid;
           grid-template-columns: repeat(4, minmax(0, 1fr));">{step_cells}</div>
      <div style="display: grid; grid-template-columns: minmax(0, 1.6fr) minmax(0, 1fr);
           gap: 52px; align-items: start; padding-top: 40px;">
        <div style="display: flex; flex-direction: column; gap: 16px;">
          <h3 style="font-size: 22px;">Categories and dues</h3>
          <div>
            <div style="display: grid; grid-template-columns: 168px minmax(0, 1fr) 158px;
                 gap: 20px; padding-bottom: 9px;">
              <span class="kick">Category</span><span class="kick">Who it is for</span>
              <span class="kick">Dues</span>
            </div>
            <div style="border-bottom: 1px solid {RULE};">{fee_rows}</div>
          </div>
          <p style="font-size: 13.5px; color: {MUTED}; line-height: 1.55;">Dues are set
            annually by the committee and confirmed at the general meeting.</p>
        </div>
        <div style="border: 1px solid {RULE}; padding: 26px; display: flex;
             flex-direction: column; gap: 13px;">
          <span class="kick kick-g">Registration</span>
          <h3 style="font-size: 20px; line-height: 1.26;">Start your application</h3>
          <p style="font-size: 14.5px; line-height: 1.6; color: {BODY};">You will need your
            qualification, proof of employment, your Qatar ID and a proposer in good standing.
            The committee decides within five business days.</p>
          <a href="#" class="btn btn-m" style="margin-top: 4px;">Register and apply</a>
          <a href="#" class="btn btn-o">Renew an existing membership</a>
        </div>
      </div>
    </div>"""

    notice_rows = ''.join(f"""<a href="#" style="display: grid;
         grid-template-columns: 148px minmax(0, 1fr) 24px; gap: 26px; padding: 20px 0;
         border-top: 1px solid {HAIR}; align-items: start;">
      <span class="date" style="padding-top: 3px;">{d}</span>
      <div style="display: flex; flex-direction: column; gap: 6px;">
        <h3 style="font-size: 19px; line-height: 1.3;">{t}</h3>
        <p style="font-size: 14px; line-height: 1.6; color: {BODY};">{b}</p>
      </div>
      <span style="padding-top: 6px;">{arrow()}</span>
    </a>""" for t, d, b in NOTICES)

    notices_sec = f"""<div class="wrap" style="padding-top: 60px;">
      <div class="sec"><h2>Notices</h2>{more('The notice board')}</div>
      <div style="border-bottom: 1px solid {HAIR};">{notice_rows}</div>
    </div>"""

    register_sec = f"""<div style="background: {BAND}; border-top: 1px solid {RULE};
         margin-top: 60px;">
      <div class="wrap" style="padding-top: 52px; padding-bottom: 54px;">
        <div class="sec"><h2>The register of members</h2>{more('About the register')}</div>
        <div style="display: grid; grid-template-columns: minmax(0, 1.6fr) minmax(0, 1fr);
             gap: 52px; align-items: start;">
          <div style="display: flex; flex-direction: column; gap: 16px;">
            <p class="std" style="font-size: 16px; max-width: 60ch;">Eight hundred engineers,
              searchable by name, employer, discipline and membership category. Each member
              decides, section by section, what the register discloses — and that decision is
              enforced on every route, including the mobile application.</p>
            <div style="display: flex; align-items: center; gap: 12px;">
              <div class="field" style="width: 320px;">{search_ico()}
                <span>Name, employer or discipline</span></div>
              <a href="#" class="btn btn-o">Search the register</a>
            </div>
            <p style="font-size: 13.5px; color: {MUTED};">Open to members in good standing.
              Sign in to search it.</p>
          </div>
          <div style="border: 1px solid {RULE}; background: #FFFFFF; padding: 26px;
               display: flex; flex-direction: column; gap: 13px;">
            <span class="kick kick-g">For partners and employers</span>
            <h3 style="font-size: 20px; line-height: 1.26;">Verify a membership</h3>
            <p style="font-size: 14.5px; line-height: 1.6; color: {BODY};">Confirm a membership
              from the member's Digital ID. Only the fields EF has configured for your partner
              type are returned, and verification fails the day a membership lapses.</p>
            <div class="field"><span>Membership number</span></div>
            <a href="#" class="btn btn-o">Verify</a>
          </div>
        </div>
      </div>
    </div>"""

    off_rows = ''.join(f"""<div style="display: grid;
         grid-template-columns: minmax(0, 1fr) 176px 62px; gap: 18px; padding: 12px 0;
         border-top: 1px solid {RULE}; align-items: baseline;">
      <span style="font-size: 14.5px; font-weight: 600; color: {INK};">{o}</span>
      {tbc('Name — EF to supply')}
      <span style="font-size: 13px; color: {MUTED};">2027</span>
    </div>""" for o in OFFICERS)

    doc_rows = ''.join(f"""<div style="display: flex; align-items: baseline;
         justify-content: space-between; gap: 18px; padding: 12px 0;
         border-top: 1px solid {RULE};">
      <a href="#" style="font-size: 14.5px; font-weight: 600;">{t}</a>
      <span style="font-size: 13px; color: {MUTED}; font-variant-numeric: tabular-nums;">{v}</span>
    </div>""" for t, v in DOCS)

    gov_sec = f"""<div class="wrap" style="padding-top: 60px; padding-bottom: 66px;">
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 52px;
           align-items: start;">
        <div>
          <div class="sec"><h2>The committee</h2>{more('Past officers')}</div>
          <div style="border-bottom: 1px solid {RULE};">{off_rows}</div>
        </div>
        <div>
          <div class="sec"><h2>Published documents</h2>{more('All publications')}</div>
          <div style="border-bottom: 1px solid {RULE};">{doc_rows}</div>
        </div>
      </div>
    </div>"""

    fcols = ''.join(
        f"""<div style="display: flex; flex-direction: column; gap: 11px;">
          <span class="kick" style="color: #E4CFD6;">{h}</span>
          {''.join(f'<a href="#" style="font-size: 14px; color: #C9B2BB;">{i}</a>'
                   for i in items)}
        </div>""" for h, items in FOOT)

    footer = f"""<div style="background: {MAROON_D};">
      <div class="wrap" style="padding-top: 52px; padding-bottom: 30px;">
        <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr));
             gap: 34px;">{fcols}</div>
        <div style="border-top: 1px solid #5A2337; margin-top: 44px; padding-top: 26px;
             display: grid; grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); gap: 40px;">
          <div style="display: flex; flex-direction: column; gap: 13px;">
            {lockup(reversed_=True)}
            <p style="font-size: 13.5px; line-height: 1.7; color: #A98D97; max-width: 46ch;">
              The apex body of engineers of Kerala origin working in the State of Qatar.
              Affiliated to the Indian Business and Professional Council, under the Embassy of
              India in Qatar.</p>
          </div>
          <div style="display: flex; flex-direction: column; gap: 9px; align-items: flex-start;">
            <span class="kick" style="color: #E4CFD6;">Contact</span>
            <span class="tbc" style="color: #C9B2BB; border-color: #7A4056;">Address — EF to
              supply</span>
            <span class="tbc" style="color: #C9B2BB; border-color: #7A4056;">Email — EF to
              supply</span>
          </div>
        </div>
        <div style="border-top: 1px solid #5A2337; margin-top: 26px; padding-top: 20px;
             display: flex; align-items: center; justify-content: space-between; gap: 24px;">
          <span style="font-size: 12.5px; color: #A98D97;">© 2027 Engineers Forum Qatar.</span>
          <span style="font-size: 12.5px; color: #A98D97;">Personal data held in the State of
            Qatar.</span>
        </div>
      </div>
    </div>"""

    body = (utility + masthead + hero(624, 46, 16.5, 68) + routes_band() + notice_bar
            + news_sec + cal_sec + apply_sec + notices_sec + register_sec + gov_sec + footer)
    return wrap_dc(body, 1440, 5300)


# ======================================================================== mobile
def home_mobile():
    burger = ('<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#191013" '
              'stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>')

    kick, img, title, std, date = NEWS_LEAD
    small = ''.join(f"""<a href="#" style="display: grid;
         grid-template-columns: 104px minmax(0, 1fr); gap: 14px; padding: 15px 0;
         border-top: 1px solid {HAIR}; align-items: start;">
      {photo(i, '3 / 2', badge=False)}
      <div style="display: flex; flex-direction: column; gap: 5px;">
        <span class="kick" style="font-size: 10px;">{k}</span>
        <h4 style="font-size: 15.5px; line-height: 1.3;">{t}</h4>
        <span class="date" style="font-size: 12px;">{d}</span>
      </div>
    </a>""" for k, i, t, d in NEWS)

    fee_rows = ''.join(f"""<div style="padding: 13px 0; border-top: 1px solid {RULE};
         display: flex; flex-direction: column; gap: 5px;">
      <div style="display: flex; align-items: baseline; justify-content: space-between;
           gap: 12px;">
        <span style="font-size: 14.5px; font-weight: 600; color: {INK};">{cat}</span>
        {f'<span style="font-size: 14px; font-weight: 600; color: {INK}; white-space: nowrap;">{dues}</span>'
           if known else tbc(dues)}
      </div>
      <span style="font-size: 13.5px; color: {BODY}; line-height: 1.5;">{who}</span>
    </div>""" for cat, who, dues, known in FEES)

    step_rows = ''.join(f"""<div style="display: grid; grid-template-columns: 30px minmax(0, 1fr);
         gap: 13px; padding: 15px 0; border-top: 1px solid rgba(255,255,255,0.16);
         align-items: start;">
      <span style="font-family: Newsreader, serif; font-size: 22px; color: {GREEN};
            line-height: 1.1;">{k + 1}</span>
      <div style="display: flex; flex-direction: column; gap: 4px;">
        <span style="font-size: 14.5px; font-weight: 600; color: #FFFFFF;">{t}</span>
        <span style="font-size: 13px; line-height: 1.5; color: #C9B2BB;">{d}</span>
      </div>
    </div>""" for k, (t, d) in enumerate(STEPS))

    notice_rows = ''.join(f"""<a href="#" style="display: flex; flex-direction: column; gap: 6px;
         padding: 16px 0; border-top: 1px solid {HAIR};">
      <span class="date" style="font-size: 12px;">{d}</span>
      <h3 style="font-size: 17px; line-height: 1.3;">{t}</h3>
      <p style="font-size: 13.5px; line-height: 1.6; color: {BODY};">{b}</p>
    </a>""" for t, d, b in NOTICES)

    off_rows = ''.join(f"""<div style="display: flex; align-items: baseline;
         justify-content: space-between; gap: 14px; padding: 11px 0;
         border-top: 1px solid {RULE};">
      <span style="font-size: 14px; font-weight: 600; color: {INK};">{o}</span>
      {tbc('EF to supply')}
    </div>""" for o in OFFICERS)

    doc_rows = ''.join(f"""<div style="display: flex; align-items: baseline;
         justify-content: space-between; gap: 14px; padding: 11px 0;
         border-top: 1px solid {RULE};">
      <a href="#" style="font-size: 14px; font-weight: 600;">{t}</a>
      <span style="font-size: 12.5px; color: {MUTED};">{v}</span>
    </div>""" for t, v in DOCS)

    def sec(title, link, content, band=False, pad=38):
        return f"""<div style="{f'background: {BAND}; border-top: 1px solid {RULE};' if band else ''}">
          <div style="padding: {pad}px 20px {30 if band else 0}px;">
            <div class="sec" style="margin-bottom: 20px;">
              <h2 style="font-size: 23px;">{title}</h2>{more(link) if link else ''}</div>
            {content}
          </div>
        </div>"""

    ftop = ''.join(f"""<div style="display: flex; flex-direction: column; gap: 9px;">
      <span class="kick" style="color: #E4CFD6; font-size: 10px;">{h}</span>
      {''.join(f'<a href="#" style="font-size: 13.5px; color: #C9B2BB;">{i}</a>' for i in items)}
    </div>""" for h, items in FOOT[:4])

    body = f"""
  <div style="background: {MAROON_D}; padding: 9px 20px; display: flex;
       justify-content: center;">
    <span style="font-size: 11.5px; color: #C9B2BB; text-align: center; line-height: 1.4;">
      Affiliated to the Indian Business and Professional Council</span>
  </div>
  <div style="padding: 13px 20px; display: flex; align-items: center;
       justify-content: space-between; gap: 14px; border-bottom: 1px solid {RULE};">
    {lockup()}
    <div style="display: flex; align-items: center; gap: 4px;">
      <a href="#" style="width: 44px; height: 44px; display: flex; align-items: center;
         justify-content: center;">{search_ico('#191013', 20)}</a>
      <a href="#" style="width: 44px; height: 44px; display: flex; align-items: center;
         justify-content: center;">{burger}</a>
    </div>
  </div>

  {hero(430, 27, 14, 30, mobile=True)}
  {routes_band(mobile=True)}

  <div style="background: {BAND}; border-bottom: 1px solid {RULE}; padding: 16px 20px;
       display: flex; flex-direction: column; gap: 9px;">
    <span class="kick kick-g">Notice</span>
    <span style="font-size: 14.5px; line-height: 1.55; color: {INK};">Renewal for 2027 is open
      until <strong style="font-weight: 600;">31 March</strong>. Nominations close on
      28 February.</span>
    {more('All notices')}
  </div>

  {sec('News', 'All news',
       f'''<a href="#" style="display: flex; flex-direction: column; gap: 12px;">
         {photo(img, '3 / 2')}
         <span class="kick" style="font-size: 10px;">{kick}</span>
         <h3 style="font-size: 23px; line-height: 1.2;">{title}</h3>
         <p class="std" style="font-size: 14.5px;">{std}</p>
         <span class="date" style="font-size: 12px;">{date}</span>
       </a><div style="padding-top: 6px;">{small}</div>''')}

  {sec('March at EF', 'Full calendar',
       f'''<div style="display: flex; align-items: baseline; justify-content: space-between;
            margin-bottom: 12px;"><h3 style="font-size: 19px;">March 2027</h3></div>
       {calendar_grid(13)}
       <h3 style="font-size: 19px; padding-top: 26px;">This month's programme</h3>
       <div style="border-bottom: 1px solid {HAIR}; margin-top: 8px;">{programme_rows(True)}</div>
       <a href="#" class="btn btn-m" style="width: 100%; margin-top: 18px;">Book a place</a>''',
       band=True)}

  <div style="padding: 38px 20px 0;">
    <div class="sec" style="margin-bottom: 20px;"><h2 style="font-size: 23px;">How to
      apply</h2></div>
    <div style="background: {MAROON}; padding: 6px 20px 20px;">{step_rows}</div>
    <h3 style="font-size: 19px; padding-top: 26px;">Categories and dues</h3>
    <div style="border-bottom: 1px solid {RULE}; margin-top: 8px;">{fee_rows}</div>
    <div style="border: 1px solid {RULE}; padding: 20px; margin-top: 24px; display: flex;
         flex-direction: column; gap: 12px;">
      <span class="kick kick-g">Registration</span>
      <h3 style="font-size: 18px; line-height: 1.26;">Start your application</h3>
      <p style="font-size: 14px; line-height: 1.6; color: {BODY};">You will need your
        qualification, proof of employment, your Qatar ID and a proposer in good standing.</p>
      <a href="#" class="btn btn-m">Register and apply</a>
      <a href="#" class="btn btn-o">Renew an existing membership</a>
    </div>
  </div>

  {sec('Notices', 'Notice board',
       f'<div style="border-bottom: 1px solid {HAIR};">' + notice_rows + '</div>')}

  {sec('The register of members', 'About it',
       '<p class="std" style="font-size: 15px; margin-bottom: 14px;">Eight hundred engineers, '
       'searchable by name, employer, discipline and category. Each member decides, section by '
       'section, what the register discloses.</p>'
       '<div class="field" style="margin-bottom: 12px;">' + search_ico()
       + '<span>Name, employer or discipline</span></div>'
       '<a href="#" class="btn btn-o" style="width: 100%;">Search the register</a>'
       f'<div style="border: 1px solid {RULE}; background: #FFFFFF; padding: 20px; '
       'margin-top: 22px; display: flex; flex-direction: column; gap: 12px;">'
       '<span class="kick kick-g">For partners and employers</span>'
       '<h3 style="font-size: 18px; line-height: 1.28;">Verify a membership</h3>'
       f'<p style="font-size: 14px; line-height: 1.6; color: {BODY};">Confirm a membership from '
       "the member's Digital ID. Only the fields EF has configured for your partner type are "
       'returned.</p><div class="field"><span>Membership number</span></div>'
       '<a href="#" class="btn btn-o">Verify</a></div>', band=True)}

  {sec('The committee', 'Past officers',
       f'<div style="border-bottom: 1px solid {RULE};">' + off_rows + '</div>')}
  {sec('Published documents', 'All publications',
       f'<div style="border-bottom: 1px solid {RULE};">' + doc_rows + '</div>')}

  <div style="background: {MAROON_D}; margin-top: 40px; padding: 32px 20px 24px; display: flex;
       flex-direction: column; gap: 22px;">
    {lockup(reversed_=True)}
    <p style="font-size: 13.5px; line-height: 1.7; color: #A98D97;">The apex body of engineers
      of Kerala origin working in the State of Qatar.</p>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));
         gap: 22px;">{ftop}</div>
    <span style="font-size: 12px; color: #A98D97; border-top: 1px solid #5A2337;
          padding-top: 18px; line-height: 1.6;">© 2027 Engineers Forum Qatar. Personal data
      held in the State of Qatar.</span>
  </div>
"""
    return wrap_dc(body, 390, 6900)


def wrap_dc(body, w, h):
    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  {FONTS}
  <style>{CSS}  </style>
</helmet>

<div style="width: {w}px; background: #FFFFFF;">{body}</div>
</x-dc>
<script data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{}}
</script>
</body>
</html>
"""


if __name__ == '__main__':
    for name, html in [('Main.dc.html', home()), ('HomeMobile.dc.html', home_mobile())]:
        (HERE / name).write_text(html, encoding='utf-8')
        print('wrote', name, len(html), 'bytes')
