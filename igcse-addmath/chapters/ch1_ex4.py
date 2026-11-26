"""JEE Main Mathematics, Chapter 1: Functions, Exercise 1.4 (modulus equations).
Source exercise: Cambridge IGCSE & O Level Additional Mathematics Coursebook, Chapter 1, Exercise 1.4 (p. 12).
Answers (solved with SymPy and checked by hand, never printed):
Q1 a -8/3, 4; b -7, -2; c 4/5, 8/5; d -23, 25; e -5, -2; f -1/2, 15/2; g 16, 24; h -5, 35/9; i 5/3, 5.
Q2 a -29/6, -19/10; b -4/5, 0; c -28/5, 4; d 3/4, 7/2; e 13/2; f 10/3.
Q3 a -2, 2; b -3, 3; c -3, -1, 2; d 0, 4, 6; e -2, 1, 3; f -2, -1, 0, 3; g 1/2, 1; h -1, 2; i 0, 2, 6.
Q4 a (-4, 0), (3, 7), (5, 9); b (0, 0), (1, 1), (2, 2); c (1, 3), (5/2, 15/2).
Supplementary: see the SUPP comment below (answers never printed)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_class'))
from glyphs_svg import MAP, TO, IN, R, sym

x = '<i>x</i>'; y = '<i>y</i>'
def fr(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'
def md(e):
    return f'<span class="mod"><span>{e}</span></span>'
def sim(a, b):
    return f'<span class="sim"><span>{a}</span><span>{b}</span></span>'
LE = '≤'; GE = '≥'; NE = '≠'
X2 = f'{x}<sup>2</sup>'
XA = f'{x} ='

CH = dict(
    num=1, title='Functions', first_page=42, exercise='Exercise 1.4',
    subject='Cambridge IGCSE &amp; O Level Additional Mathematics',
    lecture_qr=None, dyna_qr='CGN000024',   # lecture QR not issued yet (placeholder); CGN000024 = Chapter 1 Cognoo pathway, issued 26 Nov 2026
    count_line='Exercise 1.4 · 4 questions, 27 parts · Modulus equations · Goes with Chapter 1 of your Additional Mathematics Coursebook',
)

KNOW = [
    f'<b>Modulus:</b> {md("<i>a</i>")} is the size of <i>a</i> without its sign. {md("−4")} = {md("4")} = 4, and a modulus is never negative.',
    f'<b>Key rule:</b> {md("<i>A</i>")} = <i>k</i>, with <i>k</i> {GE} 0, means <i>A</i> = <i>k</i> or <i>A</i> = −<i>k</i>.',
    f'<b>x on the right:</b> in {md("<i>A</i>")} = <i>B</i>, the right side <i>B</i> must be {GE} 0. Check every answer.',
    f'<b>Graph:</b> y = {md("f(" + x + ")")} reflects the part of y = f({x}) below the {x}-axis up above it.',
]

BARS = [
    ('Modulus Function', 'size without sign', 3, '#007ea2', 'Q 1 a–c, d–f, g–i'),
    ('Extraneous Roots', 'check every answer', 3, '#007ea2', 'Q 3 a–c, d–f, g–i'),
    ('Other Algebraic Equations', 'with fractions and x outside', 2, '#05ccab', 'Q 2 a–c, d–f'),
    ('Geometrical Representation', 'where two graphs meet', 1, '#05ccab', 'Q 4'),
]
BARS_TITLE = 'Concepts this exercise tests'
BARS_SUB = 'Main concept of each of the 9 question blocks'
ALSO = ['Solution of Quadratic Equations · Q 3, 4', 'Rational Function · Q 2 a–c', 'Extraneous Roots · Q 1 i, Q 2 d–f, Q 4',
        'Graphing Piecewise Functions · Q 4', 'Modulus Function · Q 2, 3, 4']

ROUTINE = [('READ', 'What is inside the modulus? What is on the other side?'),
           ('SPLIT', 'Write two cases: inside = + right side, inside = − right side.'),
           ('SOLVE', 'Solve each case on its own.'),
           ('CHECK', 'Put every answer back into the original equation.')]
WATCH_SUB = 'When x is on the right side, some answers will not work.'
WATCH = [
    ('Q 1 i, Q 2 d–f', f'The right side contains {x}: it must not be negative.', f'{md("2" + x + " − 5")} = {x} needs {x} {GE} 0.'),
    ('Q 1 d–h', 'Clear the fraction <b>after</b> you split into two cases.', f'{md(fr(x + " − 1", "4"))} = 6 means {fr(x + " − 1", "4")} = 6 or −6.'),
    ('Q 2 a–c', f'{x} cannot make a bottom equal to 0.', f'{x} {NE} −3 in Q 2 a.'),
    ('Q 3', 'A quadratic in each case can give up to four candidates.', 'Solve both cases, then test each root.'),
    ('Q 4', f'An intersection needs both {x} and {y}.', f'Put each {x} back into {y} = … to find {y}.'),
]
TRYONE = dict(
    q=f'<b>Solve</b>&nbsp; {md(x + " + 3")} = 2{x}.',
    opts=[], write=XA,
    hints=[('Echo', f'Say it in your own words: “{x} + 3 is 2{x} away from 0.” A distance cannot be negative, so 2{x} {GE} 0.'),
           ('Slicer', f'Split into two cases: {x} + 3 = 2{x} and {x} + 3 = −2{x}. Solve each one.'),
           ('Roots', 'Ask why you must check: one case may give a value that makes the right side negative.')],
    turn='Test both answers in the original equation. Which one survives?',
)
BEFORE = 'Read Section 1.4 of the coursebook: modulus functions, the definition of |x|, and Worked example 6.'
AHEAD = 'Q 4 asks where a line meets a modulus curve. A quick sketch tells you how many crossings to expect.'

SK = {
    'Bridge': 'connect to everyday life', 'Starter': 'decide how to begin', 'Slicer': 'break it into small parts',
    'Echo': 'say it in your own words', 'Vault': 'pick what you already know', 'Roots': 'ask why it works',
    'Translator': 'turn words into numbers, pictures or steps'}
SQ = {
    'Bridge': 'What does this remind me of from my everyday life?', 'Starter': 'Where do I begin? Which clue is the easiest to use first?',
    'Slicer': 'Can I break this into small steps and solve one step at a time?', 'Echo': 'Can I say this question again in my own words?',
    'Vault': 'What do I already know that can help me here?', 'Roots': 'Why does this work? What is the rule hiding behind it?',
    'Translator': 'Can I turn the words into numbers, a drawing or a list of steps?'}

S1 = f'Solve each equation for {x}.'
Q = [
 dict(n=1, label='Q 1 a–c', text=S1, part_label=XA,
      parts=[('a', f'{md("3" + x + " − 2")} = 10'), ('b', f'{md("2" + x + " + 9")} = 5'), ('c', f'{md("6 − 5" + x)} = 2')],
      dyna=[('Vault', f'Use the key rule: {md("<i>A</i>")} = <i>k</i> means <i>A</i> = <i>k</i> or <i>A</i> = −<i>k</i>.'),
            ('Bridge', f'Think of a number line: {md("3" + x + " − 2")} = 10 means 3{x} − 2 is 10 steps from 0, to the right <b>or</b> to the left.')],
      turn='Write the two cases for each part, solve them, and check one answer by substituting.'),
 dict(n=1, label='Q 1 d–f', text=S1 + ' (continued)', part_label=XA,
      parts=[('d', f'{md(fr(x + " − 1", "4"))} = 6'), ('e', f'{md(fr("2" + x + " + 7", "3"))} = 1'), ('f', f'{md(fr("7 − 2" + x, "2"))} = 4')],
      dyna=[('Echo', f'Say part d in words: “the fraction {fr(x + " − 1", "4")} is 6 away from 0.”'),
            ('Translator', 'Write the two cases, then multiply both sides by the bottom number to clear the fraction.')],
      turn='Solve each case. Expect two answers per part.'),
 dict(n=1, label='Q 1 g–i', text=S1 + ' (continued)', part_label=XA,
      parts=[('g', f'{md(fr(x, "4") + " − 5")} = 1'), ('h', f'{md(fr(x + " + 1", "2") + " + " + fr("2" + x, "5"))} = 4'), ('i', f'{md("2" + x + " − 5")} = {x}')],
      dyna=[('Starter', 'In h, begin by combining the two fractions inside the modulus into one fraction (use 10 as the common bottom).'),
            ('Roots', f'In i, the right side is {x}. A modulus is never negative, so ask why {x} must be {GE} 0. Check both answers against that.')],
      turn='Solve g, h and i. Keep only the answers that pass your check.'),
 dict(n=2, label='Q 2 a–c', text=S1, part_label=XA,
      parts=[('a', f'{md(fr("2" + x + " − 5", x + " + 3"))} = 8'), ('b', f'{md(fr("3" + x + " + 2", x + " + 1"))} = 2'), ('c', f'{md("1 + " + fr(x + " + 12", x + " + 4"))} = 3')],
      dyna=[('Translator', f'Write the two cases, for example {fr("2" + x + " − 5", x + " + 3")} = 8 and = −8. Multiply both sides by the bottom.'),
            ('Vault', f'Remember: {x} can never be the value that makes a bottom 0. In c, first write 1 + {fr(x + " + 12", x + " + 4")} as one fraction.')],
      turn='Solve both cases in each part and write the answers.'),
 dict(n=2, label='Q 2 d–f', text=S1 + ' (continued)', part_label=XA,
      parts=[('d', f'{md("3" + x + " − 5")} = {x} + 2'), ('e', f'{x} + {md(x + " − 5")} = 8'), ('f', f'9 − {md("1 − " + x)} = 2{x}')],
      dyna=[('Slicer', f'In e and f, first get the modulus on its own, for example {md(x + " − 5")} = 8 − {x}. Then split into two cases.'),
            ('Roots', 'Ask why some answers fail: a modulus cannot equal a negative number. So the other side must be ≥ 0 for each answer.')],
      turn='Solve, then cross out any answer that makes the other side negative.'),
 dict(n=3, label='Q 3 a–c', text=S1, part_label=XA,
      parts=[('a', f'{md(X2 + " − 1")} = 3'), ('b', f'{md(X2 + " + 1")} = 10'), ('c', f'{md("4 − " + X2)} = 2 − {x}')],
      dyna=[('Starter', f'Begin with b: can {X2} + 1 ever be negative? If not, the modulus changes nothing and there is only one case.'),
            ('Slicer', f'For a and c, write the two cases. Each case is a quadratic: rearrange it to = 0 and solve.')],
      turn='Solve each case and check every root in the original equation.'),
 dict(n=3, label='Q 3 d–f', text=S1 + ' (continued)', part_label=XA,
      parts=[('d', f'{md(X2 + " − 5" + x)} = {x}'), ('e', f'{md(X2 + " − 4")} = {x} + 2'), ('f', f'{md(X2 + " − 3")} = {x} + 3')],
      dyna=[('Translator', 'Each case gives a quadratic. Rearrange it to = 0, then factorise.'),
            ('Vault', f'Recall that the right side must be ≥ 0: in d, {x} {GE} 0; in e, {x} {GE} −2; in f, {x} {GE} −3.')],
      turn='Collect the roots from both cases and keep those that pass the check.'),
 dict(n=3, label='Q 3 g–i', text=S1 + ' (continued)', part_label=XA,
      parts=[('g', f'{md("2" + X2 + " + 1")} = 3{x}'), ('h', f'{md("2" + X2 + " − 3" + x)} = 4 − {x}'), ('i', f'{md(X2 + " − 7" + x + " + 6")} = 6 − {x}')],
      dyna=[('Roots', f'In g, 2{X2} + 1 is always positive. Ask why that means you need only one case.'),
            ('Slicer', 'In h and i, write both cases, solve each quadratic, then test every root in the original equation.')],
      turn='Write the roots that survive your test.'),
 dict(n=4, label='Q 4 a–c', text='Solve each pair of simultaneous equations.', part_label='(x, y):', cols=1,
      parts=[('a', sim(f'{y} = {x} + 4', f'{y} = {md(X2 + " − 16")}')), ('b', sim(f'{y} = {x}', f'{y} = {md("3" + x + " − 2" + X2)}')), ('c', sim(f'{y} = 3{x}', f'{y} = {md("2" + X2 + " − 5")}'))],
      dyna=[('Bridge', f'Think of two roads on a map: a crossing is a point on both roads. You need the {x} and the {y} of every crossing.'),
            ('Translator', f'Set the two expressions for {y} equal. Split the modulus into two cases, solve, then find {y} for each {x}. Remember {y} = a modulus cannot be negative.')],
      turn='List every point (x, y) for each part.'),
]
SPOT = None

# Supplementary (Atul's rules, 26 Nov 2026): only bank questions within the scope of the coursebook text before the
# exercise (Section 1.4, with Sections 1.1 to 1.3 before it: the modulus is the size of a number without its sign and is
# never negative; |x| = k means x = k or x = -k; |ax + b| = cx + d and checking answers) and of comparable hardness.
# Fewer than 10 is fine. Neither bank has a modulus EQUATION at this level, so these four use the modulus definition
# (values, a range, an identity); they are a little easier than the exercise.
# Banks: "Relation and Functions Obj" (74865) and "1_Functions_Obj" (87577, 74864, 87579).
# Wording and options exactly as in the bank; Q-IDs read from the report pages.
# Bank answers (never printed), each checked by hand: 74865 B (|-4| + 2 = 6), 87577 B ((-1 - 1)/1 = -2),
# 74864 D (-|x| <= 0, so the negative reals with 0), 87579 B (4x + 2|x| - 2x + |x| - 2x - |x| = 2|x|).
# Left out: 47696 (|f + g| = |f| + |g| for x <= -1 or x >= 2; the bank answer (2, inf) is incomplete, and it is an
# inequality), 47850 and 47689 (inequalities / parameters, harder), modulus with trig, logs or the greatest-integer function,
# relations (74645, 85397, 88772), 64196 (bijective, Section 1.1 scope).
CUP = sym('∪', 0.95)
SUPP = [
 dict(n=1, qid='74865', text='If f(x) = |x − 3| + 2 then f(−1) =', opts=['2', '6', '−6', '0'],
      hint=[('Starter', 'Begin inside the modulus: work out −1 − 3 first.'),
            ('Vault', 'Recall from Section 1.4: the modulus of a number is its size without the sign, so it is never negative.')]),
 dict(n=2, qid='87577', text=f'If <i>f</i>(x) = {fr("x − | x |", "| x |")}, then <i>f</i>(−1) =', opts=['1', '−2', '0', '+2'], raw=True,
      hint=[('Translator', 'Put x = −1 in every place: the top becomes −1 − |−1| and the bottom becomes |−1|.'),
            ('Echo', 'Say |−1| aloud as “the size of −1”. What number is that?')]),
 dict(n=3, qid='74864', text='The range of −|x| is', opts=['−R', 'N', 'W', f'−R {CUP} {{0}}'], raw=True,
      hint=[('Roots', 'Ask why |x| is never negative. What does the minus sign in front then do to every output?'),
            ('Bridge', 'Think of depths measured from sea level: 0 m or below, never above. (−R means all the negative real numbers.)')]),
 dict(n=4, qid='87579', text=f'Let <i>f</i> : <i>R</i> {TO} <i>R</i> be defined by <i>f</i>(x) = 2x + |x|, then <i>f</i>(2x) + <i>f</i>(−x) − <i>f</i>(x) =',
      opts=['2<i>x</i>', '2|<i>x</i>|', '−2<i>x</i>', '−2|<i>x</i>|'], raw=True,
      hint=[('Slicer', 'Work out each part on its own: f(2x), then f(−x), then f(x). Then add and subtract.'),
            ('Vault', 'Use two facts: |2x| = 2|x| and |−x| = |x|. Then collect the x terms and the |x| terms.')]),
]

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1, 2], True), ('questions', [3, 4, 5]), ('questions', [6, 7, 8]),
    ('questions', [9], False, 'spaceqr'),
    ('supp', [1, 2, 3], True, 'space'), ('supp', [4], False, 'howdid+space'),
]
