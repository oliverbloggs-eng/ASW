#!/usr/bin/env python3
"""Convert source/*.dc.html (Claude Design) to a static site at the repo root.
Run from the repo root: python3 tools/build_static.py"""
import re,os,sys,json,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,'tools'))
from csstools import flatten,emit
from PIL import Image
os.chdir(ROOT)
PAGES={ # source -> (output file, body class, title, description)
 'Main':('index.html','home','ASW Law Advocates LLP | Legal Practice in Nairobi, Kenya','We are a legal practice based in Nairobi, Kenya, specializing in offering client-centric legal solutions to our clientele, which includes individuals and corporations.'),
 'About':('about.html','about','About Us | ASW Law Advocates LLP','About ASW Law Advocates LLP: who we are, our pillars, our approach and our team of advocates in Nairobi.'),
 'Areas':('areas-of-practice.html','areas','Areas of Practice | ASW Law Advocates LLP','Our areas of practice: dispute resolution, commercial and corporate, public procurement and tax, property and real estate, private client, and employment and pensions.'),
 'Insights':('insights.html','insights','Insights | ASW Law Advocates LLP','Recent blog posts and insights from ASW Law Advocates LLP.'),
 'Article':('article-know-about-industrial-laws.html','article','Know about Industrial Laws | ASW Law Advocates LLP','Know about Industrial Laws: an insight from ASW Law Advocates LLP.'),
 'ArticleMarriage':('article-flexibility-of-marriage-in-us.html','article','Flexibility of marriage in US | ASW Law Advocates LLP','Flexibility of marriage in US: an insight from ASW Law Advocates LLP.'),
 'Contact':('contact.html','contact','Contact Us | ASW Law Advocates LLP','Contact ASW Law Advocates LLP, Tourism Fund Building, Nairobi. Call +254 788 685 911 or email info@aswlaw.africa.'),
 'FAQ':('faq.html','faq','Frequently Asked Questions | ASW Law Advocates LLP','Answers to common questions about booking an appointment, confidentiality, fees and our areas of practice.'),
}
LINKS={'Main.dc.html':'index.html','About.dc.html':'about.html','Areas.dc.html':'areas-of-practice.html','Insights.dc.html':'insights.html','Article.dc.html':'article-know-about-industrial-laws.html','ArticleMarriage.dc.html':'article-flexibility-of-marriage-in-us.html','Contact.dc.html':'contact.html','FAQ.dc.html':'faq.html','Book.dc.html':'contact.html#send-a-message','Privacy.dc.html':'privacy.html','Terms.dc.html':'terms.html'}
NOINDEX='<!-- REMOVE BEFORE LAUNCH: this page is sample copy for client review, so search engines are told not to index it. Delete the robots meta tag below and the Disallow rule in robots.txt when the firm approves the copy. -->\n<meta name="robots" content="noindex, nofollow">'
def read(p): return open(p,encoding='utf-8').read()

# ---------- images ----------
IMG={}
for f in os.listdir('assets'):
    if f.lower().endswith(('.jpg','.png')):
        try:
            with Image.open('assets/'+f) as im: IMG[f]=im.size
        except Exception: pass

# ---------- CSS ----------
def drop_rule(r):
    ctx,sel,body=r
    if 'wa-' in sel or sel.startswith('@keyframes wa-'): return True
    if re.match(r'^(\.rv|\.nv)$',sel): return True
    if sel.startswith('@keyframes') and re.search(r'(pg-rise|nv-rise)',sel): return True
    return False
raw={}
for src in PAGES:
    css=re.search(r'<style>(.*?)</style>',read('source/%s.dc.html'%src),re.S).group(1)
    raw[src]=[r for r in flatten(css) if not drop_rule(r)]
shared=set.intersection(*[set(v) for v in raw.values()])
seen=set();shared_rules=[]
for r in raw['Main']:
    if r in shared and r not in seen: seen.add(r);shared_rules.append(r)
SHARED_EXTRA=read('tools/site_extra.css')
os.makedirs('css/pages',exist_ok=True)
open('css/styles.css','w',encoding='utf-8').write('/* Shared styles: header, footer, base, type system, interactions. Page specific styles live in css/pages/. */\n'+emit(shared_rules)+SHARED_EXTRA)
for src,(out,cls,t,d) in PAGES.items():
    rest=[r for r in raw[src] if r not in shared]
    open('css/pages/%s.css'%cls if cls!='article' else 'css/pages/article.css','w',encoding='utf-8').write('/* Page styles: %s */\n'%out+emit(rest))
# article.css: both articles identical css; verified below

