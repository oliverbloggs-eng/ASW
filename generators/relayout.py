import json,re,glob
h=json.load(open('/home/claude/hero/heights6.json'))
c=json.load(open('/home/claude/hero/project/canvas.json'));B=c['boards'];N=c['notes']
for k,v in h.items():
    if k+'.dc.html' in B: B[k+'.dc.html']['h']=v
B['Insights.dc.html']['y']=h['Main']+160
B['Header.dc.html']['y']=B['Insights.dc.html']['y']+h['Insights']+160
hy=B['Header.dc.html']['y']+124+400
for k in('HeroDesktop','HeroTablet','HeroPhone'): B[k+'.dc.html']['y']=hy
N['t2']['y']=hy-230
ay=hy+max(h['HeroDesktop'],h['HeroTablet'],h['HeroPhone'])+500
N['t3']['y']=ay-240
for k in('About','AboutTablet','AboutPhone'): B[k+'.dc.html']['y']=ay
N['t4']['y']=ay+2300
N['t10']['y']=ay+1100
N['t9']['y']=hy+3215+60
cy=ay+max(h['About'],h['AboutTablet'],h['AboutPhone'])+500
N['t5']['y']=cy-250
for k in('Contact','ContactTablet','ContactPhone','ContactFormStates'): B[k+'.dc.html']['y']=cy
N['t6']['y']=cy+1700
fy=cy+max(h['Contact'],h['ContactTablet'],h['ContactPhone'])+500
N['t8']['y']=fy-250
for k in('FAQ','FAQTablet','FAQPhone'): B[k+'.dc.html']['y']=fy
for k,b in B.items():
    N['s_'+k]={'x':b['x'],'y':b['y']-110,'w':min(b['w'],340),'text':'Sample copy for review, to be confirmed by the firm.','fill':'orange','size':'s'}
bl=[(k,b['x'],b['y'],b['w'],b['h']) for k,b in B.items()]
print('overlaps',[(a[0],b[0]) for i,a in enumerate(bl) for b in bl[i+1:] if a[1]<b[1]+b[3] and b[1]<a[1]+a[3] and a[2]<b[2]+b[4] and b[2]<a[2]+a[4]])
json.dump(c,open('/home/claude/hero/project/canvas.json','w'),indent=1)
bad=0
for f in glob.glob('/home/claude/hero/project/*.dc.html')+['/home/claude/hero/project/canvas.json']:
    s=open(f,encoding='utf-8').read(); s=re.sub(r'<style.*?</style>|<script.*?</script>|<!--.*?-->','',s,flags=re.S)
    bad+=len(re.findall(r'[–—]|\s-\s|&[nm]dash;',s))
print('dash',bad)
