#!/usr/bin/env python3
"""The four EF Qatar Console artboards. Run this to (re)write the .dc.html files."""
from build import (page, ic, chip, avatar, mark, lockup, OUT)

H = 1120  # app frames are 1440x1120; the member record is taller (it scrolls)


# ------------------------------------------------------------------ helpers
def card(title, body, right='', pad='0', style=''):
    head = f'<div class="card-h"><span class="card-t">{title}</span>{right}</div>' if title else ''
    return (f'<div class="card" style="display: flex; flex-direction: column; '
            f'overflow: hidden; {style}">{head}'
            f'<div style="padding: {pad}; flex-grow: 1; min-height: 0; overflow: hidden;">'
            f'{body}</div></div>')


def bar(pct, color='#4BB148', track='#EDF2F7', h=7, target=None):
    mark_ = (f'<div style="position: absolute; left: {target}%; top: -3px; bottom: -3px; '
             f'width: 2px; background: #4B1728;"></div>') if target else ''
    return (f'<div style="position: relative; height: {h}px; border-radius: 100px; '
            f'background: {track};">'
            f'<div style="width: {pct}%; height: {h}px; border-radius: 100px; '
            f'background: {color};"></div>{mark_}</div>')


def row(cols, tmpl, pad='13px 20px', border=True, bg='#FFFFFF', gap=14, align='center'):
    cells = ''.join(f'<div style="min-width: 0;">{c}</div>' for c in cols)
    bd = 'border-bottom: 1px solid #EEF3F8;' if border else ''
    return (f'<div style="display: grid; grid-template-columns: {tmpl}; gap: {gap}px; '
            f'align-items: {align}; padding: {pad}; {bd} background: {bg};">{cells}</div>')


def hrow(labels, tmpl, gap=14):
    return row([f'<span class="th">{l}</span>' for l in labels], tmpl,
               pad='11px 20px', bg='#FAFCFE', gap=gap)


def person(initials, name, sub, size=34):
    return (f'<div style="display: flex; align-items: center; gap: 11px; min-width: 0;">'
            f'{avatar(initials, size)}'
            f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0;">'
            f'<span style="font-size: 14px; font-weight: 700; color: #241017; overflow: hidden; '
            f'text-overflow: ellipsis; white-space: nowrap;">{name}</span>'
            f'<span style="font-size: 12.5px; color: #7D7278; overflow: hidden; '
            f'text-overflow: ellipsis; white-space: nowrap;">{sub}</span></div></div>')


def sel(label):
    return (f'<div class="field" style="justify-content: space-between; gap: 8px;">'
            f'<span>{label}</span>{ic("down", 15, "#9A9096")}</div>')


def box(checked=False):
    if checked:
        return ('<div style="width: 18px; height: 18px; border-radius: 4px; background: #4B1728; '
                'display: flex; align-items: center; justify-content: center;">'
                '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" '
                'stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">'
                '<path d="m5 12.5 4.5 4.5L19 7.5"/></svg></div>')
    return ('<div style="width: 18px; height: 18px; border-radius: 4px; background: #FFFFFF; '
            'border: 1.5px solid #C6D0DC;"></div>')


# =========================================================== 1 — Dashboard
def stat(label, value, sub, icon, tone='#2A6B27', tone_bg='#F1FAF0', progress=None, sub_c='#7D7278'):
    p = f'<div style="padding-top: 12px;">{bar(progress)}</div>' if progress else ''
    return f"""<div class="card" style="padding: 18px 20px; display: flex; flex-direction: column; gap: 9px;">
      <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px;">
        <span style="font-size: 12.5px; color: #7D7278; font-weight: 700;">{label}</span>
        <div style="width: 30px; height: 30px; border-radius: 7px; background: {tone_bg};
             display: flex; align-items: center; justify-content: center;">{ic(icon, 16, tone)}</div>
      </div>
      <div style="font-family: Quicksand, sans-serif; font-size: 30px; font-weight: 700;
           color: #241017; line-height: 1;">{value}</div>
      <span style="font-size: 12.5px; color: {sub_c};">{sub}</span>{p}
    </div>"""


APPROVALS_TMPL = 'minmax(0, 1fr) 150px 130px 108px'
AUDIT_TMPL = 'minmax(0, 1fr) 190px 128px'

_appr = [
    ('SN', 'Sreenath Nair', 'Mechanical · Aamal Industrial', 'Ordinary Member', '6 days', True),
    ('DP', 'Divya Pillai', 'Civil · Qatar Design Consortium', 'Ordinary Member', '5 days', True),
    ('AT', 'Ashok Thomas', 'Electrical · Kahramaa', 'Associate Member', '3 days', False),
    ('MK', 'Meera Krishnan', 'Chemical · QAFCO', 'Ordinary Member', '2 days', False),
    ('VS', 'Vinod Sasidharan', 'Mechanical · Milaha', 'Student Member', '1 day', False),
]

