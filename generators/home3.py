import sys
sys.path.insert(0,'/home/claude/hero')
from faqdata import *
PORT='/_blob/6a71c35ed220aaa8ba6455a78de01d88'
AREA_IDS=[("dispute","Dispute Resolution","2f9ce9737e758419c7843a6b52aeeb80"),("commercial","Commercial and Corporate","bc21d296171ed55434e696b22d269465"),("procurement","Public Procurement and Tax","a50705e4f7f7690f9aeea13a447e23ad"),("property","Property &amp; Real Estate","42f37620f2e5d87828aa00609d8ec8be"),("private","Private Client","ae893e31afab0a7bd15accf76ca31d4e"),("employment","Employment and Pensions","3b59ac2f7aa43ff1616140725066af49")]
PV_CSS = r"""
/* ===== preview pattern (home) ===== */
@keyframes nv-rise{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
@supports (animation-timeline:view()){@media (prefers-reduced-motion:no-preference){.nv{animation:nv-rise linear both;animation-timeline:view();animation-range:entry 0% entry 55%}}}
.pv{padding:80px 0}
.pv-w{background:#ffffff}.pv-o{background:#F2F2F0}
.pv-wrap{max-width:1280px;margin:0 auto;padding:0 40px}
.pv-head{display:flex;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;gap:16px 32px}
.pv-eyebrow{display:flex;align-items:center;gap:14px;font-size:13px;line-height:16px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#0B66A0}
.pv-eyebrow::before{content:"";width:36px;height:2px;background:#0B66A0}
.pv-eyebrow + .pv-h2{margin-top:18px}
.pv-h2{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:40px;line-height:1.12;letter-spacing:-.01em;color:#0E1F3D}
.pv-bar{display:block;width:56px;height:4px;margin-top:22px;border-radius:4px;background:#94BBE4}
.h-root a.pv-link{display:inline-flex;align-items:center;gap:10px;min-height:44px;font-size:16px;font-weight:600;color:#0B66A0;border-bottom:2px solid transparent}
.pv-link svg{flex:none;transition:transform .2s ease}
.h-root a.pv-link:hover{border-bottom-color:#0B66A0}
.pv-link:hover svg{transform:translateX(4px)}
.h-root a.pv-bot{display:none}
.pv.at-ph{display:none}
.h-pm{display:none}
.h-root a.ta-c{color:#0E1F3D}.h-root a.at-t{color:#ffffff}
.h-root .pv a:focus-visible{outline:3px solid #0F74B5;outline-offset:3px;border-radius:8px}
/* trust bar */
.tb2{background:#ffffff;border-bottom:1px solid #E6ECF4}
.tb2-in{max-width:1280px;margin:0 auto;padding:0 40px;min-height:88px;display:flex;align-items:center;gap:16px 32px;flex-wrap:wrap}
.tb2-l{font-size:12.5px;line-height:16px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#0B66A0}
.h-root .tb2-ul{display:flex;flex-wrap:wrap;gap:12px 16px;margin:0;padding:0;list-style:none}
.tb2-b{display:inline-flex;align-items:center;gap:10px;min-height:44px;padding:0 18px 0 12px;border:1px solid #D5DFEC;border-radius:999px;font-size:15px;font-weight:500;color:#0E1F3D}
.tb2-b svg{color:#1B4584;flex:none}
.tb2 .pv-link{margin-left:auto}
/* about preview */
.ap3-top{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:32px 96px;align-items:start}
.ap3-p{margin:0;font-size:19px;line-height:1.65;color:#33445F;max-width:560px}
.h-root a.ap3-lk{margin-top:6px}
.ap3-lead{display:flex;align-items:center;gap:24px;margin:40px 0 0;font-size:19px;line-height:28px;font-weight:600;color:#0E1F3D}
.ap3-lead::after{content:"";flex:1;height:1px;background:rgba(14,31,61,.12)}
.h-root .ap3-row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin:24px 0 0;padding:0;list-style:none;background:#ffffff;border:1px solid #E6ECF4;border-radius:16px;box-shadow:0 10px 30px rgba(14,31,61,.06)}
.ap3-i{display:flex;align-items:center;gap:18px;padding:22px 28px}
.ap3-i + .ap3-i{border-left:1px solid #E6ECF4}
.ap3-ic{display:inline-flex;align-items:center;justify-content:center;flex:none;width:52px;height:52px;border-radius:50%;border:1.5px solid #C9DBF0;color:#1B4584}
.ap3-n{font-family:'DM Sans',system-ui,sans-serif;font-weight:600;font-size:20px;line-height:1;font-variant-numeric:lining-nums;color:#5A97D0}
.ap3-t{font-family:'Marcellus',Georgia,serif;font-size:26px;line-height:1.15;color:#0E1F3D}
/* who we serve */
.h-root .wo-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin:36px 0 0;padding:0;list-style:none}
.wo-c{position:relative;overflow:hidden;isolation:isolate;display:flex;align-items:center;gap:20px;min-height:112px;box-sizing:border-box;padding:20px 22px 20px 24px;border-radius:18px;transition:transform .25s ease,box-shadow .25s ease}
.wo-c:hover{transform:translateY(-3px)}
.h-root a.wo-w{color:#0E1F3D}.h-root a.wo-n{color:#ffffff}
.wo-w{background:#ffffff;border:1px solid #E1E8F2;color:#0E1F3D;box-shadow:0 10px 30px rgba(14,31,61,.07)}
.wo-n{background:#0E1F3D;color:#ffffff;box-shadow:0 14px 36px rgba(14,31,61,.22)}
.wo-n::before{content:"";position:absolute;inset:0;z-index:-1;background:repeating-linear-gradient(90deg,rgba(255,255,255,.05) 0,rgba(255,255,255,.05) 1px,transparent 1px,transparent 84px);background-position:42px 0}
.wo-ic{display:inline-flex;align-items:center;justify-content:center;flex:none;width:56px;height:56px;border-radius:50%;border:1.5px solid #C9DBF0;color:#1B4584}
.wo-n .wo-ic{border-color:rgba(148,187,228,.5);color:#ffffff}
.wo-t{flex:1;min-width:0;font-family:'Marcellus',Georgia,serif;font-size:32px;line-height:1.15}
.wo-go{display:inline-flex;align-items:center;justify-content:center;flex:none;width:48px;height:48px;border-radius:50%;background:#0E1F3D;color:#ffffff;transition:background .2s ease}
.wo-n .wo-go{background:#ffffff;color:#0E1F3D}
.wo-w:hover .wo-go{background:#1B4584}
.wo-n:hover .wo-go{background:#94BBE4}
/* areas tiles */
.h-root .at-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin:36px 0 0;padding:0;list-style:none}
.at-grid>li{display:flex;min-width:0}
.at-t{position:relative;flex:1;min-width:0;display:flex;flex-direction:column;border-radius:16px;overflow:hidden;background:#0E1F3D;box-shadow:0 8px 24px rgba(14,31,61,.10);transition:transform .25s ease,box-shadow .25s ease}
.at-t:hover{transform:translateY(-4px);box-shadow:0 16px 36px rgba(14,31,61,.18)}
.at-m{position:relative;display:block;aspect-ratio:3/2;overflow:hidden}
.at-i{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;transition:transform .6s cubic-bezier(.2,.7,.2,1)}
.at-t:hover .at-i{transform:scale(1.04)}
.at-p{position:absolute;top:12px;left:12px;z-index:2;padding:4px 11px;border-radius:999px;background:#ffffff;color:#0E1F3D;font-size:12px;line-height:16px;font-weight:600;letter-spacing:.06em;font-variant-numeric:lining-nums}
.at-b{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:56px;padding:0 18px 0 20px;background:#0E1F3D;color:#ffffff;transition:background .25s ease}
.at-t:hover .at-b{background:#1B4584}
.at-n{font-family:'Marcellus',Georgia,serif;font-size:20px;line-height:1.2;color:#ffffff}
.at-b svg{flex:none;color:#94BBE4}
.at-go{display:inline-flex;align-items:center;flex:none}
/* how we work */
.h-root .hw3{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;margin:44px 0 0;padding:0;list-style:none}
.hw3-s{position:relative}
.hw3-s::after{content:"";position:absolute;top:27px;left:72px;right:-12px;height:1.5px;background:#94BBE4}
.hw3-s:last-child::after{display:none}
.hw3-c{position:relative;z-index:1;display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border-radius:50%;background:#ffffff;border:2px solid #94BBE4;font-size:20px;font-weight:600;font-variant-numeric:lining-nums;color:#0E1F3D}
.hw3-t{margin:18px 0 0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:26px;line-height:1.2;color:#0E1F3D}
.hw3-ph{margin:10px 0 0;font-size:16px;line-height:1.6;color:#2A3A55}
.hw3-g,.hw3-ck{display:none}
.h-root .ta-foot{display:none}
/* team arches */
.h-root .ta-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin:44px 0 0;padding:0;list-style:none}
.ta-grid>li{display:flex;justify-content:center;min-width:0}
.ta-c{display:flex;flex-direction:column;align-items:center;text-align:center;min-height:44px}
.ta-fr{position:relative;width:240px;height:300px;margin:0 0 0 12px;transition:transform .3s ease}
.ta-fr::before{content:"";position:absolute;inset:0;transform:translate(-12px,12px);border:2px solid #94BBE4;border-radius:120px 120px 0 0;transition:border-color .3s ease}
.ta-ph{position:absolute;inset:0;overflow:hidden;border-radius:120px 120px 0 0;background:#0E1F3D}
.ta-img{width:100%;height:100%;object-fit:cover;object-position:50% 12%;display:block}
.ta-c:hover .ta-fr,.ta-c:focus-visible .ta-fr{transform:translateY(-8px)}
.ta-c:hover .ta-fr::before,.ta-c:focus-visible .ta-fr::before{border-color:#0E1F3D}
.ta-n{margin:30px 0 0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:26px;line-height:1.15;color:#0E1F3D}
.ta-r{margin:8px 0 0;font-size:16px;line-height:1.5;color:#2A3A55}
/* faq preview */
.h-root .fp-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 64px;margin:32px 0 0;padding:0;list-style:none}
.fp-i{border-top:1px solid #D5DFEC}
.fp-i:nth-child(n+2):nth-child(-n+2){}
.fp-list>li:last-child,.fp-list>li:nth-last-child(2){border-bottom:1px solid #D5DFEC}
.h-root a.fp-a{display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:72px;padding:10px 0;font-size:18px;line-height:1.4;color:#6B7C99}
.fp-q{font-style:italic;text-decoration:underline dashed;text-decoration-thickness:1px;text-underline-offset:4px;text-decoration-color:rgba(107,124,153,.7)}
.fp-pm{display:inline-flex;align-items:center;justify-content:center;flex:none;width:40px;height:40px;border-radius:50%;border:1.5px solid #C9DBF0;color:#1B4584;transition:background .2s ease,color .2s ease}
.fp-a:hover .fp-pm{background:#1B4584;border-color:#1B4584;color:#ffffff}
/* insights list */
.h-root .il{margin:32px 0 0;padding:0;list-style:none;border-top:1px solid #D5DFEC}
.il>li{border-bottom:1px solid #D5DFEC}
.h-root a.il-r{display:grid;grid-template-columns:200px minmax(0,1fr) auto;align-items:center;gap:24px;min-height:96px;padding:14px 20px;color:#0E1F3D;transition:background .2s ease}
.il-r:hover{background:#EAF2FB}
.il-d{display:inline-flex;align-items:center;gap:10px;font-size:15px;font-weight:600;color:#0F74B5}
.il-d svg{flex:none}
.il-t{font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:28px;line-height:1.2;color:#0E1F3D;transition:color .2s ease}
.il-r:hover .il-t{color:#0F74B5}
.il-go{display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:50%;border:1.5px solid #94BBE4;color:#0E1F3D;transition:background .2s ease,color .2s ease,border-color .2s ease}
.il-r:hover .il-go{background:#0E1F3D;border-color:#0E1F3D;color:#ffffff}
@media (prefers-reduced-motion:reduce){.wo-c,.at-t,.at-i,.ta-fr,.pv-link svg{transition:none}.wo-c:hover,.at-t:hover,.ta-c:hover .ta-fr{transform:none}}
@media (max-width:1023px){
  .pv{padding:64px 0}
  .pv-wrap,.tb2-in{padding-left:32px;padding-right:32px}
  .pv-h2{font-size:36px}
  .ap3-top{grid-template-columns:minmax(0,1fr);gap:20px}
  .ap3-i{padding:18px 18px;gap:12px}
  .ap3-ic{width:44px;height:44px}
  .ap3-t{font-size:22px}
  .wo-t{font-size:28px}
  .h-root .at-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .h-root .hw3{gap:16px}
  .hw3-t{font-size:22px}
  .ta-fr{width:200px;height:252px}
  .ta-fr::before,.ta-ph{border-radius:100px 100px 0 0}
  .ta-n{font-size:22px}
  .h-root .fp-list{gap:0 40px}
  .h-root a.il-r{grid-template-columns:170px minmax(0,1fr) auto;gap:16px;padding:14px 12px}
  .il-t{font-size:26px}
}
@media (max-width:640px){
  .pv{padding:56px 0}
  .pv-wrap,.tb2-in{padding-left:20px;padding-right:20px}
  .pv-h2{font-size:32px}
  .pv-bar{margin-top:20px}
  .pv-head{align-items:flex-start;flex-direction:column;gap:6px}
  .tb2-in{padding-top:20px;padding-bottom:12px;gap:12px}
  .h-root .tb2-ul{flex-direction:column;align-items:flex-start;gap:10px}
  .tb2 .pv-link{margin-left:0}
  .ap3-p{font-size:17px}
  .ap3-lead{margin-top:28px;font-size:17px;gap:16px}
  .h-root .ap3-row{grid-template-columns:minmax(0,1fr)}
  .ap3-i{padding:14px 18px}
  .ap3-i + .ap3-i{border-left:0;border-top:1px solid #E6ECF4}
  .ap3-t{font-size:24px}
  .h-root .wo-grid{grid-template-columns:minmax(0,1fr);gap:14px;margin-top:24px}
  .wo-c{min-height:96px;padding:16px 16px 16px 18px;gap:16px}
  .wo-ic{width:48px;height:48px}
  .wo-t{font-size:26px}
  .h-root .at-grid{display:flex;gap:12px;margin:24px -20px 0;padding:4px 20px 12px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:20px;scrollbar-width:none;-webkit-overflow-scrolling:touch}
  .at-grid::-webkit-scrollbar{display:none}
  .at-grid>li{flex:0 0 78%;scroll-snap-align:start}
  .h-root .hw3{grid-template-columns:minmax(0,1fr);gap:0;margin-top:28px}
  .hw3-s{display:grid;grid-template-columns:56px minmax(0,1fr);column-gap:20px;align-items:center;min-height:56px;padding-bottom:28px}
  .hw3-s:last-child{padding-bottom:0}
  .hw3-s::after{top:56px;left:27px;right:auto;width:1.5px;height:calc(100% - 56px)}
  .hw3-t{margin:0;font-size:26px}
  .hw3-ph{grid-column:2;margin-top:6px}
  .h-root .ta-grid{display:flex;gap:16px;margin:28px -20px 0;padding:4px 20px 14px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:20px;scrollbar-width:none;-webkit-overflow-scrolling:touch}
  .ta-grid::-webkit-scrollbar{display:none}
  .ta-grid>li{flex:0 0 68%;scroll-snap-align:start}
  .ta-fr{width:200px;height:252px}
  .h-root .fp-list{grid-template-columns:minmax(0,1fr);margin-top:24px}
  .fp-list>li:nth-last-child(2){border-bottom:0}
  .h-root a.fp-a{min-height:64px;font-size:17px}
  .h-root .il{margin-top:24px}
  .h-root a.il-r{grid-template-columns:minmax(0,1fr) auto;grid-template-areas:"d go" "t go";gap:4px 12px;min-height:88px;padding:14px 8px}
  .il-d{grid-area:d;font-size:14px}
  .il-t{grid-area:t;font-size:24px}
  .il-go{grid-area:go}
}
"""
def trust_html(ic):
    b=''.join('<li class="tb2-b">%s<span>%s</span></li>'%(ic("shield",18,1.7),t) for t in ("Law Society of Kenya","East Africa Law Society"))
    return '''  <!-- Trust bar -->
  <section class="tb2" aria-label="Professional memberships">
    <div class="tb2-in">
      <div class="tb2-l">Professional Memberships</div>
      <ul class="tb2-ul">%s</ul>
      <a class="pv-link" href="About.dc.html#team"><span>Meet the team</span>%s</a>
    </div>
  </section>
'''%(b,ic("arrow",18,2))
def head(eyebrow,title,tid,linktxt,href,ic,bar=True):
    ey='<div class="pv-eyebrow">%s</div>'%eyebrow if eyebrow else ''
    return '''      <div class="pv-head nv">
        <div>
          %s<h2 class="pv-h2" id="%s">%s</h2>
        </div>
        <a class="pv-link pv-top" href="%s"><span>%s</span>%s</a>
      </div>
'''%(ey,tid,title,href,linktxt,ic("arrow",18,2))
def about_html(ic):
    cards=''
    for n,(t,k) in enumerate((("Competence","checks"),("Integrity","shield"),("Pragmatism","scale")),1):
        cards+='        <li class="ap3-i"><span class="ap3-ic">%s</span><span><span class="ap3-n" aria-hidden="true">0%d</span><br><span class="ap3-t">%s</span></span></li>\n'%(ic(k,24,1.6),n,t)
    return '''  <!-- About preview -->
  <section class="pv pv-o" aria-labelledby="ap3-t">
    <div class="pv-wrap">
      <div class="ap3-top nv">
        <div>
          <div class="pv-eyebrow">ABOUT US</div>
          <h2 class="pv-h2" id="ap3-t">About ASW Law Advocates LLP</h2>
        </div>
        <div>
          <p class="ap3-p">We are a legal practice based in Nairobi, Kenya, specializing in offering client-centric legal solutions to our clientele, which includes individuals and corporations.</p>
          <a class="pv-link ap3-lk" href="About.dc.html"><span>Learn More about us</span>%s</a>
        </div>
      </div>
      <p class="ap3-lead nv">Underpinning our work ethic are 3 pillars:</p>
      <ul class="ap3-row nv" aria-label="Our three pillars">
%s      </ul>
    </div>
  </section>
'''%(ic("arrow",18,2),cards)
def who_html(ic):
    a=ic("arrow",22,2)
    return '''  <!-- Who we serve -->
  <section class="pv pv-w" aria-labelledby="wo-t">
    <div class="pv-wrap">
%s      <ul class="wo-grid nv">
        <li><a class="wo-c wo-w" href="About.dc.html#who-we-are"><span class="wo-ic">%s</span><span class="wo-t">Individuals</span><span class="wo-go" aria-hidden="true">%s</span></a></li>
        <li><a class="wo-c wo-n" href="About.dc.html#who-we-are"><span class="wo-ic">%s</span><span class="wo-t">Corporations</span><span class="wo-go" aria-hidden="true">%s</span></a></li>
      </ul>
    </div>
  </section>
'''%(head("WHO WE SERVE","Individuals and Corporations","wo-t","Learn more","About.dc.html#who-we-are",ic),ic("user",26,1.5),a,ic("building",26,1.5),a)
def areas_html(ic):
    t=''
    for n,(i,name,b) in enumerate(AREA_IDS,1):
        t+='        <li><a class="at-t" href="Areas.dc.html#%s"><span class="at-m"><img class="at-i" src="/_blob/%s" alt=""><span class="at-p" aria-hidden="true">0%d</span></span><span class="at-b"><span class="at-n">%s</span><span class="at-go">%s</span></span></a></li>\n'%(i,b,n,name,ic("arrow",20,2))
    return '''  <!-- Areas preview -->
  <section class="pv pv-o at-dk" aria-labelledby="at-h">
    <div class="pv-wrap">
%s      <ul class="at-grid nv" aria-label="Areas of practice">
%s      </ul>
    </div>
  </section>
'''%(head(None,"Areas of Practice","at-h","View all areas of practice","Areas.dc.html",ic),t)
def how_list(ic,desc=False,home=False):
    s=''
    CK='<svg class="hw3-ck" aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7"/></svg>'
    for n,t in enumerate(("Consultation","Advice","Representation","Resolution"),1):
        if home:
            c='<span class="hw3-c" aria-hidden="true"><span class="hw3-nm">%d</span>%s</span>'%(n,CK if n==4 else '')
            g='<span class="hw3-g" aria-hidden="true">0%d</span>'%n
        else:
            c='<span class="hw3-c" aria-hidden="true">%d</span>'%n; g=''
        s+='        <li class="hw3-s">%s<h3 class="hw3-t">%s</h3>%s%s</li>\n'%(c,t,g,('<p class="hw3-ph">%s</p>'%STEP[t]) if desc else '')
    return s
