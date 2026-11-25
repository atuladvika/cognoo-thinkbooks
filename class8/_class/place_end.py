"""Put the end matter after the last chapter page: a Notes page if the paper-page count would be odd,
then the inside back cover and back cover. Usage: python3 _class/place_end.py <last chapter page>
Expects the end pages as pages/end_notes.svg, pages/end_ibc.svg, pages/end_back.svg (+ overlays/end_*.html)."""
import os, sys, glob, re, shutil
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(HERE)
last = int(sys.argv[1])
# remove anything numbered after the chapter pages
for f in glob.glob('pages/p*.svg') + glob.glob('overlays/p*.html'):
    n = int(re.search(r'/p(\d+)', f).group(1))
    if n > last: os.remove(f)
paper = last - 2
seq = (['notes'] if paper % 2 else []) + ['ibc', 'back']
p = last
for kind in seq:
    p += 1
    shutil.copy(f'pages/end_{kind}.svg', f'pages/p{p:02d}.svg')
    for o in sorted(glob.glob(f'overlays/end_{kind}*.html')):
        suffix = o.split(f'end_{kind}')[1]
        shutil.copy(o, f'overlays/p{p:02d}{suffix}')
    if kind == 'notes':   # page number in the footer pill
        s = open(f'pages/p{p:02d}.svg').read()
        s = s.replace('>20</tspan>', f'>{p}</tspan>') if p != 20 else s
        open(f'pages/p{p:02d}.svg', 'w').write(s)
print('end matter:', ', '.join(seq), '-> last page', p)
