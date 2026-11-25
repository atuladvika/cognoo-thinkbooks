"""Class 7, Chapter 1: Large Numbers Around Us. Content for the chapter pages.
Answers (TH = TB): Q1 c, Q2 d, Q3 a, Q4 c, Q5 c, Q6 b, Q7 b, Q8 c, Q9 c, Q10 d, Thinking Spot d. Never printed.
Supplementary: the 10 questions and Q-IDs of the Dynamind Chapter 1 assessment (A00011403), in its order.
One of them (105203) differs from the TB list (which had 108456). Answers: 1 a, 2 d, 3 b, 4 b, 5 a, 6 c, 7 e, 8 c, 9 b, 10 b.
Supp. Q5: the scan's comparison symbols are garbled; they are typeset here with five distinct symbols
(U = V, V < N, R <= U as in the TB), so the answer (only I) is unchanged."""

CH = dict(
    num=1, title='Large Numbers Around Us', first_page=10,
    lecture_qr='CGN000021', dyna_qr='CGN000006',
    count_line='10 questions + 1 Thinking Spot · Goes with Chapter 1 of your CBSE Computational Thinking Student Handbook',
)

KNOW = [
    '<b>Indian names:</b> 1,00,000 is one lakh, 10,00,000 is ten lakh and 1,00,00,000 is one crore.',
    '<b>International names:</b> 1,000,000 is one million and 1,000,000,000 is one billion.',
    '<b>Place value:</b> 423 hundreds means 423 × 100 = 42,300.',
    '<b>Comparing:</b> read two numbers from the left. The first place where they differ decides which is bigger.',
]

BARS = [
    ('Decomposition', 'break it into small parts', 3, '#007ea2', 'Q 1, 7, 10'),
    ('Pattern Recognition', 'find what repeats', 2, '#05ccab', 'Q 4, 5'),
    ('Algorithmic Thinking', 'follow steps in order', 2, '#05ccab', 'Q 3, 6'),
    ('Abstract Thinking', 'keep only what matters', 1, '#05ccab', 'Q 2'),
    ('Analytical Reasoning <span style="font-weight:400">(verbal)</span>', 'clue puzzles, not a CT skill', 3, '#cccccc', 'Q 8, 9, Spot'),
]
ALSO = ['Analytical Reasoning · Q 1, 3, 7', 'Trouble Shooting · Q 2', 'Generalisation · Q 4', 'Letter-Number Coding · Q 5',
        'Sitting Arrangement · Q 6', 'Abstract Thinking · Q 8', 'Data Analysis · Q 9', 'Substitution · Q 10', 'Magic Squares · Spot']

ROUTINE = [('READ', 'What is given? Read every clue.'),
           ('MARK', 'Underline what is asked. Number the clues.'),
           ('WRITE', 'Write the digits in a place-value chart.'),
           ('CHECK', 'Test every option against all the clues.')]
