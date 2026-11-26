"""Render the chapter pages (opener, questions, supplementary) of one chapter into pages/pNN.svg (blank frame)
and overlays/pNN.html (content). Usage: python3 _class/chapter_gen.py chapters/ch1.py"""
import os, sys, re, json, importlib.util, html as H
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(HERE)
spec = importlib.util.spec_from_file_location('chap', sys.argv[1]); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
N = ''
CH = M.CH; num = CH['num']; T = CH['title']; FIG = f'assets/ch{num}/'
from PIL import Image

def isz(name):
    return Image.open(FIG + name + '.png').size

def img(name, w=None, h=None, style=''):
    W, Hh = isz(name)
    if w and not h: h = w * Hh / W
    if h and not w: w = h * W / Hh
    return f'<img src="{FIG}{name}.png" style="width:{w:.1f}pt;height:{h:.1f}pt;{style}">'

def ico(sk, size=None, cls='ico'):
    st = f' style="width:{size}pt;height:{size}pt"' if size else ''
    return f'<span class="{cls}"{st}><img src="assets/icons/icon_{sk.lower()}.png"></span>'

PLAY = ('<svg class="play" viewBox="0 0 14.4 14.4" style="left:{l}pt;top:{t}pt"><circle cx="7.2" cy="7.2" r="7.2" fill="#fff"/>'
        '<circle cx="7.2" cy="7.2" r="6" fill="{c}"/><path d="M5.6 4.4V10L10.2 7.2Z" fill="#fff"/></svg>')
CHAT = ('<svg width="11" height="9.5" viewBox="0 0 11 9.5" style="flex:none"><rect x=".6" y="2.2" width="9.8" height="6.8" rx="2.2" fill="none" stroke="#007fa3" stroke-width=".95"/>'
        '<path d="M5.5 2.2V.6" stroke="#007fa3" stroke-width=".95"/><circle cx="3.7" cy="5.6" r=".8" fill="#007fa3"/><circle cx="7.3" cy="5.6" r=".8" fill="#007fa3"/></svg>')
BULB = ('<svg width="19" height="19" viewBox="0 0 19 19"><circle cx="9.5" cy="9.5" r="9.5" fill="#00cfb4"/>'
        '<path d="M9.5 4.3a3.6 3.6 0 0 0-2.1 6.5c.4.3.6.7.6 1.1v.6h3v-.6c0-.4.2-.8.6-1.1A3.6 3.6 0 0 0 9.5 4.3Z" fill="none" stroke="#1e436d" stroke-width="1"/>'
        '<path d="M8.1 14h2.8M8.5 15.4h2" stroke="#1e436d" stroke-width="1" stroke-linecap="round"/></svg>')

def footer_num(p):
    cx = 61.18 if p % 2 == 0 else 551.67
    return (f'<div class="abs" style="left:{cx-17:.2f}pt;top:807.73pt;width:34pt;height:21pt;box-sizing:border-box;border:1.1pt solid #00cfb4;background:#d6f7f3;border-radius:6pt;display:flex;align-items:center;justify-content:center;'
            f'font-family:Poppins;font-weight:700;font-size:10.49pt;color:#1e436d">{p}</div>')

def frame(p):
    s = open(f'_class/frame_{"even" if p % 2 == 0 else "odd"}.svg').read().replace('PFX_', f'p{p}_')
    s = re.sub(r'(<tspan[^>]*>)3(</tspan>)', lambda m: m.group(1) + N + m.group(2), s, count=1) if False else s
    # class digit in the running header (single-glyph text element at y 43.5)
    from svgtext import remove_where
    s, _ = remove_where(s, lambda t: abs(t['y'] - 43.5) < 1)
    open(f'pages/p{p:02d}.svg', 'w').write(s)

sys.path.insert(0, '_class')

