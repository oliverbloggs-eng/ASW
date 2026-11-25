import re,asyncio,sys
exec(open('/home/claude/hero/shot.py').read().split('async def main')[0])
from playwright.async_api import async_playwright
import re as _re
_L=['Dispute Resolution','Commercial and Corporate','Public Procurement and Tax','Property &amp; Real Estate','Private Client','Employment and Pensions']
_src=open('/home/claude/hero/project/Areas.dc.html',encoding='utf-8').read()
_src=_re.sub(r'<sc-for list="\{\{pills\}\}".*?</sc-for>',''.join('<li><a class="ab-pill%s" href="#x">%s</a></li>'%(' on' if i==1 else '',l) for i,l in enumerate(_L)),_src,flags=_re.S)
open('/tmp/Areas_t.dc.html','w',encoding='utf-8').write(_src)
_h=prep('/tmp/Areas_t.dc.html')
open('/home/claude/hero/t_Areas.html','w').write(_h)
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for w in (1440,768,390):
            pg=await b.new_page(viewport={'width':w,'height':900}); await pg.goto('file:///home/claude/hero/t_Areas.html'); await pg.add_style_tag(content='.rv{animation:none !important}'); await pg.wait_for_timeout(900)
            r=await pg.evaluate('''()=>{const q=s=>{const e=document.querySelector(s);if(!e)return null;const b=e.getBoundingClientRect();return [Math.round(b.top+scrollY),Math.round(b.bottom+scrollY)]};return {hero:q('.pg-hero'),bar:q('.ab-bar'),a1:q('#dispute'),a6:q('#employment'),cl:q('.cl'),who:q('.wh-grid'),pl:q('.pl-list'),fs:q('.fs'),tm:q('.tm-grid'),ap:q('.ap-list'),vs:q('.vs'),ft:q('.ft'),H:document.documentElement.scrollHeight,sw:document.documentElement.scrollWidth}}''')
            print(w,r)
            await pg.screenshot(path=f'/home/claude/hero/r_{w}.png',full_page=True)
        await b.close()
asyncio.run(m())
