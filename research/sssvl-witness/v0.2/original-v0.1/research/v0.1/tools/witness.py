# Copyright 2026 Thales Rangel (to the extent of rights held)
# SPDX-License-Identifier: Apache-2.0
# Editorial license notice added for v0.1; original implementation preserved below.
"""Pure synthetic composition reconciliation. No filesystem, network or oracle access."""
import json, hashlib, re
SCHEMA_SHA256="9cf356a5646faf012a9f2ad170847158c4bed4c6ee2ab7c4f8b7dddda4bc500d"
VERSION="0.1"
def require(ok,code):
    if not ok: raise ValueError(code)
def canonical(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
def digest(x): return hashlib.sha256(x).hexdigest()
def text(x): return isinstance(x,str) and bool(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._+-]{0,127}',x))
def hexhash(x): return isinstance(x,str) and bool(re.fullmatch(r'[0-9a-f]{64}',x))
def exact(x,keys): return isinstance(x,dict) and set(x)==set(keys)
def strict(raw):
    def pairs(items):
        d={}
        for k,v in items:
            require(k not in d,'DUPLICATE_JSON_KEY'); d[k]=v
        return d
    def bad(x): raise ValueError('NON_JSON_CONSTANT')
    return json.loads(raw.decode('utf-8'),object_pairs_hook=pairs,parse_constant=bad)
def components(rows):
    require(isinstance(rows,list),'ENTITY_LIST'); out={}; names=set()
    for r in rows:
        require(exact(r,('name','version','sha256')),'ENTITY_FIELDS')
        n,v,h=r['name'],r['version'],r['sha256']; require(text(n) and text(v) and hexhash(h),'ENTITY_IDENTITY')
        require(n not in names,'AMBIGUOUS_NAME'); names.add(n); out[n+'@'+v]=h
    return out
def edges(rows,ids):
    require(isinstance(rows,list),'EDGE_LIST'); out=set()
    for x in rows:
        require(isinstance(x,list) and len(x)==2 and all(isinstance(z,str) and z in ids for z in x),'EDGE_ENDPOINT')
        t=tuple(x); require(t not in out,'DUPLICATE_EDGE'); out.add(t)
    return out
def normalize(raw):
    require(isinstance(raw,bytes) and 0<len(raw)<=1048576,'SUBMISSION_BYTES'); d=strict(raw)
    require(isinstance(d,dict) and d.get('spdxVersion')=='SPDX-2.3' and d.get('SPDXID')=='SPDXRef-DOCUMENT' and d.get('dataLicense')=='CC0-1.0','SPDX_PROFILE')
    require(not d.get('files') and not d.get('snippets') and not d.get('externalDocumentRefs'),'SPDX_EXTERNAL_OR_NONPACKAGE')
    require(isinstance(d.get('documentNamespace'),str) and bool(d['documentNamespace']),'NAMESPACE')
    require(isinstance(d.get('packages'),list) and isinstance(d.get('relationships'),list),'SPDX_LISTS')
    ids={}; rows=[]
    for p in d['packages']:
        sid=p['SPDXID']; require(isinstance(sid,str) and re.fullmatch(r'SPDXRef-[A-Za-z0-9.-]+',sid) and sid!='SPDXRef-DOCUMENT' and sid not in ids,'SPDX_ID')
        require(p.get('filesAnalyzed') is False,'PACKAGE_PROFILE')
        c=p['checksums']; require(isinstance(c,list) and len(c)==1 and c[0]['algorithm']=='SHA256','CHECKSUM_PROFILE')
        n,v,h=p['name'],p['versionInfo'],c[0]['checksumValue']; require(text(n) and text(v) and hexhash(h),'PACKAGE_IDENTITY')
        ids[sid]=n+'@'+v; rows.append({'name':n,'version':v,'sha256':h})
    entities=components(rows); descriptions=[]; dep=[]; seen=set()
    for r in d['relationships']:
        a,k,b=r['spdxElementId'],r['relationshipType'],r['relatedSpdxElement']; t=(a,k,b); require(t not in seen,'DUPLICATE_RELATION'); seen.add(t)
        if k=='DESCRIBES':
            require(a=='SPDXRef-DOCUMENT' and b in ids,'DESCRIBES_ENDPOINT'); descriptions.append(b)
        elif k=='DEPENDS_ON':
            require(a in ids and b in ids,'DEPENDENCY_ENDPOINT'); dep.append([ids[a],ids[b]])
        else: raise ValueError('RELATION_TYPE')
    require(sorted(descriptions)==sorted(ids) and sorted(d['documentDescribes'])==sorted(ids),'DOCUMENT_DESCRIBES')
    return entities,edges(dep,entities)
def reconcile(raw,submitted_config,reference,qualification):
    """Caller provides authenticated input; this pure core does not establish trust."""
    base={'contract_version':VERSION,'scope_kind':'SYNTHETIC_COMPOSITION_ONLY','witness_os_isolation':'NOT_QUALIFIED','evidence_vault':'NOT_QUALIFIED','security_assessment':'NOT_PERFORMED','assessment_support':'NOT_ESTABLISHED','verdict_authority':'NONE_FOR_SECURITY','trust':'CALLER_SUPPLIED_LOGICAL_REFERENCE_NOT_OS_QUALIFIED'}
    try:
        require(isinstance(raw,bytes),'SUBMISSION_BYTES'); sd=digest(raw)
        require(text(submitted_config),'SUBMITTED_CONFIG')
        require(exact(qualification,('sha256','schema_sha256','schema_state','referential_state','authority')),'QUALIFICATION_FIELDS')
        require(qualification['sha256']==sd and qualification['schema_sha256']==SCHEMA_SHA256 and qualification['schema_state']=='PASS' and qualification['referential_state']=='PASS' and qualification['authority'] in ('UNIT_TEST_ONLY','SEALED_Q1_CALLER_ASSERTION'),'QUALIFICATION_BINDING')
        require(exact(reference,('scope_id','configuration','lifecycle','required','excluded','required_edges','observed','observed_edges')),'REFERENCE_FIELDS')
        require(text(reference['scope_id']) and text(reference['configuration']) and reference['lifecycle']=='SYNTHETIC_INSTALL','REFERENCE_SCOPE')
        required=components(reference['required']); excluded=components(reference['excluded']); observed=components(reference['observed'])
        require(bool(required) and not set(required)&set(excluded) and not ({x.split('@')[0] for x in required}&{x.split('@')[0] for x in excluded}),'REFERENCE_UNIVERSE')
        require(set(observed)<=set(required),'OBSERVATION_SCOPE')
        wanted=edges(reference['required_edges'],required); oe=edges(reference['observed_edges'],required)
        require(oe<=wanted,'OBSERVATION_EDGE_SCOPE')
        sub,se=normalize(raw)
        issues=[]
        def issue(code,detail,kind='FAIL'): issues.append({'code':code,'detail':detail,'kind':kind})
        if submitted_config!=reference['configuration']: issue('CONFIGURATION_MISMATCH',[submitted_config,reference['configuration']])
        matched=[]; missing=[]; unknown=[]; versions=[]; hashes=[]; extra=[]
        names={k.split('@')[0]:k for k in sub}
        for k,h in sorted(required.items()):
            if k not in observed: unknown.append(k); issue('REFERENCE_ENTITY_UNKNOWN',k,'UNKNOWN')
            elif observed[k]!=h: issue('REFERENCE_HASH_CONFLICT',k)
            if k not in sub:
                missing.append(k); alt=names.get(k.split('@')[0]); issue('REQUIRED_ENTITY_MISSING',k)
                if alt is not None: versions.append([k,alt]); issue('VERSION_MISMATCH',[k,alt])
            elif sub[k]!=h: hashes.append(k); issue('HASH_MISMATCH',k)
            elif observed.get(k)==h: matched.append(k)
        for k,h in sorted(sub.items()):
            if k not in required and k not in excluded: extra.append(k); issue('UNJUSTIFIED_EXTRA_ENTITY',k)
            elif k in excluded and h!=excluded[k]: issue('EXCLUDED_IDENTITY_HASH_MISMATCH',k)
        em=[]; eu=[]; ea=[]
        for e in sorted(wanted):
            if e not in oe or any(k not in observed for k in e): eu.append(list(e)); issue('REFERENCE_EDGE_UNKNOWN',list(e),'UNKNOWN')
            if e not in se: ea.append(list(e)); issue('REQUIRED_EDGE_MISSING',list(e))
            elif e in oe and all(k in matched for k in e): em.append(list(e))
        for e in sorted(se-wanted):
            if not any(k in excluded for k in e): issue('UNJUSTIFIED_EXTRA_EDGE',list(e))
        issues.sort(key=canonical)
        state='SUFFICIENT_FOR_DECLARED_COMPOSITION_SCOPE' if not issues else 'BLOCKED'
        ref_norm={'scope_id':reference['scope_id'],'configuration':reference['configuration'],'lifecycle':reference['lifecycle'],'required':required,'excluded':excluded,'observed':observed,'required_edges':sorted(wanted),'observed_edges':sorted(oe)}
        return {**base,'state':state,'input_sha256':sd,'reference_sha256':digest(canonical(ref_norm)),'scope_id':reference['scope_id'],'configuration_identity':'MATCH' if submitted_config==reference['configuration'] else 'MISMATCH','structural_profile':'PASS','formal_schema':'CALLER_ASSERTED_PASS_BOUND_TO_BYTES','qualification_authority':qualification['authority'],'entity_coverage':{'matched':len(matched),'required':len(required),'state':'FAIL' if missing or hashes or any(observed.get(k)!=h for k,h in required.items() if k in observed) else ('UNKNOWN' if unknown else 'PASS')},'relation_coverage':{'matched':len(em),'required':len(wanted),'state':'NOT_APPLICABLE' if not wanted else ('FAIL' if ea else ('UNKNOWN' if eu else ('PASS' if len(em)==len(wanted) else 'FAIL')))},'missing_entities':missing,'version_mismatches':versions,'hash_mismatches':hashes,'extra_entities':extra,'unknown_entities':unknown,'missing_edges':ea,'unknown_edges':eu,'issues':issues}
    except (ValueError,TypeError,KeyError,AttributeError,UnicodeError,RecursionError) as e:
        return {**base,'state':'BLOCKED','structural_profile':'NOT_ESTABLISHED','issues':[{'code':'INVALID_OR_UNQUALIFIED_INPUT','kind':'FAIL','detail':str(e)}]}
