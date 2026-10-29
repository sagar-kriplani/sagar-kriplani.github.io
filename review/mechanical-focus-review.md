# Focused Mechanical Design profile review

Date: 29 October 2026. Target: `/de/mechanical/`. Baseline: `c3823b6`. Local branch: `codex/mechanical-profile-focus`.

**Publication approved by the owner on 29 October 2026. Commit, merge to main and deployment are authorized.** Review preview: http://127.0.0.1:4175/de/mechanical/ . The English Mechanical counterpart and default landing aliases reuse this presentation. R&D project ordering and detailed case content are preserved.

## 1. Exact weaknesses found

- Eight projects shared one sequence. The academic handling study appeared before the FOUP research, weakening the requested NeSt → PAU → FOUP hierarchy.
- The existing NeSt case already contained the 8 mm example and diagram, but the card emphasized a single failure anecdote more than the broader assembly/enclosure/manufacturing remit.
- Only the first project used the wide featured layout. Challenge/decision/result were not consistently visible for all three main cases before expanding methodology.
- Prominent wording such as “vom Eigentümer bestätigter Fall” made the page read like an audit. Provenance is necessary, but it was occupying valuable recruitment space.
- NeSt and Ravi experience paragraphs mixed core duties with lengthy evidence qualifications. These are now retained in accessible context disclosures.
- The first evidence selection included an ANSYS training record alongside a professional reference; this was less relevant to the hiring manager's initial question about industrial experience.
- Supporting academic-gallery and LinkedIn-context sections added substantial initial scrolling despite being secondary to the professional cases.
- The German CV already had a working one-click hero link. It was preserved and verified, not replaced or falsely described as a new feature.

## 2. Files and components modified

| File | Change |
| --- | --- |
| `scripts/mechanical_showcase.py` (new) | Mechanical-only brief renderer, readable manufacturing diagram labels, archive, project jumps and supporting-context grouping |
| `scripts/build.py` | Three primary cases plus five archived cards; Mechanical copy refinement; reusable job-context disclosure; scoped supporting-section arrangement |
| `scripts/evidence.py` | Professional references first on Mechanical pages; five supporting-evidence groups; complete library preserved |
| `assets/site.js` | Open archive/context for deep links; source-link disclosure/focus; preserve project filters; evidence category/search query support |
| `assets/site.css` | Consistent case briefs, mobile visual order, tag readability, source sections, archives and evidence groups |
| `scripts/check.py` | Scoped semantic language-row check and three-case/archive/source structure checks |
| `scripts/mechanical-check.cjs` (new) | Targeted hierarchy, archive, keyboard, source qualification, evidence routes and responsive tests |
| `scripts/recruitment-check.cjs` | Optional preview base URL for reliable local testing |
| `package.json` | Adds `test:mechanical` |
| `index.html` | Generated default Mechanical landing alias |
| `review/mechanical-focus-review.md` | This review package |

No CV PDF, canonical career facts, education dates, qualification, encrypted original, access password, CAD file, deployment workflow or external dependency changed.

## 3. Before / after content and layout

| Area | Before | After |
| --- | --- | --- |
| Main project order | NeSt, PAU, handling study, FOUP, then supporting work | NeSt, PAU, FOUP in three consistent featured cards |
| Secondary work | Five supporting projects interleaved with industrial work | Five projects in an expandable archive; all original descriptions, dates, sources and access paths retained |
| NeSt positioning | Bend-failure story led the card | Assembly development, enclosures, sheet metal/welded structures, manufacturing documentation and production/supplier coordination establish context first |
| Case interface | Mixed card sizes, detail-heavy disclosures | Overview → challenge → decision → result → expandable methodology/sources/limitations |
| Immediate visuals | Existing manufacturing diagram and report figures | Manufacturing diagram retained with larger labels; approved text-free PAU schematic; actual FOUP heating graph visible without expanding methodology |
| Provenance | Audit wording in visible headline/outcome and role prose | Dedicated “Quellen & Nachweise” plus accessible job context; qualifications remain explicit and available |
| Evidence entry | NeSt / ANSYS / master record | NeSt / Brooks reference / master record first |
| Supporting material | Full gallery/context sections on initial scroll path | Expandable background section; complete galleries, earlier-work context and library remain available |

Representative German writing:

- Before: “Fertigungsentscheidung · vom Eigentümer bestätigter Fall”.
- After: “NeSt: Konstruktion für die Fertigung”, followed by a specific challenge, a two-part welded design decision and the qualitative rework outcome.
- The source subsection still says the incident/outcome were confirmed by Sagar Kriplani and that no independent fabrication/acceptance record was provided. The general employment reference is not presented as proof of this specific incident.

Local before/after screenshots (not published):

- [Mobile before](../qa/targeted-before-390.png) / [Mobile after](../qa/targeted-after-390.png)
- [Desktop before](../qa/targeted-before-1440.png) / [Desktop after](../qa/targeted-after-1440.png)
- [NeSt mobile case](../qa/targeted-nest-390.png) / [NeSt desktop case](../qa/targeted-nest-1440.png)

Observed default German-page heights at the same viewport sizes, after fonts loaded:

| Width | Before | After |
| --- | --- | --- |
| 390px | 16665px | 12621px |
| 768px | 11429px | 9357px |
| 1440px | 10764px | 8725px |

These are local layout observations, not load-speed or recruitment-conversion results. Supporting disclosures can be expanded, restoring access to all material. No technical evidence was deleted to obtain the shorter initial view.

