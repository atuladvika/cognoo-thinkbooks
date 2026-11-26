"""Cambridge IGCSE & O Level Additional Mathematics, Exercise 1.1 Q1 (x -> x + 1, x in R): test lecture.
Built per the cognoo-lecture-video skill: phrase-by-phrase Prabhat narration, figures animated in step with
each line, Cognoo music bed ducked under the voice. Never states the answer.
Run: python3 lecture_q1.py  (needs ../src.mp4 frames already cut: atul.png, dyna.png, endcard.png in this folder)
"""
import asyncio, os, ssl, subprocess, wave, math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import edge_tts, edge_tts.communicate as _c
_c._SSL_CTX = ssl.create_default_context(cafile=os.path.expanduser("~/.ccr/ca-bundle.crt"))

HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
FONTS = "/home/claude/jeebook/fonts/"
W, H, FPS = 1920, 1080, 30
V = "en-IN-PrabhatNeural"

# palette
TURQ = (0, 207, 180); TEAL = (6, 204, 171); OCEAN = (0, 127, 163); NAVY = (30, 67, 109)
MINT = (214, 247, 243); WHITE = (226, 246, 251); CARD = (11, 47, 70); DIM = (120, 160, 180)

def F(w, s): return ImageFont.truetype(FONTS + f"Poppins-{w}.ttf", s)
def DJ(s): return ImageFont.truetype(FONTS + "DejaVuSans.ttf", s)

# ---------------- narration ----------------
K = ("-10%", "-2Hz"); Q = ("-10%", "+3Hz"); N = ("-4%", "+0Hz"); Fq = ("+4%", "+1Hz"); Wm = ("+2%", "+3Hz")
def L(t, s, ms): return (t, s[0], s[1], ms)
SCENES = [
 ("open", 1.5, [L("Hello, young thinkers!", Wm, 350),
                L("Atul Sir, your Thinking Mentor, has guided this lesson.", N, 550),
                L("Today: one-one, many-one, and one-many mappings.", N, 1100)]),
 ("question", 0.5, [L("Question one.", K, 450), L("Is this mapping one-one, many-one, or one-many?", Q, 1300),
                    L("Read the rule:", N, 250), L("x is mapped to x plus one.", N, 700),
                    L("Now read the domain:", N, 250), L("every real number is allowed.", K, 1100)]),
 ("kinds", 0.4, [L("There are three kinds of mapping.", N, 500),
                 L("One-one:", K, 200), L("each output comes from just one input.", N, 700),
                 L("Many-one:", K, 200), L("two inputs share an output.", N, 700),
                 L("One-many:", K, 200), L("one input gives two outputs.", N, 1100)]),
 ("table", 0.5, [L("Die-na's first hint:", N, 200), L("turn it into a table.", K, 600),
                 L("Minus one goes to zero.", Fq, 350), L("Zero goes to one.", Fq, 350),
                 L("One goes to two.", Fq, 350), L("Two goes to three.", Fq, 700),
                 L("Do any two outputs match?", Q, 1700)]),
 ("graph", 0.4, [L("Now picture it.", N, 450), L("Plot the points.", N, 1100), L("Join them.", N, 1000),
                 L("Slide a horizontal line along the graph.", N, 400),
                 L("Watch how many times it meets the graph.", Q, 2600)]),
 ("vault", 0.5, [L("Die-na's second hint:", N, 200), L("pick what you already know.", K, 600),
                 L("Suppose two inputs, a and b,", N, 200), L("give the same output.", N, 500),
                 L("Then a plus one equals b plus one.", N, 600),
                 L("What does that tell you about a and b?", Q, 1700)]),
 ("turn", 0.4, [L("Your turn.", K, 400), L("Can two different inputs share an output here?", Q, 1300),
                L("Pause the video, and choose your word!", ("-2%", "+3Hz"), 3000)]),
 ("end", 0.0, []),
]
END_LEN = 3.0
FADE = 0.35

