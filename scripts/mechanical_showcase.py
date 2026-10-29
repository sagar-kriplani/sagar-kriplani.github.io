"""Focused mechanical-profile presentation using the existing reviewed case content."""
from html import escape
import re
from recruitment import case_content, manufacturing_diagram
from projects import period

BRIEFS={
 'de':{
  'machine':dict(title='NeSt: Konstruktion für die Fertigung',overview='Mechanische Baugruppen, Maschinenverkleidungen sowie Blech- und Schweißkonstruktionen: von der CAD-Ausarbeitung und Fertigungsdokumentation bis zur Abstimmung mit Produktion und Lieferanten.',challenge='An einem 8-mm-Stahlblechteil rissen die Biegefreistellungen ein. Reparaturschweißungen und Nacharbeit folgten.',decision='Die problematische Biegung durch zwei Teile mit einer geplanten Schweißverbindung ersetzen.',result='Die Reparaturschweißungen und Nacharbeiten an den eingerissenen Freistellungen entfielen. Die geplante Schweißverbindung blieb Bestandteil der Konstruktion.'),
  'pau':dict(title='Brooks: Process Air Unit für EUV-Pod-Reiniger',overview='Prozessluftaufbereitung als mechanische Entwicklungsaufgabe: Heizerauslegung, Druckverlust, Komponentenauswahl und Integration in den vorhandenen Bauraum zusammen betrachten.',challenge='Eine überdimensionierte und komponentenreiche Heizanordnung vereinfachen, ohne die benötigte Prozessluftversorgung aus dem Blick zu verlieren.',decision='Heizanordnung zusammenfassen, den Strömungsweg vereinfachen und die Komponenten für den analysierten Bedarf auswählen.',result='Auslegungsvergleich: 48 → 18 kW, etwa 500 → 50 mbar Druckverlust und rund 4.200 € geringere PAU-Kosten. Keine gemessene Betriebsenergieeinsparung.'),
  'thesis':dict(title='Brooks / EAH Jena: FOUP-Erwärmung im Vakuum',overview='Interdisziplinäre Entwicklung zwischen Mechanik, Werkstoffen und Messtechnik: Strahlungsheizer und IR-LEDs für die Erwärmung von FOUP-Polymeren vergleichen.',challenge='Prüfen, ob IR-LEDs bei unterschiedlichen Materialabsorptionen die benötigte Erwärmung im untersuchten Prozess erreichen.',decision='Spektroskopie und vergleichende Heizversuche verbinden; Temperaturverteilung und Grenzen der Messmethode gemeinsam bewerten.',result='Für die untersuchte Werkstoffbreite und Gesamtheizaufgabe blieben Strahlungsheizer vorzuziehen. LEDs zeigten gleichmäßigere Erwärmung, aber Grenzen bei transparenten Polymeren und der Wärmeabfuhr.')},
 'en':{
  'machine':dict(title='NeSt: design that works in production',overview='Mechanical assemblies, machine enclosures, sheet-metal and welded structures: connecting CAD development and manufacturing documentation with production and supplier coordination.',challenge='The bend-relief slits in an 8 mm steel-sheet part tore during forming, leading to repair welding and rework.',decision='Replace the problematic bend with two parts and a planned welded joint.',result='Repair welding and rework at the torn reliefs were eliminated. The planned welded joint remained part of the design.'),
  'pau':dict(title='Brooks: Process Air Unit for EUV pod cleaning',overview='Process-air conditioning as an equipment-development problem: consider heater sizing, pressure loss, component selection and mechanical packaging together.',challenge='Simplify an oversized, component-heavy heating arrangement while meeting the analysed process-air duty.',decision='Consolidate the heating arrangement, simplify the flow path and select components for the analysed requirement.',result='Design comparison: 48 → 18 kW, approximately 500 → 50 mbar pressure drop and around €4,200 lower PAU cost. Not a measured operating-energy saving.'),
  'thesis':dict(title='Brooks / EAH Jena: FOUP heating in vacuum',overview='Interdisciplinary development connecting mechanics, materials and measurement: compare radiant heaters and IR LEDs for heating FOUP polymers.',challenge='Determine whether IR LEDs meet the tested heating duty across materials with different optical absorption.',decision='Combine spectroscopy with comparative heating tests; assess temperature distribution alongside the measurement limitations.',result='Radiant heaters remained preferable for the tested material range and overall heating duty. LEDs offered more uniform heating, with limits in transparent polymers and heat rejection.')}}

