"""Cambridge IGCSE & O Level Additional Mathematics, Chapter 1: Functions, Exercise 1.7 (the graph of a function and its inverse).
Source exercise: Cambridge IGCSE & O Level Additional Mathematics Coursebook, Chapter 1, Exercise 1.7 (pp. 20-21).
The grids for Q 1 and Q 2 are redrawn from the coursebook (assets/ch1/ex7_q1.png, ex7_q2.png; made by a matplotlib script):
f is the line y = x/2 - 1/2 from (-5, -3) to (5, 2); g is y = sqrt(x + 4) from (-4, 0) to (5, 3).
Answers (checked by hand and with SymPy, never printed):
Q1 f^-1(x) = 2x + 1, a line from (-3, -5) to (2, 5).
Q2 g^-1(x) = x^2 - 4 for 0 <= x <= 3: a curve from (0, -4) to (3, 5), crossing the x-axis at (2, 0).
Q3 f meets the y-axis at (0, 3); f^-1(x) = sqrt(x - 3) meets the x-axis at (3, 0).
Q4 g meets the y-axis at (0, 1); g^-1 meets the x-axis at (1, 0).
Q5 g: (0, -1) and (1, 0); g^-1(x) = sqrt(x + 1): (-1, 0) and (0, 1).
Q6 f from (-1, -6) to (3, 10), meets the axes at (0, -2) and (0.5, 0); f^-1(x) = (x + 2)/4 from (-6, -1) to (10, 3), meets the axes at (-2, 0) and (0, 0.5).
Q7 a f is one-one for x >= -1 (it only decreases from its turning point (-1, 3)); b f^-1(x) = sqrt(3 - x) - 1 for x <= 3;
   c f: (0, 2) and (sqrt3 - 1, 0); f^-1: (2, 0) and (0, sqrt3 - 1).
Q8 a f^-1(x) = (2x + 7)/(x - 2), the same as f; b f is self-inverse, so the graph of y = f(x) is symmetrical about the line y = x.
Supplementary: see the SUPP comment below (answers never printed)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_class'))
from glyphs_svg import MAP, TO, IN, R, sym

x = '<i>x</i>'; y = '<i>y</i>'
def fr(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'
def rt(e):
    return f'√<span style="text-decoration:overline">{e}</span>'
LE = '≤'; GE = '≥'; NE = '≠'
INV = '<sup>−1</sup>'
XR = f'{x} {IN} {R}'
AXES = 'Points on the axes:'

CH = dict(
    num=1, title='Functions', first_page=66, exercise='Exercise 1.7',
    subject='Cambridge IGCSE &amp; O Level Additional Mathematics',
    lecture_qr=None, dyna_qr='CGN000024',   # lecture QR not issued yet (placeholder); CGN000024 = Chapter 1 Cognoo pathway
    count_line='Exercise 1.7 · 8 questions · The graph of a function and its inverse · Goes with Chapter 1 of your Additional Mathematics Coursebook',
)

KNOW = [
    f'<b>Mirror:</b> the graphs of f and f{INV} are reflections of each other in the line {y} = {x}.',
    f'<b>Swap points:</b> if (<i>a</i>, <i>b</i>) lies on f, then (<i>b</i>, <i>a</i>) lies on f{INV}.',
    f'<b>Axes:</b> if f meets the {y}-axis at (0, <i>c</i>), then f{INV} meets the {x}-axis at (<i>c</i>, 0).',
    f'<b>Self-inverse:</b> if f{INV} = f, the graph of f is symmetrical about the line {y} = {x}.',
]

BARS = [
    ('Graph of an Inverse', 'reflect in y = x', 6, '#007ea2', 'Q 1 to 6'),
    ('Inverse of a Function', 'explain, find and sketch', 1, '#05ccab', 'Q 7'),
    ('Self-Inverse Functions', 'when f⁻¹ = f'.replace('⁻¹', INV), 1, '#05ccab', 'Q 8'),
]
BARS_TITLE = 'Concepts this exercise tests'
ALSO = ['One-One Functions · Q 7 a', 'Domain and Range · Q 2, 6', 'Square Root Function · Q 2, 3, 5, 7', 'Exponential Function · Q 4',
        'Rational Function · Q 8']

ROUTINE = [('SKETCH', 'Draw f, marking its end points and where it meets the axes.'),
           ('DASH', f'Draw the line {y} = {x} lightly.'),
           ('SWAP', 'Swap the coordinates of each key point.'),
           ('REFLECT', f'Join the new points as the mirror image of f.')]
WATCH_SUB = 'Swap x and y for every key point, including the end points.'
WATCH = [
    ('Q 1, 2, 6', f'Reflect the end points too: f{INV} stops where f stops.', f'An end point (4, 1) on f gives (1, 4) on f{INV}.'),
    ('Q 3, 5', 'The inverse of a squared graph is a square-root graph.', f'{y} = {x}<sup>2</sup> for {x} {GE} 0 reflects to {y} = {rt(x)}.'),
    ('Q 4', f'2<sup>{x}</sup> never reaches 0, so its inverse never reaches the {y}-axis.', f'The reflected curve gets close to the {y}-axis but does not touch it.'),
    ('Q 7 a', 'Explain with one-one: a turning point inside the domain stops f having an inverse.', f'{x}<sup>2</sup> for {x} {GE} 0 has an inverse; for {XR} it does not.'),
    ('Q 8 b', f'If f{INV} = f, reflecting the graph in {y} = {x} gives the same graph.', f'{y} = {fr("1", x)} for {x} {NE} 0 (coursebook page 19).'),
]
TRYONE = dict(
    q=f'<b>f({x}) = {x} + 2 for 0 {LE} {x} {LE} 3.</b> On the same axes, sketch {y} = f({x}) and {y} = f{INV}({x}), showing where they meet the coordinate axes.',
    opts=[], write=AXES,
    hints=[('Starter', 'Begin with f: a straight line from (0, 2) to (3, 5).'),
           ('Translator', f'Swap the coordinates of each end point to get the end points of f{INV}.'),
           ('Roots', f'Ask why the two lines are mirror images in {y} = {x}.')],
    turn=f'Draw f{INV} and label where it meets the {x}-axis.',
)
BEFORE = 'Read Section 1.7 of the coursebook: the note on reflections in y = x, self-inverse functions and Worked example 9.'
AHEAD = 'Q 8 asks you to explain a symmetry. Find f⁻¹ first, then compare it with f.'.replace('⁻¹', INV)

SK = {
    'Bridge': 'connect to everyday life', 'Starter': 'decide how to begin', 'Slicer': 'break it into small parts',
    'Echo': 'say it in your own words', 'Vault': 'pick what you already know', 'Roots': 'ask why it works',
    'Translator': 'turn words into numbers, pictures or steps'}
SQ = {
    'Bridge': 'What does this remind me of from my everyday life?', 'Starter': 'Where do I begin? Which clue is the easiest to use first?',
    'Slicer': 'Can I break this into small steps and solve one step at a time?', 'Echo': 'Can I say this question again in my own words?',
    'Vault': 'What do I already know that can help me here?', 'Roots': 'Why does this work? What is the rule hiding behind it?',
    'Translator': 'Can I turn the words into numbers, a drawing or a list of steps?'}

def same_axes(fn, var='x', word='meet'):
    return (f'On the same axes, sketch the graphs of {y} = {fn}({x}) and {y} = {fn}{INV}({x}), showing the coordinates of any points where the '
            f'{"curves" if word else "lines"} {word or "intersect"} the coordinate axes.')
Q = [
 dict(n=1, text='On a copy of the grid, draw the graph of the inverse of the function f.', fig=[('ex7_q1', 175)], write='The inverse passes through:',
      dyna=[('Translator', 'Read two points on f, such as its two end points, and swap their coordinates.'),
            ('Bridge', f'Think of a mirror standing along the line {y} = {x}: every point on f has its reflection on the other side.')],
      turn='Plot the swapped points and join them with a ruler.'),
 dict(n=2, text='On a copy of the grid, draw the graph of the inverse of the function g.', fig=[('ex7_q2', 175)], write='The inverse passes through:',
      dyna=[('Vault', f'Recall: the domain of g{INV} is the range of g. Read the range of g from the graph.'),
            ('Slicer', f'Reflect three points: the start, the point on the {y}-axis and the end. Then join them with a smooth curve.')],
      turn='Draw the curve and label it.'),
 dict(n=3, text=f'f({x}) = {x}<sup>2</sup> + 3, {x} {GE} 0.<br>' + same_axes('f', word='meet'), write=AXES,
      dyna=[('Starter', f'Begin with f: its lowest point is at {x} = 0. Then reflect the curve in {y} = {x}.'),
            ('Echo', f'Say it: “f{INV} is the mirror image of f in the line {y} = {x}.”')],
      turn='Mark and label the two points on the axes.'),
 dict(n=4, text=f'g({x}) = 2<sup>{x}</sup> for {XR}.<br>' + same_axes('g', word='intersect'), write=AXES,
      dyna=[('Roots', f'Ask why 2<sup>{x}</sup> never meets the {x}-axis. What does that mean for the reflected curve and the {y}-axis?'),
            ('Translator', f'Plot (−1, ½), (0, 1), (1, 2) and (2, 4) for g, then swap each pair for g{INV}.')],
      turn='Sketch both curves and label the axis points.'),
 dict(n=5, text=f'g({x}) = {x}<sup>2</sup> − 1 for {x} {GE} 0.<br>' + same_axes('g', word='intersect'), write=AXES,
      dyna=[('Slicer', f'Find where g meets each axis, then swap those coordinates for g{INV}.'),
            ('Vault', 'Recall Q 3: the same shape, 4 units lower.')],
      turn='Write all four points on the axes.'),
 dict(n=6, text=f'f({x}) = 4{x} − 2 for −1 {LE} {x} {LE} 3.<br>' + same_axes('f', word=None).replace('lines intersect', 'lines intersect'), write=AXES,
      dyna=[('Starter', f'Begin with the end points: put {x} = −1 and {x} = 3 into f.'),
            ('Roots', 'Ask why the inverse of a straight line is also a straight line.')],
      turn='Draw both lines with their end points and label the axis points.'),
 dict(n=7, text=f'The function f is defined by f : {x} {MAP} 3 − ({x} + 1)<sup>2</sup> for {x} {GE} −1.', cols=1,
      parts=[('a', 'Explain why f has an inverse.', 'Reason:'), ('b', f'Find an expression for f{INV} in terms of {x}.', f'f{INV}({x}) ='),
             ('c', f'On the same axes, sketch the graphs of {y} = f({x}) and {y} = f{INV}({x}), showing the coordinates of any points where the curves intersect the coordinate axes.', AXES)],
      dyna=[('Echo', f'Say a in words: “for {x} {GE} −1, does each output come from only one input?”'),
            ('Slicer', 'Do a, b, c in order. In c, swap the coordinates of the points on f to find the points on f⁻¹.'.replace('⁻¹', INV))],
      turn='Answer a and b, then sketch c.'),
 dict(n=8, text=f'<b>CHALLENGE QUESTION</b><br>f : {x} {MAP} {fr("2" + x + " + 7", x + " − 2")} for {x} {NE} 2', cols=1,
      parts=[('a', f'Find f{INV} in terms of {x}.', f'f{INV}({x}) ='), ('b', f'Explain what this implies about the symmetry of the graph of {y} = f({x}).', 'Symmetry:')],
      dyna=[('Translator', f'Use the three steps from Section 1.6 to find f{INV}({x}).'),
            ('Bridge', 'If a picture looks the same in a mirror, it is symmetrical about the mirror line. Compare your answer with f.')],
      turn='Write f⁻¹(x), then explain the symmetry.'.replace('⁻¹', INV)),
]
SPOT = None

# Supplementary (Atul's rules, 26 Nov 2026): only bank questions within the scope of the coursebook text before the
# exercise (Section 1.7: the graphs of f and f^-1 are reflections in y = x; self-inverse functions; with Sections 1.1 to 1.6
# before it) and of comparable hardness. Fewer than 10 is fine.
# Banks: "Relation and Functions Obj" (47830, 91621).
# Wording and options exactly as in the bank; Q-IDs read from the report pages.
# Bank answers (never printed), each checked by hand: 47830 D (reflection in y = x gives f^-1(x) = sqrt(x) - 1, x >= 0 ~ Q 3, 7),
# 91621 A ((1 - x)/(1 + x) is its own inverse ~ Q 8; options b and c use logs and powers, but a can be checked directly).
# Left out: duplicates of 47830 (73375, 80335, 91725); 73374 (self-inverse, already in Exercise 1.3); 21465 (already in 1.6);
# 91598 (needs (-1)^(x-1) on N, outside the scope); symmetry questions about x = 1 or x = 2 (50546, 64581, 73358: not taught).
SUPP = [
 dict(n=1, qid='47830', text=f'Suppose f(x) = (x + 1)<sup>2</sup> for x {GE} − 1. If g (x) is the function whose graph is the reflection of the graph of f(x) with respect to the line y = x, then g(x) equals:',
      opts=['−√x − 1, x ≥ 0', fr('1', '(x + 1)<sup>2</sup>') + ', x &gt; −1', rt('x + 1') + ', x ≥ −1', '√x − 1, x ≥ 0'], raw=True,
      hint=[('Roots', 'Reflecting a graph in y = x gives the graph of the inverse. Ask why g must be f⁻¹.'.replace('⁻¹', INV)),
            ('Starter', 'Begin with y = (x + 1)<sup>2</sup>, interchange x and y, and keep the square root that fits y ≥ −1.')]),
 dict(n=2, qid='91621', text='Which of the following functions is inverse of itself -',
      opts=['f (x) = ' + fr('1 − x', '1 + x'), 'g (x) = 5<sup>log x</sup>', 'h (x) = 2<sup>x (x−1)</sup>', 'None of these'], raw=True,
      hint=[('Slicer', 'Test option a first: find its inverse with the three steps and compare it with the function itself.'),
            ('Echo', 'Say it: “inverse of itself” means f⁻¹ = f, so its graph is symmetrical about y = x.'.replace('⁻¹', INV))]),
]

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1], True, 'space'), ('questions', [2, 3], False, 'space'), ('questions', [4, 5, 6], False, 'space'),
    ('questions', [7, 8], False, 'spaceqr'),
    ('supp', [1, 2], True, 'howdid+space'),
]
