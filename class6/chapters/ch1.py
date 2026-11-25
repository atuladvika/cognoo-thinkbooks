"""Class 6, Chapter 1: Patterns in Mathematics. Content for the chapter pages.
Answers (TH = TB): Q1 a, Q2 b, Q3 d, Q4 b, Q5 d, Q6 c, Q7 c, Q8 c, Q9 a, Q10 c, Thinking Spot d. Never printed.
Supplementary: the 10 questions and Q-IDs of the Dynamind Chapter 1 assessment (A00011400), in its order.
Two of them (105956, 106017) differ from the TB list (which had 107493 and 107560)."""

CH = dict(
    num=1, title='Patterns in Mathematics', first_page=10,
    lecture_qr='CGN000020', dyna_qr='CGN000005',
    count_line='10 questions + 1 Thinking Spot · Goes with Chapter 1 of your CBSE Computational Thinking Student Handbook',
)

KNOW = [
    '<b>Gaps:</b> in a number series, look at the gaps. 2, 5, 8, 11 grows by 3 each time.',
    '<b>Square numbers:</b> 1, 4, 9, 16, 25 are 1 × 1, 2 × 2, 3 × 3, 4 × 4, 5 × 5.',
    '<b>Positions:</b> the 6th term is the 6th place in the series, counting from the first.',
    '<b>Groups:</b> a long series can be read in small groups, like 1-2-3, 4-5-6.',
]

BARS = [
    ('Pattern Recognition', 'find what repeats', 3, '#007ea2', 'Q 1, 3, 4'),
    ('Generalisation', 'find the rule for any term', 2, '#05ccab', 'Q 7, 9'),
    ('Algorithmic Thinking', 'follow steps in order', 1, '#05ccab', 'Thinking Spot'),
    ('Number Series <span style="font-weight:400">(verbal)</span>', 'series reasoning, not a CT skill', 2, '#cccccc', 'Q 2, 8'),
    ('Other reasoning', 'puzzles, not CT skills', 3, '#cccccc', 'Q 5, 6, 10'),
]
ALSO = ['Number Series · Q 1, 4, 7, 9, 10', 'Trouble Shooting · Q 2', 'Coding-Decoding · Q 3', 'Magic Circles &amp; Squares · Q 5',
        'Decomposition · Q 6', 'Wrong Number Series · Q 8', 'Logical Diagrams · Spot']

ROUTINE = [('READ', 'What is given? Read the <b>Note</b> too.'),
           ('MARK', 'Underline what is asked. Number the clues.'),
           ('WRITE', 'Write the gaps between the terms.'),
           ('CHECK', 'Test every option against the rule.')]
WATCH_SUB = 'The pattern rule changes from question to question.'
WATCH = [
    ('Q 1', 'Count only the <b>NEXT 20</b> terms.', 'The terms already shown do not count.'),
    ('Q 2', 'Exactly <b>one</b> term is wrong.', 'Fix it and every later term should fit.'),
    ('Q 3', 'Each term is a <b>group</b>, not one number.', 'The symbols stand in for some numbers.'),
    ('Q 7', 'Hexagons and diamonds grow by <b>different</b> rules.', 'Count both in every term.'),
    ('Q 10', '<b>At most</b> 30 cubes.', 'Using fewer than 30 cubes is allowed.'),
]
TRYONE = dict(
    q='<b>What comes next?</b> 1, 2, 4, 7, 11, 16, ?',
    opts=['a) 20', 'b) 21', 'c) 22', 'd) 23'],
    hints=[('Echo', 'Say it in your own words: "Each number grows from the one before. By <b>how much</b> each time?"'),
           ('Translator', 'Write the gaps under the series. Now the gaps make a series of their own.'),
           ('Roots', 'Ask why the gaps change. Is there a rule hiding in the gaps?')],
    turn='Find the next gap, then add it to 16.',
)
BEFORE = 'There is no activity in this chapter. Keep a pencil ready to write the gaps under each series.'
AHEAD = 'The Thinking Spot is a three-shot puzzle: plan your shots to remove as many items as you can.'

SK = {
    'Bridge': 'connect to everyday life', 'Starter': 'decide how to begin', 'Slicer': 'break it into small parts',
    'Echo': 'say it in your own words', 'Vault': 'pick what you already know', 'Roots': 'ask why it works',
    'Translator': 'turn words into numbers, pictures or steps'}