def sh(*a): subprocess.run(a, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
async def say(text, out, rate, pitch):
    if os.path.exists(out) and os.path.getsize(out) > 1000: return
    for _ in range(25):
        try: return await edge_tts.Communicate(text, V, rate=rate, pitch=pitch).save(out)
        except Exception: await asyncio.sleep(3)
    raise RuntimeError(text)
TRIM = ("silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-62dB,"
        "areverse,afade=t=in:d=0.015,areverse,afade=t=in:d=0.02,areverse")
def wlen(p):
    with wave.open(p) as w: return w.getnframes() / w.getframerate()

async def narration():
    os.makedirs("clips", exist_ok=True)
    timeline, pieces, t = [], [], 0.0
    for si, (name, lead, lines) in enumerate(SCENES):
        start = t; cues = []
        pieces.append(("sil", lead)); t += lead
        for li, (txt, r, p, ms) in enumerate(lines):
            k = f"clips/{si:02d}_{li:02d}"
            await say(txt, k + ".mp3", r, p)
            if not os.path.exists(k + ".wav"):
                sh("ffmpeg", "-y", "-i", k + ".mp3", "-af", TRIM, "-ar", "48000", "-ac", "1", k + ".wav")
            d = wlen(k + ".wav"); cues.append((t - start, d))
            pieces += [("wav", k + ".wav"), ("sil", ms / 1000)]; t += d + ms / 1000
        if name == "end": pieces.append(("sil", END_LEN)); t += END_LEN
        timeline.append((name, start, t - start, cues))
    # write the voice track directly with numpy
    out = []
    for k, x in pieces:
        if k == "sil": out.append(np.zeros(int(round(x * 48000)), np.int16))
        else:
            with wave.open(x) as w: out.append(np.frombuffer(w.readframes(w.getnframes()), np.int16))
    with wave.open("voice_raw.wav", "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(48000); w.writeframes(np.concatenate(out).tobytes())
    sh("ffmpeg", "-y", "-i", "voice_raw.wav", "-af", "loudnorm=I=-16:TP=-1.5", "-ar", "48000", "voice.wav")
    return timeline, t

# ---------------- drawing helpers ----------------
random.seed(7)
def make_bg():
    y, x = np.mgrid[0:H, 0:W]
    top = np.array([5, 18, 32.]); bot = np.array([7, 33, 50.])
    g = top + (bot - top) * (y / H)[..., None]
    for cx, cy, r, a in [(1500, 300, 520, 10), (380, 820, 460, 8), (1000, 560, 700, 5)]:
        d = np.sqrt((x - cx) ** 2 + (y - cy) ** 2); g += (np.clip(1 - d / r, 0, 1) ** 2)[..., None] * np.array([0, a, a * 0.9])
    im = Image.fromarray(np.clip(g, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im)
    for _ in range(420):
        sx, sy = random.randrange(W), random.randrange(H); b = random.randint(70, 190); r = random.choice([1, 1, 1, 2])
        d.ellipse((sx - r / 2, sy - r / 2, sx + r / 2, sy + r / 2), fill=(b, b + 20, min(255, b + 40)))
    return im.convert("RGBA")
BG = make_bg()

def ease(u): u = max(0., min(1., u)); return u * u * (3 - 2 * u)
def appear(t, t0, d=0.45): return ease((t - t0) / d)

def runs_width(runs):
    return sum(f.getlength(s) for s, f, c in runs)
def draw_runs(dr, x, y, runs, alpha=1.0, base=None):
    """runs: (text, font, colour). y is the top of the Poppins line box; DejaVu glyphs nudged to share a baseline."""
    for s, f, c in runs:
        col = tuple(int(v) for v in c) + (int(255 * alpha),)
        dy = 0
        if "DejaVu" in f.path: dy = int(f.size * 0.12)
        dr.text((x, y + dy), s, font=f, fill=col); x += f.getlength(s)
    return x

def layer(): return Image.new("RGBA", (W, H), (0, 0, 0, 0))
def comp(base, lay, a):
    if a <= 0: return
    if a < 1:
        arr = np.array(lay); arr[..., 3] = (arr[..., 3] * a).astype(np.uint8); lay = Image.fromarray(arr)
    base.alpha_composite(lay)

def rrect(dr, box, fill=None, outline=None, w=3, r=22): dr.rounded_rectangle(box, r, fill=fill, outline=outline, width=w)

def header(dr, kicker, title_runs, a=1.0):
    k = F("Bold", 24); x = 110
    for ch in kicker:
        dr.text((x, 70), ch, font=k, fill=TURQ + (int(255 * a),)); x += k.getlength(ch) + 3.5
    draw_runs(dr, 110, 104, title_runs, a)

def arrow(dr, p0, p1, u, col, w=5):
    if u <= 0: return
    x0, y0 = p0; x1, y1 = p1; xe, ye = x0 + (x1 - x0) * u, y0 + (y1 - y0) * u
    dr.line((x0, y0, xe, ye), fill=col, width=w)
    if u > 0.25:
        ang = math.atan2(ye - y0, xe - x0); s = 18
        pts = [(xe, ye), (xe - s * math.cos(ang - 0.45), ye - s * math.sin(ang - 0.45)),
               (xe - s * math.cos(ang + 0.45), ye - s * math.sin(ang + 0.45))]
        dr.polygon(pts, fill=col)

ATUL = Image.open("atul.png").convert("RGBA")
DYNA = Image.open("dyna.png").convert("RGBA")
END = Image.open("endcard.png").convert("RGBA")

xi = F("Italic", 1)
def mathline(size, parts):
    """parts: 'x' italic Poppins, symbols from DejaVu, rest Poppins Medium."""
    out = []
    for p, kind in parts:
        f = F("Italic", size) if kind == "i" else DJ(int(size * 0.95)) if kind == "s" else F("Medium", size)
        out.append((p, f, WHITE))
    return out

def dyna_card(dr, frame, t0, t, skill, line):
    a = appear(t, t0)
    lay = layer(); d = ImageDraw.Draw(lay)
    lay.alpha_composite(DYNA.resize((300, 300)), (130, 300))
    d.ellipse((124, 294, 436, 606), outline=TURQ + (255,), width=6)
    d.text((280, 618), "Dyna", font=F("Bold", 38), fill=WHITE, anchor="mt")
    d.text((280, 664), "your Thinking Coach", font=F("Regular", 24), fill=TEAL, anchor="mt")
    rrect(d, (110, 740, 760, 900), fill=CARD + (235,), outline=TURQ + (255,), w=3)
    d.rounded_rectangle((140, 765, 140 + F("Bold", 22).getlength(skill.upper()) + 40, 805), 20, fill=TURQ)
    d.text((160, 771), skill.upper(), font=F("Bold", 22), fill=(6, 30, 48))
    d.text((140, 825), line, font=F("Medium", 28), fill=WHITE)
    comp(frame, lay, a)

# ---------------- scenes ----------------
def sc_open(fr, t, D, cues):
    lay = layer(); d = ImageDraw.Draw(lay)
    k = F("Bold", 24); x = 110
    for ch in "CAMBRIDGE IGCSE & O LEVEL · ADDITIONAL MATHEMATICS":
        d.text((x, 200), ch, font=k, fill=TURQ); x += k.getlength(ch) + 3.5
    d.text((110, 250), "Exercise 1.1", font=F("Bold", 96), fill=WHITE)
    d.text((110, 370), "Mappings", font=F("Bold", 96), fill=TURQ)
    d.text((112, 500), "Chapter 1 · Functions", font=F("Medium", 34), fill=DIM)
    comp(fr, lay, appear(t, 0.1, 0.6))
    fr.alpha_composite(ATUL, (W - ATUL.width, H - ATUL.height)) if t > 0 else None
    # bubble
    lay = layer(); d = ImageDraw.Draw(lay)
    bx, by = 560, 720
    if t < cues[2][0] - 0.2:
        rrect(d, (bx, by, bx + 560, by + 190), fill=CARD + (240,), outline=TURQ + (255,), w=3)
        d.text((bx + 30, by + 26), "Hello, young thinkers!", font=F("Medium", 32), fill=WHITE)
        x = draw_runs(d, bx + 30, by + 72, [("Atul Sir", F("Bold", 32), TURQ), (", your Thinking Mentor,", F("Medium", 32), WHITE)])
        d.text((bx + 30, by + 118), "has guided this lesson.", font=F("Medium", 32), fill=WHITE)
        comp(fr, lay, appear(t, cues[0][0] - 0.2, 0.35))
    else:
        rrect(d, (bx, by, bx + 560, by + 145), fill=CARD + (240,), outline=TURQ + (255,), w=3)
        d.text((bx + 30, by + 26), "Today: one-one, many-one", font=F("Medium", 32), fill=WHITE)
        d.text((bx + 30, by + 72), "and one-many mappings.", font=F("Medium", 32), fill=WHITE)
        comp(fr, lay, appear(t, cues[2][0] - 0.2, 0.35))
        # chips
        lay = layer(); d = ImageDraw.Draw(lay); x = 110
        for i, w in enumerate(["one-one", "many-one", "one-many"]):
            l2 = layer(); d2 = ImageDraw.Draw(l2); f = F("Bold", 30); wd = f.getlength(w) + 56
            d2.rounded_rectangle((x, 600, x + wd, 660), 30, fill=MINT); d2.text((x + 28, 609), w, font=f, fill=NAVY)
            comp(fr, l2, appear(t, cues[2][0] + 0.5 + i * 0.6, 0.35)); x += wd + 22

Q_STEM = "Determine whether this mapping is one-one, many-one or one-many."
def question_card(fr, t, glow_rule=0., glow_dom=0., a=1.0, y=300):
    lay = layer(); d = ImageDraw.Draw(lay)
    rrect(d, (110, y, 1810, y + 330), fill=(245, 252, 253, 255), outline=None, r=26)
    d.text((170, y + 50), Q_STEM, font=F("Medium", 38), fill=NAVY)
    big = 92
    rule = [("x", F("Italic", big), NAVY), ("  ↦  ", DJ(int(big * 0.9)), NAVY), ("x", F("Italic", big), NAVY), (" + 1", F("Medium", big), NAVY)]
    dom = [("x", F("Italic", big - 20), NAVY), (" ∈ ", DJ(int((big - 20) * 0.9)), NAVY), ("ℝ", DJ(int((big - 20) * 0.95)), NAVY)]
    rx, ry = 300, y + 140; rw = runs_width(rule); dx = rx + rw + 260; dw = runs_width(dom)
    if glow_rule > 0:
        d.rounded_rectangle((rx - 30, ry - 6, rx + rw + 30, ry + 132), 22, fill=(214, 247, 243, int(255 * glow_rule)),
                            outline=TURQ + (int(255 * glow_rule),), width=5)
    if glow_dom > 0:
        d.rounded_rectangle((dx - 30, ry + 6, dx + dw + 30, ry + 124), 22, fill=(214, 247, 243, int(255 * glow_dom)),
                            outline=TURQ + (int(255 * glow_dom),), width=5)
    for (s, f, c) in rule:
        dyo = int(f.size * 0.10) if "DejaVu" in f.path else 0
        d.text((rx, ry + dyo), s, font=f, fill=c); rx += f.getlength(s)
    for (s, f, c) in dom:
        dyo = int(f.size * 0.10) + 18 if "DejaVu" in f.path else 18
        d.text((dx, ry + dyo), s, font=f, fill=c); dx += f.getlength(s)
    comp(fr, lay, a)
    return (300, ry, rw), (dx - dw, ry, dw)

def sc_question(fr, t, D, cues):
    lay = layer(); d = ImageDraw.Draw(lay)
    header(d, "EXERCISE 1.1 · QUESTION 1", [("Read the ", F("Bold", 46), WHITE), ("rule", F("Bold", 46), TURQ),
                                               (" and the ", F("Bold", 46), WHITE), ("domain", F("Bold", 46), TURQ)])
    comp(fr, lay, appear(t, 0.0))
    gr = appear(t, cues[2][0], 0.35) * (1 - appear(t, cues[4][0] - 0.1, 0.35))
    gd = appear(t, cues[4][0], 0.35)
    question_card(fr, t, gr, gd, appear(t, cues[0][0] - 0.1, 0.5))
    # labels under the card
    lay = layer(); d = ImageDraw.Draw(lay)
    d.text((300, 680), "RULE: x is mapped to x + 1", font=F("Bold", 30), fill=TURQ + (255,))
    comp(fr, lay, appear(t, cues[3][0], 0.4))
    lay = layer(); d = ImageDraw.Draw(lay)
    d.text((1150, 680), "DOMAIN: every real number", font=F("Bold", 30), fill=TURQ + (255,))
    comp(fr, lay, appear(t, cues[5][0], 0.4))

def ovals(d, cx, cy, n, label, a=255):
    d.ellipse((cx - 85, cy - 150, cx + 85, cy + 150), outline=TEAL + (a,), width=4, fill=(11, 47, 70, int(a * 0.9)))
    d.text((cx, cy + 172), label, font=F("Medium", 24), fill=DIM + (a,), anchor="mt")
def dot_pos(cx, cy, n, i): return (cx, cy - 90 + i * 180 / max(1, n - 1)) if n > 1 else (cx, cy)

def kind_panel(fr, t, t0, x, title, sub, ins, outs, links):
    a = appear(t, t0)
    if a <= 0: return
    lay = layer(); d = ImageDraw.Draw(lay)
    rrect(d, (x, 300, x + 520, 880), fill=CARD + (230,), outline=TURQ + (255,), w=3)
    d.text((x + 260, 330), title, font=F("Bold", 40), fill=TURQ, anchor="mt")
    d.text((x + 260, 390), sub, font=F("Regular", 24), fill=WHITE, anchor="mt")
    ci, co, cy = x + 130, x + 390, 610
    ovals(d, ci, cy, len(ins), "inputs"); ovals(d, co, cy, len(outs), "outputs")
    for i in range(len(ins)):
        px, py = dot_pos(ci, cy, len(ins), i); d.ellipse((px - 12, py - 12, px + 12, py + 12), fill=WHITE)
    for j in range(len(outs)):
        px, py = dot_pos(co, cy, len(outs), j); d.ellipse((px - 12, py - 12, px + 12, py + 12), fill=TURQ)
    for k, (i, j) in enumerate(links):
        u = ease((t - t0 - 0.4 - 0.35 * k) / 0.7)
        p0 = dot_pos(ci, cy, len(ins), i); p1 = dot_pos(co, cy, len(outs), j)
        arrow(d, (p0[0] + 16, p0[1]), (p1[0] - 18, p1[1]), u, (255, 200, 60, 255))
    comp(fr, lay, a)

def sc_kinds(fr, t, D, cues):
    lay = layer(); d = ImageDraw.Draw(lay)
    header(d, "WHAT YOU NEED TO KNOW", [("Three kinds of ", F("Bold", 46), WHITE), ("mapping", F("Bold", 46), TURQ)])
    comp(fr, lay, appear(t, 0))
    kind_panel(fr, t, cues[1][0], 110, "One-one", "each output has one input", [0, 1, 2], [0, 1, 2], [(0, 0), (1, 1), (2, 2)])
    kind_panel(fr, t, cues[3][0], 700, "Many-one", "two inputs share an output", [0, 1, 2], [0, 1], [(0, 0), (1, 0), (2, 1)])
    kind_panel(fr, t, cues[5][0], 1290, "One-many", "one input, two outputs", [0, 1], [0, 1, 2], [(0, 0), (0, 1), (1, 2)])

ROWS = [("−1", "0"), ("0", "1"), ("1", "2"), ("2", "3")]
def sc_table(fr, t, D, cues):
    lay = layer(); d = ImageDraw.Draw(lay)
    header(d, "DYNA'S HINT 1", [("Turn the words into ", F("Bold", 46), WHITE), ("a table", F("Bold", 46), TURQ)])
    comp(fr, lay, appear(t, 0))
    dyna_card(fr, fr, 0.1, t, "Translator", "Turn words into numbers.")
    # table
    a = appear(t, cues[1][0] - 0.2)
    lay = layer(); d = ImageDraw.Draw(lay)
    tx, ty = 900, 260
    rrect(d, (tx, ty, tx + 380, ty + 100), fill=TURQ + (255,), r=18)
    d.text((tx + 95, ty + 50), "x", font=F("BoldItalic", 46), fill=(6, 30, 48), anchor="mm")
    draw_runs(d, tx + 215, ty + 20, [("x", F("BoldItalic", 46), (6, 30, 48)), (" + 1", F("Bold", 46), (6, 30, 48))])
    comp(fr, lay, a)
    # mapping ovals
    lay = layer(); d = ImageDraw.Draw(lay)
    ci, co, cy = 1420, 1700, 560
    for cx, lab in ((ci, "inputs"), (co, "outputs")):
        d.ellipse((cx - 85, cy - 250, cx + 85, cy + 250), outline=TEAL, width=4, fill=CARD + (230,))
        d.text((cx, cy + 270), lab, font=F("Medium", 24), fill=DIM, anchor="mt")
    comp(fr, lay, a)
    for k, (xin, xout) in enumerate(ROWS):
        t0 = cues[2 + k][0] - 0.1; u = appear(t, t0, 0.35)
        if u <= 0: continue
        lay = layer(); d = ImageDraw.Draw(lay)
        ry = ty + 115 + k * 100
        d.rounded_rectangle((tx, ry, tx + 380, ry + 88), 14, fill=CARD + (240,), outline=TEAL, width=2)
        d.text((tx + 95, ry + 44), xin, font=F("Medium", 44), fill=WHITE, anchor="mm")
        d.text((tx + 285, ry + 44), xout, font=F("Bold", 44), fill=TURQ, anchor="mm")
        py = cy - 180 + k * 120
        d.text((ci, py), xin, font=F("Bold", 38), fill=WHITE, anchor="mm")
        comp(fr, lay, u)
        v = ease((t - t0 - 0.3) / 0.6)
        if v > 0:
            lay = layer(); d = ImageDraw.Draw(lay)
            arrow(d, (ci + 40, py), (co - 40, py), v, (255, 200, 60, 255))
            if v > 0.95: d.text((co, py), xout, font=F("Bold", 38), fill=TURQ, anchor="mm")
            comp(fr, lay, 1)
    # question pill
    u = appear(t, cues[6][0])
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay)
        rrect(d, (900, 820, 1340, 890), fill=(255, 200, 60, 255), r=35)
        d.text((1120, 855), "Any two outputs the same?", font=F("Bold", 28), fill=(30, 40, 50), anchor="mm")
        comp(fr, lay, u)

def sc_graph(fr, t, D, cues):
    lay = layer(); d = ImageDraw.Draw(lay)
    header(d, "PICTURE IT", [("Sketch ", F("Bold", 46), WHITE), ("y = x + 1", F("Bold", 46), TURQ)])
    comp(fr, lay, appear(t, 0))
    ox, oy, s = 960, 640, 95          # origin and pixels per unit; x from -4 to 4, y from -3 to 4
    def P(x, y): return (ox + x * s, oy - y * s)
    lay = layer(); d = ImageDraw.Draw(lay)
    for gx in range(-4, 5):
        d.line((*P(gx, -3.2), *P(gx, 4.2)), fill=(40, 80, 105, 255), width=1)
    for gy in range(-3, 5):
        d.line((*P(-4.6, gy), *P(4.6, gy)), fill=(40, 80, 105, 255), width=1)
    d.line((*P(-4.8, 0), *P(4.8, 0)), fill=WHITE, width=3); d.line((*P(0, -3.4), *P(0, 4.4)), fill=WHITE, width=3)
    d.text(P(4.85, 0.05), "x", font=F("Italic", 34), fill=WHITE, anchor="lm"); d.text(P(0.12, 4.45), "y", font=F("Italic", 34), fill=WHITE, anchor="ls")
    for v in (-3, -2, -1, 1, 2, 3, 4):
        d.text(P(v, -0.15), str(v).replace("-", "−"), font=F("Regular", 22), fill=DIM, anchor="mt")
    for v in (-2, -1, 1, 2, 3):
        d.text(P(-0.15, v), str(v).replace("-", "−"), font=F("Regular", 22), fill=DIM, anchor="rm")
    comp(fr, lay, appear(t, 0.1, 0.6))
    pts = [(-1, 0), (0, 1), (1, 2), (2, 3)]
    for k, (px, py) in enumerate(pts):
        u = appear(t, cues[1][0] + 0.25 * k, 0.3)
        if u > 0:
            lay = layer(); d = ImageDraw.Draw(lay); X, Y = P(px, py)
            r = 14 * (0.6 + 0.4 * u); d.ellipse((X - r, Y - r, X + r, Y + r), fill=TURQ)
            d.text((X + 22, Y - 10), f"({str(px).replace('-', chr(8722))}, {py})", font=F("Medium", 24), fill=WHITE, anchor="ls")
            comp(fr, lay, u)
    v = ease((t - cues[2][0]) / 1.2)
    if v > 0:
        lay = layer(); d = ImageDraw.Draw(lay)
        x0, x1 = -4.0, 3.0; xe = x0 + (x1 - x0) * v
        d.line((*P(x0, x0 + 1), *P(xe, xe + 1)), fill=TURQ, width=6)
        comp(fr, lay, 1)
    u = appear(t, cues[3][0], 0.4)
    if u > 0:
        tt = t - cues[3][0]
        yv = 1.0 + 2.6 * math.sin(tt * 0.9)          # slides between about -1.6 and 3.6
        lay = layer(); d = ImageDraw.Draw(lay)
        xa, xb = -4.6, 4.6; X0, Y = P(xa, yv); X1, _ = P(xb, yv); x = X0
        while x < X1: d.line((x, Y, min(x + 24, X1), Y), fill=(255, 200, 60, 255), width=4); x += 40
        cx, cy = P(yv - 1, yv)
        if -4 <= yv - 1 <= 3: d.ellipse((cx - 13, cy - 13, cx + 13, cy + 13), outline=(255, 200, 60, 255), width=5)
        comp(fr, lay, u)

def sc_vault(fr, t, D, cues):
    lay = layer(); d = ImageDraw.Draw(lay)
    header(d, "DYNA'S HINT 2", [("Use what you ", F("Bold", 46), WHITE), ("already know", F("Bold", 46), TURQ)])
    comp(fr, lay, appear(t, 0))
    dyna_card(fr, fr, 0.1, t, "Vault", "Pick what you already know.")
    lay = layer(); d = ImageDraw.Draw(lay)
    d.text((900, 300), "Suppose two inputs,", font=F("Medium", 44), fill=WHITE)
    draw_runs(d, 900, 362, [("a", F("BoldItalic", 44), TURQ), (" and ", F("Medium", 44), WHITE), ("b", F("BoldItalic", 44), (255, 200, 60)),
                            (",  give the same output.", F("Medium", 44), WHITE)])
    comp(fr, lay, appear(t, cues[2][0] - 0.1))
    # mapping picture: a and b both arrowing to one output (the supposition)
    u = appear(t, cues[3][0] - 0.1)
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay)
        ci, co, cy = 1000, 1500, 560
        for cx in (ci, co): d.ellipse((cx - 70, cy - 110, cx + 70, cy + 110), outline=TEAL, width=4, fill=CARD + (230,))
        d.text((ci, cy - 50), "a", font=F("BoldItalic", 40), fill=TURQ, anchor="mm")
        d.text((ci, cy + 50), "b", font=F("BoldItalic", 40), fill=(255, 200, 60), anchor="mm")
        d.text((co, cy), "?", font=F("Bold", 44), fill=WHITE, anchor="mm")
        comp(fr, lay, u)
        v = ease((t - cues[3][0] - 0.2) / 0.7)
        if v > 0:
            lay = layer(); d = ImageDraw.Draw(lay)
            arrow(d, (ci + 30, cy - 50), (co - 35, cy - 8), v, TURQ + (255,)); arrow(d, (ci + 30, cy + 50), (co - 35, cy + 8), v, (255, 200, 60, 255))
            comp(fr, lay, 1)
    # equation writes itself
    t0 = cues[4][0]
    eq = [("a", F("BoldItalic", 84), TURQ), (" + 1  =  ", F("Medium", 84), WHITE), ("b", F("BoldItalic", 84), (255, 200, 60)), (" + 1", F("Medium", 84), WHITE)]
    if t > t0:
        lay = layer(); d = ImageDraw.Draw(lay)
        rrect(d, (900, 740, 1720, 900), fill=CARD + (240,), outline=TURQ + (255,), w=3)
        full = runs_width(eq); x = 1310 - full / 2
        reveal = ease((t - t0) / 1.4) * full
        draw_runs(d, x, 765, eq)
        # mask the part not yet written
        d.rectangle((x + reveal, 750, 1715, 895), fill=CARD + (255,))
        comp(fr, lay, 1)
    u = appear(t, cues[5][0])
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay)
        pulse = 0.5 + 0.5 * math.sin((t - cues[5][0]) * 5)
        rrect(d, (900, 930, 1720, 1000), fill=(255, 200, 60, 255), r=35)
        draw_runs(d, 1310 - 230, 943, [("So what must be true of ", F("Bold", 30), (30, 40, 50)), ("a", F("BoldItalic", 30), (30, 40, 50)),
                                        (" and ", F("Bold", 30), (30, 40, 50)), ("b", F("BoldItalic", 30), (30, 40, 50)), ("?", F("Bold", 30), (30, 40, 50))])
        comp(fr, lay, u)

