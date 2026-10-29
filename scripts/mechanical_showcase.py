"""Shared project presentation and Mechanical profile context."""

def refine_mechanical(c,lang):
    en=lang=='en'
    c['focusedMechanical']=True
    c['contentLanguage']=lang
    c['skills']=[row[:] for row in c['skills']]
    c['intro']=('I develop mechanical assemblies, machine enclosures and manufacturing documentation for industrial machinery. My special-purpose machinery experience is complemented by semiconductor equipment development and an M.Sc. in Scientific Instrumentation.' if en else 'Ich entwickle mechanische Baugruppen, Maschinenverkleidungen und Fertigungsunterlagen für industrielle Maschinen. Meine Praxiserfahrung im Sondermaschinenbau ergänze ich durch die Entwicklung von Halbleiteranlagen und einen M.Sc. Scientific Instrumentation.')
    c['projectsIntro']=('Three industrial and interdisciplinary cases: enclosure and assembly development at NeSt, process-air development at Brooks, and thermal research as an equipment-engineering differentiator.' if en else 'Drei industrielle und interdisziplinäre Fallstudien: Gehäuse- und Baugruppenentwicklung bei NeSt, Prozessluftentwicklung bei Brooks und thermische Forschung als Ergänzung der Anlagenentwicklung.')
    c['projectsTitle']='Engineering decisions,<br>made tangible.' if en else 'Technische Entscheidungen.<br>Praktisch nachvollziehbar.'
    c['projects']=sorted(c['projects'],key=lambda p:['machine','pau','thesis','handling','ansys','frost','shoe','ai-cad'].index(p['id']))
    c['skills'][0][3]=('Assembly development, sheet-metal and welded structures, mechanical integration and manufacturing-oriented detailing with tolerance considerations.' if en else 'Baugruppenentwicklung, Blech- und Schweißkonstruktionen, mechanische Integration sowie fertigungsgerechte Detaillierung und Toleranzbetrachtung.')
    c['skills'][3][3]=('Manufacturing drawings, sheet-metal developments, BOMs, engineering changes and production coordination. SAGE ERP and Agile PLM support the documented workflow.' if en else 'Fertigungszeichnungen, Blechabwicklungen, Stücklisten, technische Änderungen und Produktionsabstimmung. SAGE ERP und Agile PLM ergänzen den dokumentierten Arbeitsablauf.')

def archive(cards,lang):
    en=lang=='en'
    return '<details class="project-archive" id="project-archive" data-context><summary>'+('Project archive · 5 academic, training & experimental projects' if en else 'Projektarchiv · 5 Studien-, Trainings- und Erprobungsprojekte')+'</summary><p>'+('Supporting work remains fully accessible here. ANSYS work is training; academic and personal exploration are not presented as industrial delivery.' if en else 'Ergänzende Arbeiten bleiben hier vollständig zugänglich. ANSYS-Aufgaben sind Training; Studien- und persönliche Erprobungsprojekte werden als solche eingeordnet.')+'</p><div class="projects archive-projects">'+cards+'</div></details>'

def supporting_context(gallery,linkedin,lang):
    return '<details class="supporting-context" data-context><summary>'+('Academic gallery & additional background' if lang=='en' else 'Akademische Galerie & weiterer Hintergrund')+'</summary>'+gallery+linkedin+'</details>'


def enclosure_visual(lang):
    en=lang=='en'
    title='Conceptual machine enclosure: closed and open access panels' if en else 'Schematische Maschinenverkleidung: geschlossene und geöffnete Zugangstüren'
    labels=['CLOSED','OPEN / SERVICE ACCESS'] if en else ['GESCHLOSSEN','OFFEN / WARTUNGSZUGANG']
    views=[]
    for i in range(2):
        # The same generic frame is shown twice; no employer/customer geometry.
        frame='<path d="M20 100 150 65 245 115 115 155ZM20 100v155l95 55 130-40V115M115 155v155M150 65v155l95 50M20 255l130-35"/><path d="M35 120v120l65 38V162ZM130 170l100-30v113l-100 30Z" opacity=".4"/><path d="M50 267v18m65 25v18m115-55v18" stroke-width="5"/>'
        panels=('<path d="M28 112v137l77 44V158ZM125 162l111-32v131l-111 34Z" fill="currentColor" fill-opacity=".07"/><path d="M40 130v72l48 27v-72ZM140 177l79-23v65l-79 23Z" fill="currentColor" fill-opacity=".09"/><path d="M93 235v24m45-3v22" stroke-width="4"/>' if i==0 else '<path d="M28 112 -18 140v137l46-28M125 162l87 55v133l-87-55M125 162v133M212 217v133" fill="currentColor" fill-opacity=".05"/><path d="M138 180l58 37v65l-58-37Z"/><path d="M200 299v23" stroke-width="4"/><path d="M128 325q50 40 98-1m-14 0 14 0-4 14" stroke-dasharray="5 5"/>')
        views.append(f'<g transform="translate({55+i*315},15)" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round">{frame}<g stroke="#c46b32">{panels}</g><text x="110" y="385" fill="currentColor" stroke="none" text-anchor="middle" font-family="monospace" font-size="13">{labels[i]}</text></g>')
    return f'<svg class="enclosure-concept" viewBox="0 0 660 440" role="img" aria-label="{title}"><title>{title}</title>'+''.join(views)+'</svg>'
