#!/usr/bin/env python3
"""Build a six-page US Letter collection from sourced public accounts."""
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
    headings=['The struggle to be heard','The search for an injection','The human cost of unresolved pain', 'Still searching for the right care', 'When uncertainty becomes distress', 'Why access and follow-up matter']
    intros=[
      'Selected public accounts of delayed recognition and dismissal in discussions of trochleitis.',
      'Patients describe barriers to finding a clinician. Reasons for declining treatment are not always available.',
      'These accounts describe distress, interrupted care and persistent pain, including after treatment.',
      'More public accounts of unfamiliarity, referral barriers and unresolved eye pain.',
      'Patients describe uncertainty, a denied investigation and the emotional burden of waiting.',
      'Accounts of benefit show why timely assessment, treatment and continued care matter.'
    ]
    for page in range(1,7):
        c.setFillColor(HexColor(INK)); c.rect(0,784,612,8,fill=1,stroke=0)
        para(c,'PATIENT VOICES  /  TROCHLEITIS',38,755,536,9,ACCENT,'Bold')
        para(c,headings[page-1],38,732,536,23,INK,'Bold')
        para(c,intros[page-1],38,690,536,10,MUTED)
        for i,r in enumerate([r for r in records if r['page']==page]):
            top=643-i*177
            c.setFillColor(HexColor('#F2F5F6')); c.roundRect(38,top-165,536,165,6,fill=1,stroke=0)
            c.setFillColor(HexColor(ACCENT)); c.rect(38,top-165,3,165,fill=1,stroke=0)
            y=para(c,r['title'],51,top-11,510,11,INK,'Bold')
            date=r['date'] if r['id']!='01' else 'Thread: 22 Feb 2024; comment date unverified'
            y=para(c,r['community']+'  |  '+date+('  |  TRANSLATED FROM SWEDISH' if r['original_language']=='sv' else ''),51,y-4,510,7.5,MUTED)
            y=para(c,r['quote'],51,y-8,510,10.5,INK,leading=13.5)
            y=para(c,r['context'],51,y-7,510,8,MUTED,leading=10.5)
            # Fixed source footer, with readable short permalink and clickable destination.
            short=r['url'].split('/comments/')[0]+'/comments/'+r['url'].split('/comments/')[1].split('/')[0]
            footer=top-153
            if y < footer+19:
                raise RuntimeError(f'Card {r["id"]} overflows: {y} < {footer+19}')
            para(c,'ACCOUNT '+r['account']+'  |  '+r['status'],51,footer+10,510,6.6,MUTED)
            para(c,'Source: '+short,51,footer,510,6.8,MUTED)
            c.linkURL(r['url'],(51,footer-10,560,footer+2),relative=0,thickness=0)
        if page==6:
            top=289
            c.setFillColor(HexColor('#F2F5F6')); c.roundRect(38,top-165,536,165,6,fill=1,stroke=0)
            y=para(c,'About this collection',51,top-12,510,11,INK,'Bold')
            y=para(c,'17 excerpt cards across 8 public threads. Account labels organize posts; they are not verified medical case numbers. Shared labels indicate the same reported author. Cross-thread identities may overlap.',51,y-10,510,9,MUTED)
            y=para(c,'English wording is verbatim except marked omissions and editorial notes. One Swedish excerpt is translated into English; the original is retained in sources.json. It has not been reviewed by its author.',51,y-9,510,9,MUTED)
            para(c,'Selected anecdotes do not measure prevalence, prove negligence or establish which treatment any person needs. Sources were accessed 13 Nov 2026; indexed text may omit later developments.',51,y-9,510,9,MUTED)
        notes=[
          'Verbatim excerpt cards, not screenshots. Usernames omitted. Account 2.a and 2.b refer to the same commenter. Original spelling retained; bracketed notes are editorial.',
          'These comments describe access concerns. Diagnosis, clinical need and the reasons for declining a procedure are not independently established.',
          'Reported diagnoses and suspected cases are distinguished in the account labels. Treatment response and other possible causes remain part of the context.',
          'The Swedish-language excerpt is translated into English. Language alone does not establish nationality or where care was sought. Translation has not been reviewed by the author.',
          'Account 8.b claims continuity with 8.a through a new username; that link is self-reported. The follow-up date and its reference to a November appointment do not align clearly.',
          'Public reports are leads for further reporting. Seek author consent before identification or interviews, and independently check medical or institutional allegations before publication.'
        ]
        para(c,notes[page-1],38,96,536,7.4,MUTED,leading=10)
        c.setStrokeColor(HexColor('#D4DDE1')); c.line(38,50,574,50)
        para(c,'PUBLIC ACCOUNTS  /  SOURCE LINKS INCLUDED',38,37,485,7,MUTED)
        para(c,f'{page} / 6',542,37,32,7,MUTED)
        c.showPage()
    c.save()
    print(OUT)

if __name__=='__main__': main()