## 4. Recruiter usability improvements

- The opening proposition prioritizes practical industrial machinery work, with semiconductor development and Scientific Instrumentation as supporting differentiators.
- German Mechanical CV remains one click from the hero; the English counterpart points to its corresponding approved CV.
- Four project-jump links lead to NeSt, PAU, FOUP and the archive.
- All three primary cases show the key engineering result and a meaningful visual immediately. Methodology, source references and limitations remain available through native disclosure.
- Important text requires no hover or animation. The archive and supporting sections work without JavaScript.
- Five evidence groups are available: **Arbeitszeugnisse**, **Studium & Abschlüsse**, **CAD & Konstruktion**, **Simulation & Forschung**, **Weiterbildungen**.
- Evidence links can open a filtered library directly; category/search selection survives language switching.
- Source links open the relevant disclosure and move keyboard focus to the source section. Archive deep links reveal the requested project automatically.
- Existing project-category filters still cover all eight projects; selecting a filter opens the archive so matches cannot remain hidden inside it.
- German/English and Mechanical/R&D switching, direct CV paths and the existing single back-to-top arrow remain functional. No sticky header was introduced.

## 5. Engineering claims and verification limits

No new achievement, numerical saving, weld specification, manufacturing validation or CAD geometry was invented.

- **8 mm NeSt case:** the owner's earlier confirmations establish the account: bend-relief slits tore; repair welding/rework followed; two parts were welded with a planned joint; repair work from the torn reliefs was eliminated. Planned joining remained. There is no independent incident/acceptance record. The diagram remains a representative principle sketch, not the customer part.
- **General NeSt duties:** assembly/drawing/product-development scope is supported by the supplied employment reference. Supplier/ERP details follow the supplied CV and are qualified in the source/context material.
- **Existing self-reported NeSt metrics:** platform/drawing volume and cost/weight percentages remain accessible with their original self-reported qualification. They were not elevated to verified headline achievements.
- **PAU:** report-based 48 → 18 kW design capacity, approximately 500 → 50 mbar pressure loss and rounded approximately €4,200 cost comparison remain qualified. No measured operating-energy saving is implied. The unsupported space-percentage basis is still not promoted.
- **FOUP:** actual approved source figures, the existing observation table, nominal electrical-input versus absorbed-heat distinction, material response and measurement/thermal-management limitations remain. The already-visible temperature figure is not duplicated inside the Mechanical methodology section; it remains accessible in the card and full gallery.
- **ANSYS, academic and AI/CAD work:** remain clearly training, academic or exploratory work in the archive. No independently validated industrial performance, ±50 µm accuracy or unsupported project grade was added.

The existing claim ledger remains applicable: [recruitment-claims.json](recruitment-claims.json). Independent manufacturing records and quantified acceptance/cost evidence would strengthen the portfolio later; no new facts are required to present the currently confirmed account accurately.

## 6. Functional and responsive test results

All final suites passed on the fresh preview server:

- **14 targeted Mechanical samples:** EN/DE at 320, 375, 390, 430, 768, 1024 and 1440px; correct three-case order; five preserved archived projects; visible challenge/decision/result/visual; five evidence groups; professional references first; source/context access; no horizontal overflow.
- **28 all-profile samples:** German/English Mechanical and R&D; matching CV links, profile order, six-step detailed reasoning, contrast checks in light/dark themes and profile/language/anchor context.
- **98 existing UX samples:** existing routes, menu/Escape focus, keyboard controls, typography, evidence search/empty results, no-JavaScript access, reduced motion, print behavior and back-to-top.
- Existing browser checks: filters, theme persistence, clipboard, evidence viewer and bilingual routes passed.
- Existing academic gallery/local CAD checks: 96 figures, pagination/filtering/zoom, supported/invalid mesh input and no mesh upload passed.
- Download-security checks: previews remain public; original downloads require the password; wrong-password/tamper rejection, byte-exact recovery, no password transmission/storage and viewer cleanup passed.
- Static build/check: 20 generated HTML pages; local links/anchors, alt text, IDs, language, source structure, career/CV hashes and publication boundaries passed.
- Python/JavaScript syntax and `git diff --check`: passed. CV files and `scripts/career.py` show no diff.

The first final rerun encountered a local preview connection refusal. It was rerun against a fresh server with a larger request queue; every suite then passed. This was not hidden as a successful test.

Browser coverage is **Playwright Chromium only**. No real iOS/Android, Safari/Firefox, full screen-reader audit or complete WCAG conformance claim is made. Existing public previews can still be saved/captured; the unchanged password mechanism protects separate original-file downloads, not on-screen information. No confidential original was added or access restriction weakened.

## 7. Remaining recommendations and publication status

1. Review the three leading cases and their source subsections in the local preview, then approve publication if accepted.
2. Add a sanitized manufacturing-change/acceptance record if available; it would strengthen the NeSt account more than additional decorative imagery.
3. Keep new academic/experimental work in the archive unless its evidence becomes strong enough to justify featured placement.
4. Validate on actual phones and Safari/Firefox before claiming device-level coverage. The unchanged PDFs remain untagged; the existing accessible HTML CV path remains available.
5. Historic public copies are a pre-existing repository-history issue and require a separate cleanup decision. This task did not rewrite history.

The result is a more focused Mechanical Design recruitment page: industrial experience first, interdisciplinary evidence next, and supporting work on demand. This is a qualitative hiring-manager-style assessment, not a measured hiring outcome. **Commit, push and deployment approved on 29 October 2026.**