def opts_row(q):
    if q.get('parts'):
        cells = ''.join(f'<div class="part"><i class="lt">{pt[0]}</i><span class="pm">{pt[1]}</span><div class="wl"><span>{pt[2] if len(pt) > 2 else q.get("part_label", "Range:")}</span><span class="dash"></span></div></div>' for pt in q['parts'])
        cols = 'style="grid-template-columns:1fr"' if q.get('cols') == 1 else ''
        return f'<div class="parts" {cols}>{cells}</div>'
    if q.get('write'):
        return f'<div class="wline"><span class="wl-l">{q["write"]}</span><span class="dash"></span></div>'
    if 'img_opts' in q:
        cells = ''.join(f'<div class="o"><i class="lt">{l})</i>{img(n, w)}</div>' for l, (n, w) in zip('abcd', q['img_opts']))
        return f'<div class="opts img">{cells}<div class="myans">My answer<span></span></div></div>'
    if 'img_opts2' in q:  # two per row
        c = [f'<div class="o" style="width:210pt"><i class="lt">{l})</i>{img(n, w)}</div>' for l, (n, w) in zip('abcd', q['img_opts2'])]
        return (f'<div class="opts img">{c[0]}{c[1]}</div><div class="opts img" style="margin-top:3pt">{c[2]}{c[3]}'
                f'<div class="myans">My answer<span></span></div></div>')
    ops = q['opts'] if q.get('raw') else [H.escape(o) for o in q['opts']]; L = 'abcde'
    longest = max(len(re.sub(r'<svg.*?</svg>', 'xx', re.sub(r'<span class="frac">.*?</span></span>', 'xxx', o))) - len(re.findall(r'<[^>]+>', re.sub(r'<svg.*?</svg>', '', o))) * 0 for o in ops)
    longest = max(len(re.sub(r'<[^>]+>', '', re.sub(r'<svg.*?</svg>', 'x', re.sub(r'<span class="frac">.*?</span></span>', 'xx', o)))) for o in ops)
    if longest > 30:   # one option per line
        rows = [f'<div class="opts" style="height:15pt;margin-top:{3 if i == 0 else 0}pt"><div class="o" style="width:auto"><i class="lt">{l})</i> {o}</div>'
                + ('<div class="myans">My answer<span></span></div>' if i == len(ops) - 1 else '') + '</div>' for i, (l, o) in enumerate(zip(L, ops))]
        return ''.join(rows)
    if longest > 16 or (len(ops) == 5 and longest > 9):
        c = [f'<div class="o" style="width:180pt"><i class="lt">{l})</i> {o}</div>' for l, o in zip(L, ops)]
        rows = [c[i:i + 2] for i in range(0, len(c), 2)]
        return ''.join(f'<div class="opts" style="margin-top:{4 if k == 0 else 0}pt">{"".join(r)}'
                       + ('<div class="myans">My answer<span></span></div>' if k == len(rows) - 1 else '') + '</div>' for k, r in enumerate(rows))
    w = {3: 120, 4: 105}.get(len(ops), 80)
    cells = ''.join(f'<div class="o" style="width:{w}pt"><i class="lt">{l})</i> {o}</div>' for l, o in zip(L, ops))
    return f'<div class="opts">{cells}<div class="myans">My answer<span></span></div></div>'

def dyna_box(q):
    rows = ''.join(f'<div class="row"><div class="sk">{ico(s)}<div><div class="nm">{s}</div><div class="tg">{M.SK[s]}</div></div></div>'
                   f'<div class="gd">{g}</div></div>' for s, g in q['dyna'])
    return (f'<div class="dyna"><div class="hd">{CHAT}Dyna Thinking Coach</div>{rows}'
            f'<div class="yt"><div class="pill">YOUR TURN</div><div class="tx">{q["turn"]}</div></div></div>')

def figs(q):
    if 'pre' in q:
        return f'<pre class="mono" style="margin:6pt 0 2pt 0;font-size:10.5pt;line-height:14pt;color:#1e436d">{q["pre"]}</pre>'
    if 'fig' not in q: return ''
    gap = q.get('fig_gap', 14)
    return f'<div class="fig" style="gap:{gap}pt">' + ''.join(img(n, w) for n, w in q['fig']) + '</div>'

def qblock(q):
    note = f'<div class="note"><b>Note:</b> {q["note"]}</div>' if q.get('note') else ''
    mx = q.get('math', '')
    return (f'<div class="q"><div class="num">{q["n"]}</div><div class="qt">{q["text"]}</div>{mx}{note}{figs(q)}{opts_row(q)}{dyna_box(q)}</div>')

def spot_block(s):
    return (f'<div class="spot"><div class="h">{BULB}The Thinking Spot</div><div class="qt">{s["text"]}</div>{figs(s)}'
            f'{opts_row(s)}{dyna_box(s)}</div>')

