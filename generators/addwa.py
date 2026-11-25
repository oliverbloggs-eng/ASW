import glob,re
CSS="""
.wa-w{display:none}
@keyframes wa-in{from{opacity:0;pointer-events:none}to{opacity:1;pointer-events:auto}}
@media (max-width:640px){
  .wa-w{position:sticky;bottom:0;height:0;display:flex;justify-content:flex-end;padding-right:16px;z-index:60}
  .wa-b{display:flex;align-items:center;justify-content:center;width:48px;height:48px;margin-top:-68px;border-radius:9999px;background:#25d366;box-shadow:0 8px 24px rgba(14,31,61,.28)}
  @supports (animation-timeline:scroll()){.wa-w{animation:wa-in linear both;animation-timeline:scroll(root);animation-range:%s}}
  @supports (animation-timeline:--ctl){.h-root{timeline-scope:--ctl,--tctl}.wa-b{animation:wa-hide linear,wa-hide linear;animation-timeline:--ctl,--tctl;animation-range:cover 0% cover 100%,cover 0% cover 100%}}
}
@keyframes wa-hide{0%{opacity:1}6%{opacity:0;pointer-events:none}94%{opacity:0;pointer-events:none}100%{opacity:1}}
"""
HTML='''
  <!-- WhatsApp (mobile only, appears after the hero) -->
  <div class="wa-w">
    <a class="wa-b" href="https://wa.me/254788685911" target="_blank" rel="noopener" aria-label="Chat with ASW Law Advocates on WhatsApp">
      <svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21l1.65-4.9A8.5 8.5 0 1 1 8 19.4L3 21z"/><path d="M9 8.6c.2 2.7 2.6 5.4 5.6 5.9l1.2-1.3c.2-.2.5-.3.8-.2l1.5.6c.3.1.5.4.4.7-.4 1.2-1.6 1.9-2.8 1.8-3.8-.4-7-3.5-7.4-7.2-.1-1.2.6-2.3 1.8-2.6.3-.1.6.1.7.4l.6 1.5c.1.3 0 .6-.2.8"/></svg>
    </a>
  </div>
'''
SKIP=re.compile(r'/(Main|Book|Footer|Header|HeroDesktop|HeroTablet|ContactFormStates)\.dc\.html$')
for f in glob.glob('/home/claude/hero/project/*.dc.html'):
    if SKIP.search(f): continue
    s=open(f,encoding='utf-8').read()
    if 'wa-w' in s: continue
    rng='620px 880px' if 'HeroPhone' in f else '260px 380px'
    i=s.rindex('</div>\n</x-dc>')
    s=s[:i]+HTML+s[i:]
    s=s.replace('</style>\n</helmet>',CSS%rng+'</style>\n</helmet>',1)
    open(f,'w',encoding='utf-8').write(s)
