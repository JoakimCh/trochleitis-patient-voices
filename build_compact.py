#!/usr/bin/env python3
"""Build the three-page compact alternative using the same source records."""
import json
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from build import ROOT, INK, MUTED, ACCENT

OUT = ROOT / 'output/pdf/trochleitis-patient-voices-compact.pdf'

def paragraph(text, size, color=INK, bold=False, leading=None):
    style = ParagraphStyle('compact', fontName='Bold' if bold else 'Body',
        fontSize=size, leading=leading or size*1.22, textColor=HexColor(color))
    return Paragraph(escape(text).replace('\n','<br/>'), style)

def draw(c, text, top, size, color=INK, bold=False, x=44, width=524, leading=None):
    p=paragraph(text,size,color,bold,leading)
    _,h=p.wrap(width,800)
    p.drawOn(c,x,top-h)
    return top-h

def blocks(record):
    date=record['date'] if record['id']!='01' else 'Thread: 22 Feb 2024; comment date unverified'
    meta=record['community']+' | '+date
    if record['original_language']=='sv': meta+=' | TRANSLATED FROM SWEDISH'
    short=record['url'].split('/comments/')[0]+'/comments/'+record['url'].split('/comments/')[1].split('/')[0]
    return [
        (record['title'],10.1,INK,True,0),
        (meta,7,MUTED,False,2),
        (record['quote'],9.3,INK,False,4),
        (record['context'],7.5,MUTED,False,3),
        ('ACCOUNT '+record['account']+' | '+record['status'],6.6,MUTED,False,3),
        ('Source: '+short,6.6,MUTED,False,1),
    ]

def card(c, record, top):
    parts=blocks(record)
    height=12
    for text,size,color,bold,gap in parts:
        _,h=paragraph(text,size,color,bold).wrap(524,800)
        height+=gap+h
    if top-height < 98:
        raise ValueError(f'Card {record["id"]} does not fit on compact page')
    c.setFillColor(HexColor('#F2F5F6'))
    c.roundRect(34,top-height,544,height,4,fill=1,stroke=0)
    c.setFillColor(HexColor(ACCENT));c.rect(34,top-height,2,height,fill=1,stroke=0)
    y=top-6
    for text,size,color,bold,gap in parts:
        y=draw(c,text,y-gap,size,color,bold)
    c.linkURL(record['url'],(44,y-1,568,y+10),relative=0,thickness=0)
    return top-height-3

def main():
    records=json.loads((ROOT/'sources.json').read_text())
    groups=[records[:6],records[6:11],records[11:]]
    assert [len(g) for g in groups]==[6,5,6]
    OUT.parent.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(OUT),pagesize=(612,792))
    c.setTitle('Trochleitis patient voices - compact edition')
    c.setAuthor('Patient advocacy source collection')
    headings=['Being heard and finding care','Pain, waiting and referral barriers','Uncertainty, follow-up and relief']
    for index,group in enumerate(groups):
        c.setFillColor(HexColor(INK));c.rect(0,786,612,6,fill=1,stroke=0)
        draw(c,'PATIENT VOICES / TROCHLEITIS / COMPACT EDITION',760,8,ACCENT,True,x=34,width=544)
        draw(c,headings[index],741,19,INK,True,x=34,width=544)
        y=710
        for record in group: y=card(c,record,y)
        c.setStrokeColor(HexColor('#D4DDE1'));c.line(34,43,578,43)
        draw(c,f'{index+1} / 3',32,6.5,MUTED,x=548,width=30)
        c.showPage()
    c.save()
    print(OUT)

if __name__=='__main__': main()
