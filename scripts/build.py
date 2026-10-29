# -*- coding: utf-8 -*-
"""Build a bilingual, dependency-free portfolio. Only explicit public assets ship."""
from pathlib import Path
from html import escape
import json
import shutil
from copy import deepcopy
from mechanical_showcase import enclosure_visual, refine_mechanical
from recruitment import apply_profile, profile_navigation, case_content, case_outcome, PROFILES, manufacturing_diagram as manufacturing_preview
from ui import UI, icon, prepare_html, language_list
from projects import extend_projects, period
from career import apply_career, cv_body
from gallery import gallery_strip, gallery_intro, gallery_page, cad_page
from showcase import showcase
from evidence import enrich_copy, evidence_section, media_section, evidence_page, project_image, viewer, RECORDS

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'dist'
# Rebuild only the verified generated-output directory, preventing stale excluded assets.
assert OUT.resolve().parent == ROOT.resolve() and OUT.name == 'dist'
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(exist_ok=True)

COPY = {
'en': {
'title':'Mechanical Design & Development Engineer', 'nav':['Selected work','Experience','Expertise','Contact'],
'eyebrow':'MECHANICAL DESIGN · SCIENTIFIC INSTRUMENTATION',
'hero':'Thoughtful design.<br><em>Practical engineering.</em>',
'intro':'I’m Sagar Kriplani, a mechanical design and development engineer. I turn complex requirements into manufacturable machinery and carefully tested thermal systems.',
'location':'Heidenheim an der Brenz, Germany', 'work':'Explore my work', 'cv':'View my CV',
'portrait':'Sagar Kriplani, mechanical design and development engineer', 'caption':'Precision in the details. Perspective on the whole system.',
'bridge':'FROM CONCEPT TO PRODUCTION', 'bridgeText':'Custom machinery. Semiconductor equipment. Engineering decisions grounded in evidence.',
'metrics':[('21%','lower PAU cost','Reported project comparison'),('500 → 50','mbar pressure drop','PAU redesign · approx. values'),('48 → 18','kW heater capacity','Design capacity, not measured energy use')],
'section':'01 / SELECTED WORK', 'projectsTitle':'A closer look at<br>the engineering.', 'projectsIntro':'From production drawings to experimental validation. A selection of the problems I have worked on, and the decisions behind the designs.',
'filters':['All work','Machine design','Thermal & R&D','Academic'], 'read':'Explore case study', 'problem':'The challenge', 'approach':'My contribution', 'result':'Outcome & context',
'projects':[
{'id':'pau','cat':'thermal','tag':'BROOKS AUTOMATION · RESEARCH INTERNSHIP · 2023','title':'Less complexity.<br>Better process air.','short':'Redesigning the Process Air Unit for an EUV pod cleaner, from thermodynamic calculations to a more compact mechanical layout.','tools':['Thermodynamics','Mechanical layout','Component selection'],'problem':'Reassess an oversized clean-dry-air heating system, reduce pressure losses, and simplify the assembly within the available machine space.','approach':'Analysed air requirements and pressure losses, compared heater concepts, selected components, and developed the mechanical design and documentation.','result':'The July 2023 project report records about 21% lower PAU cost, pressure drop reduced from approximately 500 to 50 mbar, and a heater resized from 48 to 18 kW. These are project design comparisons; capacity reduction does not establish operating energy savings.','note':'Source: research internship report, abstract and conclusion (p. 53).','art':'pau'},
{'id':'machine','cat':'machine','tag':'NEST GMBH · MECHANICAL DESIGN · 2025–2026','title':'Designed for the<br>way it is made.','short':'Machine enclosures, sheet-metal assemblies, and welded structures for special-purpose machinery.','tools':['Autodesk Inventor','DFM / DFA','Production drawings'],'problem':'Translate machine requirements into practical structures that can be fabricated, assembled, and maintained.','approach':'Developed CAD assemblies, sheet-metal details, welded structures, production drawings, and BOMs. Coordinated design interfaces with production and suppliers, using SAGE ERP and revision-controlled documentation.','result':'A focus on manufacturable details, simpler assemblies, and clear production handover. The scope is documented in supplied CVs; exact cost, weight, drawing-volume, and platform-count claims are omitted because supporting project records were not available.','note':'Source: supplied mechanical-design CV; scope is self-reported. Illustration is conceptual.','art':'machine'},
{'id':'thesis','cat':'thermal','tag':'EAH JENA / BROOKS AUTOMATION · MASTER’S THESIS · 2025','title':'Test the idea.<br>Understand the trade-offs.','short':'Comparing radiant heaters and IR LEDs for polymer heating inside FOUP cleaner vacuum chambers.','tools':['Experimental design','FTIR / UV-Vis','Thermal measurement'],'problem':'Understand how different FOUP polymers respond to radiant heaters and LEDs, and evaluate the engineering trade-offs of a potential alternative heating method.','approach':'Investigated material absorption, selected LEDs, developed experimental arrangements, and compared heating behaviour and temperature distribution.','result':'The thesis found that LEDs offered more even surface heating in the tested arrangement, while conventional radiant heaters delivered better overall heating capacity and broader material compatibility. LED heat dissipation and temperature measurement remained limitations. This was a comparative investigation, not a production-ready LED replacement.','note':'Source: submitted thesis, 27 February 2025; discussion and conclusion (pp. 73–76).','art':'thermal'},
{'id':'handling','cat':'academic','tag':'EAH JENA · ADVANCED 3D CAD · 2022','title':'Movement, built<br>from first principles.','short':'An academic design project for an automated handling and manipulation tool, developed in Autodesk Inventor.','tools':['Mechanism design','Autodesk Inventor','Engineering calculations'],'problem':'Develop a mechanical concept for transferring products between conveyor systems.','approach':'Worked on the mechanism, CAD design, actuator selection, and supporting mechanical calculations as part of an advanced 3D CAD project.','result':'An academic design study demonstrating mechanical layout and design reasoning. No measured positioning accuracy, production deployment, or validated robot repeatability is claimed.','note':'Source: supplied academic project report and CV. Illustration is conceptual.','art':'handling'}],
'experienceLabel':'02 / EXPERIENCE', 'experienceTitle':'Different environments.<br>One engineering mindset.',
'jobs':[],
'experienceNote':'Industry roles and dates are presented separately from academic research. The master’s thesis was submitted in February 2025.',
'expertiseLabel':'03 / EXPERTISE', 'expertiseTitle':'The tools matter.<br>The judgement matters more.',
'skills':[['01','Design for manufacture','Autodesk Inventor · PTC Creo · Siemens NX','3D assemblies, sheet metal, welded structures, production drawings, and tolerance considerations.'],['02','Analysis & experimentation','ANSYS · MATLAB · Thermal measurement','Structural and thermal analysis, engineering calculations, test setup design, and interpretation of results.'],['03','Engineering delivery','BOM · SAGE ERP · Agile PLM','Revision control, technical documentation, component selection, and coordination with manufacturing.']],
'education':'EDUCATION', 'degrees':[],
'languages':'LANGUAGES','languageText':'German B2 · English C1<br>Hindi · Gujarati','languageNote':'Language levels as stated in my CV.',
'contactLabel':'04 / LET’S TALK', 'contactTitle':'Have a mechanical<br>challenge in mind?', 'contactText':'For mechanical design, development, and instrumentation opportunities, let’s discuss the problem and where I can contribute.', 'email':'Email me', 'copy':'Copy email', 'copied':'Email copied',
'footer':'Mechanical design. Clear thinking. Practical results.', 'legal':'Legal & privacy', 'back':'Back to portfolio', 'print':'Print / save as PDF', 'cvTitle':'Curriculum vitae', 'cvIntro':'Mechanical design and development across special-purpose machinery and semiconductor equipment, supported by postgraduate study in Scientific Instrumentation.', 'cvProjects':'Selected engineering projects', 'legalTitle':'Legal & privacy notice',
},
'de': {
'title':'Konstrukteur & Entwicklungsingenieur', 'nav':['Projekte','Erfahrung','Kompetenzen','Kontakt'],
'eyebrow':'KONSTRUKTION · SCIENTIFIC INSTRUMENTATION', 'hero':'Durchdacht konstruiert.<br><em>Für die Praxis entwickelt.</em>',
'intro':'Ich bin Sagar Kriplani, Konstrukteur und Entwicklungsingenieur. Aus komplexen Anforderungen entwickle ich fertigungsgerechte Maschinen und sorgfältig untersuchte thermische Systeme.',
'location':'Heidenheim an der Brenz, Deutschland','work':'Projekte entdecken','cv':'Lebenslauf ansehen', 'portrait':'Sagar Kriplani, Konstrukteur und Entwicklungsingenieur','caption':'Präzision im Detail. Das ganze System im Blick.',
'bridge':'VOM KONZEPT ZUR FERTIGUNG','bridgeText':'Sondermaschinenbau. Halbleiteranlagen. Technische Entscheidungen auf fundierter Grundlage.',
'metrics':[('21%','geringere PAU-Kosten','Vergleich laut Projektbericht'),('500 → 50','mbar Druckverlust','PAU-Redesign · Näherungswerte'),('48 → 18','kW Heizleistung','Auslegungsleistung, kein gemessener Energieverbrauch')],
'section':'01 / AUSGEWÄHLTE PROJEKTE','projectsTitle':'Ein genauerer Blick<br>auf die Entwicklung.','projectsIntro':'Von der Fertigungszeichnung bis zur experimentellen Untersuchung. Ausgewählte Aufgaben und die technischen Entscheidungen dahinter.',
'filters':['Alle Projekte','Konstruktion','Thermik & F&E','Studium'],'read':'Projekt im Detail','problem':'Die Aufgabe','approach':'Mein Beitrag','result':'Ergebnis & Einordnung',
'projects':[
{'id':'pau','cat':'thermal','tag':'BROOKS AUTOMATION · FORSCHUNGSPRAKTIKUM · 2023','title':'Weniger Komplexität.<br>Bessere Prozessluft.','short':'Neuentwicklung der Process Air Unit für einen EUV-Pod-Reiniger – von thermodynamischen Berechnungen bis zum kompakteren mechanischen Aufbau.','tools':['Thermodynamik','Mechanische Auslegung','Komponentenauswahl'],'problem':'Ein überdimensioniertes Luftheizsystem neu auslegen, Druckverluste reduzieren und die Baugruppe im verfügbaren Maschinenraum vereinfachen.','approach':'Luftbedarf und Druckverluste analysiert, Heizkonzepte verglichen, Komponenten ausgewählt sowie Konstruktion und Dokumentation des Systems erarbeitet.','result':'Der Projektbericht vom Juli 2023 nennt etwa 21 % geringere PAU-Kosten, einen Druckverlust von ungefähr 500 auf 50 mbar und eine angepasste Heizleistung von 48 auf 18 kW. Dies sind projektbezogene Auslegungsvergleiche; die geringere Nennleistung belegt keine gemessene Energieeinsparung.','note':'Quelle: Forschungspraktikumsbericht, Zusammenfassung und Fazit (S. 53).','art':'pau'},
{'id':'machine','cat':'machine','tag':'NEST GMBH · KONSTRUKTION · 2025–2026','title':'Konstruiert für<br>die Fertigung.','short':'Maschinengehäuse, Blechbaugruppen und Schweißkonstruktionen für den Sondermaschinenbau.','tools':['Autodesk Inventor','DFM / DFA','Fertigungszeichnungen'],'problem':'Maschinenanforderungen in praktikable Strukturen überführen, die sich fertigen, montieren und instand halten lassen.','approach':'CAD-Baugruppen, Blechdetails, Schweißkonstruktionen, Fertigungszeichnungen und Stücklisten entwickelt. Schnittstellen mit Fertigung und Lieferanten abgestimmt sowie SAGE ERP und revisionsgeführte Dokumentation genutzt.','result':'Schwerpunkt auf fertigungsgerechten Details, vereinfachten Baugruppen und einer klaren Übergabe an die Produktion. Der Aufgabenbereich ist in den bereitgestellten Lebensläufen beschrieben; konkrete Kosten-, Gewichts- und Mengenangaben entfallen mangels zugänglicher Projektbelege.','note':'Quelle: bereitgestellter Konstruktions-Lebenslauf; Aufgaben laut Eigenangabe. Schematische Illustration.','art':'machine'},
{'id':'thesis','cat':'thermal','tag':'EAH JENA / BROOKS AUTOMATION · MASTERARBEIT · 2025','title':'Ideen untersuchen.<br>Zielkonflikte verstehen.','short':'Vergleich von Strahlungsheizern und IR-LEDs zur Polymererwärmung in Vakuumkammern von FOUP-Reinigern.','tools':['Versuchsplanung','FTIR / UV-Vis','Thermische Messung'],'problem':'Das Erwärmungsverhalten verschiedener FOUP-Polymere untersuchen und die technischen Vor- und Nachteile alternativer Heizverfahren bewerten.','approach':'Materialabsorption untersucht, LEDs ausgewählt, Versuchsaufbauten entwickelt und Erwärmungsverhalten sowie Temperaturverteilung verglichen.','result':'LEDs zeigten im untersuchten Aufbau eine gleichmäßigere Oberflächenerwärmung. Konventionelle Strahlungsheizer boten dagegen insgesamt eine höhere Heizwirkung und breitere Materialkompatibilität. LED-Wärmeabfuhr und Temperaturmessung blieben Einschränkungen. Die Arbeit war eine Vergleichsuntersuchung, kein serienreifer LED-Ersatz.','note':'Quelle: Masterarbeit, eingereicht am 27. Februar 2025; Diskussion und Fazit (S. 73–76).','art':'thermal'},
{'id':'handling','cat':'academic','tag':'EAH JENA · ADVANCED 3D CAD · 2022','title':'Bewegung beginnt<br>mit dem Konzept.','short':'Akademische Konstruktion eines automatisierten Handhabungs- und Manipulationswerkzeugs in Autodesk Inventor.','tools':['Mechanismen','Autodesk Inventor','Technische Berechnung'],'problem':'Ein mechanisches Konzept für den Produkttransfer zwischen Förderbändern entwickeln.','approach':'Mechanismus, CAD-Konstruktion, Aktuatorauswahl und begleitende mechanische Berechnungen im Rahmen eines 3D-CAD-Studienprojekts bearbeitet.','result':'Eine akademische Konstruktionsstudie zu mechanischem Aufbau und technischer Auslegung. Gemessene Positioniergenauigkeit, Serieneinsatz oder validierte Wiederholgenauigkeit werden nicht behauptet.','note':'Quelle: bereitgestellter Studienprojektbericht und Lebenslauf. Schematische Illustration.','art':'handling'}],
'experienceLabel':'02 / BERUFSERFAHRUNG','experienceTitle':'Verschiedene Branchen.<br>Ein technischer Anspruch.',
'jobs':[],
'experienceNote':'Berufliche Tätigkeiten und Zeiträume werden getrennt von akademischer Forschung dargestellt. Die Masterarbeit wurde im Februar 2025 eingereicht.',
'expertiseLabel':'03 / KOMPETENZEN','expertiseTitle':'Gute Werkzeuge.<br>Fundierte Entscheidungen.',
'skills':[['01','Fertigungsgerechte Konstruktion','Autodesk Inventor · PTC Creo · Siemens NX','3D-Baugruppen, Blech- und Schweißkonstruktionen, Fertigungszeichnungen und Toleranzbetrachtung.'],['02','Analyse & Versuch','ANSYS · MATLAB · Thermische Messung','Strukturelle und thermische Analyse, technische Berechnungen, Versuchsaufbauten und Ergebnisbewertung.'],['03','Technische Umsetzung','Stücklisten · SAGE ERP · Agile PLM','Revisionsführung, technische Dokumentation, Komponentenauswahl und Abstimmung mit der Fertigung.']],
'education':'AUSBILDUNG','degrees':[],
'languages':'SPRACHEN','languageText':'Deutsch B2 · Englisch C1<br>Hindi · Gujarati','languageNote':'Sprachniveaus laut Lebenslauf.',
'contactLabel':'04 / KONTAKT','contactTitle':'Eine technische<br>Aufgabe im Kopf?','contactText':'Für Aufgaben in Konstruktion, Entwicklung und Instrumentierung: Lassen Sie uns über Ihre Anforderungen und meinen möglichen Beitrag sprechen.','email':'E-Mail schreiben','copy':'E-Mail kopieren','copied':'E-Mail kopiert',
'footer':'Durchdachte Konstruktion. Praktische Ergebnisse.','legal':'Impressum & Datenschutz','back':'Zum Portfolio','print':'Drucken / als PDF speichern','cvTitle':'Lebenslauf','cvIntro':'Konstruktion und Entwicklung im Sondermaschinen- und Halbleiteranlagenbau, ergänzt durch ein Masterstudium in Scientific Instrumentation.','cvProjects':'Ausgewählte Entwicklungsprojekte','legalTitle':'Impressum & Datenschutz',
}}

