#!/usr/bin/env python3
"""EF Qatar public home page — desktop and mobile artboards.

Designed as a learned society publishes, not as a product landing page. The
conventions it follows — a news-led lead story, a densely populated navigation,
a kicker and a date on everything, hairline rules instead of shadowed cards, and
information (categories, dues, officers, published documents) in place of
persuasion — are the genre's, worked from first principles. royalsociety.org and
istructe.org were both blocked from this environment, and neither society's
design is reproduced here in any case.

Deliberately absent, because they made the previous draft read as marketing: a
centred value proposition with paired buttons, a floating image collage, a
statistics band, an icon trio of "pillars", a testimonial, and a closing
call-to-action banner.

Type: Newsreader carries editorial headlines, Public Sans the interface and
reading copy, and Quicksand is held back for the logo lockup alone. The serif is
a proposed extension to the guideline — see README.

The seven photographs in images/ are generated placeholders — see README.
"""
import pathlib, sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str((HERE / '..' / 'console').resolve()))
from build import lockup  # noqa: E402

MAROON = '#4B1728'
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
    /* the category label an institution sets above every headline */
    .kick { font-family: 'Public Sans', sans-serif; font-size: 11px; font-weight: 700;
            letter-spacing: 0.14em; color: #4B1728; text-transform: uppercase; }
    .kick-g { color: #2A7F26; }
    .date { font-size: 12.5px; color: #6E6569; font-variant-numeric: tabular-nums; }
    .std { font-size: 15px; line-height: 1.62; color: #3F383B; }
    /* a section head: maroon rule, title, and the route to the full listing */
    .sec { border-top: 3px solid #4B1728; padding-top: 14px; display: flex;
           align-items: baseline; justify-content: space-between; gap: 24px;
           margin-bottom: 26px; }
    .sec h2 { font-size: 27px; }
    .more { font-size: 14px; font-weight: 600; white-space: nowrap; }
    .btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px;
           height: 44px; padding: 0 22px; font-size: 14.5px; font-weight: 600;
           font-family: 'Public Sans', sans-serif; border: 1px solid transparent;
           white-space: nowrap; }
    .btn-m { background: #4B1728; color: #FFFFFF; }
    .btn-m:hover { background: #63203A; color: #FFFFFF; text-decoration: none; }
    .btn-o { background: #FFFFFF; color: #4B1728; border-color: #B9A3AC; }
    .btn-o:hover { border-color: #4B1728; color: #4B1728; text-decoration: none; }
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
"""

NAV = ['About EF', 'Membership', 'Register of members', 'Events', 'Learning',
       'Publications', 'Governance', 'Jobs']

BRIEFS = [
    ('News', 'brief-renewal.jpg', 'Renewal for 2027 opens on 1 March', '5 February 2027'),
    ('Event', 'brief-seminar.jpg', 'Structural engineering seminar, 14 March', '4 February 2027'),
    ('Register', 'brief-register.jpg', 'The register moves to member-managed visibility',
     '28 January 2027'),
    ('Governance', 'news-committee.jpg', 'Annual report and accounts for 2026 published',
     '21 January 2027'),
]

NEWS = [
    ('News', 'news-committee.jpg', 'Committee elected for the 2027 term',
     'The officers returned at the general meeting, and the portfolio each of them holds '
     'for the year.', '28 January 2027'),
    ('Sport', 'news-tournament.jpg', 'Cricket tournament returns on 27 March',
     'Twelve teams are entered. Fixtures, waivers and emergency contacts are held against '
     'each squad.', '22 January 2027'),
    ('Arts', 'news-arts.jpg', 'Arts evening to be held on 10 April',
     'The programme is being assembled by the Arts Secretary. Members may bring their '
     'families.', '18 January 2027'),
]

EVENTS = [
    ('MAR', '14', 'Structural engineering seminar', '18:30', 'Seminar',
     '182 registered · 18 on the waiting list'),
    ('MAR', '27', 'EF cricket tournament 2027', '07:00', 'Sport', '12 teams entered'),
    ('APR', '10', 'Arts evening', '19:00', 'Arts', 'Families welcome'),
    ('APR', '24', 'Workshop: reinforced concrete detailing', '18:00', 'Workshop',
     'Places limited to 40'),
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
    'Apply with your qualification, your employment and a proposer in good standing.',
    'EF verifies your documents against the originals.',
    'The committee decides within five business days, and the decision is recorded.',
    'Pay your dues, and your Member Digital ID is issued the same day.',
]

OFFICERS = ['President', 'Secretary', 'Treasurer', 'Technical Secretary',
            'Marcoms Secretary', 'Sports Secretary', 'Arts Secretary']

DOCS = [
    ('Bylaws of Engineers Forum Qatar', 'v4.1', 'Adopted — EF to supply'),
    ('Code of conduct and committee policies', 'v2.0', 'Adopted — EF to supply'),
    ('Privacy notice', 'v2.0', 'Personal data held in the State of Qatar'),
    ('Register of past officers', '—', 'Maintained by the Secretary'),
    ('Annual report and accounts', '—', 'Year — EF to supply'),
]

FOOT = [
    ('About EF', ['What EF is', 'Governance', 'Officers and terms', 'Affiliation', 'Contact EF']),
    ('Membership', ['Who may join', 'Categories and dues', 'Apply', 'Renew',
                    'Member Digital ID']),
    ('Activities', ['Events', 'Learning', 'Publications', 'Sport', 'Arts']),
    ('Community', ['Register of members', 'Jobs', 'Marketplace', 'Partner offers']),
    ('Legal', ['Bylaws', 'Policies', 'Privacy notice', 'Accessibility']),
]


def arrow(c=GREEN_T):
    return (f'<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="{c}" '
            f'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" '
            f'style="flex-shrink: 0;"><path d="M4 12h15M13 6l6 6-6 6"/></svg>')


def search_ico(c='#8A8288', s=15):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" '
            f'stroke-width="2" stroke-linecap="round" style="flex-shrink: 0;">'
            f'<circle cx="10.5" cy="10.5" r="6.6"/><path d="m21 21-5.8-5.8"/></svg>')


def tbc(t):
    return f'<span class="tbc">{t}</span>'


def photo(src, ratio, badge=True):
    """An editorial image: square corners, no shadow, marked as a placeholder."""
    tag = '<span class="ph">placeholder</span>' if badge else ''
    return (f'<div style="position: relative; background: {BAND};">'
            f'<img src="{src}" alt="" style="width: 100%; aspect-ratio: {ratio}; '
            f'object-fit: cover;">{tag}</div>')


def more(label):
    return (f'<a href="#" class="more" style="display: inline-flex; align-items: center; '
            f'gap: 7px;">{label} {arrow()}</a>')


# ======================================================================= desktop
def home():
    nav = ''.join(f'<a href="#" class="nav-a">{n}</a>' for n in NAV)

    utility = f"""<div style="background: {MAROON};">
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
        <div class="field" style="width: 252px;">{search_ico()}<span>Search this site</span></div>
        <a href="#" class="btn btn-m">Apply for membership</a>
      </div>
    </div>
    <div style="border-top: 1px solid {RULE}; border-bottom: 1px solid {RULE};">
      <div class="wrap" style="display: flex; align-items: center; gap: 30px;">{nav}</div>
    </div>"""

    briefs = ''.join(f"""<a href="#" style="display: grid;
         grid-template-columns: 78px minmax(0, 1fr); gap: 15px; padding: 15px 0;
         border-top: 1px solid {HAIR}; align-items: start;">
      {photo(img, '1 / 1', badge=False)}
      <div style="display: flex; flex-direction: column; gap: 5px;">
        <span class="kick">{kick}</span>
        <h4 style="font-size: 16.5px; line-height: 1.32;">{title}</h4>
        <span class="date">{date}</span>
      </div>
    </a>""" for kick, img, title, date in BRIEFS)

    lead = f"""<div class="wrap" style="padding-top: 38px;">
      <div style="display: grid; grid-template-columns: minmax(0, 1.92fr) minmax(0, 1fr);
           gap: 44px;">
        <div style="display: flex; flex-direction: column; gap: 18px;">
          {photo('lead-agm.jpg', '16 / 9')}
          <div style="display: flex; flex-direction: column; gap: 12px;">
            <span class="kick">Notice</span>
            <h1 style="font-size: 40px; line-height: 1.16; max-width: 24ch;">Notice of the
              Annual General Meeting, 14 March 2027</h1>
            <p class="std" style="font-size: 17px; max-width: 56ch;">The agenda, the
              Treasurer's statement and the papers for the meeting are published for members.
              Nominations for the 2027 committee close on 28 February.</p>
            <div style="display: flex; align-items: center; gap: 18px; padding-top: 2px;">
              {more('Read the notice')}
              <span class="date">Published 12 February 2027 · The Secretary</span>
            </div>
          </div>
        </div>
        <div style="display: flex; flex-direction: column;">
          <div style="border-top: 3px solid {MAROON}; padding-top: 13px; padding-bottom: 4px;">
            <h2 style="font-size: 19px;">Also this month</h2>
          </div>
          {briefs}
          <div style="border-top: 1px solid {HAIR}; padding-top: 15px; margin-top: 4px;">
            {more('All announcements')}
          </div>
        </div>
      </div>
    </div>"""

    notice = f"""<div style="background: {BAND}; border-top: 1px solid {RULE};
         border-bottom: 1px solid {RULE}; margin-top: 44px;">
      <div class="wrap" style="padding: 18px 40px; display: flex; align-items: center;
           justify-content: space-between; gap: 28px;">
        <div style="display: flex; align-items: center; gap: 14px;">
          <span class="kick kick-g">Members</span>
          <span style="width: 1px; height: 16px; background: {RULE};"></span>
          <span style="font-size: 15px; color: {INK};">Renewal for 2027 is open until
            <strong style="font-weight: 600;">31 March</strong>. Dues are QAR 500 for the year
            and a receipt is issued on payment.</span>
        </div>
        {more('Renew your membership')}
      </div>
    </div>"""

    news = ''.join(f"""<a href="#" style="display: flex; flex-direction: column; gap: 13px;">
      {photo(img, '3 / 2')}
      <span class="kick">{kick}</span>
      <h3 style="font-size: 21px; line-height: 1.26;">{title}</h3>
      <p class="std" style="font-size: 14.5px;">{std}</p>
      <span class="date">{date}</span>
    </a>""" for kick, img, title, std, date in NEWS)

    news_sec = f"""<div class="wrap" style="padding-top: 62px;">
      <div class="sec"><h2>News</h2>{more('All news')}</div>
      <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr));
           gap: 34px;">{news}</div>
    </div>"""

    ev_rows = ''.join(f"""<div style="display: grid;
         grid-template-columns: 74px minmax(0, 1fr) 210px 104px; gap: 26px;
         align-items: center; padding: 19px 0; border-top: 1px solid {HAIR};">
      <div style="border-left: 3px solid {MAROON}; padding-left: 13px;">
        <div style="font-family: Newsreader, serif; font-size: 25px; font-weight: 500;
             color: {INK}; line-height: 1;">{day}</div>
        <div class="kick" style="font-size: 10.5px; padding-top: 3px;">{mon}</div>
      </div>
      <div style="display: flex; flex-direction: column; gap: 5px; min-width: 0;">
        <h3 style="font-size: 19px; line-height: 1.3;">{title}</h3>
        <span style="font-size: 13.5px; color: {MUTED};">{time} · {tbc('Venue')} · {cat}</span>
      </div>
      <span style="font-size: 13.5px; color: {MUTED};">{note}</span>
      <a href="#" class="btn btn-o" style="height: 38px; padding: 0 18px; font-size: 13.5px;">
        Book</a>
    </div>""" for mon, day, title, time, cat, note in EVENTS)

    events_sec = f"""<div class="wrap" style="padding-top: 62px;">
      <div class="sec"><h2>Events</h2>{more('All events and the calendar')}</div>
      <div style="border-bottom: 1px solid {HAIR};">{ev_rows}</div>
    </div>"""

    fee_rows = ''.join(f"""<div style="display: grid;
         grid-template-columns: 176px minmax(0, 1fr) 168px; gap: 22px; padding: 15px 0;
         border-top: 1px solid {RULE}; align-items: baseline;">
      <span style="font-size: 15px; font-weight: 600; color: {INK};">{cat}</span>
      <span style="font-size: 14.5px; color: {BODY}; line-height: 1.5;">{who}</span>
      {f'<span style="font-size: 15px; font-weight: 600; color: {INK};">{dues}</span>'
         if known else tbc(dues)}
    </div>""" for cat, who, dues, known in FEES)

    step_rows = ''.join(f"""<div style="display: grid;
         grid-template-columns: 26px minmax(0, 1fr); gap: 14px; padding: 12px 0;
         border-top: 1px solid {RULE}; align-items: start;">
      <span style="font-family: Newsreader, serif; font-size: 19px; color: {MAROON};
            line-height: 1.3;">{k + 1}</span>
      <span style="font-size: 14.5px; line-height: 1.55; color: {BODY};">{t}</span>
    </div>""" for k, t in enumerate(STEPS))

    membership = f"""<div style="background: {BAND}; border-top: 1px solid {RULE};
         margin-top: 62px;">
      <div class="wrap" style="padding-top: 54px; padding-bottom: 58px;">
        <div class="sec"><h2>Membership</h2>{more('Membership in full')}</div>
        <div style="display: grid; grid-template-columns: minmax(0, 1.62fr) minmax(0, 1fr);
             gap: 56px; align-items: start;">
          <div style="display: flex; flex-direction: column; gap: 18px;">
            <p class="std" style="font-size: 16px; max-width: 62ch;">EF admits qualified
              engineers of Kerala origin resident in Qatar. Admission is decided by the elected
              committee against published criteria, and every decision is recorded against the
              officer who made it.</p>
            <div>
              <div style="display: grid; grid-template-columns: 176px minmax(0, 1fr) 168px;
                   gap: 22px; padding-bottom: 9px;">
                <span class="kick">Category</span><span class="kick">Who it is for</span>
                <span class="kick">Dues</span>
              </div>
              <div style="border-bottom: 1px solid {RULE};">{fee_rows}</div>
            </div>
            <p style="font-size: 13.5px; color: {MUTED}; line-height: 1.55;">Dues are set
              annually by the committee and confirmed at the general meeting. The renewal
              window runs to 31 March.</p>
          </div>
          <div style="display: flex; flex-direction: column; gap: 16px;">
            <h3 style="font-size: 21px;">How to apply</h3>
            <div style="border-bottom: 1px solid {RULE};">{step_rows}</div>
            <div style="display: flex; align-items: center; gap: 14px; padding-top: 4px;">
              <a href="#" class="btn btn-m">Apply for membership</a>
              {more('Download the bylaws')}
            </div>
          </div>
        </div>
      </div>
    </div>"""

    register = f"""<div class="wrap" style="padding-top: 62px;">
      <div class="sec"><h2>The register of members</h2>{more('About the register')}</div>
      <div style="display: grid; grid-template-columns: minmax(0, 1.62fr) minmax(0, 1fr);
           gap: 56px; align-items: start;">
        <div style="display: flex; flex-direction: column; gap: 18px;">
          <p class="std" style="font-size: 16px; max-width: 62ch;">Eight hundred engineers,
            searchable by name, employer, discipline and membership category. Each member
            decides, section by section, what the register discloses — and that decision is
            enforced on every route, including the mobile application.</p>
          <div style="display: flex; align-items: center; gap: 12px;">
            <div class="field" style="width: 330px;">{search_ico()}
              <span>Name, employer or discipline</span></div>
            <a href="#" class="btn btn-o">Search the register</a>
          </div>
          <p style="font-size: 13.5px; color: {MUTED};">The register is open to members in good
            standing. Sign in to search it.</p>
        </div>
        <div style="border: 1px solid {RULE}; padding: 26px; display: flex;
             flex-direction: column; gap: 14px;">
          <span class="kick kick-g">For partners and employers</span>
          <h3 style="font-size: 20px; line-height: 1.28;">Verify a membership</h3>
          <p style="font-size: 14.5px; line-height: 1.6; color: {BODY};">Confirm a membership
            from the member's Digital ID. Only the fields EF has configured for your partner
            type are returned, and verification fails the day a membership lapses.</p>
          <div class="field" style="margin-top: 2px;"><span>Membership number</span></div>
          <a href="#" class="btn btn-o">Verify</a>
        </div>
      </div>
    </div>"""

    off_rows = ''.join(f"""<div style="display: grid;
         grid-template-columns: minmax(0, 1fr) 190px 74px; gap: 20px; padding: 13px 0;
         border-top: 1px solid {RULE}; align-items: baseline;">
      <span style="font-size: 14.5px; font-weight: 600; color: {INK};">{o}</span>
      {tbc('Name — EF to supply')}
      <span style="font-size: 13.5px; color: {MUTED};">2027</span>
    </div>""" for o in OFFICERS)

    doc_rows = ''.join(f"""<div style="display: grid;
         grid-template-columns: minmax(0, 1fr) 62px; gap: 18px; padding: 13px 0;
         border-top: 1px solid {RULE}; align-items: baseline;">
      <div style="display: flex; flex-direction: column; gap: 4px;">
        <a href="#" style="font-size: 14.5px; font-weight: 600;">{t}</a>
        <span style="font-size: 13px; color: {MUTED};">{note}</span>
      </div>
      <span style="font-size: 13px; color: {MUTED};
            font-variant-numeric: tabular-nums;">{v}</span>
    </div>""" for t, v, note in DOCS)

    governance = f"""<div class="wrap" style="padding-top: 62px; padding-bottom: 68px;">
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 56px;
           align-items: start;">
        <div>
          <div class="sec"><h2>The committee</h2>{more('Past officers')}</div>
          <p class="std" style="font-size: 15px; margin-bottom: 14px;">Officers are elected for
            a single term and carry out EF's administration alongside full-time employment.</p>
          <div style="border-bottom: 1px solid {RULE};">{off_rows}</div>
        </div>
        <div>
          <div class="sec"><h2>Published documents</h2>{more('All publications')}</div>
          <p class="std" style="font-size: 15px; margin-bottom: 14px;">The rules EF works to,
            published with their version and the date they were adopted.</p>
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

    footer = f"""<div style="background: {MAROON};">
      <div class="wrap" style="padding-top: 52px; padding-bottom: 30px;">
        <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr));
             gap: 34px;">{fcols}</div>
        <div style="border-top: 1px solid #6B3040; margin-top: 44px; padding-top: 26px;
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
        <div style="border-top: 1px solid #6B3040; margin-top: 26px; padding-top: 20px;
             display: flex; align-items: center; justify-content: space-between; gap: 24px;">
          <span style="font-size: 12.5px; color: #A98D97;">© 2027 Engineers Forum Qatar.</span>
          <span style="font-size: 12.5px; color: #A98D97;">Personal data held in the State of
            Qatar.</span>
        </div>
      </div>
    </div>"""

    body = (utility + masthead + lead + notice + news_sec + events_sec
            + membership + register + governance + footer)
    return wrap_dc(body, 1440, 4420)


# ======================================================================== mobile
def home_mobile():
    burger = ('<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#191013" '
              'stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>')

    briefs = ''.join(f"""<a href="#" style="display: grid;
         grid-template-columns: 68px minmax(0, 1fr); gap: 13px; padding: 14px 0;
         border-top: 1px solid {HAIR}; align-items: start;">
      {photo(img, '1 / 1', badge=False)}
      <div style="display: flex; flex-direction: column; gap: 4px;">
        <span class="kick" style="font-size: 10px;">{kick}</span>
        <h4 style="font-size: 15.5px; line-height: 1.32;">{title}</h4>
        <span class="date" style="font-size: 12px;">{date}</span>
      </div>
    </a>""" for kick, img, title, date in BRIEFS)

    news = ''.join(f"""<a href="#" style="display: flex; flex-direction: column; gap: 11px;
         padding-top: 18px; border-top: 1px solid {HAIR};">
      {photo(img, '3 / 2')}
      <span class="kick" style="font-size: 10px;">{kick}</span>
      <h3 style="font-size: 19px; line-height: 1.28;">{title}</h3>
      <p class="std" style="font-size: 14px;">{std}</p>
      <span class="date" style="font-size: 12px;">{date}</span>
    </a>""" for kick, img, title, std, date in NEWS)

    ev_rows = ''.join(f"""<div style="display: grid; grid-template-columns: 60px minmax(0, 1fr);
         gap: 15px; padding: 16px 0; border-top: 1px solid {HAIR}; align-items: start;">
      <div style="border-left: 3px solid {MAROON}; padding-left: 11px;">
        <div style="font-family: Newsreader, serif; font-size: 22px; font-weight: 500;
             color: {INK}; line-height: 1;">{day}</div>
        <div class="kick" style="font-size: 10px; padding-top: 3px;">{mon}</div>
      </div>
      <div style="display: flex; flex-direction: column; gap: 7px; min-width: 0;">
        <h3 style="font-size: 17px; line-height: 1.3;">{title}</h3>
        <span style="font-size: 13px; color: {MUTED};">{time} · {tbc('Venue')} · {cat}</span>
        <span style="font-size: 13px; color: {MUTED};">{note}</span>
        <a href="#" class="btn btn-o" style="margin-top: 3px;">Book</a>
      </div>
    </div>""" for mon, day, title, time, cat, note in EVENTS)

    fee_rows = ''.join(f"""<div style="padding: 14px 0; border-top: 1px solid {RULE};
         display: flex; flex-direction: column; gap: 6px;">
      <div style="display: flex; align-items: baseline; justify-content: space-between;
           gap: 14px;">
        <span style="font-size: 15px; font-weight: 600; color: {INK};">{cat}</span>
        {f'<span style="font-size: 14.5px; font-weight: 600; color: {INK}; white-space: nowrap;">{dues}</span>'
           if known else tbc(dues)}
      </div>
      <span style="font-size: 13.5px; color: {BODY}; line-height: 1.5;">{who}</span>
    </div>""" for cat, who, dues, known in FEES)

    step_rows = ''.join(f"""<div style="display: grid;
         grid-template-columns: 24px minmax(0, 1fr); gap: 13px; padding: 12px 0;
         border-top: 1px solid {RULE}; align-items: start;">
      <span style="font-family: Newsreader, serif; font-size: 18px; color: {MAROON};
            line-height: 1.3;">{k + 1}</span>
      <span style="font-size: 14px; line-height: 1.55; color: {BODY};">{t}</span>
    </div>""" for k, t in enumerate(STEPS))

    off_rows = ''.join(f"""<div style="display: flex; align-items: baseline;
         justify-content: space-between; gap: 14px; padding: 12px 0;
         border-top: 1px solid {RULE};">
      <span style="font-size: 14px; font-weight: 600; color: {INK};">{o}</span>
      {tbc('EF to supply')}
    </div>""" for o in OFFICERS)

    doc_rows = ''.join(f"""<div style="display: flex; flex-direction: column; gap: 4px;
         padding: 12px 0; border-top: 1px solid {RULE};">
      <a href="#" style="font-size: 14px; font-weight: 600;">{t}
        <span style="color: {MUTED}; font-weight: 400;">{v}</span></a>
      <span style="font-size: 12.5px; color: {MUTED};">{note}</span>
    </div>""" for t, v, note in DOCS)

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
  <div style="background: {MAROON}; padding: 9px 20px; display: flex; justify-content: center;">
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
  <div style="border-bottom: 1px solid {RULE}; padding: 12px 20px; display: flex;
       align-items: center; gap: 10px;">
    <a href="#" class="btn btn-m" style="flex-grow: 1;">Apply for membership</a>
    <a href="#" class="btn btn-o" style="flex-grow: 1;">Member sign in</a>
  </div>

  <div style="padding: 24px 20px 0; display: flex; flex-direction: column; gap: 14px;">
    {photo('lead-agm.jpg', '16 / 9')}
    <span class="kick">Notice</span>
    <h1 style="font-size: 29px; line-height: 1.18;">Notice of the Annual General Meeting,
      14 March 2027</h1>
    <p class="std" style="font-size: 15.5px;">The agenda, the Treasurer's statement and the
      papers for the meeting are published for members. Nominations for the 2027 committee
      close on 28 February.</p>
    <span class="date">Published 12 February 2027 · The Secretary</span>
    {more('Read the notice')}
  </div>

  <div style="padding: 30px 20px 0;">
    <div style="border-top: 3px solid {MAROON}; padding-top: 12px;">
      <h2 style="font-size: 19px;">Also this month</h2>
    </div>
    {briefs}
  </div>

  <div style="background: {BAND}; border-top: 1px solid {RULE}; border-bottom: 1px solid {RULE};
       margin-top: 30px; padding: 18px 20px; display: flex; flex-direction: column; gap: 10px;">
    <span class="kick kick-g">Members</span>
    <span style="font-size: 14.5px; line-height: 1.55; color: {INK};">Renewal for 2027 is open
      until <strong style="font-weight: 600;">31 March</strong>. Dues are QAR 500 for the
      year.</span>
    {more('Renew your membership')}
  </div>

  {sec('News', 'All news',
       '<div style="display: flex; flex-direction: column; gap: 22px;">' + news + '</div>')}
  {sec('Events', 'All events',
       f'<div style="border-bottom: 1px solid {HAIR};">' + ev_rows + '</div>')}

  {sec('Membership', None,
       '<p class="std" style="font-size: 15px; margin-bottom: 16px;">EF admits qualified '
       'engineers of Kerala origin resident in Qatar. Admission is decided by the elected '
       'committee against published criteria.</p>'
       f'<div style="border-bottom: 1px solid {RULE}; margin-bottom: 24px;">' + fee_rows
       + '</div><h3 style="font-size: 19px; margin-bottom: 10px;">How to apply</h3>'
       f'<div style="border-bottom: 1px solid {RULE}; margin-bottom: 18px;">' + step_rows
       + '</div><a href="#" class="btn btn-m" style="width: 100%;">Apply for membership</a>',
       band=True)}

  {sec('The register of members', 'About the register',
       '<p class="std" style="font-size: 15px; margin-bottom: 14px;">Eight hundred engineers, '
       'searchable by name, employer, discipline and category. Each member decides, section by '
       'section, what the register discloses.</p>'
       '<div class="field" style="margin-bottom: 12px;">' + search_ico()
       + '<span>Name, employer or discipline</span></div>'
       '<a href="#" class="btn btn-o" style="width: 100%;">Search the register</a>'
       f'<p style="font-size: 13px; color: {MUTED}; padding-top: 12px;">Open to members in good '
       'standing. Sign in to search it.</p>'
       f'<div style="border: 1px solid {RULE}; padding: 20px; margin-top: 22px; display: flex; '
       'flex-direction: column; gap: 12px;">'
       '<span class="kick kick-g">For partners and employers</span>'
       '<h3 style="font-size: 18px; line-height: 1.28;">Verify a membership</h3>'
       f'<p style="font-size: 14px; line-height: 1.6; color: {BODY};">Confirm a membership from '
       "the member's Digital ID. Only the fields EF has configured for your partner type are "
       'returned.</p><div class="field"><span>Membership number</span></div>'
       '<a href="#" class="btn btn-o">Verify</a></div>')}

  {sec('The committee', 'Past officers',
       f'<div style="border-bottom: 1px solid {RULE};">' + off_rows + '</div>')}
  {sec('Published documents', 'All publications',
       f'<div style="border-bottom: 1px solid {RULE};">' + doc_rows + '</div>')}

  <div style="background: {MAROON}; margin-top: 40px; padding: 32px 20px 24px; display: flex;
       flex-direction: column; gap: 22px;">
    {lockup(reversed_=True)}
    <p style="font-size: 13.5px; line-height: 1.7; color: #A98D97;">The apex body of engineers
      of Kerala origin working in the State of Qatar.</p>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));
         gap: 22px;">{ftop}</div>
    <span style="font-size: 12px; color: #A98D97; border-top: 1px solid #6B3040;
          padding-top: 18px; line-height: 1.6;">© 2027 Engineers Forum Qatar. Personal data
      held in the State of Qatar.</span>
  </div>
"""
    return wrap_dc(body, 390, 6560)


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