WATCH_SUB = 'One small word changes the whole answer.'
WATCH = [
    ('Q 1', 'Y must still be a <b>6-digit</b> number.', 'So X + 2,00,000 cannot reach 10 lakh.'),
    ('Q 2', '<b>All</b> the numbers on the dial-pad.', 'Do not forget the 0.'),
    ('Q 3', '<b>Exactly two</b> digits are common.', 'Y has only <b>one</b> even digit.'),
    ('Q 6', 'Only numbers <b>between 2 lakhs and 8 lakhs</b>.', 'Count the others out.'),
    ('Q 9', 'The question asks about <b>Calvin</b>.', 'Find both his job and his salary.'),
]
TRYONE = dict(
    q='<b>How many zeros</b> are there in ten crore?',
    opts=['a) 7', 'b) 8', 'c) 9', 'd) 10'],
    hints=[('Vault', 'What do I already know? One crore is 1,00,00,000.'),
           ('Echo', 'Say it in your own words: "Ten crore is <b>ten times</b> one crore."'),
           ('Translator', 'Write one crore in digits, then write ten times that number.')],
    turn='Count the zeros in the number you wrote.',
)
BEFORE = 'There is no activity in this chapter. Keep a pencil ready to write numbers in a place-value chart.'
AHEAD = 'The Thinking Spot is a column puzzle: each number appears as many times as its value.'

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
 dict(n=1, text='‘X’ is a 6-digit number formed using exactly three different digits. One of the digits appears once, another appears twice, and the third appears three times. When 2 lakhs are added to ‘X’, the resulting number ‘Y’ is still a 6-digit number. What is the highest possible value of ‘Y’?',
      opts=['977889', '999999', '999988', '999887'],
      dyna=[('Starter', 'Begin with the first digit of X. If X starts with 8 or 9, what happens when you add 2,00,000?'),
            ('Slicer', 'Then fill the other five places: which digit should appear three times, and which twice, to make X as big as possible?')],
      turn='Write the biggest X, then add 2,00,000.'),
 dict(n=2, text='What is the product of all the numbers on a telephone dial-pad?',
      opts=['12345', '32451', '362880', 'None of these'],
      dyna=[('Bridge', 'Picture a real phone keypad. Which numbers are on it? Is there one at the bottom?'),
            ('Vault', 'Remember what happens when you multiply any number by 0.')],
      turn='Check the tempting option c: which number did it leave out?'),
 dict(n=3, text='Sam forms two different 6-digit numbers, X and Y, using digits from 0 to 9 (without repetition within a number). Exactly two digits are common between X and Y.<br>• The digit 9 appears in the same position in both numbers<br>• Y ends with 0, has only one even digit, and its digits are arranged in descending order<br>• 6 is present in X, and the number of even digits on its left is equal to the number of even digits on its right<br>If X is the largest possible number, what is the difference between X and Y?',
      opts=['9310', '9210', '8420', '8310'],
      dyna=[('Starter', 'Begin with Y: it has five odd digits and a 0 at the end, in descending order. Write it down.'),
            ('Slicer', 'Now build X one clue at a time: where is the 9, which digits can it share with Y, and where must the 6 go?')],
      turn='Write the largest X, then subtract Y.'),
 dict(n=4, text='If each of the rows follows the same theme, what will come in place of “?”',
      fig=[('q4_main', 330)], img_opts=[('q4_a', 64), ('q4_b', 64), ('q4_c', 64), ('q4_d', 64)], opt_h=26,
      dyna=[('Translator', 'Put a digit in every grey circle of Row 1. Try 7, then 8. When does the comparison stop being true?'),
            ('Roots', 'Ask what the box on the right means: the <b>largest</b> digit that keeps the comparison true.')],
      turn='Try 5 and 6 in the grey circles of the last row.'),
 dict(n=5, text='What will come in place of “?”',
      fig=[('q5', 180)], opts=['0', '00', '000', '0000'],
      dyna=[('Vault', 'Remember how many zeros each number has: crore 7, million 6, thousand 3, billion 9, lakh 5.'),
            ('Slicer', 'Take one row at a time. Count the letters after the dash. Take that many zeros away.')],
      turn='Do the same for Lakh − kh.'),
 dict(n=6, text='Six number tokens are given. Rearrange them to form a 6-digit number such that:<br>• The difference between the first and last digits is as small as possible<br>• The hundreds digit is double the thousands digit<br>• No consecutive digits appear next to each other<br>• All given tokens must be used exactly once<br>How many different 6-digit numbers between 2 lakhs and 8 lakhs can be formed under these conditions?',
      fig=[('q6', 210)], opts=['1', '2', '3', 'More than 3'],
      dyna=[('Starter', 'Begin with the hundreds and thousands places. Which pairs of tokens have one digit double the other?'),
            ('Slicer', 'For each pair, choose the first and last digits, then fill the rest. Cross out any number with neighbours like 4 and 5.')],
      turn='Keep only the numbers between 2,00,000 and 8,00,000.'),
 dict(n=7, text='Two five-digit numbers are formed using different digits from 0 to 9. Both numbers have some digits missing, as shown below:<br>Number 1: _ 1 _ 9 _<br>Number 2: _ 4 _ 6 _<br>No two consecutive digits of the number series are present in the same number. What is the maximum possible difference of the numbers formed?',
      opts=['47525', '52663', '52429', '46733'],
      dyna=[('Slicer', 'List the six digits not used yet. Which of them can go in Number 1 without sitting next to 1 or 9 in counting order?'),
            ('Roots', 'Ask why the order matters: to get the biggest difference, which number should be as large as possible?')],
      turn='Make one number as big as you can and the other as small. Subtract.'),
 dict(n=8, text='A, B, C, D, and E each have a different number card among one hundred, one thousand, ten thousand, one lakh, and ten lakhs.<br>• C has an even number of zeros in his number<br>• A’s number has 2 zeros less than C’s number<br>• D’s number has 4 zeros more than A’s number<br>• The number of zeros in B is more than that of A but less than C<br>Which number card does E have?',
      opts=['One thousand', 'Ten thousand', 'One lakh', 'Ten lakh'],
      dyna=[('Translator', 'Turn each card into a count of zeros: hundred 2, thousand 3, ten thousand 4, lakh 5, ten lakh 6.'),
            ('Echo', 'Say it in your own words: "A and D are 4 zeros apart, and C sits 2 zeros above A." Which cards fit?')],
      turn='Place C and B, then find the card that is left.'),
 dict(n=9, text='4 friends, Alex, Bob, Calvin and David have a different profession – Doctor, Lawyer, Cricketer, and Engineer and earn a different salary – ₹40,000, ₹50,000, ₹60,000 and ₹70,000 per year (not necessarily in the same order).<br>• The cricketer earns the highest<br>• Alex earns more than Bob, while the doctor earns more than David, who is the engineer<br>• Bob is the lawyer, and neither Bob nor David has an exact salary of ₹50,000<br>Which of these options shows the correct profession and salary of Calvin?',
      opts=['Cricketer - ₹70,000', 'Doctor - ₹60,000', 'Doctor - ₹50,000', 'Doctor - ₹40,000'],
      dyna=[('Translator', 'Draw a table: the four friends down the side, profession and salary across the top. Fill in what is certain.'),
            ('Starter', 'Begin with the fixed clues: Bob is the lawyer and David is the engineer. Who earns ₹50,000, then?')],
      turn='Fill in the last two rows of your table.'),
 dict(n=10, text='The following are the clues to the 6-digit password of Nisha’s laptop:<br>35 tens · 31 thousands · 25 ones · 423 hundreds · 14 ten thousands<br>What is Nisha’s password?',
      opts=['213625', '203675', '212375', '213675'],
      dyna=[('Slicer', 'Work out each clue on its own: 35 tens = 350, 31 thousands = 31,000, and so on.'),
            ('Translator', 'Write the five values one under another, lining up the places, and add them.')],
      turn='Match your total with the options.'),
]
SPOT = dict(
    text='Columns A, B, and C contain 3 numbers each, such that:<br>• The number of times each number appears in all 3 columns combined is equal to its value (e.g., 2 appears twice, 3 appears thrice, etc.)<br>• Each column contains AT LEAST TWO different numbers<br>If column A is the only column with THREE different numbers, then which column has the highest sum?',
    fig=[('ts_main', 90)], opts=['Column A', 'Column B', 'Column C', 'Both columns B and C'],
    dyna=[('Vault', 'Count the circles: there are 9. A 4 is shown, so 4 must appear four times. What about 2 and 3?'),
          ('Slicer', 'Fill column A first: it must have three different numbers. Then share the numbers left between B and C.')],
    turn='Add up each column.')

