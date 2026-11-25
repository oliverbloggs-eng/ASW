import re
g=open('/home/claude/hero/gen_about.py').read()
exec(g.split("STATUS=''")[0])
ab=open('/home/claude/hero/project/About.dc.html',encoding='utf-8').read()
head=ab[ab.index('<!-- Contact bar -->'):ab.index('<!-- Page hero -->')]
head=head.replace('<a class="cur" href="About.dc.html" aria-current="page">About Us</a>','<a href="About.dc.html">About Us</a>').replace('<a class="l cur" href="About.dc.html" aria-current="page">About Us</a>','<a class="l" href="About.dc.html">About Us</a>')
head=head.replace('<a href="Areas.dc.html">Areas Of Practice</a>','<a class="cur" href="Areas.dc.html" aria-current="page">Areas Of Practice</a>').replace('<a class="l" href="Areas.dc.html">Areas Of Practice</a>','<a class="l cur" href="Areas.dc.html" aria-current="page">Areas Of Practice</a>')
hero=ab[ab.index('<!-- Page hero -->'):ab.index('<!-- Who we are -->')]
hero=hero.replace('<li><span aria-current="page">About Us</span></li>','<li><span aria-current="page">Areas of Practice</span></li>').replace('id="pg-title">About Us<','id="pg-title">Areas of Practice<')
assert 'Areas of Practice</span>' in hero and 'Areas of Practice</h1>' in hero

D=[("dispute","Dispute Resolution","2f9ce9737e758419c7843a6b52aeeb80","Disputes are costly in time, money and relationships. We help individuals and corporations resolve them efficiently, whether through negotiation, mediation, arbitration or the courts. We take a practical view of every matter: where a settlement serves your interests we will say so, and where a case must be fought we are ready to represent you.",["Civil and commercial litigation","Negotiation, mediation and settlement","Arbitration and other alternative dispute resolution","Advice on strategy and risk before a dispute escalates"]),
("commercial","Commercial and Corporate","bc21d296171ed55434e696b22d269465","We advise businesses at every stage, from setting up to day-to-day operations and major transactions. Our advice is clear, commercially minded and aimed at protecting your business while helping it grow.",["Company registration, changes and dissolution","Drafting, reviewing and negotiating commercial agreements","Conducting due diligence in commercial transactions","Structuring of commercial transactions","Represent Clients before commercial tribunals and mainstream courts in commercial disputes","Offer general advisory on intellectual property protection","Registration of intellectual property rights"]),
("procurement","Public Procurement and Tax","a50705e4f7f7690f9aeea13a447e23ad","Public tenders and tax obligations both demand precision. We guide clients through procurement processes and tax matters so that they remain compliant, and we represent them when a decision needs to be challenged.",["Offer general advisory services in respect of tax and procurement matters","Represent Clients in procurement-related disputes before the Public procurement authorities, the High Court and the Court of Appeal","Represent Clients in tax-related disputes before the Tax authorities, the High Court, and Court of Appeal","Represent Clients in the High Court and Court of Appeal on Procurement and Tax matters"]),
("property","Property &amp; Real Estate","42f37620f2e5d87828aa00609d8ec8be","Property is often a client's most valuable asset. We provide dependable advice on buying, selling, leasing and charging property in Kenya, with careful attention to title and due diligence so that every transaction proceeds with confidence.",["Draft, review, and negotiate Leases, Sales, Charge, Discharge and other property-related Agreements","Conduct due diligence in respect of property transactions","Structure property transactions","Represent Clients in property-related disputes at property tribunals","Represent Clients in property-related disputes in the mainstream courts i.e. Magistrates, Environment and Land Court and Court of Appeal"]),
("private","Private Client","ae893e31afab0a7bd15accf76ca31d4e","Our private client work is personal. We advise individuals and families on the matters that protect their wellbeing, their family and their legacy, with discretion and care.",["Estate Planning","Mental Health","Child Adoption","Succession","Child Custody","Divorce","Matrimonial Property"]),
("employment","Employment and Pensions","3b59ac2f7aa43ff1616140725066af49","We advise on employment and pension arrangements and represent clients when disputes arise.",["Draft, review and negotiate employment and pension and other employment-related agreements","Represent clients in employment-related disputes before the Magistrates Court, Employment and Labour Relations Court"])]

