#!/usr/bin/env python3
"""Inspect built-in style profiles and print tokens. No external dependencies."""
import argparse,json,pathlib,sys
DATA=pathlib.Path(__file__).resolve().parents[1]/'profiles'/'styles.json'

def main():
    p=argparse.ArgumentParser(description='List/show slide design aesthetic profiles')
    p.add_argument('--list', action='store_true')
    p.add_argument('--id',help='profile id')
    p.add_argument('--json',action='store_true',help='JSON output for selected profile')
    a=p.parse_args()
    styles=json.loads(DATA.read_text(encoding='utf-8'))['styles']
    if a.list or not a.id:
        for d in styles: print(f"{d['id']:<23} {d['name']} — {d['best_for']}")
        return 0
    s=next((d for d in styles if d['id']==a.id),None)
    if s is None:
        print('Unknown id: '+a.id, file=sys.stderr); return 2
    if a.json: print(json.dumps(s,ensure_ascii=False,indent=2))
    else:
        for k,v in s.items(): print(f'{k}: {v}')
    return 0

if __name__=='__main__':raise SystemExit(main())
