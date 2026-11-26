"""Cambridge IGCSE & O Level Additional Mathematics, Exercise 1.1 (mappings): concept-led lecture.
Reuses the drawing helpers and renderer of ../q1/lecture_q1.py. Worked examples are outside the exercise;
exercise questions only get pointers, never answers."""
import os, sys, math, asyncio, json, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "q1"))
import lecture_q1 as lq
from lecture_q1 import *          # helpers, palette, fonts
MYDIR = os.path.dirname(os.path.abspath(__file__)); os.chdir(MYDIR)
lq.ATUL = ATUL; lq.END = END      # loaded from q1 at import

N = ("-4%", "+0Hz"); K = ("-10%", "-2Hz"); Q = ("-10%", "+3Hz"); Fq = ("+4%", "+1Hz"); Wm = ("+2%", "+3Hz"); T = ("-6%", "+1Hz")
GOLD = (255, 200, 60)
SC = [
 ("open", 1.5, [L("Hello, young thinkers!", Wm, 350), L("Atul Sir, your Thinking Mentor, has guided this lesson.", N, 550),
                L("Today, we learn to tell three kinds of mapping apart.", N, 1100)]),
 ("need", 0.4, [L("First, how to read a mapping.", N, 400), L("x is mapped to two x minus three.", N, 400),
                L("Put in three:", N, 200), L("two times three, minus three,", Fq, 200), L("gives three.", K, 700),
                L("The part after the rule is the domain.", N, 300), L("It tells you which inputs are allowed.", K, 1100)]),
 ("kinds", 0.4, [L("Concept one: three kinds of mapping.", N, 500),
                 L("One-one:", K, 200), L("each output comes from just one input.", N, 700),
                 L("Many-one:", K, 200), L("two inputs share an output.", N, 700),
                 L("One-many:", K, 200), L("one input gives two outputs.", N, 1100)]),
 ("pair", 0.4, [L("Concept two: test a pair of inputs.", N, 450), L("Take x is mapped to x squared minus four.", N, 450),
                L("Try two, and minus two.", N, 400), L("Two squared is four. Minus four gives zero.", Fq, 350),
                L("Minus two squared is also four. Zero again.", Fq, 600), L("Two different inputs, one output.", K, 400),
                L("So this mapping is many-one.", K, 1000), L("Tip: always try a pair with opposite signs.", T, 1200)]),
 ("lines", 0.4, [L("Concept three: the line tests.", N, 450), L("Here is x cubed minus three x.", N, 500),
                 L("Draw a horizontal line across it.", N, 350), L("It meets the curve three times.", N, 400),
                 L("Three inputs share one output:", N, 200), L("many-one.", K, 1000),
                 L("Now try two x minus three.", N, 500), L("Every horizontal line meets it just once.", N, 400),
                 L("So it is one-one.", K, 800),
                 L("A vertical line shows how many outputs one input has.", N, 1300)]),
 ("domain", 0.4, [L("Concept four: the domain can change the answer.", N, 500),
                  L("On all real numbers, x squared minus four is many-one.", N, 500),
                  L("Now allow only x greater than or equal to zero.", N, 400), L("The left half of the curve is gone.", N, 400),
                  L("Every horizontal line now meets it once.", N, 400), L("Same rule, but now it is one-one.", K, 900),
                  L("So always read the domain first.", T, 1200)]),
 ("many", 0.4, [L("Concept five: one input, two outputs.", N, 450), L("Map each number to its square roots.", N, 400),
                L("Four goes to two,", Fq, 150), L("and to minus two.", Fq, 450), L("Nine goes to three, and to minus three.", Fq, 500),
                L("One input, two outputs:", N, 200), L("that is one-many.", K, 900),
                L("Watch for a plus-or-minus sign in the rule.", T, 1200)]),
 ("watch", 0.4, [L("Now, the traps in this exercise.", N, 500),
                 L("In questions two and six, try inputs with opposite signs.", N, 700),
                 L("In question three, odd powers keep their sign.", N, 250), L("Test before you decide.", N, 700),
                 L("In questions five and seven, read the domain first.", N, 700),
                 L("In question eight, plus-or-minus means two signs.", N, 1200)]),
 ("turn", 0.4, [L("Your turn.", K, 400), L("Here is which idea helps with which question.", N, 900),
                L("Stuck? Die-na's hints are in your ThinkBook.", N, 500),
                L("Pause the video, and try all eight!", ("-2%", "+3Hz"), 3000)]),
 ("end", 0.0, []),
]

