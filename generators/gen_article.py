import re,json,sys
g=open('/home/claude/hero/gen_about.py').read()
exec(g.split("STATUS=''")[0])
CSS3=open('/home/claude/hero/gen_insights.py').read().split('CSS3=r"""')[1].split('"""')[0]
ab=open('/home/claude/hero/project/About.dc.html',encoding='utf-8').read()
head=ab[ab.index('<!-- Contact bar -->'):ab.index('<!-- Page hero -->')]
head=head.replace('<a class="cur" href="About.dc.html" aria-current="page">About Us</a>','<a href="About.dc.html">About Us</a>').replace('<a class="l cur" href="About.dc.html" aria-current="page">About Us</a>','<a class="l" href="About.dc.html">About Us</a>')
head=head.replace('<a href="Insights.dc.html">Insights</a>','<a class="cur" href="Insights.dc.html" aria-current="page">Insights</a>').replace('<a class="l" href="Insights.dc.html">Insights</a>','<a class="l cur" href="Insights.dc.html" aria-current="page">Insights</a>')
assert head.count('aria-current="page"')==2
fin=re.search(r'<svg class="pg-fin".*?</svg>',ab,flags=re.S).group(0)
FB='<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 22v-8.2h2.8l.5-3.3h-3.3V8.4c0-1 .4-1.7 1.8-1.7H17V3.8c-.3 0-1.3-.2-2.5-.2-2.6 0-4.3 1.6-4.3 4.4v2.5H7.4v3.3h2.8V22z"/></svg>'
XI='<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2H21.5l-7.1 8.12L22.75 22h-6.55l-5.12-6.7L5.2 22H1.94l7.6-8.68L1.5 2h6.7l4.63 6.12zm-1.14 18h1.8L7.2 3.9H5.27z"/></svg>'
CHK='<svg width="26" height="26" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="#94BBE4"/><path d="m7.5 12.3 3 3 6-6.3" stroke="#0E1F3D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CSS4=r"""
.h-root .at-hero .pg-hero-in{grid-template-columns:minmax(0,1fr);min-height:0}
.at-hero .pg-copy{padding:56px 0 64px;max-width:960px}
.at-date{display:inline-flex;align-items:center;gap:10px;margin-top:10px;font-size:16px;line-height:24px;font-weight:500;color:#C9DBF0}
.at-hero .pg-h1{font-size:60px;line-height:1.1;margin:14px 0 0;text-wrap:balance}
.at-sec{padding:80px 0 0;background:#ffffff}
.at-grid{display:grid;grid-template-columns:minmax(0,1fr) 720px minmax(0,1fr);column-gap:40px;align-items:start}
.at-rail{position:sticky;top:32px;justify-self:end;display:flex;flex-direction:column;gap:12px}
.at-ic{display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:50%;border:1.5px solid #C9DBF0;background:#ffffff;color:#1B4584;transition:background .2s ease,color .2s ease,border-color .2s ease}
.h-root a.at-ic:hover{background:#1B4584;border-color:#1B4584;color:#ffffff}
.at-art{grid-column:2;min-width:0}
.at-lead{margin:0;font-size:21px;line-height:1.7;color:#0E1F3D}
.at-art p{margin:0}
.at-art p + p,.at-art p + .at-q,.at-art .at-q + p,.at-art p + h2,.at-art h2 + p,.at-art p + ul{margin-top:28px}
.at-p{font-size:18px;line-height:1.8;color:#33445F}
.at-q{margin:44px 0 0;padding:6px 0 6px 28px;border-left:4px solid #94BBE4}
.at-q blockquote{margin:0;font-family:'Marcellus',Georgia,serif;font-size:30px;line-height:1.35;color:#0E1F3D}
.at-q figcaption{margin-top:18px;font-size:15px;line-height:1.5;font-weight:500;color:#33445F}
.at-art .at-q + p{margin-top:44px}
.at-h2{margin-top:52px !important;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:32px;line-height:1.2;color:#0E1F3D}
.h-root .at-list{display:flex;flex-direction:column;gap:14px;margin-top:28px}
.at-list li{display:flex;align-items:flex-start;gap:14px;font-size:18px;line-height:1.6;color:#0E1F3D}
.at-list li svg{flex:none;margin-top:1px}
.at-below{max-width:720px;margin:0 auto}
.at-share{display:flex;flex-wrap:wrap;gap:12px;margin-top:56px;padding-top:36px;border-top:1px solid #E1E8F2}
.h-root .at-pill{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:48px;padding:0 24px;border:1.5px solid #1B4584;border-radius:999px;background:#ffffff;color:#1B4584;font-size:16px;font-weight:600;text-decoration:none;transition:background .2s ease,color .2s ease}
.h-root .at-pill:hover{background:#1B4584;color:#ffffff}
.at-cm{padding:72px 0 88px}
.at-cm-h{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:36px;line-height:1.2;color:#0E1F3D}
.at-note{margin:14px 0 0;font-size:16px;line-height:1.6;color:#33445F}
.at-form{margin-top:32px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}
.at-f{display:flex;flex-direction:column;gap:8px}
.at-f.full{grid-column:1/-1}
.at-f label{font-size:16px;font-weight:600;color:#0E1F3D}
.at-f input[type=text],.at-f input[type=email],.at-f input[type=url]{width:100%;box-sizing:border-box;min-height:56px;padding:0 18px;border:1.5px solid #8798B2;border-radius:12px;background:#ffffff;color:#0E1F3D;font:inherit;font-size:17px;outline:none;transition:border-color .2s ease,box-shadow .2s ease}
.at-f input:focus{border-color:#0F74B5;box-shadow:0 0 0 3px #ffffff,0 0 0 6px #0F74B5}
.at-f label.at-ck{font-weight:400;display:flex;align-items:flex-start;gap:14px;font-size:16px;line-height:1.55;color:#33445F;cursor:pointer}
.at-ck input{flex:none;width:24px;height:24px;margin:0;accent-color:#1B4584;cursor:pointer}
.at-ck input:focus-visible{outline:3px solid #0F74B5;outline-offset:3px}
.at-f .at-submit{align-self:flex-start;display:inline-flex;align-items:center;justify-content:center;min-height:56px;padding:0 38px;border:0;border-radius:999px;background:#1B4584;color:#ffffff;font:inherit;font-size:17px;font-weight:600;cursor:pointer;transition:background .2s ease,transform .2s ease}
.at-submit:hover{background:#0E1F3D;transform:translateY(-2px)}
.at-submit:focus-visible{outline:3px solid #0F74B5;outline-offset:3px}
.at-more{padding:88px 0}
.h-root .at-more .in-list{margin-top:44px}
@media (max-width:1023px){
  .at-hero .pg-copy{padding:44px 0 52px}
  .at-hero .pg-h1{font-size:48px}
  .at-sec{padding:80px 0 0}
  .at-grid{grid-template-columns:minmax(0,1fr);max-width:720px;margin:0 auto}
  .at-rail{position:static;flex-direction:row;justify-self:start;margin-bottom:36px}
  .at-art{grid-column:1}
  .at-cm{padding:64px 0 72px}
  .at-more{padding:72px 0}
}
@media (max-width:640px){
  .at-hero .pg-copy{padding:32px 0 40px}
  .at-hero .pg-h1{font-size:34px;line-height:1.15}
  .at-date{font-size:16px}
  .at-sec{padding:56px 0 0}
  .at-rail{margin-bottom:28px}
  .at-ic{width:48px;height:48px}
  .at-lead{font-size:19px;line-height:1.65}
  .at-p,.at-list li{font-size:17px}
  .at-q{margin-top:36px;padding-left:20px}
  .at-q blockquote{font-size:23px}
  .at-art .at-q + p{margin-top:36px}
  .at-h2{font-size:26px;margin-top:40px !important}
  .at-share{flex-direction:row;gap:10px;margin-top:44px;padding-top:28px}
  .h-root .at-pill{flex:1 1 0;min-width:0;padding:0 10px;min-height:48px;font-size:15px}
  .at-cm{padding:48px 0 56px}
  .at-cm-h{font-size:30px}
  .at-form{grid-template-columns:minmax(0,1fr);gap:20px}
  .at-f input[type=text],.at-f input[type=email],.at-f input[type=url]{min-height:48px;font-size:16px}
  .at-f .at-submit{width:100%;align-self:stretch}
  .at-more{padding:56px 0}
  .h-root .at-more .in-list{margin-top:32px}
}
"""
POSTS={'ind':dict(t='Know about Industrial Laws',slug='know-about-industrial-laws',rel=('Flexibility of marriage in US','08993c385854a23fc1db4562a381fd00','ArticleMarriage.dc.html')),
'mar':dict(t='Flexibility of marriage in US',slug='flexibility-of-marriage-in-us',rel=('Know about Industrial Laws','5b4b94f7270eb91f66f1193f7dc7a478','Article.dc.html'))}
def build_a(name,title,w,h,pk='ind'):
    po=POSTS[pk]; PT=po['t']; RT,RB,RH=po['rel']
    U='https%3A%2F%2Fwww.aswlaw.africa%2Fnew%2Fblog_posts%2F'+po['slug']+'%2F'
    FBU='https://www.facebook.com/sharer/sharer.php?u='+U
    XU='https://x.com/intent/post?text=Hey%2C+check+out+this+cool+site+I+found%3A+www.yourname.com+%23Topic+via%40my_x_twitter_name&amp;url='+U
    P=lambda n:ic(n,18,2)
    body=f'''
<div class="h-root">

  {head}
  <!-- Article hero -->
  <section class="pg-hero at-hero" aria-labelledby="pg-title">
    {fin}
    <div class="pg-hero-in">
      <div class="pg-copy">
        <nav class="pg-crumb" aria-label="Breadcrumb"><ol><li><a href="Main.dc.html">Home</a><span aria-hidden="true">/</span></li><li><a href="Insights.dc.html">Insights</a><span aria-hidden="true">/</span></li><li><span aria-current="page">{PT}</span></li></ol></nav>
        <p class="at-date">{ic("calendar",18,1.8)}<time datetime="2025-06-24">June 24, 2025</time></p>
        <h1 class="pg-h1" id="pg-title">{PT}</h1>
      </div>
    </div>
  </section>

  <!-- Article -->
  <section class="at-sec" aria-label="Article">
    <div class="pg-wrap">
      <div class="at-grid">
        <div class="at-rail" role="group" aria-label="Share this article">
          <a class="at-ic" href="{FBU}" target="_blank" rel="noopener" aria-label="Share on Facebook">{FB}</a>
          <a class="at-ic" href="{XU}" target="_blank" rel="noopener" aria-label="Post on X">{XI}</a>
        </div>
        <article class="at-art">
          <p class="at-lead">Performance marketing may involve using various types of digital marketing and advertising channels, including the following Display ads include banner ads and other types of visual advertisements that display on websites your audience visits. These ads typically include a visual element with copy and link to a landing page where users may convert into leads or customers. Using online advertising platforms such as Google Ads, you can target your ads to users whose interests, demographics, or online activity matches.</p>
          <figure class="at-q"><blockquote><p>&ldquo;We know that when you hire a removal company you&rsquo;re putting your trust in the people that move your precious belongings.&rdquo;</p></blockquote><figcaption>Simon Pierro world-famous magician</figcaption></figure>
          <p class="at-p">When you create your videos, make sure you&rsquo;re effectively capturing your audience&rsquo;s attention and making them want to watch your content. Try telling a story or sharing an interesting fact to get your audience.</p>
          <h2 class="at-h2">Strategy for providing latest it solution</h2>
          <p class="at-p">Performance marketing may involve using various types of digital marketing and advertising channels, including the following Display ads include banner ads and other types of visual advertisements that display on websites your audience visits.</p>
          <ul class="at-list">
            <li>{CHK}<span>We help digital companies to volume their self-interest</span></li>
            <li>{CHK}<span>Recognized as a Leading Digital Marketing &amp; Web Design Agency</span></li>
            <li>{CHK}<span>Preparing for your success we provide truly Develop and Propose.</span></li>
            <li>{CHK}<span>A full-service web design and digital marketing</span></li>
          </ul>
          <p class="at-p" style="margin-top:28px">That it has a more-or-less normal distribution of letters, as opposed to using Content here, making it look like readable English and a search for will uncover many web sites still in their infancy.</p>
        </article>
      </div>
      <div class="at-below">
        <div class="at-share">
          <a class="at-pill" href="{FBU}" target="_blank" rel="noopener">{FB}<span>Share on Facebook</span></a>
          <a class="at-pill" href="{XU}" target="_blank" rel="noopener">{XI}<span>Post on X</span></a>
        </div>
        <section class="at-cm" aria-labelledby="cm-t">
          <h2 class="at-cm-h" id="cm-t">Leave a Reply</h2>
          <p class="at-note">Your email address will not be published. Required fields are marked *</p>
          <form class="at-form" action="#" method="post">
            <div class="at-f"><label for="cm-name">Name *</label><input id="cm-name" name="name" type="text" autocomplete="name" required aria-required="true"></div>
            <div class="at-f"><label for="cm-email">Email *</label><input id="cm-email" name="email" type="email" autocomplete="email" required aria-required="true"></div>
            <div class="at-f full"><label for="cm-web">Website</label><input id="cm-web" name="website" type="url" autocomplete="url"></div>
            <div class="at-f full"><label class="at-ck" for="cm-save"><input id="cm-save" name="save" type="checkbox"><span>Save my name, email, and website in this browser for the next time I comment.</span></label></div>
            <div class="at-f full"><button class="at-submit" type="submit">Post Comment</button></div>
          </form>
        </section>
      </div>
    </div>
  </section>

  <!-- More insights -->
  <section class="sec sec-o at-more" aria-labelledby="mr-t">
    <div class="pg-wrap">
      <h2 class="sec-h2" id="mr-t">Recent Blog Posts</h2>
      <ul class="in-list">
        <li><a class="in-card" href="{RH}"><img class="in-img" src="/_blob/{RB}" alt=""><span class="in-body"><span class="in-date">{ic("calendar",16,1.8)}<span>June 24, 2025</span></span><h3 class="in-title">{RT}</h3><span class="in-more"><span>Read More</span>{ic("arrow",18,2)}</span></span></a></li>
      </ul>
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
{BASE_CSS}{PAGE_CSS}{FOOT_CSS}{CSS3}{CSS4}</style>
</helmet>
{body}</x-dc>
{script}
</body>
</html>
'''
    html=html.replace('{{{{','{{').replace('}}}}','}}')
    open('/home/claude/hero/project/%s.dc.html'%name,'w',encoding='utf-8').write(html)
H=json.loads(sys.argv[1]) if len(sys.argv)>1 else [3755,3965,4610]
build_a('Article','Article: Know about Industrial Laws',1440,H[0])
build_a('ArticleTablet','Article: Tablet 768',768,H[1])
build_a('ArticlePhone','Article: Phone 390',390,H[2])
build_a('ArticleMarriage','Article: Flexibility of marriage in US',1440,H[0],'mar')
build_a('ArticleMarriageTablet','Article (marriage): Tablet 768',768,H[1],'mar')
build_a('ArticleMarriagePhone','Article (marriage): Phone 390',390,H[2],'mar')
print('ok')