def sc_turn(fr, t, D, cues):
    lay = layer(); d = ImageDraw.Draw(lay)
    d.rounded_rectangle((110, 90, 330, 140), 25, fill=TEAL); d.text((220, 115), "YOUR TURN", font=F("Bold", 26), fill=(6, 30, 48), anchor="mm")
    d.text((110, 170), "Can two different inputs share an output here?", font=F("Bold", 50), fill=WHITE)
    comp(fr, lay, appear(t, 0))
    question_card(fr, t, 0, 0, appear(t, 0.2), y=300)
    lay = layer(); d = ImageDraw.Draw(lay); x = 300
    for w in ["one-one", "many-one", "one-many"]:
        f = F("Bold", 38); wd = f.getlength(w) + 70
        d.rounded_rectangle((x, 720, x + wd, 800), 40, fill=MINT); d.text((x + 35, 735), w, font=f, fill=NAVY); x += wd + 40
    d.text((x + 30, 742), "My answer", font=F("Medium", 30), fill=DIM)
    bx = x + 210
    pul = 0.5 + 0.5 * math.sin(t * 4) if t > cues[1][0] else 1
    d.rounded_rectangle((bx, 715, bx + 90, 805), 14, outline=(255, 200, 60, int(120 + 135 * pul)), width=5)
    comp(fr, lay, appear(t, cues[1][0] - 0.2))
    u = appear(t, cues[2][0] - 0.1)
    if u > 0:
        lay = layer(); d = ImageDraw.Draw(lay)
        rrect(d, (300, 860, 820, 930), fill=(255, 200, 60, 255), r=35)
        d.rectangle((345, 880, 353, 910), fill=(30, 40, 50)); d.rectangle((361, 880, 369, 910), fill=(30, 40, 50))
        d.text((590, 895), "Pause the video and try!", font=F("Bold", 30), fill=(30, 40, 50), anchor="mm")
        comp(fr, lay, u)

