import re,json,sys
g=open('/home/claude/hero/gen_about.py').read()
exec(g.split("STATUS=''")[0])
ab=open('/home/claude/hero/project/About.dc.html',encoding='utf-8').read()
head=ab[ab.index('<!-- Contact bar -->'):ab.index('<!-- Page hero -->')]
head=head.replace('<a class="cur" href="About.dc.html" aria-current="page">About Us</a>','<a href="About.dc.html">About Us</a>').replace('<a class="l cur" href="About.dc.html" aria-current="page">About Us</a>','<a class="l" href="About.dc.html">About Us</a>')
head=head.replace('<a href="Contact.dc.html">Contact Us</a>','<a class="cur" href="Contact.dc.html" aria-current="page">Contact Us</a>').replace('<a class="l" href="Contact.dc.html">Contact Us</a>','<a class="l cur" href="Contact.dc.html" aria-current="page">Contact Us</a>')
assert head.count('aria-current="page"')==2
hero=ab[ab.index('<!-- Page hero -->'):ab.index('<!-- Who we are -->')]
hero=hero.replace('<span aria-current="page">About Us</span>','<span aria-current="page">Contact Us</span>').replace('id="pg-title">About Us<','id="pg-title">Contact Us<')
assert 'Contact Us</h1>' in hero
WA='<svg width="22" height="22" viewBox="0 0 24 24" fill="#25D366" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'
MAPB='/_blob/540d4e0a1684baf335b9225e8f4580e4'
LOGOL='/_blob/34f125cf125583676cd7f972966a287a'
ADDR='Tourism Fund Building, Mezzanine Floor, Office M08, Off-Bishop Rd, Community Area, Nairobi, Kenya'
FORMCSS=r"""
.ct-card{background:#ffffff;border:1px solid #E6ECF4;border-radius:20px;box-shadow:0 14px 40px rgba(14,31,61,.08);padding:40px}
.ct-form{display:flex;flex-direction:column;gap:22px}
.ct-f{display:flex;flex-direction:column;gap:8px}
.ct-f label{font-size:16px;line-height:22px;font-weight:600;color:#0E1F3D}
.ct-in{width:100%;box-sizing:border-box;min-height:52px;padding:0 18px;border:1.5px solid #8798B2;border-radius:12px;background:#ffffff;color:#0E1F3D;font-family:'DM Sans',sans-serif;font-size:17px;outline:none;transition:border-color .2s ease,box-shadow .2s ease}
textarea.ct-in{min-height:180px;padding:14px 18px;line-height:1.55;resize:vertical}
.ct-in:focus{border-color:#0F74B5;box-shadow:0 0 0 3px #ffffff,0 0 0 6px #0F74B5}
.ct-in:user-invalid,.ct-f.is-err .ct-in{border-color:#B93815;box-shadow:0 0 0 1px #B93815}
.ct-err{display:none;margin:0;font-size:15px;line-height:20px;font-weight:500;color:#B93815}
.ct-in:user-invalid ~ .ct-err,.ct-f.is-err .ct-err{display:block}
.ct-submit{align-self:flex-start;display:inline-flex;align-items:center;justify-content:center;min-height:56px;padding:0 44px;border:0;border-radius:999px;background:#1B4584;color:#ffffff;font-family:'DM Sans',sans-serif;font-size:17px;font-weight:600;cursor:pointer;transition:background .2s ease,transform .2s ease}
.ct-submit:hover{background:#0E1F3D;transform:translateY(-2px)}
.ct-submit:focus-visible{outline:3px solid #0F74B5;outline-offset:3px}
.ct-ok{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px;text-align:center;min-height:420px}
.ct-ok-ic{display:inline-flex;align-items:center;justify-content:center;width:72px;height:72px;border-radius:50%;border:1.5px solid #C9DBF0;color:#1B4584}
.ct-ph{margin:0;font-size:18px;line-height:1.6;color:#2A3A55}
"""
CSS5=FORMCSS+r"""
.ct-cards{position:relative;z-index:5;margin-top:-50px;padding-bottom:80px;background:linear-gradient(to bottom,transparent 50px,#ffffff 50px)}
.h-root .ct-cl{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px}
.ct-c{display:flex;flex-direction:column;align-items:flex-start;gap:18px;height:100%;box-sizing:border-box;padding:30px 28px;background:#ffffff;border:1px solid #E6ECF4;border-radius:20px;box-shadow:0 18px 44px rgba(14,31,61,.12)}
.ct-ic{display:inline-flex;align-items:center;justify-content:center;flex:none;width:56px;height:56px;border-radius:50%;border:1.5px solid #C9DBF0;background:#ffffff;color:#1B4584}
.ct-lab{display:block;font-size:13px;line-height:16px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#0B66A0}
.ct-val{display:block;margin-top:8px;font-size:17px;line-height:1.55;color:#0E1F3D;text-decoration:none}
.h-root a.ct-val{display:inline-flex;align-items:center;min-height:44px;margin-top:0;font-size:18px;font-weight:600;color:#0E1F3D;border-bottom:1px solid transparent;transition:color .2s ease}
.h-root a.ct-val:hover{color:#0F74B5}
.ct-form-sec{padding:96px 0}
.ct-sub{margin:20px 0 0;font-size:18px;line-height:1.6;color:#33445F}
.ct-grid{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,2fr);gap:32px;align-items:stretch;margin-top:48px}
.ct-panel{position:relative;overflow:hidden;isolation:isolate;display:flex;flex-direction:column;align-items:flex-start;padding:44px 40px;border-radius:20px;background:linear-gradient(160deg,#0E1F3D 0%,#14305F 100%);color:#ffffff}
.ct-panel::before{content:"";position:absolute;right:-120px;bottom:-160px;width:420px;height:420px;border-radius:50%;border:1.5px solid rgba(148,187,228,.22);z-index:-1;box-shadow:0 0 0 48px rgba(148,187,228,.05)}
.ct-logo{display:block;height:104px;width:auto}
.ct-tag{margin:24px 0 0;font-family:'Marcellus',Georgia,serif;font-size:26px;line-height:1.3;color:#ffffff;max-width:320px}
.ct-acts{display:flex;flex-direction:column;gap:14px;width:100%;margin-top:auto;padding-top:36px}
.h-root .ct-act{display:inline-flex;align-items:center;justify-content:center;gap:12px;min-height:52px;padding:0 24px;border-radius:999px;font-size:17px;font-weight:600;text-decoration:none;border:1.5px solid transparent;transition:background .2s ease,color .2s ease,border-color .2s ease}
.h-root .ct-call{background:#94BBE4;color:#0E1F3D}
.h-root .ct-call:hover{background:#ffffff}
.h-root .ct-mail{background:transparent;color:#ffffff;border-color:rgba(255,255,255,.6)}
.h-root .ct-mail:hover{background:#ffffff;color:#0E1F3D;border-color:#ffffff}
.h-root .ct-wa{background:#ffffff;color:#0E1F3D}
.h-root .ct-wa:hover{background:#E6F7EE}
.ct-map{padding:96px 0 0}
.mp-frame{position:relative;aspect-ratio:3/1;border-radius:20px;overflow:hidden;background:#E6ECF4;box-shadow:0 18px 44px rgba(14,31,61,.12)}
.mp-img{position:absolute;display:block;width:200%;max-width:none;left:50%;top:50%;transform:translate(-49.9%,-46.3%)}
.h-root .mp-btn{position:absolute;left:24px;bottom:24px;display:inline-flex;align-items:center;gap:10px;min-height:48px;padding:0 22px;border-radius:999px;background:#ffffff;color:#0E1F3D;font-size:16px;font-weight:600;text-decoration:none;box-shadow:0 8px 24px rgba(14,31,61,.22);transition:background .2s ease,color .2s ease}
.h-root .mp-btn:hover{background:#0E1F3D;color:#ffffff}
.mp-cap{display:flex;align-items:flex-start;gap:12px;margin:22px 0 0;font-size:16px;line-height:1.6;color:#33445F}
.mp-cap svg{flex:none;margin-top:2px;color:#1B4584}
.ct-end{height:96px}
@media (max-width:1023px){
  .h-root .ct-cl{grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
  .ct-form-sec{padding:80px 0}
  .ct-grid{grid-template-columns:minmax(0,1fr);gap:24px;margin-top:40px}
  .ct-panel{padding:40px 36px}
  .ct-acts{margin-top:0}
  .ct-map{padding-top:80px}
  .mp-frame{aspect-ratio:16/7}
  .ct-end{height:80px}
}
@media (max-width:640px){
  .pg-hero .pg-copy{padding-top:2px}
  .ct-cards{padding-bottom:56px}
  .h-root .ct-cl{grid-template-columns:minmax(0,1fr);gap:14px}
  .ct-c{flex-direction:row;align-items:center;gap:16px;min-height:72px;padding:16px 18px;border-radius:18px}
  .ct-ic{width:48px;height:48px}
  .ct-lab{font-size:14px}
  .ct-val{font-size:16px;margin-top:4px}
  .h-root a.ct-val{font-size:17px}
  .ct-form-sec{padding:56px 0}
  .ct-sub{font-size:17px;margin-top:16px}
  .ct-grid{margin-top:32px}
  .ct-card{padding:24px 20px}
  .ct-in{font-size:16px}
  .ct-submit{width:100%;align-self:stretch}
  .ct-panel{padding:32px 24px}
  .ct-logo{height:88px}
  .ct-tag{font-size:23px}
  .ct-acts{padding-top:28px}
  .h-root .ct-act{min-height:48px;width:100%}
  .ct-map{padding-top:56px}
  .mp-frame{aspect-ratio:4/3;border-radius:16px}
  .mp-img{width:300%}
  .h-root .mp-btn{left:14px;bottom:14px;min-height:44px;padding:0 18px}
  .ct-end{height:56px}
}
"""
def field(i,lab,typ='text',req=True,err=False,ta=False,auto=''):
    cls=' is-err' if err else ''
    r=' required aria-required="true"' if req else ''
    a=f' autocomplete="{auto}"' if auto else ''
    ctl=f'<textarea class="ct-in" id="{i}" name="{i}" rows="6"></textarea>' if ta else f'<input class="ct-in" id="{i}" name="{i}" type="{typ}"{r}{a}{" aria-invalid=\"true\" aria-describedby=\""+i+"-e\"" if err else ""}>'
    e='' if ta else f'<p class="ct-err" id="{i}-e">This field is required</p>'
    return f'<div class="ct-f{cls}"><label for="{i}">{lab}</label>{ctl}{e}</div>'
