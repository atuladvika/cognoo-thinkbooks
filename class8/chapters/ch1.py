"""Class 8, Chapter 1: A Square and a Cube. Content for the chapter pages.
Answers (TB): Q1 c, Q2 b, Q3 a, Q4 b, Q5 c, Q6 d, Q7 a, Q8 a, Q9 d, Q10 b, Thinking Spot b. Never printed.
Supplementary: the 10 questions and Q-IDs of the Dynamind Chapter 1 assessment (A00011405), in its order;
the same 10 as the TB list. Answers: 1 b, 2 b, 3 c, 4 d, 5 c, 6 c, 7 c, 8 c, 9 d, 10 b.
Supplementary figures (Q1 circles, Q8 and Q10 grids) are retyped from the scan, which is low resolution."""

CH = dict(
    num=1, title='A Square and a Cube', first_page=10,
    lecture_qr='CGN000022', dyna_qr='CGN000007',
    count_line='10 questions + 1 Thinking Spot · Goes with Chapter 1 of your CBSE Computational Thinking Student Handbook',
)

KNOW = [
    '<b>Squares:</b> 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 are 1<sup>2</sup> to 10<sup>2</sup>.',
    '<b>Cubes:</b> 1, 8, 27, 64, 125, 216 are 1<sup>3</sup> to 6<sup>3</sup>. 1 and 64 are both squares and cubes.',
    '<b>Prime factors:</b> in a perfect cube every prime comes in groups of three: 216 = 2 × 2 × 2 × 3 × 3 × 3.',
    '<b>Last digits:</b> the last digit of a square or cube depends only on the last digit of the number.',
]

BARS = [
    ('Pattern Recognition', 'find what repeats', 4, '#007ea2', 'Q 1, 3, 5, 10'),
    ('Decomposition', 'break it into small parts', 2, '#05ccab', 'Q 4, Spot'),
    ('Generalisation', 'find the rule for any case', 2, '#05ccab', 'Q 6, 7'),
    ('Algorithmic Thinking', 'follow steps in order', 2, '#05ccab', 'Q 8, 9'),
    ('Abstract Thinking', 'keep only what matters', 1, '#05ccab', 'Q 2'),
]
ALSO = ['Missing Numbers · Q 1, 9, 10', 'Logical Diagrams · Q 2', 'Analytical Reasoning · Q 3, 6, 8, Spot',
        'Substitution · Q 4, 5', 'Completing the Series · Q 7']

ROUTINE = [('READ', 'What is given? Read every rule.'),
           ('MARK', 'Underline what is asked. Number the rules.'),
           ('WRITE', 'Write the squares and cubes you need.'),
           ('CHECK', 'Test every option against all the rules.')]
