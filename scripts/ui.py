"""Shared bilingual interface labels and dependency-free SVG controls."""
from html import escape
from html.parser import HTMLParser
from html.entities import html5
from pathlib import Path
import json

UI = {
    'en': dict(legal='Legal Notice', privacy='Privacy Policy', top='Back to top', home='Sagar Kriplani — Home', zoom_in='Zoom in', zoom_out='Zoom out', fit='Fit', close='Close viewer'),
    'de': dict(legal='Impressum', privacy='Datenschutz', top='Nach oben', home='Sagar Kriplani — Startseite', zoom_in='Vergrößern', zoom_out='Verkleinern', fit='Einpassen', close='Ansicht schließen'),
}
PATHS = {
    'external':'M7 17 17 7M7 7h10v10', 'right':'M5 12h14m-6-6 6 6-6 6',
    'left':'M19 12H5m6-6-6 6 6 6', 'up':'M12 19V5m-6 6 6-6 6 6',
    'down':'M12 5v14m-6-6 6 6 6-6', 'diagonal':'M7 7l10 10M7 17h10V7',
    'plus':'M12 5v14M5 12h14', 'minus':'M5 12h14', 'close':'m6 6 12 12M6 18 18 6',
    'menu':'M4 6h16M4 12h16M4 18h16',
    'lock':'M7 10V7a5 5 0 0 1 10 0v3M5 10h14v11H5zM12 14v3',
    'theme':'M20 13a8 8 0 1 1-9-9 6 6 0 0 0 9 9',
}
def icon(name):
    return f'<svg class="icon icon-{name}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="{PATHS[name]}"/></svg>'

ARROWS={'↗':'external','→':'right','←':'left','↑':'up','↓':'down','↘':'diagonal'}
VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
class ControlIcons(HTMLParser):
    """Replace arrows only in controls, preserving prose, metadata and engineering data."""
    def __init__(self):
        super().__init__(convert_charrefs=False);self.out=[];self.stack=[]
        manifest=Path(__file__).resolve().parent.parent/'assets/protected/manifest.json'
        records=json.loads(manifest.read_text(encoding='utf-8')) if manifest.exists() else []
        self.downloads={r['preview']:'/assets/protected/'+r['key']+'.skvault' for r in records if 'preview' in r}
    def handle_starttag(self,tag,attrs):
        markup=self.get_starttag_text()
        values=dict(attrs)
        if tag=='a' and 'data-viewer' in values and values.get('href') in self.downloads:
            markup=markup[:-1]+' data-download="'+escape(self.downloads[values['href']],quote=True)+'">'
        self.out.append(markup)
        if tag not in VOID:self.stack.append(tag)
    def handle_startendtag(self,tag,attrs):self.out.append(self.get_starttag_text())
    def handle_endtag(self,tag):
        self.out.append(f'</{tag}>')
        if tag in self.stack:
            self.stack=self.stack[:len(self.stack)-1-self.stack[::-1].index(tag)]
    def handle_data(self,data):
        if any(t in self.stack for t in ('a','button','summary')) and not any(t in self.stack for t in ('script','style','svg')):
            for char,name in ARROWS.items():data=data.replace(char,icon(name))
            if 'summary' in self.stack and data.strip()=='+':data=data.replace('+',icon('plus'))
        self.out.append(data)
    def handle_entityref(self,name):self.out.append('&'+name+';' if name+';' in html5 else '&amp;'+name)
    def handle_charref(self,name):self.out.append('&#'+name+';')
    def handle_decl(self,decl):self.out.append('<!'+decl+'>')
    def handle_comment(self,data):self.out.append('<!--'+data+'-->')

def prepare_html(html):
    parser=ControlIcons();parser.feed(html);parser.close();return ''.join(parser.out)


def language_list(lang):
    rows=([('German','Professional working'),('English','Full professional'),('Hindi','Native / bilingual'),('Gujarati','Native / bilingual'),('Sindhi','Native / bilingual')] if lang=='en' else [('Deutsch','Berufliche Arbeitskenntnisse'),('Englisch','Professionelle Kenntnisse'),('Hindi','Muttersprache / zweisprachig'),('Gujarati','Muttersprache / zweisprachig'),('Sindhi','Muttersprache / zweisprachig')])
    return '<dl class="language-list">'+''.join('<div><dt>'+escape(name)+'</dt><dd>'+escape(level)+'</dd></div>' for name,level in rows)+'</dl>'