# ---------- HTML ----------
def body_of(src):
    s=read('source/%s.dc.html'%src)
    return s[s.index('</helmet>')+9:s.index('</x-dc>')]
def common(b):
    b=re.sub(r'<!--.*?-->','',b,flags=re.S)
    for k,v in LINKS.items(): b=b.replace('href="%s'%k,'href="%s'%v)
    # menu
    b=re.sub(r'<sc-if value="\{\{open\}\}"[^>]*>(.*?)</sc-if>',lambda m:m.group(1).replace('<nav class="h-menu" aria-label="Mobile">','<nav class="h-menu" id="mobile-menu" aria-label="Mobile" hidden>'),b,flags=re.S)
    b=b.replace('aria-label="{{burgerLabel}}" aria-expanded="{{open}}" onClick="{{toggle}}"','aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu" data-menu-toggle')
    b=b.replace('d="{{burgerPath}}"','d="M4 7h16M4 12h16M4 17h16"')
    # wa
    b=re.sub(r'<div class="wa-w">.*?</a>\s*</div>','',b,flags=re.S)
    # images
    def img(m):
        tag=m.group(0)
        src=re.search(r'src="([^"]+)"',tag).group(1)
        name=os.path.basename(src)
        tag=tag.replace('../assets/','assets/')
        if name in IMG and 'width=' not in tag:
            w,h=IMG[name]; tag=tag.replace('<img ','<img width="%d" height="%d" '%(w,h),1)
        eager=re.search(r'class="(h-logo|pg-statue|h-art|h-hero)',tag) or 'h-logo' in tag
        if 'loading=' not in tag and not name.startswith('logo'):
            if not re.search(r'class="[^"]*(h-statue|h-art-img|pg-statue)',tag): tag=tag.replace('<img ','<img loading="lazy" decoding="async" ',1)
        return tag
    b=re.sub(r'<img [^>]*>',img,b)
    b=re.sub(r'\s+(onClick|onScroll)="\{\{[^}]*\}\}"','',b)
    return b