def refine_mechanical(c,lang):
    en=lang=='en'
    c['focusedMechanical']=True
    c['contentLanguage']=lang
    c['skills']=[row[:] for row in c['skills']]
    c['intro']=('I develop mechanical assemblies, machine enclosures and manufacturing documentation for industrial machinery. My special-purpose machinery experience is complemented by semiconductor equipment development and an M.Sc. in Scientific Instrumentation.' if en else 'Ich entwickle mechanische Baugruppen, Maschinenverkleidungen und Fertigungsunterlagen für industrielle Maschinen. Meine Praxiserfahrung im Sondermaschinenbau ergänze ich durch die Entwicklung von Halbleiteranlagen und einen M.Sc. Scientific Instrumentation.')
    c['projectsIntro']=('Three industrial and interdisciplinary cases: fabrication decisions at NeSt, process-air development at Brooks, and thermal research as an equipment-engineering differentiator.' if en else 'Drei industrielle und interdisziplinäre Fallstudien: Fertigungsentscheidungen bei NeSt, Prozessluftentwicklung bei Brooks und thermische Forschung als Ergänzung der Anlagenentwicklung.')
    c['projectsTitle']='Engineering decisions,<br>made tangible.' if en else 'Technische Entscheidungen.<br>Praktisch nachvollziehbar.'
    c['projects']=sorted(c['projects'],key=lambda p:['machine','pau','thesis','handling','ansys','frost','shoe','ai-cad'].index(p['id']))
    c['skills'][0][3]=('Assembly development, sheet-metal and welded structures, mechanical integration and manufacturing-oriented detailing with tolerance considerations.' if en else 'Baugruppenentwicklung, Blech- und Schweißkonstruktionen, mechanische Integration sowie fertigungsgerechte Detaillierung und Toleranzbetrachtung.')
    c['skills'][3][3]=('Manufacturing drawings, sheet-metal developments, BOMs, engineering changes and production coordination. SAGE ERP and Agile PLM support the documented workflow.' if en else 'Fertigungszeichnungen, Blechabwicklungen, Stücklisten, technische Änderungen und Produktionsabstimmung. SAGE ERP und Agile PLM ergänzen den dokumentierten Arbeitsablauf.')

def methodology(project,lang):
    content=case_content(project,lang)
    # Provenance remains available in the source subsection rather than interrupting the case narrative.
    replacements={
     'This account is confirmed by the project owner; proprietary drawings, weld sizes and customer geometry are not published.':'The schematic omits proprietary geometry and weld dimensions.',
     'The owner reports that repair welding and rework caused by the torn bend relief were eliminated.':'Repair welding and rework caused by the torn bend relief were eliminated.',
     'Der Projekteigentümer bestätigt diesen Ablauf; proprietäre Zeichnungen, Schweißnahtmaße und Kundengeometrien werden nicht veröffentlicht.':'Die schematische Darstellung zeigt keine proprietären Geometrien oder Schweißnahtmaße.',
     'Nach Angabe des Eigentümers entfielen die durch eingerissene Biegefreistellungen verursachten Reparaturschweißungen und Nacharbeiten.':'Die durch eingerissene Biegefreistellungen verursachten Reparaturschweißungen und Nacharbeiten entfielen.'}
    for old,new in replacements.items():content=content.replace(escape(old),escape(new))
    if project['id']=='machine':content=content.replace(manufacturing_diagram(lang),'')
    if project['id']=='thesis':content=re.sub(r'<figure><a href="/assets/gallery/thesis-06\.webp".*?</figure>','',content,flags=re.S)
    return content

