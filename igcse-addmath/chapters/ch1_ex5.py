"""Cambridge IGCSE & O Level Additional Mathematics, Chapter 1: Functions, Exercise 1.5 (graphs of y = |f(x)| where f(x) is linear).
Source exercise: Cambridge IGCSE & O Level Additional Mathematics Coursebook, Chapter 1, Exercise 1.5 (pp. 14-15).
Answers (checked by hand and with SymPy, never printed):
Q1 a corner (-1, 0), meets y-axis (0, 1); b (1.5, 0), (0, 3); c (5, 0), (0, 5); d (-6, 0), (0, 3); e (5, 0), (0, 10); f (18, 0), (0, 6).
Q2 a x = -2, -1, 0, 1, 2, 3, 4 give y = 7, 6, 5, 4, 3, 4, 5; b V-shape with lowest point (2, 3), from (-2, 7) to (4, 5).
Q3 a V, corner (0, 1); b V, corner (0, -3), meets x-axis at (-3, 0), (3, 0); c upside-down V, top (0, 2), meets x-axis at (-2, 0), (2, 0);
   d V, corner (3, 1), meets y-axis (0, 4); e V, corner (-3, -3), meets x-axis (-4.5, 0), (-1.5, 0), y-axis (0, 3).
Q4 a -3 <= f(x) <= 11; b 0 <= g(x) <= 11; c -3 <= h(x) <= 5.
Q5 -5 <= f(x) <= 5; 0 <= g(x) <= 5; -5 <= h(x) <= 3.
Q6 a (-2, 0), (0, 4); b line through (-5, 0) and (0, 5); c x = -3 or x = 1.
Q7 a V, corner (3, -3), ends (-1, 5) and (8, 7); b -3 <= f(x) <= 7; c x = 0.5 or x = 5.5.
Q8 a (4/3, 0), (0, 4); b line through the origin, gradient 2; c x = 0.8 or x = 4.
Q9 a f(x) = -2x for x <= -2, 4 for -2 <= x <= 2, 2x for x >= 2 (a flat-bottomed V); b x = -3 or x = 3.
Supplementary: none. Neither bank (Relation and Functions Obj; 1_Functions_Obj) has a question within the scope of Section 1.5
(sketching y = |ax + b|, reading ranges and solving modulus equations from graphs) that is not already used: 74864
(range of -|x|) is printed in Exercise 1.4; the bank's graph questions use symmetry, sgn, logs or inverse graphs."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_class'))
from glyphs_svg import MAP, TO, IN, R, sym

x = '<i>x</i>'; y = '<i>y</i>'
def fr(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'
def md(e):
    return f'<span class="mod"><span>{e}</span></span>'
LE = '≤'; GE = '≥'
YE = f'{y} ='

CH = dict(
    num=1, title='Functions', first_page=46, exercise='Exercise 1.5',
    subject='Cambridge IGCSE &amp; O Level Additional Mathematics',
    lecture_qr=None, dyna_qr='CGN000024',   # lecture QR not issued yet (placeholder); CGN000024 = Chapter 1 Cognoo pathway
    count_line='Exercise 1.5 · 9 questions · Graphs of y = |f(x)| where f(x) is linear · Goes with Chapter 1 of your Additional Mathematics Coursebook',
)

KNOW = [
    f'<b>Reflect:</b> to sketch {y} = {md("f(" + x + ")")}, draw {y} = f({x}), then reflect the part below the {x}-axis.',
    f'<b>V-shape:</b> {y} = {md("<i>a</i>" + x + " + <i>b</i>")} has its corner on the {x}-axis, where <i>a</i>{x} + <i>b</i> = 0.',
    f'<b>Axes:</b> put {x} = 0 to find where the graph meets the {y}-axis; the corner gives the {x}-axis point.',
    f'<b>Solve by graph:</b> the solutions of {md("f(" + x + ")")} = g({x}) are the {x}-values where the graphs meet.',
]

BARS = [
    ('Piecewise Graphs', 'sketch y = |f(x)|', 5, '#007ea2', 'Q 1 a–c, d–f, Q 2, Q 3 a–c, d–e'),
    ('Domain and Range', 'range over a given domain', 3, '#05ccab', 'Q 4, 5, 7'),
    ('Graphical Solutions', 'where two graphs meet', 3, '#05ccab', 'Q 6, 8, 9'),
]
BARS_TITLE = 'Concepts this exercise tests'
BARS_SUB = 'Main concept of each of the 11 question blocks'
ALSO = ['Modulus Function · Q 1 to 9', 'Polynomial Functions · straight lines, Q 1 to 9', 'Extraneous Roots · Q 6 c, 8 c',
        'Domain and Range · restricted x in Q 2, 6, 8']

ROUTINE = [('SKETCH', f'Draw {y} = f({x}) as a straight line first.'),
           ('REFLECT', f'Reflect the part below the {x}-axis up above it.'),
           ('MARK', 'Label the corner and where the graph meets the axes.'),
           ('READ', 'Read the range or the crossing points from your graph.')]
WATCH_SUB = 'A modulus graph never dips below the x-axis, unless something is added outside.'
WATCH = [
    ('Q 1', f'The corner sits on the {x}-axis, where the inside equals 0.', f'{md("2" + x + " − 5")} has its corner at {x} = 2.5.'),
    ('Q 3', 'A number <b>outside</b> the modulus moves the whole V up or down.', f'{y} = {md(x)} − 2 has its corner at (0, −2).'),
    ('Q 3 c, 4 c, 5', 'A minus sign in front of the modulus turns the V upside down.', f'{y} = 4 − {md(x)} has its highest point at (0, 4).'),
    ('Q 4, 5, 7', 'The smallest value may be at the corner, not at an end of the domain.', f'{md(x + " − 1")} for −2 {LE} {x} {LE} 3 is smallest at {x} = 1.'),
    ('Q 6 c, 8 c', 'Check each answer in the original equation.', f'{md(x + " − 3")} = 2{x} gives {x} = −3, which fails.'),
]
TRYONE = dict(
    q=f'<b>Sketch the graph of</b>&nbsp; {y} = {md(x + " − 4")}, showing the coordinates of the points where it meets the axes.',
    opts=[], write='Meets the axes at:',
    hints=[('Echo', f'Say it in your own words: “the distance of {x} from 4”. A distance is never negative.'),
           ('Starter', f'Begin with the corner: where is {x} − 4 = 0? That point sits on the {x}-axis.'),
           ('Translator', f'Make a table for {x} = 2, 3, 4, 5, 6, plot the points and join them.')],
    turn=f'Put {x} = 0 to find where the graph meets the {y}-axis. Mark both points.',
)
BEFORE = 'Read Section 1.5 of the coursebook: reflecting y = f(x) in the x-axis, Worked example 7, and solving modulus equations with graphs.'
AHEAD = 'Q 9 adds two moduli. Split the x-axis at −2 and 2 and look at each piece on its own.'

SK = {
    'Bridge': 'connect to everyday life', 'Starter': 'decide how to begin', 'Slicer': 'break it into small parts',
    'Echo': 'say it in your own words', 'Vault': 'pick what you already know', 'Roots': 'ask why it works',
    'Translator': 'turn words into numbers, pictures or steps'}
SQ = {
    'Bridge': 'What does this remind me of from my everyday life?', 'Starter': 'Where do I begin? Which clue is the easiest to use first?',
    'Slicer': 'Can I break this into small steps and solve one step at a time?', 'Echo': 'Can I say this question again in my own words?',
    'Vault': 'What do I already know that can help me here?', 'Roots': 'Why does this work? What is the rule hiding behind it?',
    'Translator': 'Can I turn the words into numbers, a drawing or a list of steps?'}

def table2():
    xs = ['−2', '−1', '0', '1', '2', '3', '4']; ys = ['', '6', '', '4', '', '', '']
    td = 'border:.75pt solid #1e436d;width:30pt;height:17pt;text-align:center;font-size:9.5pt'
    th = td + ';background:#d6f7f3;font-weight:700;color:#007fa3;width:24pt'
    r1 = f'<td style="{th}"><i>x</i></td>' + ''.join(f'<td style="{td}">{v}</td>' for v in xs)
    r2 = f'<td style="{th}"><i>y</i></td>' + ''.join(f'<td style="{td}">{v}</td>' for v in ys)
    return f'<table style="border-collapse:collapse;margin:5pt 0 3pt 16pt"><tr>{r1}</tr><tr>{r2}</tr></table>'

S1 = 'Sketch the graphs of each of the following functions, showing the coordinates of the points where the graph intersects the axes.'
S3 = 'Draw the graph of each of the following functions.'
Q = [
 dict(n=1, label='Q 1 a–c', text=S1, part_label='Axes:',
      parts=[('a', f'{y} = {md(x + " + 1")}'), ('b', f'{y} = {md("2" + x + " − 3")}'), ('c', f'{y} = {md("5 − " + x)}')],
      dyna=[('Starter', 'Begin with the corner: where does the inside of the modulus equal 0? That point is on the x-axis.'),
            ('Translator', f'For a, sketch {y} = {x} + 1 first (gradient 1, crossing the {y}-axis at 1). Then reflect the part below the {x}-axis.')],
      turn=f'Mark the corner and the {y}-axis point on each sketch and write their coordinates.'),
 dict(n=1, label='Q 1 d–f', text=S1 + ' (continued)', part_label='Axes:',
      parts=[('d', f'{y} = {md(fr("1", "2") + x + " + 3")}'), ('e', f'{y} = {md("10 − 2" + x)}'), ('f', f'{y} = {md("6 − " + fr("1", "3") + x)}')],
      dyna=[('Vault', f'Recall Worked example 7: a line like {fr("1", "2")}{x} − 1 is sketched first, then the part below the axis is reflected.'),
            ('Slicer', f'For each part find two points: the corner (inside = 0) and the {y}-axis point (put {x} = 0). Then join with a V.')],
      turn='Write the coordinates of both points for d, e and f.'),
 dict(n=2, text=f'<b>a</b>&nbsp; Complete the table of values for {y} = {md(x + " − 2")} + 3.', math=table2() +
      f'<div class="qt" style="margin-top:2pt"><b>b</b>&nbsp; Draw the graph of {y} = {md(x + " − 2")} + 3 for −2 {LE} {x} {LE} 4.</div>', noans=True,
      dyna=[('Translator', f'For each {x}: work out {x} − 2, drop its sign, then add 3. The two given values (6 and 4) let you check your method.'),
            ('Bridge', 'Think of a fare of 3 coins plus 1 coin for each stop you are away from stop 2. Where is the ride cheapest?')],
      turn='Fill in the table, plot the seven points and join them with straight lines.'),
 dict(n=3, label='Q 3 a–c', text=S3, part_label='Key points:',
      parts=[('a', f'{y} = {md(x)} + 1'), ('b', f'{y} = {md(x)} − 3'), ('c', f'{y} = 2 − {md(x)}')],
      dyna=[('Echo', f'Say part a in words: “the V of {md(x)}, moved up 1”. Do the same for b.'),
            ('Roots', f'Ask why the minus sign in c turns the V upside down: every output of {md(x)} changes sign before 2 is added.')],
      turn=f'Sketch all three and mark the corner and any points where each graph meets the {x}-axis.'),
 dict(n=3, label='Q 3 d–e', text=S3 + ' (continued)', part_label='Key points:',
      parts=[('d', f'{y} = {md(x + " − 3")} + 1'), ('e', f'{y} = {md("2" + x + " + 6")} − 3')],
      dyna=[('Slicer', 'Two steps: sketch the V of the modulus part, then move it up or down by the number outside.'),
            ('Vault', f'Recall: the corner is where the inside is 0. In e, ask where 2{x} + 6 = 0, then where the moved V crosses the {x}-axis.')],
      turn='Mark the corner and where each graph meets the axes.'),
 dict(n=4, text=f'Given that each of these functions is defined for the domain −3 {LE} {x} {LE} 4, find the range of', part_label='Range:',
      parts=[('a', f'f : {x} {MAP} 5 − 2{x}'), ('b', f'g : {x} {MAP} {md("5 − 2" + x)}'), ('c', f'h : {x} {MAP} 5 − {md("2" + x)}')],
      dyna=[('Starter', f'Begin with f: it is a straight line, so its range comes from the two ends, {x} = −3 and {x} = 4.'),
            ('Roots', 'For g and h, ask why the smallest (or largest) value may be at the corner inside the domain, not at an end.')],
      turn='Sketch each graph over the domain, then write each range.'),
 dict(n=5, text=(f'f : {x} {MAP} 3 − 2{x}&nbsp; for −1 {LE} {x} {LE} 4<br>g : {x} {MAP} {md("3 − 2" + x)}&nbsp; for −1 {LE} {x} {LE} 4<br>'
                 f'h : {x} {MAP} 3 − {md("2" + x)}&nbsp; for −1 {LE} {x} {LE} 4<br>Find the range of each function.'),
      parts=[('', '', 'Range of f:'), ('', '', 'Range of g:'), ('', '', 'Range of h:')], cols=1,
      dyna=[('Vault', 'Use what you did in Q 4: the same three shapes, with new numbers and a new domain.'),
            ('Translator', f'Sketch each graph for −1 {LE} {x} {LE} 4 and mark its value at both ends and at the corner.')],
      turn='Read the lowest and highest values from each sketch.'),
 dict(n=6, text='', cols=1,
      parts=[('a', f'Sketch the graph of {y} = {md("2" + x + " + 4")} for −6 &lt; {x} &lt; 2, showing the coordinates of the points where the graph intersects the axes.', 'Meets the axes at:'),
             ('b', f'On the same diagram, sketch the graph of {y} = {x} + 5.', 'The graphs cross near:'),
             ('c', f'Solve the equation {md("2" + x + " + 4")} = {x} + 5.', 'x =')],
      dyna=[('Translator', 'Draw both graphs on one diagram. The solutions of c are the x-coordinates where they cross.'),
            ('Echo', 'Say c in words: “where is the V at the same height as the line?”')],
      turn='Read the crossing points, then check each one in the equation.'),
 dict(n=7, text=f'A function f is defined by f({x}) = {md("2" + x + " − 6")} − 3, for −1 {LE} {x} {LE} 8.', cols=1,
      parts=[('a', f'Sketch the graph of {y} = f({x}).', 'Lowest point:'), ('b', 'State the range of f.', 'Range of f:'), ('c', f'Solve the equation f({x}) = 2.', 'x =')],
      dyna=[('Slicer', 'Do a, b, c in order: the sketch gives the range, and the range tells you how many solutions to expect in c.'),
            ('Starter', f'Begin at the corner: where is 2{x} − 6 = 0, and what is f there? Then work out f(−1) and f(8).')],
      turn='Write the range, then solve f(x) = 2 and check both answers lie in the domain.'),
 dict(n=8, text='', cols=1,
      parts=[('a', f'Sketch the graph of {y} = {md("3" + x + " − 4")} for −2 &lt; {x} &lt; 5, showing the coordinates of the points where the graph intersects the axes.', 'Meets the axes at:'),
             ('b', f'On the same diagram, sketch the graph of {y} = 2{x}.', 'The graphs cross near:'),
             ('c', f'Solve the equation 2{x} = {md("3" + x + " − 4")}.', 'x =')],
      dyna=[('Roots', f'Ask why you must check: 2{x} is negative when {x} &lt; 0, but a modulus never is.'),
            ('Bridge', 'Think of two roads on a map: every crossing is a solution, so count the crossings on your sketch first.')],
      turn='Solve both cases and keep the answers that match your sketch.'),
 dict(n=9, text='<b>CHALLENGE QUESTION</b>', cols=1,
      parts=[('a', f'Sketch the graph of f({x}) = {md(x + " + 2")} + {md(x + " − 2")}.', 'Shape:'),
             ('b', f'Use your graph to solve the equation {md(x + " + 2")} + {md(x + " − 2")} = 6.', 'x =')],
      dyna=[('Slicer', f'Split the {x}-axis at −2 and 2. On each piece, remove the modulus signs and simplify.'),
            ('Echo', f'Say it: “the distance from −2 plus the distance from 2”. What happens to that total when {x} is between −2 and 2?')],
      turn='Draw the three pieces, then read where the graph reaches 6.'),
]
SPOT = None

SUPP = []

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1], True, 'space'), ('questions', [2, 3], False, 'space'), ('questions', [4, 5, 6], False, 'space'),
    ('questions', [7, 8], False, 'space'), ('questions', [9, 10], False, 'space'), ('questions', [11], False, 'spaceqr'),
]
