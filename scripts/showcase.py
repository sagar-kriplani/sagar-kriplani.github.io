"""Curated public engineering figures; reuse the gallery's asset metadata."""
from html import escape
from gallery import FIGURES
from ui import icon

# Selection only: paths, dimensions, source pages and translated alt text stay in catalog.json.
# Scores / rationale are documented in review/engineering-showcase.md.
SELECTION = {
    'mechanical': ['handling-27', 'handling-09', 'ansys-19', 'handling-05', 'ansys-25'],
    'research': ['thesis-06', 'thesis-02', 'thesis-01', 'frost-08'],
}
COPY = {
    'en': dict(
        eyebrow='CAD · ANALYSIS · RESEARCH',
        title='Engineering in practice.', subtitle='Selected projects',
        intro='From CAD assemblies and manufacturing details to thermal research and numerical modelling.',
        mechanical='Mechanical design', research='R&D · Scientific Instrumentation',
        previous='Previous project', next='Next project', pause='Pause slideshow', play='Play slideshow',
        explore='Explore case study', zoom='Enlarge figure', gallery='All engineering figures',
        slide='Slide', of='of', carousel='carousel', slideRole='slide',
        playing='Auto · 6s', paused='Playback paused', hover='Paused while reading',
        ready='Autoplay ready', focus='Paused for reading', reduced='Reduced motion · paused',
        help='Use the arrow keys when focused, or swipe to explore.',
        source='Report excerpt', page='p.',
        academic='Academic CAD project', training='ANSYS training', thesis='Master’s thesis', modelling='Academic numerical study',
    ),
    'de': dict(
        eyebrow='CAD · ANALYSE · FORSCHUNG',
        title='Ingenieurarbeit in der Praxis.', subtitle='Ausgewählte Projekte',
        intro='Von CAD-Baugruppen und Fertigungsdetails bis zur thermischen Forschung und numerischen Modellierung.',
        mechanical='Konstruktion', research='F&E · Scientific Instrumentation',
        previous='Vorheriges Projekt', next='Nächstes Projekt', pause='Diashow pausieren', play='Diashow starten',
        explore='Fallstudie ansehen', zoom='Abbildung vergrößern', gallery='Alle technischen Abbildungen',
        slide='Folie', of='von', carousel='Karussell', slideRole='Folie',
        playing='Auto · 6s', paused='Wiedergabe pausiert', hover='Lesepause',
        ready='Automatik bereit', focus='Lesepause', reduced='Bewegung reduziert · pausiert',
        help='Mit den Pfeiltasten im Fokus oder per Wischgeste navigieren.',
        source='Berichtsauszug', page='S.',
        academic='Akademisches CAD-Projekt', training='ANSYS-Training', thesis='Masterarbeit', modelling='Akademische numerische Studie',
    ),
}

# Each caption is grounded in the existing project narrative, not inferred performance.
CAPTIONS = {
    'handling-27': dict(context='academic', category=('Assembly design', 'Baugruppenkonstruktion'),
        text=('Developed the mechanism, CAD layout and actuator selection for an academic conveyor-transfer concept.',
              'Mechanismus, CAD-Aufbau und Aktuatorauswahl für ein akademisches Konzept zum Transfer zwischen Förderbändern entwickelt.')),
    'handling-09': dict(context='academic', category=('Mechanical integration', 'Mechanische Integration'),
        text=('Detailed the vertical guide within the handling mechanism, connecting CAD geometry with technical drawings.',
              'Die vertikale Führung des Handhabungsmechanismus konstruktiv detailliert und CAD-Geometrie mit technischen Zeichnungen verknüpft.')),
    'handling-05': dict(context='academic', category=('Manufacturing details', 'Fertigungsdetails'),
        text=('Documented the foundation plate through a dimensioned drawing and its corresponding CAD geometry.',
              'Die Grundplatte mit bemaßter Zeichnung und zugehöriger CAD-Geometrie dokumentiert.')),
    'ansys-19': dict(context='training', category=('Structural analysis', 'Strukturanalyse'),
        text=('Explored structural response using ANSYS training exercises; the frame figure shows a random-vibration result.',
              'Strukturverhalten in ANSYS-Trainingsaufgaben untersucht; die Rahmenabbildung zeigt ein Ergebnis der Zufallsschwingungsanalyse.')),
    'ansys-25': dict(context='training', category=('Finite element analysis', 'Finite-Elemente-Analyse'),
        text=('Practised finite element analysis; this finned geometry shows a static-structural deformation result.',
              'Die Finite-Elemente-Analyse erprobt; diese Rippengeometrie zeigt ein Verformungsergebnis der statischen Strukturanalyse.')),
    'thesis-06': dict(context='thesis', category=('Thermal research · FOUP', 'Thermische Forschung · FOUP'),
        text=('Compared IR-LED and radiant-heater responses for FOUP polymers, evaluating temperature behaviour and measurement limits.',
              'Das Erwärmungsverhalten von FOUP-Polymeren mit IR-LEDs und Strahlungsheizern verglichen und Messgrenzen bewertet.')),
    'thesis-02': dict(context='thesis', category=('Materials & spectroscopy', 'Werkstoffe & Spektroskopie'),
        text=('Used polymer absorption measurements to inform infrared source selection for comparative heating experiments.',
              'Absorptionsmessungen an Polymeren zur Auswahl von Infrarotquellen für vergleichende Heizversuche genutzt.')),
    'thesis-01': dict(context='thesis', category=('Experimental methodology', 'Versuchsmethodik'),
        text=('Structured the investigation from material analysis and experimental setup through heating tests and data evaluation.',
              'Die Untersuchung von der Materialanalyse und dem Versuchsaufbau über Heizversuche bis zur Datenauswertung strukturiert.')),
    'frost-08': dict(context='modelling', category=('Heat transfer modelling', 'Modellierung der Wärmeübertragung'),
        text=('Investigated numerical temperature development in an academic frost-modelling study; this is model output.',
              'Die numerische Temperaturentwicklung in einer akademischen Studie zur Frostmodellierung untersucht; dargestellt ist ein Modellergebnis.')),
}