# ---------- generic graph ----------
class Axes:
    def __init__(s, ox, oy, sx, sy, xr, yr): s.ox, s.oy, s.sx, s.sy, s.xr, s.yr = ox, oy, sx, sy, xr, yr
    def P(s, x, y): return (s.ox + x * s.sx, s.oy - y * s.sy)
    def draw(s, fr, a):
        lay = layer(); d = ImageDraw.Draw(lay)
        for gx in range(math.ceil(s.xr[0]), math.floor(s.xr[1]) + 1): d.line((*s.P(gx, s.yr[0]), *s.P(gx, s.yr[1])), fill=(40, 80, 105, 255), width=1)
        for gy in range(math.ceil(s.yr[0]), math.floor(s.yr[1]) + 1): d.line((*s.P(s.xr[0], gy), *s.P(s.xr[1], gy)), fill=(40, 80, 105, 255), width=1)
        d.line((*s.P(s.xr[0] - .3, 0), *s.P(s.xr[1] + .3, 0)), fill=WHITE, width=3); d.line((*s.P(0, s.yr[0] - .2), *s.P(0, s.yr[1] + .3)), fill=WHITE, width=3)
        d.text(s.P(s.xr[1] + .4, 0), "x", font=F("Italic", 32), fill=WHITE, anchor="lm"); d.text(s.P(.15, s.yr[1] + .35), "y", font=F("Italic", 32), fill=WHITE, anchor="ls")
        comp(fr, lay, a)
    def curve(s, fr, f, x0, x1, u, col=TURQ, w=6, alpha=1.0, clip=None):
        if u <= 0: return
        n = 240; xe = x0 + (x1 - x0) * u; pts = []
        for i in range(n + 1):
            x = x0 + (xe - x0) * i / n; y = f(x)
            if s.yr[0] - .5 <= y <= s.yr[1] + .5: pts.append(s.P(x, y))
            elif pts: break
        if len(pts) > 1:
            lay = layer(); ImageDraw.Draw(lay).line(pts, fill=col + (255,), width=w, joint="curve"); comp(fr, lay, alpha)
    def hline(s, fr, y, a=1.0, col=GOLD):
        lay = layer(); d = ImageDraw.Draw(lay); X0, Y = s.P(s.xr[0], y); X1, _ = s.P(s.xr[1], y); x = X0
        while x < X1: d.line((x, Y, min(x + 24, X1), Y), fill=col + (255,), width=4); x += 40
        comp(fr, lay, a)
    def vline(s, fr, x, a=1.0, col=GOLD):
        lay = layer(); d = ImageDraw.Draw(lay); X, Y0 = s.P(x, s.yr[0]); _, Y1 = s.P(x, s.yr[1]); y = Y1
        while y < Y0: d.line((X, y, X, min(y + 24, Y0)), fill=col + (255,), width=4); y += 40
        comp(fr, lay, a)
    def dot(s, fr, x, y, a=1.0, col=GOLD, ring=True):
        if a <= 0: return
        lay = layer(); d = ImageDraw.Draw(lay); X, Y = s.P(x, y); r = 15
        if ring: d.ellipse((X - r, Y - r, X + r, Y + r), outline=col + (255,), width=6)
        else: d.ellipse((X - r, Y - r, X + r, Y + r), fill=col + (255,))
        comp(fr, lay, a)

