import sys,re,urllib.parse,subprocess,html
def ddg(q):
    u="https://html.duckduckgo.com/html/?q="+urllib.parse.quote(q)
    try:
        t=subprocess.run(["curl","-s","--max-time","30","-A","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",u],capture_output=True,text=True,timeout=40).stdout
    except Exception as e:
        print("ERR",e);return
    if "result__a" not in t:
        u2="https://lite.duckduckgo.com/lite/?q="+urllib.parse.quote(q)
        t=subprocess.run(["curl","-s","--max-time","30","-A","Mozilla/5.0",u2],capture_output=True,text=True,timeout=40).stdout
        links=re.findall(r'<a[^>]+href="([^"]+)"[^>]*class="result-link"[^>]*>(.*?)</a>',t,re.S)
        if not links: links=re.findall(r'<a[^>]+class="result-link"[^>]+href="([^"]+)"[^>]*>(.*?)</a>',t,re.S)
        snips=re.findall(r'class="result-snippet"[^>]*>(.*?)</td>',t,re.S)
        for i,(href,ti) in enumerate(links[:6]):
            ti=re.sub(r'<[^>]+>','',ti); s=re.sub(r'<[^>]+>','',snips[i]) if i<len(snips) else ''
            print("-",html.unescape(ti.strip())[:120]);print("  ",html.unescape(href)[:160]);print("  ",html.unescape(s.strip())[:280])
        return
    items=re.findall(r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>',t,re.S)
    snips=re.findall(r'class="result__snippet"[^>]*>(.*?)</a>',t,re.S)
    for i,(href,ti) in enumerate(items[:6]):
        ti=re.sub(r'<[^>]+>','',ti); s=re.sub(r'<[^>]+>','',snips[i]) if i<len(snips) else ''
        print("-",html.unescape(ti.strip())[:120]);print("  ",html.unescape(href)[:170]);print("  ",html.unescape(s.strip())[:280])
for q in sys.argv[1:]:
    print("#### QUERY:",q)
    ddg(q); print()
