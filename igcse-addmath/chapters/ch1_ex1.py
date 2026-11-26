"""JEE Main Mathematics, Chapter 1: Functions, Exercise 1.1 (mappings). Content for the companion pages.
Source exercise: Cambridge IGCSE & O Level Additional Mathematics Coursebook, Chapter 1, Exercise 1.1 (p. 3).
Answers (checked by hand, never printed): Q1 one-one, Q2 many-one, Q3 one-one, Q4 one-one, Q5 one-one,
Q6 one-one, Q7 one-one, Q8 one-many.
Supplementary: see the SUPP comment below (answers never printed)."""
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
    lecture_qr='CGN000023', dyna_qr='CGN000024',   # lecture QR issued 26 Nov 2026; CGN000024 = Chapter 1 Cognoo pathway (all exercises), issued 26 Nov 2026
    count_line='Exercise 1.1 · 8 questions · One-one, many-one and one-many mappings · Goes with Chapter 1 of your Additional Mathematics Coursebook',
)

KNOW = [
    f'<b>Mapping notation:</b> {x} {MAP} {x} + 1 is read “{x} is mapped to {x} + 1”. So 3 {MAP} 4.',
    f'<b>The domain:</b> {XR} means any real number. “{x} &gt; 0” keeps only positive inputs.',
    f'<b>Table of values:</b> for {x}<sup>2</sup>, the inputs −1, 0, 1 give the outputs 1, 0, 1.',
    f'<b>Line tests:</b> a horizontal line finds inputs that share an output; a vertical line finds the outputs of one input.',
]

# Main STCA concept of each question (STCA Engg/Med Mathematics: Topic 1 Ch 6 Relation and Functions; Topic 2 Ch 1 Functions)
BARS = [
    ('Polynomial Functions', 'linear, quadratic, cubic', 3, '#007ea2', 'Q 1, 2, 3'),
    ('Rational Function', 'a fraction with x below', 2, '#05ccab', 'Q 5, 7'),
    ('Exponential Function', 'a fixed number to the power x', 1, '#05ccab', 'Q 4'),
    ('Domain and Range', 'which inputs are allowed', 1, '#05ccab', 'Q 6'),
    ('Relation and its Type', 'a rule that may give two outputs', 1, '#05ccab', 'Q 8'),
]
BARS_TITLE = 'Concepts this exercise tests'
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

# Supplementary (rule set by Atul, 26 Nov 2026): print only bank questions that are of comparable hardness to the
# coursebook questions AND well within the scope of the text before the exercise (Section 1.1: mapping diagrams,
# x ↦ notation, one-one / many-one / one-many read from a rule or a graph). Fewer than 10 is fine.
# Both banks searched (Relation and Functions Obj; 1_Functions_Obj). Only one question qualifies:
# 142578 C (L2; one-one test on four familiar graphs ~ Q 2, 3, 4). Bank answer checked by hand, never printed.
# Left out as outside Section 1.1 or harder: questions using onto / into / surjective / bijective (e.g. 47851, 142962,
# 47828, 91586, 73176, 64187, 80338), "is a function" (50129, 142926: Section 1.2), domain / range (50125, 50140: Section 1.2),
# counting maps (142568), 91618 (level 6, injective on restricted domains), 143007 (same as 142578), 73350 (two true options).
SUPP = [
 dict(n=1, qid='142578', text='Which of the following functions defined from R to R are one-one.',
      opts=['f(x) = |x|', 'f(x) = cos x', 'f(x) = e<sup>x</sup>', 'f(x) = x<sup>2</sup>'], raw=True,
      hint=[('Translator', 'For each option, put in a pair of opposite inputs, such as 1 and −1, and compare the outputs.'),
            ('Bridge', 'Waves on the sea rise to the same height again and again. Does the graph of cos x do the same?')]),
]

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1, 2], True, 'space'), ('questions', [3, 4, 5], False, 'space'), ('questions', [6, 7, 8], False, 'spaceqr'),
    ('supp', [1], True, 'howdid+space'),
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