def how_html(ic):
    return '''  <!-- How we work -->
  <section class="pv pv-w" aria-labelledby="hw-t">
    <div class="pv-wrap">
%s      <ol class="hw3 nv" aria-label="Our approach in four steps">
%s      </ol>
    </div>
  </section>
'''%(head("HOW WE WORK","Our Approach","hw-t","Learn about our approach","About.dc.html#approach",ic),how_list(ic,False,True))
def team_html(ic):
    c=''
    for k,nm in enumerate(("Anthony Simiyu","Alphonse Odido","Roy Chidi")):
        c+='        <li class="{{tc%d}}"><a class="ta-c" href="About.dc.html#team"><span class="ta-fr"><span class="ta-ph"><img class="ta-img" src="%s" alt="Portrait of %s"></span></span><span class="ta-n">%s</span><span class="ta-r">Advocate</span></a></li>\n'%(k,PORT,nm,nm)
    return '''  <!-- Team preview -->
  <section class="pv pv-o" aria-labelledby="ta-t">
    <div class="pv-wrap">
%s      <ul class="ta-grid nv" id="tm-track" aria-label="Our advocates" onScroll="{{onTeam}}">
%s      </ul>
@@TCTL@@
    </div>
  </section>
'''%(head("THE TEAM","Meet the Advocates","ta-t","Meet the full team","About.dc.html#team",ic),c)
def faq_html(ic):
    pm='<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg>'
    r=''.join('        <li class="fp-i"><a class="fp-a" href="FAQ.dc.html"><span class="fp-q">%s</span><span class="fp-pm" aria-hidden="true">%s</span></a></li>\n'%(q,pm) for (_t,q,_a) in FAQS[:3])
    return '''  <!-- FAQ preview -->
  <section class="pv pv-w" aria-labelledby="fp-t">
    <div class="pv-wrap">
%s      <ul class="fp-list nv" aria-label="Frequently asked questions">
%s      </ul>
    </div>
  </section>
'''%(head("FAQ","Frequently Asked Questions","fp-t","View all questions","FAQ.dc.html",ic),r)
def blog_html(ic):
    r=''
    for t,h in (("Know about Industrial Laws","Article.dc.html"),("Flexibility of marriage in US","ArticleMarriage.dc.html")):
        r+='        <li><a class="il-r" href="%s"><span class="il-d">%s<span>June 24, 2025</span></span><span class="il-t">%s</span><span class="il-go" aria-hidden="true">%s</span></a></li>\n'%(h,ic("calendar",18,1.8),t,ic("arrow",20,2))
    return '''  <!-- Insights preview -->
  <section class="pv pv-o" aria-labelledby="il-h">
    <div class="pv-wrap">
%s      <ul class="il nv" aria-label="Recent blog posts">
%s      </ul>
    </div>
  </section>
'''%(head("INSIGHTS","Recent Blog Posts","il-h","All Blog Posts","Insights.dc.html",ic),r)