CSS2=r"""
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
.h-root .ab-bar{position:sticky;top:88px;z-index:30;background:rgba(255,255,255,.97);border-bottom:1px solid #E1E8F2;box-shadow:0 6px 20px rgba(14,31,61,.06)}
.ab-in{max-width:1280px;margin:0 auto;padding:12px 40px}
.h-root .ab-list{display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px}
.h-root .ab-pill{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:0 15px;border:1px solid #C9DBF0;border-radius:999px;background:#ffffff;color:#0E1F3D;font-size:15px;line-height:20px;font-weight:500;white-space:nowrap;text-decoration:none;transition:background .2s ease,color .2s ease,border-color .2s ease}
.h-root .ab-pill:hover{border-color:#1B4584;color:#1B4584}
.h-root .ab-pill.on{background:#1B4584;border-color:#1B4584;color:#ffffff}
.ar{position:relative;padding:96px 0;scroll-margin-top:76px}
.ar-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:72px;align-items:center}
.ab-bar + .ar{padding-top:80px}
.h-root section.ar[id]{scroll-margin-top:170px}
.ar-even .ar-media{order:2}
.ar-media{margin:0}
.ar-img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:20px;box-shadow:0 22px 50px rgba(14,31,61,.16)}
.ar-num{display:block;font-family:'DM Sans',sans-serif;font-weight:600;font-size:96px;line-height:1;letter-spacing:-.02em;font-variant-numeric:lining-nums;color:#94BBE4}
.ar-h2{margin:10px 0 0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:40px;line-height:1.14;letter-spacing:-.01em;color:#0E1F3D;text-wrap:balance}
.ar-p{margin:28px 0 0;font-size:18px;line-height:1.7;color:#33445F}
.ar-hh{margin:32px 0 14px;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:24px;line-height:1.2;color:#0E1F3D}
.h-root .ar-list{display:flex;flex-direction:column;gap:12px}
.ar-list li{display:flex;align-items:flex-start;gap:12px;font-size:17px;line-height:1.5;color:#0E1F3D}
.ar-list li svg{flex:none;margin-top:1px;color:#1B4584}
.h-root .ar-btn{display:inline-flex;align-items:center;justify-content:center;min-height:52px;margin-top:36px;padding:0 30px;border-radius:999px;background:#1B4584;color:#ffffff;font-size:16px;line-height:22px;font-weight:600;text-decoration:none;text-align:center;transition:background .2s ease,transform .2s ease}
.h-root .ar-btn:hover{background:#0E1F3D;transform:translateY(-2px)}
.ar-mob{display:none}
.h-root .ar-two{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 28px}
.h-root .ar-chips{display:flex;flex-wrap:wrap;gap:12px}
.ar-chips li{display:inline-flex;align-items:center;min-height:44px;padding:0 20px;border:1.5px solid #94BBE4;border-radius:999px;background:transparent;color:#0E1F3D;font-size:16px;line-height:22px;font-weight:500}
.cl{position:relative;background:#0E1F3D;color:#ffffff;padding:80px 0;border-top:1px solid rgba(148,187,228,.18)}
.cl-in{max-width:1280px;margin:0 auto;padding:0 40px;display:flex;align-items:center;justify-content:space-between;gap:40px}
.cl-h{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:44px;line-height:1.15;color:#ffffff;max-width:640px;text-wrap:balance}
.cl-act{display:flex;align-items:center;gap:28px;flex-wrap:wrap}
.h-root .cl-book{display:inline-flex;align-items:center;justify-content:center;min-height:56px;padding:0 34px;border-radius:999px;background:#94BBE4;color:#0E1F3D;font-size:17px;font-weight:600;text-decoration:none;transition:background .2s ease}
.h-root .cl-book:hover{background:#ffffff}
.h-root .cl-link{display:inline-flex;align-items:center;gap:10px;min-height:44px;color:#ffffff;font-size:17px;font-weight:500;text-decoration:underline;text-decoration-color:#94BBE4;text-underline-offset:6px;text-decoration-thickness:1px}
.h-root .cl-link:hover{text-decoration-thickness:2px}
@media (max-width:1023px){
  .ab-in{padding:10px 32px}
  .h-root .ab-bar{top:80px}
  .h-root .ab-list{flex-wrap:nowrap;justify-content:flex-start;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}
  .ab-list::-webkit-scrollbar{display:none}
  .ar{padding:80px 0}
  .ar-grid{grid-template-columns:minmax(0,1fr);gap:40px}
  .ar-even .ar-media{order:0}
  .ar-num{font-size:84px}
  .h-root .ar-two{display:flex;gap:12px}
  .cl{padding:72px 0}
  .cl-in{padding:0 32px}
  .cl-h{font-size:38px}
}
@media (max-width:640px){
  .ab-in{padding:8px 20px}
  .h-root .ab-bar{top:72px}
  .h-root section[id]{scroll-margin-top:152px}
  .h-root .ab-list{margin:0 -20px;padding:2px 20px 4px;scroll-padding-left:20px}
  .h-root .ab-pill{font-size:16px;flex:none}
  .ar{padding:56px 0;scroll-margin-top:68px}
  .ab-bar + .ar{padding-top:56px}
  .ar-grid{gap:28px}
  .ar-img{border-radius:16px}
  .ar-num{font-size:64px}
  .ar-h2{font-size:32px}
  .ar-p{font-size:17px;margin-top:22px}
  .ar-dsk{display:none}
  .ar-mob{display:block;margin-top:26px;border-top:1px solid #D2DCEA;border-bottom:1px solid #D2DCEA}
  .ar-mob summary{display:flex;align-items:center;justify-content:space-between;min-height:56px;cursor:pointer;list-style:none;font-family:'Marcellus',Georgia,serif;font-size:22px;color:#0E1F3D}
  .ar-mob summary::-webkit-details-marker{display:none}
  .ar-mob summary svg{transition:transform .25s ease;color:#1B4584}
  .ar-mob[open] summary svg{transform:rotate(180deg)}
  .ar-mob .ar-list{padding:2px 0 20px}
  .h-root .ar-btn{display:flex;width:100%;margin-top:28px;padding:12px 24px}
  .cl{padding:56px 0}
  .cl-in{flex-direction:column;align-items:flex-start;padding:0 20px;gap:28px}
  .cl-h{font-size:32px}
  .cl-act{width:100%;flex-direction:column;align-items:stretch;gap:12px}
  .h-root .cl-book{width:100%}
  .h-root .cl-link{justify-content:center}
}
"""
def secs(ic):
    out=''
    for n,(i,t,b,p,items) in enumerate(D,1):
        bg='sec-w' if n%2 else 'sec-o'
        ev='' if n%2 else ' ar-even'
        li=''.join('<li>%s<span>%s</span></li>'%(ic("checkc",22,1.7),x) for x in items)
        two=' ar-two' if i=='commercial' else ''
        chev='<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'
        if i=='private':
            lst='          <h3 class="ar-hh">Matters we handle</h3><ul class="ar-chips">'+''.join('<li>%s</li>'%x for x in items)+'</ul>'
        else:
            lst=f'          <div class="ar-dsk"><h3 class="ar-hh">What we do</h3><ul class="ar-list{two}">{li}</ul></div>\n          <details class="ar-mob"{" open" if n==1 else ""}><summary>What we do{chev}</summary><ul class="ar-list">{li}</ul></details>'
        out+=f'''  <section class="ar {bg}{ev}" id="{i}" aria-labelledby="{i}-t">
    <div class="pg-wrap">
      <div class="ar-grid">
        <figure class="ar-media rv"><img class="ar-img" src="/_blob/{b}" alt="{t}"></figure>
        <div class="ar-tx rv">
          <span class="ar-num" aria-hidden="true">0{n}</span>
          <h2 class="ar-h2" id="{i}-t">{t}</h2>
          <p class="ar-p">{p}</p>
{lst}
          <a class="ar-btn" href="Book.dc.html">Talk to us about {t}</a>
        </div>
      </div>
    </div>
  </section>

'''
    return out
