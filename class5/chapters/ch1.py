"""Class 5, Chapter 1: We the Travellers – I. Content for the chapter pages.
Answers (TH = TB): Q1 c, Q2 b, Q3 c, Q4 b, Q5 d, Q6 d, Q7 b, Q8 c, Q9 c, Q10 c, Thinking Spot a. Never printed."""

CH = dict(
    num=1, title='We the Travellers – I', first_page=10,
    lecture_qr='CGN000019', dyna_qr='CGN000004',
    count_line='10 questions + 1 Thinking Spot · Goes with Chapter 1 of your CBSE Computational Thinking Student Handbook',
)

KNOW = [
    '<b>Place value:</b> in 47253 the 4 stands for 40000 and the 3 for 3 ones.',
    '<b>Odd and even:</b> a number is even when its units digit is 0, 2, 4, 6 or 8.',
    '<b>Largest and smallest:</b> digits in descending order give the largest number.',
    '<b>First digit:</b> a 5-digit number cannot start with 0. 01234 is really 1234.',
]

BARS = [
    ('Decomposition', 'break it into small parts', 7, '#007ea2', 'Q 1, 2, 4, 5, 6, 9, 10'),
    ('Pattern Recognition', 'find what repeats', 1, '#05ccab', 'Q 3'),
    ('Algorithmic Thinking', 'follow steps in order', 1, '#05ccab', 'Q 7'),
    ('Visual Reasoning', 'read what a picture shows', 1, '#05ccab', 'Thinking Spot'),
    ('Logical Diagrams <span style="font-weight:400">(verbal)</span>', 'logic reasoning, not a CT skill', 1, '#cccccc', 'Q 8'),
]
ALSO = ['Analytical Reasoning · Q 1, 2, Spot', 'Changing Order · Q 3', 'Substitution · Q 4', 'Algorithmic Thinking · Q 5, 10',
        'Visual Reasoning · Q 6', 'Decomposition · Q 7', 'Generalisation · Q 8', 'Pattern Recognition · Q 9']

ROUTINE = [('READ', 'What is given? Read the <b>Note</b> too.'),
           ('MARK', 'Underline what is asked. Number the clues.'),
           ('WRITE', 'Write the digits in place-value boxes.'),
           ('CHECK', 'Test every option against every clue.')]
