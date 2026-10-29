# Final enclosure-focused revision

Prepared locally for review; not deployed.

- Retained the preferred featured order: NeSt, PAU, FOUP, followed by five supporting projects in the archive.
- Replaced the NeSt 8 mm bending incident with industrial enclosure and assembly development in German and English, including the R&D profile case.
- Reused the existing conceptual enclosure illustration; it is not a customer CAD model. Detailed methodology includes a representative CAD-to-production workflow.
- Preserved the case-study disclosure, accessible source subsection, evidence grouping, profile/language switching, dates, CVs and protected downloads.
- Sources: NeSt employment reference supports broad mechanical design/drawing duties. Detailed task scope, supplier coordination and ERP use follow the supplied CV. No project-specific quantified performance result is asserted.

Validation: static checks passed for 20 pages; 14 Mechanical viewport samples and 28 role/language/viewport samples passed in Chromium, covering 320–1440 px, case expansion, provenance, archive, filters, language/profile context and no-JavaScript access. The case-specific test now checks the enclosure title, conceptual visual and absence of the removed bending incident.

Modified: scripts/build.py, scripts/recruitment.py, scripts/mechanical_showcase.py, scripts/mechanical-check.cjs, generated index.html, this review.

## Uniform project layout follow-up

Every project now uses the same image/content card renderer. The project shortcut row and prominent challenge/decision/result blocks are removed. Detailed methodology, results and sources are inside the native case-study disclosure. NeSt remains enclosure-focused and uses the labelled conceptual open/closed enclosure visual. The profile eyebrow is 12 px, up from 10 px. The former featured-card renderer was removed to prevent layout divergence.

Fresh preview: http://127.0.0.1:4176/ (Cache-Control: no-store). Run `python scripts/preview.py` to restart it. Live deployment is unchanged.

## Continuous project list / Konstruktion–F&E consistency

Removed the project archive: all eight projects now appear in the main list. Both profiles use the same card renderer and responsive image/content grid. Mechanical project order remains NeSt, PAU, FOUP, handling, ANSYS training, heat-transfer research, footwear study, personal AI/CAD exploration. Research retains its role-specific ordering. Desktop/tablet cards align the image left and text right; mobile stacks them. Fixed the narrow PAU column at the reported 1074 px width. Case methodology, results and provenance remain within the disclosure.

Validation: 128 card checks across 16 language/profile/viewport combinations (375, 768, 1074, 1440 px); all eight initially visible, matching structure, collapsed details, source access, alignment and no horizontal overflow. PAU visual checked at 1074 px. Static build checks passed for 20 pages. These follow-up changes are local and not deployed.
