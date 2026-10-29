"""Role-specific recruitment paths and source-reviewed engineering reasoning."""
from html import escape

PROFILES={
 'mechanical':{
  'en':dict(title='Mechanical Design & Development Engineer',hero='Mechanical design.<br><em>Ready for manufacture.</em>',intro='I’m Sagar Kriplani, a mechanical design engineer with an M.Sc. in Scientific Instrumentation. I develop machine enclosures, mechanical assemblies and production drawings, connecting CAD decisions with fabrication and assembly.',specialisms=['Special-purpose machinery','Sheet metal & welded structures','DFM / DFA','Precision assemblies'],cv='mechanical',roles='For mechanical design, development and equipment engineering roles.',order=['machine','pau','handling','thesis','ai-cad','ansys','frost','shoe']),
  'de':dict(title='Konstruktions- und Entwicklungsingenieur',hero='Mechanisch durchdacht.<br><em>Fertigungsgerecht entwickelt.</em>',intro='Ich bin Sagar Kriplani, Konstruktionsingenieur mit M.Sc. Scientific Instrumentation. Ich entwickle Maschinenverkleidungen, mechanische Baugruppen und Fertigungszeichnungen und verbinde CAD-Entscheidungen mit der Fertigung und Montage.',specialisms=['Sondermaschinenbau','Blech- und Schweißkonstruktionen','DFM / DFA','Präzisionsbaugruppen'],cv='mechanical',roles='Für Positionen in Konstruktion, Entwicklung und Anlagentechnik.',order=['machine','pau','handling','thesis','ai-cad','ansys','frost','shoe'])},
 'research':{
  'en':dict(title='R&D Engineer | M.Sc. Scientific Instrumentation',hero='Develop the experiment.<br><em>Understand the system.</em>',intro='I’m Sagar Kriplani, a mechanical engineer with an M.Sc. in Scientific Instrumentation. My research and development work connects semiconductor equipment, vacuum heating, material absorption and experimental thermal evaluation.',specialisms=['Semiconductor equipment','Vacuum & thermal systems','IR heating & materials','Experiments & measurement'],cv='rd',roles='For R&D, equipment development and mechanical/thermal engineering roles.',order=['thesis','pau','ansys','frost','machine','handling','ai-cad','shoe']),
  'de':dict(title='Entwicklungsingenieur | M.Sc. Scientific Instrumentation',hero='Versuche entwickeln.<br><em>Systeme verstehen.</em>',intro='Ich bin Maschinenbauingenieur Sagar Kriplani mit M.Sc. Scientific Instrumentation. Meine Forschungs- und Entwicklungsarbeit verbindet Halbleiteranlagen, Vakuumerwärmung, Materialabsorption und experimentelle thermische Untersuchungen.',specialisms=['Halbleiteranlagen','Vakuum- und Thermalsysteme','IR-Erwärmung & Werkstoffe','Versuchsplanung & Messtechnik'],cv='rd',roles='Für Positionen in F&E, Anlagenentwicklung und mechanisch-thermischer Entwicklung.',order=['thesis','pau','ansys','frost','machine','handling','ai-cad','shoe'])}}