WATCH_SUB = 'The digit rule changes from question to question.'
WATCH = [
    ('Q 1', '<b>CAN</b> be implied: test every option.', 'One example that breaks a claim makes it false.'),
    ('Q 2', '<b>SUFFICIENT</b> means enough to fix one password.', 'A statement you do not need can be left out.'),
    ('Q 4', 'All the digits must be <b>different</b>.', '1 + 1 + 1 + 1 + 6 is not allowed.'),
    ('Q 7', 'A swap may join digits that are <b>not side by side</b>.', 'Swapping the 1st and 5th digits is one swap.'),
    ('Q 10', 'Each digit is used <b>at least once</b>.', '77777 is not allowed: it has no 1 or 5.'),
]
TRYONE = dict(
    q='<b>Use each of the digits 4, 0, 7 and 2 once.</b> What is the smallest 4-digit even number you can make?',
    opts=['a) 2047', 'b) 2074', 'c) 2470', 'd) 2407'],
    hints=[('Echo', 'Say it in your own words: "4 digits, each used once, the <b>smallest</b> number, and it must be <b>even</b>."'),
           ('Vault', 'What do you know? A number cannot start with 0, and an even number ends in 0, 2, 4, 6 or 8.'),
           ('Slicer', 'Fill one place at a time. Pick the smallest digit allowed in the first place, then the smallest for the next place.')],
    turn='Two digits are left. Which order keeps the number even and as small as possible?',
)
BEFORE = 'There is no activity in this chapter. Keep a sheet ready to write numbers in place-value boxes, from ten thousands to ones.'
AHEAD = 'The Thinking Spot is a stacking puzzle: four shapes, four friends and two clues. Keep your starting routine ready!'

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
 dict(n=1, text='Which of the following CAN be implied if the given statement is true?<br>Statement: A 5-digit number is formed using single-digit whole numbers such that the units digit is even and all the remaining digits are odd.',
      opts=['The number definitely lies between 11111 and 99999', 'The number formed CAN be a multiple of 100',
            'The sum of the digits of the largest such number is 44', 'The sum of the digits is NOT divisible by 2'],
      dyna=[('Echo', 'Say the rule in your own words: "the last digit is even, and every other digit is odd." Then read each option as a claim to test.'),
            ('Slicer', 'Test the options one at a time. For each one, try to build a number that follows the rule but breaks the claim. If you can, the claim is false.')],
      turn='Which claim could you not break?'),
 dict(n=2, text='Rohan revealed his 5-digit phone password in a code word to Rajesh where all the digits are NATURAL NUMBERS. Which of the following statements are <u>SUFFICIENT</u> to crack the code?'
      '<br>Statement 1: One of these digits is 1, and 2 appears thrice in the password<br>Statement 2: The first digit is smaller than all other digits and the 2nd digit is smaller than the 3rd'
      '<br>Statement 3: The largest digit in the password is 3 and it appears only once',
      opts=['Statements 1 and 2', 'Statements 2 and 3', 'All the statements are required', 'Cannot be determined even after using all the statements'],
      dyna=[('Starter', 'Begin with Statement 3: the largest digit is 3. So which digits can the password use at all?'),
            ('Slicer', 'Add one statement at a time. After each one, write what you know about every place: 1st, 2nd, 3rd, 4th and 5th. Stop when only one password fits.')],
      turn='Which statements did you actually need?'),
 dict(n=3, text='What will come in place of "?"',
      fig=[('q3_main', 322)], img_opts2=[('q3_a', 102), ('q3_b', 102), ('q3_c', 102), ('q3_d', 102)], opt_h=24,
      dyna=[('Translator', 'Write each row as two lists: the digits of the number, and the digits in the boxes. What do you notice about the order of the digits in the boxes?'),
            ('Roots', 'Ask <b>why</b> some digits sit in black circles. Compare each place in the number with the same place in the boxes.')],
      turn='Use your rule on 82154. Then find the option that matches.'),
 dict(n=4, text='A 5-digit number is formed such that all the digits are different and the sum of all the digits is 10. What is the highest digit this number can have?',
      opts=['3', '4', '5', '6'],
      dyna=[('Starter', 'To make one digit as big as possible, what should the other four digits be: big or small?'),
            ('Vault', 'Remember: all 5 digits are different, and the smallest different digits are 0, 1, 2, 3, and so on.')],
      turn='Add the four smallest different digits. Take that total away from 10.'),
 dict(n=5, text='Using the instructions given below, form two numbers.<br>Instruction 1: Form the largest 5-digit number using the digits in the 5-sided figures, without repeating any digit.'
      '<br>Instruction 2: Form the smallest 3-digit number using the digits in the circles, without repeating any digit.<br>What is the sum of the two numbers formed?',
      fig=[('q5', 107)], opts=['99394', '93394', '98743', '98848'],
      dyna=[('Slicer', 'Split the digits into two lists: the ones in 5-sided figures and the ones in circles. Then do one instruction at a time.'),
            ('Vault', 'Recall: the largest number puts the biggest digits first. The smallest 3-digit number cannot start with 0.')],
      turn='Build both numbers, then add them.'),
 dict(n=6, text='Using the digits at the ends of the vertical lines, form numbers by reading the digits from left to right without rearranging them. Which option represents the greatest even number that can be formed?',
      fig=[('q6_main', 94)], img_opts=[('q6_a', 82), ('q6_b', 82), ('q6_c', 82), ('q6_d', 82)], opt_h=38,
      dyna=[('Starter', 'Begin with the <b>last</b> line. It gives the units digit, and an even number needs an even units digit. Which end must you use there?'),
            ('Slicer', 'Then go line by line from the left. On each line, take the bigger of the two digits.')],
      turn='Write your number. Find the option whose lines show the ends you used.'),
 dict(n=7, text='A string of digits is given below. At MINIMUM, how many pairs of digits (may or may not be adjacent to each other) must be interchanged such that the second largest 5-digit number is formed from left to right?',
      note='A digit can change its position any number of times', fig=[('q7', 156)], opts=['2', '3', '4', '5'],
      dyna=[('Translator', 'First write the target: the largest number from 0, 7, 3, 6 and 5, then the second largest. Write it under 07365, place by place.'),
            ('Slicer', 'Fix one place at a time. When two digits have simply traded places, one swap fixes both. Look out for three digits that go round in a loop.')],
      turn='Count the swaps you needed.'),
 dict(n=8, text='There is a 7-digit number X in which all the digits are different. Using the digits of X, two 5-digit numbers Y and Z are formed, such that no digit is repeated within Y or within Z. What is the MINIMUM number of digits that Y and Z must have in common?',
      opts=['1', '2', '3', '4'],
      dyna=[('Bridge', 'Picture 7 different stickers and two cards with 5 empty slots each. Every slot must get a sticker, and no card may repeat one.'),
            ('Translator', 'Turn it into numbers: Y and Z together have 5 + 5 slots, but X gives only 7 different digits.')],
      turn='How many digits must be used in both numbers?'),
 dict(n=9, text='A 5-digit number has the property that the number formed by its first three digits is the same as the number formed by its last three digits (without changing the order of digits). What is the minimum number of times any digit can appear in this number?',
      opts=['3', '1', '2', '5'],
      dyna=[('Translator', 'Draw five boxes: 1st, 2nd, 3rd, 4th, 5th. The first three boxes must read the same as the last three.'),
            ('Roots', 'Ask why the 3rd box matters: it belongs to both groups. Match place by place: 1st = 3rd, 2nd = 4th, 3rd = 5th.')],
      turn='Write the pattern you get. How few times can a digit appear?'),
 dict(n=10, text='Which digit appears in the tens place of the second largest 5-digit number formed using 1, 5, and 7, where each digit is used at least once?',
      opts=['5', '7', '1', 'Either a or c'],
      dyna=[('Vault', 'Recall how to make the largest number: fill the higher places with the biggest digit, but leave room for one 5 and one 1.'),
            ('Slicer', 'First write the largest such number. Then count down, checking that each number still uses 1, 5 and 7.')],
      turn='Read the tens digit of the second largest number.'),
]
SPOT = dict(
    text="P, Q, R, and S each has a different shape - Circle, Pentagon, Square, and Triangle (not necessarily in the same order). They arranged the shapes as shown below, where the Circle is placed at the bottom-most position."
         "<ul><li>S placed his shape immediately above P's shape</li><li>There are exactly 2 shapes placed above R's shape</li></ul>Which of the following is Q's shape?",
    fig=[('ts_main', 105)], opts=['Circle', 'Square', 'Pentagon', 'Triangle'],
    dyna=[('Translator', 'Turn the picture into a list from top to bottom. Which shape covers all the others? Which one is just under it?'),
          ('Slicer', 'Use one clue at a time. The second clue tells you whose shape has exactly 2 shapes above it. Then try P in each place left and check where S can sit just above.')],
    turn="Fill in all four names. Which shape belongs to Q?")

