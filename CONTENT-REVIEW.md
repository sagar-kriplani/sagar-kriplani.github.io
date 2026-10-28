# Career content review — 28 October 2026

Review instruction: reconcile the English/German portfolio and CVs against supplied records and the owner's explicit corrections; distinguish employer evidence, academic results and self-reported achievements; protect NDA material and personal identifiers; regenerate CVs, validate and deploy.

## Resolved content

- Brooks overall research/design period: **07/2023–06/2024**. Research and development for the master's thesis: **07/2023–01/2024**. Mechanical Design Engineer (Working Student / Werkstudent): **02/2024–06/2024**. Working-student status explicitly confirmed by the owner in the follow-up correction. These follow the owner's latest explicit role breakdown, superseding an editable draft with different months. No issued employment reference independently confirms these two subperiods. Do not relabel them as full-time employment or assert an unconfirmed contract type.
- The issued **01/2023–06/2023 internship** remains separate. Company research dates differ from academic thesis submission in February 2025 and degree award in March 2025.
- Ravi: **08/2020–09/2021**, departure confirmed by the owner. The April 2021 employment letter supports the start and employment at its issue date. Use its employer name, Ravi Brass Industries, without assuming that the profile's different company name is a verified legal alias.
- NeSt: **09/2025–09/2026**, employer location Herbrechtingen, residence Heidenheim. Employment reference supports title and duties. Figures of 8+ platforms, approximately 200 drawings/month, up to 70% lower component costs and 60% lower weight are explicitly attributed to owner-reported projects, not independently audited or established by the reference.
- Master: final grade **1.8**, thesis **1.3**, **120 ECTS**, **ECTS B**. Bachelor **8.14/10**. Diploma **9.50/10**, a mechanical engineering diploma rather than a high-school diploma. No unsupported German grade conversions.
- Languages follow current self-reported proficiency. The supplied German record proves B1-plus coursework, not a B2 examination.
- PAU heater capacity differs from measured energy consumption. Academic training and simulations remain labelled as such. No independent power-plant operations responsibility is claimed.
- All existing 16 certificate/training/recognition images remain accessible in the evidence library. A profile-listed Design Foundations course has no supplied certificate and is not promoted to a verified credential.
- Removed stale statements about published AI LinkedIn equipment media. Brooks equipment imagery and raw CAD remain excluded; the diagram-only process flow remains in place.

## Maintenance

`scripts/career.py` holds the shared role periods, qualifications, summaries and concise CV project descriptions. `scripts/cv_pdf.py` produces six two-page English/German PDFs (general, mechanical design, R&D) using ReportLab and pypdf, and refreshes legacy repository aliases. Run it with a Python environment containing those packages and Windows Arial fonts.

Then run `python scripts/build.py` and `python scripts/check.py`. The publication check validates career dates, CV source/file hashes, local links and privacy boundaries. Render and inspect every generated PDF page before committing. PDFs are checked in; deployment does not require ReportLab. Raw evidence documents remain private and never ship.