enrich_copy(COPY)
apply_career(COPY)
extend_projects(COPY)

def header(lang, c, sub=False):
    prefix = f'/{lang}/{sub}/' if sub in ('mechanical','research') else f'/{lang}/'
    links = ''.join(f'<a href="{prefix}#{i}">{escape(t)}</a>' for i,t in zip(['work','experience','expertise','evidence','contact'],c['nav']))
    return f'''<a class="skip" href="#main">{'Skip to content' if lang=='en' else 'Zum Inhalt'}</a>
    <header class="header"><a class="brand" href="{prefix}" aria-label="{UI[lang]['home']}"><span class="monogram">sk<span>.</span></span><span>SAGAR KRIPLANI<small>M.Sc. Scientific Instrumentation</small></span></a><nav aria-label="{'Main navigation' if lang=='en' else 'Hauptnavigation'}">{links}</nav><div class="utilities"><a class="language" href="/{'de' if lang=='en' else 'en'}/{str(sub)+'/' if sub else ''}" lang="{'de' if lang=='en' else 'en'}">{'DE' if lang=='en' else 'EN'} <span aria-hidden="true">↗</span></a><button class="theme" type="button" aria-label="{'Toggle dark theme' if lang=='en' else 'Dunkles Design umschalten'}" aria-pressed="false"><span aria-hidden="true">◐</span></button><button class="menu-toggle" type="button" aria-expanded="false" aria-label="{'Toggle menu' if lang=='en' else 'Menü umschalten'}" aria-controls="mobile-nav">{icon('menu')}</button></div><nav id="mobile-nav" class="mobile-nav" aria-label="{'Mobile navigation' if lang=='en' else 'Mobile Navigation'}" hidden>{links}</nav><noscript><nav class="no-js-nav" aria-label="{'Navigation without JavaScript' if lang=='en' else 'Navigation ohne JavaScript'}">{links}</nav></noscript></header>'''