def form(err=()):
    return ('<form class="ct-form" action="#" method="post" novalidate>'+field('ct-name','Your name',auto='name',err='name' in err)+field('ct-email','Your email','email',auto='email',err='email' in err)+field('ct-subj','Subject',err='subj' in err)+field('ct-msg','Your message (optional)',req=False,ta=True)+'<button class="ct-submit" type="submit">Submit</button></form>').replace(' novalidate','')
def page(name,title,w,h):
    cards=''.join(f'<li class="rv"><div class="ct-c"><span class="ct-ic">{ic(i,24,1.6)}</span><div><span class="ct-lab">{l}</span>{v}</div></div></li>' for i,l,v in (
      ("phone","Phone",'<a class="ct-val" href="tel:+254788685911">+254 788 685 911</a>'),
      ("mail","Email",'<a class="ct-val" href="mailto:info@aswlaw.africa">info@aswlaw.africa</a>'),
      ("pin","Address",f'<span class="ct-val">{ADDR}</span>'),
      ("clock","Hours",'<span class="ct-val">Mon to Fri: 9.00am to 5.00pm</span>')))
    body=f'''
<div class="h-root">

  {head}
{hero}
  <!-- Contact cards -->
  <section class="ct-cards" aria-label="Contact details">
    <div class="pg-wrap">
      <ul class="ct-cl">{cards}</ul>
    </div>
  </section>

  <!-- Message form -->
  <section class="sec sec-o ct-form-sec" aria-labelledby="ct-t">
    <div class="pg-wrap">
      <h2 class="sec-h2" id="ct-t">Send Us a Message</h2>
      <p class="ct-sub">ASW Law Advocates LLP</p>
      <div class="ct-grid">
        <div class="ct-card rv">{form()}</div>
        <aside class="ct-panel rv" aria-label="Contact options">
          <img class="ct-logo" src="{LOGOL}" alt="ASW Law Advocates LLP">
          <p class="ct-tag">We offer world-class legal representation.</p>
          <div class="ct-acts">
            <a class="ct-act ct-call" href="tel:+254788685911">{ic("phone",20,1.8)}<span>Call us</span></a>
            <a class="ct-act ct-mail" href="mailto:info@aswlaw.africa">{ic("mail",20,1.8)}<span>Email us</span></a>
            <a class="ct-act ct-wa" href="https://wa.me/254788685911" target="_blank" rel="noopener">{WA}<span>WhatsApp</span></a>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <!-- Map -->
  <section class="sec-w ct-map" aria-label="Map">
    <div class="pg-wrap">
      <div class="mp-frame">
        <img class="mp-img" src="{MAPB}" alt="Map of Nairobi with a pin at the Tourism Fund building on Valley Road">
        <a class="mp-btn" href="https://www.google.com/maps/search/?api=1&amp;query=Tourism+Fund+Building+Off-Bishop+Rd+Nairobi+Kenya" target="_blank" rel="noopener"><span>Open in Maps</span>{ic("arrowur",18,2)}</a>
      </div>
      <p class="mp-cap">{ic("pin",20,1.7)}<span>{ADDR}</span></p>
      <div class="ct-end"></div>
    </div>
  </section>

{foot_html(ic,False,True)}
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
    out=f'''<!doctype html>
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
{BASE_CSS}{PAGE_CSS}{FOOT_CSS}{CSS5}</style>
</helmet>
{body}</x-dc>
{script}
</body>
</html>
'''
    out=out.replace('{{{{','{{').replace('}}}}','}}')
    open('/home/claude/hero/project/%s.dc.html'%name,'w',encoding='utf-8').write(out)
def states(h=760):
    check=ic("checkc",36,1.5)
    body=f'''
