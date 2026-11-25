"""Inline SVG versions of math symbols that Poppins lacks (drawn from DejaVu Sans outlines,
so no fallback font is embedded in the PDF)."""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

import os
F = TTFont(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'fonts', 'DejaVuSans.ttf'))
GS = F.getGlyphSet(); CM = F.getBestCmap(); UPM = F['head'].unitsPerEm
ASC = 0.80; DESC = 0.22


def sym(ch, scale=1.0):
    g = CM[ord(ch)]; p = SVGPathPen(GS); GS[g].draw(p); adv = GS[g].width
    w = adv / UPM; h = ASC + DESC
    return (f'<svg class="msym" viewBox="0 {-ASC*UPM:.0f} {adv} {h*UPM:.0f}" '
            f'style="width:{w*scale:.3f}em;height:{h*scale:.3f}em;vertical-align:{-DESC*scale:.3f}em;display:inline-block">'
            f'<path transform="scale(1,-1)" d="{p.getCommands()}" fill="currentColor"/></svg>')


MAP = sym('↦')   # maps to
TO = sym('→')    # arrow
IN = sym('∈', 0.95)  # element of
R = sym('ℝ', 0.98)   # real numbers