def hdr(fr, t, kicker, runs): lay = layer(); d = ImageDraw.Draw(lay); header(d, kicker, runs); comp(fr, lay, appear(t, 0))
def B(s): return (s, F("Bold", 46), WHITE)
def BT(s): return (s, F("Bold", 46), TURQ)
def pill(fr, t0, t, box, text, fill=GOLD, col=(30, 40, 50), size=30):
    u = appear(t, t0)
    if u <= 0: return
    lay = layer(); d = ImageDraw.Draw(lay); rrect(d, box, fill=fill + (255,), r=(box[3] - box[1]) // 2)
    d.text(((box[0] + box[2]) / 2, (box[1] + box[3]) / 2), text, font=F("Bold", size), fill=col, anchor="mm"); comp(fr, lay, u)
def mtext(d, x, y, parts, size, col=WHITE):
    """parts like [('x','i'),(' ↦ ','s'),('2','n')] drawn on one baseline."""
    for p, k in parts:
        f = F("Italic", size) if k == "i" else DJ(int(size * .9)) if k == "s" else F("Medium", size) if k == "n" else F("Bold", size)
        dy = int(size * .10) if k == "s" else 0
        d.text((x, y + dy), p, font=f, fill=col); x += f.getlength(p)
    return x
def rule_card(fr, t, t0, box, parts, size=64, sub=None):
    u = appear(t, t0)
    if u <= 0: return
    lay = layer(); d = ImageDraw.Draw(lay); rrect(d, box, fill=CARD + (240,), outline=TURQ + (255,), w=3)
    mtext(d, box[0] + 40, box[1] + 22, parts, size)
    if sub: d.text((box[0] + 40, box[3] - 50), sub, font=F("Medium", 26), fill=DIM)
    comp(fr, lay, u)
SQ2 = "²"; SQ3 = "³"; MINUS = "−"

# ---------- scenes ----------
def sc_need(fr, t, D, c):
    hdr(fr, t, "WHAT YOU NEED", [B("How to read a "), BT("mapping")])
    rule_card(fr, t, c[1][0] - .1, (110, 260, 900, 400), [("x", "i"), ("  ↦  ", "s"), ("2", "n"), ("x", "i"), (f" {MINUS} 3", "n")])
    u = appear(t, c[1][0] + .3)
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay); d.text((150, 420), "“x is mapped to 2x − 3”", font=F("Medium", 30), fill=TURQ); comp(fr, lay, u)
    # input 3 -> output 3 with arrow
    u = appear(t, c[2][0])
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay)
        for cx, lab in ((1150, "input"), (1650, "output")):
            d.ellipse((cx - 90, 260, cx + 90, 440), outline=TEAL, width=4, fill=CARD + (230,)); d.text((cx, 460), lab, font=F("Medium", 24), fill=DIM, anchor="mt")
        d.text((1150, 350), "3", font=F("Bold", 64), fill=WHITE, anchor="mm"); comp(fr, lay, u)
        v = ease((t - c[3][0]) / 1.0)
        lay = layer(); d = ImageDraw.Draw(lay); arrow(d, (1200, 350), (1590, 350), v, GOLD + (255,))
        if v > 0: d.text((1395, 300), f"2 × 3 {MINUS} 3", font=F("Medium", 30), fill=GOLD, anchor="mm")
        if t > c[4][0]: d.text((1650, 350), "3", font=F("Bold", 64), fill=TURQ, anchor="mm")
        comp(fr, lay, 1)
    # domain chips
    for k, (sym, txt) in enumerate([([("x", "i"), (" ∈ ", "s"), ("ℝ", "s")], "every real number"),
                                    ([("x", "i"), (" > 0", "n")], "positive numbers only")]):
        u = appear(t, c[5][0] + .2 + k * .7)
        if u <= 0: continue
        lay = layer(); d = ImageDraw.Draw(lay); y = 600 + k * 150
        rrect(d, (110, y, 1000, y + 120), fill=(245, 252, 253, 255), r=24)
        x = mtext(d, 150, y + 22, sym, 56, NAVY); d.text((x + 40, y + 60), txt, font=F("Medium", 34), fill=OCEAN, anchor="lm")
        comp(fr, lay, u)
    u = appear(t, c[6][0])
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay); d.text((1100, 690), "The domain = the inputs", font=F("Bold", 40), fill=WHITE)
        d.text((1100, 745), "that are allowed.", font=F("Bold", 40), fill=TURQ); comp(fr, lay, u)

def sc_kinds(fr, t, D, c):
    hdr(fr, t, "CONCEPT 1", [B("Three kinds of "), BT("mapping")])
    lq.kind_panel(fr, t, c[1][0], 110, "One-one", "each output has one input", [0, 1, 2], [0, 1, 2], [(0, 0), (1, 1), (2, 2)])
    lq.kind_panel(fr, t, c[3][0], 700, "Many-one", "two inputs share an output", [0, 1, 2], [0, 1], [(0, 0), (1, 0), (2, 1)])
    lq.kind_panel(fr, t, c[5][0], 1290, "One-many", "one input, two outputs", [0, 1], [0, 1, 2], [(0, 0), (0, 1), (1, 2)])

