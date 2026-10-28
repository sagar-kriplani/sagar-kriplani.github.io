"""Canonical reviewed career content shared by the website and downloadable CVs."""
from html import escape

JOBS = {
 'en': [
 ['09/2025 – 09/2026','NeSt GmbH','Mechanical Design Engineer · Konstrukteur','Herbrechtingen, Germany','Developed machine enclosures, precision assemblies, sheet-metal details and manufacturing drawings using Autodesk Inventor, with DFM/DFA and production coordination. Project figures reported by me: 8+ machine platforms, approximately 200 drawings per month, component cost reductions up to 70% and weight reduction of 60%. These figures are not independently established by the employer reference.'],
 ['02/2024 – 06/2024','Brooks Automation','Mechanical Design Engineer (Working Student)','Steißlingen, Germany','Designed precision components and assemblies for semiconductor automation, developed CAD models and manufacturing drawings, and collaborated with R&D, electrical engineering and production.'],
 ['07/2023 – 01/2024','Brooks Automation','Research & Development · Master’s Thesis','Steißlingen, Germany','Compared radiant heaters and LEDs for polymer heating in vacuum chambers. Developed thermal models and experimental setups to assess heating performance and thermal uniformity. The thesis was submitted separately in February 2025.'],
 ['01/2023 – 06/2023','Brooks Automation','Engineering Intern · Mechanical Design','Steißlingen, Germany','Analysed the Process Air Unit, compared heater concepts and developed mechanical design and assembly documentation for semiconductor automation equipment. The issued internship reference reports 20% cost reduction; the project report separately records approximately 21%.'],
 ['08/2020 – 09/2021','Ravi Brass Industries','Design & Development Engineer','Jamnagar, India','Designed mechanical components and assemblies, prepared manufacturing drawings and coordinated with production on manufacturability and quality. Departure month confirmed by me; the employment confirmation establishes the start date and employment in April 2021.']],
 'de': [
 ['09/2025 – 09/2026','NeSt GmbH','Konstrukteur · Mechanische Entwicklung','Herbrechtingen, Deutschland','Maschinenverkleidungen, Präzisionsbaugruppen, Blechdetails und Fertigungszeichnungen mit Autodesk Inventor entwickelt; DFM/DFA und Abstimmung mit der Fertigung. Von mir berichtete Projektkennzahlen: über 8 Maschinenplattformen, etwa 200 Zeichnungen pro Monat, bis zu 70 % geringere Bauteilkosten und 60 % Gewichtsreduzierung. Das Arbeitszeugnis bestätigt diese Kennzahlen nicht unabhängig.'],
 ['02/2024 – 06/2024','Brooks Automation','Werkstudent · Mechanische Konstruktion','Steißlingen, Deutschland','Präzisionsbauteile und Baugruppen für die Halbleiterautomation konstruiert, CAD-Modelle und Fertigungszeichnungen erstellt sowie mit Forschung und Entwicklung, Elektrotechnik und Produktion zusammengearbeitet.'],
 ['07/2023 – 01/2024','Brooks Automation','Forschung und Entwicklung · Masterarbeit','Steißlingen, Deutschland','Strahlungsheizer und LEDs zur Polymererwärmung in Vakuumkammern verglichen. Thermische Modelle und Versuchsaufbauten zur Untersuchung von Heizleistung und Temperaturgleichmäßigkeit entwickelt. Die Masterarbeit wurde gesondert im Februar 2025 eingereicht.'],
 ['01/2023 – 06/2023','Brooks Automation','Praktikant · Mechanische Konstruktion','Steißlingen, Deutschland','Process Air Unit analysiert, Heizkonzepte verglichen sowie Konstruktion und Montagedokumentation für Halbleiter-Automatisierungsanlagen erarbeitet. Das Praktikumszeugnis nennt 20 % Kostenreduktion; der Projektbericht dokumentiert gesondert etwa 21 %.'],
 ['08/2020 – 09/2021','Ravi Brass Industries','Design & Development Engineer','Jamnagar, Indien','Mechanische Bauteile und Baugruppen konstruiert, Fertigungszeichnungen erstellt und Herstellbarkeit sowie Qualität mit der Produktion abgestimmt. Austrittsmonat von mir bestätigt; die Beschäftigungsbestätigung belegt Beginn und Beschäftigung im April 2021.']]
}
DEGREES = {
 'en': [['10/2021 – 03/2025','M.Sc. Scientific Instrumentation','Ernst-Abbe-Hochschule Jena · Grade 1.8 · Thesis 1.3 · 120 ECTS · ECTS B'],['2017 – 2020','B.E. Mechanical Engineering','A. D. Patel Institute of Technology / GTU · CGPA 8.14/10 · First Class with Distinction'],['2014 – 2017','Diploma in Mechanical Engineering','Government Polytechnic Jamnagar / GTU · CGPA 9.50/10']],
 'de': [['10/2021 – 03/2025','M.Sc. Scientific Instrumentation','Ernst-Abbe-Hochschule Jena · Note 1,8 · Masterarbeit 1,3 · 120 ECTS · ECTS B'],['2017 – 2020','B.E. Mechanical Engineering','A. D. Patel Institute of Technology / GTU · CGPA 8,14/10 · First Class with Distinction'],['2014 – 2017','Diploma in Mechanical Engineering','Government Polytechnic Jamnagar / GTU · CGPA 9,50/10']]
}
SUMMARIES = {
 'en': {
 'general':'Mechanical design engineer with experience in special-purpose machinery, semiconductor equipment and scientific instrumentation. Combines manufacturable CAD design, production documentation and experimental thermal investigation.',
 'mechanical':'Mechanical design engineer focused on machine enclosures, precision assemblies and manufacturing-ready documentation. Practical experience with Autodesk Inventor, sheet-metal design, DFM/DFA and production coordination.',
 'rd':'Mechanical engineer with an M.Sc. in Scientific Instrumentation, focused on thermal investigation, experimental setups and precision equipment development. Experience with vacuum polymer-heating research, mechanical design and engineering analysis.'},
 'de': {
 'general':'Konstrukteur mit Erfahrung im Sondermaschinenbau, in Halbleiteranlagen und wissenschaftlicher Instrumentierung. Verbindet fertigungsgerechte CAD-Konstruktion und Produktionsdokumentation mit experimentellen thermischen Untersuchungen.',
 'mechanical':'Konstrukteur mit Schwerpunkt auf Maschinenverkleidungen, Präzisionsbaugruppen und fertigungsgerechter Dokumentation. Praxiserfahrung mit Autodesk Inventor, Blechkonstruktion, DFM/DFA und Fertigungsabstimmung.',
 'rd':'Maschinenbauingenieur mit M.Sc. Scientific Instrumentation und Schwerpunkt auf thermischen Untersuchungen, Versuchsaufbauten und Präzisionsanlagen. Erfahrung in der Polymererwärmung im Vakuum, mechanischer Konstruktion und technischer Analyse.'}
}
PROJECTS = {
 'en': [('PAU redesign · Brooks internship','Thermodynamic calculations, component selection and mechanical design. Project report: approximately 500 to 50 mbar pressure drop and 48 to 18 kW heater design capacity; not measured operating energy savings.'),('Polymer heating · Master’s thesis','Compared radiant heaters and LEDs in vacuum chambers. LEDs improved uniformity in the tested setup; radiant heaters performed better overall. Company research: 07/2023–01/2024; thesis submitted 02/2025.'),('Academic CAD & simulation','Cylindrical handling mechanism in Inventor; ANSYS training exercises; MATLAB finite-difference frost-growth model in a four-student team. Academic results are not production validation.')],
 'de': [('PAU-Optimierung · Brooks-Praktikum','Thermodynamische Berechnungen, Komponentenauswahl und Konstruktion. Projektbericht: Druckverlust etwa 500 auf 50 mbar und Heizerauslegung 48 auf 18 kW; keine gemessene Betriebsenergieeinsparung.'),('Polymererwärmung · Masterarbeit','Strahlungsheizer und LEDs in Vakuumkammern verglichen. LEDs zeigten im Versuch gleichmäßigere Erwärmung; Strahlungsheizer schnitten insgesamt besser ab. Betriebliche Forschung: 07/2023–01/2024; Abgabe 02/2025.'),('Akademische CAD- und Simulationsprojekte','Zylindrischer Handhabungsmechanismus in Inventor; ANSYS-Trainingsaufgaben; MATLAB-Modell zum Frostwachstum in einem Viererteam. Akademische Ergebnisse ohne Produktionsvalidierung.')]
}

