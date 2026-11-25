"""lxml helpers: find drawing elements by their bounding box (pt) and remove them."""
import re
from lxml import etree
NS = '{http://www.w3.org/2000/svg}'

def _mat(e):
    m = re.search(r'matrix\(([^)]*)\)', e.get('transform', ''))
    return [float(v) for v in re.split(r'[ ,]+', m.group(1).strip())] if m else [1, 0, 0, 1, 0, 0]

def bbox(e):
    """Rough bbox of a <path> (numbers in d, pairs as x,y) or <image>, in page pt, ignoring parent transforms."""
    a, b, c, d, ex, fy = _mat(e)
    if e.tag == NS + 'image':
        x, y, w, h = (float(e.get(k, 0)) for k in ('x', 'y', 'width', 'height'))
        return (a * x + ex, d * y + fy, a * (x + w) + ex, d * (y + h) + fy)
    xs, ys = [], []
    cx = cy = 0.0
    for cmd, args in re.findall(r'([MLCQHVZmlcqhvz])([^MLCQHVZmlcqhvz]*)', e.get('d', '')):
        v = [float(t) for t in re.findall(r'-?\d*\.?\d+(?:e-?\d+)?', args)]
        if cmd in 'MLCQ':
            for i in range(0, len(v) - 1, 2):
                cx, cy = v[i], v[i + 1]; xs.append(cx); ys.append(cy)
        elif cmd == 'H':
            for t in v: cx = t; xs.append(cx); ys.append(cy)
        elif cmd == 'V':
            for t in v: cy = t; xs.append(cx); ys.append(cy)
    if not xs:
        return None
    return (a * min(xs) + ex, d * min(ys) + fy, a * max(xs) + ex, d * max(ys) + fy)

def find(root, pred):
    return [e for e in root.iter(NS + 'path', NS + 'image') if (bb := bbox(e)) and pred(bb, e)]

def drop(e):
    e.getparent().remove(e)
