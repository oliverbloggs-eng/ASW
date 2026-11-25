import re,os
src=open('/home/claude/hero/gen.py').read().split('TEMPLATE = open')[0]
exec(src)
import sys; sys.path.insert(0,'/home/claude/hero')
from about import FOOT_CSS, foot_html
from home3 import PV_CSS, how_list
from faqdata import *
HW_CSS=r"""
.h-root .hw3{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;margin:48px 0 0;padding:0;list-style:none}
.hw3-s{position:relative}
.hw3-s::after{content:"";position:absolute;top:27px;left:72px;right:-12px;height:1.5px;background:#94BBE4}
.hw3-s:last-child::after{display:none}
.hw3-c{position:relative;z-index:1;display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border-radius:50%;background:#ffffff;border:2px solid #94BBE4;font-size:20px;font-weight:600;font-variant-numeric:lining-nums;color:#0E1F3D}
.hw3-t{margin:18px 0 0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:26px;line-height:1.2;color:#0E1F3D}
.hw3-ph{margin:10px 0 0;font-size:16px;line-height:1.6;color:#2A3A55}
@media (max-width:1023px){.h-root .hw3{gap:16px;margin-top:36px}.hw3-t{font-size:22px}}
@media (max-width:640px){
  .h-root .hw3{grid-template-columns:minmax(0,1fr);gap:0;margin-top:28px}
  .hw3-s{display:grid;grid-template-columns:56px minmax(0,1fr);column-gap:20px;align-items:center;min-height:56px;padding-bottom:28px}
  .hw3-s:last-child{padding-bottom:0}
  .hw3-s::after{top:56px;left:27px;right:auto;width:1.5px;height:calc(100% - 56px)}
  .hw3-t{margin:0;font-size:26px}
  .hw3-ph{grid-column:2;margin-top:6px}
}
"""
P["building"]='<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4"/><path d="M10 10h4"/><path d="M10 14h4"/><path d="M10 18h4"/>'
P["checkc"]='<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>'
P["arrowur"]='<path d="M7 7h10v10"/><path d="M7 17 17 7"/>'
P["pin"]='<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>'

T=open('/home/claude/hero/template.html',encoding='utf-8').read()
# ---- shared css: header/top bar/menu only ----
css=T[T.index('<style>')+7:T.index('</style>')]
def blocks(s):
    out=[];i=0;n=len(s)
    while i<n:
        j=s.find('{',i)
        if j<0:break
        depth=1;k=j+1
        while depth and k<n:
            depth+= (s[k]=='{')-(s[k]=='}');k+=1
        out.append((s[i:j].strip(),s[j+1:k-1]));i=k
    return out
KEEP=re.compile(r'\.h-(root|wrap|top|ti|nav|links|logo|pillbtn|burger|menu|hours|email|top-r)\b|^body|^\*')
def filt(rules):
    res=''
    for sel,body in blocks(rules):
        if sel.startswith('@media'):
            inner=filt(body)
            if inner.strip(): res+=sel+'{'+inner+'}\n'
        elif KEEP.search(sel) or sel.startswith('/*'):
            res+=sel+'{'+body+'}\n'
    return res
# strip comments first
css_nc=re.sub(r'/\*.*?\*/','',css,flags=re.S)
BASE_CSS=filt(css_nc)

