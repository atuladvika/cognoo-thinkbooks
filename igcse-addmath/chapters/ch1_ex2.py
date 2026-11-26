"""JEE Main Mathematics, Chapter 1: Functions, Exercise 1.2 (definition of a function, domain and range).
Source exercise: Cambridge IGCSE & O Level Additional Mathematics Coursebook, Chapter 1, Exercise 1.2 (p. 5).
Answers (checked by hand, never printed):
Q1 mappings 1 to 7 of Exercise 1.1 are functions (8 is one-many, not a function).
Q2 a −7 ≤ f(x) ≤ 2; b 2 ≤ f(x) ≤ 17; c −1 ≤ f(x) ≤ 9; d 0 ≤ f(x) ≤ 9; e 1/8 ≤ f(x) ≤ 8; f 1/5 ≤ f(x) ≤ 1.
Q3 g(x) ≥ 2; Q4 f(x) ≥ −4; Q5 f(x) ≥ 5; Q6 f(x) ≥ −5; Q7 −6 ≤ f(x) ≤ 10; Q8 f(x) ≥ 3.
Supplementary: see the SUPP comment below (answers never printed)."""
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
    lecture_qr=None, dyna_qr='CGN000024',   # lecture QR not issued yet (placeholder); CGN000024 = Chapter 1 Cognoo pathway, issued 26 Nov 2026
    count_line='Exercise 1.2 · 8 questions (Q 2 has 6 parts) · Definition of a function, domain and range · Goes with Chapter 1 of your Additional Mathematics Coursebook',
)

KNOW = [
    '<b>Function:</b> exactly one output for each input. One-one and many-one are functions; one-many is not.',
    f'<b>Domain and range:</b> the inputs and the outputs. For f({x}) = 2{x}, 1 {LE} {x} {LE} 3, the range is 2 {LE} f({x}) {LE} 6.',
    f'<b>Completing the square:</b> {x}<sup>2</sup> − 6{x} + 11 = ({x} − 3)<sup>2</sup> + 2. A square is never negative.',
    '<b>Rising or falling:</b> if a graph only rises or only falls, its end points give the smallest and largest outputs.',
]

BARS = [
    ('Greatest and Least Values', 'of a quadratic expression', 5, '#007ea2', 'Q 3, 4, 5, 6, 7'),
    ('Polynomial Functions', 'straight lines', 1, '#05ccab', 'Q 2 a–c'),
    ('Domain and Range', 'of different types of function', 1, '#05ccab', 'Q 2 d–f'),
    ('Definition of a Function', 'one output for each input', 1, '#05ccab', 'Q 1'),
    ('Square Root Function', 'the non-negative root', 1, '#05ccab', 'Q 8'),
]
BARS_TITLE = 'Concepts this exercise tests'
BARS_SUB = 'Main concept of each of the 9 question blocks (Q 2 is split in two)'
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

# Supplementary (Atul's rules, 26 Nov 2026): only bank questions within the scope of the coursebook text before the
# exercise (Section 1.2: a function gives each input one output; f(x) notation and finding values; domain; range
# (image set), read from a sketch, including quadratics with a lowest point) and of comparable hardness. Fewer than 10 is fine.
# Banks: "Relation and Functions Obj" (50129, 142505, 142933) and "1_Functions_Obj" (50125, 74868, 50140).
# Wording and options exactly as in the bank; Q-IDs read from the report pages.
# Bank answers (never printed), each checked by hand, with the coursebook question it matches:
# 50129 B (L2; which set of pairs is a function ~ Q 1), 142505 C (L2; same ~ Q 1), 50125 A (L2; domain of a mapping),
# 142933 C (L3; f(25)/(f(9) + f(16)) = 5/7, values from f(x) notation), 74868 D (L3; range of x^2 + 2 ~ Q 3, 4),
# 50140 A (L4; four primes, four different cubes in the range).
# Left out: 74895 (range of sqrt(16 - x^2) is [0, 4], but the bank answer is (0, 4)); 142926 (same as 142505);
# onto / into, relations (domain of a relation, reflexive and so on), modulus (74865, 74864: Section 1.4), trig, logs,
# composite or inverse questions, functional equations and rational ranges (harder than the exercise).
SUPP = [
 dict(n=1, qid='50129', text='Which of the following relations is function?',
      opts=['{(a, 1), (a, 2), (b, 3), (c, 4)}', '{(a, 2), (b, 3), (c, 4)}', '{(a, 3), (b, 1), (a, 4), (b, 2)}', 'None of these'],
      hint=[('Echo', 'Read each set aloud: “a goes to 1, a goes to 2 …”. Does any letter go to two places?'),
            ('Vault', 'A function gives each input just one output. Look for an input that appears twice.')]),
 dict(n=2, qid='142505', text='Which of the following relation is a function ?',
      opts=['{(1,4), (2,6), (1,5), (3,9)}', '{(3,3), (2,1), (1,2), (2,3)}', '{(1,2), (2,2), (3,2), (4,2)}', '{(3,1), (3,2), (3,3), (3,4)}'],
      hint=[('Translator', 'Draw a small arrow diagram for each set: inputs on the left, outputs on the right.'),
            ('Bridge', 'Think of students and birthdays: two students can share a birthday, but one student cannot have two birthdays.')]),
 dict(n=3, qid='50125', text=f'Let A = B = {{1, 2, 3, 4, 5}} and f = {{(x, y) {IN} A × B : x = y}} then which of the following option is correct.',
      opts=['Domain = {1, 2, 3, 4, 5}', 'Range = {1, 2, 3, 4}', 'Number of elements in Domain &gt; Number of elements in Range', 'None Of These'], raw=True,
      hint=[('Starter', 'Begin by writing out the pairs in f: (1, 1), (2, 2) and so on.'),
            ('Slicer', 'Find the domain (the first numbers) and the range (the second numbers). Then test each option against them.')]),
 dict(n=4, qid='142933', text=f'If f : N {TO} R<sup>+</sup>, f(x) = √x , then the value of {fr("f(25)", "f(9) + f(16)")} is -',
      opts=['0', '1', '5/7', '9/7'], raw=True,
      hint=[('Starter', 'Begin with the top: f(25) means √25.'),
            ('Slicer', 'Work out f(9) and f(16) one at a time, add them, then put everything into the fraction.')]),
 dict(n=5, qid='74868', text='Range of <i>f</i>(x) = x<sup>2</sup> + 2 is',
      opts=['(−∞, ∞)', '[0, ∞)', '(−∞, 0])', '[2, ∞)'], raw=True,
      hint=[('Roots', 'x<sup>2</sup> is a square, so it is never below 0. Ask what that makes the smallest value of x<sup>2</sup> + 2.'),
            ('Bridge', 'Think of a lift that never goes below floor 2 but can go as high as you like. Which floors can it reach?')]),
 dict(n=6, qid='50140', text='The relation defined R = {(x, x<sup>3</sup>) : x is a prime number less than 10 } how many elements are there in Range ?',
      opts=['4', '5', '2', '1'],
      hint=[('Translator', 'List every prime less than 10, then write its cube next to it.'),
            ('Vault', 'The range is the set of outputs. Count how many different outputs you have.')]),
]

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1, 2], True, 'space'), ('questions', [3, 4, 5], False, 'space'), ('questions', [6, 7], False, 'space'), ('questions', [8, 9], False, 'spaceqr'),
    ('supp', [1, 2, 3], True, 'space'), ('supp', [4, 5, 6], False, 'howdid+space'),
]