SQ = {
    'Bridge': 'What does this remind me of from my everyday life?', 'Starter': 'Where do I begin? Which clue is the easiest to use first?',
    'Slicer': 'Can I break this into small steps and solve one step at a time?', 'Echo': 'Can I say this question again in my own words?',
    'Vault': 'What do I already know that can help me here?', 'Roots': 'Why does this work? What is the rule hiding behind it?',
    'Translator': 'Can I turn the words into numbers, a drawing or a list of steps?'}

Q = [
 dict(n=1, text='The following series follows a fixed pattern:<br>2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, …<br>If the pattern continues, determine how many times the number 9 appears in the NEXT 20 terms.',
      opts=['3', '4', '7', '8'],
      dyna=[('Translator', 'Turn the series into a rule. Write each number with how many times it appears: 2 once, 3 twice, 4 three times, and so on.'),
            ('Slicer', 'Split the next 20 terms into blocks: the 6s still to come, then all the 7s, then all the 8s. Count each block.')],
      turn='How many places are left for 9s?'),
 dict(n=2, text='The following number series is based on a pattern. One term is incorrect. Identify the incorrect term.<br>2, 3, 6, 11, 18, 25, 38, 51, 66, 83',
      opts=['11', '25', '51', '66'],
      dyna=[('Translator', 'Write the gaps under the series. What pattern do most of the gaps follow?'),
            ('Roots', 'Ask which <b>single</b> term, if changed, makes every gap fit. Check the terms after it too.')],
      turn='Name the term you would change.'),
 dict(n=3, text='What will come in place of "?" in the given series?<br>1@3, #5#, 7@9, #11#, 13@15, ?, 19@21',
      opts=['@17@', '#15#', '16#18', '#17#'],
      dyna=[('Slicer', 'Break each term into three parts and read them as numbers: 1@3 hides 1, 2, 3. Which numbers hide in #5#?'),
            ('Roots', 'Ask <b>why</b> some terms use @ and others use #. Does it depend on whether the term is 1st, 2nd, 3rd and so on?')],
      turn='Build the 6th term with the right numbers and symbols.'),
 dict(n=4, text='The first four terms of a block series are shown below. If the pattern continues in the same manner, which term of the series will be the first to contain more than 20 blocks?',
      fig=[('q4', 202)], opts=['5th term', '6th term', '7th term', '8th term'],
      dyna=[('Bridge', 'Picture building stairs with toy blocks: each new term adds a longer row at the bottom.'),
            ('Translator', 'Write the number of blocks in each term. What do you add each time?')],
      turn='Keep adding until the total goes past 20. Which term is it?'),
 dict(n=5, text='What will come in place of "?" in the given series?',
      fig=[('q5_main', 300)], img_opts=[('q5_a', 47), ('q5_b', 47), ('q5_c', 47), ('q5_d', 47)], opt_h=47,
      dyna=[('Slicer', 'Follow one corner at a time. The top-left numbers go 1, 2, 3, 4. Do the same for the other three corners.'),
            ('Echo', 'Say in your own words what happens to every number from one term to the next. Do the grey squares move?')],
      turn='Write the next number for each corner. Match both the numbers and the grey squares.'),
 dict(n=6, text='What will come in place of "?" in the given series?',
      fig=[('q6_main', 200)], img_opts=[('q6_a', 28), ('q6_b', 30), ('q6_c', 30), ('q6_d', 30)], opt_h=72,
      dyna=[('Slicer', 'Treat the top circles, the bottom circles and the middle squares as three separate series.'),
            ('Translator', 'Write the gaps for the top and the bottom series. Then compare each middle number with the two numbers above and below it.')],
      turn='Work out the next top, bottom and middle numbers.'),
 dict(n=7, text='The first five terms of a series formed using grey hexagons and white diamonds are given below. If the same pattern continues, how many diamonds will be present in the term where the number of hexagons is 144?',
      fig=[('q7', 300)], opts=['100', '135', '121', '169'],
      dyna=[('Translator', 'Make a table: term 1, 2, 3, 4, 5, with the number of hexagons and of diamonds in each.'),
            ('Roots', 'Ask why the counts grow that way. The hexagons make a square, n by n. What size of square do the diamonds make?')],
      turn='Find the term with 144 hexagons. Count its diamonds.'),
 dict(n=8, text='Given below are two sets of numbers, P and Q. Which number from Set P can be interchanged with a number from Set Q such that both new sets follow a particular series or pattern?<br>Set P: (18, 22, 24, 27, 30)<br>Set Q: (21, 24, 27, 31, 36)',
      opts=['18', '27', '22', '30'],
      dyna=[('Starter', 'Begin with Set P: most of it goes up by the same step. Which number breaks that step?'),
            ('Slicer', 'Then check Set Q. Which of its numbers would fill the gap in P? Does Q still follow a pattern after the swap?')],
      turn='Name the number from Set P that should move.'),
 dict(n=9, text='The first three terms of a series of circles are shown below. If the pattern continues in the same manner, how many circles will be there in term 91?',
      fig=[('q9', 246)], opts=['184', '180', '194', '204'],
      dyna=[('Translator', 'Count the circles in terms 1, 2 and 3 and write them in a table. How many columns of circles does each term have?'),
            ('Vault', 'Remember: once you have a rule for term n, you can jump straight to any term without drawing it.')],
      turn='Use your rule for term 91.'),
 dict(n=10, text='A pyramid has to be formed by combining cubes. Every level will have two fewer cubes than the level below it. If a pyramid is formed using at most 30 cubes, what is the maximum number of levels it can have?',
      opts=['3', '4', '5', '6'],
      dyna=[('Bridge', 'Picture stacking blocks with the widest level at the bottom. To fit more levels, should the top level be big or small?'),
            ('Slicer', 'Start from the smallest top level and add levels one at a time, keeping a running total. Stop before you pass 30.')],
      turn='Count the levels you managed.'),
]
SPOT = dict(
    text='You must shoot exactly one item from each box, to eliminate it from its box. When an item is shot, the same item in the adjacent box is also eliminated. What is the MAXIMUM number of items that can be eliminated, after all 3 shots?',
    fig=[('ts_main', 196)], opts=['4', '5', '6', '7'],
    dyna=[('Starter', 'Begin with the shape found in all three boxes. In which box should you shoot it to remove the most?'),
          ('Slicer', 'Plan the other two shots one at a time. Each shot can also remove the same item in a box next to it.')],
    turn='Add up the items removed by your three shots.')

