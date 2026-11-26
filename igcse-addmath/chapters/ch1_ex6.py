"""Cambridge IGCSE & O Level Additional Mathematics, Chapter 1: Functions, Exercise 1.6 (inverse functions).
Source exercise: Cambridge IGCSE & O Level Additional Mathematics Coursebook, Chapter 1, Exercise 1.6 (pp. 17-18).
Answers (checked by hand and with SymPy, never printed):
Q1 f^-1(x) = sqrt(x + 7) - 5. Q2 f^-1(x) = 6/x - 2. Q3 f^-1(x) = (3 + sqrt(x - 1))/2. Q4 f^-1(x) = (8 - x)^2 + 3.
Q5 f^-1(x) = (x + 3)/5, g^-1(x) = 2 - 7/x. Q6 a f^-1(x) = sqrt(x + 5) - 2, b x = 20.
Q7 a f^-1(x) = 4 + sqrt(x - 5), b f(0) = 21 so x = 294. Q8 a g^-1(x) = (x + 3)/(x - 2), b x = 13/4.
Q9 a f^-1(x) = 2x - 4, b fg(x) = (x^2 - 2x)/2 + 2 = 2x - 4 gives x^2 - 6x + 12 = 0: discriminant -12, so no real solutions.
Q10 g^-1(17) = 7, gf(x) = 2x^2 + 7, so x = 0. Q11 g^-1(x) = 2x + 3; 2x^2 - 3x - 14 = 0, x = -2 or x = 3.5.
Q12 f^-1(x) >= 0. Q13 x -> x^2 - 6 is f^-1 g^-1. Q14 f and h have inverses (g is many-one: g(0) = g(3) = 3).
Q15 a x >= 2, b g^-1(x) >= 0. Q16 a f^-1(x) = (x + k)/3, g^-1(x) = (x + 14)/(5 - x); b k = 13; c g^-1 g(x) = x.
Q17 a f^-1 g, b g^-1 f, c g f^-1, d f^-1 g^-1.
Supplementary: see the SUPP comment below (answers never printed)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_class'))
from glyphs_svg import MAP, TO, IN, R, sym

x = '<i>x</i>'; y = '<i>y</i>'
def fr(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'
def md(e):
    return f'<span class="mod"><span>{e}</span></span>'
def rt(e):
    return f'√<span style="text-decoration:overline">{e}</span>'
LE = '≤'; GE = '≥'; NE = '≠'
INV = '<sup>−1</sup>'
FI = f'f{INV}({x}) ='; GI = f'g{INV}({x}) ='
XR = f'{x} {IN} {R}'

CH = dict(
    num=1, title='Functions', first_page=54, exercise='Exercise 1.6',
    subject='Cambridge IGCSE &amp; O Level Additional Mathematics',
    lecture_qr=None, dyna_qr='CGN000024',   # lecture QR not issued yet (placeholder); CGN000024 = Chapter 1 Cognoo pathway
    count_line='Exercise 1.6 · 17 questions · Inverse functions · Goes with Chapter 1 of your Additional Mathematics Coursebook',
)

KNOW = [
    f'<b>Inverse:</b> f{INV} undoes what f does. It exists only if f is a one-one function.',
    f'<b>Swap:</b> the domain of f{INV} is the range of f; the range of f{INV} is the domain of f.',
    f'<b>Three steps:</b> write {y} = f({x}), interchange {x} and {y}, then make {y} the subject.',
    f'<b>Check:</b> a solution of f{INV}({x}) = … must lie in the domain of f{INV} (Worked example 8).',
]

BARS = [
    ('Inverse of a Function', 'find the inverse', 8, '#007ea2', 'Q 1 to 8'),
    ('Composite Function', 'built with inverses', 6, '#05ccab', 'Q 9, 10, 11, 13, 16, 17'),
    ('Domain and Range', 'of an inverse', 2, '#05ccab', 'Q 12, 15'),
    ('One-One Functions', 'which have an inverse', 1, '#05ccab', 'Q 14'),
]
BARS_TITLE = 'Concepts this exercise tests'
ALSO = ['Square Root Function · Q 1, 3, 4, 6, 7', 'Rational Function · Q 2, 5, 8, 11, 16', 'Extraneous Roots · Q 6 b, 7 b, 8 b, 11',
        'Solution of Quadratic Equations · Q 9, 11', 'Modulus Function · Q 14']

ROUTINE = [('WRITE', f'Write {y} = f({x}).'),
           ('SWAP', f'Interchange {x} and {y}.'),
           ('SOLVE', f'Rearrange to make {y} the subject.'),
           ('CHECK', 'Is every answer in the right domain?')]
WATCH_SUB = 'The domain decides which square root and which answers to keep.'
WATCH = [
    ('Q 1, 3, 6, 7', 'When you take a square root, keep the sign the domain allows.', f'{x} {GE} −5 means {x} + 5 {GE} 0, so use the + root.'),
    ('Q 2, 5, 8, 11', f'With a fraction, multiply out first, then collect every {y} term on one side.', f'{x} = {fr("4", y + " + 1")} gives {y} + 1 = {fr("4", x)}.'),
    ('Q 7 b, 10', f'f(0) and g{INV}(17) are numbers. Work them out first.', f'Then solve f{INV}({x}) = that number.'),
    ('Q 12, 15', 'Domain and range swap places for the inverse.', f'f({x}) = {x} + 1, {x} {GE} 0 has range f({x}) {GE} 1, so f{INV} has domain {x} {GE} 1.'),
    ('Q 14', 'Only one-one functions have an inverse.', f'{md(x)} for −1 {LE} {x} {LE} 1 has no inverse: −1 and 1 share the output 1.'),
]
TRYONE = dict(
    q=f'<b>Find</b>&nbsp; f{INV}({x})&nbsp; for f({x}) = 3{x} + 4, {XR}.',
    opts=[], write=FI,
    hints=[('Echo', f'Say what f does: “times 3, then add 4”. The inverse undoes these steps in reverse order.'),
           ('Starter', f'Begin with step 1: write {y} = 3{x} + 4. Then interchange {x} and {y}.'),
           ('Translator', f'Rearrange {x} = 3{y} + 4 to make {y} the subject.')],
    turn=f'Check your answer: does f{INV}(f(2)) give 2?',
)
BEFORE = 'Read Section 1.6 of the coursebook: the three steps for finding an inverse, the class discussion on x², and Worked example 8.'
AHEAD = 'Q 17 uses f, g, f<sup>−1</sup> and g<sup>−1</sup> together. Read each rule as a chain of steps, then match each step to a function.'

SK = {
    'Bridge': 'connect to everyday life', 'Starter': 'decide how to begin', 'Slicer': 'break it into small parts',
    'Echo': 'say it in your own words', 'Vault': 'pick what you already know', 'Roots': 'ask why it works',
    'Translator': 'turn words into numbers, pictures or steps'}
SQ = {
    'Bridge': 'What does this remind me of from my everyday life?', 'Starter': 'Where do I begin? Which clue is the easiest to use first?',
    'Slicer': 'Can I break this into small steps and solve one step at a time?', 'Echo': 'Can I say this question again in my own words?',
    'Vault': 'What do I already know that can help me here?', 'Roots': 'Why does this work? What is the rule hiding behind it?',
    'Translator': 'Can I turn the words into numbers, a drawing or a list of steps?'}

FIND = f'Find an expression for f{INV}({x}).'
Q = [
 dict(n=1, text=f'f({x}) = ({x} + 5)<sup>2</sup> − 7 for {x} {GE} −5. {FIND}', write=FI,
      dyna=[('Vault', f'Use the three steps: write {y} = …, interchange {x} and {y}, then make {y} the subject.'),
            ('Roots', f'Ask why you keep only the + square root: {x} {GE} −5 means {x} + 5 is never negative.')],
      turn=f'Write f{INV}({x}).'),
 dict(n=2, text=f'f({x}) = {fr("6", x + " + 2")} for {x} {GE} 0. {FIND}', write=FI,
      dyna=[('Starter', f'Begin with {y} = {fr("6", x + " + 2")}, then interchange {x} and {y}.'),
            ('Translator', f'Multiply both sides by ({y} + 2) to clear the fraction, then get {y} on its own.')],
      turn=f'Write f{INV}({x}).'),
 dict(n=3, text=f'f({x}) = (2{x} − 3)<sup>2</sup> + 1 for {x} {GE} 1.5. {FIND}', write=FI,
      dyna=[('Slicer', 'After swapping, undo one step at a time: subtract 1, take the square root, add 3, divide by 2.'),
            ('Roots', f'Ask why {x} {GE} 1.5 lets you use the + root: 2{x} − 3 is not negative there.')],
      turn=f'Write f{INV}({x}).'),
 dict(n=4, text=f'f({x}) = 8 − {rt(x + " − 3")} for {x} {GE} 3. {FIND}', write=FI,
      dyna=[('Echo', f'Say f in words: “start at 8 and take away the square root of {x} − 3”.'),
            ('Slicer', 'After swapping, get the square root on its own first, then square both sides.')],
      turn=f'Write f{INV}({x}).'),
 dict(n=5, text=f'f : {x} {MAP} 5{x} − 3&nbsp; for {x} &gt; 0<br>g : {x} {MAP} {fr("7", "2 − " + x)}&nbsp; for {x} {NE} 2<br>Express f{INV}({x}) and g{INV}({x}) in terms of {x}.',
      parts=[('', '', FI), ('', '', GI)], cols=1,
      dyna=[('Translator', 'Find each inverse on its own with the three steps.'),
            ('Bridge', 'Like walking back home along the same road: undo the last step first.')],
      turn='Write both inverses.'),
 dict(n=6, text=f'f : {x} {MAP} ({x} + 2)<sup>2</sup> − 5 for {x} &gt; −2',
      parts=[('a', f'Find an expression for f{INV}({x}).', FI), ('b', f'Solve the equation f{INV}({x}) = 3.', 'x =')], cols=1,
      dyna=[('Vault', f'Part a is like Q 1. For b, set your f{INV}({x}) equal to 3.'),
            ('Starter', 'Begin b by getting the square root on its own, then square both sides.')],
      turn='Solve b and check the answer in your f<sup>−1</sup>(x).'),
 dict(n=7, text=f'f({x}) = ({x} − 4)<sup>2</sup> + 5 for {x} &gt; 4',
      parts=[('a', f'Find an expression for f{INV}({x}).', FI), ('b', f'Solve the equation f{INV}({x}) = f(0).', 'x =')], cols=1,
      dyna=[('Echo', f'Say b in words: “which {x} does f{INV} send to the same number as f(0)?”'),
            ('Slicer', 'Two steps: work out f(0) with the formula, then solve f<sup>−1</sup>(x) = that number.')],
      turn='Find f(0), then solve.'),
 dict(n=8, text=f'g({x}) = {fr("2" + x + " + 3", x + " − 1")} for {x} &gt; 1',
      parts=[('a', f'Find an expression for g{INV}({x}).', GI), ('b', f'Solve the equation g{INV}({x}) = 5.', 'x =')], cols=1,
      dyna=[('Translator', f'After swapping, multiply out {x}({y} − 1), collect every {y} term on one side and factorise.'),
            ('Roots', f'Ask why your answer to b must be greater than 2: the domain of g{INV} is the range of g.')],
      turn='Write g<sup>−1</sup>(x), then solve b.'),
 dict(n=9, text=f'f({x}) = {fr(x, "2")} + 2&nbsp; for {XR}<br>g({x}) = {x}<sup>2</sup> − 2{x}&nbsp; for {XR}',
      parts=[('a', f'Find f{INV}({x}).', FI), ('b', f'Solve fg({x}) = f{INV}({x}).', 'x =')], cols=1,
      dyna=[('Slicer', f'Find f{INV}({x}) first. Then write fg({x}) as one expression and set the two equal.'),
            ('Vault', 'Recall b² − 4ac: check it before you try to factorise the quadratic you get.')],
      turn='Write what you find for b.'),
 dict(n=10, text=f'f({x}) = {x}<sup>2</sup> + 2&nbsp; for {XR}<br>g({x}) = 2{x} + 3&nbsp; for {XR}<br>Solve the equation gf({x}) = g{INV}(17).', write='x =',
      dyna=[('Starter', 'Begin with the number on the right: g<sup>−1</sup>(17) asks “which input gives g an output of 17?”'),
            ('Translator', f'Write gf({x}) as one expression, then set it equal to that number.')],
      turn='Solve for x.'),
 dict(n=11, text=f'f : {x} {MAP} {fr("2" + x + " + 8", x + " − 2")}&nbsp; for {x} {NE} 2<br>g : {x} {MAP} {fr(x + " − 3", "2")}&nbsp; for {x} &gt; −5<br>Solve the equation f({x}) = g{INV}({x}).', write='x =',
      dyna=[('Vault', f'Find g{INV}({x}) first with the three steps.'),
            ('Slicer', f'Set f({x}) = g{INV}({x}), multiply by ({x} − 2), rearrange into a quadratic and solve. Check each root.')],
      turn='Write the solutions that pass your check.'),
 dict(n=12, text=f'f({x}) = 3{x} − 24 for {x} {GE} 0. Write down the range of f{INV}.', write=f'Range of f{INV}:',
      dyna=[('Roots', f'Ask why the range of f{INV} is the domain of f.'),
            ('Echo', f'Say it: “f{INV} gives back the inputs that f used.”')],
      turn='Write the range.'),
 dict(n=13, text=f'f : {x} {MAP} {x} + 6&nbsp; for {x} &gt; 0<br>g : {x} {MAP} {rt(x)}&nbsp; for {x} &gt; 0<br>Express {x} {MAP} {x}<sup>2</sup> − 6 in terms of f and g.',
      write=f'{x} {MAP} {x}<sup>2</sup> − 6 is',
      dyna=[('Bridge', f'Like a recipe read backwards: {x}<sup>2</sup> − 6 means “square, then subtract 6”. Which inverses do those two steps?'),
            ('Starter', f'Begin by finding f{INV}({x}) and g{INV}({x}).')],
      turn='Put them in the right order.'),
 dict(n=14, text=(f'f : {x} {MAP} 3 − 2{x}&nbsp; for 0 {LE} {x} {LE} 5<br>g : {x} {MAP} {md("3 − 2" + x)}&nbsp; for 0 {LE} {x} {LE} 5<br>'
                  f'h : {x} {MAP} 3 − {md("2" + x)}&nbsp; for 0 {LE} {x} {LE} 5<br>State which of the functions f, g and h has an inverse.'),
      write='Has an inverse:',
      dyna=[('Translator', f'Sketch each graph for 0 {LE} {x} {LE} 5.'),
            ('Roots', 'Ask which graphs pass the horizontal line test: only one-one functions have an inverse.')],
      turn='Name the functions that have an inverse.'),
 dict(n=15, text=f'f({x}) = {x}<sup>2</sup> + 2&nbsp; for {x} {GE} 0<br>g({x}) = 5{x} − 4&nbsp; for {x} {GE} 0',
      parts=[('a', f'Write down the domain of f{INV}.', f'Domain of f{INV}:'), ('b', f'Write down the range of g{INV}.', f'Range of g{INV}:')], cols=1,
      dyna=[('Echo', f'Say a in words: “the inputs of f{INV} are the outputs of f.”'),
            ('Vault', f'The domain of f{INV} is the range of f; the range of g{INV} is the domain of g.')],
      turn='Write both answers.'),
 dict(n=16, text=f'The functions f and g are defined, for {XR}, by<br>f : {x} {MAP} 3{x} − <i>k</i>, where <i>k</i> is a positive constant<br>g : {x} {MAP} {fr("5" + x + " − 14", x + " + 1")} where {x} {NE} −1.', cols=1,
      parts=[('a', f'Find expressions for f{INV} and g{INV}.', f'f{INV}({x}), g{INV}({x}):'), ('b', f'Find the value of <i>k</i> for which f{INV}(5) = 6.', 'k ='),
             ('c', f'Simplify g{INV}g({x}).', f'g{INV}g({x}) =')],
      dyna=[('Slicer', f'Do a, b, c in order: b uses your f{INV} from a.'),
            ('Roots', 'For c, ask what happens when you do g and then undo it.')],
      turn='Answer a, b and c.'),
 dict(n=17, text=f'f : {x} {MAP} {x}<sup>3</sup>&nbsp; for {XR}&nbsp;&nbsp;&nbsp;&nbsp;g : {x} {MAP} {x} − 8&nbsp; for {XR}<br>Express each of the following as a composite function, using only f, g, f{INV} and/or g{INV}:',
      part_label='As a composite:',
      parts=[('a', f'{x} {MAP} ({x} − 8)<sup>1/3</sup>'), ('b', f'{x} {MAP} {x}<sup>3</sup> + 8'), ('c', f'{x} {MAP} {x}<sup>1/3</sup> − 8'), ('d', f'{x} {MAP} ({x} + 8)<sup>1/3</sup>')],
      dyna=[('Translator', 'Write each rule as steps in order, for example a: “subtract 8, then take the cube root”.'),
            ('Bridge', 'Like putting on socks, then shoes: the order of the functions matters.')],
      turn='Write each composite, with the function that acts first on the right.'),
]
SPOT = None

# Supplementary (Atul's rules, 26 Nov 2026): only bank questions within the scope of the coursebook text before the
# exercise (Section 1.6: an inverse exists only for a one-one function; domain and range swap; the three steps for finding
# f^-1(x); solving with f^-1; with Sections 1.1 to 1.5 before it) and of comparable hardness. Fewer than 10 is fine.
# Banks: "Relation and Functions Obj" (47840, 73190) and "1_Functions_Obj" (73363, 74254, 21465).
# Wording and options exactly as in the bank; Q-IDs read from the report pages.
# Bank answers (never printed), each checked by hand, with the coursebook question it matches:
# 47840 B ((x + 5)/3 ~ Q 5), 73363 C ((y - 3)/4 ~ Q 5), 74254 B (gof = identity, so g = f^-1 = x - 2 ~ Q 16 c),
# 73190 A ((3x - 2)/(x - 1) ~ Q 8), 21465 D (f is its own inverse ~ Q 8, 16).
# Left out: graph reflections in y = x (47830, 73375, 80335, 91725: Section 1.7), inverses of exponential, log, trig or
# greatest-integer functions (47838, 73367, 47694, 64586, 32193, 85416, 85417, 73188), 85412 (needs "strictly monotonic and
# continuous"), 47833 / 80331 (x + 1/x needs the quadratic formula; harder), 64589 (modulus, harder), relation inverses (88748).
SUPP = [
 dict(n=1, qid='47840', text='If f(x) = 3x − 5, then f<sup>−1</sup> (x) is given by',
      opts=[fr('1', '3x − 5'), fr('x + 5', '3'), 'does not exist because f is not one-one', 'does not exist because f is not onto'], raw=True,
      hint=[('Starter', 'Begin with y = 3x − 5, then interchange x and y.'),
            ('Echo', 'Say what f does: “times 3, then subtract 5”. The inverse undoes it in reverse order.')]),
 dict(n=2, qid='73363', text=f'Let f : N {TO} Y be a function defined as f(x) = 4x + 3 where Y = {{y {IN} N : y = 4x + 3 for some x {IN} N}}. Show that f is invertible and its inverse is',
      opts=['g(y) = 4 + ' + fr('y + 3', '4'), 'g(y) = ' + fr('y + 3', '4'), 'g(y) = ' + fr('y − 3', '4'), 'g(y) = ' + fr('3y + 4', '3')], raw=True,
      hint=[('Translator', 'Write y = 4x + 3 and make x the subject. That gives g(y).'),
            ('Vault', 'Recall: a one-one function has an inverse, and 4x + 3 never gives the same output twice.')]),
 dict(n=3, qid='74254', text=f'If f : Z {TO} Z, f = x + 2 and g : Z {TO} Z with gof = I<sub>Z</sub>, then g is',
      opts=['x + 2', 'x − 2', 'x − 1', 'x + 1'],
      hint=[('Bridge', 'Like a lift that goes up 2 floors: which trip brings you back to where you started?'),
            ('Roots', 'I<sub>Z</sub> means every x is mapped to itself. Ask why g must then undo f.')]),
 dict(n=4, qid='73190', text=f'f : R − {{3}} {TO} R − {{1}} defined by f(x) = {fr("x − 2", "x − 3")}. f<sup>−1</sup> is equal to',
      opts=[fr('3x − 2', 'x − 1'), fr('x − 1', '3x − 2'), fr('x − 2', 'x − 3'), 'Does not exist'], raw=True,
      hint=[('Slicer', 'Interchange x and y, multiply both sides by (y − 3), then collect the y terms on one side.'),
            ('Vault', 'Recall coursebook Q 8: the same steps work for any fraction like this.')]),
 dict(n=5, qid='21465', text=f'For the function f(x) = {fr("5x + 3", "2x − 5")} which of the following holds?',
      opts=['f<sup>−1</sup>(x) = ' + fr('2x − 5', '5x + 3'), 'f<sup>−1</sup>(x) does not exist as f is non bijective', 'Domain of f is not same as range of f',
            'f<sup>−1</sup>(x) = ' + fr('5x + 3', '2x − 5')], raw=True,
      hint=[('Translator', 'After interchanging x and y, multiply out x(2y − 5) and gather the y terms on one side.'),
            ('Roots', 'Compare the f<sup>−1</sup>(x) you find with f(x). What do you notice?')]),
]

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1, 2], True, 'space'), ('questions', [3, 4, 5], False, 'space'), ('questions', [6, 7], False, 'space'),
    ('questions', [8, 9], False, 'space'), ('questions', [10, 11, 12], False, 'space'), ('questions', [13, 14], False, 'space'),
    ('questions', [15, 16], False, 'space'), ('questions', [17], False, 'spaceqr'),
    ('supp', [1, 2, 3], True, 'space'), ('supp', [4, 5], False, 'howdid+space'),
]
