import re,sys
sys.path.insert(0,'/home/claude/hero')
src=open('/home/claude/hero/gen.py').read().split('TEMPLATE = open')[0]
exec(src)
P["building"]='<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4"/><path d="M10 10h4"/><path d="M10 14h4"/><path d="M10 18h4"/>'
P["checkc"]='<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>'
KEYS=['w0','w1','p0','p1','p2','s0','s1','s2','s3','b0','b1','b2']
def acc(k,lead,title,body,cls=''):
    return '''          <li class="{{c_%s}}%s"><h3 class="ac-h"><button class="ac-btn" type="button" aria-expanded="{{a_%s}}" aria-controls="ac-%s" onClick="{{t_%s}}">%s<span class="ac-t">%s</span><span class="ac-pm" aria-hidden="true"></span></button></h3><div class="ac-p" id="ac-%s" role="region" aria-label="%s"><div class="ac-pi">%s</div></div></li>
'''%(k,cls,k,k,k,lead,title,k,title,body)
PH='<p class="bd">%s</p>'
import faqdata as FD
CK='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>'
def icn(n): return '<span class="pg-ic">%s</span>'%ic(n,20,1.6)
M_WHO='''<div class="m-only">
      <div class="sec-eyebrow">WHO WE ARE</div>
      <h2 class="sec-h2" id="who-m">About ASW Law Advocates LLP</h2>
      <p class="wh-p">We are a legal practice based in Nairobi, Kenya, specializing in offering client-centric legal solutions to our clientele, which includes individuals and corporations.</p>
      <ul class="ac-list ind52" aria-label="Who we serve">
'''+acc('w0',icn('user'),'Individuals',PH%FD.WHO['Individuals'])+acc('w1',icn('building'),'Corporations',PH%FD.WHO['Corporations'])+'''      </ul>
    </div>'''
pl=''
for i,(t,k) in enumerate((("Competence","checks"),("Integrity","shield"),("Pragmatism","scale"))):
    pl+=acc('p%d'%i,'<span class="ac-num" aria-hidden="true">0%d</span>%s'%(i+1,icn(k)),t,PH%FD.PILL[t])
M_PILL='''<div class="m-only">
      <div class="sec-eyebrow">OUR PILLARS</div>
      <h2 class="sec-h2" id="pill-m">Our Pillars</h2>
      <p class="pl-lead">Underpinning our work ethic are 3 pillars:</p>
      <ul class="ac-list ind90" aria-label="Our three pillars">
'''+pl+'''      </ul>
    </div>'''
hw=''
for i,t in enumerate(("Consultation","Advice","Representation","Resolution")):
    c='<span class="hs-c" aria-hidden="true">%s</span>'%(CK.replace('width="16" height="16"','width="18" height="18"') if i==3 else str(i+1))
    hw+=acc('s%d'%i,c,t,PH%FD.STEP[t])
M_HOW='''<div class="m-only">
      <div class="sec-eyebrow">HOW WE WORK</div>
      <h2 class="sec-h2" id="hw-m">Our Approach</h2>
      <ol class="ac-list hw-m ind52" aria-label="Our approach in four steps">
'''+hw+'''      </ol>
    </div>'''
tm=''
for i,nm in enumerate(("Anthony Simiyu","Alphonse Odido","Roy Chidi")):
    tm+='''        <li class="{{tc%d}}"><article class="mt-card"><span class="mt-fr"><span class="mt-ph"><img class="mt-img" src="/_blob/6a71c35ed220aaa8ba6455a78de01d88" alt="Portrait of %s"></span></span>
          <h3 class="mt-n">%s</h3><p class="mt-r bd">Advocate</p>
          <div class="mt-mh">Professional Memberships</div>
          <ul class="mt-mem"><li><span class="mt-ck">%s</span><span>Law Society of Kenya</span></li><li><span class="mt-ck">%s</span><span>East Africa Law Society</span></li></ul>
          <ul class="ac-list mt-bio">
%s          </ul></article></li>
'''%(i,nm,nm,CK,CK,acc('b%d'%i,'','Biography',PH%FD.BIO(nm)))
LEFT=ic('arrow',20,2).replace('d="M5 12h14"/><path d="m12 5 7 7-7 7"','d="M19 12H5"/><path d="m12 19-7-7 7-7"')
M_TEAM='''<div class="m-only">
      <div class="sec-eyebrow">THE TEAM</div>
      <h2 class="sec-h2" id="team-m">The Team</h2>
      <ul class="mt-grid" id="tm-m-track" aria-label="The team" onScroll="{{onTeamM}}">
'''+tm+'''      </ul>
      <div class="at-ctl mt-ctl">
        <div class="at-cnt">
          <p class="at-num" aria-live="polite"><span class="at-cur">{{tcur}}</span><span class="at-tot"> / 03</span></p>
          <span class="at-track" aria-hidden="true"><span class="{{tFill}}"></span></span>
        </div>
        <div class="at-btns">
          <button class="{{tPrevCls}}" type="button" aria-label="Previous advocate" aria-disabled="{{tPrevAria}}" onClick="{{tPrev}}">'''+LEFT+'''</button>
          <button class="{{tNextCls}}" type="button" aria-label="Next advocate" aria-disabled="{{tNextAria}}" onClick="{{tNext}}">'''+ic('arrow',20,2)+'''</button>
        </div>
      </div>
    </div>'''