SKILLS={
 'en':[
 ['01','Mechanical engineering','Assembly design · DFM / DFA','Sheet-metal and welded structures, mechanical integration, tolerance considerations and production-oriented detailing. GD&T and tolerance analysis are relevant design methods; no advanced specialist certification is claimed.'],
 ['02','CAD & engineering tools','Autodesk Inventor · Creo Parametric · Siemens NX','Inventor assemblies and manufacturing drawings in professional work. Creo/NX according to supplied CVs and training. ANSYS and MATLAB demonstrated through academic and training work.'],
 ['03','Thermal & scientific methods','Heat transfer · IR absorption · Vacuum heating','Comparative heating experiments, spectroscopy, temperature evaluation and interpretation of measurement limitations. Evidence: PAU internship and master’s thesis.'],
 ['04','Manufacturing & documentation','Drawings · BOMs · Engineering changes','Sheet-metal developments, production documentation and manufacturing coordination. SAGE ERP and Agile PLM according to supplied CVs; no blanket DIN/ISO-compliance certification is implied.']],
 'de':[
 ['01','Mechanische Entwicklung','Baugruppenentwicklung · DFM / DFA','Blech- und Schweißkonstruktionen, mechanische Integration, Toleranzbetrachtung und fertigungsgerechte Detaillierung. Form- und Lagetolerierung sowie Toleranzanalyse sind relevante Methoden; keine fortgeschrittene Spezialzertifizierung wird behauptet.'],
 ['02','CAD & technische Werkzeuge','Autodesk Inventor · Creo Parametric · Siemens NX','Inventor-Baugruppen und Fertigungszeichnungen in der Berufspraxis. Creo/NX gemäß Lebenslauf und Schulungsnachweisen. ANSYS und MATLAB anhand von Studien- und Trainingsarbeiten.'],
 ['03','Thermische & wissenschaftliche Methoden','Wärmeübertragung · IR-Absorption · Vakuumerwärmung','Vergleichende Heizversuche, Spektroskopie, Temperaturauswertung und Einordnung von Messgrenzen. Nachweise: PAU-Praktikum und Masterarbeit.'],
 ['04','Fertigung & Dokumentation','Technische Zeichnungen · Stücklisten · Änderungen','Blechabwicklungen, Fertigungsdokumentation und Produktionsabstimmung. SAGE ERP und Agile PLM gemäß Lebenslauf; keine pauschale DIN-/ISO-Konformitätszertifizierung.']]}

