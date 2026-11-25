import re,asyncio,sys
exec(open('/home/claude/hero/shot.py').read().split('async def main')[0])
from playwright.async_api import async_playwright
open('/home/claude/hero/t_Ct.html','w').write(prep('/home/claude/hero/project/Contact.dc.html'))
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for w in (1440,768,390):
            pg=await b.new_page(viewport={'width':w,'height':900}); await pg.goto('file:///home/claude/hero/t_Ct.html'); await pg.add_style_tag(content='.rv{animation:none !important}'); await pg.wait_for_timeout(900)
            r=await pg.evaluate('''()=>{const q=s=>{const e=document.querySelector(s);if(!e)return null;const b=e.getBoundingClientRect();return [Math.round(b.top+scrollY),Math.round(b.bottom+scrollY)]};return {hero:q('.pg-hero'),cards:q('.ct-cl'),fm:q('.ct-grid'),mp:q('.mp-frame'),ft:q('.ft'),who:q('.wh-grid'),pl:q('.pl-list'),fs:q('.fs'),tm:q('.tm-grid'),ap:q('.ap-list'),vs:q('.vs'),ft:q('.ft'),H:document.documentElement.scrollHeight,sw:document.documentElement.scrollWidth}}''')
            print(w,r)
            await pg.screenshot(path=f'/home/claude/hero/k_{w}.png',full_page=True)
        await b.close()
asyncio.run(m())