def head(lang,c,title=None,path=None):
    path = path or f'/{lang}/'
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light dark"><title>{escape(title or ('Sagar Kriplani | '+c['title']))}</title><meta name="description" content="{escape(c['intro'],quote=True)}"><link rel="canonical" href="https://sagar-kriplani.github.io{path}"><link rel="alternate" hreflang="en" href="https://sagar-kriplani.github.io/en/{path.split('/',2)[-1] if path not in ['/en/','/de/'] else ''}"><link rel="alternate" hreflang="de" href="https://sagar-kriplani.github.io/de/{path.split('/',2)[-1] if path not in ['/en/','/de/'] else ''}"><link rel="alternate" hreflang="x-default" href="https://sagar-kriplani.github.io/"><meta property="og:title" content="Sagar Kriplani | {escape(c['title'])}"><meta property="og:description" content="{escape(c['intro'],quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="https://sagar-kriplani.github.io{path}"><meta property="og:image" content="https://sagar-kriplani.github.io/assets/images/sagar-kriplani.webp"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/site.css"><script src="/assets/site.js" defer></script></head><body id="page-top">{header(lang,c)}'''

def footer(lang,c):
    labels=UI[lang]
    return f'''<footer class="footer"><a class="footer-name" href="/{lang}/">Sagar Kriplani<span> {c['footer']}</span></a><span>© 2026</span><a href="/{lang}/legal/">{labels['legal']} ↗</a><a href="/{lang}/privacy/">{labels['privacy']} ↗</a><a class="footer-top" href="/{lang}/#top" aria-label="{labels['top']}">↑</a></footer><a class="back-to-top" href="#page-top" aria-label="{labels['top']}" hidden>{icon('up')}</a></body></html>'''


