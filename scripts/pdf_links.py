"""Add navigation/language metadata to approved CVs without changing text or page layout.

Requires pypdf and pdfplumber. This does not claim PDF/UA or tagged-PDF compliance.
"""
from pathlib import Path
import hashlib
import json
import shutil
import pdfplumber
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
from pypdf.generic import NameObject, TextStringObject

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'assets/cv'
for file in OUT.glob('*.pdf'):
    reader=PdfReader(file)
    before=[page.extract_text() for page in reader.pages]
    writer=PdfWriter();writer.clone_document_from_reader(reader)
    if '/Outlines' in writer.root_object:del writer.root_object['/Outlines']
    writer.root_object[NameObject('/Lang')]=TextStringObject('de-DE' if file.stem.endswith('-de') else 'en-GB')
    # Annotation-only updates; the existing text/font streams and page boxes remain intact.
    for page in writer.pages:
        if '/Annots' in page:del page['/Annots']
    count=0
    with pdfplumber.open(file) as document:
        for index,page in enumerate(document.pages):
            for word in page.extract_words():
                text=word['text'].strip('.,;')
                uri=None
                if text=='sagar.kriplani@outlook.com':uri='mailto:'+text
                elif text.startswith('linkedin.com/in/sagar-kriplani'):uri='https://www.linkedin.com/in/sagar-kriplani/'
                elif text.startswith('sagar-kriplani.github.io'):uri='https://'+text
                if uri:
                    writer.add_annotation(index,Link(rect=(word['x0'],page.height-word['bottom'],word['x1'],page.height-word['top']),url=uri))
                    count+=1
    writer.add_outline_item('Berufserfahrung' if file.stem.endswith('-de') else 'Experience',0)
    writer.add_outline_item('Projekte und Qualifikationen' if file.stem.endswith('-de') else 'Projects and qualifications',1)
    temporary=file.with_suffix('.linked.pdf')
    with temporary.open('wb') as stream:writer.write(stream)
    checked=PdfReader(temporary)
    assert [page.extract_text() for page in checked.pages]==before,'CV text changed'
    assert len(checked.pages)==2 and count>=4
    file.write_bytes(temporary.read_bytes());temporary.unlink()
    print(file.name,'2 pages; text preserved;',count,'links; language metadata set')

aliases={'CV_Sagar_Kriplani_General_EN.pdf':'general-en.pdf','CV_Sagar_Kriplani_Mechanical_Design_EN.pdf':'mechanical-en.pdf','CV_Sagar_Kriplani_RD_Engineer_EN.pdf':'rd-en.pdf','Lebenslauf_Sagar_Kriplani_Allgemein_DE.pdf':'general-de.pdf','Lebenslauf_Sagar_Kriplani_Konstruktion_DE.pdf':'mechanical-de.pdf','Lebenslauf_Sagar_Kriplani_FE_Entwicklung_DE.pdf':'rd-de.pdf','mechanical-design-en.pdf':'mechanical-en.pdf','mechanical-design-de.pdf':'mechanical-de.pdf','rd-engineer-en.pdf':'rd-en.pdf','rd-engineer-de.pdf':'rd-de.pdf'}
for folder in ('cv','assets/docs','public/cv'):
    for old,new in aliases.items():
        target=ROOT/folder/old
        if target.exists():shutil.copy2(OUT/new,target)
manifest=json.loads((OUT/'manifest.json').read_text())
manifest['pdfs']={file.name:hashlib.sha256(file.read_bytes()).hexdigest() for file in OUT.glob('*.pdf')}
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
