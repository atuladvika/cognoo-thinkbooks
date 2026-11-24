"""Class 4, Chapter 1: Shapes Around Us. Content for the chapter pages (opener, questions, supplementary).
Answers (TH = TB): Q1 d, Q2 c, Q3 d, Q4 a, Q5 a, Q6 b, Q7 c, Q8 a, Q9 c, Q10 b, Thinking Spot a. Never printed."""

CH = dict(
    num=1, title='Shapes Around Us', first_page=10,
    lecture_qr='CGN000018', dyna_qr='CGN000003',
    count_line='10 questions + 1 Thinking Spot · Goes with Chapter 1 of your CBSE Computational Thinking Student Handbook',
)

KNOW = [
    '<b>Faces, edges, corners:</b> a cube has 6 faces, 12 edges and 8 corners.',
    '<b>Sides and angles:</b> a triangle has 3 of each, a square 4, a pentagon 5.',
    '<b>Nets:</b> a flat shape made of 6 squares can fold up into a cube.',
    '<b>Touching faces</b> share an edge. <b>Opposite faces</b> never touch, like the top and bottom of a box.',
]

# primary STCA concept of each item (TB mapping)
BARS = [  # (name, tag, count, colour, questions)
    ('Decomposition', 'break it into small parts', 3, '#007ea2', 'Q 4, 7, 10'),
    ('Spatial Reasoning', 'picture shapes in your head', 3, '#007ea2', 'Q 1, 2, 9'),
    ('Algorithmic Thinking', 'follow steps in order', 2, '#05ccab', 'Q 8, Thinking Spot'),
    ('Abstract Thinking', "see what's hidden", 1, '#05ccab', 'Q 3'),
    ('Pattern Recognition', 'find what repeats', 1, '#05ccab', 'Q 6'),
    ('Odd Figure <span style="font-weight:400">(non-verbal)</span>', 'picture reasoning, not a CT skill', 1, '#cccccc', 'Q 5'),
]
ALSO = ['Cubes &amp; Dice · Q 1, 2, 9', 'Spatial Reasoning · Q 3, 7, 10', 'Visual Reasoning · Q 4', 'Pattern Recognition · Q 5',
        'Similar Figures · Q 6', 'Analytical Reasoning · Q 8', 'Seating Arrangement · Spot']

ROUTINE = [('READ', 'What is given? Read the <b>Note</b> too.'),
           ('MARK', 'Underline what is asked. Number the clues.'),
           ('DRAW', 'Sketch the shape. Label its faces or sides.'),
           ('CHECK', 'Test every option against every clue.')]
WATCH_SUB = 'The shape rule changes from question to question.'
WATCH = [
    ('Q 1', 'You <b>cannot rotate</b> the images.', 'A shape lying on its side is a different option.'),
    ('Q 3', 'Count the angles of the <b>piece you keep</b>.', 'A rectangle has 4 angles before any cut.'),
    ('Q 7', '<b>Adjacent</b> means sharing an edge, not just a corner.', 'Faces that meet only at a point may share a colour.'),
    ('Q 9', 'Count the faces you <b>cannot</b> see.', 'A face pressed against another cube is hidden.'),
    ('Q 10', 'Both conditions: yellow at <b>one end</b>, no red at the <b>other</b>.', 'An edge from yellow to red does not count.'),
]
TRYONE = dict(
    q="<b>Ravi's shape:</b> (1) It has 4 sides. (2) All 4 sides are equal. (3) It has no right angle. Which shape is it?",
    opts=['a) Square', 'b) Rectangle', 'c) Rhombus', 'd) Triangle'],
    hints=[('Echo', 'Say it in your own words: "I need one shape that passes <b>all 3</b> clues." Number the clues.'),
           ('Vault', 'What do you know? A square has 4 equal sides and 4 right angles. A rectangle has 4 right angles.'),
           ('Slicer', 'Check one clue at a time. Clue 1 removes the triangle. Clue 2 removes the rectangle.')],
    turn='Two shapes are left. Use clue 3 on them. Which one has no right angle?',
)
BEFORE = 'There is no activity in this chapter. Keep paper, scissors and a few blocks or a dice ready to try the shapes.'
AHEAD = 'The Thinking Spot is a shape-placing puzzle with three rules. Keep your starting routine ready!'