def apply_career(copy):
    for lang,c in copy.items():
        en=lang=='en'
        c['jobs']=[row[:] for row in JOBS[lang]]
        c['degrees']=[row[:] for row in DEGREES[lang]]
        c['cvIntro']=SUMMARIES[lang]['general']
        c['experienceNote']=('Brooks research and design periods follow my confirmed role breakdown. The company research period is distinct from the thesis submission in February 2025. Employer locations are shown separately from my residence.' if en else 'Brooks-Forschungs- und Konstruktionszeiträume folgen meiner bestätigten Rollenaufteilung. Betriebliche Forschung und Abgabe der Masterarbeit im Februar 2025 sind getrennte Zeitangaben. Arbeitgeberstandorte sind vom Wohnort getrennt.')
        c['projects'][1]['result']=c['jobs'][0][4]
        c['projects'][1]['note']=('Sources: issued NeSt reference for role and scope; my supplied profile for project figures. Figures are self-reported project results, not independently audited. Conceptual illustration.' if en else 'Quellen: ausgestelltes NeSt-Zeugnis für Tätigkeit und Aufgaben; mein bereitgestelltes Profil für Projektkennzahlen. Kennzahlen sind selbst berichtete, nicht unabhängig geprüfte Projektergebnisse. Schematische Illustration.')
        c['languageText']=('German: professional working · English: full professional' if en else 'Deutsch: berufliche Arbeitskenntnisse · Englisch: professionelle Kenntnisse')+'<br>Hindi · Gujarati · Sindhi: '+('native/bilingual' if en else 'muttersprachlich/zweisprachig')
        c['languageNote']=('Self-reported language proficiency; the supplied German certificate documents B1-plus coursework, not a B2 examination.' if en else 'Sprachkenntnisse nach Selbsteinschätzung; der vorliegende Deutsch-Nachweis belegt einen B1-plus-Kurs, keine B2-Prüfung.')