def supp_block(q):
    hint = ''.join(f'<div class="card">{ico(s)}<div><div class="nm">{s}</div><div class="qq">{M.SQ[s]}</div></div></div>' for s in q['hint'])
    return (f'<div class="q sup"><div class="num">{q["n"]}</div><div class="qid">Q-ID {q["qid"]}</div><div class="qt">{q["text"]}</div>'
            f'{figs(q)}{opts_row(q)}<div class="hint"><div class="lab">THINKING<br>HINT</div>{hint}</div></div>')

PLAYICO = '<svg width="11" height="11" viewBox="0 0 14.4 14.4"><circle cx="7.2" cy="7.2" r="7.2" fill="#007fa3"/><path d="M5.6 4.4V10L10.2 7.2Z" fill="#fff"/></svg>'
def qr(code, w, kind='Dyna QR'):
    if not code:
        return f'<div class="qrph" style="width:{w}pt;height:{w}pt">{PLAYICO}<span>{kind}<br>coming soon</span></div>'
    return f'<img src="assets/{code}.png" style="width:{w}pt;height:{w}pt;display:block">'

def kick_ls(kick, maxw):
    from fontTools.ttLib import TTFont
    f = TTFont('fonts/Poppins-Bold.ttf'); cm = f.getBestCmap(); hm = f['hmtx']
    w = sum(hm[cm.get(ord(c), cm[ord('?')])][0] for c in H.unescape(kick)) * 7.87 / 1000
    n = len(H.unescape(kick))
    return max(0.12, min(0.32, (maxw - w) / n / 7.87))

def band_q(kick, title, pill, pill_box, qr_code=None):
    ls = kick_ls(kick, pill_box[0] - 48.7 - 8)
    out = [f'<div class="band" style="height:58.5pt"><div class="kick" style="top:11.2pt;letter-spacing:{ls:.3f}em">{kick}</div>'
           f'<div class="ttl" style="top:15.7pt;font-size:20.24pt;line-height:30pt">{title}</div>'
           f'<div class="pill" style="left:{pill_box[0]+0.3}pt;top:17.2pt;width:{pill_box[1]}pt;height:25.5pt">{pill}</div>']
    if qr_code:
        out.append(f'<div class="qrsq" style="left:517.3pt;top:5.3pt;width:47.5pt;height:47.5pt">{qr(qr_code,41.5)}</div>')
    out.append('</div>')
    return ''.join(out)

def flowbox(top, inner, bottom=790):
    return f'<div class="flow" style="top:{top}pt;height:{bottom-top}pt;display:flex;flex-direction:column">{inner}</div>'

def space(qr_code=None, min_h=60):
    q = ''
    if qr_code:
        q = (f'<div class="qrcard" style="position:absolute;right:10pt;top:4pt;width:90pt;height:80pt;padding-top:5pt;border-color:#00cfb4">'
             f'{qr(qr_code,54)}<div class="cap" style="margin-top:3pt">Scan to get help from Dyna<br>Thinking Coach</div></div>'
             + PLAY.format(l=500 - 48.4 - 0 + 0, t=0, c='#00cfb4').replace('style="left:', 'style="display:none;left:'))
    return f'<div class="space" style="flex:1;min-height:{min_h}pt"><div class="lab">MY THINKING SPACE</div>{q}</div>'

pages = {}
p = int(os.environ.get('FIRST', CH['first_page']))
kick_title = H.escape(T.upper())

