#!/usr/bin/env python3
"""Render a standalone clinical literature briefing as a US Letter PDF."""
import re
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from build import ROOT

SOURCE=ROOT/'docs/trochleitis-care-gap.md'
OUT=ROOT/'output/pdf/trochleitis-care-gap.pdf'

def markup(text):
    # Allow only Markdown hyperlinks; escape all author text first.
    text=escape(text)
    return re.sub(r'\[([^\]]+)\]\((https://[^\s)]+)\)',
        lambda m: f'<link href="{m[2]}" color="#243f50"><u>{m[1]}</u></link>',text)

def main():
    styles={
      'title':ParagraphStyle('title',fontName='Bold',fontSize=23,leading=28,textColor=colors.black,spaceAfter=10),
      'subtitle':ParagraphStyle('subtitle',fontName='Body',fontSize=9,leading=13,textColor=colors.HexColor('#506370'),spaceAfter=19),
      'h2':ParagraphStyle('h2',fontName='Bold',fontSize=12,leading=15,spaceBefore=10,spaceAfter=7,keepWithNext=True,textColor=colors.black),
      'h3':ParagraphStyle('h3',fontName='Bold',fontSize=10,leading=13,spaceBefore=9,spaceAfter=6,keepWithNext=True,textColor=colors.black),
      'body':ParagraphStyle('body',fontName='Body',fontSize=10,leading=13.6,spaceAfter=9,textColor=colors.HexColor('#182D39'),allowWidows=0,allowOrphans=0),
      'reference':ParagraphStyle('reference',fontName='Body',fontSize=8.2,leading=10.8,spaceAfter=6,textColor=colors.HexColor('#182D39'),allowWidows=0,allowOrphans=0),
    }
    story=[]
    section=0
    for block in SOURCE.read_text().strip().split('\n\n'):
        if block.strip()=='<!-- pagebreak -->':
            story.append(PageBreak());section+=1;continue
        if block.startswith('# '):style='title';text=block[2:]
        elif block.startswith('### '):style='h3';text=block[4:]
        elif block.startswith('## '):style='h2';text=block[3:]
        elif block.startswith('Recognition diagnosis'):style='subtitle';text=block
        else:style='reference' if section==2 else 'body';text=block
        story.append(Paragraph(markup(text.replace('\n',' ')),styles[style]))
    def footer(c,doc):
        c.saveState()
        c.setFont('Body',7)
        c.setFillColor(colors.HexColor('#506370'))
        c.drawString(48,30,'TROCHLEITIS AND ACCESS TO CARE  |  13 NOV 2026')
        c.drawRightString(564,30,str(doc.page))
        c.restoreState()
    OUT.parent.mkdir(parents=True,exist_ok=True)
    doc=SimpleDocTemplate(str(OUT),pagesize=(612,792),leftMargin=48,rightMargin=48,topMargin=43,bottomMargin=51,
        title='Trochleitis and barriers to care',author='Clinical literature briefing')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    print(OUT)

if __name__=='__main__':main()
