ABOUT_CSS = r"""
/* about section */
.ab{position:relative;overflow:hidden;contain:paint;background:#ffffff;padding:96px 0}
.ab-arc{position:absolute;right:-140px;bottom:-170px;width:600px;height:680px;border-radius:300px 300px 0 0;background:rgba(148,187,228,.10);pointer-events:none}
.ab-wrap{position:relative;z-index:1;max-width:1280px;margin:0 auto;padding:0 40px}
.ab-top{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:48px 96px;align-items:start}
.ab-eyebrow{display:flex;align-items:center;gap:14px;font-size:13px;line-height:16px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#0F74B5}
.ab-eyebrow::before{content:"";width:36px;height:2px;background:#0F74B5}
.ab-h2{margin:20px 0 0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:44px;line-height:1.12;letter-spacing:-.01em;color:#0E1F3D;text-wrap:balance;max-width:520px}
.ab-bar{display:block;width:64px;height:4px;margin-top:26px;border-radius:4px;background:#94BBE4}
.ab-r{padding-top:4px}
.ab-p{margin:0;font-size:20px;line-height:1.65;color:#33445F;max-width:560px}
.ab .ab-link{display:inline-flex;align-items:center;gap:10px;min-height:44px;margin-top:20px;font-size:16px;font-weight:600;color:#0F74B5;border-bottom:2px solid transparent}
.ab-link svg{transition:transform .2s ease}
.ab .ab-link:hover{border-bottom-color:#0F74B5}
.ab-link:hover svg{transform:translateX(4px)}
.ab-lead{display:flex;align-items:center;gap:24px;margin:48px 0 0;font-size:20px;line-height:28px;font-weight:600;color:#0E1F3D}
.ab-lead::after{content:"";flex:1;height:1px;background:rgba(14,31,61,.12)}
.ab-root-ul{margin:0}
.ab .ab-cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin-top:28px}
.ab-card{display:grid;grid-template-columns:minmax(0,1fr) auto;grid-template-rows:auto 1fr;grid-template-areas:"num ic" "name name";align-items:start;min-height:182px;padding:26px 28px 28px;background:#ffffff;border:1px solid #E6ECF4;border-top:3px solid #94BBE4;border-radius:18px;box-shadow:0 14px 40px rgba(14,31,61,.07);transition:transform .25s ease,box-shadow .25s ease}
.ab-card:hover{transform:translateY(-6px);box-shadow:0 26px 56px rgba(14,31,61,.14)}
.ab-num{grid-area:num;font-family:'DM Sans',system-ui,sans-serif;font-weight:500;font-variant-numeric:lining-nums;font-feature-settings:'lnum' 1;font-size:48px;line-height:1;letter-spacing:-.02em;color:#0F74B5}
.ab-z{display:inline-block;transform:scaleX(.74);transform-origin:0 50%;margin-right:-.17em}
.ab-ic{grid-area:ic;display:inline-flex;align-items:center;justify-content:center;width:64px;height:64px;border-radius:50%;background:#ffffff;border:1px solid #C9DBF0;color:#1B4584;transition:background .25s ease,color .25s ease,border-color .25s ease}
.ab-card:hover .ab-ic{background:#1B4584;border-color:#1B4584;color:#ffffff}
.ab-name{grid-area:name;align-self:end;margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:28px;line-height:1.15;color:#0E1F3D}
@media (prefers-reduced-motion:reduce){.ab-card,.ab-ic,.ab-link svg{transition:none}.ab-card:hover{transform:none}.ab-link:hover svg{transform:none}}
@media (max-width:1023px){
  .ab{padding:80px 0;border-top:1px solid #E3E6EC}
  .ab-wrap{padding:0 32px}
  .ab-top{grid-template-columns:minmax(0,1fr);gap:36px}
  .ab-h2{font-size:40px;max-width:none}
  .ab-p{font-size:19px;max-width:620px}
  .ab-lead{margin-top:36px}
  .ab .ab-cards{gap:16px}
  .ab-card{min-height:154px;padding:20px 20px 22px;border-radius:16px}
  .ab-num{font-size:40px}
  .ab-ic{width:52px;height:52px}
  .ab-ic svg{width:26px;height:26px}
  .ab-name{font-size:26px}
  .ab-arc{width:420px;height:480px;border-radius:210px 210px 0 0;right:-120px;bottom:-130px}
  }
@media (max-width:640px){
  .ab-eyebrow{font-size:14px}
  .ab{padding:64px 0}
  .ab-wrap{padding:0 20px}
  .ab-top{gap:28px}
  .ab-h2{font-size:32px;margin-top:18px}
  .ab-bar{margin-top:22px}
  .ab-p{font-size:17px;line-height:1.65}
  .ab-link{margin-top:14px}
  .ab-lead{margin-top:28px;font-size:17px;line-height:24px;gap:16px}
  .ab .ab-cards{grid-template-columns:minmax(0,1fr);gap:20px;margin-top:22px}
  .ab-card{grid-template-columns:56px minmax(0,1fr);grid-template-rows:auto auto;grid-template-areas:"ic num" "ic name";column-gap:20px;align-items:center;min-height:0;padding:16px 20px 16px 16px;border-radius:16px}
  .ab-ic{width:56px;height:56px;align-self:center}
  .ab-num{font-size:28px;align-self:end}
  .ab-name{font-size:26px;align-self:start;margin-top:4px}
  .ab-arc{width:320px;height:380px;border-radius:160px 160px 0 0;right:-110px;bottom:-110px}
  }
"""