SK = {  # tag lines
    'Bridge': 'connect to everyday life', 'Starter': 'decide how to begin', 'Slicer': 'break it into small parts',
    'Echo': 'say it in your own words', 'Vault': 'pick what you already know', 'Roots': 'ask why it works',
    'Translator': 'turn words into numbers, pictures or steps'}
SQ = {  # simple-words questions
    'Bridge': 'What does this remind me of from my everyday life?', 'Starter': 'Where do I begin? Which clue is the easiest to use first?',
    'Slicer': 'Can I break this into small steps and solve one step at a time?', 'Echo': 'Can I say this question again in my own words?',
    'Vault': 'What do I already know that can help me here?', 'Roots': 'Why does this work? What is the rule hiding behind it?',
    'Translator': 'Can I turn the words into numbers, a drawing or a list of steps?'}

Q = [
 dict(n=1, text='What will come in place of "?"', note='You cannot rotate the images',
      fig=[('q1_main', 169)], img_opts=[('q1_a', 39), ('q1_b', 35), ('q1_c', 52), ('q1_d', 40)], opt_h=62,
      dyna=[('Starter', 'Start with the <b>small shape</b>. Count its cubes: one cube in front and a stack of two behind it. Now find that same group of 3 cubes inside the big shape.'),
            ('Slicer', 'Take the big shape apart in your head. Cover the group you found. Which cubes are left? How tall is the column, and which cubes stick out at its foot?')],
      turn='Match what is left with the options. Remember: you cannot rotate them.'),
 dict(n=2, text='The figure below forms a cube when folded. Which of the following options represents a pair of opposite faces of the cube?',
      note='You cannot rotate the question or option images',
      fig=[('q2_net', 137)], img_opts=[('q2_a', 81), ('q2_b', 82), ('q2_c', 85), ('q2_d', 83)], opt_h=40,
      dyna=[('Translator', 'Turn the net into numbers. Write 1 on the top square, 2, 3, 4 and 5 along the middle row from left to right, and 6 on the bottom square.'),
            ('Vault', 'Use the folding rule you know: two squares in a straight line with <b>exactly one square between them</b> end up opposite each other. List every such pair in your numbered net.')],
      turn='Find the option whose two faces make one of your opposite pairs. Check the yellow parts carefully.'),
 dict(n=3, text='From a rectangular piece of paper, a shape having which of the following number of angles CANNOT be formed by making only a SINGLE STRAIGHT CUT in any direction?',
      opts=['3 angles', '4 angles', '5 angles', '6 angles'],
      dyna=[('Bridge', 'Take a real sheet of paper, or picture one. It has 4 corners. Make one straight cut and count the corners of the piece you keep.'),
            ('Slicer', 'Split the cuts into three kinds: <b>corner to corner</b>, <b>side to the opposite side</b>, and <b>across one corner</b>. Count the angles for each kind.')],
      turn='Which number of angles never showed up in any of your three cuts?'),
 dict(n=4, text='Count the number of TRIANGLES in the image given below.',
      fig=[('q4', 76)], opts=['4', '5', '3', '2'],
      dyna=[('Starter', 'Begin with the <b>corners</b> of the square. Look in each corner for a small space closed by 3 straight lines.'),
            ('Slicer', 'Then check the inside, part by part. Number each space that has 3 sides. Then see if two spaces join to make a bigger triangle.')],
      turn='Count your numbered triangles. Did you check every space only once?'),
 dict(n=5, text='Find the ODD one out.',
      img_opts=[('q5_a', 74), ('q5_b', 68), ('q5_c', 41), ('q5_d', 60)], opt_h=54,
      dyna=[('Echo', 'Say what each shape shows in your own words, for example: "a triangle with T3 written inside". Do this for all four.'),
            ('Roots', 'Ask <b>why</b> T and 3 go with a triangle. What does T stand for? What does 3 count? Test the same rule on S4 and P5.')],
      turn='Which shape breaks your rule?'),
 dict(n=6, text='If each of the given terms follows the same theme, what will come in place of "?"',
      fig=[('q6_main', 133)], img_opts=[('q6_a', 58), ('q6_b', 58), ('q6_c', 63), ('q6_d', 61)], opt_h=55,
      dyna=[('Translator', 'Turn each shape into a number: count its sides. Write Row 1 as three numbers: yellow, white, yellow.'),
            ('Roots', 'Ask why the white middle shape fits. Does adding the two yellow numbers give the middle one? Check that it works for Row 2 too.')],
      turn='Use the same rule on Row 3. Then count the sides of each option.'),
 dict(n=7, text='Each face of a triangular prism is coloured with a colour in such a way that no two adjacent faces have the same colour. What is the MINIMUM number of colours required to do this?',
      note='Two faces are said to be adjacent if they share a common edge',
      opts=['2', '3', '4', '5'],
      dyna=[('Bridge', 'Picture a tent or a Toblerone box: 2 triangle ends and 3 rectangle sides. Faces that share an edge need different colours.'),
            ('Slicer', 'Colour in parts. First the 3 rectangles: does each one touch the other two? Then the front triangle: which faces does it touch? Then the back triangle.')],
      turn='Can the two triangles share a colour? Count the colours you used in all.'),
 dict(n=8, text='Which of these shapes will come in place of A and B, such that no two shapes having the same number of sides, pattern, or colour appear in the same row or column?',
      note='Not all blocks will necessarily have a shape present in them',
      fig=[('q8_main', 121)], img_opts2=[('q8_a', 125), ('q8_b', 125), ('q8_c', 126), ('q8_d', 126)], opt_h=31,
      dyna=[('Starter', 'Begin with <b>A</b>. List what is already in its row and in its column: the number of sides, any pattern and the colour.'),
            ('Slicer', 'Make three checks for each option: sides, pattern, colour. Then do the same for <b>B</b>, using its own row and column.')],
      turn='Cross out any option that fails even one check for A or for B.'),
 dict(n=9, text='Six concrete blocks of cubical shape are used for building the stairs as shown below. How many faces of these blocks are not visible?',
      fig=[('q9', 92)], opts=['12', '15', '21', '24'],
      dyna=[('Translator', 'Turn the picture into a sum. There are 6 cubes and each cube has 6 faces. How many faces are there in all?'),
            ('Slicer', 'Split the stairs into the left column and the right column. For each cube, count the faces you can see: front, top or side?')],
      turn='Take the faces you can see away from all the faces.'),
 dict(n=10, text='How many edges of the pyramid shown below have a yellow dot at one of their corners but do not have a red dot on the other corner?',
      fig=[('q10', 119)], opts=['1', '2', '3', '4'],
      dyna=[('Vault', 'Recall a pyramid with a square base: 4 corners on the base, 1 corner at the top, and 8 edges in all.'),
            ('Slicer', 'Take one yellow dot at a time. Follow each edge that leaves it. What is at the other end: red, yellow or no dot?')],
      turn='Count only the edges whose other end has no red dot.'),
]
SPOT = dict(
    text='All the shapes of Set A must be placed into the squares present in Box 1, such that'
         '<ul><li>Each square has EXACTLY ONE shape</li><li>The shape and the square CANNOT be of the same colour</li>'
         '<li>Two squares connected by a line CANNOT have the same shape inside them</li></ul>'
         'Which option shows the shapes which are NOT next to each other in the final arrangement?',
    fig=[('ts_main', 272)], img_opts=[('ts_a', 35), ('ts_b', 35), ('ts_c', 32), ('ts_d', 34)], opt_h=15,
    dyna=[('Starter', 'Begin with the square that has the <b>most lines</b> joined to it. What colour of shape can it hold?'),
          ('Slicer', 'Place one shape at a time. Black squares take white shapes, and joined squares cannot hold the same shape. If a choice gets stuck, go back and try the other one.')],
    turn='Write your final row of 6 shapes. Then check each option: are the two shapes side by side?')

