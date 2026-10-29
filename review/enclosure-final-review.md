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
