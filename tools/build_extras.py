#!/usr/bin/env python3
"""Generate 404.html, privacy.html, terms.html, favicons, robots.txt, vercel.json. Run after build_static.py."""
import re,os,json
from PIL import Image
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));os.chdir(ROOT)
# favicons from logo
lg=Image.open('assets/logo.png').convert('RGBA')
bb=lg.getbbox(); lg=lg.crop(bb)
def sq(n):
    c=Image.new('RGBA',(n,n),(255,255,255,0)); r=min(n*.86/lg.width,n*.86/lg.height)
    t=lg.resize((max(1,int(lg.width*r)),max(1,int(lg.height*r))),Image.LANCZOS); c.paste(t,((n-t.width)//2,(n-t.height)//2),t); return c
sq(64).save('assets/favicon.png',optimize=True)
bg=Image.new('RGBA',(180,180),(255,255,255,255)); bg.alpha_composite(sq(180)); bg.convert('RGB').save('assets/apple-touch-icon.png',optimize=True)
src=open('faq.html',encoding='utf-8').read()
head_end=src.index('<main id="main">'); foot=src[src.index('</main>')+7:]
hdr=src[src.index('<body'):head_end]
def mk(out,title,desc,main,css='faq'):
    h=src[:src.index('<body')]
    h=re.sub(r'<title>.*?</title>','<title>%s</title>'%title,h)
    h=re.sub(r'(<meta name="description" content=")[^"]*','\\g<1>'+desc,h)
    h=re.sub(r'(<meta property="og:title" content=")[^"]*','\\g<1>'+title,h)
    h=re.sub(r'(<meta property="og:description" content=")[^"]*','\\g<1>'+desc,h)
    h=h.replace('css/pages/faq.css','css/pages/%s.css'%css)
    b=re.sub(r'<body class="[^"]*"','<body class="pg-legal"',hdr)
    open(out,'w',encoding='utf-8').write(h+b+main+foot)
sec=lambda inner:'<main id="main">\n<section class="pg-hero" aria-labelledby="pg-title"><div class="h-wrap">%s</div></section>\n</main>'
mk('404.html','Page not found | ASW Law Advocates LLP','The page you are looking for could not be found.',
 '<main id="main">\n<section class="lg-sec"><div class="lg-wrap lg-center"><p class="lg-eye"><span class="lg-dot" aria-hidden="true"></span>Error 404</p><h1 id="pg-title" class="lg-h1">Page not found</h1><p class="lg-p">The page you are looking for may have moved or no longer exists. Use the links below to continue.</p><p class="lg-btns"><a class="h-pillbtn" href="index.html">Back to Home</a><a class="lg-link" href="contact.html">Contact us</a></p></div></section>\n</main>')
LEG='<main id="main">\n<section class="lg-sec"><div class="lg-wrap"><p class="lg-eye"><span class="lg-dot" aria-hidden="true"></span>%s</p><h1 id="pg-title" class="lg-h1">%s</h1>%s</div></section>\n</main>'
P=lambda *t:''.join('<p class="lg-p">%s</p>'%x for x in t)
mk('privacy.html','Privacy | ASW Law Advocates LLP','How ASW Law Advocates LLP handles the information you share with us.',
 LEG%('Legal','Privacy',P('Sample copy for review, to be confirmed by the firm.','We treat all information you share with us as confidential, in line with our professional obligations as advocates.','To discuss how your information is handled, call +254 788 685 911 or email info@aswlaw.africa.')))
mk('terms.html','Terms | ASW Law Advocates LLP','Terms of use for the ASW Law Advocates LLP website.',
 LEG%('Legal','Terms',P('Sample copy for review, to be confirmed by the firm.','The information on this website is general in nature and is not legal advice. Please contact us to discuss your specific matter.','For any question about these terms, call +254 788 685 911 or email info@aswlaw.africa.')))
open('css/pages/legal.css','w').write('''/* Page styles: 404, privacy, terms */
.lg-sec{background:#F2F2F0;padding:72px 0 88px;flex:0 0 auto}
.lg-wrap{max-width:760px;margin:0 auto;padding:0 20px}
.lg-center{text-align:center}
.lg-eye{display:flex;align-items:center;gap:8px;margin:0 0 10px;font-size:12px;line-height:16px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#1B4584}
.lg-center .lg-eye{justify-content:center}
.lg-dot{width:6px;height:6px;border-radius:50%;background:#94BBE4}
.lg-h1{margin:0 0 16px;font-family:Marcellus,serif;font-weight:400;font-size:34px;line-height:1.1;color:#0E1F3D}
.lg-p{margin:0 0 16px;font-size:16px;line-height:1.7;color:#33445F}
.lg-btns{display:flex;flex-wrap:wrap;gap:20px;align-items:center;justify-content:center;margin:28px 0 0}
.lg-link{font-weight:600;color:#0F74B5;text-decoration:underline;text-underline-offset:4px}
@media (min-width:641px){.lg-sec{padding:96px 0 112px}.lg-h1{font-size:44px}.lg-p{font-size:17px}}
@media (min-width:1025px){.lg-sec{padding:120px 0 140px}.lg-h1{font-size:56px}.lg-p{font-size:18px}}
''')
open('robots.txt','w').write('# REMOVE BEFORE LAUNCH: the copy on this site is sample copy for client review.\n# Delete the Disallow rule below (and the robots meta tag on every page) when the firm approves the copy.\nUser-agent: *\nDisallow: /\n')
json.dump({"cleanUrls":True,"trailingSlash":False,"headers":[
 {"source":"/assets/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=31536000, immutable"}]},
 {"source":"/(css|js)/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=86400, must-revalidate"}]},
 {"source":"/(.*)","headers":[{"key":"X-Content-Type-Options","value":"nosniff"},{"key":"Referrer-Policy","value":"strict-origin-when-cross-origin"},{"key":"X-Robots-Tag","value":"noindex, nofollow"}]}]},open('vercel.json','w'),indent=2)
print('extras ok')