_audit = [
    ('RM', 'Rajesh Menon', 'approved a membership application', 'EF/2027/0061', '11:42'),
    ('PT', 'Priya Thomas', 'issued a credit note', 'CRN-2027-00014', '10:08'),
    ('RM', 'Rajesh Menon', 'changed a role assignment', 'Sports Secretary', 'Yesterday'),
    ('SK', 'Suresh Kumar', 'refunded an event fee', 'RFD-2027-00007', 'Yesterday'),
    ('PT', 'Priya Thomas', 'withdrew a marketplace listing', 'MKT-2027-00092', '2 days ago'),
]


def dashboard():
    tiles = ''.join([
        stat('In good standing', '612', 'of 800 on the register', 'people', progress=76),
        stat('Renewals outstanding', '188', 'Window closes 31 March 2027', 'clock',
             '#7A4E12', '#FBF2E2'),
        stat('Approvals waiting', '7', '2 are past their time limit', 'alert',
             '#4B1728', '#F3E3E8', sub_c='#7A4E12'),
        stat('Dues collected online', '78%', 'Target is 80% by month six', 'money',
             progress=78),
    ])

    appr_rows = ''.join(
        row([person(i, n, s),
             f'<span style="font-size: 13.5px; color: #4A4045;">{cat}</span>',
             (f'<span class="chip" style="background: #FBF2E2; color: #7A4E12; '
              f'border: 1px solid #EEDCBC;">{w} · overdue</span>' if od else
              f'<span style="font-size: 13.5px; color: #7D7278;">{w}</span>'),
             '<a href="#" class="btn btn-s" style="height: 32px; padding: 0 14px; '
             'font-size: 13px;">Review</a>'],
            APPROVALS_TMPL, pad='11px 20px', border=(i != 'VS'))
        for i, n, s, cat, w, od in _appr)

    audit_rows = ''.join(
        row([f'<div style="display: flex; align-items: center; gap: 10px;">{avatar(i, 28)}'
             f'<span style="font-size: 13.5px; color: #241017;">'
             f'<strong style="font-weight: 700;">{n}</strong> {act}</span></div>',
             f'<span class="mono" style="font-size: 12.5px; color: #4A4045;">{ref}</span>',
             f'<span style="font-size: 12.5px; color: #7D7278;">{when}</span>'],
            AUDIT_TMPL, pad='11px 20px', border=(k < len(_audit) - 1))
        for k, (i, n, act, ref, when) in enumerate(_audit))

    renewal = f"""<div style="padding: 20px; display: flex; flex-direction: column; gap: 18px;">
      <div style="display: flex; flex-direction: column; gap: 10px;">
        <div style="display: flex; align-items: baseline; justify-content: space-between;">
          <span style="font-family: Quicksand, sans-serif; font-size: 34px; font-weight: 700;
                color: #241017; line-height: 1;">76%</span>
          <span style="font-size: 12.5px; color: #7D7278;">target 70%</span>
        </div>
        {bar(76, target=70, h=9)}
        <span style="font-size: 12.5px; color: #2A6B27; font-weight: 700;">Ahead of the
          self-service target</span>
      </div>
      <div style="display: flex; flex-direction: column; gap: 11px; border-top: 1px solid #EEF3F8;
           padding-top: 15px;">
        <div style="display: flex; align-items: center; justify-content: space-between;">
          <span style="font-size: 13.5px; color: #4A4045;">Renewed without help</span>
          <span class="mono" style="font-size: 13.5px; font-weight: 700; color: #241017;">612</span>
        </div>
        <div style="display: flex; align-items: center; justify-content: space-between;">
          <span style="font-size: 13.5px; color: #4A4045;">Chased by an officer</span>
          <span class="mono" style="font-size: 13.5px; font-weight: 700; color: #241017;">41</span>
        </div>
        <div style="display: flex; align-items: center; justify-content: space-between;">
          <span style="font-size: 13.5px; color: #4A4045;">Not yet renewed</span>
          <span class="mono" style="font-size: 13.5px; font-weight: 700; color: #7A4E12;">147</span>
        </div>
      </div>
    </div>"""

    events = '<div style="display: flex; flex-direction: column; height: 100%;">' + ''.join(f"""<div style="display: flex; gap: 14px; padding: 14px 20px;
         {'border-bottom: 1px solid #EEF3F8;' if last else ''}">
      <div style="width: 46px; border: 1px solid #DCE3EC; border-radius: 7px; overflow: hidden;
           text-align: center; flex-shrink: 0;">
        <div style="background: #4B1728; color: #FFFFFF; font-size: 9.5px; font-weight: 800;
             letter-spacing: 0.1em; padding: 3px 0;">{mon}</div>
        <div style="font-family: Quicksand, sans-serif; font-size: 19px; font-weight: 700;
             color: #241017; padding: 4px 0 6px;">{day}</div>
      </div>
      <div style="display: flex; flex-direction: column; gap: 4px; min-width: 0;">
        <span style="font-size: 14px; font-weight: 700; color: #241017;">{name}</span>
        <span style="font-size: 12.5px; color: #7D7278;">{meta}</span>
      </div></div>""" for mon, day, name, meta, last in [
        ('MAR', '14', 'Structural engineering seminar', '182 registered · 18 on the waiting list', True),
        ('MAR', '27', 'EF cricket tournament 2027', '96 registered · 12 teams', True),
        ('APR', '10', 'Arts evening', '54 registered · 3 performances', True),
    ]) + ('<div style="flex-grow: 1;"></div>'
          '<div style="display: flex; align-items: center; justify-content: space-between;'
          ' gap: 12px; padding: 14px 20px; border-top: 1px solid #EEF3F8;">'
          '<span style="font-size: 12.5px; color: #7D7278;">9 more events scheduled this year</span>'
          '<span style="font-size: 12.5px; color: #7D7278;">Capacity 84% taken</span></div></div>')

    body = f"""      <div style="display: flex; flex-direction: column; gap: 20px; height: 100%;">
        <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px;">
          {tiles}
        </div>
        <div style="display: grid; grid-template-columns: minmax(0, 1.62fr) minmax(0, 1fr);
             gap: 20px; flex-grow: 1; min-height: 0;">
          <div style="display: flex; flex-direction: column; gap: 20px; min-height: 0;">
            {card('Approvals waiting',
                  hrow(['Applicant', 'Applied for', 'Waiting', ''], APPROVALS_TMPL) + appr_rows,
                  '<a href="#" style="font-size: 13px; font-weight: 700;">Open the queue</a>')}
            {card('Recent privileged actions',
                  hrow(['Action', 'Reference', 'When'], AUDIT_TMPL) + audit_rows,
                  '<a href="#" style="font-size: 13px; font-weight: 700;">Audit log</a>',
                  style='flex-grow: 1;')}
          </div>
          <div style="display: flex; flex-direction: column; gap: 20px; min-height: 0;">
            {card('Renewal window', renewal)}
            {card('Next events', events,
                  '<a href="#" style="font-size: 13px; font-weight: 700;">All events</a>',
                  style='flex-grow: 1;')}
          </div>
        </div>
      </div>"""

    return page(body, 'Dashboard', 'Dashboard', h=H, actions=(
        '<a href="#" class="btn btn-p">' + ic('plus', 16, '#FFFFFF') + 'New announcement</a>'))