def sc_end(fr, t, D, cues):
    comp(fr, END.copy(), appear(t, 0, 0.6))

DRAW = dict(open=sc_open, question=sc_question, kinds=sc_kinds, table=sc_table, graph=sc_graph, vault=sc_vault, turn=sc_turn, end=sc_end)

def render(timeline, total):
    n = int(math.ceil(total * FPS))
    p = subprocess.Popen(["ffmpeg", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "video.mp4"],
                         stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for i in range(n):
        T = i / FPS
        for name, st, D, cues in timeline:
            if st <= T < st + D or name == timeline[-1][0]:
                break
        t = T - st
        fr = BG.copy()
        DRAW[name](fr, t, D, cues)
        # scene fade in / out (to background)
        out_a = 1 - ease((t - (D - FADE)) / FADE) if name != "end" else 1
        in_a = ease(t / FADE) if name not in ("open",) else 1
        a = min(out_a, in_a)
        if a < 1: fr = Image.blend(BG, fr, a)
        p.stdin.write(fr.convert("RGB").tobytes())
    p.stdin.close(); p.wait()

if __name__ == "__main__":
    import sys, json
    timeline, total = asyncio.run(narration())
    json.dump(timeline, open("timeline.json", "w"), indent=1)
    print("total", round(total, 1), [(n, round(s, 1), round(d, 1)) for n, s, d, _ in timeline])
    if len(sys.argv) > 1 and sys.argv[1] == "stills":
        for name, st, D, cues in timeline:
            fr = BG.copy(); DRAW[name](fr, D - 0.5, D, cues); fr.convert("RGB").save(f"still_{name}.png")
        sys.exit()
    render(timeline, total)
    sh("python3", "/home/claude/lec/music.py", "voice.wav", "mix.wav")
    sh("ffmpeg", "-y", "-i", "video.mp4", "-i", "mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
       "-shortest", "IGCSE_AddMath_Ex1.1_Q1_lecture_test.mp4")
    print("done")