def about_html(ic):
    cards=""
    for n,(t,k) in enumerate((("Competence","checks"),("Integrity","shield"),("Pragmatism","scale")),1):
        cards+='        <li class="ab-card"><span class="ab-num" aria-hidden="true"><span class="ab-z">0</span>%d</span><span class="ab-ic">%s</span><h3 class="ab-name">%s</h3></li>\n'%(n,ic(k,30,1.6),t)
    return '''  <!-- About -->
  <section class="ab" aria-labelledby="about-title">
    <div class="ab-arc" aria-hidden="true"></div>
    <div class="ab-wrap">
      <div class="ab-top">
        <div class="ab-l">
          <div class="ab-eyebrow">ABOUT US</div>
          <h2 class="ab-h2" id="about-title">About ASW Law Advocates LLP</h2>
        </div>
        <div class="ab-r">
          <p class="ab-p">We are a legal practice based in Nairobi, Kenya, specializing in offering client-centric legal solutions to our clientele, which includes individuals and corporations.</p>
          <a class="ab-link" href="About.dc.html"><span>Learn More about us</span>%s</a>
        </div>
      </div>
      <p class="ab-lead">Underpinning our work ethic are 3 pillars:</p>
      <ul class="ab-cards" aria-label="Our three pillars">
%s      </ul>
    </div>
  </section>
''' % (ic("arrow",20,2),cards)


AREA_LIST=[("Dispute Resolution","2f9ce9737e758419c7843a6b52aeeb80"),("Commercial and Corporate","bc21d296171ed55434e696b22d269465"),("Public Procurement and Tax","a50705e4f7f7690f9aeea13a447e23ad"),("Property &amp; Real Estate","42f37620f2e5d87828aa00609d8ec8be"),("Private Client","ae893e31afab0a7bd15accf76ca31d4e"),("Employment and Pensions","3b59ac2f7aa43ff1616140725066af49")]

