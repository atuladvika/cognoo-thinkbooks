"""One-time: build blank inner-page frames (running header + footer, no page number) from an approved book PDF.
Usage: python3 _class/make_frames.py <approved.pdf> <even page no> <odd page no>"""
import sys, os, re, base64, hashlib
import pymupdf as fitz
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(HERE)
src = fitz.open(sys.argv[1]); ev, od = int(sys.argv[2]), int(sys.argv[3])
out = fitz.open()
for pno in (ev, od):
    out.insert_pdf(src, from_page=pno - 1, to_page=pno - 1)
for p in out:
    nums = [fitz.Rect(s['bbox']) for b in p.get_text('dict')['blocks'] for l in b.get('lines', []) for s in l['spans']
            if s['bbox'][1] > 800 and s['text'].strip().isdigit()]
    p.add_redact_annot(fitz.Rect(-5, 71.5, 620, 801))            # content area: text, images and drawings
    p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_REMOVE, graphics=fitz.PDF_REDACT_LINE_ART_REMOVE_IF_TOUCHED, text=fitz.PDF_REDACT_TEXT_REMOVE)
    for r in nums:                                                 # page number only (keep the pill)
        p.add_redact_annot(r)
    p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE, graphics=fitz.PDF_REDACT_LINE_ART_NONE, text=fitz.PDF_REDACT_TEXT_REMOVE)
seen = {}
def ext(m):
    kind, data = m.group(2), m.group(3)
    raw = base64.b64decode(data); h = hashlib.md5(raw).hexdigest()[:12]
    fn = f'assets/img_{h}.{"jpg" if kind == "jpeg" else kind}'
    if not os.path.exists(fn): open(fn, 'wb').write(raw)
    return f'{m.group(1)}="{fn}"'
for name, p in zip(('even', 'odd'), out):
    s = p.get_svg_image(text_as_path=False)
    s = re.sub(r'(xlink:href|href)="data:image/(png|jpeg|jpg);base64,([^"]+)"', ext, s)
    s = re.sub(r'^<\?xml[^>]*>\s*', '', s)
    s = re.sub(r'id="([^"]+)"', lambda m: f'id="PFX_{m.group(1)}"', s)
    s = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#PFX_{m.group(1)})', s)
    s = re.sub(r'(xlink:href|href)="#([^"]+)"', lambda m: f'{m.group(1)}="#PFX_{m.group(2)}"', s)
    s = s.replace('<svg ', '<svg class="pg" ', 1)
    open(f'_class/frame_{name}.svg', 'w').write(s)
print('frames written')
