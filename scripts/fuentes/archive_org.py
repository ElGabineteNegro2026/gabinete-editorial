"""archive.org vía /stream (las descargas directas van a nodos dn*.archive.org bloqueados).
uso: ia.py search "<query>"   |   ia.py get <identifier> <outfile> [nombre_fichero]"""
import sys, json, re, html, subprocess, urllib.parse, time
def curl(u):
    for k in range(4):
        r = subprocess.run(['curl','-s','-m','60',u],capture_output=True,text=True)
        if r.returncode==0 and r.stdout: return r.stdout
        time.sleep(5)
    return ''
if sys.argv[1]=='search':
    q=urllib.parse.urlencode({'q':sys.argv[2],'fl[]':['identifier','title','creator','date'],'rows':30,'output':'json'},doseq=True)
    for d in json.loads(curl('https://archive.org/advancedsearch.php?'+q))['response']['docs']:
        print(d['identifier'],'|',d.get('title'),'|',d.get('creator'),'|',d.get('date'))
else:
    ident,out=sys.argv[2],sys.argv[3]
    fn=sys.argv[4] if len(sys.argv)>4 else None
    if not fn:
        fs=json.loads(curl(f'https://archive.org/metadata/{ident}/files'))['result']
        txt=[f['name'] for f in fs if f['name'].endswith('.txt') and not f['name'].endswith('_meta.txt')]
        pref=[n for n in txt if n.endswith('-0.txt')]+[n for n in txt if re.search(r'\d\.txt$',n) and '-8' not in n]+[n for n in txt if n.endswith('-8.txt')]+[n for n in txt if n.endswith('_djvu.txt')]+txt
        fn=pref[0]
    h=curl(f'https://archive.org/stream/{ident}/{urllib.parse.quote(fn)}')
    m=re.search(r'<pre[^>]*>(.*?)</pre>',h,re.S)
    t=html.unescape(m.group(1)) if m else ''
    open(out,'w').write(t); print(ident,fn,len(t.split()),'palabras')