AREAS_CSS = r"""
/* areas of practice section */
.ar{background:#F2F2F0;padding:96px 0}
.ar-wrap{max-width:1280px;margin:0 auto;padding:0 40px}
.ar-head{display:flex;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;gap:20px 32px}
.ar-h2{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:44px;line-height:1.12;letter-spacing:-.01em;color:#0E1F3D}
.ar-bar{display:block;width:64px;height:4px;margin-top:26px;border-radius:4px;background:#94BBE4}
.ar .ar-all{display:inline-flex;align-items:center;gap:10px;min-height:44px;font-size:16px;font-weight:600;color:#0B66A0;border-bottom:2px solid transparent}
.ar .ar-all svg{transition:transform .2s ease}
.ar .ar-all:hover{border-bottom-color:#0B66A0}
.ar .ar-all:hover svg{transform:translateX(4px)}
.ar .ar-all-bot,.ar .ar-dots{display:none}
.ar .ar-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin-top:48px}
.ar .ar-card{position:relative;display:flex;flex-direction:column;border-radius:20px;overflow:hidden;isolation:isolate;color:#ffffff;background:#0E1F3D;box-shadow:0 10px 30px rgba(14,31,61,.10)}
.ar-media{position:relative;display:block;aspect-ratio:3/2;overflow:hidden;background:#0E1F3D}
.ar .ar-card:focus-visible{border-radius:20px}
.ar-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;display:block;transition:transform .6s cubic-bezier(.2,.7,.2,1)}
.ar .ar-card:hover .ar-img,.ar .ar-card:focus-visible .ar-img{transform:scale(1.04)}
.ar-num{position:absolute;top:16px;left:16px;z-index:2;padding:5px 12px;border-radius:999px;background:#ffffff;color:#0E1F3D;font-size:12px;line-height:16px;font-weight:600;letter-spacing:.06em;font-variant-numeric:lining-nums}
.ar .ar-grid>li{display:flex;min-width:0}
.ar .ar-card{flex:1;min-width:0}
.ar-foot{flex:1;display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:128px;min-width:0;padding:16px 22px 16px 24px;background:#0E1F3D;transition:background .25s ease}
.ar .ar-card:hover .ar-foot,.ar .ar-card:focus-visible .ar-foot{background:#1B4584}
.ar-name{font-family:'Marcellus',Georgia,serif;font-size:22px;line-height:1.2;color:#ffffff}
.ar-go{display:inline-flex;align-items:center;justify-content:center;flex:none;width:44px;height:44px;border-radius:50%;background:#ffffff;color:#0E1F3D;transition:background .25s ease,transform .25s ease}
.ar .ar-card:hover .ar-go,.ar .ar-card:focus-visible .ar-go{background:#94BBE4}
@media (prefers-reduced-motion:reduce){.ar-img,.ar-go,.ar-foot,.ar .ar-all svg{transition:none}.ar .ar-card:hover .ar-img{transform:none}}
@media (max-width:1023px){
  .ar{padding:80px 0}
  .ar-wrap{padding:0 32px}
  .ar-h2{font-size:40px}
  .ar .ar-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:36px}
}
@media (max-width:640px){
  .ar-num{font-size:14px;line-height:18px}
  .ar{padding:64px 0}
  .ar-wrap{padding:0 20px}
  .ar-h2{font-size:32px}
  .ar-bar{margin-top:22px}
  .ar .ar-all-top{display:none}
  .ar .ar-grid{display:flex;gap:14px;margin:28px -20px 0;padding:4px 20px 8px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:20px;scrollbar-width:none;-webkit-overflow-scrolling:touch}
  .ar .ar-grid::-webkit-scrollbar{display:none}
  .ar .ar-grid>li{flex:0 0 calc((100% + 40px) * .85);scroll-snap-align:start}
  .ar .ar-dots{display:flex;justify-content:center;margin-top:10px}
  .ar-dotb{display:inline-flex;align-items:center;justify-content:center;width:32px;height:44px;padding:0;border:0;background:transparent;cursor:pointer}
  .ar-dotb:focus-visible{outline:3px solid #0F74B5;outline-offset:-3px;border-radius:10px}
  .ar-dot{display:block;width:8px;height:8px;border-radius:8px;background:rgba(14,31,61,.25);transition:width .25s ease,background .25s ease}
  .ar-dot.on{width:24px;background:#1B4584}
  .ar .ar-all-bot{display:flex;justify-content:center;margin-top:4px}
}
"""

