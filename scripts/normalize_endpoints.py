import re,json
method_map=json.load(open('artifacts/analysis/method-map.json'))

# Load plain strings
plain=open('artifacts/analysis/all-path-strings.txt').read().splitlines()
# Also method-call raw? We'll just use plain strings + a method inference.
# But we need method-call methods for some. We'll create method map from known calls.
method_map = {
 # v1
}
# Infer method
MUTATION_KEYWORDS = ['add','edit','deactivate','delete','create','update','upload','receive','transfer','charge','dump','end','fire','recal','switch','withdraw','run','fill','package','adjust','generate','change-status','cancel','ship','undo','approve','processupload','recal','metrics','save']
def infer_method(path):
    low=path.lower()
    for kw in MUTATION_KEYWORDS:
        if kw in low:
            return 'POST'
    return 'GET'

# Known base replacements
def normalize_raw(raw):
    # remove surrounding quotes/backticks
    s=raw.strip().strip('`"\'')
    # base var replacements
    s=s.replace('${D}/', 'api/').replace('${D}', 'api')
    s=s.replace('${j}', '')
    # standalone ${t} base
    s=re.sub(r'\$\{t\}', '', s)
    s=re.sub(r'\$\{c\.value\}', 'api', s)
    s=re.sub(r'\$\{e\.apiUri\}', 'api', s)
    s=re.sub(r'\$\{g\.value\}', 'api/clients/db-backups/backups/', s)
    s=re.sub(r'\$\{p\}', 'api/containers/overview', s)
    # other ${...} -> {id}
    s=re.sub(r'\$\{[^}]*\}', '{id}', s)
    # remove leading base variables already
    s=s.strip()
    # if starts with ${...} leftover
    s=re.sub(r'^\$\{[^}]*\}', '', s)
    # split query
    path=s
    query=''
    if '?' in s:
        path,query=s.split('?',1)
    # clean double slashes
    path=re.sub(r'/{2,}', '/', path)
    # remove trailing slash? keep for some; normalize trailing slash remove except root
    if len(path)>1 and path.endswith('/'):
        path=path.rstrip('/')
    # query params
    qparams=[]
    if query:
        for part in query.split('&'):
            if not part: continue
            name=part.split('=',1)[0].strip()
            if name and name not in qparams:
                qparams.append(name)
    return path,qparams

# Filter endpoint-like
def is_endpoint(path):
    if not path or ' ' in path:
        return False
    # exclude UI/dom-ish
    ui_tokens = ['messages__','v-messages','notes-pane','notes-section','raw-material-tank-card','raw-material-tank-form','suppliers-wrapper','warehouses','suppliers','no-notes','dx5-','containers/overview/1? no']
    for t in ui_tokens:
        if path==t or path.startswith(t):
            # allow if has slash? 
            if '/' not in path:
                return False
    # must contain a known prefix or slash with letters
    if '/' not in path and path not in ('messages',):
        return False
    # exclude http
    if path.startswith('http'):
        return False
    # exclude assets
    if 'assets/' in path or 'bundled/' in path:
        return False
    return True

endpoints={}
for raw in plain:
    path,qps=normalize_raw(raw)
    if not is_endpoint(path):
        continue
    method=method_map.get(path, infer_method(path))
    if isinstance(method,list): method=method[0]
    key=(method,path)
    if key not in endpoints:
        endpoints[key]={'method':method,'path':path,'query':[]}
    for qp in qps:
        if qp not in endpoints[key]['query']:
            endpoints[key]['query'].append(qp)

# Also add method-call endpoints with known methods from earlier extraction? We already have plain strings includes all. But methods inferred may be wrong for some GET mutation? We'll override using a manual method map if needed. 
# Save
out=list(endpoints.values())
out.sort(key=lambda x:(x['path'],x['method']))
json.dump(out, open('artifacts/analysis/endpoints.json','w'), indent=2)
print('count',len(out))
for e in out:
    print(e['method'], e['path'], e['query'])
