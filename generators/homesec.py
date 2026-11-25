import re
FORMCSS=open('/home/claude/hero/gen_contact.py').read().split('FORMCSS=r"""')[1].split('"""')[0]
MAPB='/_blob/540d4e0a1684baf335b9225e8f4580e4'
PORT='/_blob/6a71c35ed220aaa8ba6455a78de01d88'
ADDR='Tourism Fund Building, Mezzanine Floor, Office M08, Off-Bishop Rd, Community Area, Nairobi, Kenya'
HOME2_CSS = FORMCSS + r"""
/* team */
.te{background:#F2F2F0;padding:96px 0}
.te-wrap,.fq-wrap,.bk-wrap,.vu-wrap{max-width:1280px;margin:0 auto;padding:0 40px}
.te-head{display:flex;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;gap:20px 32px}
.h-root a.te-all{display:inline-flex;align-items:center;gap:10px;min-height:44px;font-size:16px;font-weight:600;color:#0B66A0;border-bottom:2px solid transparent}
.te-all svg{transition:transform .2s ease}
.h-root a.te-all:hover{border-bottom-color:#0B66A0}
.te-all:hover svg{transform:translateX(4px)}
.h-root .te-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin:48px 0 0;padding:0;list-style:none}
.te-card{height:100%;box-sizing:border-box;display:flex;flex-direction:column;background:#ffffff;border:1px solid #E6ECF4;border-top:3px solid transparent;border-radius:20px;padding:20px;box-shadow:0 14px 40px rgba(14,31,61,.07);transition:transform .3s ease,box-shadow .3s ease,border-color .3s ease}
.te-card:hover{transform:translateY(-6px);border-top-color:#94BBE4;box-shadow:0 26px 56px rgba(14,31,61,.14)}
.te-ph{position:relative;aspect-ratio:4/5;border-radius:16px;overflow:hidden;background:#0E1F3D;isolation:isolate}
.te-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 10%;display:block}
.te-ph::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,31,61,0) 58%,rgba(14,31,61,.5) 100%);pointer-events:none}
.te-body{padding:24px 6px 8px}
.te-name{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:28px;line-height:1.15;color:#0E1F3D}
.te-role{margin:10px 0 0}
.ph2{font-style:italic;color:#6B7C99;text-decoration:underline dashed;text-decoration-thickness:1px;text-underline-offset:4px;text-decoration-color:rgba(107,124,153,.7)}
.te-mem{margin-top:22px;padding-top:18px;border-top:1px solid #E6ECF4}
.te-mem-h{font-size:12.5px;line-height:16px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#0B66A0}
.h-root .te-mem ul{display:flex;flex-direction:column;gap:10px;margin:14px 0 0;padding:0;list-style:none}
.te-mem li{display:flex;align-items:center;gap:10px;font-size:16px;line-height:22px;color:#0E1F3D}
.te-mem li svg{flex:none;color:#1B4584}
/* faq */
.fq{background:#ffffff;padding:96px 0}
.h-root .fq-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 64px;align-items:start;margin:48px 0 0;padding:0;list-style:none}
.fq-i{border-top:1px solid #D5DFEC}
.fq-i:nth-last-child(-n+2){border-bottom:1px solid #D5DFEC}
.fq-i summary{display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:76px;padding:12px 0;cursor:pointer;list-style:none;font-size:19px;line-height:1.4}
.fq-i summary::-webkit-details-marker{display:none}
.fq-pm{position:relative;flex:none;width:40px;height:40px;border-radius:50%;border:1.5px solid #C9DBF0;color:#1B4584;transition:background .2s ease,color .2s ease}
.fq-pm::before,.fq-pm::after{content:"";position:absolute;left:50%;top:50%;width:14px;height:1.8px;margin:-.9px 0 0 -7px;background:currentColor;border-radius:2px;transition:transform .25s ease}
.fq-pm::after{transform:rotate(90deg)}
.fq-i[open] .fq-pm{background:#1B4584;border-color:#1B4584;color:#ffffff}
.fq-i[open] .fq-pm::after{transform:rotate(0)}
.fq-i summary:focus-visible{outline:3px solid #0F74B5;outline-offset:2px;border-radius:8px}
.fq-a{margin:0;padding:0 60px 26px 0;font-size:17px;line-height:1.65}
/* booking band */
.bk{position:relative;overflow:hidden;isolation:isolate;background:#0E1F3D;color:#ffffff;padding:104px 0}
.bk::before{content:"";position:absolute;inset:0;z-index:-1;background:repeating-linear-gradient(90deg,rgba(255,255,255,.05) 0,rgba(255,255,255,.05) 1px,transparent 1px,transparent 96px);background-position:48px 0}
.bk-arch{position:absolute;left:-140px;bottom:-1px;width:520px;height:600px;border:1.5px solid rgba(148,187,228,.16);border-bottom:0;border-radius:260px 260px 0 0;z-index:-1;pointer-events:none}
.bk-arch::after{content:"";position:absolute;inset:36px;border:1.5px solid rgba(148,187,228,.09);border-bottom:0;border-radius:224px 224px 0 0}
.bk-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:72px;align-items:center}
.bk-h2{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-.01em;color:#ffffff}
.bk-sub{margin:22px 0 0;font-size:19px;line-height:1.6;color:#C9DBF0}
.bk .ct-card{padding:40px}
.bk .ct-submit{background:#94BBE4;color:#0E1F3D}
.bk .ct-submit:hover{background:#0E1F3D;color:#ffffff}
/* visit */
.vu{background:#ffffff;padding:96px 0}
.vu-top{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:64px;align-items:start;margin-top:32px}
.vu-addr{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:34px;line-height:1.25;color:#0E1F3D}
.h-root .vu-list{display:flex;flex-direction:column;gap:20px;margin:0;padding:0;list-style:none}
.vu-item{display:flex;align-items:flex-start;gap:16px}
.vu-ic{display:inline-flex;align-items:center;justify-content:center;flex:none;width:48px;height:48px;border-radius:50%;border:1.5px solid #C9DBF0;color:#1B4584}
.vu-lab{display:block;font-size:13px;line-height:16px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#0B66A0}
.vu-val{display:block;margin-top:4px;font-size:18px;line-height:1.5;color:#0E1F3D}
.h-root a.vu-val{display:inline-flex;align-items:center;min-height:44px;margin-top:-8px;font-weight:600;border-bottom:1px solid transparent}
.h-root a.vu-val:hover{color:#0F74B5}
.vu-map{position:relative;aspect-ratio:3/1;margin-top:56px;border-radius:20px;overflow:hidden;background:#E6ECF4;box-shadow:0 18px 44px rgba(14,31,61,.12)}
.vu-img{position:absolute;display:block;width:200%;max-width:none;left:50%;top:50%;transform:translate(-49.9%,-46.3%)}
.h-root .vu-btn{position:absolute;left:24px;bottom:24px;display:inline-flex;align-items:center;gap:10px;min-height:48px;padding:0 22px;border-radius:999px;background:#ffffff;color:#0E1F3D;font-size:16px;font-weight:600;box-shadow:0 8px 24px rgba(14,31,61,.22);transition:background .2s ease,color .2s ease}
.h-root .vu-btn:hover{background:#0E1F3D;color:#ffffff}
@media (prefers-reduced-motion:reduce){.te-card,.fq-pm,.fq-pm::before,.fq-pm::after{transition:none}.te-card:hover{transform:none}}
@media (max-width:1023px){
  .te,.fq,.vu{padding:80px 0}
  .bk{padding:80px 0}
  .te-wrap,.fq-wrap,.bk-wrap,.vu-wrap{padding:0 32px}
  .h-root .te-grid{gap:18px;margin-top:36px}
  .te-card{padding:16px}
  .te-name{font-size:24px}
  .te-body{padding:20px 4px 6px}
  .te-mem li{font-size:15px}
  .h-root .fq-grid{gap:0 40px;margin-top:36px}
  .fq-i summary{font-size:17px}
  .bk-grid{grid-template-columns:minmax(0,1fr);gap:40px}
  .bk-h2{font-size:52px}
  .vu-top{grid-template-columns:minmax(0,1fr);gap:32px}
  .vu-addr{font-size:30px}
  .vu-map{aspect-ratio:16/7;margin-top:44px}
}
@media (max-width:640px){
  .te,.fq,.vu{padding:64px 0}
  .bk{padding:64px 0}
  .te-wrap,.fq-wrap,.bk-wrap,.vu-wrap{padding:0 20px}
  .h-root .te-grid{display:flex;gap:14px;margin:28px -20px 0;padding:4px 20px 12px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:20px;scrollbar-width:none;-webkit-overflow-scrolling:touch}
  .te-grid::-webkit-scrollbar{display:none}
  .te-grid>li{flex:0 0 calc((100% + 40px) * .85);scroll-snap-align:start}
  .te-name{font-size:28px}
  .te-mem li{font-size:16px}
  .h-root .fq-grid{grid-template-columns:minmax(0,1fr);margin-top:28px}
  .fq-i:nth-last-child(-n+2){border-bottom:0}
  .fq-i:last-child{border-bottom:1px solid #D5DFEC}
  .fq-i summary{min-height:64px;font-size:17px}
  .fq-a{padding-right:8px}
  .bk-h2{font-size:40px}
  .bk-sub{font-size:17px}
  .bk .ct-card{padding:24px 20px}
  .ct-in{font-size:16px}
  .ct-submit{width:100%;align-self:stretch}
  .vu-addr{font-size:26px}
  .vu-map{aspect-ratio:4/3;border-radius:16px;margin-top:36px}
  .vu-img{width:300%}
  .h-root .vu-btn{left:14px;bottom:14px;min-height:44px;padding:0 18px}
}
"""
def team_html(ic):
    cards=''
    for nm in ("Anthony Simiyu","Alphonse Odido","Roy Chidi"):
        cards+='''        <li class="nv"><article class="te-card"><div class="te-ph"><img class="te-img" src="%s" alt="Portrait placeholder for %s (current website portrait)"></div><div class="te-body"><h3 class="te-name">%s</h3><p class="te-role ph2">[Title / role]</p><div class="te-mem"><div class="te-mem-h">Professional Memberships</div><ul><li>%s<span>Law Society of Kenya</span></li><li>%s<span>East Africa Law Society</span></li></ul></div></div></article></li>
'''%(PORT,nm,nm,ic("checkc",22,1.7),ic("checkc",22,1.7))
    return '''  <!-- Meet the advocates -->
  <section class="te" aria-labelledby="te-title">
    <div class="te-wrap">
      <div class="te-head nv">
        <div>
          <div class="ws-eyebrow">THE TEAM</div>
          <h2 class="ws-h2" id="te-title">Meet the Advocates</h2>
        </div>
        <a class="te-all" href="About.dc.html"><span>Meet the full team</span>%s</a>
      </div>
      <ul class="te-grid" aria-label="Our advocates">
%s      </ul>
    </div>
  </section>
'''%(ic("arrow",20,2),cards)
def faq_html(ic):
    items=''
    for n in range(4):
        items+='''        <li class="fq-i nv"><details%s><summary><span class="ph2">[Question to come from the firm]</span><span class="fq-pm" aria-hidden="true"></span></summary><p class="fq-a ph2">[Answer to come from the firm]</p></details></li>
'''%(' open' if n==0 else '')
    # border on li, details inside
    return '''  <!-- FAQ -->
  <section class="fq" aria-labelledby="fq-title">
    <div class="fq-wrap">
      <div class="nv">
        <div class="ws-eyebrow">FAQ</div>
        <h2 class="ws-h2" id="fq-title">Frequently Asked Questions</h2>
      </div>
      <ul class="fq-grid">
%s      </ul>
    </div>
  </section>
'''%items
def band_html(ic):
    def f(i,lab,typ='text',req=True,ta=False,auto=''):
        r=' required aria-required="true"' if req else ''
        a=f' autocomplete="{auto}"' if auto else ''
        ctl=f'<textarea class="ct-in" id="{i}" name="{i}" rows="6"></textarea>' if ta else f'<input class="ct-in" id="{i}" name="{i}" type="{typ}"{r}{a}>'
        e='' if ta else f'<p class="ct-err" id="{i}-e">This field is required</p>'
        return f'<div class="ct-f"><label for="{i}">{lab}</label>{ctl}{e}</div>'
    form='<form class="ct-form" action="#" method="post">'+f('bk-name','Your name',auto='name')+f('bk-email','Your email','email',auto='email')+f('bk-subj','Subject')+f('bk-msg','Your message (optional)',req=False,ta=True)+'<button class="ct-submit" type="submit">Submit</button></form>'
    return '''  <!-- Book appointment band -->
  <section class="bk" id="book" aria-labelledby="bk-title">
    <div class="bk-arch" aria-hidden="true"></div>
    <div class="bk-wrap">
      <div class="bk-grid">
        <div class="nv">
          <h2 class="bk-h2" id="bk-title">Book Appointment</h2>
          <p class="bk-sub">ASW Law Advocates LLP</p>
        </div>
        <div class="ct-card nv">%s</div>
      </div>
    </div>
  </section>
'''%form
def visit_html(ic):
    return '''  <!-- Visit us -->
  <section class="vu" aria-labelledby="vu-title">
    <div class="vu-wrap">
      <div class="nv">
        <div class="ws-eyebrow">VISIT US</div>
        <div class="vu-top">
          <h2 class="vu-addr" id="vu-title">%s</h2>
          <ul class="vu-list">
            <li class="vu-item"><span class="vu-ic">%s</span><div><span class="vu-lab">Hours</span><span class="vu-val">Mon to Fri: 9.00am to 5.00pm</span></div></li>
            <li class="vu-item"><span class="vu-ic">%s</span><div><span class="vu-lab">Phone</span><a class="vu-val" href="tel:+254788685911">+254 788 685 911</a></div></li>
            <li class="vu-item"><span class="vu-ic">%s</span><div><span class="vu-lab">Email</span><a class="vu-val" href="mailto:info@aswlaw.africa">info@aswlaw.africa</a></div></li>
          </ul>
        </div>
      </div>
      <div class="vu-map nv">
        <img class="vu-img" src="%s" alt="Map of Nairobi with a pin at the Tourism Fund building on Valley Road">
        <a class="vu-btn" href="https://www.google.com/maps/search/?api=1&amp;query=Tourism+Fund+Building+Off-Bishop+Rd+Nairobi+Kenya" target="_blank" rel="noopener"><span>Open in Maps</span>%s</a>
      </div>
    </div>
  </section>
'''%(ADDR,ic("clock",22,1.6),ic("phone",22,1.6),ic("mail",22,1.6),MAPB,ic("arrowur",18,2))
