import json,re,subprocess,sys
h=json.load(open('/home/claude/hero/heights6.json'))
def run(*a): subprocess.run(['python3',*a],cwd='/home/claude/hero',capture_output=True)
def sub(f,pairs):
    s=open('/home/claude/hero/'+f).read()
    for pat,val in pairs: s=re.sub(pat,lambda m:m.group(1)+str(val)+m.group(2),s,count=1)
    open('/home/claude/hero/'+f,'w').write(s)
def gen():
    sub('gen_about.py',[(r"(LLP',1440,)\d+(\))",h['About']),(r"(Tablet 768',768,)\d+(\))",h['AboutTablet']),(r"(Phone 390',390,)\d+(\))",h['AboutPhone'])])
    sub('gen_areas.py',[(r"(LLP',1440,)\d+(\))",h['Areas']),(r"(Tablet 768',768,)\d+(\))",h['AreasTablet']),(r"(Phone 390',390,)\d+(\))",h['AreasPhone'])])
    sub('gen.py',[(r"(Desktop 1440\",1440,)\d+(\))",h['HeroDesktop']),(r"(Tablet 768\",768,)\d+(\))",h['HeroTablet']),(r"(Phone 390\",390,)\d+(\))",h['HeroPhone']),(r'(replace\("@@H@@","?)\d+("?\))',h['Main'])])
    for a in (['gen.py'],['gen_about.py'],['gen_areas.py'],['gen_insights.py',json.dumps([h['Insights'],h['InsightsTablet'],h['InsightsPhone']])],['gen_article.py',json.dumps([h['Article'],h['ArticleTablet'],h['ArticlePhone']])],['gen_contact.py',json.dumps([h['Contact'],h['ContactTablet'],h['ContactPhone'],880])],['gen_faq.py',json.dumps([h['FAQ'],h['FAQTablet'],h['FAQPhone']])]): run(*a)
    run('addwa.py'); run('addtype.py'); run('addclean.py'); run('addfoot.py'); run('addabout.py')
gen()
run('measure.py')
m=json.load(open('/home/claude/hero/heights.json'))
h={k:v[0]+6 for k,v in m.items()}
print({k:v[1] for k,v in m.items() if v[1]!=int(re.search(r'\d+',k and '0').group())+0 and False})
json.dump(h,open('/home/claude/hero/heights6.json','w'))
gen()
print('overflow',[k for k,v in m.items() if v[1]>{'D':1440}.get('D') or (('Phone' in k) and v[1]>390) or (('Tablet' in k) and v[1]>768)])