AREA_ITEMS=[("Civil and commercial litigation","Negotiation, mediation and settlement"),
("Company registration, changes and dissolution","Drafting, reviewing and negotiating commercial agreements"),
("Offer general advisory services in respect of tax and procurement matters","Represent Clients in procurement related disputes"),
("Draft, review, and negotiate Leases, Sales, Charge, Discharge and other property-related Agreements","Conduct due diligence in respect of property transactions"),
("Estate Planning","Succession"),
("Draft, review and negotiate employment and pension and other employment-related agreements","Represent clients in employment-related disputes")]
def areas_html(ic):
    cards=""
    for n,(t,b) in enumerate(AREA_LIST,1):
        it=''.join('<span class="ar-li">%s</span>'%x for x in AREA_ITEMS[n-1])
        cards+='        <li><a class="ar-card" href="Areas.dc.html"><span class="ar-media"><img class="ar-img" src="/_blob/%s" alt=""><span class="ar-num" aria-hidden="true">0%d</span></span><span class="ar-foot"><span class="ar-txt"><span class="ar-name">%s</span>%s</span><span class="ar-go" aria-hidden="true">%s</span></span></a></li>\n'%(b,n,t,it,ic("arrow",20,2))
    link=ic("arrow",20,2)
    return '''  <!-- Areas of Practice -->
  <section class="ar" aria-labelledby="areas-title">
    <div class="ar-wrap">
      <div class="ar-head">
        <div>
          <h2 class="ar-h2" id="areas-title">Areas of Practice</h2>
        </div>
        <a class="ar-all ar-all-top" href="Areas.dc.html"><span>View all areas of practice</span>%s</a>
      </div>
      <ul class="ar-grid" id="ar-track" aria-label="Areas of practice" onScroll="{{onTrack}}">
%s      </ul>
      <div class="ar-dots" role="group" aria-label="Choose area">
        <sc-for list="{{dots}}" as="d" hint-placeholder-count="6">
          <button class="ar-dotb" type="button" aria-label="{{d.label}}" aria-current="{{d.cur}}" onClick="{{d.go}}"><span class="{{d.cls}}"></span></button>
        </sc-for>
      </div>
      <a class="ar-all ar-all-bot" href="Areas.dc.html"><span>View all areas of practice</span>%s</a>
    </div>
  </section>
''' % (link,cards,link)

BLOG_POSTS=[("08993c385854a23fc1db4562a381fd00","Flexibility of marriage in US"),("5b4b94f7270eb91f66f1193f7dc7a478","Know about Industrial Laws")]
BLOG_EXCERPT="Performance marketing may involve using various types of digital marketing and advertising channels, including the [&hellip;]"