def art(kind):
    # Original conceptual diagrams; no employer drawings or confidential dimensions.
    common='<svg viewBox="0 0 640 400" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><defs><pattern id="grid-'+kind+'" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" stroke="currentColor" stroke-opacity=".08"/></pattern></defs><rect width="640" height="400" fill="url(#grid-'+kind+')"/>'
    if kind=='workflow':
        return common+'<g stroke="currentColor" stroke-width="2"><rect x="45" y="140" width="140" height="100" rx="8"/><rect x="250" y="140" width="140" height="100" rx="8"/><rect x="455" y="140" width="140" height="100" rx="8"/><path d="M185 190h65m-12-8 12 8-12 8M390 190h65m-12-8 12 8-12 8M525 240v65H115v-65m-8 12 8-12 8 12"/><path d="M75 165h80m-80 20h60m-60 20h70M275 195l35-35 50 20v35l-35 15-50-35 50-15 35 0m-35 15v35m-15-70 15 35M480 215h90m-80 0v-20m20 20v-45m20 45v-30m20 30v-60"/></g></svg>'
    if kind=='pau':
        lines='<g stroke="currentColor" stroke-width="2"><path d="M80 255H180V165H420V255H560" stroke-width="14" opacity=".12"/><path d="M80 255H180V165H420V255H560"/><rect x="220" y="128" width="150" height="74" rx="5"/><path d="M235 180l15-30 15 30 15-30 15 30 15-30 15 30 15-30 15 30" stroke="#c46b32"/><rect x="466" y="230" width="42" height="50" rx="3"/><circle cx="130" cy="255" r="15"/><path d="M130 240v-35m-15 0h30M190 315h230m-230-8v16m230-16v16"/><path d="M420 165h70m-10-7 10 7-10 7" stroke="#c46b32"/></g><g fill="currentColor" font-family="monospace" font-size="11"><text x="80" y="290">AIR IN</text><text x="244" y="112">HEATING MODULE</text><text x="467" y="302">FILTER</text><text x="268" y="343">SIMPLIFIED FLOW PATH</text></g>'
    elif kind=='machine':
        lines='<g stroke="currentColor" stroke-width="2"><path d="M170 130l200-55 130 85-200 60zM170 130v150l130 75V220m200-60v150l-200 45M170 280l200-55 130 85M370 75v150"/><path d="M195 151v112l80 48V199zM325 227l145-40v99l-145 40z" fill="currentColor" fill-opacity=".05"/><path d="M337 242l115-31v60l-115 31zM393 227v61" stroke="#c46b32"/><path d="M184 295v25m115 38v18m190-57v25M150 130l-25-15m45-15 190-52m20 4 125 83" stroke-dasharray="4 5"/></g><text x="70" y="365" fill="currentColor" font-family="monospace" font-size="11">CONCEPT / ENCLOSURE ASSEMBLY</text>'
    elif kind=='thermal':
        lines='<g stroke="currentColor" stroke-width="2"><rect x="110" y="95" width="420" height="220" rx="18"/><rect x="240" y="150" width="160" height="120" rx="8"/><path d="M255 172h130m-130 20h130m-130 20h130m-130 20h130m-130 20h130" opacity=".25"/><path d="M145 135v145m350-145v145" stroke="#c46b32" stroke-width="7"/><path d="M170 160q35 30 60 0m-60 45q35 30 60 0m-60 45q35 30 60 0M410 160q35 30 60 0m-60 45q35 30 60 0m-60 45q35 30 60 0" stroke="#c46b32"/><path d="M290 315v28h60v-28"/></g><g fill="currentColor" font-family="monospace" font-size="11"><text x="145" y="75">SOURCE</text><text x="270" y="135">POLYMER</text><text x="248" y="375">COMPARATIVE TEST SETUP</text></g>'
    else:
        lines='<g stroke="currentColor" stroke-width="2"><ellipse cx="300" cy="320" rx="110" ry="25"/><path d="M250 310v-30h100v30M275 280v-90l90-80 40 35-80 70v65"/><circle cx="300" cy="200" r="25"/><circle cx="385" cy="130" r="25"/><path d="M405 115l75 60-20 25-75-45M480 175l35-5 20 25-10 15-20-20-25 10"/><path d="M385 75a115 115 0 0 1 125 66m-13-5 13 5-1-14" stroke="#c46b32"/><path d="M170 335h310m-310 10h310" stroke-dasharray="5 5"/></g><text x="170" y="375" fill="currentColor" font-family="monospace" font-size="11">CONCEPT / HANDLING MECHANISM</text>'
    return common+lines+'</svg>'