WATCH_SUB = 'Read the words in capitals twice.'
WATCH = [
    ('Q 2', 'The <b>MINIMUM</b> number of <b>distinct</b> numbers.', 'Some numbers are both a square and a cube.'),
    ('Q 3', 'The cube has <b>4 digits</b>.', 'So AB can only be from 10 to 21.'),
    ('Q 4', 'The <b>smallest</b> k.', '56 already has some of the factors.'),
    ('Q 6', 'The <b>remainder</b> when divided by 100.', 'Look only at the last two digits.'),
    ('Q 8', 'Shape A <b>without rotation</b>.', 'Do not turn the shape.'),
]
TRYONE = dict(
    q='Which of these is <b>both</b> a perfect square and a perfect cube?',
    opts=['a) 16', 'b) 27', 'c) 64', 'd) 100'],
    hints=[('Vault', 'What do I already know? The cubes are 1, 8, 27, 64, 125.'),
           ('Slicer', 'Check each option twice: is it a square? Is it a cube?'),
           ('Roots', 'Ask what such a number needs: its prime factors must come in groups of 2 <b>and</b> in groups of 3.')],
    turn='Name the option that passes both checks.',
)
BEFORE = 'There is no activity in this chapter. Keep a list of squares up to 15 × 15 and cubes up to 10 × 10 × 10 ready.'
AHEAD = 'The Thinking Spot is a stacked-box puzzle: fill the columns one box at a time, using every rule.'

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
 dict(n=1, text='In the following grid, all the circles follow the same theme. What will be the value of A + B?',
      fig=[('q1', 125)], opts=['12', '14', '13', '15'],
      dyna=[('Slicer', 'Take one circle at a time. Which grey numbers does the circle with 25 touch? How can 4 and 3 make 25?'),
            ('Roots', 'Ask why the rule works for every circle: check it on 13 and 106 too. Then use it to find B, and after that A.')],
      turn='Find B from 117, then A from 85. Add them.'),
 dict(n=2, text='Sam writes a list of natural numbers. The list has three perfect cubes and three perfect squares. If no number in the list has more than two digits, what is the MINIMUM number of distinct numbers he must have written?',
      opts=['3', '4', '5', '6'],
      dyna=[('Vault', 'List what you know: the squares up to 99, and the cubes up to 99.'),
            ('Echo', 'Say it in your own words: "Which numbers can count as a square <b>and</b> a cube at the same time?"')],
      turn='Use those numbers first. How many more do you need?'),
 dict(n=3, text='If AB is a two-digit number whose cube is in the form of a 4-digit number “_ _ _ C” such that A &lt; C &lt; B, how many different values can C have?',
      opts=['2', '3', '4', 'More than 4'],
      dyna=[('Starter', 'Begin with the size: which two-digit numbers have a 4-digit cube? Try 10<sup>3</sup> and 22<sup>3</sup>.'),
            ('Roots', 'Ask why only the last digit matters: the last digit of a cube comes from the last digit of the number. When is it smaller?')],
      turn='Check each possible AB against A &lt; C &lt; B.'),
 dict(n=4, text='56 × k is a perfect cube where k is a natural number. What could be the smallest possible value of k?',
      opts=['36', '49', '56', '72'],
      dyna=[('Slicer', 'Break 56 into prime factors: 56 = 2 × 2 × 2 × 7.'),
            ('Vault', 'Remember: in a perfect cube every prime factor comes in groups of three. Which group is not complete?')],
      turn='Multiply the missing factors to get k.'),
 dict(n=5, text='Each geometrical shape denotes a certain operation. What will come in place of “?”',
      fig=[('q5', 190)], opts=['2888', '1914', '1924', '340'],
      dyna=[('Translator', 'Turn each shape into an operation: what does a square do to 16? What does a cube do to 15?'),
            ('Slicer', 'Work out the square part and the cube part separately, then add.')],
      turn='Calculate both parts and add them.'),
 dict(n=6, text='XYZ is a 3-digit number such that it is the square of a multiple of 5. What will be the HIGHEST possible remainder of (XYZ)/100?',
      opts=['10', '15', '20', '25'],
      dyna=[('Starter', 'Begin with the list: which multiples of 5 have a 3-digit square?'),
            ('Roots', 'Ask why the last two digits repeat: what do squares of numbers ending in 0 end with? And ending in 5?')],
      turn='The remainder is the last two digits. Pick the highest.'),
 dict(n=7, text='A class teacher wrote the following pattern on the board, where an expression is written after the “=” sign in each row. She then asked the class to find the expression for 13<sup>3</sup> − 12<sup>3</sup>. Which DIGIT appears the HIGHEST number of times in the expression that denotes 13<sup>3</sup> − 12<sup>3</sup>?',
      fig=[('q7', 140)], opts=['1', '2', '3', '4'],
      dyna=[('Echo', 'Say each row in your own words: "1 plus the two numbers multiplied, times 3."'),
            ('Translator', 'Write the same rule for 13<sup>3</sup> − 12<sup>3</sup> as an expression, exactly in the board’s form.')],
      turn='Count each digit in your expression.'),
 dict(n=8, text='Fill in the grid with the squares and cubes of digits 2 to 5 such that:<br>• Each square/cube number appears twice<br>• Both square and cube of the same number cannot appear in the same row/column<br>• Same numbers do not appear diagonally<br>What is the maximum possible sum that can be obtained by the cells present in the configuration of Shape A (without rotation)?',
      fig=[('q8', 130)], opts=['197', '161', '193', '216'],
      dyna=[('Starter', 'Begin with the rows that are almost full. Which number can still go in each empty cell?'),
            ('Slicer', 'Place one pair at a time: 4 and 8, 9 and 27, 16 and 64, 25 and 125. Check the rules after each one.')],
      turn='Slide Shape A over the filled grid. Where is its sum largest?'),
 dict(n=9, text='The image below shows a logic machine, where numbers move from Column to Column (starting from column 1 as input and reach column 4) through the tunnel, where they change in a different way, each time. What would be the sum of A, B, and C?',
      fig=[('q9', 215)], opts=['2259', '1795', '180', '1788'],
      dyna=[('Slicer', 'Study one tunnel at a time. What does the red tunnel do to 4 to make 15? Check it on 22 and 11.'),
            ('Translator', 'Write each tunnel as a rule, like "square it, take away 1". Then send 7 through all three.')],
      turn='Find A, B and C, and add them.'),
 dict(n=10, text='Every column follows a certain rule. What number should come in place of “?”',
      fig=[('q10', 130)], opts=['17', '18', '19', '21'],
      dyna=[('Bridge', 'Think of a square tile with area 16 × 9. How long is its side?'),
            ('Roots', 'Ask how the bottom number is linked to the two above it. Test your idea on all three full columns.')],
      turn='Use the rule on 12 and 27.'),
]
SPOT = dict(
    text='Boxes are stacked in four columns A, B, C, and D, such that:<br>• Each box is labelled with a number from 1, 2, and 3, with labels on some of the boxes already shown in the image given below<br>• No two adjacent boxes in the same column are labelled with the same number<br>• No two adjacent columns have the same number on the topmost box<br>• For every column, the sum of the numbers labelled on the topmost and bottommost block is equal<br>In the shaded boxes, which of these numbers will occur the HIGHEST number of times?',
    fig=[('ts_main', 95)], opts=['1', '2', '3', 'All of them occur equally'],
    dyna=[('Starter', 'Begin with column C: it has only two boxes, and the top one is 2. What can the bottom one be?'),
          ('Slicer', 'Once you know the top + bottom total, fill the columns one at a time: D, then B, then A.')],
    turn='Count the 1s, 2s and 3s in the shaded boxes.')

