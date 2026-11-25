import re,json
g=open('/home/claude/hero/gen_about.py').read()
exec(g.split("STATUS=''")[0])
ab=open('/home/claude/hero/project/About.dc.html',encoding='utf-8').read()
head=ab[ab.index('<!-- Contact bar -->'):ab.index('<!-- Page hero -->')]
head=head.replace('<a class="cur" href="About.dc.html" aria-current="page">About Us</a>','<a href="About.dc.html">About Us</a>').replace('<a class="l cur" href="About.dc.html" aria-current="page">About Us</a>','<a class="l" href="About.dc.html">About Us</a>')
head=head.replace('<a href="Insights.dc.html">Insights</a>','<a class="cur" href="Insights.dc.html" aria-current="page">Insights</a>').replace('<a class="l" href="Insights.dc.html">Insights</a>','<a class="l cur" href="Insights.dc.html" aria-current="page">Insights</a>')
assert head.count('aria-current="page"')==2
hero=ab[ab.index('<!-- Page hero -->'):ab.index('<!-- Who we are -->')]
hero=hero.replace('<span aria-current="page">About Us</span>','<span aria-current="page">Insights</span>').replace('id="pg-title">About Us<','id="pg-title">Insights<')
assert 'Insights</h1>' in hero and 'Insights</span>' in hero
EX="Performance marketing may involve using various types of digital marketing and advertising channels, including the …"
POSTS=[("5b4b94f7270eb91f66f1193f7dc7a478","Know about Industrial Laws","Article.dc.html"),("08993c385854a23fc1db4562a381fd00","Flexibility of marriage in US","ArticleMarriage.dc.html")]
CSS3=r"""
.h-root .in-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:32px}
.in-card{display:flex;align-items:stretch;gap:28px;height:100%;padding:20px 28px 20px 20px;background:#ffffff;border:1px solid #E6ECF4;border-radius:20px;box-shadow:0 14px 40px rgba(14,31,61,.07);text-decoration:none;color:inherit;transition:transform .25s ease,box-shadow .25s ease}
.in-card:hover,.in-card:focus-visible{transform:translateY(-4px);box-shadow:0 20px 46px rgba(14,31,61,.13)}
.in-img{flex:none;align-self:flex-start;width:220px;aspect-ratio:4/5;border-radius:16px;object-fit:cover;display:block;background:#E6ECF4}
.in-body{min-width:0;flex:1;display:flex;flex-direction:column;align-items:flex-start}
.in-date{display:inline-flex;align-items:center;gap:8px;font-size:15px;line-height:20px;font-weight:600;color:#0B66A0}
.in-title{margin:12px 0 0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:26px;line-height:1.22;color:#0E1F3D;transition:color .2s ease}
.in-card:hover .in-title,.in-card:focus-visible .in-title{color:#0F74B5}
.in-ex{margin:12px 0 0;font-size:16px;line-height:1.6;color:#33445F;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.in-more{display:inline-flex;align-items:center;gap:8px;min-height:44px;margin-top:auto;padding-top:6px;font-size:16px;font-weight:600;color:#0B66A0}
.in-more svg{transition:transform .2s ease}
.in-card:hover .in-more svg{transform:translateX(4px)}
@media (prefers-reduced-motion:reduce){.in-card,.in-title,.in-more svg{transition:none}.in-card:hover{transform:none}}
@media (max-width:1023px){
  .h-root .in-list{grid-template-columns:minmax(0,1fr);gap:24px}
  .in-card{padding:22px 32px 22px 22px;gap:32px}
}
@media (max-width:640px){
  .h-root .in-list{gap:16px}
  .in-card{gap:16px;padding:14px;border-radius:18px}
  .in-img{width:96px;aspect-ratio:4/5;border-radius:12px}
  .in-ex{display:none}
  .in-title{margin-top:6px;font-size:20px;line-height:1.25;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
  .in-date{font-size:14px}
  .in-more{padding-top:2px}
}
"""
def build_i(name,title,w,h):
    cards=''.join('        <li class="rv"><a class="in-card" href="%s"><img class="in-img" src="/_blob/%s" alt=""><span class="in-body"><span class="in-date">%s<span>June 24, 2025</span></span><h2 class="in-title">%s</h2><p class="in-ex">%s</p><span class="in-more"><span>Read More</span>%s</span></span></a></li>\n'%(href,b,ic("calendar",16,1.8),t,EX,ic("arrow",18,2)) for b,t,href in POSTS)
    body=f'''
<div class="h-root">

  {head}
{hero}
  <!-- Posts -->
  <section class="sec sec-o" aria-label="Insights posts">
    <div class="pg-wrap">
      <ul class="in-list">
{cards}      </ul>
    </div>
  </section>

{foot_html(ic)}
</div>
'''
    script='''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":%d,"height":%d}}'>
class Component extends DCLogic {
  constructor(props) { super(props); this.state = { open: false }; }
  renderVals() {
    const open = this.state.open;
    return {
      open,
      toggle: () => this.setState({ open: !this.state.open }),
      burgerPath: open ? 'M6 6l12 12M18 6L6 18' : 'M4 7h16M4 12h16M4 17h16',
      burgerLabel: open ? 'Close menu' : 'Open menu'
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
build_i('Insights','Insights: ASW Law Advocates LLP',1440,H[0])
build_i('InsightsTablet','Insights: Tablet 768',768,H[1])
build_i('InsightsPhone','Insights: Phone 390',390,H[2])
print('ok')