BLOG_CSS = r"""
/* recent blog posts */
.bl{background:#ffffff;padding:96px 0}
.bl-wrap{max-width:1280px;margin:0 auto;padding:0 40px}
.bl-head{display:flex;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;gap:20px 32px}
.bl-h2{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:44px;line-height:1.12;letter-spacing:-.01em;color:#0E1F3D}
.bl-bar{display:block;width:64px;height:4px;margin-top:26px;border-radius:4px;background:#94BBE4}
.bl .bl-all{display:inline-flex;align-items:center;gap:10px;min-height:44px;font-size:16px;font-weight:600;color:#0B66A0;border-bottom:2px solid transparent}
.bl .bl-all-bot{display:none}
.bl .bl-all svg,.bl .bl-more svg{transition:transform .2s ease}
.bl .bl-all:hover{border-bottom-color:#0B66A0}
.bl .bl-all:hover svg{transform:translateX(4px)}
.bl .bl-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px;margin-top:48px}
.bl .bl-card{display:flex;align-items:center;gap:24px;height:100%;padding:18px 24px 18px 18px;background:#ffffff;border:1px solid #E6ECF4;border-radius:20px;box-shadow:0 14px 40px rgba(14,31,61,.07);transition:transform .25s ease,box-shadow .25s ease}
.bl .bl-card:hover,.bl .bl-card:focus-visible{transform:translateY(-4px);box-shadow:0 24px 52px rgba(14,31,61,.13)}
.bl .bl-card:focus-visible{border-radius:20px}
.bl-img{flex:none;width:200px;aspect-ratio:261/286;border-radius:20px;object-fit:cover;object-position:center;display:block;background:#F2F2F0}
.bl-body{min-width:0;display:flex;flex-direction:column;align-items:flex-start}
.bl-date{display:inline-flex;align-items:center;gap:8px;font-size:14px;line-height:20px;font-weight:600;color:#0F74B5}
.bl-date svg{flex:none}
.bl-title{margin:10px 0 0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:24px;line-height:1.25;color:#0E1F3D;transition:color .2s ease}
.bl .bl-card:hover .bl-title,.bl .bl-card:focus-visible .bl-title{color:#0F74B5}
.bl-ex{margin:10px 0 0;font-size:15px;line-height:1.6;color:#33445F;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.bl-more{display:inline-flex;align-items:center;gap:8px;min-height:44px;margin-top:4px;font-size:16px;font-weight:600;color:#0B66A0}
.bl .bl-card:hover .bl-more svg{transform:translateX(4px)}
@media (prefers-reduced-motion:reduce){.bl .bl-card,.bl-title,.bl .bl-all svg,.bl .bl-more svg{transition:none}.bl .bl-card:hover{transform:none}}
@media (max-width:1023px){
  .bl{padding:80px 0}
  .bl-wrap{padding:0 32px}
  .bl-h2{font-size:40px}
  .bl .bl-grid{grid-template-columns:minmax(0,1fr);gap:20px;margin-top:36px}
  .bl .bl-card{padding:20px 28px 20px 20px;gap:28px}
  .bl-ex{font-size:16px}
}
@media (max-width:640px){
  .bl{padding:64px 0}
  .bl-wrap{padding:0 20px}
  .bl-h2{font-size:32px}
  .bl-bar{margin-top:22px}
  .bl .bl-all-top{display:none}
  .bl .bl-all-bot{display:flex;justify-content:center;margin-top:12px}
  .bl .bl-grid{gap:16px;margin-top:28px}
  .bl .bl-card{align-items:flex-start;gap:14px;padding:12px 16px 4px 12px;border-radius:18px}
  .bl-img{width:96px;height:96px;aspect-ratio:1/1;border-radius:14px;margin-bottom:8px}
  .bl-ex{display:none}
  .bl-date{font-size:16px}
  .bl-title{margin-top:6px;font-size:20px;line-height:1.25;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
  .bl-more{margin-top:2px}
}
"""

def blog_html(ic):
    cards=""
    for b,t in BLOG_POSTS:
        cards+='        <li><a class="bl-card" href="Insights.dc.html"><img class="bl-img" src="/_blob/%s" alt=""><span class="bl-body"><span class="bl-date">%s<span>June 24, 2025</span></span><h3 class="bl-title">%s</h3><p class="bl-ex">%s</p><span class="bl-more"><span>Read More</span>%s</span></span></a></li>\n'%(b,ic("calendar",16,1.8),t,BLOG_EXCERPT,ic("arrow",18,2))
    return '''  <!-- Recent Blog Posts -->
  <section class="bl" aria-labelledby="blog-title">
    <div class="bl-wrap">
      <div class="bl-head">
        <div>
          <h2 class="bl-h2" id="blog-title">Recent Blog Posts</h2>
        </div>
        <a class="bl-all bl-all-top" href="Insights.dc.html"><span>All Blog Posts</span>%s</a>
      </div>
      <ul class="bl-grid" aria-label="Recent blog posts">
%s      </ul>
      <a class="bl-all bl-all-bot" href="Insights.dc.html"><span>All Blog Posts</span>%s</a>
    </div>
  </section>
''' % (ic("arrow",20,2),cards,ic("arrow",20,2))

