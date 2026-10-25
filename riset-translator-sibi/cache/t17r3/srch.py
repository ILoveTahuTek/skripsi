import sys,re,subprocess,html
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
def fetch(u):
    return subprocess.run(["curl","-s","--max-time","30","-A",UA,u],capture_output=True,text=True,timeout=40).stdout
def bing(q):
    t=fetch("https://www.bing.com/search?q="+q.replace(' ','+')+"&count=10")
    items=re.findall(r'<h2><a href="([^"]+)"[^>]*>(.*?)</a></h2>',t,re.S)
    if not items:
        items=re.findall(r'<li class="b_algo".*?<a href="([^"]+)"[^>]*>(.*?)</a>',t,re.S)
    seen=0
    for href,ti in items:
        ti=re.sub(r'<[^>]+>','',ti)
        if 'bing.com' in href or 'microsoft' in href: continue
        print("-",html.unescape(ti.strip())[:130]); print("  ",href[:170]); seen+=1
        if seen>=7: break
    if seen==0: print("  (no results parsed, len=%d)"%len(t))
def ddg(q):
    t=fetch("https://html.duckduckgo.com/html/?q="+q.replace(' ','+'))
    items=re.findall(r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>',t,re.S)
    snips=re.findall(r'class="result__snippet"[^>]*>(.*?)</a>',t,re.S)
    for i,(href,ti) in enumerate(items[:6]):
        ti=re.sub(r'<[^>]+>','',ti); s=re.sub(r'<[^>]+>','',snips[i]) if i<len(snips) else ''
        print("-",html.unescape(ti.strip())[:130]); print("  ",html.unescape(href)[:170]); print("  ",html.unescape(s.strip())[:240])
    if not items: print("  (no results parsed, len=%d)"%len(t))
mode,q=sys.argv[1],sys.argv[2]
print("#### %s: %s"%(mode,q))
bing(q) if mode=="b" else ddg(q); print()
