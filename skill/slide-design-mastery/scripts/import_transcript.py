#!/usr/bin/env python3
"""Import user-provided transcript into local evidence chunks. No video downloading/AI extraction."""
import argparse,pathlib,re,json,hashlib,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]

def strip_vtt(t):
    lines=[]; clock=None
    for line in t.splitlines():
        s=line.strip()
        if not s or s.startswith(('WEBVTT','Kind:','Language:','NOTE')): continue
        if '-->' in s:
            clock=s.split('-->',1)[0].strip(); continue
        if re.fullmatch(r'\d+',s):continue
        s=re.sub(r'<[^>]*>','',s)
        lines.append((clock,s))
    return lines

def main():
    p=argparse.ArgumentParser(description='Import *user-supplied* TXT/VTT transcript into dated source chunks')
    p.add_argument('transcript',type=pathlib.Path)
    p.add_argument('--creator',default='unverified')
    p.add_argument('--video-id',default='fkxw0SrwVkA')
    p.add_argument('--chars',type=int,default=3500)
    a=p.parse_args()
    content=a.transcript.read_text(encoding='utf-8-sig')
    if not content.strip():raise SystemExit('Empty transcript')
    entries=strip_vtt(content) if a.transcript.suffix.lower() in ('.vtt','.srt') else [(None,x.strip()) for x in content.splitlines() if x.strip()]
    if not entries: raise SystemExit('No transcript content detected')
    dest=ROOT/'sources'/('transcript-'+a.video_id)
    dest.mkdir(exist_ok=True)
    segments=[];current=[];length=0;ix=1
    for ts,txt in entries:
        line=f'[{ts}] {txt}' if ts else txt
        if current and length+len(line)>max(500,a.chars):
            output='\n'.join(current); path=dest/f'chunk-{ix:03d}.md';path.write_text(output+'\n',encoding='utf-8');segments.append(str(path.relative_to(ROOT))); ix+=1;current=[];length=0
        current.append(line);length+=len(line)
    if current:
        path=dest/f'chunk-{ix:03d}.md';path.write_text('\n'.join(current)+'\n',encoding='utf-8');segments.append(str(path.relative_to(ROOT)))
    meta={'video_id':a.video_id,'creator_user_label':a.creator,'source_file':str(a.transcript),'sha256':hashlib.sha256(content.encode()).hexdigest(),'ingested_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'chunks':segments,'status':'ingested-unreviewed','warning':'Transcript is user-provided and has not been independently source-verified. No extracted speaker claims yet.'}
    (dest/'manifest.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    print(f'Imported {len(segments)} chunks to {dest}; manually review evidence before adding to references.')

if __name__=='__main__':main()