CASES={
 'machine':{'en': [('Engineering problem', 'Develop machine enclosures and mechanical assemblies for special-purpose machinery, connecting machine requirements with fabrication and assembly.'), ('Requirements & constraints', 'Consider equipment interfaces, sheet-metal and welded construction, manufacturability and assembly access. Customer geometry and internal manufacturing drawings remain confidential.'), ('Technical analysis', 'Work through assembly interfaces, component detailing and production requirements using Autodesk Inventor and DFM/DFA principles.'), ('Design decision', 'Develop the enclosure as coordinated mechanical assemblies, with manufacturing details and documentation considered alongside the CAD design.'), ('Implementation', 'Prepared CAD assemblies, sheet-metal details, manufacturing drawings and BOMs; coordinated revisions with production. Supplier coordination and ERP workflow are described in the supplied CV.'), ('Result & scope', 'Delivered mechanical designs and manufacturing documentation within the documented NeSt role. No project-specific cost saving, weight reduction or acceptance measurement is claimed in this case.')], 'de': [('Technische Aufgabe', 'Maschinenverkleidungen und mechanische Baugruppen für den Sondermaschinenbau entwickeln und Maschinenanforderungen mit Fertigung und Montage verbinden.'), ('Anforderungen & Randbedingungen', 'Anlagenschnittstellen, Blech- und Schweißkonstruktionen, Fertigbarkeit und Montagezugänglichkeit berücksichtigen. Kundengeometrien und interne Fertigungszeichnungen bleiben vertraulich.'), ('Technische Analyse', 'Baugruppenschnittstellen, Bauteildetails und Fertigungsanforderungen mit Autodesk Inventor sowie DFM/DFA-Grundsätzen bearbeiten.'), ('Konstruktionsentscheidung', 'Die Maschinenverkleidung als abgestimmte mechanische Baugruppen entwickeln und Fertigungsdetails sowie Dokumentation zusammen mit der CAD-Konstruktion ausarbeiten.'), ('Umsetzung', 'CAD-Baugruppen, Blechdetails, Fertigungszeichnungen und Stücklisten erstellt; Änderungen mit der Produktion abgestimmt. Lieferantenabstimmung und ERP-Ablauf sind im bereitgestellten Lebenslauf beschrieben.'), ('Ergebnis & Umfang', 'Mechanische Konstruktionen und Fertigungsunterlagen im belegten NeSt-Tätigkeitsbereich erarbeitet. Diese Fallstudie behauptet keine projektspezifischen Kosten-, Gewichts- oder Abnahmemesswerte.')]},
 'pau':{
  'en':[
   ('Engineering problem','The existing Process Air Unit for an EUV pod cleaner combined excess heater design capacity, pressure losses and a complex mechanical layout.'),
   ('Requirements & constraints','Supply the required heated process air while fitting the available equipment space. Consider flow, pressure/temperature requirements, component interfaces, fabrication and integration without disclosing proprietary geometry.'),
   ('Technical analysis','Compared the air-heating requirement with the installed heater capacity; assessed pressure losses and component selection. The report includes pipe/flange design checks and a comparative component-cost calculation.'),
   ('Design decision','Consolidate the heating arrangement and simplify the flow path rather than retain an oversized, component-heavy layout. Select a heater sized for the analysed duty and reduce unnecessary transitions and fittings.'),
   ('Implementation','Developed the mechanical arrangement, component selection and design documentation. The public schematic shows only the process logic; employer CAD and equipment photographs remain excluded.'),
   ('Documented result','The report compares 48 → 18 kW heater design capacity and approximately 500 → 50 mbar pressure drop. It reports about €4,200 lower PAU cost, approximately 21%. These are report-based design/cost comparisons; capacity reduction is not measured operating-energy saving.')],
  'de':[
   ('Technische Aufgabe','Die vorhandene Process Air Unit eines EUV-Pod-Reinigers verband überhöhte Heizerauslegung, Druckverluste und einen komplexen mechanischen Aufbau.'),
   ('Anforderungen & Randbedingungen','Benötigte erwärmte Prozessluft innerhalb des verfügbaren Anlagenbauraums bereitstellen. Volumenstrom, Druck-/Temperaturanforderungen, Schnittstellen, Fertigung und Integration berücksichtigen, ohne proprietäre Geometrien offenzulegen.'),
   ('Technische Analyse','Wärmebedarf und installierte Heizerauslegung verglichen; Druckverluste und Komponentenauswahl bewertet. Der Bericht enthält Rohr-/Flanschprüfungen und eine vergleichende Bauteilkalkulation.'),
   ('Konstruktionsentscheidung','Die Heizanordnung zusammenfassen und den Strömungsweg vereinfachen, statt den überdimensionierten Aufbau mit vielen Einzelkomponenten beizubehalten. Einen für den analysierten Bedarf ausgelegten Heizer wählen und unnötige Übergänge reduzieren.'),
   ('Umsetzung','Mechanische Anordnung, Komponentenauswahl und Konstruktionsdokumentation erarbeitet. Das öffentliche Schema zeigt ausschließlich die Prozesslogik; Arbeitgeber-CAD und Anlagenfotos bleiben ausgeschlossen.'),
   ('Dokumentiertes Ergebnis','Der Bericht vergleicht 48 → 18 kW Heizerauslegung und etwa 500 → 50 mbar Druckverlust. Er nennt rund 4.200 € geringere PAU-Kosten beziehungsweise etwa 21 %. Dies sind Auslegungs-/Kostenvergleiche aus dem Bericht; eine geringere Heizerauslegung ist keine gemessene Betriebsenergieeinsparung.')]},
 'thesis':{
  'en':[
   ('Research question','Could infrared LEDs replace radiant heaters for polymer heating within FOUP-cleaner vacuum chambers, across materials with different optical absorption?'),
   ('Requirements & test conditions','Compare black EBM and transparent polycarbonate under the stated test cycle and source-to-surface distances. The methodology reports 20 °C ambient and a 0.03 kPa vacuum condition; no independent chamber log was supplied.'),
   ('Technical analysis','Used FTIR and visible/near-IR absorption measurements to compare spectral response and select 940 nm LEDs. Evaluated surface-temperature observations and distribution, not electrical input alone.'),
   ('Engineering decision','Conventional radiant heaters remained preferable for the tested overall heating duty and material range. LEDs showed more uniform heating and potential for selective absorption, but transparent polymers and LED heat rejection limited substitution.'),
   ('Experimental implementation','Developed mechanical supports and vacuum-compatible electrical integration for comparative source arrangements. Used post-cycle infrared-camera readings and irreversible temperature strips. These are not continuous in-situ temperature measurements.'),
   ('Findings & limitations','The source plots below show the tested black-polymer response. Treat nominal power × time as an electrical-input comparison, not absorbed thermal energy or full-system efficiency. Venting/cooling before measurement, emissivity, LED heat dissipation and short test duration limit the conclusions.')],
  'de':[
   ('Forschungsfrage','Können Infrarot-LEDs Strahlungsheizer zur Polymererwärmung in FOUP-Reiniger-Vakuumkammern ersetzen – auch bei Werkstoffen mit unterschiedlicher optischer Absorption?'),
   ('Anforderungen & Versuchsbedingungen','Schwarzes EBM und transparentes Polycarbonat unter den angegebenen Heizzyklen und Abständen vergleichen. Die Methodik nennt 20 °C Umgebungstemperatur und 0,03 kPa Vakuumbedingung; ein unabhängiges Kammerprotokoll liegt nicht vor.'),
   ('Technische Analyse','FTIR- und sichtbare/Nahinfrarot-Absorptionsmessungen zur Bewertung des spektralen Verhaltens und Auswahl von 940-nm-LEDs genutzt. Oberflächentemperatur und Temperaturverteilung bewertet, nicht allein die elektrische Eingangsleistung.'),
   ('Technische Entscheidung','Für die untersuchte Gesamtheizaufgabe und Werkstoffbreite blieben konventionelle Strahlungsheizer vorzuziehen. LEDs zeigten gleichmäßigere Erwärmung und Potenzial für selektive Absorption; transparente Polymere und die LED-Wärmeabfuhr begrenzten den Ersatz.'),
   ('Versuchsumsetzung','Mechanische Halterungen und vakuumgeeignete elektrische Integration für vergleichende Quellenanordnungen entwickelt. IR-Kamera-Messungen nach dem Heizzyklus und irreversible Temperaturmessstreifen verwendet; keine kontinuierliche In-situ-Thermometrie.'),
   ('Erkenntnisse & Grenzen','Die untenstehenden Originaldiagramme zeigen die untersuchte Reaktion des schwarzen Polymers. Nennleistung × Zeit ist ein Vergleich elektrischer Eingangsenergie, keine absorbierte Wärmeenergie oder Gesamtanlageneffizienz. Abkühlung/Belüftung vor der Messung, Emissionsgrad, LED-Wärmeabfuhr und kurze Versuchsdauer begrenzen die Aussagekraft.')]}}

