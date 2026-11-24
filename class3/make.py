"""Build the ThinkBook from source: pages/*.svg + overlays/*.html -> build/book.html -> out PDF.
Usage: python3 make.py <output.pdf>"""
import os, sys, glob, asyncio
from playwright.async_api import async_playwright
here=os.path.dirname(os.path.abspath(__file__)); os.chdir(here)
pages=sorted(glob.glob('pages/p*.svg'))
html=['<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="book.css"></head><body>']
for f in pages:
    n=os.path.basename(f)[1:3]
    ov=f'overlays/p{n}.html'
    html.append(f'<section class="page" id="page{int(n)}">'+open(f).read()+(open(ov).read() if os.path.exists(ov) else '')+'</section>')
html.append('</body></html>')
open('book.html','w').write('\n'.join(html))
out=os.path.abspath(sys.argv[1] if len(sys.argv)>1 else 'book.pdf')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome' if os.path.exists('/usr/bin/google-chrome') else None)
        pg=await b.new_page(); await pg.goto('file://'+here+'/book.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(500)
        await pg.pdf(path=out,prefer_css_page_size=True,print_background=True,width='216.6mm',height='303.6mm',margin={'top':'0','bottom':'0','left':'0','right':'0'})
        await b.close()
asyncio.run(main())
# Chrome rounds the page size; trim every page to the exact A4 + 9 pt bleed box (613.276 x 859.89 pt), anchored top-left
import pymupdf as fitz
d=fitz.open(out); tmp=out+'.tmp'
for pg in d:
    H=pg.mediabox.height
    pg.set_mediabox(fitz.Rect(0,H-859.89,613.276,H))
d.save(tmp,garbage=3,deflate=True); d.close(); os.replace(tmp,out); print('wrote',out)