LOGO_LIGHT="/_blob/34f125cf125583676cd7f972966a287a"
FOOT_AREAS=["Dispute Resolution","Commercial and Corporate","Public Procurement and Tax","Property &amp; Real Estate","Private Client","Employment and Pensions"]

FOOT_CSS = r"""
.ft-slim-brand{display:flex;flex-direction:column;align-items:center;text-align:center;padding:48px 0 36px}
.ft-slim-brand .ft-logo{height:88px}
/* footer / let's talk */
.ft{position:relative;overflow:hidden;contain:paint;color:#ffffff;background:linear-gradient(160deg,#0E1F3D 0%,#122B55 55%,#1B4584 135%)}
.ft-top{position:relative;overflow:hidden}
.ft-arc{position:absolute;right:-170px;top:-250px;width:500px;height:500px;border:1.5px solid rgba(148,187,228,.12);border-radius:50%;pointer-events:none}
.ft-wrap{position:relative;z-index:1;max-width:1280px;margin:0 auto;padding:0 40px}
.ft-cta{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:28px 40px;padding:96px 0 64px}
.ft-talk{display:flex;align-items:center;gap:24px}
.ft-h2{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-.01em;color:#ffffff}
.ft .ft-go{display:inline-flex;align-items:center;justify-content:center;flex:none;width:64px;height:64px;border-radius:50%;background:#ffffff;color:#0E1F3D;transition:background .25s ease,transform .25s ease}
.ft .ft-go:hover{background:#94BBE4;transform:translateX(4px)}
.ft .ft-book{display:inline-flex;align-items:center;justify-content:center;min-height:56px;padding:0 34px;border-radius:999px;background:#94BBE4;color:#0E1F3D;font-size:16px;font-weight:700;transition:background .2s ease}
.ft .ft-book:hover{background:#ffffff}
.ft-rule{height:1px;background:rgba(255,255,255,.14)}
.ft-r2,.ft-menu{display:none}
.ft-cols{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr) minmax(0,1fr);grid-template-areas:"contact logo areas";gap:56px;padding:64px 0}
.ft-contact{grid-area:contact}
.ft-brand{grid-area:logo;display:flex;flex-direction:column;align-items:center;text-align:center}
.ft-areas{grid-area:areas}
.ft .ft-list{display:flex;flex-direction:column;gap:18px}
.ft-item{display:flex;align-items:flex-start;gap:16px}
.ft-ic{display:inline-flex;align-items:center;justify-content:center;flex:none;width:44px;height:44px;border-radius:50%;border:1px solid rgba(148,187,228,.40);color:#94BBE4}
.ft-lab{display:block;font-size:13px;line-height:16px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#C9DBF0}
.ft-val{display:block;margin-top:4px;font-size:16px;line-height:1.5;color:#ffffff}
.ft .ft-txt{padding-top:2px}
.ft a.ft-val{display:inline-flex;align-items:center;min-height:44px;margin-top:-6px;border-bottom:1px solid transparent}
.ft a.ft-val:hover{color:#94BBE4}
.ft-logo{display:block;height:104px;width:auto}
.ft-tag{margin:18px 0 0;max-width:250px;font-size:16px;line-height:1.6;color:#C9DBF0}
.ft-ah{margin:0 0 14px;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:24px;line-height:30px;color:#94BBE4}
.ft .ft-links{display:flex;flex-direction:column;gap:0}
.ft .ft-links a{display:inline-flex;align-items:center;min-height:44px;font-size:16px;color:#ffffff;border-bottom:1px solid transparent}
.ft .ft-links a:hover{color:#94BBE4}
.ft-sub{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:4px 32px;padding:10px 0}
.h-root .ft-nl,.h-root .ft-legal{display:flex;flex-wrap:wrap;gap:0 28px;margin:0;padding:0;list-style:none}
.ft .ft-nl a,.ft .ft-legal a{display:inline-flex;align-items:center;min-height:44px;font-size:14px;line-height:20px;color:#ffffff}
.ft .ft-legal a{color:#C9DBF0}
.ft .ft-nl a:hover,.ft .ft-legal a:hover{color:#94BBE4}
.ft-copy{padding:24px 0 30px;text-align:center;font-size:14px;line-height:22px;color:#C9DBF0}
@media (prefers-reduced-motion:reduce){.ft .ft-go,.ft .ft-book{transition:none}.ft .ft-go:hover{transform:none}}
@media (max-width:1023px){
  .ft-wrap{padding:0 32px}
  .ft-cta{flex-direction:column;justify-content:center;text-align:center;padding:80px 0 52px;gap:30px}
  .ft-arc{width:420px;height:420px;right:-150px;top:-210px}
  .ft-h2{font-size:56px}
  .ft-cols{grid-template-columns:minmax(0,1fr) minmax(0,1fr);grid-template-areas:"logo logo" "contact areas";gap:48px 40px;padding:52px 0}
    }
@media (max-width:640px){
  .ft-lab{font-size:14px}
  .ft-wrap{padding:0 20px}
  .ft-cta{align-items:stretch;text-align:left;padding:64px 0 40px;gap:24px}
  .ft-arc{width:320px;height:320px;right:-130px;top:-150px}
  .ft-talk{justify-content:space-between}
  .ft-h2{font-size:44px}
  .ft .ft-go{width:56px;height:56px}
  .ft .ft-book{width:100%;min-height:56px}
  .ft-cols{grid-template-columns:minmax(0,1fr);grid-template-areas:"contact" "logo" "areas";gap:40px;padding:40px 0}
  .ft-brand{align-items:flex-start;text-align:left}
  .ft-tag{max-width:none}
  .ft-sub{flex-direction:column;align-items:flex-start;padding:12px 0}
  .h-root .ft-nl{gap:0 24px}
  .ft .ft-nl a,.ft .ft-legal a{font-size:16px}
  .ft-slim-brand{align-items:flex-start;text-align:left;padding:40px 0 28px}
  .ft-copy{text-align:left;font-size:16px;line-height:24px;padding:22px 76px 72px 0}
    }
"""