import re as _re
def _wrap(fn):
    def w(ic):
        t=fn(ic); m=_re.search(r'<a class="pv-link pv-top" href="([^"]+)"><span>([^<]+)</span>',t)
        if not m: return t
        k=t.rindex('    </div>\n  </section>')
        return t[:k]+'      <a class="pv-link pv-bot" href="%s"><span>%s</span>%s</a>\n'%(m.group(1),m.group(2),ic("arrow",18,2))+t[k:]
    return w
who_html=_wrap(who_html);areas_html=_wrap(areas_html);how_html=_wrap(how_html);_team_raw=team_html
def team_html(ic):
    t=_wrap(_team_raw)(ic)
    LEFT=ic('arrow',20,2).replace('d="M5 12h14"/><path d="m12 5 7 7-7 7"','d="M19 12H5"/><path d="m12 19-7-7 7-7"')
    ctl='<div class="ta-foot"><div class="at-ctl ta-ctl">\n        <div class="at-cnt">\n          <p class="at-num" aria-live="polite"><span class="at-cur">{{tcur}}</span><span class="at-tot"> / 03</span></p>\n          <span class="at-track" aria-hidden="true"><span class="{{tFill}}"></span></span>\n        </div>\n        <div class="at-btns">\n          <button class="{{tPrevCls}}" type="button" aria-label="Previous advocate" aria-disabled="{{tPrevAria}}" onClick="{{tPrev}}">%s</button>\n          <button class="{{tNextCls}}" type="button" aria-label="Next advocate" aria-disabled="{{tNextAria}}" onClick="{{tNext}}">%s</button>\n        </div></div>'%(LEFT,ic('arrow',20,2))
    t=t.replace('@@TCTL@@\n',ctl+'\n')
    k=t.rindex('    </div>\n  </section>')
    return t[:k]+'      </div>\n'+t[k:]