# ============================================================= 2 — Members
M_TMPL = '32px minmax(0, 1fr) 132px 142px 152px 112px 98px 36px'

_members = [
    ('AK', 'Anand Krishnan',   'Senior Structural Engineer · Aamal',      'EF/2019/0412', 'Ordinary Member',  'expiring',  '31 Mar 2027', 'Due',      True),
    ('LM', 'Lakshmi Menon',    'Project Manager · Qatar Design Consortium', 'EF/2016/0188', 'Life Member',      'active',    '—',           'Paid',     True),
    ('SN', 'Sreenath Nair',    'Mechanical Engineer · Aamal Industrial',  'EF/2027/0061', 'Ordinary Member',  'pending',   '—',           '—',        False),
    ('JV', 'Joseph Varghese',  'Electrical Engineer · Kahramaa',          'EF/2014/0093', 'Ordinary Member',  'lapsed',    '31 Mar 2026', 'Overdue',  False),
    ('RB', 'Reshma Balan',     'Civil Engineer · Ashghal',                'EF/2021/0577', 'Ordinary Member',  'active',    '31 Mar 2028', 'Paid',     False),
    ('TG', 'Thomas George',    'QA/QC Engineer · Milaha',                 'EF/2020/0501', 'Associate Member', 'active',    '31 Mar 2028', 'Paid',     False),
    ('NS', 'Nisha Suresh',     'Chemical Engineer · QAFCO',               'EF/2018/0342', 'Ordinary Member',  'expiring',  '31 Mar 2027', 'Due',      False),
    ('PK', 'Pradeep Kumar',    'Site Engineer · UrbaCon',                 'EF/2022/0630', 'Ordinary Member',  'suspended', '31 Mar 2028', 'Paid',     False),
    ('AR', 'Arun Radhakrishnan', 'Piping Engineer · Dolphin Energy',      'EF/2017/0264', 'Ordinary Member',  'active',    '31 Mar 2028', 'Paid',     False),
    ('SJ', 'Sandhya Jayan',    'Instrumentation Engineer · QChem',         'EF/2019/0455', 'Ordinary Member',  'active',    '31 Mar 2028', 'Paid',     False),
    ('BM', 'Biju Mathew',      'HVAC Engineer · Al Jaber',                'EF/2015/0121', 'Life Member',      'active',    '—',           'Paid',     False),
    ('RK', 'Rekha Krishnadas', 'Environmental Engineer · Ashghal',         'EF/2023/0702', 'Associate Member', 'active',    '31 Mar 2028', 'Paid',     False),
]