PAGE_CSS=r"""
.h-root{overflow-x:clip}
.h-root ol{list-style:none;margin:0;padding:0}
.pg-wrap{max-width:1280px;margin:0 auto;padding:0 40px}
.sec{position:relative;padding:96px 0}
.sec-w{background:#ffffff}.sec-o{background:#F2F2F0}
.pg-hero + .sec{padding-top:80px}
.sec-eyebrow{display:flex;align-items:center;gap:14px;font-size:13px;line-height:16px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#0B66A0}
.sec-eyebrow::before{content:"";width:36px;height:2px;background:#0B66A0}
.sec-h2{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:44px;line-height:1.12;letter-spacing:-.01em;color:#0E1F3D;text-wrap:balance}
.sec-eyebrow + .sec-h2{margin-top:20px}
.sec-bar{display:block;width:64px;height:4px;margin-top:26px;border-radius:4px;background:#94BBE4}

/* page hero */
.pg-hero{position:relative;overflow:clip;isolation:isolate;background:radial-gradient(ellipse 46% 95% at 74% 62%,rgba(27,69,132,.95) 0%,rgba(27,69,132,.45) 55%,rgba(27,69,132,0) 100%),linear-gradient(90deg,#0E1F3D 0%,#0E1F3D 38%,#16376C 100%);color:#ffffff}
.pg-fin{position:absolute;left:-120px;bottom:-190px;width:620px;height:620px;opacity:.06;z-index:0;pointer-events:none}
.pg-hair{display:block;width:80px;height:1px;margin:0 0 18px;background:#94BBE4}
.pg-hero-in{position:relative;max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:minmax(0,1fr) 340px;column-gap:40px;min-height:360px}
.pg-copy{position:relative;z-index:3;display:flex;flex-direction:column;justify-content:center;align-items:flex-start;padding:32px 0}
.pg-crumb ol{display:flex;flex-wrap:wrap;align-items:center;gap:0 12px}
.pg-crumb li{display:inline-flex;align-items:center;gap:12px;font-size:15px;color:#C9DBF0}
.pg-crumb a{display:inline-flex;align-items:center;min-height:44px;color:#C9DBF0;border-bottom:1px solid transparent}
.pg-crumb a:hover{color:#ffffff;border-bottom-color:#94BBE4}
.pg-crumb [aria-current]{color:#ffffff;font-weight:600}
.pg-h1{margin:6px 0 14px;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:76px;line-height:1.04;letter-spacing:-.015em;color:#ffffff}
.pg-tag{margin:0;font-size:20px;line-height:1.55;color:#C9DBF0;max-width:520px}
.pg-art{position:relative;z-index:1;margin-right:96px}
.pg-arch2,.pg-arch{position:absolute;left:50%;bottom:0;border:1.5px solid rgba(148,187,228,.26);border-bottom:0}
.pg-arch{width:231px;height:280px;margin-left:-115px;border-radius:115px 115px 0 0}
.pg-arch2{width:266px;height:304px;margin-left:-133px;border-radius:133px 133px 0 0;border-color:rgba(148,187,228,.13)}
.pg-statue{position:absolute;left:50%;bottom:-30px;height:358px;width:auto;max-width:none;transform:translateX(-50%);filter:drop-shadow(0 22px 30px rgba(0,0,0,.38))}

/* who we are */
.wh-grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:48px 96px;align-items:start}
.wh-p{margin:36px 0 0;font-size:20px;line-height:1.65;color:#33445F;max-width:560px}
.wh-cards{display:flex;flex-direction:column;gap:20px}
.wh-card{display:flex;align-items:flex-start;gap:22px;padding:30px;background:#ffffff;border:1px solid #E6ECF4;border-radius:20px;box-shadow:0 14px 40px rgba(14,31,61,.07)}
.pg-ic{display:inline-flex;align-items:center;justify-content:center;flex:none;width:56px;height:56px;border-radius:50%;background:#ffffff;border:1px solid #C9DBF0;color:#1B4584}
.wh-card h3{margin:2px 0 8px;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:26px;line-height:1.2;color:#0E1F3D}
.wh-card p{margin:0;font-size:16px;line-height:1.6}

/* pillars */
.h-root .pl-list{display:flex;flex-direction:column;gap:24px;margin-top:48px}
.pl-card{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);align-items:center;gap:48px;padding:44px 56px;background:#ffffff;border:1px solid #E6ECF4;border-radius:24px;box-shadow:0 14px 40px rgba(14,31,61,.06)}
.pl-card:nth-child(even) .pl-id{order:2;justify-self:end}
.pl-card:nth-child(even) .pl-tx{order:1}
.pl-id{display:flex;align-items:center;gap:28px}
.pl-num{font-family:'DM Sans',system-ui,sans-serif;font-weight:500;font-variant-numeric:lining-nums;font-feature-settings:'lnum' 1;font-size:112px;line-height:1;letter-spacing:-.03em;color:#94BBE4}
.pl-z{display:inline-block;transform:scaleX(.74);transform-origin:0 50%;margin-right:-.17em}
.pl-id .pg-ic{width:72px;height:72px}
.pl-tx h3{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:36px;line-height:1.15;color:#0E1F3D}
.pl-tx p{margin:12px 0 0;font-size:18px;line-height:1.6}

/* facts */
.fs{position:relative;background:#0E1F3D;color:#ffffff;padding:96px 0}
.fs-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.fs-i{display:flex;flex-direction:column;padding:8px 32px;border-left:1px solid rgba(255,255,255,.16)}
.fs-i:first-child{border-left:0;padding-left:0}
.fs-n{font-family:'Marcellus',Georgia,serif;font-size:72px;line-height:1;color:#ffffff}
.fs-l{margin-top:16px;font-size:14px;line-height:20px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#C9DBF0}

/* team */
.h-root .tm-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin-top:48px}
.tm-card{display:flex;flex-direction:column;height:100%;padding:20px 20px 30px;background:#ffffff;border:1px solid #E6ECF4;border-top:3px solid transparent;border-radius:24px;box-shadow:0 14px 40px rgba(14,31,61,.07);transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}
.tm-card:hover{transform:translateY(-6px);border-top-color:#94BBE4;box-shadow:0 26px 56px rgba(14,31,61,.14)}
.tm-ph{position:relative;aspect-ratio:4/5;border-radius:20px;background:#0E1F3D;overflow:hidden;isolation:isolate}
.tm-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 10%;display:block}
.tm-ph::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,31,61,0) 58%,rgba(14,31,61,.5) 100%);pointer-events:none}
.tm-body{display:flex;flex-direction:column;padding:26px 8px 0}
.tm-name{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:28px;line-height:1.15;color:#0E1F3D}
.tm-role{margin:8px 0 0;font-size:16px;line-height:1.5}
.tm-bio{margin:14px 0 0;font-size:16px;line-height:1.6}
.tm-mem{margin-top:22px;padding-top:20px;border-top:1px solid #E3E6EC}
.tm-mem-h{font-size:13px;line-height:16px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#0B66A0}
.h-root .tm-mem ul{display:flex;flex-direction:column;gap:10px;margin-top:14px}
.tm-mem li{display:flex;align-items:center;gap:12px;font-size:16px;line-height:1.4;color:#0E1F3D}
.tm-mem li svg{flex:none;color:#1B4584}
.tm-dots{display:none}

/* areas */
.h-root .ap-list{display:flex;flex-wrap:wrap;gap:16px;margin-top:48px}
.ap-pill{display:inline-flex;align-items:center;justify-content:space-between;gap:20px;min-height:64px;padding:8px 10px 8px 28px;border-radius:999px;background:#ffffff;border:1px solid #E1E7F0;font-size:17px;font-weight:500;color:#0E1F3D;transition:background .2s ease,color .2s ease,border-color .2s ease}
.ap-go{display:inline-flex;align-items:center;justify-content:center;flex:none;width:44px;height:44px;border-radius:50%;background:#F2F2F0;color:#1B4584;transition:background .2s ease,color .2s ease}
.ap-pill:hover{background:#1B4584;border-color:#1B4584;color:#ffffff}
.ap-pill:hover .ap-go{background:#94BBE4;color:#0E1F3D}

/* visit */
.vs-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:64px;align-items:stretch}
.vs-addr{margin:20px 0 0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:30px;line-height:1.3;color:#0E1F3D;max-width:520px}
.h-root .vs-list{display:flex;flex-direction:column;gap:18px;margin-top:36px;padding-top:32px;border-top:1px solid #E3E6EC}
.vs-item{display:flex;align-items:flex-start;gap:16px}
.vs-item .pg-ic{width:44px;height:44px}
.vs-lab{display:block;font-size:13px;line-height:16px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#0B66A0}
.vs-val{display:block;margin-top:4px;font-size:17px;line-height:1.5;color:#0E1F3D}
.vs a.vs-val{display:inline-flex;align-items:center;min-height:44px;margin-top:-6px}
.vs a.vs-val:hover{color:#0F74B5}
.vs-maps{display:inline-flex;align-items:center;gap:10px;min-height:44px;margin-top:22px;font-size:16px;font-weight:600;color:#0B66A0;border-bottom:2px solid transparent}
.vs-maps:hover{border-bottom-color:#0B66A0}
.vs-map{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;min-height:460px;border-radius:24px;background:repeating-linear-gradient(0deg,rgba(27,69,132,.06) 0 1px,transparent 1px 56px),repeating-linear-gradient(90deg,rgba(27,69,132,.06) 0 1px,transparent 1px 56px),rgba(27,69,132,.08);color:#1B4584;border:1px solid #DCE5F2}
.vs-map span{font-family:'Marcellus',Georgia,serif;font-size:26px;color:#0E1F3D}

/* subtle fade-up on scroll (CSS only, progressive) */
@keyframes pg-rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
@supports (animation-timeline:view()){@media (prefers-reduced-motion:no-preference){
  .rv{animation:pg-rise linear both;animation-timeline:view();animation-range:entry 0% entry 55%}
}}
@media (prefers-reduced-motion:reduce){.tm-card{transition:none}.tm-card:hover{transform:none}}

@media (max-width:1023px){
  .sec,.fs{padding:80px 0}
  .pg-wrap,.pg-hero-in{padding-left:32px;padding-right:32px}
  .sec-h2{font-size:40px}
  .pg-hero-in{grid-template-columns:minmax(0,1fr) 250px;column-gap:24px;min-height:300px}
  .pg-art{margin-right:40px}
  .pg-fin{width:480px;height:480px;left:-120px;bottom:-150px}
  .pg-h1{font-size:56px}
  .pg-copy{padding:24px 0}
  .pg-tag{font-size:19px}
  .pg-arch{width:170px;height:228px;margin-left:-85px;border-radius:85px 85px 0 0}
  .pg-arch2{width:198px;height:252px;margin-left:-99px;border-radius:99px 99px 0 0}
  .pg-statue{height:292px;bottom:-24px}
  .wh-grid{grid-template-columns:minmax(0,1fr);gap:40px}
  .wh-p{margin-top:32px;max-width:none}
  .pl-card{grid-template-columns:minmax(0,4fr) minmax(0,7fr);gap:32px;padding:36px 36px}
  .pl-card:nth-child(even) .pl-id,.pl-card:nth-child(even) .pl-tx{order:0;justify-self:auto}
  .pl-num{font-size:84px}
  .pl-id{gap:20px}
  .pl-id .pg-ic{width:60px;height:60px}
  .pl-tx h3{font-size:34px}
  .fs-grid{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:32px}
  .fs-i:nth-child(odd){border-left:0;padding-left:0}
  .fs-i:nth-child(n+3){border-top:1px solid rgba(255,255,255,.16);padding-top:32px}
  .h-root .tm-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;margin-top:36px}
  .h-root .ap-list{margin-top:36px}
  .vs-grid{grid-template-columns:minmax(0,1fr);gap:40px}
  .vs-map{min-height:340px}
}
@media (max-width:640px){
  .sec,.fs{padding:64px 0}
  .pg-wrap,.pg-hero-in{padding-left:20px;padding-right:20px}
  .pg-hero + .sec{padding-top:56px}
  .sec-h2{font-size:32px}
  .sec-eyebrow{font-size:14px}
  .sec-bar{margin-top:22px}
  .pg-hero-in{grid-template-columns:minmax(0,1fr);min-height:260px}
  .pg-copy{padding:12px 0 18px;max-width:calc(100% - 128px)}
  .pg-crumb li{font-size:16px}
  .pg-h1{font-size:34px;line-height:1.1;margin:0 0 10px}
  .pg-tag{font-size:16px;line-height:1.5}
  .pg-art{position:absolute;right:14px;top:0;bottom:0;width:116px;height:auto;margin:0}
  .pg-fin{width:360px;height:360px;left:-100px;bottom:-150px}
  .pg-arch{width:84px;height:150px;margin-left:-42px;border-radius:42px 42px 0 0}
  .pg-arch2{width:106px;height:168px;margin-left:-53px;border-radius:53px 53px 0 0}
  .pg-statue{height:232px;bottom:-14px}
  .wh-p{font-size:17px;margin-top:28px}
  .wh-card{padding:22px;gap:16px}
  .wh-card h3{font-size:24px}
  .pg-ic{width:48px;height:48px}
  .h-root .pl-list{margin-top:36px;gap:20px}
  .pl-card{grid-template-columns:minmax(0,1fr);gap:20px;padding:28px 24px}
  .pl-num{font-size:68px}
  .pl-id .pg-ic{width:56px;height:56px}
  .pl-tx h3{font-size:30px}
  .pl-tx p{font-size:17px}
  .fs-n{font-size:46px}
  .fs-l{font-size:14px;margin-top:12px}
  .fs-i{padding:8px 16px}
  .fs-i:nth-child(n+3){padding-top:28px}
  .h-root .tm-grid{display:flex;gap:14px;margin:28px -20px 0;padding:4px 20px 12px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:20px;scrollbar-width:none;-webkit-overflow-scrolling:touch}
  .tm-grid::-webkit-scrollbar{display:none}
  .tm-grid>li{flex:0 0 calc((100% + 40px) * .85);scroll-snap-align:start}
  .tm-dots{display:flex;justify-content:center;margin-top:6px}
  .tm-dotb{display:inline-flex;align-items:center;justify-content:center;width:32px;height:44px;padding:0;border:0;background:transparent;cursor:pointer}
  .tm-dot{display:block;width:8px;height:8px;border-radius:8px;background:rgba(14,31,61,.25);transition:width .25s ease,background .25s ease}
  .tm-dot.on{width:24px;background:#1B4584}
  .h-root .ap-list{gap:12px;margin-top:28px}
  .ap-pill{min-height:60px;font-size:17px}
  .vs-addr{font-size:26px}
  .vs-map{min-height:280px}
}
"""
STATUS=''
def build(name,title,w,h):
    head=T[T.index('<!-- Contact bar -->'):T.index('<!-- Hero -->')]
    head=head.replace('<a class="cur" href="Main.dc.html" aria-current="page">Home</a>','<a href="Main.dc.html">Home</a>')
    head=head.replace('<a href="About.dc.html">About Us</a>','<a class="cur" href="About.dc.html" aria-current="page">About Us</a>')
    head=head.replace('<a class="l cur" href="Main.dc.html" aria-current="page">Home</a>','<a class="l" href="Main.dc.html">Home</a>')
    head=head.replace('<a class="l" href="About.dc.html">About Us</a>','<a class="l cur" href="About.dc.html" aria-current="page">About Us</a>')
    head=(head.replace("@@LOGO@@",LOGO).replace("@@I_CLOCK@@",ic("clock",15)).replace("@@I_MAIL@@",ic("mail",15)).replace("@@I_PHONE@@",ic("phone",15)))
    areas=''.join('      <li><a class="ap-pill" href="Areas.dc.html"><span>%s</span><span class="ap-go" aria-hidden="true">%s</span></a></li>\n'%(a,ic("arrow",20,2)) for a,_ in AREAS)
    pill=''
    for n,(t,k) in enumerate((("Competence","checks"),("Integrity","shield"),("Pragmatism","scale")),1):
        pill+='''      <li class="pl-card rv"><div class="pl-id"><span class="pl-num" aria-hidden="true"><span class="pl-z">0</span>%d</span><span class="pg-ic">%s</span></div><div class="pl-tx"><h3>%s</h3><p class="bd">%s</p></div></li>\n'''%(n,ic(k,32,1.6),t,PILL[t])
    team=''
    for ini,nm in (("AS","Anthony Simiyu"),("AO","Alphonse Odido"),("RC","Roy Chidi")):
        team+='''      <li><article class="tm-card">
        <div class="tm-ph"><img class="tm-img" src="/_blob/6a71c35ed220aaa8ba6455a78de01d88" alt="Portrait of %s"></div>
        <div class="tm-body">
          <h3 class="tm-name">%s</h3>
          <p class="tm-role bd">Advocate</p>
          <p class="tm-bio bd">%s</p>
          <div class="tm-mem"><div class="tm-mem-h">Professional Memberships</div>
            <ul><li>%s<span>Law Society of Kenya</span></li><li>%s<span>East Africa Law Society</span></li></ul></div>
        </div>
      </article></li>
'''%(nm,nm,BIO(nm),ic("checkc",22,1.7),ic("checkc",22,1.7))
    body=f'''
<div class="h-root">

  {head}
  <!-- Page hero -->
  <section class="pg-hero" aria-labelledby="pg-title">
    <svg class="pg-fin" viewBox="0 0 760 760" fill="none" stroke="#94BBE4" stroke-width="3" aria-hidden="true"><path d="M60 760V380a320 320 0 0 1 640 0v380"/><path d="M130 760V380a250 250 0 0 1 500 0v380"/><path d="M200 760V380a180 180 0 0 1 360 0v380"/><path d="M270 760V380a110 110 0 0 1 220 0v380"/></svg>
    <div class="pg-hero-in">
      <div class="pg-copy">
        <nav class="pg-crumb" aria-label="Breadcrumb"><ol><li><a href="Main.dc.html">Home</a><span aria-hidden="true">/</span></li><li><span aria-current="page">About Us</span></li></ol></nav>
        <h1 class="pg-h1" id="pg-title">About Us</h1>
        <p class="pg-tag">We offer world-class legal representation.</p>
      </div>
      <div class="pg-art">
        <div class="pg-arch2" aria-hidden="true"></div>
        <div class="pg-arch" aria-hidden="true"></div>
        <img class="pg-statue" src="{STATUE}" alt="Bronze statue of blindfolded Lady Justice holding scales and a sword">
      </div>
    </div>
  </section>

  <!-- Who we are -->
  <section class="sec sec-w" id="who-we-are" aria-labelledby="who-title">
    <div class="pg-wrap">
      <div class="wh-grid">
        <div class="rv">
          <div class="sec-eyebrow">WHO WE ARE</div>
          <h2 class="sec-h2" id="who-title">About ASW Law Advocates LLP</h2>
          <p class="wh-p">We are a legal practice based in Nairobi, Kenya, specializing in offering client-centric legal solutions to our clientele, which includes individuals and corporations.</p>
        </div>
        <ul class="wh-cards rv" aria-label="Who we serve">
          <li class="wh-card"><span class="pg-ic">{ic("user",24,1.6)}</span><div><h3>Individuals</h3><p class="bd">{WHO["Individuals"]}</p></div></li>
          <li class="wh-card"><span class="pg-ic">{ic("building",24,1.6)}</span><div><h3>Corporations</h3><p class="bd">{WHO["Corporations"]}</p></div></li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Our pillars -->
  <section class="sec sec-o" aria-labelledby="pillars-title">
    <div class="pg-wrap">
      <div class="rv">
        <div class="sec-eyebrow">OUR PILLARS</div>
        <h2 class="sec-h2" id="pillars-title" style="max-width:780px">Underpinning our work ethic are 3 pillars:</h2>
      </div>
      <ul class="pl-list" aria-label="Our three pillars">
{pill}      </ul>
    </div>
  </section>

  <!-- How we work -->
  <section class="sec sec-w" id="approach" aria-labelledby="hw-title">
    <div class="pg-wrap">
      <div class="rv">
        <div class="sec-eyebrow">HOW WE WORK</div>
        <h2 class="sec-h2" id="hw-title">Our Approach</h2>
      </div>
      <ol class="hw3 rv" aria-label="Our approach in four steps">
{how_list(ic,True)}      </ol>
    </div>
  </section>

  <!-- Facts strip -->
  <section class="fs" aria-label="ASW Law Advocates at a glance">
    <div class="pg-wrap">
      <ul class="fs-grid rv">
        <li class="fs-i"><span class="fs-n">6</span><span class="fs-l">Areas of Practice</span></li>
        <li class="fs-i"><span class="fs-n">3</span><span class="fs-l">Guiding Pillars</span></li>
        <li class="fs-i"><span class="fs-n">2</span><span class="fs-l">Professional Memberships</span></li>
        <li class="fs-i"><span class="fs-n fs-w">Nairobi</span><span class="fs-l">Kenya</span></li>
      </ul>
    </div>
  </section>

  <!-- Team -->
  <section class="sec sec-w" id="team" aria-labelledby="team-title">
    <div class="pg-wrap">
      <div class="rv">
        <h2 class="sec-h2" id="team-title">The Team</h2>
      </div>
      <ul class="tm-grid" id="tm-track" aria-label="The team" onScroll="{{{{onTrack}}}}">
{team}      </ul>
      <div class="tm-dots" role="group" aria-label="Choose team member">
        <sc-for list="{{{{dots}}}}" as="d" hint-placeholder-count="3">
          <button class="tm-dotb" type="button" aria-label="{{{{d.label}}}}" aria-current="{{{{d.cur}}}}" onClick="{{{{d.go}}}}"><span class="{{{{d.cls}}}}"></span></button>
        </sc-for>
      </div>
    </div>
  </section>

{foot_html(ic)}
</div>
'''
    script='''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":%d,"height":%d}}'>
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { open: false, ai: 0 };
  }
  renderVals() {
    const open = this.state.open;
    const ai = this.state.ai;
    return {
      open,
      toggle: () => this.setState({ open: !this.state.open }),
      burgerPath: open ? 'M6 6l12 12M18 6L6 18' : 'M4 7h16M4 12h16M4 17h16',
      burgerLabel: open ? 'Close menu' : 'Open menu',
      dots: [0, 1, 2].map((i) => ({
        cls: i === ai ? 'tm-dot on' : 'tm-dot',
        cur: i === ai ? 'true' : 'false',
        label: 'Show team member ' + (i + 1) + ' of 3',
        go: () => {
          const t = document.getElementById('tm-track');
          if (t && t.children[i]) t.scrollTo({ left: t.children[i].offsetLeft - t.children[0].offsetLeft, behavior: 'smooth' });
        }
      })),
      onTrack: (e) => {
        const t = e.currentTarget || e.target;
        if (!t || !t.children || t.children.length < 2) return;
        const step = t.children[1].offsetLeft - t.children[0].offsetLeft;
        const i = Math.max(0, Math.min(2, Math.round(t.scrollLeft / step)));
        if (i !== this.state.ai) this.setState({ ai: i });
      }
    };
  }
}
</script>''' % (w,h)
    html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Marcellus&display=swap" rel="stylesheet">
<style>
{BASE_CSS}{PAGE_CSS}{FOOT_CSS}{HW_CSS}</style>
</helmet>
{body}</x-dc>
{script}
</body>
</html>
'''
    html=html.replace('{{{{','{{').replace('}}}}','}}')
    open('/home/claude/hero/project/%s.dc.html'%name,'w',encoding='utf-8').write(html)
build('About','About Us: ASW Law Advocates LLP',1440,5009)
build('AboutTablet','About Us: Tablet 768',768,6118)
build('AboutPhone','About Us: Phone 390',390,3999)
print('ok')
