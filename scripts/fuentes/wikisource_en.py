# Descarga el texto de una página de Wikisource en inglés; si es página de versiones o índice, sigue los enlaces
import sys,json,time,urllib.parse,subprocess,re,html
UA="GabineteEditorialBot/1.0 (https://elgabinetenegro.com)"
def api(params):
    u='https://en.wikisource.org/w/api.php?'+urllib.parse.urlencode({**params,'format':'json','redirects':1})
    for k in range(6):
        r=subprocess.run(['curl','-s','-m','40','-A',UA,u],capture_output=True,text=True).stdout
        try: return json.loads(r)
        except Exception: time.sleep(15)
def parse(title):
    d=api({'action':'parse','page':title,'prop':'text|links'}); time.sleep(2)
    if not d or 'error' in d: return None,[]
    return d['parse']['text']['*'],[l['*'] for l in d['parse']['links'] if l['ns']==0]
def paras(h):
    h=re.sub(r'<style.*?</style>','',h,flags=re.S); h=re.sub(r'<sup.*?</sup>','',h,flags=re.S)
    h=re.sub(r'<span[^>]*class="pagenum[^"]*"[^>]*>.*?</span>','',h,flags=re.S)
    h=re.sub(r'<div[^>]*(ws-noexport|headertemplate|wst-header|licenseContainer|footer)[^>]*>.*?</div>','',h,flags=re.S)
    out=[]
    for tag,x in re.findall(r'<(p|h2|h3|h4|center|dd)[^>]*>(.*?)</\1>',h,flags=re.S):
        x=re.sub(r'<br\s*/?>',' ',x); x=re.sub(r'</?(i|em)>','*',x); x=re.sub(r'</?(b|strong)>','',x)
        x=re.sub(r'<[^>]+>','',x); x=html.unescape(x); x=re.sub(r'\s+',' ',x).strip().replace('**','')
        if x: out.append((tag,x))
    return out
title,out=sys.argv[1],sys.argv[2]
h,links=parse(title); ps=paras(h) if h else []
w=sum(len(x.split()) for _,x in ps)
if w<800:   # página de versiones / índice: elegir el enlace más largo
    cands=[l for l in links if l.startswith(title.split('/')[0]) or title.split(' (')[0] in l][:8]
    best=(0,None,None)
    for c in cands:
        hh,_=parse(c)
        if not hh: continue
        pp=paras(hh); ww=sum(len(x.split()) for _,x in pp)
        if ww>best[0]: best=(ww,c,pp)
    if best[1]: w,title,ps=best
open(out,'w').write(json.dumps({'title':title,'paras':ps},ensure_ascii=False))
print(f'{w:6d} palabras  {title}')