DUES = {'Paid': ('#2A6B27', 700), 'Due': ('#7A4E12', 700), 'Overdue': ('#4B1728', 800),
        '—': ('#9A9096', 400)}


def members():
    rows = ''.join(
        row([box(chk),
             person(i, n, s),
             f'<span class="mono" style="font-size: 12.5px; color: #4A4045;">{num}</span>',
             f'<span style="font-size: 13.5px; color: #4A4045;">{cat}</span>',
             chip(st),
             f'<span style="font-size: 13px; color: #4A4045;">{exp}</span>',
             f'<span style="font-size: 13px; color: {DUES[d][0]}; '
             f'font-weight: {DUES[d][1]};">{d}</span>',
             f'<a href="#" style="display: flex;">{ic("dots", 17, "#9A9096")}</a>'],
            M_TMPL, pad='12px 20px', border=(n != 'Rekha Krishnadas'),
            bg='#FBF7F8' if chk else '#FFFFFF')
        for i, n, s, num, cat, st, exp, d, chk in _members)

    bulk = f"""<div style="display: flex; align-items: center; gap: 16px; padding: 12px 20px;
         background: #F3E3E8; border-bottom: 1px solid #E3CBD3;">
      <span style="font-size: 13.5px; font-weight: 700; color: #4B1728;">2 members selected</span>
      <div style="width: 1px; height: 20px; background: #DCB9C5;"></div>
      <a href="#" style="font-size: 13.5px; font-weight: 700;">Send a renewal notice</a>
      <a href="#" style="font-size: 13.5px; font-weight: 700;">Change category</a>
      <a href="#" style="font-size: 13.5px; font-weight: 700;">Export selection</a>
      <div style="flex-grow: 1;"></div>
      <a href="#" style="display: flex;">{ic('x', 16, '#4B1728')}</a>
    </div>"""

    footer = f"""<div style="display: flex; align-items: center; justify-content: space-between;
         gap: 16px; padding: 14px 20px; border-top: 1px solid #EEF3F8;">
      <span style="font-size: 13px; color: #7D7278;">Showing 1&ndash;12 of 800 members</span>
      <div style="display: flex; align-items: center; gap: 6px;">
        <a href="#" class="btn btn-s" style="height: 32px; padding: 0 12px; font-size: 13px;">Previous</a>
        <a href="#" class="btn btn-p" style="height: 32px; width: 32px; padding: 0; font-size: 13px;">1</a>
        <a href="#" class="btn btn-s" style="height: 32px; width: 32px; padding: 0; font-size: 13px;">2</a>
        <a href="#" class="btn btn-s" style="height: 32px; width: 32px; padding: 0; font-size: 13px;">3</a>
        <span style="font-size: 13px; color: #9A9096; padding: 0 4px;">&hellip;</span>
        <a href="#" class="btn btn-s" style="height: 32px; width: 32px; padding: 0; font-size: 13px;">89</a>
        <a href="#" class="btn btn-s" style="height: 32px; padding: 0 12px; font-size: 13px;">Next</a>
      </div>
    </div>"""

    body = f"""      <div style="display: flex; flex-direction: column; gap: 18px; height: 100%;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <div class="field" style="width: 250px; color: #7D7278;">{ic('search', 16, '#9A9096')}
            <span>Name, number or employer</span></div>
          <div style="width: 156px;">{sel('All categories')}</div>
          <div style="width: 150px;">{sel('All statuses')}</div>
          <div style="width: 148px;">{sel('Any expiry')}</div>
          <a href="#" class="btn btn-s">{ic('filter', 15, '#4B1728')}More filters</a>
          <div style="flex-grow: 1;"></div>
          <a href="#" class="btn btn-s">{ic('export', 15, '#4B1728')}Export</a>
          <a href="#" class="btn btn-p">{ic('plus', 15, '#FFFFFF')}Add a member</a>
        </div>
        <div class="card" style="display: flex; flex-direction: column; overflow: hidden;
             flex-grow: 1; min-height: 0;">
          {bulk}
          {hrow(['', 'Member', 'Number', 'Category', 'Status', 'Expires', 'Dues', ''], M_TMPL)}
          <div style="flex-grow: 1; min-height: 0; overflow: hidden;">{rows}</div>
          {footer}
        </div>
      </div>"""

    return page(body, 'Members', 'Members', h=H)