MULT = ('      9 b c\n      3 5 d\n    ───────\n    3 a 4 b\n  4 a 3 5\n2 9 6 1\n───────────\n3 4 a 3 9 b')
SUPP = [
 dict(n=1, qid='110275', text='Which one of the alternatives is different from the rest?', opts=['2437', '2419', '5407', '1459'], hint=['Translator', 'Roots']),
 dict(n=2, qid='107693', text='Choose the number which is different from the others in the group.', opts=['751', '734', '981', '853', '532'], hint=['Roots', 'Slicer']),
 dict(n=3, qid='110268', text='Which one of the alternatives is different from the rest?', opts=['7654', '4567', '9876', '4321'], hint=['Roots', 'Echo']),
 dict(n=4, qid='107732', text='Choose the one which does not belong to the group.', opts=['147 : 741', '253 : 352', '518 : 816', '303 : 303', '419 : 914'], hint=['Roots', 'Slicer']),
 dict(n=5, qid='110000', text='If the following numbers are written in ascending order, what will be the middle digit of the middle term?<br>745, 657, 825, 475, 692, 612, 735',
      opts=['2', '9', '4', '7'], hint=['Slicer', 'Vault']),
 dict(n=6, qid='109985', text='Answer the question based on the following number series.<br><span class="mono" style="font-weight:400">7 3 2 9 5 7 4 1 3 6 4 9 5 4 6 5 2 7 2 4 1 6 7 2 1 3</span>'
      '<br>How many odd digits in the series are preceded and followed by an even digit?', opts=['4', '2', '5', '3'], hint=['Echo', 'Slicer']),
 dict(n=7, qid='107484', text='Find out the wrong term.<br>1236, 2346, 3456, 4566, 5686', opts=['1236', '3456', '4566', '5686'], hint=['Roots', 'Slicer']),
 dict(n=8, qid='108455', text='Find the digits that the letters stand for in the multiplication given below. What does b stand for?',
      pre=MULT, opts=['6', '7', '8', '9'], hint=['Starter', 'Translator']),
 dict(n=9, qid='107880', text='In a row of boys, Deepak is seventh from the left and Madhu is twelfth from the right. If they interchange their positions, Deepak becomes twenty-second from the left. How many boys are there in the row?',
      opts=['19', '31', '33', 'Cannot be determined', 'None of these'], hint=['Translator', 'Bridge']),
 dict(n=10, qid='108874', text='Five friends A, B, C, D and E are sitting on a bench.<br>(i) A is sitting next to B. (ii) C is sitting next to D. (iii) D is not sitting with E. (iv) E is on the left end of the bench.'
      '<br>(v) C is in the second position from the right. (vi) A is on the right side of B and to the right side of E. (vii) A and C are sitting together.<br>Who is sitting at the centre?',
      opts=['A', 'B', 'C', 'D'], hint=['Starter', 'Slicer']),
]

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1, 2], True), ('questions', [3, 4], False, 'space'), ('questions', [5, 6], False, 'space'),
    ('questions', [7, 8, 9]), ('questions', [10, 'spot'], False, 'spaceqr'),
    ('supp', [1, 2, 3, 4, 5], True), ('supp', [6, 7, 8], False, 'space'), ('supp', [9, 10], False, 'howdid+space'),
]
