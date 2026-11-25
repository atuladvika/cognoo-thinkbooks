"""JEE Main Mathematics, Chapter 1: Functions, Exercise 1.1 (mappings). Content for the companion pages.
Source exercise: Cambridge IGCSE & O Level Additional Mathematics Coursebook, Chapter 1, Exercise 1.1 (p. 3).
Answers (checked by hand, never printed): Q1 one-one, Q2 many-one, Q3 one-one, Q4 one-one, Q5 one-one,
Q6 one-one, Q7 one-one, Q8 one-many.
Supplementary answers: see the SUPP comment below (never printed)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_class'))
from glyphs_svg import MAP, TO, IN, R, sym
DELTA = sym('\u0394', 0.95)

x = '<i>x</i>'
def fr(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'
def mp(rule, dom):
    return f'<span class="mx">{x} {MAP} {rule}&nbsp;&nbsp;&nbsp;{dom}</span>'

XR = f'{x} {IN} {R}'

CH = dict(
    num=1, title='Functions', first_page=10, exercise='Exercise 1.1', lecture_label='Exercise 1.1',
    subject='Cambridge IGCSE &amp; O Level Additional Mathematics',
    lecture_qr=None, dyna_qr=None,   # QR Manager codes not issued yet: placeholders are printed
    count_line='Exercise 1.1 · 8 questions · One-one, many-one and one-many mappings · Goes with Chapter 1 of your Additional Mathematics Coursebook',
)

KNOW = [
    f'<b>Mapping notation:</b> {x} {MAP} {x} + 1 is read “{x} is mapped to {x} + 1”. So 3 {MAP} 4.',
    f'<b>The domain:</b> {XR} means any real number. “{x} &gt; 0” keeps only positive inputs.',
    f'<b>Table of values:</b> for {x}<sup>2</sup>, the inputs −1, 0, 1 give the outputs 1, 0, 1.',
    f'<b>Line tests:</b> on a graph, a horizontal line shows inputs that share one output; a vertical line shows outputs of one input.',
]

# Main STCA concept of each question (STCA Engg/Med Mathematics: Topic 1 Ch 6 Relation and Functions; Topic 2 Ch 1 Functions)
BARS = [
    ('Polynomial Functions', 'linear, quadratic, cubic', 3, '#007ea2', 'Q 1, 2, 3'),
    ('Rational Function', 'a fraction with x below', 2, '#05ccab', 'Q 5, 7'),
    ('Exponential Function', 'a fixed number to the power x', 1, '#05ccab', 'Q 4'),
    ('Domain and Range', 'which inputs are allowed', 1, '#05ccab', 'Q 6'),
    ('Relation and its Type', 'a rule that may give two outputs', 1, '#05ccab', 'Q 8'),
]
BARS_TITLE = 'STCA concepts this exercise tests'
ALSO = ['One-One (Injective) Functions · Q 1 to 7', 'Definition of a Function · Q 8', 'Domain and Range · Q 5, 7',
        'Graphing Transcendental · Q 4', 'Square Root as Inverse of Square · Q 2, 6']

ROUTINE = [('READ', 'Read the rule <b>and</b> the domain written after it.'),
           ('TEST', 'Try two inputs, including a pair with opposite signs.'),
           ('SKETCH', 'Sketch the graph. Draw a horizontal and a vertical line.'),
           ('NAME', 'One-one, many-one or one-many? Check with your table.')]
WATCH_SUB = 'The domain can change the answer.'
WATCH = [
    ('Q 2', 'Try inputs with <b>opposite signs</b>.', f'Compare {x} = 2 and {x} = −2.'),
    ('Q 3', f'Odd powers do not behave like {x}<sup>2</sup>.', f'Test −2 and 2 in {x}<sup>3</sup> before you decide.'),
    ('Q 5, Q 7', 'Read the <b>domain</b> before you test.', f'{x} = −3 is not allowed when {x} &gt; 0.'),
    ('Q 6', 'Same rule shape as Q 2, but a <b>different domain</b>.', f'{x} ≥ 0 keeps 2 but drops −2.'),
    ('Q 8', 'Read the <b>±</b> sign carefully.', '± stands for two signs, + and −.'),
]
TRYONE = dict(
    q=f'<b>Determine whether this mapping is one-one, many-one or one-many:</b>&nbsp;&nbsp;{mp("|" + x + "|", XR)}',
    opts=['a) one-one', 'b) many-one', 'c) one-many', ''],
    hints=[('Echo', f'Say it in your own words: “|{x}| is the distance of {x} from 0, so it is never negative.”'),
           ('Translator', f'Make a table for {x} = −2, −1, 0, 1, 2 and write each output.'),
           ('Starter', 'Begin with one pair of inputs with opposite signs, such as 3 and −3.')],
    turn='Look at your table. Do two inputs share an output? Pick the word.',
)
BEFORE = 'Read Section 1.1 of the coursebook: the mapping diagram and the table of one-one, many-one and one-many graphs. Keep graph paper ready.'
AHEAD = 'Q 8 maps one input to two outputs. Keep it in mind for Section 1.2: can such a mapping be a function?'

SK = {
    'Bridge': 'connect to everyday life', 'Starter': 'decide how to begin', 'Slicer': 'break it into small parts',
    'Echo': 'say it in your own words', 'Vault': 'pick what you already know', 'Roots': 'ask why it works',
    'Translator': 'turn words into numbers, pictures or steps'}
SQ = {
    'Bridge': 'What does this remind me of from my everyday life?', 'Starter': 'Where do I begin? Which clue is the easiest to use first?',
    'Slicer': 'Can I break this into small steps and solve one step at a time?', 'Echo': 'Can I say this question again in my own words?',
    'Vault': 'What do I already know that can help me here?', 'Roots': 'Why does this work? What is the rule hiding behind it?',
    'Translator': 'Can I turn the words into numbers, a drawing or a list of steps?'}

STEM = 'Determine whether this mapping is one-one, many-one or one-many.'
OPTS = ['one-one', 'many-one', 'one-many']

Q = [
 dict(n=1, text=STEM, math=mp(f'{x} + 1', XR), opts=OPTS,
      dyna=[('Translator', f'Make a small table: {x} = −1, 0, 1, 2. Write the output for each. Do any two outputs match?'),
            ('Vault', f'Recall the test for one-one: if two inputs give the same output, they must be the same input. Suppose <i>a</i> + 1 = <i>b</i> + 1. What does that tell you about <i>a</i> and <i>b</i>?')],
      turn='Can two different inputs share an output here? Choose your word.'),
 dict(n=2, text=STEM, math=mp(f'{x}<sup>2</sup> + 5', XR), opts=OPTS,
      dyna=[('Starter', f'Begin with a pair of opposite inputs: {x} = 2 and {x} = −2. Work out both outputs.'),
            ('Bridge', 'Squaring is like a mirror: a number and its negative look the same once squared. Think of the U-shaped graph in the table on page 3.')],
      turn='How many inputs reach the output 9? Now pick the word.'),
 dict(n=3, text=STEM, math=mp(f'{x}<sup>3</sup>', XR), opts=OPTS,
      dyna=[('Echo', f'Say it simply: “Every real {x} is cubed.” The question is whether two different numbers can have the same cube.'),
            ('Roots', f'Ask why {x}<sup>2</sup> let two inputs meet: the minus sign disappeared. Work out (−2)<sup>3</sup> and 2<sup>3</sup>. Does the sign survive cubing?')],
      turn='Use what you found about the sign. Sketch the curve if you need to, then decide.'),
 dict(n=4, text=STEM, math=mp(f'2<sup>{x}</sup>', XR), opts=OPTS,
      dyna=[('Translator', f'Plot a few points: {x} = −1, 0, 1, 2 give ½, 1, 2, 4. Join them into a curve.'),
            ('Roots', 'Ask why the curve has its shape: each step to the right doubles the output. Can the output ever come back down to a value it had earlier?')],
      turn='Draw one horizontal line on your sketch. Count the crossings, then name the mapping.'),
 dict(n=5, text=STEM, math=mp(fr('1', x), f'{XR}, {x} &gt; 0'), opts=OPTS,
      dyna=[('Vault', f'Recall what the domain says: only {x} &gt; 0 is allowed. Negative inputs are not part of this mapping at all.'),
            ('Translator', f'Make a table for {x} = ½, 1, 2, 4. As {x} grows, what happens to the output? Can it come back to a value it had before?')],
      turn='Decide if two allowed inputs can share an output.'),
 dict(n=6, text=STEM, math=mp(f'{x}<sup>2</sup> + 1', f'{XR}, {x} ≥ 0'), opts=OPTS,
      dyna=[('Echo', f'Say it in your own words: “The same U-shaped rule as in Q 2, but now only {x} ≥ 0 is allowed.” What has the domain removed?'),
            ('Slicer', f'Break it into two steps. Step 1: write which inputs the domain removes. Step 2: test the pair that met in Q 2, 2 and −2. Is −2 still allowed?')],
      turn='Sketch only the allowed part of the curve. Then decide.'),
 dict(n=7, text=STEM, math=mp(fr('12', x), f'{XR}, {x} &gt; 0'), opts=OPTS,
      dyna=[('Bridge', f'Picture 12 kg of rice shared equally among {x} people. More people means a smaller share for each. Can two different group sizes give the same share?'),
            ('Vault', f'Compare with Q 5: {fr("12", x)} is just {fr("1", x)} made 12 times taller. Does stretching a graph upwards change how many inputs meet one output?')],
      turn=f'Check two inputs, such as {x} = 3 and {x} = 4. Then choose your word.'),
 dict(n=8, text=STEM, math=mp(f'±{x}', f'{XR}, {x} ≥ 0'), opts=OPTS,
      dyna=[('Echo', f'Read the ± sign aloud: “{x} is mapped to plus {x} and to minus {x}.” How many outputs is that for one input?'),
            ('Translator', f'Make a table for {x} = 1, 2, 3. Write <b>every</b> output each input gives. Then compare with the third graph in the table on page 3.')],
      turn=f'Count the outputs for {x} = 3. Then pick the word.'),
]
SPOT = None

# Supplementary: 10 questions from the i2K / Dynamind bank "Relation and Functions Obj" (Engg/Med Entrance),
# wording and options as in the bank, Q-IDs read from the report. Bank answers (never printed):
# 50129 B, 142578 C, 142543 C, 47851 D, 142568 C, 73199 B, 73377 A, 73364 C, 91726 A, 73383 B.
f_ = '<i>f</i>'
SUPP = [
 dict(n=1, qid='50129', text='Which of the following relations is function?',
      opts=['{(a, 1), (a, 2), (b, 3), (c, 4)}', '{(a, 2), (b, 3), (c, 4)}', '{(a, 3), (b, 1), (a, 4), (b, 2)}', 'None of these'], hint=['Echo', 'Vault']),
 dict(n=2, qid='142578', text='Which of the following functions defined from R to R are one-one.',
      opts=['f(x) = |x|', 'f(x) = cos x', 'f(x) = e<sup>x</sup>', 'f(x) = x<sup>2</sup>'], raw=True, hint=['Translator', 'Roots']),
 dict(n=3, qid='142543', text=f'If {f_} : R {TO} R , {f_}(x) = sin<sup>2</sup> x + cos<sup>2</sup> x , then {f_} is -',
      opts=['one-one but not onto', 'onto but not one-one', 'neither one-one nor onto', 'both one-one onto'], hint=['Slicer', 'Vault']),
 dict(n=4, qid='47851', text=f'Let R be the set of real numbers. If {f_} : R {TO} R is a function defined by {f_}(x) = x<sup>2</sup>, then {f_} is:',
      opts=['injective but not surjective', 'surjective but not injective', 'bijective', 'none of the above'], hint=['Starter', 'Vault']),
 dict(n=5, qid='142568', text='Set A has 3 elements and set B has 4 elements. The number of injections that can be defined from A to B is -',
      opts=['144', '12', '24', '64'], hint=['Slicer', 'Bridge']),
 dict(n=6, qid='73199', text=f'Let S be the set of all triangles and R<sup>+</sup> be the set of positive real numbers. Then the function, {f_} : S {TO} R<sup>+</sup>, {f_}({DELTA}) = area of the {DELTA}, where {DELTA} {IN} S is',
      opts=['injective but not surjective', 'surjective but not injective', 'injective as well as surjective', 'neither injective nor surjective'], hint=['Bridge', 'Echo']),
 dict(n=7, qid='73377', text=f'Let {f_}(x) = {fr("x", "1 + x")} defined from (0, ∞) {TO} [0, ∞) then by {f_}(x) is',
      opts=['one-one but not onto', 'one-one and onto', 'Many one but not onto', 'Many one and onto'], hint=['Translator', 'Roots']),
 dict(n=8, qid='73364', text=f'For real x, let {f_}(x) = x<sup>3</sup> + 5x + 1, then -',
      opts=['f is one-one but not onto R', 'f is onto R but not one-one', 'f is one-one and onto R', 'f is neither one-one nor onto R'], hint=['Roots', 'Starter']),
 dict(n=9, qid='91726', text=f'Let function {f_} : R {TO} R be defined by {f_}(x) = 2x + sin x for x {IN} R. Then {f_} is–',
      opts=['one to one and onto', 'one to one but not onto', 'onto but not one to one', 'neither one to one nor onto'], hint=['Roots', 'Slicer']),
 dict(n=10, qid='73383', text=f'The function {f_} : [0, 3] {TO} [1, 29], defined by {f_}(x) = 2x<sup>3</sup> − 15x<sup>2</sup> + 36x + 1, is',
      opts=['one-one and onto', 'onto but not one-one', 'one-one but not onto', 'neither one-one nor onto'], hint=['Slicer', 'Translator']),
]

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1, 2], True, 'space'), ('questions', [3, 4, 5], False, 'space'), ('questions', [6, 7, 8], False, 'spaceqr'),
    ('supp', [1, 2, 3, 4], True, 'space'), ('supp', [5, 6, 7], False, 'space'), ('supp', [8, 9, 10], False, 'howdid+space'),
]

# Opener panel: the three kinds of mapping (definitions in plain words; mini graphs drawn as SVG)
KINDS = [
    ('one-one', 'Each input has one output; no two inputs share it.',
     '<path d="M8 50 L62 8" stroke="#1e436d" stroke-width="2" fill="none"/>'),
    ('many-one', 'Two or more inputs can share one output.',
     '<path d="M8 8 Q35 92 62 8" stroke="#1e436d" stroke-width="2" fill="none"/>'),
    ('one-many', 'One input gives two or more outputs.',
     '<path d="M62 6 Q2 29 62 52" stroke="#1e436d" stroke-width="2" fill="none"/>'),
]