# ======================================================== 3 — Member record
def member_detail():
    tabs = ['Overview', 'Documents', 'Payments', 'Events', 'Audit']
    tabbar = ''.join(
        f'<a href="#" style="padding: 0 2px 12px; font-size: 14px; font-family: Quicksand, '
        f'sans-serif; font-weight: 700; color: {"#4B1728" if t == "Overview" else "#7D7278"}; '
        f'border-bottom: 2.5px solid {"#4B1728" if t == "Overview" else "transparent"};">{t}</a>'
        for t in tabs)

    header = f"""<div class="card" style="padding: 20px 22px; display: flex; align-items: center;
         gap: 18px;">
      {avatar('AK', 58, '#F3E3E8', '#4B1728', 21)}
      <div style="display: flex; flex-direction: column; gap: 6px; min-width: 0;">
        <div style="display: flex; align-items: center; gap: 11px;">
          <h2 style="font-size: 21px;">Anand Krishnan</h2>{chip('expiring')}
        </div>
        <span style="font-size: 13.5px; color: #7D7278;">
          <span class="mono">EF/2019/0412</span> &nbsp;·&nbsp; Ordinary Member
          &nbsp;·&nbsp; Member since 14 August 2019</span>
      </div>
      <div style="flex-grow: 1;"></div>
      <a href="#" class="btn btn-s">Message</a>
      <a href="#" class="btn btn-s">Suspend</a>
      <a href="#" class="btn btn-p">{ic('money', 15, '#FFFFFF')}Record a renewal</a>
      <a href="#" style="display: flex;">{ic('dots', 18, '#7D7278')}</a>
    </div>"""

    def kv(k, v, mono=False):
        return (f'<div style="display: flex; flex-direction: column; gap: 4px;">'
                f'<span style="font-size: 11.5px; color: #7D7278; font-weight: 700;">{k}</span>'
                f'<span class="{"mono" if mono else ""}" style="font-size: 14px; '
                f'color: #241017; font-weight: {"500" if mono else "600"};">{v}</span></div>')

    membership = f"""<div style="padding: 20px; display: grid;
         grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px 16px;">
      {kv('Category', 'Ordinary Member')}
      {kv('Member number', 'EF/2019/0412', True)}
      {kv('Status', 'Expiring soon')}
      {kv('Expires', '31 March 2027')}
      {kv('Renewal opened', '1 March 2027')}
      {kv('Dues', 'QAR 500 outstanding')}
      {kv('College', 'Mechanical')}
      {kv('Verified by', 'Rajesh Menon')}
      {kv('Digital ID', 'Active, offline copy 8 min old')}
    </div>"""

    VIS = [('Employment', 'All members', 'eye'), ('Education', 'All members', 'eye'),
           ('Skills', 'All members', 'eye'), ('Contact details', 'Administrators only', 'lock'),
           ('Professional summary', 'Hidden', 'off')]
    vis_icon = {
        'eye': '<path d="M2 12s3.6-6.5 10-6.5S22 12 22 12s-3.6 6.5-10 6.5S2 12 2 12Z"/><circle cx="12" cy="12" r="2.6"/>',
        'lock': '<rect x="4" y="10.5" width="16" height="10.5" rx="2"/><path d="M8 10.5V7a4 4 0 0 1 8 0v3.5"/>',
        'off': '<path d="M3 3l18 18M10.6 10.7a2.6 2.6 0 0 0 3.6 3.6"/><path d="M6.6 6.8C4 8.4 2 12 2 12s3.6 6.5 10 6.5c1.9 0 3.5-.6 4.8-1.4M9.5 5.8A9.9 9.9 0 0 1 12 5.5c6.4 0 10 6.5 10 6.5a19 19 0 0 1-2.7 3.5"/>',
    }
    profile = ''.join(f"""<div style="display: flex; align-items: center;
         justify-content: space-between; gap: 16px; padding: 13px 20px;
         {'border-bottom: 1px solid #EEF3F8;' if n != 'Professional summary' else ''}">
      <span style="font-size: 14px; font-weight: 600; color: #241017;">{n}</span>
      <span class="chip" style="background: #F4F7FA; color: #4A4045; border: 1px solid #DCE3EC;">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#7D7278"
             stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{vis_icon[k]}</svg>
        {v}</span></div>""" for n, v, k in VIS)

    docs = ''.join(f"""<div style="display: flex; align-items: center; gap: 12px; padding: 13px 20px;
         {'border-bottom: 1px solid #EEF3F8;' if last else ''}">
      {ic('doc', 18, '#7D7278')}
      <div style="display: flex; flex-direction: column; gap: 2px; flex-grow: 1; min-width: 0;">
        <span style="font-size: 13.5px; font-weight: 600; color: #241017;">{n}</span>
        <span style="font-size: 12px; color: {c};">{m}</span>
      </div>
      <a href="#" style="font-size: 13px; font-weight: 700;">View</a></div>""" for n, m, c, last in [
        ('Degree certificate', 'Verified 16 August 2019', '#7D7278', True),
        ('Qatar ID', 'Verified 2 March 2026', '#7D7278', True),
        ('Engineering qualification', 'Expires 30 June 2027', '#7A4E12', False),
    ])

    audit = ''.join(f"""<div style="display: flex; gap: 12px; padding: 12px 20px;
         {'border-bottom: 1px solid #EEF3F8;' if last else ''}">
      <div style="width: 7px; height: 7px; border-radius: 50%; background: {dot};
           margin-top: 6px; flex-shrink: 0;"></div>
      <div style="display: flex; flex-direction: column; gap: 3px; min-width: 0;">
        <span style="font-size: 13px; color: #241017; line-height: 1.45;">{t}</span>
        <span style="font-size: 11.5px; color: #7D7278;">{w}</span>
      </div></div>""" for t, w, dot, last in [
        ('Invoice <span class="mono">INV-2027-00214</span> issued', 'Rajesh Menon · 1 Mar 2027', '#4BB148', True),
        ('Profile visibility changed on Contact details', 'The member · 12 Feb 2027', '#B79AA4', True),
        ('Receipt <span class="mono">RCT-2026-00873</span> issued', 'Priya Thomas · 9 Mar 2026', '#4BB148', True),
        ('Qatar ID re-verified', 'Rajesh Menon · 2 Mar 2026', '#B79AA4', True),
        ('Registered for the structural engineering seminar', 'The member · 2 Feb 2027', '#B79AA4', True),
        ('Digital ID reissued after a device change', 'The member · 18 Jan 2027', '#B79AA4', True),
        ('Employment updated to Aamal Industrial', 'The member · 4 Nov 2026', '#B79AA4', False),
    ])

    PAY_TMPL = '150px minmax(0, 1fr) 104px 92px'
    pay = hrow(['Document', 'What it is for', 'Amount', 'Date'], PAY_TMPL) + ''.join(
        row([f'<div style="display: flex; flex-direction: column; gap: 2px;">'
             f'<span style="font-size: 13.5px; font-weight: 700; color: #241017;">{d}</span>'
             f'<span class="mono" style="font-size: 11.5px; color: #9A9096;">{ref}</span></div>',
             f'<span style="font-size: 13.5px; color: #4A4045;">{what}</span>',
             f'<span class="mono" style="font-size: 13px; color: #241017;">{amt}</span>',
             f'<span style="font-size: 12.5px; color: #7D7278;">{when}</span>'],
            PAY_TMPL, pad='11px 20px', border=(k < 2))
        for k, (d, what, ref, amt, when) in enumerate([
            ('Invoice', 'Annual membership, 2027', 'INV-2027-00214', 'QAR 500.00', '1 Mar 2027'),
            ('Receipt', 'Annual membership, 2026', 'RCT-2026-00873', 'QAR 500.00', '9 Mar 2026'),
            ('Credit note', 'Cricket tournament, cancelled', 'CRN-2026-00031', 'QAR 75.00', '22 Nov 2026'),
        ]))

    body = f"""      <div style="display: flex; flex-direction: column; gap: 18px; height: 100%;">
        {header}
        <div style="display: flex; gap: 26px; border-bottom: 1px solid #DCE3EC;
             margin-top: -2px;">{tabbar}</div>
        <div style="display: grid; grid-template-columns: minmax(0, 1.55fr) minmax(0, 1fr);
             gap: 20px; flex-grow: 1; min-height: 0;">
          <div style="display: flex; flex-direction: column; gap: 20px; min-height: 0;">
            {card('Membership', membership)}
            {card('Profile and who can see it', profile,
                  '<a href="#" style="font-size: 13px; font-weight: 700;">Open the profile</a>')}
            {card('Payments and documents', pay,
                  '<a href="#" style="font-size: 13px; font-weight: 700;">All payments</a>',
                  style='flex-grow: 1;')}
          </div>
          <div style="display: flex; flex-direction: column; gap: 20px; min-height: 0;">
            {card('Documents', docs)}
            {card('Audit trail', audit,
                  '<a href="#" style="font-size: 13px; font-weight: 700;">Full trail</a>',
                  style='flex-grow: 1;')}
          </div>
        </div>
      </div>"""

    return page(body, 'Members', 'Anand Krishnan', crumb='Members', h=1200)


