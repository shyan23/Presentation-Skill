#!/usr/bin/env python3
"""Validate package structure and style registry."""
import pathlib,json,sys,re
r=pathlib.Path(__file__).resolve().parents[1]
needed=['SKILL.md','README.md','profiles/styles.json','references/source-integrity.md','references/anti-slop-audit.md','references/source-learning.md','references/quality-assurance.md','memory/active-lessons.md','scripts/audit_pptx.py','sources/VIDEO_SOURCE.md']
missing=[n for n in needed if not (r/n).is_file()]
if missing:print('Missing files:',*missing,sep='\n');sys.exit(2)
s=(r/'SKILL.md').read_text(encoding='utf-8')
assert s.startswith('---\n') and 'name: slide-design-mastery' in s, 'SKILL metadata missing'
refs=re.findall(r'`((?:references|profiles|workflows|memory|scripts|sources)/[^` ]+)`',s)
notfound=[x for x in refs if not (r/x).is_file() and not x.endswith('/')]
if notfound:print('Broken referenced paths:',notfound);sys.exit(3)
data=json.loads((r/'profiles/styles.json').read_text(encoding='utf-8'))
assert len(data['styles'])==data['profile_count']>=12
ids=[v['id'] for v in data['styles']]
assert len(ids)==len(set(ids)), 'Duplicate style IDs'
for d in data['styles']:
    assert all(k in d for k in ['best_for','avoid_for','colors','grid_and_layout','data_visualization','failure_mode'])
print(f'PASS: {len(list(r.rglob("*")))} package entries, {len(ids)} style profiles, all core references exist.')
