"""JEE Main Mathematics, Chapter 1: Functions, Exercise 1.3 (composite functions).
Source exercise: Cambridge IGCSE & O Level Additional Mathematics Coursebook, Chapter 1, Exercise 1.3 (pp. 8-10).
Answers (checked by hand, never printed):
Q1 9; Q2 51; Q3 675; Q4 1; Q5 67; Q6 a hk, b kh; Q7 x = -1/3; Q8 x = 4 or -2/3; Q9 x = 3/4; Q10 x = 5/2;
Q11 x = 5; Q12 x = 4 (x = 3 rejected: h(3) = -1 is outside the domain of g); Q13 a fg, b gf, c g^2, d f^2;
Q14 x in R, x != 0, x != -3/2; Q15 domain x > 20, range fg(x) > -9; Q16 a x != 1, b x != 0, x != 1;
Q17 a fg(x) = 2 sqrt(x) - 6, domain x >= 0, range >= -6; b gf(x) = sqrt(2x - 6), domain x >= 3, range >= 0;
Q18 a i f(x) >= -1/8, ii g(x) != 0; b i fg(x) = 2/x^2 - 1/x, domain x != 0, range >= -1/8;
    ii gf(x) = 1/(2x^2 - x), domain x != 0, 1/2, range gf(x) <= -8 or gf(x) > 0;
Q19 a i f(x) < 9, ii g(x) > 0; b gf(x) = (2x + 2)^2; c domain -1 < x < 2, range 0 < gf(x) < 36;
Q20 a i f(x) > 5, ii g(x) > 47; b gf(x) = (2x - 1)^2 - 2; c domain x > 4, range gf(x) > 47;
Q21 a i f(x) > 5, ii g(x) > 65; b gf(x) = (3x + 2)^2 + 1; c domain x > 2, range gf(x) > 65.
Supplementary: see the SUPP comment below (answers never printed)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_class'))
from glyphs_svg import MAP, TO, IN, R, sym
NOTIN = sym('∉', 0.95); CUP = sym('∪', 0.95); ALPHA = sym('α', 0.95)

x = '<i>x</i>'
def fr(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'
def rt(e):
    return f'√<span style="text-decoration:overline">{e}</span>'
LE = '≤'; GE = '≥'; NE = '≠'
XR = f'{x} {IN} {R}'
def defs(*lines):
    return '<br>'.join(lines)

CH = dict(
    num=1, title='Functions', first_page=28, exercise='Exercise 1.3',
    subject='Cambridge IGCSE &amp; O Level Additional Mathematics',
    lecture_qr=None, dyna_qr='CGN000024',   # lecture QR not issued yet (placeholder); CGN000024 = Chapter 1 Cognoo pathway, issued 26 Nov 2026
    count_line='Exercise 1.3 · 21 questions · Composite functions · Goes with Chapter 1 of your Additional Mathematics Coursebook',
)

KNOW = [
    f'<b>Order:</b> fg({x}) means f(g({x})). g acts <b>first</b>, then f acts on the result.',
    f'<b>Twice:</b> f<sup>2</sup>({x}) means f(f({x})), not [f({x})]<sup>2</sup>.',
    f'<b>Exists only if:</b> fg exists where the output of g lies in the domain of f.',
    f'<b>Solving:</b> write the composite as one expression, then solve. Check each answer against the domain.',
]

BARS = [
    ('Domain and Range', 'of a composite function', 8, '#007ea2', 'Q 14 to 21'),
    ('Composite Function', 'evaluate and build', 7, '#05ccab', 'Q 1, 2, 3, 4, 5, 6, 13'),
    ('Extraneous Roots', 'check answers against the domain', 4, '#05ccab', 'Q 8, 9, 11, 12'),
    ('Other Algebraic Equations', 'equations with fractions', 2, '#05ccab', 'Q 7, 10'),
]
BARS_TITLE = 'Concepts this exercise tests'
ALSO = ['Solution of Quadratic Equations · Q 8, 9, 11, 12', 'Rational Function · Q 7, 10, 14, 16', 'Square Root Function · Q 4, 6, 17',
        'Greatest and Least Values of a Quadratic · Q 18', 'Definition of a Function · Q 14 to 21']

ROUTINE = [('READ', 'Which function acts first? In fg, it is g.'),
           ('INNER', 'Work out the inner output first, as a number or an expression.'),
           ('OUTER', 'Put that output into the outer function.'),
           ('CHECK', 'Is every input and output allowed by the domains?')]
WATCH_SUB = 'The order of the letters decides which function acts first.'
WATCH = [
    ('Q 1, Q 2', '<b>fg</b> and <b>gf</b> use the same functions in a different order.', 'fg(2) = f(g(2)); gf(5) = g(f(5)).'),
    ('Q 3', f'f<sup>2</sup> means apply f <b>twice</b>.', 'f<sup>2</sup>(3) is not f(3) × f(3).'),
    ('Q 9, 11, 12', 'An equation can give an answer the <b>domain</b> does not allow.', f'Reject answers that break “{x} &gt; 0” or “{x} {GE} 0”.'),
    ('Q 14 to 16', 'A composite needs the inner output to be allowed in the outer function.', f'f({x}) = {fr(x, x + " + 2")} cannot take −2 as an input.'),
    ('Q 19 to 21', 'For the domain of gf, f’s outputs must lie in g’s domain.', f'g needs inputs &gt; 3, so you need f({x}) &gt; 3.'),
]
TRYONE = dict(
    q=f'<b>f({x}) = 3{x} − 1 and g({x}) = {x}<sup>2</sup> for {XR}. Find fg(2) and gf(2).</b>',
    opts=[], write='fg(2) = ________&nbsp;&nbsp;&nbsp;&nbsp;gf(2) =',
    hints=[('Echo', 'Say it in your own words: “fg(2) means f of g of 2. g goes first.”'),
           ('Slicer', 'Step 1: work out g(2). Step 2: put that number into f. Then do the same in the other order.'),
           ('Roots', 'Ask why the two answers might differ: squaring then tripling is not the same as tripling then squaring.')],
    turn='Compare your two answers. Are they equal?',
)
BEFORE = 'Read Section 1.3 of the coursebook: composite functions, the three important points in the box, and Worked examples 3, 4 and 5.'
AHEAD = 'Q 19 to 21 ask for the domain of gf. Only inputs whose f-output g can accept are allowed.'

SK = {
    'Bridge': 'connect to everyday life', 'Starter': 'decide how to begin', 'Slicer': 'break it into small parts',
    'Echo': 'say it in your own words', 'Vault': 'pick what you already know', 'Roots': 'ask why it works',
    'Translator': 'turn words into numbers, pictures or steps'}
SQ = {
    'Bridge': 'What does this remind me of from my everyday life?', 'Starter': 'Where do I begin? Which clue is the easiest to use first?',
    'Slicer': 'Can I break this into small steps and solve one step at a time?', 'Echo': 'Can I say this question again in my own words?',
    'Vault': 'What do I already know that can help me here?', 'Roots': 'Why does this work? What is the rule hiding behind it?',
    'Translator': 'Can I turn the words into numbers, a drawing or a list of steps?'}

A = 'Answer:'
Q = [
 dict(n=1, text=defs(f'f : {x} {MAP} 2{x} + 3 for {XR}', f'g : {x} {MAP} {x}<sup>2</sup> − 1 for {XR}', 'Find fg(2).'), write='fg(2) =',
      dyna=[('Echo', 'Say fg(2) as “f of g of 2”: g acts on 2 first, then f acts on the result.'),
            ('Bridge', 'Picture two machines on a conveyor belt. The 2 goes into machine g first; whatever comes out goes straight into machine f.')],
      turn='Do step 2 and write fg(2).'),
 dict(n=2, text=defs(f'f({x}) = {x}<sup>2</sup> − 1 for {XR}', f'g({x}) = 2{x} + 3 for {XR}', 'Find gf(5).'), write='gf(5) =',
      dyna=[('Echo', 'Say gf(5) aloud as “g of f of 5”. Which function sits inside the brackets, next to the 5?'),
            ('Starter', 'Begin with that inside function: work out f(5). Then use that number as the input of g.')],
      turn='Finish the second step and write gf(5).'),
 dict(n=3, text=defs(f'f({x}) = ({x} + 2)<sup>2</sup> − 1 for {XR}', 'Find f<sup>2</sup>(3).'), write='f<sup>2</sup>(3) =',
      dyna=[('Vault', f'Recall what f<sup>2</sup> means: f(f({x})), apply f twice. It is not f(3) squared.'),
            ('Slicer', 'Step 1: work out f(3). Step 2: put that answer into f again.')],
      turn='Do step 2 carefully: the number is large.'),
 dict(n=4, text=defs(f'The function f is defined by f({x}) = 1 + {rt(x + " − 2")} for {x} {GE} 2.', f'The function g is defined by g({x}) = {fr("10", x)} − 1 for {x} &gt; 0.', 'Find gf(18).'), write='gf(18) =',
      dyna=[('Bridge', f'Think of a relay race: f runs the first leg with 18 and hands its result to g. So work out 1 + {rt("18 − 2")} first.'),
            ('Vault', 'Check that f(18) is greater than 0, so g is allowed to take it.')],
      turn='Finish the calculation in g.'),
 dict(n=5, text=defs(f'The function f is defined by f({x}) = ({x} − 1)<sup>2</sup> + 3 for {x} &gt; −1.', f'The function g is defined by g({x}) = {fr("2" + x + " + 4", x + " − 5")} for {x} &gt; 5.', 'Find fg(7).'), write='fg(7) =',
      dyna=[('Starter', 'Begin with g, the function written next to the 7: work out the top and the bottom of the fraction at 7, then divide.'),
            ('Translator', f'Write the number you get in place of {x} in ({x} − 1)<sup>2</sup> + 3.')],
      turn='Work out fg(7).'),
 dict(n=6, text=defs(f'h : {x} {MAP} {x} + 2 for {x} &gt; 0', f'k : {x} {MAP} {rt(x)} for {x} &gt; 0', 'Express each of the following in terms of h and k.'),
      parts=[('a', f'{x} {MAP} {rt(x)} + 2', A), ('b', f'{x} {MAP} {rt(x + " + 2")}', A)],
      dyna=[('Echo', 'Say each rule in words: h means “add 2”, k means “take the square root”.'),
            ('Roots', 'Ask which happens first in each part. The function that acts first is written on the <b>right</b>.')],
      turn='Write a and b using the letters h and k.'),
 dict(n=7, text=defs(f'The function f is defined by f : {x} {MAP} 3{x} + 1 for {XR}.', f'The function g is defined by g : {x} {MAP} {fr("10", "2 − " + x)} for {x} {NE} 2.', 'Solve the equation gf(<i>x</i>) = 5.'), write=f'{x} =',
      dyna=[('Translator', f'Write gf({x}) as one expression: replace {x} in {fr("10", "2 − " + x)} by 3{x} + 1. Tidy the bottom.'),
            ('Slicer', 'Then set it equal to 5. Clear the fraction first, then solve the straight-line equation.')],
      turn=f'Solve for {x}. Check the bottom of the fraction is not 0.'),
 dict(n=8, text=defs(f'g({x}) = {x}<sup>2</sup> + 2 for {XR}', f'h({x}) = 3{x} − 5 for {XR}', 'Solve the equation gh(<i>x</i>) = 51.'), write=f'{x} =',
      dyna=[('Translator', f'Build gh({x}): h acts first, so it is (3{x} − 5)<sup>2</sup> + 2.'),
            ('Roots', 'Ask why there may be two answers: a square equals 49 when the bracket is 7 <b>or</b> −7.')],
      turn='Solve both cases. Both are allowed here.'),
 dict(n=9, text=defs(f'f({x}) = {x}<sup>2</sup> − 3 for {x} &gt; 0', f'g({x}) = {fr("3", x)} for {x} &gt; 0', 'Solve the equation fg(<i>x</i>) = 13.'), write=f'{x} =',
      dyna=[('Translator', f'Build fg({x}): put {fr("3", x)} into {x}<sup>2</sup> − 3.'),
            ('Vault', f'Remember the domain {x} &gt; 0: any negative solution must be rejected.')],
      turn='Solve, then keep only the allowed answer.'),
 dict(n=10, text=defs(f'The function f is defined by f : {x} {MAP} {fr("3" + x + " + 5", x + " − 2")}, {x} {NE} 2, for {XR}, {x} {NE} 2.', f'The function g is defined by g : {x} {MAP} {fr(x + " − 1", "2")}, for {XR}.', 'Solve the equation gf(<i>x</i>) = 12.'), write=f'{x} =',
      dyna=[('Starter', f'Begin with g: if g(something) = 12, what must that “something” be? Work backwards to the value of f({x}).'),
            ('Slicer', f'Step 1: solve {fr("f(" + x + ") − 1", "2")} = 12 for f({x}). Step 2: solve f({x}) = that value.')],
      turn='Cross-multiply in step 2 and solve.'),
 dict(n=11, text=defs(f'f({x}) = ({x} + 4)<sup>2</sup> + 3 for {x} &gt; 0', f'g({x}) = {fr("10", x)} for {x} &gt; 0', 'Solve the equation fg(<i>x</i>) = 39.'), write=f'{x} =',
      dyna=[('Slicer', f'Step 1: let <i>u</i> = g({x}) and solve (<i>u</i> + 4)<sup>2</sup> + 3 = 39 for <i>u</i>. Step 2: solve {fr("10", x)} = <i>u</i>.'),
            ('Vault', f'Since {x} &gt; 0, g({x}) = {fr("10", x)} is positive too. Which value of <i>u</i> can you keep?')],
      turn=f'Keep the allowed value and find {x}.'),
 dict(n=12, text=defs(f'The function g is defined by g({x}) = {x}<sup>2</sup> − 1 for {x} {GE} 0.', f'The function h is defined by h({x}) = 2{x} − 7 for {x} {GE} 0.', 'Solve the equation gh(<i>x</i>) = 0.'), write=f'{x} =',
      dyna=[('Translator', f'Build gh({x}) = (2{x} − 7)<sup>2</sup> − 1 and solve it equal to 0.'),
            ('Roots', f'Ask what g is allowed to take: inputs {GE} 0. So h({x}) = 2{x} − 7 must be {GE} 0. Test each solution.')],
      turn='Keep only the solution that passes the test.'),
 dict(n=13, text=defs(f'The function f is defined by f : {x} {MAP} {x}<sup>3</sup> for {XR}.', f'The function g is defined by g : {x} {MAP} {x} − 1 for {XR}.', 'Express each of the following as a composite function, using only f and/or g:'),
      parts=[('a', f'{x} {MAP} ({x} − 1)<sup>3</sup>', A), ('b', f'{x} {MAP} {x}<sup>3</sup> − 1', A), ('c', f'{x} {MAP} {x} − 2', A), ('d', f'{x} {MAP} {x}<sup>9</sup>', A)],
      dyna=[('Echo', 'Say what each function does: f “cubes”, g “subtracts 1”.'),
            ('Bridge', 'Think of getting dressed: socks first, then shoes. List the steps done to x in order, then write the letters from right to left, so the last step sits on the left. A function may be used twice.')],
      turn='Write each part using f and g.'),
 dict(n=14, text=defs(f'f({x}) = {fr(x, x + " + 2")} for {XR}, {x} {NE} −2&nbsp;&nbsp;&nbsp;&nbsp;g({x}) = {fr("3", x)} for {XR}, {x} {NE} 0', 'Find the domain of fg(<i>x</i>).'), write='Domain:',
      dyna=[('Roots', f'fg({x}) = f(g({x})) exists only when {x} is in g’s domain <b>and</b> g({x}) is an input f allows.'),
            ('Translator', f'f cannot take −2. Solve g({x}) = −2 to find the {x} you must exclude.')],
      turn='Write the domain as “all real x except …”.'),
 dict(n=15, text=defs(f'f({x}) = {x}<sup>2</sup> − 9 for {XR}, {x} &lt; 0&nbsp;&nbsp;&nbsp;&nbsp;g({x}) = 10 − {fr(x, "2")} for {XR}, {x} &gt; 6', 'Find the domain and range of fg(<i>x</i>).'), write='Domain and range:',
      dyna=[('Slicer', f'Step 1: f only takes negative inputs, so you need g({x}) &lt; 0. Solve this together with {x} &gt; 6. Step 2: find which outputs g gives on that domain.'),
            ('Vault', f'Then put those outputs through {x}<sup>2</sup> − 9. On negative inputs, what is the smallest value {x}<sup>2</sup> can approach?')],
      turn='Write the domain and the range of fg.'),
 dict(n=16, text=defs(f'f({x}) = {fr("1", x)} for {XR}, {x} {NE} 0&nbsp;&nbsp;&nbsp;&nbsp;g({x}) = {fr("1", x + " − 1")} for {XR}, {x} {NE} 1', 'Find the domain of'),
      parts=[('a', 'fg(<i>x</i>)', 'Domain:'), ('b', 'gf(<i>x</i>)', 'Domain:')],
      dyna=[('Translator', f'Write each composite: fg({x}) = {fr("1", "g(" + x + ")")} and gf({x}) = {fr("1", "f(" + x + ") − 1")}. Simplify.'),
            ('Roots', 'For the domain, keep the inner function’s restriction, then remove any x that makes the outer function fail.')],
      turn='List the values excluded in each part.'),
 dict(n=17, text=defs(f'f({x}) = 2{x} − 6 for {XR}&nbsp;&nbsp;&nbsp;&nbsp;g({x}) = {rt(x)} for {XR}, {x} {GE} 0', 'Find the domain and range of'),
      parts=[('a', 'fg(<i>x</i>)', 'Domain and range:'), ('b', 'gf(<i>x</i>)', 'Domain and range:')],
      dyna=[('Starter', 'Begin each part by writing the composite as one formula. Do a and b separately.'),
            ('Vault', '√ needs an input that is not negative, and it gives outputs that are not negative.')],
      turn='Write the domain and range for each part.'),
 dict(n=18, text=f'f({x}) = 2{x}<sup>2</sup> − {x} for {XR}&nbsp;&nbsp;&nbsp;&nbsp;g({x}) = {fr("1", x)} for {XR}, {x} {NE} 0', cols=1,
      parts=[('a', 'Find the range of&nbsp;&nbsp; i&nbsp; f(<i>x</i>)&nbsp;&nbsp;&nbsp; ii&nbsp; g(<i>x</i>)', 'Ranges:'),
             ('b', 'Find the domain and range of&nbsp;&nbsp; i&nbsp; fg(<i>x</i>)&nbsp;&nbsp;&nbsp; ii&nbsp; gf(<i>x</i>)', 'Domains and ranges:')],
      dyna=[('Vault', f'f is a quadratic. Complete the square, or find the turning point at {x} = −{fr("b", "2a")}, for part a i.'),
            ('Slicer', f'For b, write fg({x}) and gf({x}). For the range of fg, let <i>t</i> = {fr("1", x)} and treat it as a quadratic in <i>t</i>.')],
      turn='Work through a i, a ii, b i, b ii in order.'),
 dict(n=19, text=f'f({x}) = 2{x} + 5 for {XR}, {x} &lt; 2&nbsp;&nbsp;&nbsp;&nbsp;g({x}) = ({x} − 3)<sup>2</sup> for {XR}, {x} &gt; 3', cols=1,
      parts=[('a', 'Find the range of&nbsp;&nbsp; i&nbsp; f(<i>x</i>)&nbsp;&nbsp;&nbsp; ii&nbsp; g(<i>x</i>)', 'Ranges:'), ('b', 'Find gf(<i>x</i>).', 'gf(x) ='),
             ('c', 'Find the domain and range of gf(<i>x</i>).', 'Domain and range:')],
      dyna=[('Slicer', 'Do a, then b, then c. Part c uses part a: g only accepts inputs greater than 3.'),
            ('Translator', f'Write “f({x}) &gt; 3” as an inequality in {x} and solve it. Remember {x} &lt; 2 as well.')],
      turn='Use the domain you found to work out the range of gf.'),
 dict(n=20, text=f'f({x}) = 2{x} − 1 for {XR}, {x} &gt; 3&nbsp;&nbsp;&nbsp;&nbsp;g({x}) = {x}<sup>2</sup> − 2 for {XR}, {x} &gt; 7', cols=1,
      parts=[('a', 'Find the range of&nbsp;&nbsp; i&nbsp; f(<i>x</i>)&nbsp;&nbsp;&nbsp; ii&nbsp; g(<i>x</i>)', 'Ranges:'), ('b', 'Find gf(<i>x</i>).', 'gf(x) ='),
             ('c', 'Find the domain and range of gf(<i>x</i>).', 'Domain and range:')],
      dyna=[('Starter', f'Begin part c by asking: which inputs does g accept? Then you need f({x}) to be one of them.'),
            ('Vault', 'Use the pattern from Q 19: the domain of gf is the inputs of f whose outputs lie in the domain of g.')],
      turn='Solve the inequality, then find the range of gf.'),
 dict(n=21, text=f'f({x}) = 3{x} + 2 for {XR}, {x} &gt; 1&nbsp;&nbsp;&nbsp;&nbsp;g({x}) = {x}<sup>2</sup> + 1 for {XR}, {x} &gt; 8', cols=1,
      parts=[('a', 'Find the range of&nbsp;&nbsp; i&nbsp; f(<i>x</i>)&nbsp;&nbsp;&nbsp; ii&nbsp; g(<i>x</i>)', 'Ranges:'), ('b', 'Find gf(<i>x</i>).', 'gf(x) ='),
             ('c', 'Find the domain and range of gf(<i>x</i>).', 'Domain and range:')],
      dyna=[('Echo', f'Say part c in words: “Which {x} greater than 1 give f({x}) greater than 8?”'),
            ('Translator', 'Solve 3x + 2 &gt; 8. Then put the smallest f-output into g to see where the range of gf starts.')],
      turn='Write the domain and range of gf.'),
]
SPOT = None

# Supplementary (Atul's rules, 26 Nov 2026): only bank questions within the scope of the coursebook text before the
# exercise (Section 1.3: fg means g first, then f; fg(x) and gf(x) differ; f^2(x) = ff(x); fg exists only where the range
# of g lies in the domain of f; building, evaluating and solving with composites of polynomial, rational and root
# functions) and of comparable hardness. Fewer than 10 is fine.
# Banks: "1_Functions_Obj" (64186, 2771) and "Relation and Functions Obj" (74898, 109055, 73374).
# Wording and options exactly as in the bank; Q-IDs read from the report pages.
# Bank answers (never printed), each checked by hand and with SymPy, with the coursebook question it matches:
# 64186 B (L4; ff(x) = x^4 - 2x^3 + 2x^2 - x + 1 ~ Worked example 4c, Q 3), 74898 A (L3; ff(x) = (2x + 1)/(2x + 3) ~ Q 3, 16),
# 2771 C (L3; fg = gf needs ad + b = cb + d, that is f(d) = g(b) ~ Q 1, 2, 6), 109055 B (L4; t^2 + t - 1 = -5/4 gives
# t = -1/2 ~ Q 7 to 12), 73374 D (L3; ff(x) = x for all x needs alpha = -1 ~ Q 10).
# Left out: greatest-integer, trig, log and modulus composites (47832, 142605, 74899, 47845, 91589, 142582),
# onto / injective (73180), inverse (74254: gof = I, Section 1.6), relation composition (88757, 88755),
# 142987 (a number puzzle, harder than the exercise), duplicates of 73374 (85404, 47831, 91721, 64592, 80334).
SUPP = [
 dict(n=1, qid='64186', text='If <i>f</i> : R → R is defined by <i>f</i>(x) = x<sup>2</sup> − x + 1, then (<i>f</i> o <i>f</i>) (x) is'.replace('→', TO),
      opts=['2x<sup>4</sup> − 2x<sup>2</sup> + 2', 'x<sup>4</sup> − 2x<sup>3</sup> + 2x<sup>2</sup> − x + 1', 'x<sup>4</sup> − 4x<sup>3</sup> + 2x<sup>2</sup> − x + 3', 'x<sup>4</sup> − x<sup>2</sup> + 1'], raw=True,
      hint=[('Echo', 'Say it in words: f o f means do f, then do f again. It is f<sup>2</sup>(x), as in Worked example 4.'),
            ('Slicer', 'Put x<sup>2</sup> − x + 1 in place of every x in f. Expand the square first, then collect like terms.')]),
 dict(n=2, qid='74898', text=f'If <i>f</i>(x) = {fr("1", "2x + 1")} then find <i>f</i>(<i>f</i>(x))',
      opts=[fr('2x + 1', '2x + 3'), fr('x + 1', '2x + 3'), '−x', fr('1 − x', 'x + 3')], raw=True,
      hint=[('Starter', 'Begin with the inside: f(x) is the fraction 1 over 2x + 1. Put that whole fraction in place of x in 2x + 1.'),
            ('Vault', 'To tidy a fraction inside a fraction, multiply its top and bottom by 2x + 1.')]),
 dict(n=3, qid='2771', text='If f(x) = (ax + b) and g(x) = cx + d, then f[g(x)] = g[f(x)] if and only if :',
      opts=['f(a) = g(c)', 'f(b) = g(b)', 'f(d) = g(b)', 'f(c) = g(a)'],
      hint=[('Translator', 'Write f(g(x)) and g(f(x)) as expressions in x. Both are straight lines.'),
            ('Roots', 'The x-terms already match: both are acx. Ask why only the constant terms now need to be equal, then compare them with each option.')]),
 dict(n=4, qid='109055', text=f'If g(x) = x<sup>2</sup> + x − 1 and (gof)(x) = 4x<sup>2</sup> − 10x + 5, then f({fr("5", "4")}) is equal to:',
      opts=['−' + fr('3', '2'), '−' + fr('1', '2'), fr('1', '2'), fr('3', '2')], raw=True,
      hint=[('Bridge', 'Like a parcel that went through two machines: you know the final output, so work back to what the first machine gave out.'),
            ('Starter', 'Begin by putting x = 5/4 into 4x<sup>2</sup> − 10x + 5. Then call f(5/4) = t and solve t<sup>2</sup> + t − 1 = that value.')]),
 dict(n=5, qid='73374', text=f'Let f(x) = {fr(ALPHA + "x", "x + 1")}, x {NE} −1. Then for what value of {ALPHA} is f(f(x)) = x ?',
      opts=['√2', '−√2', '1', '−1'],
      hint=[('Translator', 'Write f(f(x)) as one fraction, simplify it, and set it equal to x.'),
            ('Roots', f'It must be true for every x, so both sides must match term by term. Ask which value of {ALPHA} removes the x-term from the bottom.')]),
]

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1, 2], True, 'space'), ('questions', [3, 4, 5], False, 'space'), ('questions', [6, 7, 8], False, 'space'),
    ('questions', [9, 10, 11], False, 'space'), ('questions', [12, 13, 14]), ('questions', [15, 16, 17], False, 'space'),
    ('questions', [18, 19], False, 'space'), ('questions', [20, 21], False, 'spaceqr'),
    ('supp', [1, 2, 3], True, 'space'), ('supp', [4, 5], False, 'howdid+space'),
]
