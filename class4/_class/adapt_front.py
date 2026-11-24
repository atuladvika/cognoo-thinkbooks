"""Adapt the class-specific text of pages 1-9, the Notes page and the back cover.
Run once when creating a new class folder from class3/. Reads _class/config.json.
Pages are edited in place (SVG text removed or swapped); new text goes into overlays/pNN_front.html,
which make.py appends after the page's own overlay."""
import json, os, re, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from svgtext import texts, remove_where, swap
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(HERE)
C = json.load(open('_class/config.json'))
N = str(C['class'])

_fonts = {}
def width(s, size, face='Poppins-Medium'):
    if face not in _fonts:
        f = TTFont(f'fonts/{face}.ttf'); _fonts[face] = (f.getBestCmap(), f['hmtx'], f['head'].unitsPerEm)
    cm, hm, upm = _fonts[face]
    return sum(hm[cm.get(ord(ch), cm[ord('?')])][0] for ch in s) * size / upm

def esc(s):
    return html.escape(s, quote=False)

def rd(p): return open(f'pages/{p}.svg').read()
def wr(p, s): open(f'pages/{p}.svg', 'w').write(s)
def ov(p, body):
    open(f'overlays/{p}_front.html', 'w').write(f'<!-- Class {N} text for this page (from _class/adapt_front.py) -->\n<div class="ov">\n{body}\n</div>\n')

def txt(x, base, size, text, weight=400, color='#1e436d', style='normal', anchor='start', family='Poppins', extra=''):
    """Absolutely placed single line; base = baseline in pt. Poppins ascent ~1.05em; we place by top = base - 0.93*size*1.0."""
    top = base - size * 1.1
    al = {'start': '', 'end': 'transform:translateX(-100%);', 'middle': 'transform:translateX(-50%);'}[anchor]
    return (f'<div class="abs" style="left:{x:.2f}pt;top:{top:.2f}pt;font-family:{family};font-size:{size}pt;line-height:{size*1.5:.2f}pt;'
            f'font-weight:{weight};font-style:{style};color:{color};white-space:pre;{al}{extra}">{text}</div>')

# ---------- every page: running header class number ----------
for p in sorted(f[:-4] for f in os.listdir('pages') if f.endswith('.svg')):
    s = rd(p)
    s, n = swap(s, '&#x00b7; Class 3', f'&#x00b7; Class {N}')
    if n: wr(p, s)

# ---------- page 1: class badge ----------
s = rd('p01')
s, gone = remove_where(s, lambda t: t['size'] > 55 and t['text'].strip() == '3')
wr('p01', s)
b = gone[0]
ov('p01', txt(516.15, b['y'], 60, N, 700, '#ffffff', anchor='middle'))

# ---------- page 2: class pill ----------
s = rd('p02'); s, _ = swap(s, 'CLASS 3', f'CLASS {N}'); wr('p02', s)

# ---------- page 3: contents ----------
s = rd('p03')
s, _ = swap(s, 'CBSE Class 3 Computational', f'CBSE Class {N} Computational')
rows = [t for t in texts(s) if abs(t['size'] - 12.5) < 0.1 and t['x'] > 100 and t['y'] > 230]
rows.sort(key=lambda t: t['y'])
assert len(rows) == 14, len(rows)
# remove chapter leader dots (rows below the front-matter box)
s = re.sub(r'<path transform="matrix\(\.75,0,0,\.75,[\d.]+,(\d+\.\d+)\)" d="M\d+ 0H\d+V1H\d+Z" fill="#cccccc"/>\n?',
           lambda m: '' if float(m.group(1)) > 240 else m.group(0), s)
s, _ = remove_where(s, lambda t: abs(t['size'] - 12.5) < 0.1 and t['x'] > 100 and t['y'] > 230)
add = []
titles = C['chapters']
lead_y = [250.50545, 291.00544, 332.25544, 373.50544, 414.00544, 455.25544, 496.50547, 537.7555, 578.2555, 619.5055, 660.7555, 701.2555, 742.5055, 783.7555]
for i, (r, title) in enumerate(zip(rows, titles)):
    el = r['el']
    el = re.sub(r'(<tspan y="[^"]+" x=")[^"]+(">)[^<]*(</tspan>)', lambda m: m.group(1) + '149.9375' + m.group(2) + esc(title) + m.group(3), el)
    add.append(el)
    x0 = 112.453 + width(title, 12.5) + 10.7
    k0 = 0
    xs = x0
    dots = []
    k = 0
    while xs + 0.75 * (2 * k + 1) <= 512.3:
        dots.append(f'<path transform="matrix(.75,0,0,.75,{x0:.3f},{lead_y[i]})" d="M{2*k} 0H{2*k+1}V1H{2*k}Z" fill="#cccccc"/>')
        k += 1
    add.extend(dots)