<div class="st-root">
  <div class="st-col"><p class="st-cap">Form card: error state</p><div class="ct-card">{form(('name','email'))}</div></div>
  <div class="st-col"><p class="st-cap">Form card: success state</p><div class="ct-card"><div class="ct-ok" role="status"><span class="ct-ok-ic">{check}</span><p class="ct-ph ct-okt">Thank you for contacting ASW Law Advocates LLP. We have received your message and will respond as soon as possible.</p></div></div></div>
</div>
'''
    css=r"""
body{margin:0}
.st-root{box-sizing:border-box;width:1080px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:40px;align-items:stretch;padding:48px;background:#F2F2F0;font-family:'DM Sans',sans-serif}
.st-col{display:flex;flex-direction:column;gap:14px}
.st-col .ct-card{flex:1}
.st-cap{margin:0;font-size:15px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#0B66A0}
"""
    script='''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1080,"height":%d}}'>
class Component extends DCLogic {
  renderVals() { return {}; }
}
</script>''' % h
    out=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Contact: Form states</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Marcellus&display=swap" rel="stylesheet">
<style>
{css}{FORMCSS}</style>
</helmet>
{body}</x-dc>
{script}
</body>
</html>
'''
    open('/home/claude/hero/project/ContactFormStates.dc.html','w',encoding='utf-8').write(out)
H=json.loads(sys.argv[1]) if len(sys.argv)>1 else [3000,3600,3600,760]
page('Contact','Contact Us: ASW Law Advocates LLP',1440,H[0])
page('ContactTablet','Contact Us: Tablet 768',768,H[1])
page('ContactPhone','Contact Us: Phone 390',390,H[2])
states(H[3])
print('ok')
