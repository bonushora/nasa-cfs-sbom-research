#!/usr/bin/env python3
"""Verify the distributed package only; no experiment execution or network."""
from pathlib import Path
import hashlib, json, re, sys

ROOT = Path(__file__).resolve().parent

def need(ok, message):
    if not ok:
        raise ValueError(message)

def read(name):
    p = ROOT / name
    need(not Path(name).is_absolute() and '..' not in Path(name).parts and p.resolve().is_relative_to(ROOT), 'path: '+name)
    need(p.is_file() and not p.is_symlink(), 'file: '+name)
    return p.read_bytes()

def sha(raw): return hashlib.sha256(raw).hexdigest()

def load(name): return json.loads(read(name))

def main():
    entries = {}
    for line in read('SHA256SUMS').decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(bool(m), 'manifest format')
        h, name = m.groups()
        need(name not in entries and name != 'SHA256SUMS', 'manifest duplicate/self')
        need(sha(read(name)) == h, 'manifest hash: '+name)
        entries[name] = h
    need(set(entries)|{'SHA256SUMS'} == {str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file()}, 'package file set')
    need(not any(p.is_symlink() for p in ROOT.rglob('*')), 'symlink')
    rt = load('runtime-evidence.public.json')
    lk = load('SBOM-LINKAGE.public.json')
    anchor = load('ORIGINAL-ANCHORS.json')
    need(rt['baseline_commit']=='088b2fa828db9ff7e00733f1908e0eeb59f66ce3', 'baseline')
    need(anchor['consolidation_manifest_sha256']=='7b03476395aa059d3761b2d81fe11107dcfab9507d8837964508cb4d2c39eac6', 'original anchor')
    need(sha(read(anchor['original_manifest_public_path']))==anchor['consolidation_manifest_sha256'],'original manifest bytes')
    need(rt['historical_status']=='BLOCKED_PRESERVED' and rt['resume_status']=='PASS', 'history')
    expected={'cpu1-shared-sockets':(117,16),'cpu1-vxworks-loader':(10,4),'cpu2-shared-sockets':(117,16),'cpu2-vxworks-loader':(10,4)}
    need(len(rt['tests'])==len(lk['test_links'])==4 and set(t['label'] for t in rt['tests'])==set(expected), 'test identities')
    need(len(lk['documents'])==6 and len({d['documentNamespace'] for d in lk['documents']})==6, 'SPDX identities')
    docs={}
    for d in lk['documents']:
        raw=read(d['public_path']); obj=json.loads(raw)
        need(sha(raw)==d['public_sha256'], 'SPDX payload')
        ns=d['documentNamespace']
        if d['distribution']=='ORIGINAL_BYTES':
            need(sha(raw)==d['sha256'] and obj['documentNamespace']==ns and obj['spdxVersion']=='SPDX-2.3' and obj['SPDXID']=='SPDXRef-DOCUMENT', 'original SPDX')
            docs[ns]=[(kind,x) for kind in ('files','packages','snippets') for x in obj.get(kind,[])]
        else:
            need(d['distribution']=='DERIVED_EXCERPT_NOT_SPDX' and obj['original_namespace']==ns and obj['original_sha256']==d['sha256'], 'excerpt provenance')
            docs[ns]=[('files',x) for x in obj['selected_file_records']]
    links={x['test']:x for x in lk['test_links']}
    need(set(links)==set(expected),'link identities')
    for t in rt['tests']:
        label=t['label']; n,k=expected[label]
        need((t['assertions'],t['segments'])==(n,k) and t['exit_code']==0,'test counters')
        text=read(t['summary_path']).decode(); lines=text.splitlines()
        global_lines=[x for x in lines if re.fullmatch(r'\[\s*END\]\s+\d+\s+SUMMARY\s+.*',x)]
        need(len(global_lines)==1,'global summary')
        def counts(line):
            pairs=re.findall(r'\b(TOTAL|PASS|FAIL|MIR|TSF|TTF)::(\d+)\b',line)
            need(len(pairs)==6 and len(dict(pairs))==6,'counter format')
            return {a:int(b) for a,b in pairs}
        total=counts(global_lines[0]); need(total=={'TOTAL':n,'PASS':n,'FAIL':0,'MIR':0,'TSF':0,'TTF':0},'global counters')
        seg=[x for x in lines if re.match(r'^\[\s*END\]\s+\d+\s+.+?\s+TOTAL::',x) and x not in global_lines]
        need(len(seg)==k and [int(re.match(r'^\[\s*END\]\s+(\d+)',x)[1]) for x in seg]==list(range(1,k+1)),'segment order')
        values=[counts(x) for x in seg]
        need(all(v['TOTAL']==v['PASS'] and all(v[a]==0 for a in ('FAIL','MIR','TSF','TTF')) for v in values),'segment outcomes')
        need(all(sum(v[a] for v in values)==b for a,b in total.items()),'segment sums')
        need(sum(x.strip()==f'COMPLETE: {k} tests Segment(s) executed' for x in lines)==1,'complete marker')
        a=bytes.fromhex(t['gcov_header_pair']['gcda']); b=bytes.fromhex(t['gcov_header_pair']['gcno'])
        need(len(a)==len(b)==12 and a[:4]==b'adcg' and b[:4]==b'oncg' and a[4:]==b[4:],'GCOV header excerpt')
        digest=t['binary_sha256']; found=[]
        for ns, records in docs.items():
            for kind,x in records:
                if any(c.get('algorithm')=='SHA256' and c.get('checksumValue','').lower()==digest for c in x.get('checksums',[])):
                    found.append((ns,x['SPDXID'],kind))
        l=links[label]; need(l['binary_sha256']==digest,'link hash')
        need(len(found)==2 and sorted(found)==sorted((x['documentNamespace'],x['SPDXID'],x['record_type']) for x in l['matches']),'SPDX linkage')
        print('PUBLIC_READBACK=PASS:'+label)
    need(rt['assertions']==254 and rt['segments']==40 and rt['qualified_tests']==4,'totals')
    print('PUBLIC_PACKAGE_READBACK=PASS')
    print('ORIGINAL_BINARY_BYTE_VERIFICATION=NOT_PERFORMED')
    print('EXPERIMENT_REEXECUTION=NONE')

if __name__=='__main__':
    try: main()
    except Exception as e:
        print('PUBLIC_PACKAGE_READBACK=BLOCKED:'+str(e),file=sys.stderr); sys.exit(1)
