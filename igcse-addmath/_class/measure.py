"""Print the height (pt) of every question block on every page of book.html, to plan page breaks."""
import asyncio, os
from playwright.async_api import async_playwright
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome' if os.path.exists('/usr/bin/google-chrome') else None)
        pg = await b.new_page(); await pg.goto('file://' + here + '/book.html'); await pg.evaluate('document.fonts.ready')
        r = await pg.evaluate('''() => [...document.querySelectorAll('section.page')].map((s,i)=>{
            const f=s.querySelector('.flow'); if(!f) return null;
            return {page:i+1, top: f.getBoundingClientRect().top*0.75, h: f.clientHeight*0.75,
              blocks:[...f.children].filter(c=>!c.classList.contains('space')).map(c=>{const st=getComputedStyle(c);return Math.round((c.getBoundingClientRect().height+parseFloat(st.marginBottom)+parseFloat(st.marginTop))*0.75)})};
        }).filter(Boolean)''')
        for x in r: print(x)
        await b.close()
asyncio.run(main())