SUPP = [
 dict(n=1, qid='108335', text='Thirty six vehicles are parked in a parking lot in a single row. After the first car, there is one scooter. After the second car, there are two scooters. After the third car, there are three scooters, and so on. Work out the number of scooters in the second half of the row.',
      opts=['10', '12', '15', '17'], hint=['Translator', 'Slicer']),
 dict(n=2, qid='105956', text='Find out the wrong term:<br>15, 16, 22, 29, 45, 70', opts=['16', '22', '45', '70'], hint=['Translator', 'Roots']),
 dict(n=3, qid='107446', text='What is the missing number in the following sequence?<br>8, 6, 24, 7, 3, 21, 5, 4, 20, …, 9, 18', opts=['1', '3', '4', '5', '6'], hint=['Slicer', 'Roots']),
 dict(n=4, qid='105905', text='Find the missing number in the series.<br>1, 3, 6, 10, 15, …, 28, 36', opts=['20', '21', '23', '24'], hint=['Translator', 'Roots']),
 dict(n=5, qid='106017', text='Find out the set that does not match with the others.', opts=['3 (58) 7', '1 (10) 3', '2 (20) 4', '5 (51) 6', '8 (145) 9'], hint=['Roots', 'Slicer']),
 dict(n=6, qid='105972', text='Find out the wrong term:<br>25, 36, 49, 81, 121, 169, 225', opts=['36', '49', '169', '225'], hint=['Vault', 'Roots']),
 dict(n=7, qid='107410', text='Which is the number that comes next in the sequence: 0, 6, 24, 60, 120, 210?', opts=['240', '290', '336', '504'], hint=['Translator', 'Roots']),
 dict(n=8, qid='107489', text='Find out the wrong term.<br>1, 5, 5, 9, 7, 11, 11, 15, 12, 17', opts=['11', '12', '17', '15'], hint=['Slicer', 'Echo']),
 dict(n=9, qid='105975', text='Find the missing number in the following series.<br>2, 6, 12, 20, …, 42, 56, 72, 90', opts=['20', '21', '30', '12'], hint=['Translator', 'Starter']),
 dict(n=10, qid='107453', text='Find the wrong number in the series.<br>7, 28, 63, 124, 215, 342, 511', opts=['7', '28', '124', '215'], hint=['Vault', 'Translator']),
]

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1, 2], True, 'space'), ('questions', [3, 4], False, 'space'), ('questions', [5, 6], False, 'space'),
    ('questions', [7, 8], False, 'space'), ('questions', [9, 10], False, 'space'), ('questions', ['spot'], False, 'spaceqr'),
    ('supp', [1, 2, 3, 4, 5], True), ('supp', [6, 7, 8, 9, 10], False, 'howdid'),
]
