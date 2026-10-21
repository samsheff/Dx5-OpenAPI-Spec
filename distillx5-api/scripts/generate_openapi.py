import json,re,yaml

endpoints=json.load(open('artifacts/analysis/endpoints.json'))
# unique path params names
def unique_path(path):
    # replace sequential {id} with {id1} etc
    count=0
    def repl(m):
        nonlocal count
        count+=1
        return '{id%d}'%count if count>1 else '{id}'
    # only replace {id} tokens (already normalized)
    return re.sub(r'\{id\}', lambda m: '{id%d}'% ( (lambda: None)() ) if False else '{id}', path)  # placeholder
# simpler manual
def normalize_params(path):
    parts=path.split('{id}')
    # rebuild
    out=parts[0]
    for i,p in enumerate(parts[1:],start=1):
        name='id' if i==1 and parts.count('{id}')==1 else 'id%d'%i
        # Actually if only one, id; if multiple, id1..idN
        out += '{' + name + '}' + p
    # fix naming: if multiple, first should id1 not id
    if path.count('{id}')>1:
        # rename {id} first occurrence? We'll just use id1..idN consistently
        # Rebuild with id1..idN
        out=parts[0]
        for i,p in enumerate(parts[1:],start=1):
            out += '{id%d}'%i + p
    return out

def tag_for(path):
    segs=[s for s in path.split('/') if s]
    # remove api/v1/rpc etc
    if segs and segs[0]=='api':
        # find resource after rpc/rest
        if len(segs)>=4 and segs[1]=='v1' and segs[2] in ('rpc','rest'):
            return segs[3].split('-')[0].capitalize() if not segs[3].startswith('{') else 'Api'
        if len(segs)>=2:
            return segs[1].capitalize()
        return 'Api'
    if segs:
        return segs[0].capitalize()
    return 'General'

def op_id(method,path):
    slug=re.sub(r'[^a-zA-Z0-9]+','_', path).strip('_')
    return (method.lower()+'_'+slug)[:80]

paths={}
for e in endpoints:
    raw_path=e['path']
    # remove leading slash
    if raw_path.startswith('/'):
        raw_path=raw_path[1:]
    path_params_count=raw_path.count('{id}')
    norm_path='/'+normalize_params(raw_path)
    method=e['method'].lower()
    if method not in ('get','post','put','patch','delete'):
        method='get'
    # ensure path key
    paths.setdefault(norm_path,{})
    # path params
    pnames=re.findall(r'\{([^}]+)\}', norm_path)
    params=[]
    for pn in pnames:
        params.append({'name':pn,'in':'path','required':True,'schema':{'type':'string'}})
    for qp in e.get('query',[]):
        params.append({'name':qp,'in':'query','required':False,'schema':{'type':'string'}})
    op={
      'operationId': op_id(e['method'], norm_path),
      'tags':[tag_for(raw_path)],
      'summary': e['method']+' '+norm_path,
      'description': 'Discovered from DISTILL x 5 frontend bundle. Business purpose inferred from path and module context.',
      'parameters': params if params else None,
      'responses': {
        '200': {'description':'Successful response','content':{'application/json':{'schema':{'type':'object','additionalProperties':True}}}},
        '401': {'description':'Unauthenticated'},
        '403': {'description':'Forbidden / CSRF failure'},
        '404': {'description':'Not found'},
        '419': {'description':'CSRF token mismatch'},
        '500': {'description':'Server error'}
      },
      'x-discovery': {
        'confidence':'medium',
        'source':'bundle-extracted',
        'evidence':['artifacts/analysis/endpoints.json','artifacts/bundles/']
      }
    }
    if params is None:
        del op['parameters']
    if method in ('post','put','patch','delete'):
        op['requestBody']={
          'required': False,
          'content': {
            'application/x-www-form-urlencoded': {'schema':{'type':'object','additionalProperties':True}},
            'application/json': {'schema':{'type':'object','additionalProperties':True}}
          }
        }
    # remove None
    if op.get('parameters') is None:
        del op['parameters']
    paths[norm_path][method]=op

openapi={
 'openapi':'3.1.0',
 'info':{
   'title':'DISTILL x 5 Frontend API',
   'version':'0.1.0',
   'license':{'name':'Reverse-engineered documentation (internal use)'},
   'description':'Reverse-engineered from the DISTILL x 5 web application frontend assets. Endpoints discovered via static analysis of JavaScript bundles; methods and paths evidence-backed. Schemas are partial/generic where not fully observable.'
 },
 'servers':[{'url':'https://distillx5.com/archetype','description':'Observed application base path'}],
 'paths':paths,
 'components':{
   'securitySchemes':{
     'cookieAuth':{'type':'apiKey','in':'cookie','name':'session','description':'Session cookie (exact cookie name not confirmed).'},
     'csrfToken':{'type':'apiKey','in':'header','name':'X-CSRF-Token','description':'CSRF token from meta[name=csrf-token].'}
   }
 },
 'security':[{'cookieAuth':[]}]
}

# write yaml
with open('distillx5-api/openapi.yaml','w') as f:
    # ensure dir
    pass
import os
os.makedirs('distillx5-api',exist_ok=True)
with open('distillx5-api/openapi.yaml','w') as f:
    yaml.safe_dump(openapi,f,sort_keys=False,allow_unicode=True)
# json
with open('distillx5-api/openapi.json','w') as f:
    json.dump(openapi,f,indent=2)
print('written', len(paths))
