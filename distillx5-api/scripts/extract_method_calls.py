import re,glob,json

def norm_url(url):
    s=url.strip().strip('`"\'')
    s=s.replace('${D}/', 'api/').replace('${D}', 'api')
    s=re.sub(r'\$\{t\}', '', s)
    s=re.sub(r'\$\{j\}', '', s)
    s=re.sub(r'\$\{c\.value\}', 'api', s)
    s=re.sub(r'\$\{e\.apiUri\}', 'api', s)
    s=re.sub(r'\$\{g\.value\}', 'api/clients/db-backups/backups/', s)
    s=re.sub(r'\$\{p\}', 'api/containers/overview', s)
    s=re.sub(r'\$\{[^}]*\}', '{id}', s)
    s=s.strip()
    s=re.sub(r'^\$\{[^}]*\}', '', s)
    path=s
    if '?' in s:
        path=s.split('?',1)[0]
    path=re.sub(r'/{2,}', '/', path)
    if len(path)>1 and path.endswith('/'):
        path=path.rstrip('/')
    return path

pats = [
 (r"Ajax\.(get|post)\s*\(\s*('([^']*)'|\"([^\"]*)\")", None),
 (r"wt\.(get|post|put|patch|delete)\s*\(\s*(`([^`]*)`|'([^']*)'|\"([^\"]*)\")", None),
 (r"o\.a\.(get|post|put|patch|delete)\s*\(\s*(`([^`]*)`|'([^']*)'|\"([^\"]*)\")", None),
 (r"\bfetch\s*\(\s*(`([^`]*)`|'([^']*)'|\"([^\"]*)\")", 'GET'),
 (r"\$\.(get|post)\s*\(\s*(?:G_URI_BASE\s*\+\s*)?(`([^`]*)`|'([^']*)'|\"([^\"]*)\")", None),
]
method_map={}
for f in glob.glob('artifacts/bundles/*.js'):
    s=open(f).read()
    for pat, fixed in pats:
        for m in re.finditer(pat,s):
            groups=[g for g in m.groups() if g is not None]
            if fixed:
                method=fixed
                url=groups[0]
            else:
                method=groups[0].upper()
                # url is first group after method that contains path
                url=None
                for g in groups[1:]:
                    if '/' in g or g in ('messages',):
                        url=g; break
                if not url:
                    url=groups[-1]
            path=norm_url(url)
            if not path or ' ' in path:
                continue
            method_map.setdefault(path,set()).add(method)

# collapse to unique if single
mm={k:(list(v)[0] if len(v)==1 else sorted(v)) for k,v in method_map.items()}
json.dump(mm, open('artifacts/analysis/method-map.json','w'), indent=2)
print(len(mm))
for k,v in sorted(mm.items()):
    print(v,k)