s = s.replace('</svg>', '\n'.join(add) + '\n</svg>')
wr('p03', s)

# ---------- page 4 ----------
s = rd('p04')
s, _ = swap(s, 'Even in Class 3', f'Even in Class {N}')
s, _ = swap(s, 'Class 3, you begin', f'Class {N}, you begin')
s, _ = swap(s, 'CBSE Class 3 Computational', f'CBSE Class {N} Computational')
s, line = remove_where(s, lambda t: abs(t['y'] - 721.47) < 0.5 and t['x'] < 400)
wr('p04', s)
y = 721.47; x = 54.35; parts = [(C['first_chapter'], 'italic'), (' to ', 'normal'), (C['last_chapter'], 'italic'), ('. Each chapter includes:', 'normal')]
body = []
for t, st in parts:
    body.append(txt(x, y, 9.2, esc(t), 400, style=st))
    x += width(t, 9.2, 'Poppins-Italic' if st == 'italic' else 'Poppins-Regular')
ov('p04', '\n'.join(body))

# ---------- page 5 ----------
s = rd('p05')
s, _ = remove_where(s, lambda t: 150 < t['y'] < 192 and t['x'] > 100)          # mock card text
s, _ = remove_where(s, lambda t: abs(t['y'] - 428.97) < 0.5)                    # 3rd line of Gap Analysis paragraph
s, _ = remove_where(s, lambda t: t['text'].startswith('e.g. '))                   # diagram example
wr('p05', s)
m = C['mock']
body = [txt(107.53, 155.22, 7.39, esc(m['title']), 700, '#007fa3')]
qx = 107.53
for seg, bold in m['question']:
    body.append(txt(qx, 170.97, 9.79, esc(seg), 700 if bold else 400))
    qx += width(seg, 9.79, 'Poppins-Bold' if bold else 'Poppins-Regular')
ox = 107.53
for o in m['options']:
    body.append(txt(ox, 188.97, 9.4, esc(o), 400))
    ox += width(o, 9.4, 'Poppins-Regular') + m.get('option_gap', 14)
body.append(txt(71.36, 428.97, 9.5, f'<b>{esc(C["concept"])}</b>) to show exactly what needs more practice in that chapter.', 400))
body.append(txt(93.48, 649.02, 6.38, 'e.g. ' + esc(C['concept']), 400))
ov('p05', '\n'.join(body))

# ---------- pages 6-9: Try it boxes ----------
BOX = {'p06': [368.2, 685.5], 'p07': [299.2, 664.5], 'p08': [298.5, 665.2], 'p09': [324.0]}
BOXH = {'p06': [74.3, 74.2], 'p07': [86.3, 62.2], 'p08': [74.2, 74.3], 'p09': [86.2]}
k = 0
for p in ['p06', 'p07', 'p08', 'p09']:
    s = rd(p)
    for top, h in zip(BOX[p], BOXH[p]):
        s, _ = remove_where(s, lambda t, top=top, h=h: t['x'] > 285 and top < t['y'] < top + h)
    wr(p, s)
    body = []
    for top, h in zip(BOX[p], BOXH[p]):
        ex = C['tryit'][k]; k += 1
        body.append(f'<div class="abs tryit" style="left:290.52pt;top:{top+4.3:.2f}pt;width:258pt;height:{h-6:.1f}pt">'
                    f'<div class="lab">TRY IT · CHAPTER {ex["ch"]}, QUESTION {ex["q"]}</div>'
                    f'<p>{ex["text"]}</p><p class="th"><b>Think:</b> {ex["think"]}</p></div>')
    ov(p, '<style>.tryit{font-family:Poppins;color:#1e436d}.tryit .lab{font-size:6.99pt;font-weight:700;color:#007fa3;line-height:12pt;letter-spacing:.02em}'
           '.tryit p{font-size:8.59pt;line-height:12pt;margin:.95pt 0 0}.tryit p.th{margin-top:2.25pt}.tryit p.th b{color:#007fa3}</style>\n' + '\n'.join(body))

# ---------- Notes page (p20 in class3) ----------
# header already swapped above

# ---------- back cover intro ----------
s = rd('p22')
s, gone = remove_where(s, lambda t: 150 < t['y'] < 200 and t['x'] < 60)
wr('p22', s)
ov('p22', f'<div class="abs" style="left:46.55pt;top:{162.74-12.03:.2f}pt;width:514pt;font-family:Poppins;font-size:10.8pt;line-height:16.5pt;color:#1e436d">{C["backcover_intro"]}</div>')
print('front matter adapted for Class', N)
