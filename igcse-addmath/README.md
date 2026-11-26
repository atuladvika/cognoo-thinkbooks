# Cognoo ThinkBook Guide: Cambridge IGCSE & O Level Additional Mathematics (source)

Build: `python3 build_chapter.py chapters/ch1_ex1.py chapters/ch1_ex2.py chapters/ch1_ex3.py chapters/ch1_ex4.py` then `python3 make.py <output.pdf>`
and `python3 _class/check_flow.py` (every page must show `over: 0`).

## Structure: one unit per exercise
A JEE chapter has several exercises (1.1, 1.2, ...). Each exercise is its own unit, in coursebook order:
1. Exercise opener, 2 facing pages (even + odd): what you need to know, STCA concepts, Dyna skills per question,
   starting routine, Watch out!, a warm-up with hints, and the exercise's own lecture QR (Atul Sir, one lecture per exercise).
2. Exercise questions: every coursebook question in order, each with two Dyna skills and YOUR TURN.
   Questions with many parts (e.g. 1.2 Q2 a–f) are split into blocks of three parts.
3. 10 supplementary questions from the i2K / Dynamind question bank, printed exactly as in the bank with their Q-IDs.
4. A Notes page only when needed so the next exercise's opener starts on an even (left-hand) page.

One content file per exercise: `chapters/ch<chapter>_ex<n>.py`. Pages are numbered continuously by `build_chapter.py`.
Answers are kept in each file's docstring and never printed.

`_class/measure.py` prints the height of every question block, to plan which questions go on which page.

## Page plan
Pages 1-2 cover and copyright (card); 3-5 contents for all 16 chapters (from `_class/coursebook_toc.py`; page numbers appear only for built exercises); 6-7 The Thinking Coach; 8-11 Thinking Skills; chapters from page 12 (exercise openers always on even pages).

## Front and end matter
After building the chapters, build pages 1-9 and the end pages from the Class 5 book:
`python3 _class/adapt_front.py ../class5 <last chapter page>` (e.g. 49). It adds a Notes page only when the inner page
count needs one, then the inside back cover and the back cover. Re-run it whenever chapters or exercises are added,
so the contents page and the end-page numbers stay right.

Full rebuild:
```
python3 build_chapter.py chapters/ch1_ex1.py chapters/ch1_ex2.py chapters/ch1_ex3.py chapters/ch1_ex4.py
python3 _class/adapt_front.py ../class5 49
python3 make.py ../print/<name>.pdf
```