def profile_navigation(lang,selected):
    labels=[('mechanical','Mechanical Design' if lang=='en' else 'Konstruktion'),('research','R&D / Equipment Development' if lang=='en' else 'F&E / Anlagenentwicklung')]
    return '<nav class="profile-switch" aria-label="'+('Engineering profile' if lang=='en' else 'Ingenieurprofil')+'">'+''.join(f'<a href="/{lang}/{key}/" data-profile="{key}"'+(' aria-current="page"' if selected==key else '')+'>'+escape(label)+'</a>' for key,label in labels)+'</nav>'

def apply_profile(c,lang,profile):
    data=PROFILES[profile][lang]
    for key in ['title','hero','intro']:c[key]=data[key]
    c['skills']=SKILLS[lang]
    c['read']='Explore case study' if lang=='en' else 'Fallstudie ansehen'
    c['work']='View engineering projects' if lang=='en' else 'Technische Projekte ansehen'
    c['cv']='Download relevant CV' if lang=='en' else 'Passenden Lebenslauf herunterladen'
    c['eyebrow']=data['title']
    c['bridgeText']='Special-purpose machinery | Semiconductor equipment | Precision & thermal systems' if lang=='en' else 'Sondermaschinenbau | Halbleiteranlagen | Präzisions- und Thermalsysteme'
    c['industryText']=c['bridgeText']
    c['bridgeText']=(('Requirements → assemblies → manufacturing drawings → fabrication feedback.' if lang=='en' else 'Anforderungen → Baugruppen → Fertigungszeichnungen → Rückmeldung aus der Fertigung.') if profile=='mechanical' else ('Material response → comparative experiments → measurement limits → engineering decision.' if lang=='en' else 'Materialverhalten → Vergleichsversuche → Messgrenzen → technische Entscheidung.'))
    c['experienceNote']='Roles, research and internship periods are shown separately. Find the matching CV above; document previews and source context are available in the evidence library.' if lang=='en' else 'Berufstätigkeit, Forschung und Praktikum sind getrennt dargestellt. Den passenden Lebenslauf finden Sie oben; Dokumentvorschauen und Quellenkontext in der Nachweisbibliothek.'
    c['projects']=sorted(c['projects'],key=lambda p:data['order'].index(p['id']))
    for project in c['projects']:
        if project['id']=='machine':
            project['title']='NeSt: machine enclosures & assemblies' if lang=='en' else 'NeSt: Maschinenverkleidungen & Baugruppen'
            project['short']='Industrial enclosure and assembly development, from CAD detailing to manufacturing documentation and production coordination.' if lang=='en' else 'Maschinenverkleidungen und Baugruppen: von der CAD-Detaillierung über Fertigungsunterlagen bis zur Produktionsabstimmung.'
            project['note']='Sources: NeSt employment reference for the broader design and drawing scope; supplied mechanical-design CV for detailed responsibilities, supplier coordination and ERP workflow. Conceptual visual, not a customer design. No project-specific performance metrics are asserted.' if lang=='en' else 'Quellen: NeSt-Arbeitszeugnis für den allgemeinen Konstruktions- und Zeichnungsumfang; bereitgestellter Konstruktions-Lebenslauf für detaillierte Aufgaben, Lieferantenabstimmung und ERP-Ablauf. Prinzipdarstellung, keine Kundenkonstruktion. Keine projektspezifischen Leistungskennzahlen.'
        if project['id']=='pau':project['note']+=' '+('Cost basis: report p. 52; conclusion p. 53. Rounded outcome, not an audited lifecycle saving. Space percentage is not asserted.' if lang=='en' else 'Kostenbasis: Bericht S. 52; Fazit S. 53. Gerundetes Ergebnis, keine geprüfte Lebenszyklusersparnis. Kein behaupteter Bauraum-Prozentsatz.')
    return data

