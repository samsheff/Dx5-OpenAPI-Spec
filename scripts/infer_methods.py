import re,glob
# Build occurrence context method inference for each raw path string
raws=open('artifacts/analysis/all-path-strings.txt').read().splitlines()
ctx_method={}
for raw in raws:
    ctx_method[raw]=set()
    for f in glob.glob('artifacts/bundles/*.js'):
        s=open(f).read()
        for m in re.finditer(re.escape(raw), s):
            start=max(0,m.start()-60)
            ctx=s[start:m.start()].lower()
            if 'post' in ctx or 'submit' in ctx:
                ctx_method[raw].add('POST')
            if 'get' in ctx or 'ajax.get' in ctx:
                ctx_method[raw].add('GET')
            if 'fetch' in ctx:
                ctx_method[raw].add('GET')
print({k:v for k,v in ctx_method.items() if len(v)>1})  # conflicts