def jobs(c):
    result=''
    for j in c['jobs']:
        description=j[4];context=''
        if c.get('focusedMechanical'):
            for marker in ('Project figures reported by me:', ' Von mir berichtete Projektkennzahlen:', 'Departure month confirmed by me;', 'Austrittsmonat von mir bestätigt;'):
                if marker in description:
                    description=description.split(marker,1)[0].strip()
                    context='<details class="job-context"><summary>'+('Project details & sources' if c.get('contentLanguage')=='en' else 'Projektangaben & Quellen')+'</summary><p>'+escape(j[4])+'</p></details>'
                    break
        result+=f'<article class="job"><p class="date">{j[0]}</p><div><h3>{j[1]}</h3><p class="role">{j[2]}</p><p class="place">{j[3]}</p><p class="job-description">{description}</p>{context}</div></article>'
    return result

def home(lang,profile='mechanical',route=None):
    c=deepcopy(COPY[lang])
    data=apply_profile(c,lang,profile)
    if profile=='mechanical':refine_mechanical(c,lang)
    c['profile']=profile
    c['hero']=data['title']
    c['eyebrow']='MECHANICAL DESIGN / DEVELOPMENT' if profile=='mechanical' and lang=='en' else 'KONSTRUKTION / ENTWICKLUNG' if profile=='mechanical' else 'R&D / SCIENTIFIC INSTRUMENTATION' if lang=='en' else 'F&E / WISSENSCHAFTLICHE INSTRUMENTIERUNG'
    c['metrics']=[('CAD','Manufacturing-ready documentation' if lang=='en' else 'Fertigungsgerechte Dokumentation','Inventor · drawings · BOM' if lang=='en' else 'Inventor · Zeichnungen · Stücklisten'),('DFM','Fabrication & assembly decisions' if lang=='en' else 'Fertigungs- und Montageentscheidungen','Sheet metal · welded structures' if lang=='en' else 'Blech- und Schweißkonstruktionen'),('M.Sc.','Scientific Instrumentation','EAH Jena · 2025')] if profile=='mechanical' else [('IR / LED','Comparative heating research' if lang=='en' else 'Vergleichende Heizversuche','Polymer absorption & temperature' if lang=='en' else 'Polymerabsorption & Temperatur'),('1.3','Master’s thesis grade' if lang=='en' else 'Note der Masterarbeit','Issued final transcript' if lang=='en' else 'Abschließender Notennachweis'),('M.Sc.','Scientific Instrumentation','EAH Jena · 2025')]
    cards=''
    for n,p in enumerate(c['projects']):
        content=case_content(p,lang) or ''.join(f'<div><h4>{c[label]}</h4><p>{p[label]}</p></div>' for label in ['problem','approach','result'])
        content+=gallery_strip(p['id'],lang)
        source_art=project_image(p['id'],lang)
        visual=source_art or (art(p['art']))
        if p['id']=='machine':visual=enclosure_visual(lang)
        illustration_label=('CONCEPTUAL ILLUSTRATION' if lang=='en' else 'SCHEMATISCHE ILLUSTRATION') if not source_art else ('SOURCE REPORT EXCERPT' if lang=='en' else 'AUSZUG AUS PROJEKTBERICHT')
        card=f'''<article class="project" data-category="{p['cat']}" id="{p['id']}"><div class="project-art">{visual}<span class="art-label">{illustration_label}</span><span class="art-no">0{n+1}</span></div><div class="project-content"><p class="eyebrow">{p['tag']}</p>{period(p['id'],lang)}<h3>{p['title']}</h3><p>{p['short']}</p><div class="tags">{''.join('<span>'+t+'</span>' for t in p['tools'])}</div><details class="case-details"><summary>{c['read']} <span aria-hidden="true">↗</span></summary><div class="case-content">{content}<section class="case-sources" id="{p['id']}-sources" tabindex="-1"><h4>{'Sources & evidence' if lang=='en' else 'Quellen & Nachweise'}</h4><p class="source">{p['note']}</p></section></div></details></div></article>'''
        cards+=card
    jumps=''
    filters=''.join(f'<button type="button" data-filter="{v}" aria-pressed="{"true" if i==0 else "false"}">{c["filters"][i]}</button>' for i,v in enumerate(['all','machine','thermal','academic']))
    skills=''.join(f'<article class="skill"><span class="skill-no">{s[0]}</span><h3>{s[1]}</h3><p class="skill-tools">{s[2]}</p><p>{s[3]}</p></article>' for s in c['skills'])
    degree_sources=['master-degree','bachelor-degree','diploma-degree']
    degrees=''.join(f'<li class="education-step"><p class="date">{escape(d[0])}</p><div><h3>{escape(d[1])}</h3><p>{escape(d[2])}</p><a class="text-link education-proof" href="/{lang}/evidence/#{source}">{"View qualification" if lang=="en" else "Abschlussnachweis ansehen"} <span aria-hidden="true">↗</span></a></div></li>' for d,source in zip(c['degrees'],degree_sources))
    metrics=''.join(f'<div class="metric"><strong>{m[0]}</strong><span>{m[1]}</span><small>{m[2]}</small></div>' for m in c['metrics'])
    result=head(lang,c,path=route or f'/{lang}/').replace(header(lang,c),header(lang,c,profile if route else False)).replace('<body id="page-top">',f'<body id="page-top" data-engineering-profile="{profile}">')+f'''<main id="main">{profile_navigation(lang,profile)}<section class="hero" id="top" data-role-profile="{profile}"><div class="hero-copy"><p class="eyebrow"><span class="tiny-cross">+</span> {c['eyebrow']}</p><h1>{escape(c['hero'])}</h1><p class="profile-industries">{c['industryText']}</p><p class="intro">{c['intro']}</p><ul class="hero-specialisms">{''.join('<li>'+item+'</li>' for item in data['specialisms'])}</ul><p class="role-fit">{escape(data['roles'])}</p><div class="hero-actions"><a class="button primary" href="#work">{c['work']} <span>↗</span></a><a class="button cv-primary" href="/assets/cv/{data['cv']}-{lang}.pdf" data-relevant-cv>{c['cv']} · PDF <span>↓</span></a></div><div class="hero-contact"><a href="https://www.linkedin.com/in/sagar-kriplani/">LinkedIn ↗</a><a href="mailto:sagar.kriplani@outlook.com">{'Contact' if lang=='en' else 'Kontakt'} ↗</a><a href="/{lang}/cv/">{'Read CV online / all versions' if lang=='en' else 'Lebenslauf online / alle Varianten'} ↗</a></div><p class="location"><span class="location-dot"></span>{c['location']}</p></div><figure class="portrait"><div class="portrait-frame"><a class="portrait-preview" href="/assets/images/sagar-kriplani.webp" data-viewer data-caption="{c['portrait']}"><img src="/assets/images/sagar-kriplani.webp" alt="{c['portrait']}" width="1000" height="1381" fetchpriority="high"></a></div><figcaption><span>+ M.Sc.</span>{c['caption']}</figcaption></figure></section>
    <section class="bridge"><p class="eyebrow">{c['bridge']}</p><p>{c['bridgeText']}</p><span aria-hidden="true">{icon('diagonal')}</span></section>
    <section class="metrics" aria-label="{'Selected technical evidence' if lang=='en' else 'Ausgewählte fachliche Nachweise'}">{metrics}</section>
    <section class="work section" id="work"><div class="section-heading"><div><p class="eyebrow">{c['section']}</p><h2>{c['projectsTitle']}</h2></div><p>{c['projectsIntro']}</p></div>{jumps}<div class="filters" role="group" aria-label="{'Filter projects' if lang=='en' else 'Projekte filtern'}">{filters}</div><p class="filter-status sr-only" role="status" aria-live="polite"></p><div class="projects" id="featured-projects">{cards}</div></section>
    <section class="experience section" id="experience"><div class="section-heading"><div><p class="eyebrow">{c['experienceLabel']}</p><h2>{c['experienceTitle']}</h2></div><p>{c['experienceNote']}</p></div><div class="jobs">{jobs(c)}</div><a class="text-link education-jump" href="#education">{'Explore my education timeline' if lang=='en' else 'Zur Ausbildungsübersicht'} <span aria-hidden="true">↓</span></a></section>
    <section class="expertise section" id="expertise"><p class="eyebrow">{c['expertiseLabel']}</p><h2>{c['expertiseTitle']}</h2><div class="skills">{skills}</div><div class="education" id="education"><div><p class="eyebrow">{c['education']}</p><h2 class="education-title">{'Education timeline' if lang=='en' else 'Ausbildung im Überblick'}</h2><p class="education-intro">{'From mechanical engineering to scientific instrumentation. Study periods are distinct from the dates on the award certificates.' if lang=='en' else 'Vom Maschinenbau zur wissenschaftlichen Instrumentierung. Studienzeiträume sind von den Ausstellungsdaten der Abschlussurkunden zu unterscheiden.'}</p><ol class="education-timeline">{degrees}</ol></div><div class="languages"><p class="eyebrow">{c['languages']}</p>{language_list(lang)}<p>{c['languageNote']}</p><a class="text-link" href="/{lang}/cv/">{c['cv']} ↗</a></div></div></section>
    <section class="contact" id="contact"><p class="eyebrow">{c['contactLabel']}</p><div class="contact-grid"><div><h2>{c['contactTitle']}</h2><p>{c['contactText']}</p></div><div class="contact-links"><a class="email-address" href="mailto:sagar.kriplani@outlook.com">sagar.kriplani@outlook.com <span>↗</span></a><button class="copy-email" type="button" data-copied="{c['copied']}">{c['copy']}</button><p class="copy-status" role="status" aria-live="polite"></p><a href="https://www.linkedin.com/in/sagar-kriplani/">LinkedIn <span>↗</span></a><a href="https://github.com/sagar-kriplani">GitHub <span>↗</span></a></div></div></section></main>'''+footer(lang,c)
    # Keep the profile introduction first; offer a visual route into the existing cases next.
    result=result.replace('<section class="bridge">',showcase(lang,profile)+'<section class="bridge">',1)
    result=result.replace('</head>', '<link rel="stylesheet" href="/assets/showcase.css"><script src="/assets/showcase.js" defer></script></head>',1)
    supporting=gallery_intro(lang)+evidence_section(lang,profile)+media_section(lang)
    result=result.replace('<section class="contact"',supporting+'<section class="contact"')
    result=result.replace('</main>', '</main>'+viewer(lang))
    return result