def manufacturing_diagram(lang):
    labels=['CAD assemblies','Manufacturing details','Production handover'] if lang=='en' else ['CAD-Baugruppen','Fertigungsdetails','Produktionsübergabe']
    title='Representative enclosure-development workflow' if lang=='en' else 'Schematischer Ablauf der Gehäuseentwicklung'
    boxes=''.join(f'<rect x="{20+i*215}" y="70" width="190" height="100" rx="8"/><text fill="currentColor" stroke="none" font-size="15" x="{115+i*215}" y="125" text-anchor="middle">{label}</text>' for i,label in enumerate(labels))
    return f'<figure class="manufacturing-diagram"><svg viewBox="0 0 660 220" role="img" aria-label="{title}"><title>{title}</title><g stroke="currentColor" fill="none" stroke-width="2">{boxes}<path d="M212 120h20m-7-6 7 6-7 6M427 120h20m-7-6 7 6-7 6"/></g></svg><figcaption>{title}</figcaption></figure>'


def comparison_table(lang,project):
    en=lang=='en'
    if project=='pau':
        headers=['Quantity','Previous design','Revised design','Interpretation'] if en else ['Größe','Bisherige Auslegung','Überarbeitete Auslegung','Einordnung']
        rows=[['Heater capacity' if en else 'Heizerauslegung','48 kW','18 kW','Design capacity; not measured energy' if en else 'Auslegung; keine gemessene Energie'],['Pressure drop' if en else 'Druckverlust','≈ 500 mbar','≈ 50 mbar','Reported project comparison' if en else 'Vergleich laut Projektbericht'],['PAU cost' if en else 'PAU-Kosten','—','≈ €4,200 lower' if en else '≈ 4.200 € geringer','Rounded component-cost estimate; ≈ 21%' if en else 'Gerundete Bauteilkalkulation; ≈ 21 %']]
        caption='Report-based before/after comparison · internship report pp. 52–53' if en else 'Vorher-/Nachher-Vergleich laut Praktikumsbericht S. 52–53'
    else:
        headers=['Source / distance','60 s','120 s','180 s'] if en else ['Quelle / Abstand','60 s','120 s','180 s']
        rows=[['LED · 20 mm','46.8 °C','57.2 °C','65.2 °C'],['LED · 40 mm','41.8 °C','49.8 °C','55.1 °C'],['LED · 60 mm','34.0 °C','36.5 °C','45.8 °C'],['Radiant heater' if en else 'Strahlungsheizer','37.5 °C','51.2 °C','65.2 °C']]
        if not en:rows=[[cell.replace('.',',') for cell in row] for row in rows]
        caption='Black-polymer surface observations · thesis Fig. 5-1, p. 63. Selected post-cycle points, not continuous in-situ readings.' if en else 'Oberflächenwerte schwarzes Polymer · Masterarbeit Abb. 5-1, S. 63. Ausgewählte Werte nach dem Heizzyklus, keine kontinuierlichen In-situ-Messungen.'
    return '<div class="table-scroll case-table" tabindex="0" aria-label="'+('Scrollable engineering comparison' if en else 'Horizontal scrollbarer technischer Vergleich')+'"><table><caption>'+caption+'</caption><thead><tr>'+''.join('<th scope="col">'+escape(h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr><th scope="row">'+escape(row[0])+'</th>'+''.join('<td>'+escape(x)+'</td>' for x in row[1:])+'</tr>' for row in rows)+'</tbody></table></div>'

def case_content(project,lang):
    key=project['id'];en=lang=='en'
    if key not in CASES:return None
    steps='<ol class="engineering-steps">'+''.join(f'<li><h4><span>{i:02}</span>{escape(title)}</h4><p>{escape(body)}</p></li>' for i,(title,body) in enumerate(CASES[key][lang],1))+'</ol>'
    if key=='machine':steps+='<p class="scope-context"><strong>'+('Broader role scope: ' if en else 'Übergeordneter Tätigkeitsumfang: ')+'</strong>'+escape(project['approach'])+'</p>'+manufacturing_diagram(lang)
    if key=='pau':steps+=comparison_table(lang,'pau')
    if key=='thesis':
        steps+='<div class="research-plots">'
        for image,label in [('thesis-06','Same-time heating comparison' if en else 'Vergleich bei gleicher Heizdauer'),('thesis-07','Nominal electrical-input comparison' if en else 'Vergleich nomineller elektrischer Eingangsenergie')]:
            caption=label+' · '+('Master’s thesis, pp. 63–64' if en else 'Masterarbeit, S. 63–64')
            steps+=f'<figure><a href="/assets/gallery/{image}.webp" data-viewer data-caption="{caption}"><img src="/assets/gallery/{image}.webp" alt="{caption}" loading="lazy" width="1200" height="600"></a><figcaption>{caption}</figcaption></figure>'
        steps+='</div>'+comparison_table(lang,'thesis')
        steps+='<p class="measurement-note">'+('The equivalent-input comparison uses nominal 550 W heater / 150 W LED power. LED points at 60/120/180 s are compared with rounded heater durations of 16/33/49 s: approximately P × t, not equal absorbed heat. Driver/cooling losses and full-system energy are not established. Source: thesis Fig. 5-2 and discussion, pp. 63–65.' if en else 'Der Vergleich gleicher Eingangsenergie nutzt nominell 550 W Heizer- und 150 W LED-Leistung. LED-Werte bei 60/120/180 s werden mit gerundeten Heizerzeiten von 16/33/49 s verglichen: näherungsweise P × t, keine gleiche absorbierte Wärme. Treiber-/Kühlverluste und Gesamtanlagenenergie sind nicht nachgewiesen. Quelle: Masterarbeit Abb. 5-2 und Diskussion, S. 63–65.')+'</p>'
        steps+='<p class="source">'+('Submitted title: Comparative Study of Radiant Heater and LED for Polymer Heating within FOUP Cleaner Vacuum Chambers. Source: methods pp. 45–46; comparison pp. 63–68; limitations pp. 73–75; conclusion p. 76.' if en else 'Eingereichter Titel: Comparative Study of Radiant Heater and LED for Polymer Heating within FOUP Cleaner Vacuum Chambers. Methodik S. 45–46; Vergleich S. 63–68; Grenzen S. 73–75; Fazit S. 76.')+'</p>'
    return steps

def case_outcome(key,lang):
    en=lang=='en'
    text={
     'machine':('Machine enclosure & assembly development','Maschinenverkleidung & Baugruppenentwicklung'),
     'pau':('Documented design comparison · 48 → 18 kW · ≈ €4,200 lower component cost','Dokumentierter Auslegungsvergleich · 48 → 18 kW · ≈ 4.200 € geringere Bauteilkosten'),
     'thesis':('Experimental study · material response, measurement limits and a qualified design decision','Versuchsstudie · Materialverhalten, Messgrenzen und begründete technische Entscheidung')}
    return '<p class="case-evidence">'+escape(text[key][0 if en else 1])+'</p>' if key in text else ''
