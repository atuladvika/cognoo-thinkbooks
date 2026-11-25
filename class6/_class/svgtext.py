"""Helpers to find, list and remove <text> elements in the page SVGs by position or content."""
import re, html

TEXT_RE = re.compile(r'<text\b[^>]*>.*?</text>', re.S)


def _matrix(tag):
    m = re.search(r'transform="matrix\(([^)]*)\)"', tag)
    if not m:
        return (1, 0, 0, 1, 0, 0)
    v = [float(x) for x in re.split(r'[ ,]+', m.group(1).strip())]
    return tuple(v)


def texts(svg):
    """Yield dicts: start, end, text, x, y (absolute pt, baseline of first tspan), size, el."""
    out = []
    for m in TEXT_RE.finditer(svg):
        el = m.group(0)
        a, b, c, d, e, f = _matrix(el)
        t = re.search(r'<tspan y="([-\d.e]+)" x="([-\d.e]+)', el)
        if not t:
            continue
        y0, x0 = float(t.group(1)), float(t.group(2))
        X = a * x0 + c * y0 + e
        Y = b * x0 + d * y0 + f
        fs = re.search(r'font-size="([\d.]+)"', el)
        size = float(fs.group(1)) * a if fs else 0
        out.append(dict(start=m.start(), end=m.end(), el=el, x=X, y=Y, size=size,
                        text=html.unescape(re.sub('<[^>]+>', '', el))))
    return out


def remove_where(svg, pred):
    """Remove every <text> element for which pred(info) is true. Returns (svg, removed list)."""
    items = [t for t in texts(svg) if pred(t)]
    for t in sorted(items, key=lambda t: -t['start']):
        svg = svg[:t['start']] + svg[t['end']:]
    return svg, items


def swap(svg, old, new, count=None):
    """Replace text content inside tspans (same glyph slots: use for equal-length swaps such as 3 -> 4)."""
    n = 0
    def rep(m):
        nonlocal n
        if count is not None and n >= count:
            return m.group(0)
        n += 1
        return m.group(0).replace(old, new)
    svg = re.sub(r'<tspan[^>]*>[^<]*' + re.escape(old) + r'[^<]*</tspan>', rep, svg)
    return svg, n