def showcase(lang, profile):
    c = COPY[lang]
    figures = {f['key']: f for f in FIGURES}
    keys = SELECTION[profile]
    slides, indicators = [], []
    for index, key in enumerate(keys):
        f, caption = figures[key], CAPTIONS[key]
        locale = 0 if lang == 'en' else 1
        title = f[lang]
        # The gallery's ANSYS/frost labels are intentionally broad; name only visually verified results.
        if key == 'ansys-19': title = ('Frame · random-vibration study', 'Rahmen · Zufallsschwingungsanalyse')[locale]
        if key == 'ansys-25': title = ('Finned geometry · structural study', 'Rippengeometrie · Strukturanalyse')[locale]
        if key == 'frost-08': title = ('Numerical temperature development', 'Numerische Temperaturentwicklung')[locale]
        src = '/assets/gallery/' + key + '.webp'
        href = '#' + f['group']
        alt = escape(f[lang] + ' · ' + c[caption['context']], quote=True)
        label = escape(f'{c["slide"]} {index+1} {c["of"]} {len(keys)}: {title}', quote=True)
        slides.append(f'''<article class="showcase-slide{' is-current' if index == 0 else ''}" id="showcase-{key}" data-showcase-slide data-key="{key}" role="group" aria-roledescription="{c['slideRole']}" aria-label="{label}"{'' if index == 0 else ' hidden'}>
          <div class="showcase-image"><a href="{href}" data-showcase-project aria-label="{escape(c['explore'] + ': ' + title, quote=True)}"><img src="{src}" alt="{alt}" width="{f['width']}" height="{f['height']}" loading="{'eager' if index == 0 else 'lazy'}" decoding="async"></a><a class="showcase-zoom" href="{src}" data-viewer data-caption="{alt}" aria-label="{escape(c['zoom'] + ': ' + title, quote=True)}">{icon('plus')}<span>{c['zoom']}</span></a></div>
          <div class="showcase-caption"><div class="showcase-meta"><span>{escape(caption['category'][locale])}</span><span>{escape(c[caption['context']])}</span></div><h3>{escape(title)}</h3><p>{escape(caption['text'][locale])}</p><div class="showcase-caption-bottom"><a href="{href}" data-showcase-project>{c['explore']} {icon('right')}</a><small>{c['source']} · {c['page']} {f['page']}</small></div></div>
        </article>''')
        indicators.append(f'<button type="button" data-showcase-go="{index}" aria-label="{label}" aria-controls="showcase-{key}" aria-pressed="{str(index == 0).lower()}"><span class="showcase-marker" aria-hidden="true"></span><span class="showcase-indicator-number" aria-hidden="true">{index+1:02}</span></button>')
    return f'''<section class="engineering-showcase" id="engineering-showcase" data-showcase data-play-label="{c['play']}" data-pause-label="{c['pause']}" data-playing-label="{c['playing']}" data-paused-label="{c['paused']}" data-hover-label="{c['hover']}" data-ready-label="{c['ready']}" data-focus-label="{c['focus']}" data-reduced-label="{c['reduced']}" aria-labelledby="showcase-heading" aria-roledescription="{c['carousel']}" tabindex="0">
      <div class="showcase-heading"><div><p class="showcase-eyebrow">{c['eyebrow']}</p><h2 id="showcase-heading">{c['title']}<span>{c['subtitle']}</span></h2><p class="showcase-intro">{c['intro']}</p></div><span class="showcase-profile">{c[profile]}</span></div>
      <div class="showcase-viewport">{''.join(slides)}</div>
      <div class="showcase-controls" hidden><div class="showcase-playback"><button type="button" data-showcase-play aria-label="{c['pause']}"><span data-showcase-play-icon aria-hidden="true">Ⅱ</span></button><span data-showcase-state>{c['paused']}</span></div><div class="showcase-indicators" role="group" aria-label="{c['subtitle']}">{''.join(indicators)}</div><div class="showcase-arrows"><span class="showcase-count"><span data-showcase-count>01</span> / {len(keys):02}</span><button type="button" data-showcase-prev aria-label="{c['previous']}">{icon('left')}</button><button type="button" data-showcase-next aria-label="{c['next']}">{icon('right')}</button></div></div>
      <div class="showcase-footer"><p class="showcase-help" hidden>{c['help']}</p><a href="/{lang}/gallery/">{c['gallery']} {icon('external')}</a></div><p class="sr-only showcase-announcement" role="status" aria-live="polite" aria-atomic="true"></p>
    </section>'''