SUPP = [
 dict(n=1, qid='108364', text='Suppose in view of a number system, a symbol system was substituted, which had digits □, ∧, Z, ∑, ★, S, a, &lt;, X and Θ corresponding to the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 respectively. The digit □ is used in the same fashion as the digit 0 in the decimal system. Which is equal to 10²?',
      img_opts=[('s1_a', 40), ('s1_b', 26), ('s1_c', 42), ('s1_d', 37)], opt_h=17, hint=['Translator', 'Vault']),
 dict(n=2, qid='105203', text='If in a certain language, 943 is coded as BED and 12448 is coded as SWEET, how is 492311 coded in that language?',
      opts=['EDSWBS', 'TSWBDD', 'DSWTEE', 'EBWDSS'], hint=['Translator', 'Slicer']),
 dict(n=3, qid='105207', text='In a certain code, a number 13479 is written as AQFJL and 5268 is written as DMPN. How is 396824 written in that code?',
      opts=['QLPNKJ', 'QLPNMF', 'QLPMNF', 'QLPNDF'], hint=['Translator', 'Slicer']),
 dict(n=4, qid='105222', text='If ROSE is coded as 6821, CHAIR is coded as 73456 and PREACH is coded as 961473, what will be the code for SEARCH?',
      opts=['246173', '214673', '214763', '216473'], hint=['Slicer', 'Vault']),
 dict(n=5, qid='108381', text='The symbols ©, ®, =, * and $ mean: ‘A © B’ A is greater than B; ‘A ® B’ A is greater than or equal to B; ‘A = B’ A is equal to B; ‘A * B’ A is smaller than B; ‘A $ B’ A is smaller than or equal to B. If the statements are true, which conclusion is definitely true?<br>Statements: U = V, V * N, R $ U<br>Conclusions: I. R * N &nbsp; II. U © N',
      opts=['Only I is true', 'Only II is true', 'Either I or II is true', 'Neither I nor II is true'], hint=['Translator', 'Roots']),
 dict(n=6, qid='108355', text='(i) In a class of boys and girls, Amar’s rank is 12th and Meeta’s rank is 8th. (ii) Amar’s rank among the boys is 6th and Meeta’s rank among the girls is 3rd. (iii) In the class, Meeta’s rank is 52nd from the other end. (iv) From the other end, Amar’s rank among the boys is 26th. Which of the following is Meeta’s rank among the girls from the other end?',
      opts=['23rd', '28th', '26th', 'Can’t be determined'], hint=['Slicer', 'Translator']),
 dict(n=7, qid='107879', text='In a row of 21 girls, when Monika was shifted by four places towards the right, she became 12th from the left end. What was her earlier position from the right end of the row?',
      opts=['9th', '10th', '11th', '12th', '14th'], hint=['Bridge', 'Translator']),
 dict(n=8, qid='108882', text='Ten students A, B, C, D, E, F, G, H, I and J are sitting in a row facing West. (i) B and F are not sitting on either of the edges. (ii) G is sitting to the left of D and H is sitting to the right of J. (iii) There are four persons between E and A. (iv) I is to the North of B and F is to the South of D. (v) J is in between A and D and G is in between E and F. (vi) There are two persons between H and C. Who among the following is definitely sitting at one of the ends?',
      opts=['C', 'H', 'E', 'Cannot be determined'], hint=['Translator', 'Starter']),
 dict(n=9, qid='105120', text='Five friends A, B, C, D and E wore shirts of green, yellow, pink, red and blue colours and shorts of black, white, grey, blue and green colours. Nobody wore a shirt and shorts of the same colour. D wore a blue shirt and C wore green shorts. The one who wore a green shirt wore black shorts, and the one who wore blue shorts wore a red shirt. A wore white shorts and a pink shirt. E did not wear a red shirt. Which colour shorts did B wear?',
      opts=['Grey', 'Blue', 'White', 'Black'], hint=['Translator', 'Starter']),
 dict(n=10, qid='105096', text='There are five persons P, Q, R, S and T. One is a football player, one is a chess player and one is a hockey player. P and S are unmarried ladies and do not play any game. None of the ladies plays chess or football. There is a married couple in which T is the husband. Q is the brother of R and is neither a chess player nor a hockey player. Who is the football player?',
      opts=['P', 'Q', 'R', 'S'], hint=['Starter', 'Roots']),
]

PAGES = [
    ('opener1',), ('opener2',),
    ('questions', [1, 2], True, 'space'), ('questions', [3, 4], False, 'space'), ('questions', [5, 6], False, 'space'),
    ('questions', [7, 8], False, 'space'), ('questions', [9, 10], False, 'space'), ('questions', ['spot'], False, 'spaceqr'),
    ('supp', [1, 2, 3, 4], True), ('supp', [5, 6, 7], False, 'space'), ('supp', [8, 9, 10], False, 'howdid'),
]