SUPP = [
 dict(n=1, qid='108117', text='A dice is thrown four times and its four different positions are given below. What number is on the face opposite 4?',
      fig=[('s1', 172)], opts=['1', '2', '3', '5'], hint=['Starter', 'Slicer']),
 dict(n=2, qid='108120', text='The figure is folded to form a box. Choose from among the alternatives the box or boxes that can be formed by folding the figure.',
      fig=[('s2', 146)], opts=['Both II and IV', 'Both I and II', 'IV only', 'Both II and III'], hint=['Vault', 'Translator']),
 dict(n=3, qid='108121', text='The figure is folded to form a box. Choose from among the alternatives the box or boxes that can be formed by folding the figure.',
      fig=[('s3', 131)], opts=['II, III and IV', 'III and IV only', 'II and III only', 'I and IV only'], hint=['Translator', 'Slicer']),
 dict(n=4, qid='108124', text='A dice is thrown 3 times and its 3 positions are given below. Which number is opposite 1?',
      fig=[('s4a', 39), ('s4b', 38), ('s4c', 38)], fig_gap=0, opts=['2', '3', '4', '6'], hint=['Starter', 'Vault']),
 dict(n=5, qid='108110', text='The six faces of a cube are coloured black, brown, green, red, white and blue, such that (i) red is opposite black, (ii) green is between red and black, (iii) blue is adjacent to white, (iv) brown is adjacent to blue and (v) red is at the bottom. Which three colours are adjacent to each other?',
      fig=[('s5', 177)], opts=['Black, Blue, Red', 'Black, Brown, White', 'Black, Blue, White', 'Brown, Red, White'], hint=['Slicer', 'Translator']),
 dict(n=6, qid='108099', text='A wooden cube is painted blue on all four sides and green on the top and bottom. It is then cut at equal distances four times vertically (top to bottom) and two times horizontally, as shown in the figure, where the dotted lines are the cuts. How many cubes will have no face painted at all?',
      fig=[('s6', 105)], opts=['1', '2', '3', '4'], hint=['Translator', 'Slicer']),
 dict(n=7, qid='108107', text='125 cubes of the same size are arranged in the form of a cube on a table. Then a column of five cubes is removed from each of the four corners. All the exposed faces of the rest of the solid (except the face touching the table) are coloured red. How many cubes have only one red face each?',
      opts=['40', '25', '20', '15'], hint=['Slicer', 'Roots']),
 dict(n=8, qid='108180', text='Out of these four figures, one figure is different, while three figures are similar in some way. Find the odd one out.',
      img_opts=[('s8a', 34), ('s8b', 34), ('s8c', 34), ('s8d', 34)], opt_h=34, hint=['Roots', 'Echo']),
 dict(n=9, qid='108181', text='Out of these four figures, one figure is different, while three figures are similar in some way. Find the odd one out.',
      img_opts=[('s9a', 37), ('s9b', 37), ('s9c', 37), ('s9d', 37)], opt_h=37, hint=['Roots', 'Vault']),
 dict(n=10, qid='107673', text='Four young men, Raj, Sunder, Tarun and Upal, are married to Rekha, Sunita, Tara and Uma, and the couples live in Rampur, Sanchi, Tirupati and Udhampur.'
      '<br>(I) The first letters of the names of a man, his wife and their city do not match.<br>(II) Sunita is not Raj\'s wife.'
      '<br>(III) Sunder does not live in Rampur or Udhampur and is not Rekha\'s husband.<br>(IV) Upal and Tara do not live in Sanchi.'
      '<br>Which pair given below is the right combination of wife and city for Tarun?',
      opts=['Sunita, Tirupati', 'Tara, Sanchi', 'Uma, Rampur', 'Rekha, Sanchi'], hint=['Starter', 'Slicer']),
]

PAGES = [  # page number: what goes on it
    ('opener1',), ('opener2',),
    ('questions', [1], True, 'space'), ('questions', [2, 3], False, 'space'), ('questions', [4, 5], False, 'space'), ('questions', [6, 7], False, 'space'),
    ('questions', [8, 9]), ('questions', [10, 'spot'], False, 'spaceqr'),
    ('supp', [1, 2, 3], True), ('supp', [4, 5, 6]), ('supp', [7, 8, 9, 10], False, 'howdid'),
]
