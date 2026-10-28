"""Check the published artifact, including links and bilingual content integrity."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

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
    assert text.count('data-category=')==4
    assert '70%' not in text and '200+' not in text and 'Blue Card' not in text
assert not (ROOT/'reference').exists()
assert not list(ROOT.rglob('*.pdf')), 'Do not republish legacy CV claims'
assert not (ROOT/'.git').exists()
print(f'PASS: {len(pages)} pages; internal assets, anchors, languages, IDs, alt text and publication boundaries.')