TOPHTML='''    <div class="ft-top">
      <div class="ft-arc" aria-hidden="true"></div>
      <div class="ft-wrap">
      <div class="ft-cta">
        <div class="ft-talk">
          <h2 class="ft-h2">Let&rsquo;s Talk</h2>
          <a class="ft-go" href="Contact.dc.html" aria-label="Contact Us">%(arrow)s</a>
        </div>
        <a class="ft-book" href="Book.dc.html">Book Appointment</a>
      </div>
      </div>
    </div>
'''
NAV=''.join('          <li><a href="%s">%s</a></li>\n'%(h,l) for h,l in (("Main.dc.html","Home"),("About.dc.html","About Us"),("Areas.dc.html","Areas Of Practice"),("Insights.dc.html","Insights"),("Book.dc.html","Book Appointment"),("Contact.dc.html","Contact Us")))
def foot_html(ic,cta=True,slim=False):
    if slim: return slim_foot(ic)
    rows=''.join('          <li><a href="Areas.dc.html">%s</a></li>\n'%a for a in FOOT_AREAS)
    return '''  <!-- Let's Talk + footer -->
  <footer class="ft ft-full%(nocta)s" aria-label="Contact and footer">
%(top)s    <div class="ft-wrap">
      %(rule)s
      <div class="ft-cols">
        <div class="ft-contact">
          <ul class="ft-list">
            <li class="ft-item"><span class="ft-ic">%(phone)s</span><div class="ft-txt"><span class="ft-lab">Phone</span><a class="ft-val" href="tel:+254788685911">+254 788 685 911</a></div></li>
            <li class="ft-item"><span class="ft-ic">%(pin)s</span><div class="ft-txt"><span class="ft-lab">Address</span><span class="ft-val">Tourism Fund Building, Mezzanine Floor, Office M08, Off-Bishop Rd, Community Area, Nairobi, Kenya</span></div></li>
            <li class="ft-item"><span class="ft-ic">%(mail)s</span><div class="ft-txt"><span class="ft-lab">Email</span><a class="ft-val" href="mailto:info@aswlaw.africa">info@aswlaw.africa</a></div></li>
            <li class="ft-item"><span class="ft-ic">%(clock)s</span><div class="ft-txt"><span class="ft-lab">Hours</span><span class="ft-val">Mon to Fri: 9.00am to 5.00pm</span></div></li>
          </ul>
        </div>
        <div class="ft-rule ft-r2" aria-hidden="true"></div>
        <div class="ft-brand">
          <a href="Main.dc.html" aria-label="ASW Law Advocates LLP, home"><img class="ft-logo" src="%(logo)s" alt="ASW Law Advocates LLP"></a>
          <p class="ft-tag">We offer world-class legal representation.</p>
        </div>
        <nav class="ft-areas" aria-label="Areas of practice">
          <h2 class="ft-ah">Areas of Practice</h2>
          <ul class="ft-links">
%(rows)s          </ul>
        </nav>
        <nav class="ft-menu" aria-label="Menu">
          <h2 class="ft-ah">Menu</h2>
          <ul class="ft-links">
%(nav)s          </ul>
        </nav>
      </div>
      <div class="ft-rule"></div>
      <div class="ft-sub">
        <nav aria-label="Site pages"><ul class="ft-nl">
%(nav)s        </ul></nav>
        <ul class="ft-legal">
          <li><a href="FAQ.dc.html">Frequently Asked Questions</a></li>
          <li><a href="Privacy.dc.html">Privacy Policy</a></li>
          <li><a href="Terms.dc.html">Terms of Use</a></li>
        </ul>
      </div>
      <div class="ft-rule"></div>
      <p class="ft-copy">&copy; Copyright 2026 ASW Law Advocates LLP. All Rights Reserved.</p>
    </div>
  </footer>
''' % dict(nocta='' if cta else ' ft-nocta',top=(TOPHTML%dict(arrow=ic("arrow",28,2))) if cta else '',rule='<div class="ft-rule"></div>' if cta else '',nav=NAV,arrow=ic("arrow",28,2),phone=ic("phone",20,1.7),pin=ic("pin",20,1.7),mail=ic("mail",20,1.7),clock=ic("clock",20,1.7),logo=LOGO_LIGHT,rows=rows)


