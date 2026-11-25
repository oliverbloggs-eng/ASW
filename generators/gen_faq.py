import re,json
g=open('/home/claude/hero/gen_about.py').read()
exec(g.split("STATUS=''")[0])
ab=open('/home/claude/hero/project/About.dc.html',encoding='utf-8').read()
head=ab[ab.index('<!-- Contact bar -->'):ab.index('<!-- Page hero -->')]
head=head.replace('<a class="cur" href="About.dc.html" aria-current="page">About Us</a>','<a href="About.dc.html">About Us</a>').replace('<a class="l cur" href="About.dc.html" aria-current="page">About Us</a>','<a class="l" href="About.dc.html">About Us</a>')
assert head.count('aria-current="page"')==0
hero=ab[ab.index('<!-- Page hero -->'):ab.index('<!-- Who we are -->')]
hero=hero.replace('<span aria-current="page">About Us</span>','<span aria-current="page">Frequently Asked Questions</span>').replace('id="pg-title">About Us<','id="pg-title">Frequently Asked Questions<')
assert 'Frequently Asked Questions</h1>' in hero
CSS3=r"""
.h-root .fq-pills{display:flex;flex-wrap:wrap;gap:12px;margin:0;padding:0;list-style:none}
.fq-pill{display:inline-flex;align-items:center;min-height:44px;padding:0 22px;border:1.5px solid #8FB0D6;border-radius:999px;background:#ffffff;font:500 16px/1 'DM Sans',system-ui,sans-serif;color:#0E1F3D;cursor:pointer;transition:background .2s ease,color .2s ease,border-color .2s ease}
.fq-pill:hover{background:#1B4584;border-color:#1B4584;color:#ffffff}
.fq-pill.on{background:#1B4584;border-color:#1B4584;color:#ffffff}
.fq-off{display:none}
.fq-pill:focus-visible{outline:3px solid #0F74B5;outline-offset:3px}
.h-root .fq-acc{max-width:960px;margin:40px 0 0;padding:0;list-style:none;border-bottom:1px solid #D5DFEC}
.fq-i{border-top:1px solid #D5DFEC}
.fq-i summary{display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:76px;padding:12px 0;cursor:pointer;list-style:none;font-size:20px;line-height:1.4}
.fq-i summary::-webkit-details-marker{display:none}
.fq-pm{position:relative;flex:none;width:40px;height:40px;border-radius:50%;border:1.5px solid #C9DBF0;color:#1B4584;transition:background .2s ease,color .2s ease}
.fq-pm::before,.fq-pm::after{content:"";position:absolute;left:50%;top:50%;width:14px;height:1.8px;margin:-.9px 0 0 -7px;background:currentColor;border-radius:2px;transition:transform .25s ease}
.fq-pm::after{transform:rotate(90deg)}
.fq-q{color:#0E1F3D;font-weight:500}
.fq-a{color:#2A3A55}
.fq-i[open] .fq-pm{background:#1B4584;border-color:#1B4584;color:#ffffff}
.fq-i[open] .fq-pm::after{transform:rotate(0)}
.fq-i summary:focus-visible{outline:3px solid #0F74B5;outline-offset:2px;border-radius:8px}
.fq-a{margin:0;padding:0 64px 26px 0;font-size:17px;line-height:1.65}
@media (prefers-reduced-motion:reduce){.fq-pill,.fq-pm,.fq-pm::before,.fq-pm::after{transition:none}}
@media (max-width:640px){
  .h-root .fq-pills{flex-wrap:nowrap;overflow-x:auto;margin:0 -20px;padding:2px 20px 8px;scrollbar-width:none;scroll-snap-type:x proximity}
  .fq-pills::-webkit-scrollbar{display:none}
  .fq-pills>li{flex:none}
  .h-root .fq-acc{margin-top:24px}
  .fq-i summary{min-height:68px;font-size:17px}
  .fq-a{padding-right:8px}
}
"""
from faqdata import FAQS
AR=["Dispute Resolution","Commercial and Corporate","Public Procurement and Tax","Property &amp; Real Estate","Private Client","Employment and Pensions"]
def build_i(name,title,w,h):
    pills='        <li><button class="{{pc_all}}" type="button" aria-pressed="{{pa_all}}" onClick="{{pf_all}}">All</button></li>\n        <li><button class="{{pc_g}}" type="button" aria-pressed="{{pa_g}}" onClick="{{pf_g}}">General</button></li>\n'
    for k,x in enumerate(AR): pills+='        <li><button class="{{pc_%d}}" type="button" aria-pressed="{{pa_%d}}" onClick="{{pf_%d}}">%s</button></li>\n'%(k,k,k,x)
    acc=''
    for n,(t,q,a) in enumerate(FAQS):
        acc+='        <li class="{{fc_%d}}"><details><summary><span class="fq-q">%s</span><span class="fq-pm" aria-hidden="true"></span></summary><p class="fq-a">%s</p></details></li>\n'%(n,q,a)
    body=f'''
<div class="h-root">

  {head}
{hero}
  <!-- FAQ -->
  <section class="sec sec-w" aria-label="Frequently asked questions">
    <div class="pg-wrap">
      <ul class="fq-pills" aria-label="Filter by area of practice">
{pills}      </ul>
      <ul class="fq-acc">
{acc}      </ul>
    </div>
  </section>

{foot_html(ic)}
</div>
'''
    script='''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":%d,"height":%d}}'>
const TAGS = ['g','g','g','g',0,1,2,3,4,5];
class Component extends DCLogic {
  constructor(props) { super(props); this.state = { open: false, f: 'all' }; }
  renderVals() {
    const open = this.state.open;
    const f = this.state.f;
    const v = {
      open,
      toggle: () => this.setState({ open: !this.state.open }),
      burgerPath: open ? 'M6 6l12 12M18 6L6 18' : 'M4 7h16M4 12h16M4 17h16',
      burgerLabel: open ? 'Close menu' : 'Open menu'
    };
    ['all', 'g', 0, 1, 2, 3, 4, 5].forEach((k) => {
      v['pc_' + k] = f === k ? 'fq-pill on' : 'fq-pill';
      v['pa_' + k] = f === k ? 'true' : 'false';
      v['pf_' + k] = () => this.setState({ f: k });
    });
    TAGS.forEach((t, n) => {
      v['fc_' + n] = (f === 'all' || f === t) ? 'fq-i' : 'fq-i fq-off';
    });
    return v;
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
{BASE_CSS}{PAGE_CSS}{FOOT_CSS}{CSS3}</style>
</helmet>
{body}</x-dc>
{script}
</body>
</html>
'''
    html=html.replace('{{{{','{{').replace('}}}}','}}')
    open('/home/claude/hero/project/%s.dc.html'%name,'w',encoding='utf-8').write(html)
import sys
H=json.loads(sys.argv[1]) if len(sys.argv)>1 else [2000,2200,2000]
build_i('FAQ','Frequently Asked Questions: ASW Law Advocates LLP',1440,H[0])
build_i('FAQTablet','Frequently Asked Questions: Tablet 768',768,H[1])
build_i('FAQPhone','Frequently Asked Questions: Phone 390',390,H[2])
print('ok')
