#!/usr/bin/env python3
"""Build a three-page US Letter collection from verified excerpt records."""
import json
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output/pdf/trochleitis-patient-voices.pdf'
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
for name, filename in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
INK = '#182D39'
MUTED = '#506370'
ACCENT = '#A24135'

def para(c, text, x, top, width, size=10, color=INK, font='Body', leading=None):
    style=ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.37,textColor=HexColor(color))
    p=Paragraph(escape(text).replace('\n','<br/>'),style)
    _,h=p.wrap(width,900)
    p.drawOn(c,x,top-h)
    return top-h

def main():
    records=json.loads((ROOT/'sources.json').read_text())
    OUT.parent.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(OUT),pagesize=(612,792))
    c.setTitle('Trochleitis: patient voices on pain and access to care')
    c.setAuthor('Patient advocacy source collection')
    headings=['The struggle to be heard','The search for an injection','The human cost of unresolved pain']
    intros=[
      'Selected public accounts of delayed recognition and dismissal in discussions of trochleitis.',
      'Patients describe barriers to finding a clinician. Reasons for declining treatment are not always available.',
      'These accounts describe distress, interrupted care and persistent pain, including after treatment.'
    ]
    for page in range(1,4):
        c.setFillColor(HexColor(INK)); c.rect(0,784,612,8,fill=1,stroke=0)
        para(c,'PATIENT VOICES  /  TROCHLEITIS',38,755,536,9,ACCENT,'Bold')
        para(c,headings[page-1],38,732,536,23,INK,'Bold')
        para(c,intros[page-1],38,690,536,10,MUTED)
        for i,r in enumerate([r for r in records if r['page']==page]):
            top=643-i*177
            c.setFillColor(HexColor('#F2F5F6')); c.roundRect(38,top-165,536,165,6,fill=1,stroke=0)
            c.setFillColor(HexColor(ACCENT)); c.rect(38,top-165,3,165,fill=1,stroke=0)
            y=para(c,r['id']+'  '+r['title'],51,top-11,510,11,INK,'Bold')
            date=r['date'] if r['id']!='01' else 'Thread: 22 Feb 2024; comment date unverified'
            y=para(c,r['community']+'  |  '+date,51,y-4,510,7.5,MUTED)
            y=para(c,r['quote'],51,y-8,510,10.5,INK,leading=13.5)
            y=para(c,r['context'],51,y-7,510,8,MUTED,leading=10.5)
            # Fixed source footer, with readable short permalink and clickable destination.
            short=r['url'].split('/comments/')[0]+'/comments/'+r['url'].split('/comments/')[1].split('/')[0]
            footer=top-153
            if y < footer+7:
                raise RuntimeError(f'Card {r["id"]} overflows: {y} < {footer+7}')
            para(c,'Source: '+short,51,footer,510,6.8,MUTED)
            c.linkURL(r['url'],(51,footer-10,560,footer+2),relative=0,thickness=0)
        notes=[
          'Verbatim excerpt cards, not screenshots. Usernames omitted. Original wording retained; bracketed notes are editorial. Excerpts 02 and 03 are the same account.',
          'Selected anecdotes, not a representative sample or a measure of health-system performance. Diagnoses, treatment need and clinician conduct have not been independently verified.',
          'Compiled 13 Nov 2026 from publicly indexed Reddit text. Five threads; nine excerpts, not nine verified patients. Locations are not established. No claim of worldwide prevalence is made.'
        ]
        para(c,notes[page-1],38,96,536,7.4,MUTED,leading=10)
        c.setStrokeColor(HexColor('#D4DDE1')); c.line(38,50,574,50)
        para(c,'PUBLIC ACCOUNTS  /  SOURCE LINKS INCLUDED',38,37,485,7,MUTED)
        para(c,f'{page} / 3',542,37,32,7,MUTED)
        c.showPage()
    c.save()
    print(OUT)

if __name__=='__main__': main()