# ---------------- opener 1 ----------------
def opener1():
    o = [f'<div class="band" style="height:99pt"><div class="kick" style="top:12.6pt">CHAPTER {num}</div>'
         f'<div class="ttl" style="top:15.5pt;font-size:31.49pt;line-height:47pt">{H.escape(T)} <span style="font-size:15pt;color:#00cfb4;letter-spacing:.02em">· {CH.get("exercise","")}</span></div>'
         f'<div class="sub" style="top:64.3pt;width:340pt">{CH["count_line"]}</div>'
         f'<div class="qrcard" style="left:484.8pt;top:6pt;width:80pt;height:87pt;padding-top:7pt">{qr(CH["lecture_qr"],54,"Lecture video")}'
         f'<div class="cap" style="margin-top:4.2pt">Atul Sir\'s guided lecture<br>{CH.get("exercise","Chapter "+str(num))}</div></div>'
         + PLAY.format(l=476.6, t=-2.2, c='#007fa3') + '</div>']
    def sec(n, t, s, y):
        return f'<div class="sec" style="top:{y}pt"><div class="n">{n}</div><div class="t">{t}</div><div class="s">{s}</div></div>'
    o.append(sec(1, 'What you need to know', 'Tick each one you know.', 186))
    for i, k in enumerate(M.KNOW):
        x = 48.8 if i % 2 == 0 else 309.0; y = 211.9 if i < 2 else 250.1
        o.append(f'<div class="know" style="left:{x}pt;top:{y}pt"><span class="tick"></span>{k}</div>')
    total = len(M.Q) + (1 if M.SPOT else 0)
    o.append(sec(2, getattr(M, 'BARS_TITLE', 'CT skills this chapter tests'), getattr(M, 'BARS_SUB', f'Main STCA concept of each of the {total} questions'), 303))
    nb = len(M.BARS); pitch = 22.5 if nb > 5 else 24
    sep = 335.5 + pitch * nb + 3.5
    panel_bottom = sep + 6 + 13.5 * 2 + 3.7 + 8
    o.append(f'<div class="panel" style="left:48.8pt;top:328.9pt;width:515.2pt;height:{panel_bottom-328.9:.1f}pt"></div>')
    top_c = max(b[2] for b in M.BARS)
    for i, (nm, tg, c, col, qs) in enumerate(M.BARS):
        y = 335.5 + pitch * i
        L = 18.2 * c
        o.append(f'<div class="abs" style="left:59.7pt;top:{y}pt;font-size:8.99pt;font-weight:700;line-height:12.6pt;white-space:nowrap">{nm}</div>'
                 f'<div class="abs" style="left:59.7pt;top:{y+11.8}pt;font-size:7.03pt;color:#007fa3;line-height:9.9pt;white-space:nowrap">{tg}</div>'
                 f'<div class="bar" style="left:187.2pt;top:{y+6.5}pt;width:{L:.1f}pt;background:{col}"></div>'
                 f'<div class="abs" style="left:{187.2+L+5:.1f}pt;top:{y+4.1}pt;font-size:9.37pt;font-weight:700;line-height:13.2pt">{c}</div>'
                 f'<div class="abs" style="left:418.2pt;top:{y+6}pt;font-size:7.64pt;font-weight:700;color:#007fa3;line-height:10.7pt;white-space:nowrap">{qs}</div>')
        if c == top_c:
            o.append(f'<div class="abs" style="left:{187.2+L+15.5:.1f}pt;top:{y+5}pt;width:60pt;height:14.2pt;border-radius:8pt;background:#1e436d;color:#fff;'
                     f'font-size:6.14pt;font-weight:700;letter-spacing:.3em;display:flex;align-items:center;justify-content:center">STRONGEST</div>')
    o.append(f'<div class="abs" style="left:59.7pt;top:{sep}pt;width:493.5pt;height:.75pt;background:#cccccc"></div>')
    o.append(f'<div class="abs" style="left:59.7pt;top:{sep+6}pt;width:493.5pt;font-size:6.97pt;line-height:13.5pt">'
             f'<span style="font-weight:700;color:#007fa3;margin-right:9pt">Also uses:</span>' + ''.join(f'<span class="chip">{a}</span>' for a in M.ALSO) + '</div>')
    y3 = panel_bottom + 38.6
    o.append(sec(3, "Dyna's thinking skills, question by question", '', y3))
    # skill tiles sorted by use
    cnt = {}
    items = [q for q in M.Q] + ([dict(M.SPOT, n='Spot')] if M.SPOT else [])
    for q in items:
        for s, _ in q['dyna']: cnt[s] = cnt.get(s, 0) + 1
    order = sorted(cnt, key=lambda s: -cnt[s])
    for s in M.SK:
        if s not in cnt: order.append(s); cnt[s] = 0
    ty = y3 + 25.9
    X = [48.8, 123.1, 197.3, 271.5, 346.5, 420.8, 495.0]
    for i, s in enumerate(order):
        c = cnt[s]
        if i < 2: bg, fg, bd = '#007ea2', '#fff', '#007ea2'
        elif c >= 3: bg, fg, bd = '#d6f7f3', '#1e436d', '#d6f7f3'
        else: bg, fg, bd = '#fff', '#1e436d', '#cccccc'
        o.append(f'<div class="tile" style="left:{X[i]}pt;top:{ty:.1f}pt;background:{bg};border:.75pt solid {bd};color:{fg}">{ico(s)}'
                 f'<div class="nm">{s}</div><div class="ct">{c} Q{"s" if c != 1 else ""}</div><div class="tg">{M.SK[s]}</div></div>')
    cy = ty + 98.2
    for i, q in enumerate(items):
        x = X[i % 7]; y = cy + 51 * (i // 7)
        last = q['n'] == 'Spot'
        st = 'background:#d6f7f3;border-color:#00cfb4' if last else ''
        lab = 'Thinking Spot' if last else q.get('label', f'Q {q["n"]}')
        rows = ''.join(f'<div class="r" style="top:{17.2+12*j}pt">{ico(s, cls="ico")}{s}</div>' for j, (s, _) in enumerate(q['dyna']))
        o.append(f'<div class="cell" style="left:{x}pt;top:{y:.1f}pt;{st}"><div class="qn">{lab}</div>{rows}</div>')
    assert cy + 51 * ((len(items) - 1) // 7) + 45.8 < 792, 'opener page 1 overflows'
    if getattr(M, 'KINDS', None):
        yk = cy + 51 * ((len(items) - 1) // 7)   # second row, beside the last cell
        for i, (nm, d, path) in enumerate(M.KINDS):
            x0 = 123.1 + 148 * i
            axes = '<path d="M35 2V58M2 30H68" stroke="#cccccc" stroke-width="1.2"/>'
            o.append(f'<div class="abs" style="left:{x0}pt;top:{yk:.1f}pt;width:141pt;height:45.8pt;background:#d6f7f3;border-radius:6pt;box-sizing:border-box">'
                     f'<svg viewBox="0 0 70 60" style="position:absolute;left:4pt;top:4pt;width:44pt;height:37.8pt;background:#fff;border-radius:4pt">{axes}{path}</svg>'
                     f'<div style="position:absolute;left:53pt;top:3.5pt;right:5pt;font-size:8.2pt;font-weight:700;line-height:10pt">{nm}</div>'
                     f'<div style="position:absolute;left:53pt;top:14pt;right:5pt;font-size:6.3pt;line-height:8.1pt">{d}</div></div>')
    return '<div class="ch">' + ''.join(o) + '</div>'

# ---------------- opener 2 ----------------
def opener2():
    def sec(n, t, s, y):
        return f'<div class="sec" style="top:{y}pt"><div class="n">{n}</div><div class="t">{t}</div><div class="s">{s}</div></div>'
    o = [sec(4, 'My starting routine', 'The same 4 steps for every question', 84)]
    for i, (w, d) in enumerate(M.ROUTINE):
        o.append(f'<div class="routine" style="left:{48.4+130.5*i}pt"><div class="w">{w}</div><div class="d">{d}</div></div>')
    o.append(sec(5, 'Watch out!', M.WATCH_SUB, 207))
    rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in M.WATCH)
    o.append(f'<table class="watch" style="left:48.8pt;top:232.9pt;width:515.2pt"><colgroup><col style="width:56.2pt"><col style="width:242.3pt"><col></colgroup>'
             f'<thead><tr><th>Question</th><th>Watch for</th><th>Example</th></tr></thead><tbody>{rows}</tbody></table>')
    t = M.TRYONE
    hints = ''.join(f'<div style="display:flex;align-items:center;margin-top:{6 if i else 7}pt"><div style="width:112.5pt;height:19.5pt;background:#d6f7f3;border-radius:5pt;display:flex;align-items:center;gap:7.5pt;padding-left:3pt;box-sizing:border-box;flex:none">'
                    f'{ico(s, 15)}<span style="font-size:7.79pt;font-weight:700">Hint {i+1} · {s}</span></div><div style="margin-left:7.5pt;font-size:8.17pt;line-height:11.4pt">{h}</div></div>'
                    for i, (s, h) in enumerate(t['hints']))
    opts = ''.join(f'<div style="width:121.5pt;font-size:10.12pt;font-weight:700">{x}</div>' for x in t['opts'] if x)
    sec6y = 424.5
    o.append(sec(6, 'Try one first, with Dyna', '', sec6y))
    o.append(f'<div class="tryone" style="left:49.2pt;top:{sec6y+26.2}pt;width:514.5pt">'
             f'<div style="font-size:9.44pt;line-height:14.2pt">{t["q"]}</div>'
             f'' + (f'<div style="display:flex;margin-top:7pt">{opts}</div>' if opts else f'<div class="wline" style="margin-top:6pt"><span class="wl-l">{t.get("write", "Range")}</span><span class="dash"></span></div>') +
             f'<div style="margin-top:7pt;height:24pt;background:#d6f7f3;border-radius:5pt;display:flex;align-items:center;padding-left:9pt;font-size:8.09pt">'
             f'Before you open a hint, write your plan in one line:<span style="flex:1;border-bottom:.8pt dashed #1e436d;margin:0 9pt 0 5pt;height:7pt"></span></div>'
             f'{hints}'
             f'<div style="display:flex;align-items:center;margin-top:6pt"><div style="width:112.5pt;height:15pt;background:#00cfb4;border-radius:8pt;font-size:7.49pt;font-weight:700;letter-spacing:.12em;display:flex;align-items:center;justify-content:center;flex:none">YOUR TURN</div>'
             f'<div style="margin-left:7.5pt;font-size:8.17pt;line-height:11.4pt">{t["turn"]}</div></div>'
             f'<div style="border-top:.75pt solid #cccccc;margin-top:6pt;padding:5pt 0 7pt;font-size:7.72pt;color:#007fa3">Use the hints one at a time. Try on your own before you read the next one.</div></div>')
    o.append(f'<div class="mini" style="left:48.4pt;top:703.5pt;width:255pt"><div class="h">Before you start</div><div class="x">{M.BEFORE}</div></div>'
             f'<div class="mini" style="left:310.2pt;top:703.5pt;width:254.2pt"><div class="h">Challenge ahead</div><div class="x">{M.AHEAD}</div></div>')
    return '<div class="ch">' + ''.join(o) + '</div>'

# ---------------- question pages ----------------
SKILLS_BOX = None
def qpage(spec):
    items = spec[1]; first = len(spec) > 2 and spec[2]; tail = spec[3] if len(spec) > 3 else None
    o = []; top = 84
    if first:
        o.append(band_q(f'CHAPTER {num} · {kick_title} · {CH["exercise"].upper()} QUESTIONS', 'Think it through with Dyna', 'Try first, then ask Dyna', (374.7, 137.2), CH['dyna_qr']))
        tiles = ''.join(f'<div style="position:absolute;left:{7.9+72*i}pt;top:24.3pt;width:67.5pt;height:78pt;background:#d6f7f3;border-radius:6pt;text-align:center">'
                        f'<span class="ico" style="position:absolute;left:19.5pt;top:6pt;width:28.5pt;height:28.5pt"><img src="assets/icons/icon_{s.lower()}.png"></span>'
                        f'<div style="position:absolute;left:0;right:0;top:35.2pt;font-size:8.62pt;font-weight:700;line-height:12pt">{s}</div>'
                        f'<div style="position:absolute;left:2pt;right:2pt;top:47.3pt;font-size:6.44pt;line-height:7.9pt;color:#007fa3">{M.SK[s]}</div></div>'
                        for i, s in enumerate(['Bridge', 'Starter', 'Slicer', 'Echo', 'Vault', 'Roots', 'Translator']))
        o.append(f'<div class="panel" style="left:48.8pt;top:144.4pt;width:515.2pt;height:110.2pt">'
                 f'<div style="position:absolute;left:10.9pt;top:7.5pt;font-size:7.49pt;font-weight:700;color:#007fa3;letter-spacing:.3em">DYNA\'S 7 THINKING SKILLS</div>{tiles}</div>')
        steps = [('Try it', ' on your own first.'), ('Stuck?', " Read Dyna's two skills."), ('Your turn:', ' take the last step.'), ('Write', ' your answer in the box.')]
        for i, (a, b) in enumerate(steps):
            o.append(f'<div style="position:absolute;left:{48.4+130.5*i}pt;top:258pt;width:124.5pt;height:30.7pt;background:#1e436d;border-radius:6pt;display:flex;align-items:center">'
                     f'<div style="width:15pt;height:15pt;border-radius:50%;background:#00cfb4;margin:0 6.5pt 0 7.5pt;flex:none;font-size:8.24pt;font-weight:700;display:flex;align-items:center;justify-content:center">{i+1}</div>'
                     f'<div style="font-size:7.64pt;line-height:9.8pt;color:#fff;padding-right:6pt"><b style="color:#00cfb4">{a}</b>{b}</div></div>')
        top = 298.5
    inner = ''.join(spot_block(M.SPOT) if it == 'spot' else qblock(M.Q[it - 1]) for it in items)
    if tail == 'space': inner += space()
    if tail == 'spaceqr': inner += space(CH['dyna_qr'])
    o.append(flowbox(top, inner))
    return '<div class="ch">' + ''.join(o) + '</div>'

def suppage(spec):
    items = spec[1]; first = len(spec) > 2 and spec[2]; tail = spec[3] if len(spec) > 3 else None
    o = []; top = 84
    if first:
        o.append(band_q(f'CHAPTER {num} · {kick_title} · {CH["exercise"].upper()} SUPPLEMENTARY', 'More thinking practice', f'{len(M.SUPP)} questions · {2*len(M.SUPP)} minutes', (417.4, 147.0)))
        o.append(f'<div class="goonline"><div style="position:absolute;left:12.7pt;top:6.5pt;font-size:7.49pt;font-weight:700;color:#007fa3;letter-spacing:.3em">GO ONLINE WITH DYNA</div>'
                 f'<div style="position:absolute;left:12.7pt;top:17.5pt;font-size:11.99pt;font-weight:700;line-height:17pt">Stuck? Take guidance from Dyna Thinking Coach online.</div>'
                 f'<div style="position:absolute;left:13pt;top:37.5pt;width:340pt;font-size:7.6pt;line-height:10.4pt">Try the two thinking skills first. Still stuck? Scan the QR, find the question by its Q-ID, and Dyna will guide you one step at a time.</div>'
                 f'<div style="position:absolute;left:378pt;top:22.5pt;width:70pt;text-align:right;font-size:6.19pt;font-weight:700;line-height:7.5pt">Scan to get help from<br>Dyna Thinking Coach</div>'
                 f'<div class="qrsq" style="left:453pt;top:4pt;width:54pt;height:54pt;border-width:1.6pt;padding:3pt">{qr(CH["dyna_qr"],45)}</div></div>')
        top = 223.5
    inner = ''.join(supp_block(M.SUPP[i - 1]) for i in items)
    if tail == 'space': inner += space()
    if tail and tail.startswith('howdid'):
        inner += (f'<div class="howdid"><div class="h">How did I do?</div>'
                  f'<div class="l">Questions I tried <span class="dash" style="width:34pt"></span> /{len(M.SUPP)}</div>'
                  f'<div class="l">Questions I got right online <span class="dash" style="width:34pt"></span> /{len(M.SUPP)}</div>'
                  f'<div class="l">The thinking skill that helped me most <span class="dash" style="width:222pt"></span></div>'
                  f'<div class="qrcard" style="position:absolute;right:12pt;top:10pt;width:88pt;height:100pt;padding-top:9pt;border-color:#00cfb4">{qr(CH["dyna_qr"],66)}'
                  f'<div class="cap" style="margin-top:4pt">Scan to get help from Dyna<br>Thinking Coach</div></div></div>')
        if tail.endswith('+space'): inner += '<div style="height:14pt;flex:none"></div>' + space()
    o.append(flowbox(top, inner))
    return '<div class="ch">' + ''.join(o) + '</div>'

def notes():
    lines = ''.join(f'<div style="position:absolute;left:48.4pt;width:516pt;top:{140+26*i}pt;border-bottom:.75pt solid #cccccc"></div>' for i in range(25))
    return ('<div class="ch"><div class="abs" style="left:48.4pt;top:84pt;font-size:24pt;font-weight:700;line-height:34pt">Notes</div>'
            f'<div class="abs" style="left:48.4pt;top:118pt;font-size:8pt;color:#007fa3">Your own working, doubts to ask Dyna, and ideas from {CH["exercise"]}.</div>{lines}</div>')

for spec in M.PAGES:
    kind = spec[0]
    body = {'opener1': opener1, 'opener2': opener2, 'notes': notes}.get(kind)
    html = body() if body else (qpage(spec) if kind == 'questions' else suppage(spec))
    frame(p)
    open(f'overlays/p{p:02d}.html', 'w').write(f'<!-- Chapter {num} page (generated by _class/chapter_gen.py from {sys.argv[1]}) -->\n{html}\n<div class="ov">{footer_num(p)}<div class="hdr2">{CH["subject"]}</div></div>\n')
    print('page', p, kind)
    p += 1