def sc_pair(fr, t, D, c):
    hdr(fr, t, "CONCEPT 2", [B("Test a "), BT("pair of inputs")])
    rule_card(fr, t, c[1][0] - .1, (110, 250, 820, 380), [("x", "i"), ("  ↦  ", "s"), ("x", "i"), (SQ2, "n"), (f" {MINUS} 4", "n")], 60,
              None)
    lay = layer(); d = ImageDraw.Draw(lay)
    tx, ty = 110, 430
    rrect(d, (tx, ty, tx + 560, ty + 90), fill=TURQ + (255,), r=16)
    d.text((tx + 120, ty + 45), "x", font=F("BoldItalic", 42), fill=(6, 30, 48), anchor="mm")
    draw_runs(d, tx + 280, ty + 16, [("x", F("BoldItalic", 42), (6, 30, 48)), (f"{SQ2} {MINUS} 4", F("Bold", 42), (6, 30, 48))])
    comp(fr, lay, appear(t, c[2][0] - .1))
    rows = [("2", f"4 {MINUS} 4 = 0"), (f"{MINUS}2", f"4 {MINUS} 4 = 0")]
    ci, co, cy = 1250, 1650, 520
    lay = layer(); d = ImageDraw.Draw(lay)
    for cx, lab in ((ci, "inputs"), (co, "outputs")):
        d.ellipse((cx - 90, cy - 200, cx + 90, cy + 200), outline=TEAL, width=4, fill=CARD + (230,)); d.text((cx, cy + 220), lab, font=F("Medium", 24), fill=DIM, anchor="mt")
    comp(fr, lay, appear(t, c[2][0]))
    for k, (xi_, yo) in enumerate(rows):
        t0 = c[3 + k][0]; u = appear(t, t0 - .1, .35)
        if u <= 0: continue
        lay = layer(); d = ImageDraw.Draw(lay); ry = ty + 105 + k * 100
        d.rounded_rectangle((tx, ry, tx + 560, ry + 88), 14, fill=CARD + (240,), outline=TEAL, width=2)
        d.text((tx + 120, ry + 44), xi_, font=F("Medium", 42), fill=WHITE, anchor="mm")
        d.text((tx + 400, ry + 44), yo, font=F("Bold", 40), fill=TURQ, anchor="mm")
        py = cy - 90 + k * 180; d.text((ci, py), xi_, font=F("Bold", 44), fill=WHITE, anchor="mm")
        comp(fr, lay, u)
        v = ease((t - t0 - .4) / .7)
        if v > 0:
            lay = layer(); d = ImageDraw.Draw(lay); arrow(d, (ci + 45, py), (co - 40, cy + (py - cy) * .1), v, GOLD + (255,))
            d.text((co, cy), "0", font=F("Bold", 52), fill=TURQ, anchor="mm"); comp(fr, lay, 1)
    u = appear(t, c[5][0])
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay); pul = .5 + .5 * math.sin((t - c[5][0]) * 5)
        d.ellipse((co - 50, cy - 50, co + 50, cy + 50), outline=GOLD + (int(150 + 105 * pul),), width=6); comp(fr, lay, u)
    pill(fr, c[6][0], t, (110, 760, 770, 840), "Two inputs, one output: many-one", TURQ, (6, 30, 48))
    u = appear(t, c[7][0])
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay); rrect(d, (110, 880, 1810, 970), fill=CARD + (240,), outline=GOLD + (255,), w=3)
        d.text((150, 925), "TIP", font=F("Bold", 30), fill=GOLD, anchor="lm")
        d.text((240, 925), "Always try a pair with opposite signs, such as 2 and −2.", font=F("Medium", 34), fill=WHITE, anchor="lm"); comp(fr, lay, u)