def cv(lang):
    c=COPY[lang]
    result=head(lang,c,c['cvTitle']+' | Sagar Kriplani',f'/{lang}/cv/')
    result+=f'<main id="main" class="cv-page"><div class="cv-actions"><a href="/{lang}/">← {c["back"]}</a><button class="button primary print-cv" type="button">{c["print"]}</button></div><p class="eyebrow">{c["cvTitle"]}</p><h1>Sagar Kriplani</h1><p class="cv-role">{c["title"]}</p><p>{c["location"]} · <a href="mailto:sagar.kriplani@outlook.com">sagar.kriplani@outlook.com</a><br><a href="https://www.linkedin.com/in/sagar-kriplani/">linkedin.com/in/sagar-kriplani</a></p><p>{c["cvIntro"]}</p><h2>{c["nav"][1]}</h2>{jobs(c)}<h2>{c["cvProjects"]}</h2>'
    # Use the same reviewed content as the downloadable PDFs.
    start=result.index('<h2>'+c['nav'][1]+'</h2>')
    result=result[:start]+cv_body(lang,c)+'</main>'+footer(lang,c)
    return result.replace(header(lang,c),header(lang,c,'cv'))


def legal(lang):
    c=COPY[lang];en=lang=='en'
    body=('<h2>Website operator</h2>' if en else '<h2>Websitebetreiber</h2>')+'<p>Sagar Kriplani<br><a href="mailto:sagar.kriplani@outlook.com">sagar.kriplani@outlook.com</a></p>'
    body+=('<h2>About the content</h2><p>This personal portfolio presents professional experience and academic work. Conceptual illustrations and source excerpts are identified. Project figures apply to their stated context; they are not general performance guarantees.</p>' if en else '<h2>Zu den Inhalten</h2><p>Dieses persönliche Portfolio stellt Berufserfahrung und akademische Arbeiten vor. Schematische Illustrationen und Quellenauszüge sind gekennzeichnet. Projektkennzahlen gelten im beschriebenen Kontext und sind keine allgemeinen Leistungszusagen.</p>')
    body+=f'<p><a href="/{lang}/privacy/">{UI[lang]["privacy"]} ↗</a></p>'
    return (head(lang,c,UI[lang]['legal']+' | Sagar Kriplani',f'/{lang}/legal/')+f'<main id="main" class="legal-page"><a href="/{lang}/">← {c["back"]}</a><h1>{UI[lang]["legal"]}</h1>{body}</main>'+footer(lang,c)).replace(header(lang,c),header(lang,c,'legal'))


