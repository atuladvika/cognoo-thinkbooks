"""Report chapter pages whose content overflows the page (run after make.py has written book.html)."""
import asyncio, os
from playwright.async_api import async_playwright
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome' if os.path.exists('/usr/bin/google-chrome') else None)
        pg = await b.new_page(); await pg.goto('file://' + here + '/book.html'); await pg.evaluate('document.fonts.ready')
        r = await pg.evaluate('''() => [...document.querySelectorAll('section.page')].map((s,i)=>{
            const f=s.querySelector('.flow'); if(!f) return null;
            const kids=[...f.children]; const last=kids[kids.length-1];
            const sp=f.querySelector('.space');
            return {page:i+1, over: f.scrollHeight - f.clientHeight, free: f.getBoundingClientRect().bottom - last.getBoundingClientRect().bottom,
                    space: sp? sp.getBoundingClientRect().height*0.75 : null};
        }).filter(Boolean)''')
        for x in r: print(x)
        await b.close()
asyncio.run(main())