def sc_lines(fr, t, D, c):
    hdr(fr, t, "CONCEPT 3", [B("The "), BT("line tests")])
    A = Axes(700, 600, 110, 85, (-3, 3), (-4, 4)); A.draw(fr, appear(t, .1, .6))
    cub = lambda x: x ** 3 - 3 * x; lin = lambda x: 2 * x - 3
    phase2 = c[6][0]
    fade1 = 1 - appear(t, phase2 - .2, .5)
    # cubic
    A.curve(fr, cub, -2.25, 2.25, ease((t - c[1][0]) / 1.4), alpha=fade1)
    lab = layer(); d = ImageDraw.Draw(lab)
    mtext(d, 1250, 260, [("y", "i"), (" = ", "n"), ("x", "i"), (SQ3, "n"), (f" {MINUS} 3", "n"), ("x", "i")], 54); comp(fr, lab, appear(t, c[1][0]) * fade1)
    if t < phase2:
        u = appear(t, c[2][0], .4); A.hline(fr, 1.0, u)
        if t > c[3][0]:
            for k, xr in enumerate((-1.532, -0.347, 1.879)): A.dot(fr, xr, 1.0, appear(t, c[3][0] + .35 * k, .3))
        pill(fr, c[5][0] - .1, t, (1250, 380, 1780, 450), "3 crossings: many-one", TURQ, (6, 30, 48))
    # line 2x - 3
    if t >= phase2 - .2:
        A.curve(fr, lin, -.5, 3.5, ease((t - phase2) / 1.0))
        lab = layer(); d = ImageDraw.Draw(lab); mtext(d, 1250, 260, [("y", "i"), (" = 2", "n"), ("x", "i"), (f" {MINUS} 3", "n")], 54)
        comp(fr, lab, appear(t, phase2))
        if c[7][0] <= t < c[9][0]:
            tt = t - c[7][0]; yv = .5 + 3.2 * math.sin(tt * 1.0)
            A.hline(fr, yv, appear(t, c[7][0])); xv = (yv + 3) / 2
            if -0.5 <= xv <= 3.5: A.dot(fr, xv, yv, 1)
        pill(fr, c[8][0] - .1, t, (1250, 380, 1780, 450), "1 crossing each time: one-one", TURQ, (6, 30, 48), 28)
        if t >= c[9][0]:
            tt = t - c[9][0]; xv = 1.5 + 1.6 * math.sin(tt * 1.0)
            A.vline(fr, xv, appear(t, c[9][0])); A.dot(fr, xv, lin(xv), 1)
            u = appear(t, c[9][0] + .3)
            lay = layer(); d = ImageDraw.Draw(lay); rrect(d, (1250, 500, 1800, 640), fill=CARD + (240,), outline=GOLD + (255,), w=3)
            d.text((1280, 525), "Vertical line:", font=F("Bold", 32), fill=GOLD); d.text((1280, 575), "how many outputs for one input?", font=F("Medium", 28), fill=WHITE)
            comp(fr, lay, u)

def sc_domain(fr, t, D, c):
    hdr(fr, t, "CONCEPT 4", [B("The domain can "), BT("change the answer")])
    A = Axes(700, 650, 115, 66, (-3, 3), (-5, 5)); A.draw(fr, appear(t, .1, .6))
    par = lambda x: x * x - 4
    left_a = 1 - .85 * appear(t, c[2][0] + .3, .8)
    A.curve(fr, par, -2.9, 0, ease((t - c[1][0]) / 1.0), alpha=left_a)
    A.curve(fr, par, 0, 2.9, ease((t - c[1][0] - .5) / 1.0))
    lay = layer(); d = ImageDraw.Draw(lay); mtext(d, 1250, 250, [("y", "i"), (" = ", "n"), ("x", "i"), (SQ2, "n"), (f" {MINUS} 4", "n")], 54); comp(fr, lay, appear(t, c[1][0]))
    if c[1][0] + .8 <= t < c[4][0]:
        A.hline(fr, 0, appear(t, c[1][0] + .8)); A.dot(fr, -2, 0, appear(t, c[1][0] + 1.2) * (1 - appear(t, c[2][0] + .3))); A.dot(fr, 2, 0, appear(t, c[1][0] + 1.2))
    # domain chip
    u = appear(t, c[2][0])
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay); rrect(d, (1250, 360, 1700, 450), fill=(245, 252, 253, 255), r=20)
        mtext(d, 1290, 368, [("x", "i"), (" ≥ 0", "s")], 54, NAVY); d.text((1450, 405), "only", font=F("Medium", 32), fill=OCEAN, anchor="lm"); comp(fr, lay, u)
    if t >= c[4][0]:
        tt = t - c[4][0]; yv = 1 + 3.5 * math.sin(tt * 1.0); yv = max(-3.9, yv)
        A.hline(fr, yv, appear(t, c[4][0])); xv = math.sqrt(yv + 4) if yv > -4 else 0; A.dot(fr, xv, yv, 1)
    pill(fr, c[5][0] - .1, t, (1250, 500, 1800, 570), "Same rule, now one-one", TURQ, (6, 30, 48))
    u = appear(t, c[6][0])
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay); rrect(d, (1250, 610, 1800, 700), fill=CARD + (240,), outline=GOLD + (255,), w=3)
        d.text((1290, 655), "TIP  Read the domain first.", font=F("Bold", 32), fill=GOLD, anchor="lm"); comp(fr, lay, u)