SCRIPT='''<script type="text/x-dc" data-dc-script data-props='%s'>
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { open: false, ai: 0, ti: 0, o: { p0: true } };
  }
  tog(k) {
    const o = Object.assign({}, this.state.o);
    o[k] = !o[k];
    this.setState({ o });
  }
  goT(i) {
    const t = document.getElementById('tm-m-track');
    if (!t || i < 0 || i > 2 || !t.children[i]) return;
    t.scrollTo({ left: t.children[i].offsetLeft - t.children[0].offsetLeft, behavior: 'smooth' });
  }
  renderVals() {
    const open = this.state.open;
    const ai = this.state.ai;
    const ti = this.state.ti;
    const o = this.state.o;
    const v = {
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
      },
      tc0: ti === 0 ? 'ta-l on' : 'ta-l',
      tc1: ti === 1 ? 'ta-l on' : 'ta-l',
      tc2: ti === 2 ? 'ta-l on' : 'ta-l',
      tcur: String(ti + 1).padStart(2, '0'),
      tFill: 'at-fill t' + ti,
      tPrevCls: ti === 0 ? 'at-btn dis' : 'at-btn',
      tNextCls: ti === 2 ? 'at-btn dis' : 'at-btn',
      tPrevAria: ti === 0 ? 'true' : 'false',
      tNextAria: ti === 2 ? 'true' : 'false',
      tPrev: () => this.goT(this.state.ti - 1),
      tNext: () => this.goT(this.state.ti + 1),
      onTeamM: (e) => {
        const t = e.currentTarget || e.target;
        if (!t || !t.children || t.children.length < 2) return;
        const step = t.children[1].offsetLeft - t.children[0].offsetLeft;
        const i = Math.max(0, Math.min(2, Math.round(t.scrollLeft / step)));
        if (i !== this.state.ti) this.setState({ ti: i });
      }
    };
    %s.forEach((k) => {
      v['a_' + k] = o[k] ? 'true' : 'false';
      v['c_' + k] = o[k] ? 'ac open' : 'ac';
      v['t_' + k] = () => this.tog(k);
    });
    return v;
  }
}
</script>'''
CSS=open('/home/claude/hero/about_mobile.css').read()+open('/home/claude/hero/about_type.css').read()
import glob
for n in ('About','AboutPhone','AboutTablet'):
    f='/home/claude/hero/project/%s.dc.html'%n
    s=open(f,encoding='utf-8').read()
    if 'm-only' in s: continue
    def sec(s,label,block):
        i=s.index('aria-labelledby="%s"'%label); j=s.index('<div class="pg-wrap">',i)+len('<div class="pg-wrap">')
        e=s.index('    </div>\n  </section>',j)
        return s[:j]+'\n<div class="d-only">'+s[j:e]+'</div>\n    '+block+'\n'+s[e:]
    for lab,blk in (('who-title',M_WHO),('pillars-title',M_PILL),('hw-title',M_HOW),('team-title',M_TEAM)): s=sec(s,lab,blk)
    props=re.search(r"data-props='([^']*)'",s[s.index('<script type="text/x-dc"'):]).group(1)
    a=s.index('<script type="text/x-dc"'); b=s.index('</script>',a)+9
    s=s[:a]+SCRIPT%(props,repr(KEYS))+s[b:]
    s=s.replace('</style>\n</helmet>',CSS+'</style>\n</helmet>',1)
    s=s.replace('DM+Sans:wght@400;500;600;700','DM+Sans:wght@300;400;500;600;700')
    open(f,'w',encoding='utf-8').write(s)
print('about ok')