HDR_OPEN=lambda cls:'<body class="pg-%s">\n<a class="skip" href="#main">Skip to content</a>\n'%cls
WA='''
<div class="wa-w" id="wa"><a class="wa-b" href="https://wa.me/254788685911" target="_blank" rel="noopener" aria-label="Chat with ASW Law Advocates on WhatsApp"><svg aria-hidden="true" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21l1.65-4.9A8.5 8.5 0 1 1 8 19.4L3 21z"/><path d="M9 8.6c.2 2.7 2.6 5.4 5.6 5.9l1.2-1.3c.2-.2.5-.3.8-.2l1.5.6c.3.1.5.4.4.7-.4 1.2-1.6 1.9-2.8 1.8-3.8-.4-7-3.5-7.4-7.2-.1-1.2.6-2.3 1.8-2.6.3-.1.6.1.7.4l.6 1.5c.1.3 0 .6-.2.8"/></svg></a></div>
'''
JSONLD='''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"LegalService","name":"ASW Law Advocates LLP","telephone":"+254 788 685 911","email":"info@aswlaw.africa","address":{"@type":"PostalAddress","streetAddress":"Tourism Fund Building, Mezzanine Floor, Office M08, Off-Bishop Rd, Community Area","addressLocality":"Nairobi","addressCountry":"Kenya"},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"17:00"}]}
</script>
'''
def head(title,desc,cls,out,og_img='assets/hero.jpg',css_page=None,extra=''):
    css_page=css_page or cls
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{NOINDEX}
<meta name="theme-color" content="#0E1F3D">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ASW Law Advocates LLP">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Marcellus&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
<link rel="stylesheet" href="css/pages/{css_page}.css">
{extra}<script>document.documentElement.classList.add('js')</script>
<script src="js/main.js" defer></script>
</head>
'''
def wrap_main(b):
    i=b.index('</header>')+len('</header>')
    j=b.index('<footer')
    return b[:i]+'\n<main id="main">'+b[i:j]+'</main>\n'+b[j:]
def finish(b):
    b=re.sub(r'<div style="width:100%;background:#ffffff;timeline-scope:[^"]*">\s*','',b)
    b=b.rstrip()
    if b.endswith('</div>') and 'class="h-root"' in b:
        pass
    return b
def page(src):
    out,cls,t,d=PAGES[src]
    b=common(body_of(src))
    # page specific dynamic bits
    if src=='Main':
        for k,v in {'{{cur}}':'01','{{fillCls}}':'at-fill s0','{{prevCls}}':'at-btn dis','{{nextCls}}':'at-btn','{{prevAria}}':'true','{{nextAria}}':'false','{{tc0}}':'ta-l on','{{tc1}}':'ta-l','{{tc2}}':'ta-l','{{tcur}}':'01','{{tFill}}':'at-fill t0','{{tPrevCls}}':'at-btn dis','{{tNextCls}}':'at-btn','{{tPrevAria}}':'true','{{tNextAria}}':'false'}.items(): b=b.replace(k,v)
    if src=='About':
        b=re.sub(r'\{\{(c_\w+)\}\}',lambda m:'ac open' if m.group(1)=='c_p0' else 'ac',b)
        b=re.sub(r'\{\{a_(\w+)\}\}',lambda m:'true' if m.group(1)=='p0' else 'false',b)
        for k,v in {'{{tc0}}':'ta-l on','{{tc1}}':'ta-l','{{tc2}}':'ta-l','{{tcur}}':'01','{{tFill}}':'at-fill t0','{{tPrevCls}}':'at-btn dis','{{tNextCls}}':'at-btn','{{tPrevAria}}':'true','{{tNextAria}}':'false'}.items(): b=b.replace(k,v)
        dots=''.join('<button class="tm-dotb" type="button" aria-label="Show team member %d of 3" aria-current="%s" data-dot="%d"><span class="tm-dot%s"></span></button>'%(i+1,'true' if i==0 else 'false',i,' on' if i==0 else '') for i in range(3))
        b=re.sub(r'<sc-for list="\{\{dots\}\}".*?</sc-for>',dots,b,flags=re.S)
        b=re.sub(r'\s+onClick="\{\{[^}]*\}\}"','',b)
    if src=='Areas':
        ids=['dispute','commercial','procurement','property','private','employment']
        labels=['Dispute Resolution','Commercial and Corporate','Public Procurement and Tax','Property &amp; Real Estate','Private Client','Employment and Pensions']
        lis=''.join('<li><a class="ab-pill%s" href="#%s"%s>%s</a></li>'%(' on' if i==0 else '',ids[i],' aria-current="true"' if i==0 else '',labels[i]) for i in range(6))
        b=re.sub(r'<sc-for list="\{\{pills\}\}".*?</sc-for>',lis,b,flags=re.S)
    if src=='FAQ':
        for k in ['all','g','0','1','2','3','4','5']:
            b=b.replace('{{pc_%s}}'%k,'fq-pill on' if k=='all' else 'fq-pill').replace('{{pa_%s}}'%k,'true' if k=='all' else 'false')
            b=b.replace('data-x','')
        for n in range(10): b=b.replace('{{fc_%d}}'%n,'fq-i')
        tags=['g']*4+['0','1','2','3','4','5']
        pills=iter(['all','g','0','1','2','3','4','5'])
        b=re.sub(r'<button class="fq-pill( on)?" type="button" aria-pressed="(true|false)"',lambda m:'<button class="fq-pill%s" type="button" aria-pressed="%s" data-filter="%s"'%(m.group(1) or '',m.group(2),next(pills)),b)
        n=iter(range(10))
        b=re.sub(r'<li class="fq-i">',lambda m:'<li class="fq-i" data-tag="%s">'%tags[next(n)],b)
        b=re.sub(r'\s+onClick="\{\{[^}]*\}\}"','',b)
    if src=='Contact':
        b=b.replace('<form class="ct-form" action="#" method="post">','<form class="ct-form" id="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="post" novalidate><input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">')
        b=b.replace('<div class="ct-card rv">','<div class="ct-card rv" id="send-a-message">',1)
        # map: iframe
        b=re.sub(r'<img [^>]*class="mp-img"[^>]*>','<iframe class="mp-embed" title="Map of Tourism Fund Building, Valley Rd, Nairobi" src="https://www.google.com/maps?q=Tourism+Fund+Building,+Valley+Rd,+Nairobi&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>',b)
    b=finish(wrap_main(b))
    if src=='Contact':
        okhtml=re.search(r'<div class="ct-ok" role="status">.*?</div>',read('source/ContactFormStates.dc.html'),re.S).group(0)
        okhtml=okhtml.replace('<div class="ct-ok" role="status">','<div class="ct-ok" role="status" id="contact-ok" hidden>',1)
        b=b.replace('</form></div>\n        <aside','</form>'+okhtml+'</div>\n        <aside',1)
    extra=JSONLD if src=='Main' else ''
    og='assets/hero.jpg'
    html_out=head(t,d,cls,out,og,cls if cls!='article' else 'article',extra)+HDR_OPEN(cls)+b+'\n'+WA+'</body>\n</html>\n'
    html_out=re.sub(r'\n{3,}','\n\n',html_out)
    open(out,'w',encoding='utf-8').write(html_out)
for s in PAGES: page(s)
print('built',len(PAGES))
