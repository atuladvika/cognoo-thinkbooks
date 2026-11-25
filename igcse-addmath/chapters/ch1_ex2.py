"""JEE Main Mathematics, Chapter 1: Functions, Exercise 1.2 (definition of a function, domain and range).
Source exercise: Cambridge IGCSE & O Level Additional Mathematics Coursebook, Chapter 1, Exercise 1.2 (p. 5).
Answers (checked by hand, never printed):
Q1 mappings 1 to 7 of Exercise 1.1 are functions (8 is one-many, not a function).
Q2 a −7 ≤ f(x) ≤ 2; b 2 ≤ f(x) ≤ 17; c −1 ≤ f(x) ≤ 9; d 0 ≤ f(x) ≤ 9; e 1/8 ≤ f(x) ≤ 8; f 1/5 ≤ f(x) ≤ 1.
Q3 g(x) ≥ 2; Q4 f(x) ≥ −4; Q5 f(x) ≥ 5; Q6 f(x) ≥ −5; Q7 −6 ≤ f(x) ≤ 10; Q8 f(x) ≥ 3.
Supplementary (bank answers, never printed): 142505 C, 74865 B, 142929 B, 74647 C, 74646 D, 74648 C,
91584 B, 73357 D, 91617 C, 91719 D."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_class'))
from glyphs_svg import MAP, TO, IN, R, sym
IFF = sym('\u21d4')
TH = sym('\u03b8', 0.95)
PI = sym('\u03c0', 0.95)

x = '<i>x</i>'
f_ = 'f'
def fr(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'
def mx(s):
    return f'<span class="mx">{s}</span>'
SQ2 = lambda e: f'√<span style="text-decoration:overline">{e}</span>'
LE = '≤'; GE = '≥'

CH = dict(
    num=1, title='Functions', first_page=18, exercise='Exercise 1.2',
    subject='Cambridge IGCSE &amp; O Level Additional Mathematics',
    lecture_qr=None, dyna_qr=None,   # QR Manager codes not issued yet: placeholders are printed
    count_line='Exercise 1.2 · 8 questions (Q 2 has 6 parts) · Definition of a function, domain and range · Goes with Chapter 1 of your Additional Mathematics Coursebook',
)

KNOW = [
    '<b>Function:</b> each input has exactly one output. One-one and many-one mappings are functions; one-many is not.',
    f'<b>Domain and range:</b> the inputs and the outputs. For f({x}) = 2{x}, 1 {LE} {x} {LE} 3, the range is 2 {LE} f({x}) {LE} 6.',
    f'<b>Completing the square:</b> {x}<sup>2</sup> − 6{x} + 11 = ({x} − 3)<sup>2</sup> + 2. A square is never negative.',
    '<b>Rising or falling:</b> if a graph only rises (or only falls) on an interval, its end points give the smallest and largest outputs.',
]

BARS = [
    ('Greatest and Least Values', 'of a quadratic expression', 5, '#007ea2', 'Q 3, 4, 5, 6, 7'),
    ('Polynomial Functions', 'straight lines', 1, '#05ccab', 'Q 2 a–c'),
    ('Domain and Range', 'of different types of function', 1, '#05ccab', 'Q 2 d–f'),
    ('Definition of a Function', 'one output for each input', 1, '#05ccab', 'Q 1'),
    ('Square Root Function', 'the non-negative root', 1, '#05ccab', 'Q 8'),
]
BARS_TITLE = 'STCA concepts this exercise tests'
BARS_SUB = 'Main STCA concept of each of the 9 question blocks (Q 2 is split in two)'
ALSO = ['Domain and Range · Q 3 to 8', 'Quadratic Expression as Parabolic Curve · Q 2 d, 3, 4', 'Exponential Function · Q 2 e',
        'Rational Function · Q 2 f', 'One-One (Injective) Functions · Q 1']

ROUTINE = [('READ', 'Read the rule <b>and</b> the domain written after it.'),
           ('FIND', 'Find the turning point, if there is one, and the end points.'),
           ('SKETCH', 'Sketch only the part of the graph the domain allows.'),
           ('WRITE', f'Write the range using f({x}), not {x}.')]
WATCH_SUB = 'The smallest output is not always at an end point.'
WATCH = [
    ('Q 2 c', 'A <b>falling</b> line: the bigger input gives the smaller output.', f'Compare 7 − 2{x} at {x} = −1 and at {x} = 4.'),
    ('Q 2 d', 'The turning point may lie <b>inside</b> the interval.', f'For {x}<sup>2</sup>, check {x} = 0 as well as the two ends.'),
    ('Q 4, Q 5', f'Write the range in terms of <b>f({x})</b>.', f'“f({x}) {GE} …”, not “{x} {GE} …”.'),
    ('Q 6', 'See where the domain starts compared with the turning point.', f'2{x} + 1 = 0 when {x} = −½.'),
    ('Q 7', 'The two end points are <b>not</b> equally far from the top.', f'Compare {x} = 2 and {x} = 7 with {x} = 3.'),
]
TRYONE = dict(
    q=f'<b>Find the range of</b>&nbsp; f({x}) = ({x} − 2)<sup>2</sup> + 3 &nbsp;for {x} {GE} 0.',
    opts=[],
    hints=[('Echo', f'Say it in your own words: “A square, plus 3. Only {x} {GE} 0 is allowed.”'),
           ('Roots', f'Ask why a square helps: ({x} − 2)<sup>2</sup> is never negative. When is it exactly 0, and is that {x} allowed?'),
           ('Translator', f'Make a table for {x} = 0, 1, 2, 3, 4 and look for the smallest output.')],
    turn='Is there a smallest output? Is there a largest? Write the range.',
)
BEFORE = 'Read Section 1.2 of the coursebook: the definition of a function, domain and range, and Worked examples 1 and 2.'
AHEAD = 'Q 7 turns the curve upside down: a hill instead of a valley. Q 8 brings in a square root.'

SK = {
    'Bridge': 'connect to everyday life', 'Starter': 'decide how to begin', 'Slicer': 'break it into small parts',
    'Echo': 'say it in your own words', 'Vault': 'pick what you already know', 'Roots': 'ask why it works',
    'Translator': 'turn words into numbers, pictures or steps'}
SQ = {
    'Bridge': 'What does this remind me of from my everyday life?', 'Starter': 'Where do I begin? Which clue is the easiest to use first?',
    'Slicer': 'Can I break this into small steps and solve one step at a time?', 'Echo': 'Can I say this question again in my own words?',
    'Vault': 'What do I already know that can help me here?', 'Roots': 'Why does this work? What is the rule hiding behind it?',
    'Translator': 'Can I turn the words into numbers, a drawing or a list of steps?'}

def rng(rule, dom):
    return f'f({x}) = {rule},&nbsp;&nbsp; {dom}'

Q = [
 dict(n=1, text='Which of the mappings in <b>Exercise 1.1</b> are functions?', write='Mappings that are functions:',
      dyna=[('Vault', 'Recall the definition: a function gives each input <b>exactly one</b> output. One-one and many-one mappings pass this test; a one-many mapping does not.'),
            ('Slicer', 'Go back to your eight answers for Exercise 1.1. Sort them into two lists: “one output for each input” and “more than one output for an input”.')],
      turn='Write the numbers of the mappings in the first list.'),
 dict(n=2, label='Q 2 a–c', text='Find the range for each of these functions.',
      parts=[('a', rng(f'{x} − 5', f'−2 {LE} {x} {LE} 7')), ('b', rng(f'3{x} + 2', f'0 {LE} {x} {LE} 5')), ('c', rng(f'7 − 2{x}', f'−1 {LE} {x} {LE} 4'))],
      dyna=[('Bridge', f'Think of an auto fare: a fixed charge plus a rate per km. It is a straight line, so the cheapest and the dearest rides are at the shortest and longest trips. Does each line go up or down as {x} increases?'),
            ('Translator', 'Work out f at both end points of the interval. For a straight line, every output in between is also reached.')],
      turn=f'Write each range as “smallest {LE} f({x}) {LE} largest”. In part c, check which end gives the smaller value.'),
 dict(n=2, label='Q 2 d–f', text='Find the range for each of these functions (continued).',
      parts=[('d', rng(f'{x}<sup>2</sup>', f'−3 {LE} {x} {LE} 3')), ('e', rng(f'2<sup>{x}</sup>', f'−3 {LE} {x} {LE} 3')), ('f', rng(fr('1', x), f'1 {LE} {x} {LE} 5'))],
      dyna=[('Slicer', f'Treat each part on its own. First sketch the curve over its interval: a U-shape for {x}<sup>2</sup>, then 2<sup>{x}</sup>, then {fr("1", x)}.'),
            ('Roots', f'Ask where the smallest output really is. For {x}<sup>2</sup>, the bottom of the U lies inside the interval, not at an end. Do the other two curves ever turn?')],
      turn='Read the smallest and largest outputs from each sketch. Write the three ranges.'),
 dict(n=3, text=f'The function g is defined as g({x}) = {x}<sup>2</sup> + 2 for {x} {GE} 0.<br>Find the range of g.', write='Range of g:',
      dyna=[('Vault', f'You know {x}<sup>2</sup> is never negative. Here the domain starts at {x} = 0, the bottom of the U.'),
            ('Translator', f'Make a table for {x} = 0, 1, 2, 3. Is there a smallest output? Is there a largest?')],
      turn=f'Write the range using g({x}).'),
 dict(n=4, text=f'The function f is defined by f({x}) = {x}<sup>2</sup> − 4 for {x} {IN} {R}.<br>Find the range of f.', write='Range of f:',
      dyna=[('Echo', f'Say it: “every real {x} is allowed, negative ones too.” Do negative inputs give any outputs that positive inputs do not?'),
            ('Roots', f'Ask why there is a lowest point: which {x} makes {x}<sup>2</sup> as small as possible?')],
      turn=f'Work out the lowest output. Write the range using f({x}).'),
 dict(n=5, text=f'The function f is defined by f({x}) = ({x} − 1)<sup>2</sup> + 5 for {x} {GE} 1.<br>Find the range of f.', write='Range of f:',
      dyna=[('Roots', f'A square is never negative. When is ({x} − 1)<sup>2</sup> exactly 0, and is that {x} allowed here?'),
            ('Starter', f'Begin at the left end of the domain, {x} = 1. Then ask what happens to the output as {x} grows.')],
      turn='Find the smallest output. Write the range.'),
 dict(n=6, text=f'The function f is defined by f({x}) = (2{x} + 1)<sup>2</sup> − 5 for {x} {GE} −{fr("1", "2")}.<br>Find the range of f.', write='Range of f:',
      dyna=[('Translator', f'Find the {x} that makes the bracket 2{x} + 1 equal to 0. Compare it with where the domain starts.'),
            ('Vault', 'Use what you did in Q 5: the smallest value of the square gives the smallest output.')],
      turn='Write the smallest output, then the range.'),
 dict(n=7, text=f'The function f is defined by f : {x} {MAP} 10 − ({x} − 3)<sup>2</sup> for 2 {LE} {x} {LE} 7.<br>Find the range of f.', write='Range of f:',
      dyna=[('Bridge', 'Think of a ball thrown upwards: it rises to a highest point, then falls. 10 − (x − 3)<sup>2</sup> behaves the same way, a hill, not a valley.'),
            ('Slicer', f'Step 1: find the top of the hill (when is the square 0?). Step 2: work out the outputs at {x} = 2 and at {x} = 7. Which end goes lower?')],
      turn='Write the range from the lowest output to the highest.'),
 dict(n=8, text=f'The function f is defined by f({x}) = 3 + {SQ2(f"{x} − 2")} for {x} {GE} 2.<br>Find the range of f.', write='Range of f:',
      dyna=[('Vault', '√ means the non-negative square root, so the root part is never below 0.'),
            ('Translator', f'Make a table: {x} = 2, 3, 6, 11. Watch how the outputs grow.')],
      turn='Find the smallest output. Does the output have a largest value? Write the range.'),
]
SPOT = None

# Supplementary: 10 questions from the i2K / Dynamind bank "Relation and Functions Obj" (Engg/Med Entrance),
# wording and options as in the bank, Q-IDs read from the report.
th = TH
SUPP = [
 dict(n=1, qid='142505', text='Which of the following relation is a function ?',
      opts=['{(1,4), (2,6), (1,5), (3,9)}', '{(3,3), (2,1), (1,2), (2,3)}', '{(1,2), (2,2), (3,2), (4,2)}', '{(3,1), (3,2), (3,3), (3,4)}'], hint=['Vault', 'Slicer']),
 dict(n=2, qid='74865', text=f'If f(x) = |x − 3| + 2 then f(−1) =', opts=['2', '6', '−6', '0'], hint=['Translator', 'Echo']),
 dict(n=3, qid='142929', text=f'If f(x) = {fr("2x", "1 − x<sup>2</sup>")}, then f (tan {th}) equals-',
      opts=[f'cot 2{th}', f'tan 2{th}', f'sec 2{th}', f'cos 2{th}'], raw=True, hint=['Translator', 'Vault']),
 dict(n=4, qid='74647', text='Let <i>R</i> be a relation on <i>N</i> defined by x + 2y = 8. The domain of <i>R</i> is',
      opts=['{2, 4, 8}', '{2, 4, 6, 8}', '{2, 4, 6}', '{1, 2, 3, 4}'], hint=['Starter', 'Slicer']),
 dict(n=5, qid='74646', text=f'A relation <i>R</i> is defined from {{2, 3, 4, 5}} to {{3, 6, 7, 10}} by <i>xRy</i> {IFF} <i>x</i> is relatively prime to <i>y</i>.Then domain of <i>R</i> is',
      opts=['{2, 3, 5}', '{3, 5}', '{2, 3, 4}', '{2, 3, 4, 5}'], hint=['Echo', 'Slicer']),
 dict(n=6, qid='74648', text=f'If <i>R</i> = {{(x, y)| x, y {IN} <i>Z</i>, x<sup>2</sup> + y<sup>2</sup> {LE} 4}} is a relation in <i>Z</i>, then domain of <i>R</i> is',
      opts=['{0, 1, 2}', '{0, −1, −2}', '{−2, −1, 0, 1, 2}', 'None of these'], hint=['Translator', 'Slicer']),
 dict(n=7, qid='91584', text=f'The function f : [2, ∞) {TO} Y defined by f(x) = x<sup>2</sup> − 4x + 5 is both one-one &amp; onto if :',
      opts=['Y = R', 'Y = [1, ∞)', 'Y = [4, ∞)', 'Y = [5, ∞)'], hint=['Vault', 'Roots']),
 dict(n=8, qid='73357', text=f'If f : R {TO} S, defined by f(x) = sin x − √3 cos x + 1, is onto, then the interval of S is -',
      opts=['[0, 3]', '[−1, 1]', '[0, 1]', '[−1, 3]'], hint=['Vault', 'Echo']),
 dict(n=9, qid='91617', text=f'Let f : R {TO} A = {{y | 0 {LE} y &lt; {fr(PI, "2")}}} be a function such that f(x) = tan<sup>−1</sup> (x<sup>2</sup> + x + k), where k is a constant. The value of k for which f is an onto function, is -',
      opts=['1', '0', '1/4', 'None of these'], hint=['Starter', 'Roots']),
 dict(n=10, qid='91719', text='Let f (x) = (1 + b<sup>2</sup>)x<sup>2</sup> + 2bx + 1 and let m(b) be the minimum value of f(x). As b varies, the range of m(b) is -',
      opts=['[0, 1]', '[0, 1/2]', '[1/2, 1]', '(0, 1]'], hint=['Slicer', 'Translator']),
]

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1, 2], True, 'space'), ('questions', [3, 4, 5], False, 'space'), ('questions', [6, 7], False, 'space'), ('questions', [8, 9], False, 'spaceqr'),
    ('supp', [1, 2, 3, 4], True, 'space'), ('supp', [5, 6, 7], False, 'space'), ('supp', [8, 9, 10], False, 'howdid+space'),
    ('notes',),   # keeps the next exercise's opener on a left-hand (even) page
]