def privacy(lang):
    c=COPY[lang];en=lang=='en'
    sections=(
      [('Contact','The operator is Sagar Kriplani. For questions about this website or personal data, email sagar.kriplani@outlook.com.'),
       ('Hosting','This static portfolio is hosted on GitHub Pages. Requests for pages and assets reach GitHub infrastructure, which may process technical data such as IP addresses, browser information and request times for delivery and security. The portfolio does not receive a visitor analytics dashboard.'),
       ('Cookies and browser preferences','The portfolio sets no cookies and includes no analytics, advertising, tracking pixels or embedded third-party media. Fonts and images load from this website. The theme control saves only your chosen light/dark setting in your browser under portfolio-theme, so it can be restored on return visits. It is not sent to the operator. Use the reset button below to remove that preference and return to your system setting.'),
       ('Protected document downloads','Document and project previews are publicly visible and can be saved or captured. Separate original-image downloads are delivered as password-encrypted packages. The password is used locally to decrypt the selected file; it is not sent to the operator or stored by this website. Once unlocked, a recipient can save the file. This does not revoke copies previously shared or published.'),
       ('Local CAD viewing','STL/OBJ files are read locally in the current browser tab. The viewer does not upload or persist their contents. Closing the tab discards the loaded viewer state.'),
       ('Links, email and clipboard','LinkedIn, GitHub and other external resources load only when you follow their links. Their own privacy terms then apply. Email links open your email application; there is no website contact-form database. The copy-email control writes the public email address to your clipboard only after you activate it.'),
       ('Questions and rights','You can contact the operator about access, correction, deletion, restriction or objection where applicable. Hosting-related data requests can also be addressed to GitHub. You may contact your competent data-protection authority. No specific hosting-log retention period is asserted by this portfolio.')]
      if en else
      [('Kontakt','Betreiber ist Sagar Kriplani. Bei Fragen zur Website oder zu personenbezogenen Daten schreiben Sie an sagar.kriplani@outlook.com.'),
       ('Hosting','Dieses statische Portfolio wird auf GitHub Pages bereitgestellt. Seiten- und Dateiaufrufe erreichen die Infrastruktur von GitHub. GitHub kann technische Angaben wie IP-Adresse, Browserinformationen und Zugriffszeit für Bereitstellung und Sicherheit verarbeiten. Das Portfolio erhält kein Besucheranalyse-Dashboard.'),
       ('Cookies und Browsereinstellungen','Das Portfolio setzt keine Cookies und verwendet keine Analysewerkzeuge, Werbung, Tracking-Pixel oder eingebetteten Fremdmedien. Schriftarten und Bilder werden von dieser Website geladen. Der Darstellungsumschalter speichert ausschließlich Ihre Hell-/Dunkel-Auswahl im Browser unter portfolio-theme, um sie bei weiteren Besuchen wiederherzustellen. Die Auswahl wird nicht an den Betreiber gesendet. Mit der Schaltfläche unten können Sie diese Einstellung löschen und zur Systemeinstellung zurückkehren.'),
       ('Geschützte Dokumentdownloads','Dokument- und Projektvorschauen sind öffentlich und können gespeichert oder aufgenommen werden. Gesonderte Originalbild-Downloads werden als passwortverschlüsselte Dateien bereitgestellt. Das Passwort wird lokal zum Entschlüsseln verwendet und weder an den Betreiber gesendet noch von der Website gespeichert. Nach dem Entsperren kann der Empfänger die Datei speichern. Frühere veröffentlichte oder geteilte Kopien werden dadurch nicht zurückgerufen.'),
       ('Lokale CAD-Ansicht','STL-/OBJ-Dateien werden lokal im aktuellen Browser-Tab gelesen. Der Betrachter lädt keine Dateiinhalte hoch und speichert sie nicht dauerhaft. Mit dem Schließen des Tabs wird der geladene Ansichtsstatus verworfen.'),
       ('Links, E-Mail und Zwischenablage','LinkedIn, GitHub und andere externe Angebote werden erst beim Öffnen ihrer Links geladen. Dort gelten die jeweiligen Datenschutzbedingungen. E-Mail-Links öffnen Ihr E-Mail-Programm; eine Kontaktformular-Datenbank gibt es nicht. Die Kopierfunktion schreibt die öffentliche E-Mail-Adresse erst nach Ihrer Aktivierung in die Zwischenablage.'),
       ('Fragen und Rechte','Sie können den Betreiber wegen Auskunft, Berichtigung, Löschung, Einschränkung oder Widerspruch kontaktieren, soweit diese Rechte anwendbar sind. Fragen zu Hostingdaten können auch an GitHub gerichtet werden. Sie können sich an die zuständige Datenschutzaufsicht wenden. Dieses Portfolio behauptet keine bestimmte Aufbewahrungsfrist für Hostingprotokolle.')])
    body=''.join(f'<section><h2>{title}</h2><p>{text}</p></section>' for title,text in sections)
    body+=f'<p><a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">{("GitHub privacy statement" if en else "Datenschutzerklärung von GitHub")} ↗</a></p><button class="button primary reset-theme" type="button">{("Reset saved theme" if en else "Gespeicherte Darstellung zurücksetzen")}</button><p class="theme-reset-status" role="status" aria-live="polite"></p>'
    return (head(lang,c,UI[lang]['privacy']+' | Sagar Kriplani',f'/{lang}/privacy/')+f'<main id="main" class="legal-page"><a href="/{lang}/">← {c["back"]}</a><h1>{UI[lang]["privacy"]}</h1>{body}</main>'+footer(lang,c)).replace(header(lang,c),header(lang,c,'privacy'))


