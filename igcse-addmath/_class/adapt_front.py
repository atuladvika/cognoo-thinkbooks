"""Build the guide's front matter (pages 1-9) and end matter (Notes, inside back cover, back cover)
from the CBSE Class 5 ThinkBook pages, with the changes in the cambridge-addmath-guide skill.

Usage: python3 _class/adapt_front.py <class5 folder> <last chapter page>
Reads pages p01-p09, p21, p22 and assets/ from the Class 5 folder; writes pages/pNN.svg and
overlays/pNN_front.html here. Run it again whenever the contents or the end-page numbers change."""
import os, re, sys, shutil, html as H
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(HERE)
sys.path.insert(0, '_class')
from svgtext import texts, remove_where
from svgtree import etree, find, drop, bbox, NS
from fontTools.ttLib import TTFont
import importlib.util

SRC = sys.argv[1]; LAST = int(sys.argv[2])
SUBJ = 'Cambridge IGCSE &amp; O Level Additional Mathematics'
NAVY, OCEAN, TURQ, MINT = '#1e436d', '#007fa3', '#00cfb4', '#d6f7f3'

# ---------- copy sources ----------
for f in os.listdir(f'{SRC}/assets'):
    if not os.path.exists(f'assets/{f}'):
        shutil.copy(f'{SRC}/assets/{f}', 'assets/')
for n in range(1, 10):
    shutil.copy(f'{SRC}/pages/p{n:02d}.svg', f'pages/p{n:02d}.svg')
NOTES, IBC, BC = LAST + 1, LAST + 2, LAST + 3
if (NOTES - 3 + 1) % 2:          # inner pages 3..NOTES must be even; drop Notes if not needed
    NOTES, IBC, BC = None, LAST + 1, LAST + 2
for old in os.listdir('pages'):
    m = re.match(r'p(\d+)\.svg', old)
    if m and int(m.group(1)) > LAST:
        os.remove(f'pages/{old}')
for old in os.listdir('overlays'):
    m = re.match(r'p(\d+)', old)
    if m and int(m.group(1)) > LAST:
        os.remove(f'overlays/{old}')
def copy_svg(src, n, old):   # re-prefix ids so they cannot clash with chapter pages built from the frames
    t = open(src).read()
    t = re.sub(r'(id="|url\(#|href="#)' + old + '_', lambda m: m.group(1) + f'e{n}_', t)
    open(f'pages/p{n:02d}.svg', 'w').write(t)
copy_svg(f'{SRC}/pages/p21.svg', IBC, 'p21')
open(f'overlays/p{IBC:02d}.html', 'w').write(open(f'{SRC}/overlays/p21.html').read().replace(
    '.ib .hd .bar{flex:none;', '.ib .hd .bar{position:static;flex:none;').replace(
    'Developed in line with <i>NEP 2020</i> and <i>NCF-SE 2023</i>, which give Computational Thinking a central place in school learning from the early years.',
    'Designed for Cambridge IGCSE and O Level Additional Mathematics, where clear method and reasoning matter as much as the final answer.'))
assert 'NEP' not in open(f'overlays/p{IBC:02d}.html').read()
copy_svg(f'{SRC}/pages/p22.svg', BC, 'p22')

_f = {}
def width(s, size, face='Poppins-Regular', track=0):
    if face not in _f:
        t = TTFont(f'fonts/{face}.ttf'); _f[face] = (t.getBestCmap(), t['hmtx'], t['head'].unitsPerEm)
    cm, hm, upm = _f[face]
    return sum(hm[cm.get(ord(c), cm[ord('?')])][0] for c in s) * size / upm + track * size * len(s)

def rd(n): return open(f'pages/p{n:02d}.svg').read()
def wr(n, s): open(f'pages/p{n:02d}.svg', 'w').write(s)
def ov(n, body, name='front'):
    open(f'overlays/p{n:02d}_{name}.html', 'w').write(f'<!-- Guide text for this page (from _class/adapt_front.py) -->\n<div class="ov">\n{body}\n</div>\n')