def sc_many(fr, t, D, c):
    hdr(fr, t, "CONCEPT 5", [B("One input, "), BT("two outputs")])
    rule_card(fr, t, c[1][0] - .1, (110, 250, 1000, 380), [("x", "i"), ("  ↦  ", "s"), ("the square roots of ", "n"), ("x", "i")], 52)
    lay = layer(); d = ImageDraw.Draw(lay); d.text((150, 400), "domain: x > 0", font=F("Medium", 30), fill=DIM); comp(fr, lay, appear(t, c[1][0] + .3))
    ci, co, cy = 400, 900, 700
    lay = layer(); d = ImageDraw.Draw(lay)
    for cx, lab in ((ci, "inputs"), (co, "outputs")):
        d.ellipse((cx - 100, cy - 220, cx + 100, cy + 220), outline=TEAL, width=4, fill=CARD + (230,)); d.text((cx, cy + 240), lab, font=F("Medium", 24), fill=DIM, anchor="mt")
    comp(fr, lay, appear(t, c[2][0] - .3))
    def fan(t0, src, y, outs):
        u = appear(t, t0 - .1)
        if u <= 0: return
        lay = layer(); d = ImageDraw.Draw(lay); d.text((ci, y), src, font=F("Bold", 48), fill=WHITE, anchor="mm"); comp(fr, lay, u)
        for k, (o, oy) in enumerate(outs):
            v = ease((t - t0 - .1 - .6 * k) / .6)
            if v <= 0: continue
            lay = layer(); d = ImageDraw.Draw(lay); arrow(d, (ci + 45, y), (co - 45, oy), v, GOLD + (255,))
            if v > .95: d.text((co, oy), o, font=F("Bold", 44), fill=TURQ, anchor="mm")
            comp(fr, lay, 1)
    fan(c[2][0], "4", cy - 100, [("2", cy - 160), (f"{MINUS}2", cy - 50)])
    fan(c[4][0], "9", cy + 110, [("3", cy + 60), (f"{MINUS}3", cy + 170)])
    pill(fr, c[6][0] - .1, t, (1150, 560, 1780, 640), "One input, two outputs: one-many", TURQ, (6, 30, 48), 28)
    u = appear(t, c[7][0])
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay); rrect(d, (1150, 680, 1780, 780), fill=CARD + (240,), outline=GOLD + (255,), w=3)
        d.text((1190, 730), "TIP  Watch for ± in the rule.", font=F("Bold", 34), fill=GOLD, anchor="lm"); comp(fr, lay, u)

TRAPS = [("Q 2 and Q 6", "Try inputs with opposite signs."), ("Q 3", "Odd powers keep their sign. Test before you decide."),
         ("Q 5 and Q 7", "Read the domain first."), ("Q 8", "± means two signs: + and −.")]