# ============================================================ 4 — Approvals
_queue = [
    ('SN', 'Sreenath Nair', 'Ordinary Member', '6 days', 'Escalated to the Secretary', True, True),
    ('DP', 'Divya Pillai', 'Ordinary Member', '5 days', 'Past its time limit', True, False),
    ('AT', 'Ashok Thomas', 'Associate Member', '3 days', 'With EF for review', False, False),
    ('MK', 'Meera Krishnan', 'Ordinary Member', '2 days', 'With EF for review', False, False),
    ('VS', 'Vinod Sasidharan', 'Student Member', '1 day', 'Documents being verified', False, False),
    ('HN', 'Harish Nambiar', 'Ordinary Member', '4 hours', 'Newly submitted', False, False),
]


def approvals():
    items = ''.join(f"""<a href="#" style="display: flex; gap: 12px; padding: 14px 18px;
         border-bottom: 1px solid #EEF3F8; background: {'#F3E3E8' if on else '#FFFFFF'};
         border-left: 3px solid {'#4B1728' if on else 'transparent'};">
      {avatar(i, 34)}
      <div style="display: flex; flex-direction: column; gap: 4px; flex-grow: 1; min-width: 0;">
        <span style="font-size: 14px; font-weight: 700; color: #241017;">{n}</span>
        <span style="font-size: 12.5px; color: #7D7278;">{cat}</span>
        <span style="font-size: 12px; color: {'#7A4E12' if od else '#7D7278'};
              font-weight: {700 if od else 400};">{stage}</span>
      </div>
      <span style="font-size: 12px; color: {'#7A4E12' if od else '#9A9096'}; font-weight: 700;
            white-space: nowrap;">{w}</span></a>"""
        for i, n, cat, w, stage, od, on in _queue)

    checks = ''.join(f"""<div style="display: flex; align-items: flex-start; gap: 11px;
         padding: 12px 20px; {'border-bottom: 1px solid #EEF3F8;' if last else ''}">
      <div style="width: 20px; height: 20px; border-radius: 50%; background: {bg};
           display: flex; align-items: center; justify-content: center; flex-shrink: 0;
           margin-top: 1px;">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="{fg}"
             stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{glyph}</svg></div>
      <div style="display: flex; flex-direction: column; gap: 2px; min-width: 0;">
        <span style="font-size: 13.5px; font-weight: 600; color: #241017;">{t}</span>
        <span style="font-size: 12.5px; color: #7D7278; line-height: 1.5;">{d}</span>
      </div></div>""" for t, d, bg, fg, glyph, last in [
        ('Degree certificate verified', 'B.Tech Mechanical, 2011 — checked against the original',
         '#E4F4E3', '#2A6B27', '<path d="m5 12.5 4.5 4.5L19 7.5"/>', True),
        ('Employment confirmed', 'Aamal Industrial, letter dated 2 February 2027',
         '#E4F4E3', '#2A6B27', '<path d="m5 12.5 4.5 4.5L19 7.5"/>', True),
        ('Qatar ID verified', 'Valid to 14 November 2028',
         '#E4F4E3', '#2A6B27', '<path d="m5 12.5 4.5 4.5L19 7.5"/>', True),
        ('Proposer not yet recorded', 'EF requires one proposer in good standing',
         '#FBF2E2', '#7A4E12', '<path d="M12 7v7M12 17v.1"/>', False),
    ])

    SUP_TMPL = 'minmax(0, 1fr) 212px 84px'
    supplied = ''.join(
        row([f'<div style="display: flex; align-items: center; gap: 11px;">'
             f'{ic("doc", 17, "#7D7278")}'
             f'<span style="font-size: 13.5px; font-weight: 600; color: #241017;">{n}</span></div>',
             f'<span style="font-size: 12.5px; color: {c};">{m}</span>',
             '<a href="#" class="btn btn-s" style="height: 30px; padding: 0 12px; '
             'font-size: 12.5px;">Open</a>'],
            SUP_TMPL, pad='11px 20px', border=(k < 2))
        for k, (n, m, c) in enumerate([
            ('Degree certificate — B.Tech Mechanical', 'Checked against the original', '#2A6B27'),
            ('Qatar ID', 'Valid to 14 November 2028', '#2A6B27'),
            ('Employment letter — Aamal Industrial', 'Dated 2 February 2027', '#2A6B27'),
        ]))

    def kv2(k, v, mono=False):
        return (f'<div style="display: flex; flex-direction: column; gap: 4px;">'
                f'<span style="font-size: 11.5px; color: #7D7278; font-weight: 700;">{k}</span>'
                f'<span class="{"mono" if mono else ""}" style="font-size: 14px; color: #241017; '
                f'font-weight: 600;">{v}</span></div>')

    applicant = f"""<div style="padding: 20px; display: grid;
         grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px 16px;">
      {kv2('Applied for', 'Ordinary Member')}
      {kv2('Application', 'EF/2027/0061', True)}
      {kv2('Submitted', '2 February 2027')}
      {kv2('Discipline', 'Mechanical')}
      {kv2('Employer', 'Aamal Industrial')}
      {kv2('Years in Qatar', '6')}
      {kv2('Qualification', 'B.Tech Mechanical, 2011')}
      {kv2('Proposer', 'Not yet recorded')}
      {kv2('Email', 'On the application')}
    </div>"""

    decision = f"""<div style="padding: 18px 20px; display: flex; align-items: center; gap: 14px;
         background: #FAFCFE; border-top: 1px solid #EEF3F8;">
      <div style="display: flex; flex-direction: column; gap: 3px; flex-grow: 1;">
        <span style="font-size: 13.5px; font-weight: 700; color: #241017;">Your decision is
          recorded against your name</span>
        <span style="font-size: 12.5px; color: #7D7278;">A refusal needs a reason, which the
          applicant is shown.</span>
      </div>
      <a href="#" class="btn btn-s">Ask for more</a>
      <a href="#" class="btn btn-s" style="color: #4B1728; border-color: #E3CBD3;">Refuse</a>
      <a href="#" class="btn btn-g">{ic('check', 15, '#23361F')}Approve membership</a>
    </div>"""

    escalation = f"""<div style="display: flex; align-items: center; gap: 12px; padding: 13px 20px;
         background: #FBF2E2; border-bottom: 1px solid #EEDCBC;">
      {ic('alert', 17, '#7A4E12')}
      <span style="font-size: 13.5px; color: #7A4E12; font-weight: 700;">Six days in the queue —
        escalated to the Secretary on 6 February 2027.</span>
      <div style="flex-grow: 1;"></div>
      <span style="font-size: 12.5px; color: #7A4E12;">EF's limit is five business days</span>
    </div>"""

    detail = f"""<div class="card" style="display: flex; flex-direction: column; overflow: hidden;
         min-height: 0;">
      {escalation}
      <div style="padding: 20px 22px; display: flex; align-items: center; gap: 16px;
           border-bottom: 1px solid #EEF3F8;">
        {avatar('SN', 52, '#F3E3E8', '#4B1728', 19)}
        <div style="display: flex; flex-direction: column; gap: 5px;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <h2 style="font-size: 19px;">Sreenath Nair</h2>{chip('pending')}
          </div>
          <span style="font-size: 13px; color: #7D7278;">Mechanical Engineer ·
            Aamal Industrial · Doha</span>
        </div>
      </div>
      {applicant}
      <div style="border-top: 1px solid #EEF3F8;">
        <div class="card-h" style="border-bottom: 1px solid #EEF3F8;">
          <span class="card-t">Eligibility checks</span>
          <span style="font-size: 12.5px; color: #7A4E12; font-weight: 700;">3 of 4 cleared</span>
        </div>
        {checks}
      </div>
      <div style="border-top: 1px solid #EEF3F8;">
        <div class="card-h" style="border-bottom: 1px solid #EEF3F8;">
          <span class="card-t">Documents supplied</span>
          <span style="font-size: 12.5px; color: #7D7278;">Uploaded 2 February 2027</span>
        </div>
        {supplied}
      </div>
      <div style="flex-grow: 1; min-height: 0;"></div>
      {decision}
    </div>"""

    body = f"""      <div style="display: grid; grid-template-columns: 348px minmax(0, 1fr);
           gap: 20px; height: 100%;">
        <div class="card" style="display: flex; flex-direction: column; overflow: hidden;">
          <div class="card-h">
            <span class="card-t">Queue</span>
            <span class="chip" style="background: #F3E3E8; color: #4B1728;
                  border: 1px solid #E3CBD3;">7 waiting</span>
          </div>
          <div style="display: flex; align-items: center; gap: 8px; padding: 12px 16px;
               border-bottom: 1px solid #EEF3F8;">
            <div class="field" style="flex-grow: 1; color: #7D7278; height: 34px;">
              {ic('search', 15, '#9A9096')}<span style="font-size: 13.5px;">Search the queue</span></div>
            <a href="#" class="btn btn-s" style="height: 34px; padding: 0 11px;">
              {ic('filter', 14, '#4B1728')}</a>
          </div>
          <div style="flex-grow: 1; min-height: 0; overflow: hidden;">{items}</div>
        </div>
        {detail}
      </div>"""

    return page(body, 'Approvals', 'Approvals', h=H)


# --------------------------------------------------------------------- write
if __name__ == '__main__':
    for name, html in [('Main.dc.html', dashboard()),
                       ('Members.dc.html', members()),
                       ('MemberRecord.dc.html', member_detail()),
                       ('Approvals.dc.html', approvals())]:
        (OUT / name).write_text(html, encoding='utf-8')
        print('wrote', name, len(html), 'bytes')
