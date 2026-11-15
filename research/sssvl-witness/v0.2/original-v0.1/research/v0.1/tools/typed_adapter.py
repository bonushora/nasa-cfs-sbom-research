# Copyright 2026 Thales Rangel (to the extent of rights held)
# SPDX-License-Identifier: Apache-2.0
# Editorial license notice added for v0.1; original implementation preserved below.
import json,re,collections

def require(ok,msg):
    if not ok: raise ValueError(msg)
def path(name,config):
    prefix={'STD':'./native_std/install/','EDS':'install/'}[config]
    require(isinstance(name,str),'PATH_TYPE')
    if config=='EDS' and name.startswith('./'): name=name[2:]
    require(name.startswith(prefix),'PATH_NAMESPACE')
    p=name[len(prefix):]
    require(p and not any(x in ('','.','..') for x in p.split('/')) and chr(92) not in p and chr(0) not in p,'PATH_INVALID')
    return p

def unique(pairs):
    d={}
    for k,v in pairs:
        require(k not in d,'DUPLICATE_JSON_KEY'); d[k]=v
    return d

def adapt(doc,config,role):
    require(role in ('files','elf'),'ROLE')
    rows={}; ids={}; declarations={}
    for f in doc.get('files',[]):
        n=path(f['fileName'],config); i=f['SPDXID']
        require(n not in rows and i not in ids,'DUPLICATE')
        h=[x['checksumValue'].lower() for x in f.get('checksums',[]) if x['algorithm']=='SHA256']
        require(len(h)==1 and re.fullmatch('[0-9a-f]{64}',h[0]),'HASH')
        types=f.get('fileTypes',[])
        require(role!='elf' or 'BINARY' in types,'ELF_TYPE')
        rows[n]={'sha256':h[0],'type':'ELF' if 'BINARY' in types else ('REGULAR' if types else 'UNSPECIFIED')}; ids[i]=n
        if role=='elf':
            if config=='STD': declarations[n]=[]
            else:
                try: z=json.loads(f.get('comment',''),object_pairs_hook=unique); v=z['DT_NEEDED']
                except (ValueError,TypeError,KeyError): v=None
                declarations[n]=v if isinstance(v,list) and all(isinstance(x,str) and x for x in v) else None
    if config=='STD' and role=='elf':
        for z in doc.get('relationships',[]):
            if z['relationshipType']!='DYNAMIC_LINK': continue
            require(z['spdxElementId'] in ids,'DANGLING_CONSUMER')
            n=ids[z['spdxElementId']]
            if z.get('relatedSpdxElement')!='SPDXRef-Package-glibc' or z.get('comment')!='ELF_OBSERVED DT_NEEDED libc.so.6': declarations[n]=None
            elif declarations[n] is not None: declarations[n].append('libc.so.6')
    return {'configuration':config,'role':role,'files':rows,'declarations':declarations,'provider_resolution':'UNKNOWN'}

def compare(ref,submitted):
    # Typed comparison prototype, not the W04 witness. No package or provider claims.
    if ref['configuration']!=submitted['configuration']: return {'state':'BLOCKED','reason':'CONFIGURATION_MISMATCH','verdict_authority':'NONE_FOR_SECURITY'}
    a=ref['files']; b=submitted['files']; missing=sorted(set(a)-set(b)); extra=sorted(set(b)-set(a)); mismatch=sorted(n for n in a.keys()&b.keys() if a[n]['sha256']!=b[n]['sha256'] or b[n]['type'] not in (a[n]['type'],'UNSPECIFIED')); rm=re=ru=matched_rel=0
    for n,v in ref['declarations'].items():
        w=submitted['declarations'].get(n)
        if n not in b or n in mismatch or w is None: ru+=len(v); continue
        x=collections.Counter(v); y=collections.Counter(w); matched_rel+=sum((x&y).values()); rm+=sum((x-y).values()); re+=sum((y-x).values())
    unknown_consumers=sorted(n for n in ref['declarations'] if n not in b or n in mismatch or submitted['declarations'].get(n) is None)
    return {'state':'BLOCKED' if missing or extra or mismatch or rm or re or unknown_consumers else 'SUFFICIENT_FOR_DECLARED_COMPOSITION_SCOPE','required_files':len(a),'matched_files':len(a)-len(missing)-len(mismatch),'missing':missing,'extra':extra,'mismatch':mismatch,'required_relations':sum(map(len,ref['declarations'].values())),'matched_relations':matched_rel,'relation_missing':rm,'relation_extra':re,'relation_unknown':ru,'unknown_consumers':unknown_consumers,'verdict_authority':'NONE_FOR_SECURITY'}

def evaluate_pair(universe,submitted_configuration,files_document,elf_document):
    # Caller must authenticate configuration and document lineage; never infer configuration from hash/name.
    if universe['configuration']!=submitted_configuration:
        return {'state':'BLOCKED','configuration_match':False,'roles':{},'verdict_authority':'NONE_FOR_SECURITY'}
    k=submitted_configuration; roles={}
    for role,doc in [('files',files_document),('elf',elf_document)]:
        expected=universe['files'] if role=='files' else {n:x for n,x in universe['files'].items() if x['type']=='ELF'}
        declarations={} if role=='files' else universe['declarations']
        roles[role]=compare({'configuration':k,'files':expected,'declarations':declarations},adapt(doc,k,role))
    return {'state':'BLOCKED' if any(x['state']=='BLOCKED' for x in roles.values()) else 'SUFFICIENT_FOR_DECLARED_COMPOSITION_SCOPE','configuration_match':True,'roles':roles,'verdict_authority':'NONE_FOR_SECURITY'}
