"""Consistent project periods; user-reported work is distinguished from issued evidence."""
import re

PERIODS={
 'pau':('2023-01','2023-06','01/2023','06/2023'),
 'machine':('2025-09','2026-09','09/2025','09/2026'),
 'thesis':('2023-07','2024-01','07/2023','01/2024'),
 'handling':('2022-08',None,'08/2022',None),
 'ansys':('2020',None,'2020',None),
 'frost':('2019-01','2020-12','01/2019','12/2020'),
 'shoe':('2016','2017','2016','2017'),
 'ai-cad':('2024-01','present','01/2024','present'),
}

def period(project,lang):
    start,end,start_label,end_label=PERIODS[project]
    label='Project period' if lang=='en' else 'Projektzeitraum'
    text=f'<time datetime="{start}">{start_label}</time>'
    if end=='present':text+=' – <span>'+('Present' if lang=='en' else 'Heute')+'</span>'
    elif end:text+=f' – <time datetime="{end}">{end_label}</time>'
    return f'<p class="project-period"><span class="period-label">{label}</span>{text}</p>'

def extend_projects(copy):
    for lang,c in copy.items():
        en=lang=='en'
        for project in c['projects']:
            project['tag']=re.sub(r' · (?:20[0-9]{2})(?:[–-]20[0-9]{2})?$','',project['tag'])
        handling=next(p for p in c['projects'] if p['id']=='handling')
        handling['note']+=(' Academic project report: August 2022. Advanced 3D Design module grade: 1.3. The supplied report does not establish measured ±50 µm positioning accuracy.' if en else ' Akademischer Projektbericht: August 2022. Modulnote Vertiefende 3D-Konstruktion: 1,3. Der bereitgestellte Bericht belegt keine gemessene Positioniergenauigkeit von ±50 µm.')
        frost=next(p for p in c['projects'] if p['id']=='frost')
        frost['note']+=(' Project period 01/2019–12/2020 supplied by me. A project-specific grade of 1.0 / AA and a validated CFD heat-and-mass-transfer model are not established by the supplied report.' if en else ' Projektzeitraum 01/2019–12/2020 von mir angegeben. Eine projektspezifische Note 1,0 / AA und ein validiertes CFD-Wärme- und Stoffübertragungsmodell sind durch den Bericht nicht belegt.')
        c['projects'].append(dict(
          id='ai-cad',cat='machine',tag='PERSONAL PORTFOLIO · AI / CAD' if en else 'PERSÖNLICHES PORTFOLIO · KI / CAD',
          title='From a prompt.<br>To a design workflow.' if en else 'Vom Prompt.<br>Zum Konstruktionsablauf.',
          short='Personal exploration of Text-to-CAD geometry generation coupled with Python-based analysis and optimisation, using a mounting flange as a demonstration case.' if en else 'Persönliche Erprobung von Text-to-CAD-Geometrieerzeugung mit Python-basierter Analyse und Optimierung am Beispiel eines Montageflansches.',
          tools=['Text-to-CAD','Python','Parametric design' if en else 'Parametrische Konstruktion'],
          problem='Reduce repetitive modelling and analysis steps in routine mechanical design iterations.' if en else 'Wiederkehrende Modellierungs- und Analyseschritte bei mechanischen Konstruktionsiterationen reduzieren.',
          approach='I report developing a pipeline combining prompt-based geometry generation, parametric flange modelling and a Python environment for structural-analysis and optimisation iterations.' if en else 'Nach eigener Angabe entwickle ich einen Ablauf aus promptbasierter Geometrieerzeugung, parametrischer Flanschmodellierung und einer Python-Umgebung für Strukturanalyse und Optimierungsiterationen.',
          result='Ongoing, self-reported portfolio work. Source code, model files, solver outputs and timing benchmarks have not yet been supplied for review; no measured time saving, validated FEA result or production deployment is claimed here.' if en else 'Laufende Portfolioarbeit nach eigener Angabe. Quellcode, Modelldateien, Solverergebnisse und Zeitvergleiche liegen noch nicht zur Prüfung vor; daher werden keine gemessene Zeitersparnis, validierten FEM-Ergebnisse oder Produktionseinsätze behauptet.',
          note='Source: owner-supplied project description, 29 October 2026. Start date 01/2024 is self-reported. Workflow illustration is conceptual.' if en else 'Quelle: Projektbeschreibung des Eigentümers vom 29. Oktober 2026. Beginn 01/2024 nach eigener Angabe. Ablaufdarstellung ist schematisch.',
          art='workflow'))