def build_a(name,title,w,h):
    bar=''
    body=f'''
<div class="h-root">

  {head}
{hero}
  <!-- Anchor bar -->
  <nav class="ab-bar" aria-label="Areas of practice">
    <div class="ab-in" id="ab-track">
      <ul class="ab-list">
        <sc-for list="{{{{pills}}}}" as="p" hint-placeholder-count="6">
          <li><a class="{{{{p.cls}}}}" href="{{{{p.href}}}}" aria-current="{{{{p.cur}}}}">{{{{p.label}}}}</a></li>
        </sc-for>
      </ul>
    </div>
  </nav>

{secs(ic)}
  <!-- Closing prompt -->
  <section class="cl" aria-labelledby="cl-t">
    <div class="cl-in">
      <h2 class="cl-h" id="cl-t">Not sure which area applies to you?</h2>
      <div class="cl-act">
        <a class="cl-book" href="Book.dc.html">Book Appointment</a>
        <a class="cl-link" href="Contact.dc.html"><span>Contact Us</span>{ic("arrow",20,2)}</a>
      </div>
    </div>
  </section>

{foot_html(ic,False)}
</div>
'''
    labels=[re.sub('&amp;','&',t) for _,t,_,_,_ in D]
    ids=[i for i,*_ in D]
    script='''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":%d,"height":%d}}'>
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { open: false, active: 0 };
    const ids = %s;
    const f = () => {
      let a = 0;
      ids.forEach((id, i) => { const e = document.getElementById(id); if (e && e.getBoundingClientRect().top <= 150) a = i; });
      if (a !== this.state.active) {
        this.setState({ active: a });
        const tr = document.getElementById('ab-track');
        const el = document.querySelector('.h-root .ab-pill.on');
        const l = tr && tr.querySelector('.ab-list');
        if (l && el && l.scrollWidth > l.clientWidth) l.scrollTo({ left: Math.max(0, el.offsetLeft - 24), behavior: 'smooth' });
      }
    };
    try { document.addEventListener('scroll', f, true); window.addEventListener('scroll', f, { passive: true }); } catch (e) {}
  }
  renderVals() {
    const open = this.state.open;
    const labels = %s;
    const ids = %s;
    return {
      open,
      toggle: () => this.setState({ open: !this.state.open }),
      burgerPath: open ? 'M6 6l12 12M18 6L6 18' : 'M4 7h16M4 12h16M4 17h16',
      burgerLabel: open ? 'Close menu' : 'Open menu',
      pills: labels.map((l, i) => ({ label: l, href: '#' + ids[i], cls: i === this.state.active ? 'ab-pill on' : 'ab-pill', cur: i === this.state.active ? 'true' : 'false' }))
    };
  }
}
</script>''' % (w,h,json.dumps(ids),json.dumps(labels),json.dumps(ids))
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
{BASE_CSS}{PAGE_CSS}{FOOT_CSS}{CSS2}</style>
</helmet>
{body}</x-dc>
{script}
</body>
</html>
'''
    html=html.replace('{{{{','{{').replace('}}}}','}}')
    open('/home/claude/hero/project/%s.dc.html'%name,'w',encoding='utf-8').write(html)
import json
build_a('Areas','Areas of Practice: ASW Law Advocates LLP',1440,6593)
build_a('AreasTablet','Areas of Practice: Tablet 768',768,9139)
build_a('AreasPhone','Areas of Practice: Phone 390',390,7199)
print('ok')
