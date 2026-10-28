"""Generate six reviewed two-page CVs. Requires ReportLab and pypdf."""
from pathlib import Path
from html import escape
import hashlib
import json
import shutil
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader
from career import JOBS, DEGREES, SUMMARIES, PROJECTS

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'assets/cv'
OUT.mkdir(exist_ok=True)
for name,file in [('Arial','arial.ttf'),('Arial-Bold','arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/file)))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold')
INK=colors.HexColor('#173334')
STYLES={
 'name':ParagraphStyle('name',fontName='Arial-Bold',fontSize=27,leading=32,textColor=INK,spaceAfter=6),
 'title':ParagraphStyle('title',fontName='Arial-Bold',fontSize=12,leading=16,textColor=INK,spaceAfter=9),
 'body':ParagraphStyle('body',fontName='Arial',fontSize=11,leading=15.4,spaceAfter=7),
 'small':ParagraphStyle('small',fontName='Arial',fontSize=9.3,leading=12.7,spaceAfter=6,textColor=colors.HexColor('#4c6060')),
 'h2':ParagraphStyle('h2',fontName='Arial-Bold',fontSize=12,leading=16,textColor=INK,spaceBefore=13,spaceAfter=8,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='Arial-Bold',fontSize=10,leading=14,spaceAfter=3,keepWithNext=True),
}
def para(text,style='body'):
    return Paragraph(escape(text.replace('–','-').replace('’',"'")),STYLES[style])
def footer(canvas,doc):
    canvas.setStrokeColor(colors.HexColor('#c8d6d5'));canvas.line(42,40,553,40)
    canvas.setFont('Arial',8);canvas.setFillColor(INK)
    canvas.drawString(42,27,'Sagar Kriplani | sagar-kriplani.github.io')
    canvas.drawRightString(553,27,str(doc.page))

for lang in ('en','de'):
    en=lang=='en'
    for kind in ('general','mechanical','rd'):
        title=({'general':'Mechanical Design & Development Engineer','mechanical':'Mechanical Design Engineer','rd':'Mechanical Engineer | Research & Development'} if en else {'general':'Konstrukteur | Mechanische Entwicklung','mechanical':'Konstrukteur | Maschinenbau','rd':'Maschinenbauingenieur | Forschung & Entwicklung'})[kind]
        story=[para('Sagar Kriplani','name'),para(title,'title'),para('Heidenheim an der Brenz, Germany | +49 157 582 90324','small'),para('sagar.kriplani@outlook.com | linkedin.com/in/sagar-kriplani','small'),para(SUMMARIES[lang][kind]),para('EXPERIENCE' if en else 'BERUFSERFAHRUNG','h2')]
        for date,employer,role,place,desc in JOBS[lang]:
            # Retain claim provenance while keeping the CV readable.
            if employer=='Ravi Brass Industries':
                desc=desc.split('Departure month')[0].split('Austrittsmonat')[0].strip()
            story.extend([para(employer+' | '+role,'h3'),para(date+' | '+place,'small'),para(desc)])
        story.extend([PageBreak(),para('Sagar Kriplani','title'),para('PROJECTS & QUALIFICATIONS' if en else 'PROJEKTE & QUALIFIKATIONEN','h2')])
        order=[1,0,2] if kind=='rd' else [0,1,2]
        for index in order:
            project,desc=PROJECTS[lang][index]
            story.extend([para(project,'h3'),para(desc)])
        story.append(para('EDUCATION' if en else 'AUSBILDUNG','h2'))
        for date,degree,institution in DEGREES[lang]:
            story.extend([para(degree+' | '+date,'h3'),para(institution)])
        story.extend([para('TECHNICAL SKILLS' if en else 'FACHKENNTNISSE','h2'),para('Autodesk Inventor | Siemens NX | PTC Creo | ANSYS | MATLAB | DFM/DFA | BOM | SAGE ERP | Agile PLM'),para('TRAINING' if en else 'WEITERBILDUNG','h2'),para('ANSYS Basic to Professional (2020); Siemens Centre of Excellence: NX, NC, Drafting, Robotics (2016-2017); LinkedIn Learning: Siemens NX, Engineering Drawings, Semiconductor Manufacturing (2026).'),para('LANGUAGES' if en else 'SPRACHEN','h2'),para('German: professional working; English: full professional; Hindi, Gujarati, Sindhi: native/bilingual. Self-reported; German certificate: B1-plus coursework.' if en else 'Deutsch: berufliche Arbeitskenntnisse; Englisch: professionelle Kenntnisse; Hindi, Gujarati, Sindhi: muttersprachlich/zweisprachig. Selbsteinschätzung; Deutsch-Nachweis: B1-plus-Kurs.'),para('Redacted certificates, references and transcripts: sagar-kriplani.github.io/en/evidence/' if en else 'Bereinigte Zertifikate, Zeugnisse und Notenübersichten: sagar-kriplani.github.io/de/evidence/','small')])
        path=OUT/f'{kind}-{lang}.pdf'
        doc=SimpleDocTemplate(str(path),pagesize=(595.28,841.89),rightMargin=42,leftMargin=42,topMargin=36,bottomMargin=54,title='Sagar Kriplani - '+title,author='Sagar Kriplani')
        doc.build(story,onFirstPage=footer,onLaterPages=footer)
        reader=PdfReader(path)
        assert len(reader.pages)==2,(path,len(reader.pages))
        text='\n'.join(p.extract_text() for p in reader.pages)
        for date in ['07/2023 - 06/2024','07/2023 - 01/2024','02/2024 - 06/2024','08/2020 - 09/2021']:
            assert date in text,(path,date)
        print(path.name, len(reader.pages),'pages')

# Replace legacy repository copies as well, so old files cannot contradict the website.
aliases={
 'CV_Sagar_Kriplani_General_EN.pdf':'general-en.pdf',
 'CV_Sagar_Kriplani_Mechanical_Design_EN.pdf':'mechanical-en.pdf',
 'CV_Sagar_Kriplani_RD_Engineer_EN.pdf':'rd-en.pdf',
 'Lebenslauf_Sagar_Kriplani_Allgemein_DE.pdf':'general-de.pdf',
 'Lebenslauf_Sagar_Kriplani_Konstruktion_DE.pdf':'mechanical-de.pdf',
 'Lebenslauf_Sagar_Kriplani_FE_Entwicklung_DE.pdf':'rd-de.pdf',
 'mechanical-design-en.pdf':'mechanical-en.pdf','mechanical-design-de.pdf':'mechanical-de.pdf',
 'rd-engineer-en.pdf':'rd-en.pdf','rd-engineer-de.pdf':'rd-de.pdf'}
for folder in ('cv','assets/docs','public/cv'):
    for old,new in aliases.items():
        dest=ROOT/folder/old
        if dest.exists():shutil.copy2(OUT/new,dest)
manifest={'source_sha256':hashlib.sha256((ROOT/'scripts/career.py').read_bytes()).hexdigest(),'pdfs':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.glob('*.pdf')}}
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