def line(x, base, size, text, weight=400, color=NAVY, style='normal', anchor='start', extra=''):
    top = base - size * 1.1
    al = {'start': '', 'end': 'transform:translateX(-100%);', 'middle': 'transform:translateX(-50%);'}[anchor]
    return (f'<div class="abs" style="left:{x:.2f}pt;top:{top:.2f}pt;font-family:Poppins;font-size:{size}pt;line-height:{size*1.5:.2f}pt;'
            f'font-weight:{weight};font-style:{style};color:{color};white-space:pre;{al}{extra}">{text}</div>')

def para(x, base, w, size, pitch, text, justify=True, color=NAVY):
    top = base - size * 1.1 - (pitch - size * 1.5) / 2
    return (f'<div class="abs fpara" style="left:{x:.2f}pt;top:{top:.2f}pt;width:{w:.2f}pt;font-family:Poppins;font-size:{size}pt;'
            f'line-height:{pitch}pt;color:{color};text-align:{"justify" if justify else "left"}">{text}</div>')

def header_fix(n):
    s = rd(n)
    s, _ = remove_where(s, lambda t: 40 < t['y'] < 50 and t['x'] > 400)
    wr(n, s)
    return f'<div class="hdr2">{SUBJ}</div>'

def xml_edit(n, fn):
    tree = etree.parse(f'pages/p{n:02d}.svg'); fn(tree.getroot())
    s = etree.tostring(tree.getroot(), encoding='unicode')
    wr(n, s)

STYLE = ('<style>.fpara b{font-weight:700}.fpara i{font-style:italic}.fpara .oc{color:#007fa3}'
         '.qrph{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3pt;border:1pt dashed #007fa3;border-radius:4pt;'
         'box-sizing:border-box;font-size:6.6pt;font-weight:700;line-height:8pt;color:#007fa3;text-align:center;background:#fff}</style>')

# ======================= page 1: front cover =======================
s = rd(1)
s, _ = remove_where(s, lambda t: t['text'] in ('THINKBOOK COMPANION', 'Computational', 'Thinking', 'CLASS')
                    or (280 < t['y'] < 312 and t['size'] > 13))
wr(1, s)
def cover(root):
    for e in find(root, lambda bb, e: e.get('fill') == MINT and 115 < bb[1] < 130 and bb[0] < 60):
        drop(e)                                             # old pill (sized for COMPANION)
    for g in list(root.iter(NS + 'g')):                     # class badge: glow, disc, ring, CLASS text group
        cp, mk = g.get('clip-path', ''), g.get('mask', '')
        if mk == 'url(#p1_mask_53)' or cp in ('url(#p1_clip_56)', 'url(#p1_clip_60)', 'url(#p1_clip_63)'):
            if g.getparent() is not None:
                g.getparent().remove(g)
xml_edit(1, cover)
pill_text = 'THINKBOOK GUIDE'
pw = width(pill_text, 11.52, 'Poppins-Bold', 0.15) + 2 * 10.7
T1, T2 = 'Cambridge IGCSE &amp; O Level', 'Additional Mathematics'
size = round(min(53.28, 517.8 / max(width('Cambridge IGCSE & O Level', 1, 'Poppins-Bold'), width('Additional Mathematics', 1, 'Poppins-Bold'))) - 0.05, 2)
b2 = 249.0; b1 = b2 - size * 1.12
body = [
    f'<div class="abs" style="left:48.0pt;top:121.5pt;width:{pw:.1f}pt;height:26.2pt;border-radius:13.1pt;background:{MINT}"></div>',
    line(58.7, 138.7, 11.52, pill_text, 700, OCEAN, extra='letter-spacing:.15em;'),
    line(48.2, b1, size, T1, 700, NAVY),
    line(48.2, b2, size, T2, 700, OCEAN),
    line(49.6, 289.5, 13.44, f'Your <b style="color:{OCEAN}">thinking guide</b>', 400, NAVY),
]
ov(1, '\n'.join(body))
for f in os.listdir('overlays'):
    if f == 'p01.html': os.remove('overlays/p01.html')