def cv_body(lang,c):
    en=lang=='en'
    out='<div class="cv-downloads"><h2>'+('Download a CV' if en else 'Lebenslauf herunterladen')+'</h2><p>'
    for key,label in [('general','General' if en else 'Allgemein'),('mechanical','Mechanical Design' if en else 'Konstruktion'),('rd','Research & Development' if en else 'Forschung & Entwicklung')]:
        out+=f'<a class="button" href="/assets/cv/{key}-{lang}.pdf">{label} · PDF ↓</a> '
    out+='</p></div><h2>'+('Experience' if en else 'Berufserfahrung')+'</h2>'
    for date,employer,title,place,description in JOBS[lang]:
        out+=f'<article class="cv-project"><h3>{escape(employer)} · {escape(title)}</h3><p class="date">{date} · {place}</p><p>{description}</p></article>'
    out+='<h2>'+('Selected projects' if en else 'Ausgewählte Projekte')+'</h2>'
    for title,desc in PROJECTS[lang]:out+=f'<p><strong>{title}</strong><br>{desc}</p>'
    out+='<h2>'+c['education']+'</h2>'
    for date,title,school in DEGREES[lang]:out+=f'<p><strong>{title}</strong> · {date}<br>{school}</p>'
    out+='<h2>'+('Technical skills' if en else 'Fachkenntnisse')+'</h2><p>Autodesk Inventor · Siemens NX · PTC Creo · ANSYS · MATLAB · DFM/DFA · BOM · SAGE ERP · Agile PLM</p>'
    out+='<h2>'+c['languages']+'</h2><p>'+c['languageText']+'</p><p class="source">'+c['languageNote']+'</p>'
    out+='<h2>'+('Training' if en else 'Weiterbildung')+'</h2><p>ANSYS Basic to Professional (2020) · Siemens Centre of Excellence: NX, NC, Drafting, Robotics (2016–2017) · LinkedIn Learning: Siemens NX, Engineering Drawings, Semiconductor Manufacturing (2026).</p>'
    out+=f'<p><a href="/{lang}/evidence/">'+('All certificate images, references and transcripts' if en else 'Alle Zertifikatsbilder, Zeugnisse und Notenübersichten')+' ↗</a></p>'
    return out
