#!/usr/bin/env python3
"""Non-destructive PPTX structural audit. Does not replace visual review.
Optional dependency: pip install python-pptx
"""
import argparse,collections,json,pathlib,re,sys

def main():
    p=argparse.ArgumentParser(description='Static audit editable PowerPoint deck')
    p.add_argument('deck',type=pathlib.Path)
    p.add_argument('--json',type=pathlib.Path,help='Save machine-readable report')
    a=p.parse_args()
    try:from pptx import Presentation
    except ImportError:print('Install optional dependency: pip install python-pptx',file=sys.stderr);return 3
    if not a.deck.exists():print('No such file: '+str(a.deck),file=sys.stderr);return 2
    prs=Presentation(str(a.deck))
    emu=914400;W=prs.slide_width/emu;H=prs.slide_height/emu
    report={'deck':str(a.deck),'slide_count':len(prs.slides),'dimensions_inches':[round(W,2),round(H,2)],'warnings':[],'slides':[],'limitations':['Cannot detect all actual text overflows, true overlaps, false content or contrast of complex backgrounds. Render every slide.']}
    signature=collections.Counter()
    for idx,s in enumerate(prs.slides,1):
        counts=collections.Counter();warnings=[];words=0;fonts=[];has_source=False
        shape_boxes=[]
        for j,shape in enumerate(s.shapes,1):
            counts[str(shape.shape_type)]+=1
            x,y,w,h=[getattr(shape,k,0)/emu for k in ('left','top','width','height')]
            if x < -0.01 or y < -0.01 or x+w > W+0.01 or y+h > H+0.01:
                warnings.append({'type':'off_slide','shape_index':j,'shape_name':shape.name,'bbox_in':[round(z,2) for z in [x,y,w,h]]})
            if getattr(shape,'has_text_frame',False):
                t=shape.text.strip(); words+=len(re.findall(r'\S+',t))
                if re.search(r'(source|references|doi:|https?://)',t,re.I):has_source=True
                for para in shape.text_frame.paragraphs:
                    for run in para.runs:
                        if run.font.size:
                            pt=run.font.size.pt;fonts.append(pt)
                            if pt<12 and len(run.text.strip())>5:
                                warnings.append({'type':'very_small_font','shape_index':j,'size_pt':round(pt,1),'text_excerpt':run.text[:90]})
            if getattr(shape,'has_chart',False):counts['charts']+=1
            if getattr(shape,'has_table',False):counts['tables']+=1
        if words>120:warnings.append({'type':'high_word_count','count':words,'note':'Review information density; appendices/handouts may intentionally be dense.'})
        if words>0 and fonts and max(fonts)<=18:warnings.append({'type':'no_large_type_detected','max_pt':round(max(fonts),1),'note':'May be small on projection; check visually.'})
        layout_sig=(counts.get('AUTO_SHAPE (1)',0),counts.get('TEXT_BOX (17)',0),counts.get('PICTURE (13)',0))
        signature[layout_sig]+=1
        report['slides'].append({'slide':idx,'shape_count':len(s.shapes),'word_count':words,'native_charts':counts.get('charts',0),'native_tables':counts.get('tables',0),'has_text_source_cue':has_source,'font_pts_min_max':[round(min(fonts),1),round(max(fonts),1)] if fonts else None,'warnings':warnings})
    for sig,n in signature.items():
        if n>=max(5,len(prs.slides)*0.7) and len(prs.slides)>=7:
            report['warnings'].append(f'{n} slides share coarse shape-count signature {sig}; inspect for repetitive layouts (may be benign).')
    total=sum(len(s['warnings']) for s in report['slides'])+len(report['warnings'])
    report['warning_count']=total
    if a.json:a.json.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(f"{len(prs.slides)} slides, size {W:.2f}x{H:.2f} inches, {total} static warnings")
    for s in report['slides']:
        if s['warnings']:
            print(f"Slide {s['slide']}: "+', '.join(w['type'] for w in s['warnings'][:7]))
    for w in report['warnings']:print('Deck:',w)
    return 0

if __name__=='__main__':raise SystemExit(main())
