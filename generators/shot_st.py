import re,asyncio,sys
exec(open('/home/claude/hero/shot.py').read().split('async def main')[0])
from playwright.async_api import async_playwright
open('/home/claude/hero/t_St.html','w').write(prep('/home/claude/hero/project/ContactFormStates.dc.html'))
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for w in (1080,):
            pg=await b.new_page(viewport={'width':w,'height':900}); await pg.goto('file:///home/claude/hero/t_St.html'); await pg.add_style_tag(content='.rv{animation:none !important}'); await pg.wait_for_timeout(900)
            r=await pg.evaluate('''()=>{const q=s=>{const e=document.querySelector(s);if(!e)return null;const b=e.getBoundingClientRect();return [Math.round(b.top+scrollY),Math.round(b.bottom+scrollY)]};return {hero:q('.st-root'),who:q('.wh-grid'),pl:q('.pl-list'),fs:q('.fs'),tm:q('.tm-grid'),ap:q('.ap-list'),vs:q('.vs'),ft:q('.ft'),H:document.documentElement.scrollHeight,sw:document.documentElement.scrollWidth}}''')
            print(w,r)
            await pg.screenshot(path=f'/home/claude/hero/s_{w}.png',full_page=True)
        await b.close()
asyncio.run(m())
