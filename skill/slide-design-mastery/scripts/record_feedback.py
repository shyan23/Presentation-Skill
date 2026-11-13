#!/usr/bin/env python3
"""Save reviewed feedback and maintain active-lessons summary. Avoids automatic generalizing."""
import argparse,pathlib,json,datetime,uuid
ROOT=pathlib.Path(__file__).resolve().parents[1];F=ROOT/'memory'/'feedback.jsonl';ACTIVE=ROOT/'memory'/'active-lessons.md'

def main():
    p=argparse.ArgumentParser()
    for x in ('context','issue','fix','evidence'):p.add_argument('--'+x,required=True)
    p.add_argument('--category',choices=['story','accuracy','readability','layout','style','accessibility','editability','delivery','other'],default='other')
    p.add_argument('--reviewed',action='store_true',help='Required: has a real reviewer actually assessed the fix?')
    a=p.parse_args()
    if not a.reviewed:raise SystemExit('Will not store unreviewed inference as learned fact. Pass --reviewed only after reviewer confirmation.')
    obj={k:getattr(a,k) for k in ('context','issue','fix','evidence','category')};obj.update({'id':str(uuid.uuid4()),'reviewed':True,'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
    with F.open('a',encoding='utf-8') as h:h.write(json.dumps(obj,ensure_ascii=False)+'\n')
    records=[]
    for line in F.read_text(encoding='utf-8').splitlines():
        if not line.strip():continue
        try:r=json.loads(line)
        except json.JSONDecodeError:continue
        if r.get('reviewed'):records.append(r)
    lines=['# Active reviewed lessons','',f'{len(records)} reviewer-confirmed local observations. These are context-sensitive, not changes to model weights.','']
    for r in records[-12:][::-1]:
        lines.append(f"- **{r['category']}** ({r['context']}): {r['issue']} → **{r['fix']}**. Evidence: {r['evidence']}.")
    ACTIVE.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'Recorded reviewed feedback; active summary has {min(12,len(records))} item(s).')

if __name__=='__main__':main()
