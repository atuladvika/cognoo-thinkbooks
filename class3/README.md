# Class 3 CT ThinkBook, Chapter 1: source of record (v7)

Build:  `pip install playwright pymupdf` (and a Chromium/Chrome), then
        `python3 make.py ../Class3_CT_ThinkBook_Ch1_v7.pdf`

What is here
- `pages/p01.svg … p22.svg`: one SVG per page (real Poppins text, vector art).
  Card stock: p01 front cover, p02 inside front (copyright), p21 inside back cover, p22 back cover. Paper: p03–p20 (inner pages, kept even; p20 is a Notes page that makes 18).
- `overlays/pNN.html`: HTML layers printed on top of page NN (redrawn arrows/ticks on pages 13, 15, 16, 17; inside back cover content on page 21; back-cover QR section on page 22). Change text here, not in the PDF.
- `assets/`: images used by the pages, including the QR Manager codes `CGN0000xx.png` (Deep Navy).
- `fonts/`: Poppins (Regular, Medium, Bold, Italic, Bold Italic) and DejaVu Sans Mono, loaded by `book.css`.
- `book.css`: page size (A4 + 9 pt bleed), fonts, brand colours.
- `make.py`: assembles `book.html` and prints the PDF with Chromium, trimmed to 613.276 × 859.89 pt.
- `QR_Code_Map_Class3.csv`: which QR Manager code goes where.
- `_migration/`: the one-time scripts that converted v6 PDF to this source (24 Nov 2026). Not needed for builds.

Changes from v6
- All QR codes replaced by Cognoo QR Manager codes (CGN000002, 008–017).
- Discover page (Student Tour, Mentor Guide) removed.
- Four cover pages on card: front, inside front, inside back, back. Chapter content stays on the paper pages 3–20; a Notes page keeps the inner page count even.
- Old back cover split: inside back = A Common Thinking Language, Dyna Thinking Coach (NEP/NCF-SE), as two Pale Mint cards (no notes lines); back = Learning to Think Starts Early, What This ThinkBook Develops, Scan to Get Started (explainer CGN000016 + Dyna CGN000002).
- Fallback-font arrows and ticks on pages 13, 15, 16, 17 redrawn as SVG (Poppins and DejaVu Sans Mono only).