SUPP = [
 dict(n=1, qid='107520', text='Study the following numbers carefully and find the missing number (?).',
      fig=[('s1', 190)], opts=['24', '26', '28', '22'], hint=['Slicer', 'Roots']),
 dict(n=2, qid='108617', text='Numbers given in four out of the five alternatives have some relationship. Choose the one which does not belong to the group.',
      opts=['4', '8', '16', '9', '25'], hint=['Vault', 'Echo']),
 dict(n=3, qid='107438', text='Find the next number of the series:<br>−2, 4, 22, 58, 118, 208', opts=['118', '210', '334', '298'], hint=['Translator', 'Vault']),
 dict(n=4, qid='105552', text='Find the missing number:<br>√1296 ÷ ? = ? ÷ 2.25', opts=['6', '7', '8', '9'], hint=['Translator', 'Vault']),
 dict(n=5, qid='108361', text='If × means ÷, − means ×, ÷ means + and + means −, then<br>(3 − 15 ÷ 19) × 8 + 6 = ?', opts=['8', '4', '2', '−1'], hint=['Translator', 'Slicer']),
 dict(n=6, qid='108614', text='Numbers given in four out of the five alternatives have some relationship. Choose the one which does not belong to the group.',
      opts=['3 : 8', '6 : 35', '7 : 50', '1 : 0', '9 : 80'], hint=['Roots', 'Vault']),
 dict(n=7, qid='108276', text='Find the missing number:<br>2, 12, 36, 80, 150, ?', opts=['194', '210', '252', '258'], hint=['Slicer', 'Roots']),
 dict(n=8, qid='107517', text='Study the following number grid carefully and find the missing number (?).',
      fig=[('s8', 90)], opts=['729', '1331', '−729', '−343'], hint=['Roots', 'Echo']),
 dict(n=9, qid='107676', text='Four out of the five pairs of numbers have the same relationship. Find the odd-man out.',
      opts=['4 : 63', '1 : 0', '5 : 124', '2 : 15', '3 : 26'], hint=['Translator', 'Roots']),
 dict(n=10, qid='107515', text='Study the following number grid carefully and find the missing number (?).',
      fig=[('s10', 90)], opts=['36', '9', '25', '64'], hint=['Slicer', 'Roots']),
]

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1], True, 'space'), ('questions', [2, 3, 4], False, 'space'), ('questions', [5, 6], False, 'space'),
    ('questions', [7, 8], False, 'space'), ('questions', [9, 10], False, 'space'), ('questions', ['spot'], False, 'spaceqr'),
    ('supp', [1, 2, 3, 4], True), ('supp', [5, 6, 7], False, 'space'), ('supp', [8, 9, 10], False, 'howdid'),
]