def featured_card(project,lang,visual):
    en=lang=='en';key=project['id'];brief=BRIEFS[lang][key]
    rows=[('Engineering challenge' if en else 'Technische Aufgabe','challenge'),('Technical decision' if en else 'Konstruktionsentscheidung','decision'),('Result' if en else 'Ergebnis','result')]
    facts='<dl class="case-brief">'+''.join('<div><dt>'+label+'</dt><dd>'+escape(brief[field])+'</dd></div>' for label,field in rows)+'</dl>'
    note=project['note']
    if key=='machine':note=('The manufacturing incident, 8 mm thickness and qualitative outcome were confirmed by Sagar Kriplani on 29 October 2026. No independent fabrication or acceptance record was supplied. The NeSt employment reference supports the broader design/drawing scope; supplier/ERP details follow the supplied CV. The diagram is representative; customer geometry, numerical savings and weld specifications are not published.' if en else 'Fertigungsfall, 8-mm-Blechdicke und qualitatives Ergebnis wurden von Sagar Kriplani am 29. Oktober 2026 bestätigt. Ein unabhängiger Fertigungs- oder Abnahmenachweis liegt nicht vor. Das NeSt-Arbeitszeugnis belegt den allgemeinen Konstruktions-/Zeichnungsumfang; Lieferanten-/ERP-Angaben folgen dem Lebenslauf. Die Grafik ist eine Prinzipdarstellung ohne Kundengeometrie, Einsparquote oder Schweißspezifikation.')
    return f'''<article class="project featured industrial-case" data-category="{project['cat']}" id="{key}"><div class="project-art">{visual}<span class="art-label">{'REPRESENTATIVE DIAGRAM' if en and key=='machine' else 'PRINZIPDARSTELLUNG' if key=='machine' else 'SOURCE REPORT EXCERPT' if en else 'AUSZUG AUS PROJEKTBERICHT'}</span></div><div class="project-content"><p class="eyebrow">{escape(project['tag'])}</p>{period(key,lang)}<h3>{brief['title']}</h3><p class="case-overview">{escape(brief['overview'])}</p><div class="tags">{''.join('<span>'+escape(t)+'</span>' for t in project['tools'])}</div>{facts}<a class="text-link case-source-link" href="#{key}-sources" data-open-evidence>{'Sources & evidence' if en else 'Quellen & Nachweise'} ↗</a><details class="case-details"><summary>{'Methodology, evidence & limitations' if en else 'Methodik, Nachweise & Grenzen'} <span aria-hidden="true">↗</span></summary><div class="case-content">{methodology(project,lang)}<section class="case-sources" id="{key}-sources" tabindex="-1"><h4>{'Sources & evidence' if en else 'Quellen & Nachweise'}</h4><p>{escape(note)}</p></section></div></details></div></article>'''

def thesis_visual(lang):
    caption='FOUP heating comparison · thesis Figure 5-1' if lang=='en' else 'Vergleich der FOUP-Erwärmung · Masterarbeit Abb. 5-1'
    return f'<figure class="project-source-image"><a href="/assets/gallery/thesis-06.webp" data-viewer data-caption="{caption}"><img src="/assets/gallery/thesis-06.webp" alt="{caption}" loading="lazy" width="1200" height="600"></a><figcaption>{caption}</figcaption></figure>'

def project_jumps(lang):
    en=lang=='en'
    return '<nav class="project-jumps" aria-label="'+('Featured cases' if en else 'Fallstudien auswählen')+'">'+''.join(f'<a href="#{key}">{label}</a>' for key,label in [('machine','NeSt · '+('Manufacturing' if en else 'Industriekonstruktion')),('pau','Brooks · PAU'),('thesis','Brooks / EAH · FOUP'),('project-archive','Archive · 5' if en else 'Projektarchiv · 5')])+'</nav>'

def archive(cards,lang):
    en=lang=='en'
    return '<details class="project-archive" id="project-archive" data-context><summary>'+('Project archive · 5 academic, training & experimental projects' if en else 'Projektarchiv · 5 Studien-, Trainings- und Erprobungsprojekte')+'</summary><p>'+('Supporting work remains fully accessible here. ANSYS work is training; academic and personal exploration are not presented as industrial delivery.' if en else 'Ergänzende Arbeiten bleiben hier vollständig zugänglich. ANSYS-Aufgaben sind Training; Studien- und persönliche Erprobungsprojekte werden als solche eingeordnet.')+'</p><div class="projects archive-projects">'+cards+'</div></details>'

def supporting_context(gallery,linkedin,lang):
    return '<details class="supporting-context" data-context><summary>'+('Academic gallery & additional background' if lang=='en' else 'Akademische Galerie & weiterer Hintergrund')+'</summary>'+gallery+linkedin+'</details>'


def manufacturing_visual(lang):
    diagram=manufacturing_diagram(lang)
    labels=({'BEFORE: ONE BENT PART':'Bent part','AFTER: TWO PARTS + PLANNED WELD':'Two welded parts','Torn bend relief':'Torn relief','Repair welding / rework':'Repair / rework','Repair operation eliminated':'No repair operation'} if lang=='en' else {'VORHER: EIN BIEGETEIL':'Biegeteil','NACHHER: ZWEI TEILE + SCHWEISSNAHT':'Zwei Schweißteile','Eingerissene Freistellung':'Riss an Freistellung','Geplante Verbindung':'Schweißverbindung','Reparaturschweißen / Nacharbeit':'Reparatur / Nacharbeit','Reparaturarbeit entfällt':'Keine Reparatur'})
    for old,new in labels.items():diagram=diagram.replace(old,new)
    return diagram.replace('font-size="13"','font-size="26"')