SLIM_CSS = r"""
.ft-slim-brand{display:flex;flex-direction:column;align-items:center;text-align:center;padding:48px 0 36px}
.ft-slim-brand .ft-logo{height:88px}
@media (max-width:640px){.ft-slim-brand{align-items:flex-start;text-align:left;padding:40px 0 28px}}
"""
def slim_foot(ic):
    return '''  <!-- Slim footer -->
  <footer class="ft" aria-label="Footer">
    <div class="ft-wrap">
      <div class="ft-slim-brand">
        <a href="Main.dc.html" aria-label="ASW Law Advocates LLP, home"><img class="ft-logo" src="%s" alt="ASW Law Advocates LLP"></a>
        <p class="ft-tag">We offer world-class legal representation.</p>
      </div>
      <div class="ft-rule"></div>
      <div class="ft-sub">
        <nav aria-label="Site pages"><ul class="ft-nl">
%s        </ul></nav>
        <ul class="ft-legal">
          <li><a href="FAQ.dc.html">Frequently Asked Questions</a></li>
          <li><a href="Privacy.dc.html">Privacy Policy</a></li>
          <li><a href="Terms.dc.html">Terms of Use</a></li>
        </ul>
      </div>
      <div class="ft-rule"></div>
      <p class="ft-copy">&copy; Copyright 2026 ASW Law Advocates LLP. All Rights Reserved.</p>
    </div>
  </footer>
''' % (LOGO_LIGHT,NAV)
