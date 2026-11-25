# Class 6 CT ThinkBook, Chapter 1: source of record (v1)

Build (from this folder): `python3 make.py <absolute path of the output PDF>`
Needs Python 3 with `playwright`, `pymupdf`, `fonttools`, `pillow`, and Chromium/Chrome.

## What is here
- `pages/pNN.svg`: one SVG per page. Pages 1–9, 20 (Notes) and 21–22 come from the Class 3 book with the class-specific text taken out; pages 10–19 are blank page frames (running header and footer).
- `overlays/pNN.html` and `overlays/pNN_front.html`: the HTML printed on top of each page. Chapter pages 10–19 are generated; do not edit them by hand.
- `chapters/ch1.py`: **all Chapter 1 content** (opener, every handbook question with its two Dyna skills and YOUR TURN, the Thinking Spot, the 10 supplementary questions with Q-IDs and hints, and which questions go on which page). Edit here, then regenerate.
- `chapter.css`: styles of the chapter pages (sizes measured from the Class 3 book).
- `_class/config.json`: Class 6 text for pages 1–9 and the back cover (chapter list, first and last chapter, page 5 mock question and concept, the seven Try it examples, back-cover intro).
- `_class/chapter_gen.py`: writes pages 10–19 from `chapters/ch1.py`. `_class/check_flow.py` reports any page that overflows.
- `_class/adapt_front.py`, `_class/make_frames.py`, `_class/svgtext.py`: one-time scripts used to make this class folder from `class3/` (keep them for Classes 5–8).
- `assets/`: images. `assets/ch1/` holds the Chapter 1 figures (from the Student Handbook and the supplementary scan); `assets/icons/` the 7 skill icons; `CGN0000xx.png` the QR Manager codes (Deep Navy).
- `QR_Code_Map_Class6.csv`: which QR Manager code goes where.

## Page structure (22 pages)
- Card: p1 front cover, p2 copyright page, p21 inside back cover, p22 back cover.
- Paper: p3–p20 (18 pages). Chapter 1: opener p10–11, questions p12–16, Thinking Spot p17, supplementary p18–19, Notes p20.
- Contents (p3) lists the 10 CT chapters only (Part 2 of the handbook, Artificial Intelligence, is not covered).
- End matter templates: `pages/end_notes.svg`, `end_ibc.svg`, `end_back.svg` (+ `overlays/end_*.html`). After regenerating chapters run `python3 _class/place_end.py <last chapter page>`: it adds a Notes page if needed and places the two back covers.

## To change Chapter 1 or add Chapter 2
1. Edit `chapters/ch1.py` (or create `chapters/ch2.py` with the same structure and the next free page as `first_page`).
2. `python3 _class/chapter_gen.py chapters/ch1.py` (and each other chapter file).
3. `python3 make.py <output.pdf>` then `python3 _class/check_flow.py` (every page must show `over: 0`).
4. Move the inside back cover and back cover to the last two page numbers and add a Notes page if the paper page count is odd.