for lang in COPY:
    for sub,html in [('',home(lang)),('mechanical',home(lang,'mechanical',f'/{lang}/mechanical/')),('research',home(lang,'research',f'/{lang}/research/')),('cv',cv(lang)),('legal',legal(lang)),('privacy',privacy(lang)),('evidence',evidence_page(lang,head,footer,COPY[lang]).replace(header(lang,COPY[lang]),header(lang,COPY[lang],'evidence'))),('gallery',gallery_page(lang,head,footer,COPY[lang],viewer).replace(header(lang,COPY[lang]),header(lang,COPY[lang],'gallery'))),('cad',cad_page(lang,head,footer,COPY[lang]).replace(header(lang,COPY[lang]),header(lang,COPY[lang],'cad')))]:
        target=OUT/lang/sub
        target.mkdir(parents=True,exist_ok=True)
        (target/'index.html').write_text(html,encoding='utf-8')
(OUT/'index.html').write_text(home('en').replace('https://sagar-kriplani.github.io/en/\"','https://sagar-kriplani.github.io/\"',1),encoding='utf-8')
# Keep root entrypoint usable for local review and straightforward Pages fallback.
(ROOT/'index.html').write_text((OUT/'index.html').read_text(encoding='utf-8'),encoding='utf-8')
for name in ['site.css','site.js','showcase.css','showcase.js','cad-viewer.js','favicon.svg']:
    shutil.copy2(ROOT/'assets'/name,OUT/'assets'/name) if (OUT/'assets').exists() else ((OUT/'assets').mkdir(),shutil.copy2(ROOT/'assets'/name,OUT/'assets'/name))
for directory in ['images','fonts','evidence','gallery','cv','protected']:
    shutil.copytree(ROOT/'assets'/directory,OUT/'assets'/directory,dirs_exist_ok=True)
(OUT/'.nojekyll').write_text('',encoding='utf-8')
(OUT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://sagar-kriplani.github.io/sitemap.xml\n',encoding='utf-8')
urls=['/','/en/','/de/','/en/mechanical/','/de/mechanical/','/en/research/','/de/research/','/en/cv/','/de/cv/','/en/legal/','/de/legal/','/en/privacy/','/de/privacy/','/en/evidence/','/de/evidence/','/en/gallery/','/de/gallery/','/en/cad/','/de/cad/']
(OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>https://sagar-kriplani.github.io'+u+'</loc></url>' for u in urls)+'</urlset>',encoding='utf-8')
(OUT/'404.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Page not found | Sagar Kriplani</title><link rel="stylesheet" href="/assets/site.css"><main class="legal-page"><p class="eyebrow">404 / PAGE NOT FOUND</p><h1>Let’s get you<br>back on track.</h1><a class="button primary" href="/">Back to portfolio ↗</a></main></html>',encoding='utf-8')
print('Built bilingual portfolio, CV pages, legal pages, sitemap and 404 in dist/.')

for page in OUT.rglob('*.html'):
    page.write_text(prepare_html(page.read_text(encoding='utf-8')),encoding='utf-8')
(ROOT/'index.html').write_text((OUT/'index.html').read_text(encoding='utf-8'),encoding='utf-8')