def sc_watch(fr, t, D, c):
    hdr(fr, t, "WATCH-OUTS", [B("Traps in "), BT("this exercise")])
    starts = [c[1][0], c[2][0], c[4][0], c[5][0]]
    for k, (q, txt) in enumerate(TRAPS):
        u = appear(t, starts[k] - .1)
        if u <= 0: continue
        lay = layer(); d = ImageDraw.Draw(lay); x = 110 + (k % 2) * 860; y = 270 + (k // 2) * 330
        rrect(d, (x, y, x + 820, y + 290), fill=CARD + (240,), outline=GOLD + (255,), w=3)
        d.rounded_rectangle((x + 30, y + 30, x + 60 + F("Bold", 30).getlength(q), y + 80), 25, fill=GOLD)
        d.text((x + 45, y + 55), q, font=F("Bold", 30), fill=(30, 40, 50), anchor="lm")
        words = txt.split(); line = ""; yy = y + 120
        for w_ in words:
            if F("Medium", 38).getlength(line + w_) > 740: d.text((x + 30, yy), line, font=F("Medium", 38), fill=WHITE); yy += 54; line = ""
            line += w_ + " "
        d.text((x + 30, yy), line, font=F("Medium", 38), fill=WHITE)
        comp(fr, lay, u)

MAPROWS = [("Test a pair of inputs", "Q 1, 2, 3"), ("Line tests", "Q 3, 4"), ("Read the domain first", "Q 5, 6, 7"), ("Two outputs (±)", "Q 8")]
def sc_turn(fr, t, D, c):
    lay = layer(); d = ImageDraw.Draw(lay)
    d.rounded_rectangle((110, 90, 330, 140), 25, fill=TEAL); d.text((220, 115), "YOUR TURN", font=F("Bold", 26), fill=(6, 30, 48), anchor="mm")
    d.text((110, 170), "Which idea helps with which question", font=F("Bold", 50), fill=WHITE); comp(fr, lay, appear(t, 0))
    for k, (idea, qs) in enumerate(MAPROWS):
        u = appear(t, c[1][0] + .4 * k)
        if u <= 0: continue
        lay = layer(); d = ImageDraw.Draw(lay); y = 290 + k * 120
        rrect(d, (110, y, 1100, y + 100), fill=CARD + (240,), outline=TEAL + (255,), w=2, r=18); d.text((150, y + 50), idea, font=F("Medium", 38), fill=WHITE, anchor="lm")
        rrect(d, (1140, y, 1500, y + 100), fill=MINT + (255,), r=18); d.text((1320, y + 50), qs, font=F("Bold", 40), fill=NAVY, anchor="mm")
        comp(fr, lay, u)
    u = appear(t, c[2][0])
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay); lay.alpha_composite(DYNA.resize((200, 200)), (1580, 300))
        d.ellipse((1576, 296, 1784, 504), outline=TURQ + (255,), width=5)
        d.text((1680, 530), "Dyna's hints", font=F("Bold", 30), fill=WHITE, anchor="mt"); d.text((1680, 572), "are in your ThinkBook", font=F("Regular", 24), fill=TEAL, anchor="mt")
        comp(fr, lay, u)
    u = appear(t, c[3][0] - .1)
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay); rrect(d, (110, 820, 700, 900), fill=GOLD + (255,), r=40)
        d.rectangle((160, 843, 169, 877), fill=(30, 40, 50)); d.rectangle((178, 843, 187, 877), fill=(30, 40, 50))
        d.text((430, 860), "Pause the video and try!", font=F("Bold", 32), fill=(30, 40, 50), anchor="mm"); comp(fr, lay, u)

lq.SCENES = SC
lq.DRAW = dict(open=lq.sc_open, need=sc_need, kinds=sc_kinds, pair=sc_pair, lines=sc_lines, domain=sc_domain, many=sc_many,
               watch=sc_watch, turn=sc_turn, end=lq.sc_end)
lq.sc_open.__globals__["SCENES"] = SC

if __name__ == "__main__":
    timeline, total = asyncio.run(lq.narration())
    json.dump(timeline, open("timeline.json", "w"), indent=1)
    print("total", round(total, 1), [(n, round(s, 1), round(d, 1)) for n, s, d, _ in timeline], flush=True)
    if len(sys.argv) > 1 and sys.argv[1] == "stills":
        for name, st, D, cues in timeline:
            for frac in (0.55, 0.97):
                fr = BG.copy(); lq.DRAW[name](fr, D * frac, D, cues); fr.convert("RGB").save(f"still_{name}_{int(frac*100)}.png")
        sys.exit()
    lq.render(timeline, total)
    lq.sh("python3", "/home/claude/lec/music.py", "voice.wav", "mix.wav")
    lq.sh("ffmpeg", "-y", "-i", "video.mp4", "-i", "mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
          "-shortest", "IGCSE_AddMath_Ex1.1_lecture_v1.mp4")
    print("done", flush=True)