# ======================= page 2: copyright (only the pill changes) =======================
s = rd(2)
s, _ = remove_where(s, lambda t: t['text'].startswith('CLASS '))
wr(2, s)
xml_edit(2, lambda r: [drop(e) for e in find(r, lambda bb, e: e.get('fill') == MINT and 125 < bb[1] < 140 and bb[0] < 60)])
pill2 = 'IGCSE &amp; O LEVEL · ADDITIONAL MATHEMATICS'
pw2 = width('IGCSE & O LEVEL · ADDITIONAL MATHEMATICS', 10.56, 'Poppins-Bold', 0.15) + 2 * 10.3
ov(2, f'<div class="abs" style="left:48.0pt;top:133.5pt;width:{pw2:.1f}pt;height:24pt;border-radius:12pt;background:{MINT}"></div>\n'
      + line(58.3, 149.2, 10.56, pill2, 700, OCEAN, extra='letter-spacing:.15em;'))

# ======================= page 3: contents =======================
s = rd(3)
s, _ = remove_where(s, lambda t: (40 < t['y'] < 50 and t['x'] > 400) or (abs(t['y'] - 111) < 1 and abs(t['size'] - 9.99) < .1))
wr(3, s)
def load(f):
    sp = importlib.util.spec_from_file_location('m', f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
exfiles = sorted(f'chapters/{f}' for f in os.listdir('chapters') if re.match(r'ch\d+_ex\d+\.py$', f))
chapters = {}; pg = 10
for f in exfiles:
    m = load(f); c = m.CH['num']
    chapters.setdefault(c, {'title': m.CH['title'], 'page': pg, 'ex': []})['ex'].append((m.CH['exercise'], pg))
    pg += len(m.PAGES)
sub = 'Follows the Cambridge IGCSE &amp; O Level Additional Mathematics Coursebook'
subw = width('Follows the Cambridge IGCSE & O Level Additional Mathematics Coursebook', 9.99, 'Poppins-Medium')
rows = [line(198.2 if 198.2 + subw < 564 else 54.3, 111.0 if 198.2 + subw < 564 else 127.0, 9.99, sub, 500, OCEAN)]
y = 230.22
def leader(x0, y0, x1):
    return (f'<div class="abs" style="left:{x0:.2f}pt;top:{y0:.2f}pt;width:{x1-x0:.2f}pt;height:.75pt;'
            f'background-image:linear-gradient(90deg,#cccccc 50%,transparent 50%);background-size:1.5pt .75pt"></div>')
def pbox(y0, n, x=522.37):
    return (f'<div class="abs" style="left:{x}pt;top:{y0 + 4.13:.2f}pt;width:36pt;height:23.25pt;border:.75pt solid #00cfb4;border-radius:4.5pt;box-sizing:border-box"></div>'
            + line(x + 18.1, y0 + 19.49, 11.49, str(n), 700, NAVY, anchor='middle'))
for i, (c, ch) in enumerate(sorted(chapters.items())):
    navy = (c % 2 == 1); tab = '#1d426d' if navy else '#007ea2'; capc = TURQ if navy else MINT
    tw = width(ch['title'], 12.49, 'Poppins-Medium')
    rows.append(f'<div class="abs" style="left:54pt;top:{y:.2f}pt;width:48.75pt;height:31.5pt;border-radius:5.7pt;background:{tab}"></div>'
                + line(78.24, y + 10.49, 5.59, 'CHAPTER', 700, capc, anchor='middle')
                + line(78.4, y + 22.49, 12.99, str(c), 700, '#ffffff', anchor='middle')
                + line(112.44, y + 20.24, 12.49, H.escape(ch['title']), 500)
                + leader(112.44 + tw + 10.7, y + 20.28, 512.3) + pbox(y, ch['page']))
    y += 38
    for ex, p in ch['ex']:
        ew = width(ex, 11, 'Poppins-Medium')
        rows.append(f'<div class="abs" style="left:116pt;top:{y + 11.5:.2f}pt;width:5pt;height:5pt;border-radius:50%;background:{TURQ}"></div>'
                    + line(128, y + 19.0, 11, ex, 500)
                    + leader(128 + ew + 10.7, y + 19.0, 512.3) + pbox(y - 1.5, p))
        y += 30
    y += 10
assert y < 790, 'contents overflow'
ov(3, header_fix(3) + '\n' + '\n'.join(rows))

# ======================= page 4: The Thinking Coach =======================
s = rd(4)
s, _ = remove_where(s, lambda t: (140 < t['y'] < 240)                                  # heading + intro
                    or (290 < t['y'] < 345)                                             # habit cards
                    or abs(t['y'] - 469.5) < 1                                          # flow title
                    or (t['x'] < 290 and 530 < t['y'] < 580)                            # STEP 1 and 2 text
                    or (700 < t['y'] < 760))                                            # closing paragraph + bullet 1
wr(4, s)
CARDS = [(45.1, 'Break it down', 'SMALLER STEPS', 'Split a long question into parts and cases. Solve one at a time.'),
         (173.2, 'Spot the pattern', 'FUNCTION TYPE', 'Recognise the kind of function: line, quadratic, modulus, fraction.'),
         (301.6, 'Picture it', 'SKETCH THE GRAPH', 'Sketch the graph to see the range, crossings and turning points.'),
         (428.9, 'Check each step', 'DOMAIN AND METHOD', 'Follow a clear method. Check each answer against the domain.')]
b = [line(67.7, 146.2, 13.0, 'Why Thinking Matters in Additional Mathematics', 700),
     para(54.4, 165.7, 510, 9.2, 13.5,
          'Additional Mathematics asks for more than a formula you remember. Each exercise asks you to read a question closely, '
          'choose a method, work through it step by step and check that the answer makes sense, often against a domain, a graph '
          'or the original equation.'),
     para(54.4, 211.5, 510, 9.2, 13.0,
          'Good questions do not ask <b>“What is the answer?”</b> They ask <b>“How did you work it out?”</b> Examiners reward the '
          '<i>process of thinking</i> and clear working, not just the final line. In this guide, you build four big thinking habits:')]
for x0, t, lab, d in CARDS:
    cx = x0 + 60.4
    b.append(line(cx, 296.2, 9.6, t, 700, anchor='middle'))
    b.append(line(cx, 308.2, 7.39, lab, 700, OCEAN, anchor='middle'))
    b.append(f'<div class="abs" style="left:{x0 + 6:.1f}pt;top:{314.0:.1f}pt;width:108.8pt;font-family:Poppins;font-size:7.6pt;line-height:9.75pt;color:{NAVY};text-align:center">{d}</div>')
b += [line(297.4, 469.5, 11.54, 'THINKBOOK FLOW: ONE EXERCISE AT A TIME', 700, anchor='middle'),
      line(118.0, 540.2, 8.14, 'Exercise Opener', 700, anchor='middle'),
      line(118.0, 553.1, 6.52, 'What you need to know', 400, anchor='middle'),
      line(118.0, 562.6, 6.52, 'and Atul Sir\'s lecture', 400, anchor='middle'),
      line(225.0, 540.2, 8.14, 'Exercise Questions', 700, anchor='middle'),
      line(225.0, 553.1, 6.52, 'Every coursebook question,', 400, anchor='middle'),
      line(225.0, 562.6, 6.52, 'in the same order', 400, anchor='middle'),
      para(54.4, 708.0, 510, 9.2, 13.47,
           'The ThinkBook Guide follows the <b>Cambridge IGCSE &amp; O Level Additional Mathematics Coursebook</b> chapter by chapter '
           f'and exercise by exercise. This volume covers <i>Chapter 1: Functions</i>. Each exercise includes:', justify=False),
      para(71.4, 740.2, 492, 9.2, 12.8,
           'An <b>exercise opener</b> with Atul Sir\'s lecture, then <b>every question from the coursebook exercise</b> in the same order',
           justify=False)]
ov(4, header_fix(4) + '\n' + STYLE + '\n' + '\n'.join(b))

# ======================= page 5: AI tutoring, personalisation, note =======================
s = rd(5)
s, _ = remove_where(s, lambda t: (728 < t['y'] < 805 and 60 < t['x'] < 560) or t['text'].startswith('.Younger learners'))
wr(5, s)
sys.path.insert(0, '_class')
from glyphs_svg import MAP, IN, R
X = '<i>x</i>'
b = [line(555.0, 113.7, 9.5, '.', 400),
     line(107.53, 155.22, 7.39, 'CHAPTER 1 · FUNCTIONS · EXERCISE 1.1', 700, OCEAN),
     line(107.53, 170.97, 9.79, f'Is the mapping <b>{X} {MAP} {X}<sup>3</sup>, {X} {IN} {R}</b> one-one, many-one or one-many?', 400),
     line(107.53, 188.97, 9.4, 'a) one-one&#160;&#160;&#160;&#160;&#160;&#160;b) many-one&#160;&#160;&#160;&#160;&#160;&#160;c) one-many', 400),
     line(71.36, 428.97, 9.5, '<b>Composite functions</b>) to show exactly what needs more practice in that exercise.', 400),
     line(93.48, 649.02, 6.38, 'e.g. Composite functions', 400),
     para(70.2, 738.0, 478, 9.3, 13.8,
          'Use this guide <b>before</b> the class discusses the answers. Let the student try first, read the Thinking Question aloud, '
          'and give them time to choose a method.', justify=False),
     para(70.2, 785.2, 478, 9.3, 13.8,
          'Praise the method, not only the right answer. A wrong attempt that is checked and corrected is a step in learning, not a failure.',
          justify=False)]
ov(5, header_fix(5) + '\n' + STYLE + '\n' + '\n'.join(b))

# ======================= pages 6-9: Try it examples from the coursebook =======================
TRY = [
    ('EXERCISE 1.3, QUESTION 1', f'f : {X} {MAP} 2{X} + 3 and g : {X} {MAP} {X}<sup>2</sup> − 1 for {X} {IN} {R}. Find fg(2).',
     'Two machines in a line: g works on 2 first, then f works on what comes out.'),
    ('EXERCISE 1.2, QUESTION 3', f'g({X}) = {X}<sup>2</sup> + 2 for {X} ≥ 0. Find the range of g.',
     f'Begin at the start of the domain, {X} = 0. What output does it give?'),
    ('EXERCISE 1.4, QUESTION 1a', 'Solve |3<i>x</i> − 2| = 10.',
     'Split it into two equations: 3x − 2 = 10 and 3x − 2 = −10. Solve each.'),
    ('EXERCISE 1.1, QUESTION 8', f'Is {X} {MAP} ±{X}, {X} ≥ 0 one-one, many-one or one-many?',
     f'Say it aloud: “{X} goes to plus {X} and to minus {X}.” How many outputs is that?'),
    ('EXERCISE 1.3, QUESTION 3', f'f({X}) = ({X} + 2)<sup>2</sup> − 1 for {X} {IN} {R}. Find f<sup>2</sup>(3).',
     'Recall what f² means: apply f twice. It is not f(3) squared.'),
    ('EXERCISE 1.1, QUESTION 2', f'Is {X} {MAP} {X}<sup>2</sup> + 5, {X} {IN} {R} one-one, many-one or one-many?',
     'Ask why two inputs could meet: what does squaring do to a minus sign?'),
    ('EXERCISE 1.2, QUESTION 2a', f'Find the range of f({X}) = {X} − 5 for −2 ≤ {X} ≤ 7.',
     'Turn it into numbers: work out f(−2) and f(7), the outputs at the two ends.'),
]
BOX = {6: [368.2, 685.5], 7: [299.2, 664.5], 8: [298.5, 665.2], 9: [324.0]}
BOXH = {6: [74.3, 74.2], 7: [86.3, 62.2], 8: [74.2, 74.3], 9: [86.2]}
k = 0
for n in (6, 7, 8, 9):
    s = rd(n)
    if n == 6:
        s, _ = remove_where(s, lambda t: t['text'].startswith(' example from your handbook'))
    wr(n, s)
    body = []
    if n == 6:
        body.append(line(286.1, 153.7, 9.3, ' example from your coursebook.', 400))
    for top, h in zip(BOX[n], BOXH[n]):
        lab, q, th = TRY[k]; k += 1
        body.append(f'<div class="abs tryit" style="left:290.52pt;top:{top+4.3:.2f}pt;width:258pt;height:{h-6:.1f}pt">'
                    f'<div class="lab">TRY IT · {lab}</div><p>{q}</p><p class="th"><b>Think:</b> {th}</p></div>')
    ov(n, header_fix(n) + '\n<style>.tryit{font-family:Poppins;color:#1e436d}.tryit .lab{font-size:6.99pt;font-weight:700;color:#007fa3;line-height:12pt;letter-spacing:.02em}'
          '.tryit p{font-size:8.59pt;line-height:12pt;margin:.95pt 0 0}.tryit p.th{margin-top:2.25pt}.tryit p.th b{color:#007fa3}</style>\n' + '\n'.join(body))

# ======================= Notes page =======================
def footer_num(p):
    cx = 61.18 if p % 2 == 0 else 551.67
    return (f'<div class="abs" style="left:{cx-17:.2f}pt;top:807.73pt;width:34pt;height:21pt;box-sizing:border-box;border:1.1pt solid #00cfb4;background:#d6f7f3;border-radius:6pt;display:flex;align-items:center;justify-content:center;'
            f'font-family:Poppins;font-weight:700;font-size:10.49pt;color:#1e436d">{p}</div>')
if NOTES:
    s = open(f'_class/frame_{"even" if NOTES % 2 == 0 else "odd"}.svg').read().replace('PFX_', f'p{NOTES}_')
    s, _ = remove_where(s, lambda t: abs(t['y'] - 43.5) < 1)
    wr(NOTES, s)
    lines_ = ''.join(f'<div class="abs" style="left:48.4pt;width:516pt;top:{140+26*i}pt;border-bottom:.75pt solid #cccccc"></div>' for i in range(25))
    ov(NOTES, footer_num(NOTES) + f'<div class="hdr2">{SUBJ}</div>'
              '<div class="abs" style="left:48.4pt;top:84pt;font-family:Poppins;font-size:24pt;font-weight:700;line-height:34pt;color:#1e436d">Notes</div>'
              '<div class="abs" style="left:48.4pt;top:118pt;font-family:Poppins;font-size:8pt;color:#007fa3">Your own working and the doubts you want to ask Dyna.</div>' + lines_)

# ======================= back cover =======================
s = rd(BC)
s, _ = remove_where(s, lambda t: 205 < t['y'] < 252 or t['text'] in ('Learning to Think ', 'Starts Early'))
wr(BC, s)
ov(BC, STYLE + '\n' + line(46.9, 137.2, 25.0, f'Learning to Think, <span style="color:{OCEAN}">Not Just to Solve</span>', 700) + '\n' + para(46.55, 150.71 + 10.8 * 1.1 + 1.65, 514, 10.8, 16.5,
       'In Additional Mathematics, students move from following methods to choosing them: reading a question closely, splitting it '
       'into cases, sketching a graph and checking each answer. These thinking skills matter in every exam and every subject.', justify=False)
       + '\n' + para(46.55, 224.0, 514, 10.8, 16.5,
       'This ThinkBook Guide works alongside the <b class="oc">Cambridge IGCSE &amp; O Level Additional Mathematics Coursebook</b>. '
       'It helps students <b class="oc">learn how to think</b> through each exercise step by step, while supporting parents and teachers in guiding them.',
       justify=False))
bc = open(f'{SRC}/overlays/p22.html').read()
ph = lambda kind: (f'<div class="qrph" style="width:72pt;height:72pt"><svg width="11" height="11" viewBox="0 0 14.4 14.4"><circle cx="7.2" cy="7.2" r="7.2" fill="#007fa3"/>'
                   f'<path d="M5.6 4.4V10L10.2 7.2Z" fill="#fff"/></svg><span>{kind}<br>coming soon</span></div>')
bc = bc.replace('<img src="assets/CGN000016.png" alt="Explainer video QR">', ph('Explainer video'))
bc = bc.replace('<img src="assets/CGN000004.png" alt="Dyna Thinking Coach QR">', ph('Dyna QR'))
bc = bc.replace("CBSE now asks every child in Classes 3–8 to think, not just answer. See how this ThinkBook and <b>Dyna</b>, your child's personal Thinking Coach, guide each step with the 7 Thinking Skills.",
                'See how this ThinkBook Guide and <b>Dyna</b>, your personal Thinking Coach, take you through every Additional Mathematics exercise with the 7 Thinking Skills.')
bc = bc.replace('Scan to watch the<br>4-minute video', 'Scan to watch the<br>explainer video')
bc = bc.replace('When a child is stuck', 'When a student is stuck').replace('guides them with', 'guides them with')
assert 'CBSE' not in bc and 'CGN0000' not in bc
open(f'overlays/p{BC:02d}.html', 'w').write(bc)
print('front matter built; notes', NOTES, 'inside back', IBC, 'back', BC)