faq_html=_wrap(faq_html);blog_html=_wrap(blog_html)

def areas_phone_html(ic):
    t=''
    for n,(i,name,b) in enumerate(AREA_IDS,1):
        t+='        <li><a class="at-t" href="Areas.dc.html#%s"><span class="at-m"><img class="at-i" src="/_blob/%s" alt=""><span class="at-p" aria-hidden="true">0%d</span></span><span class="at-b"><span class="at-n">%s</span><span class="at-go">%s</span></span></a></li>\n'%(i,b,n,name,ic("arrow",18,2))
    return '''  <!-- Areas carousel (phone) -->
  <section class="pv pv-o at-ph" aria-labelledby="atp-h">
    <div class="pv-wrap">
      <div class="pv-head nv">
        <div>
          <h2 class="pv-h2" id="atp-h">Areas of Practice</h2>
        </div>
      </div>
      <div class="at-reg" role="region" aria-roledescription="carousel" aria-label="Areas of Practice">
        <ul class="at-grid" id="ar-track" onScroll="{{onTrack}}">
%s        </ul>
      </div>
      <div class="at-foot">
        <div class="at-ctl">
          <div class="at-cnt">
            <p class="at-num" aria-live="polite"><span class="at-cur">{{cur}}</span><span class="at-tot"> / 06</span></p>
            <span class="at-track" aria-hidden="true"><span class="{{fillCls}}"></span></span>
          </div>
          <div class="at-btns">
            <button class="{{prevCls}}" type="button" aria-label="Previous area" aria-disabled="{{prevAria}}" onClick="{{goPrev}}">%s</button>
            <button class="{{nextCls}}" type="button" aria-label="Next area" aria-disabled="{{nextAria}}" onClick="{{goNext}}">%s</button>
          </div>
        </div>
        <a class="pv-link pv-bot" href="Areas.dc.html"><span>View all areas of practice</span>%s</a>
      </div>
    </div>
  </section>
'''%(t,ic("arrow",20,2).replace('d="M5 12h14"/><path d="m12 5 7 7-7 7"','d="M19 12H5"/><path d="m12 19-7-7 7-7"'),ic("arrow",20,2),ic("arrow",18,2))
