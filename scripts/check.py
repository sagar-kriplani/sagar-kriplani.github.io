"""Check the published artifact, including links and bilingual content integrity."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
import json
import hashlib

ROOT=Path(__file__).resolve().parent.parent/'dist'
class Page(HTMLParser):
    def __init__(self,path):
        super().__init__(); self.path=path; self.ids=set(); self.links=[]; self.lang=None; self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, f'Duplicate ID {a["id"]} in {self.path}'
            self.ids.add(a['id'])
        if tag=='html': self.lang=a.get('lang')
        if tag=='h1': self.h1+=1
        if tag=='img': assert a.get('alt'), f'Missing alt in {self.path}'
        for attr in ('href','src'):
            if a.get(attr): self.links.append(a[attr])

pages={}
for path in ROOT.rglob('*.html'):
    p=Page(path); p.feed(path.read_text(encoding='utf-8')); pages[path.resolve()]=p
    assert p.lang in ('en','de') and p.h1==1, f'Page semantics: {path}'
for path,p in pages.items():
    for link in p.links:
        url=urlsplit(link)
        if url.scheme or url.netloc: continue
        target=(ROOT/unquote(url.path).lstrip('/')) if url.path.startswith('/') else (path.parent/unquote(url.path))
        if not url.path: target=path
        if target.is_dir(): target=target/'index.html'
        assert target.exists(), f'Broken local link in {path}: {link}'
        if url.fragment and target.resolve() in pages:
            assert url.fragment in pages[target.resolve()].ids, f'Broken anchor: {path} -> {link}'
for lang in ('en','de'):
    p=pages[(ROOT/lang/'index.html').resolve()]
    assert {'pau','machine','thesis','handling','work','experience','expertise','contact'}<=p.ids
    text=p.path.read_text(encoding='utf-8')
    assert text.count('data-category=')==7
    assert 'Blue Card' not in text
    for date in ['07/2023 – 06/2024','07/2023 – 01/2024','02/2024 – 06/2024','08/2020 – 09/2021']:
        assert date in text, f'Missing canonical career date: {date}'
    assert 'until June' not in text and 'bis Juni' not in text
    from sys import path as module_path
    module_path.insert(0,str(ROOT.parent/'scripts'))
    from evidence import RECORDS
    library=pages[(ROOT/lang/'evidence/index.html').resolve()]
    assert len(RECORDS)==29
    assert all(r['key'] in library.ids for r in RECORDS)
    assert len([r for r in RECORDS if r['group']=='certifications'])==16
    public_text=library.path.read_text(encoding='utf-8')
    # Generic patterns avoid placing the user's actual private identifiers in source control.
    for pattern in [r'(?i)(student id|enrollment number|matrikelnummer)\s*[:=]\s*\d{5,}',r'\b[A-Z]{2}\d{2}(?: ?\d){15,}\b']:
        assert not re.search(pattern, public_text), 'Private-identifier pattern in evidence HTML'
for forbidden in ['pau-assembly.webp','linkedin-concept.webp','linkedin-concept.webm']:
    assert not list(ROOT.rglob(forbidden)), 'Excluded employer imagery must not ship'
for extension in ['*.iam','*.ipt','*.step','*.stp']:
    assert not list(ROOT.rglob(extension)), 'Raw CAD must remain local'
assert (ROOT/'assets/evidence/process-flow.svg').exists()
assert '<text' not in (ROOT/'assets/evidence/process-flow.svg').read_text()
assert len(list((ROOT/'assets/gallery').glob('*.webp')))==96
assert not list(ROOT.rglob('*.mp4')), 'Only silent reviewed WebM ships'
assert not list(ROOT.rglob('*.docx'))
assert not (ROOT/'reference').exists()
assert {p.name for p in ROOT.rglob('*.pdf')} == {f'{kind}-{lang}.pdf' for kind in ('general','mechanical','rd') for lang in ('en','de')}, 'Only six reviewed CVs may ship'
assert not (ROOT/'.git').exists()
manifest=json.loads((ROOT/'assets/cv/manifest.json').read_text())
assert manifest['source_sha256']==hashlib.sha256((ROOT.parent/'scripts/career.py').read_bytes()).hexdigest(), 'Regenerate CVs after career content changes'
for name,digest in manifest['pdfs'].items():
    assert hashlib.sha256((ROOT/'assets/cv'/name).read_bytes()).hexdigest()==digest, 'CV file differs from reviewed manifest'
print(f'PASS: {len(pages)} pages; internal assets, anchors, languages, IDs, alt text and publication boundaries.')
