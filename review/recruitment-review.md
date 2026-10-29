# Engineering recruitment optimisation — review package

Date: 29 October 2026 (Europe/Berlin). Baseline: `dce1285`. Development branch: `codex/recruitment-optimisation`.

**Implementation reviewed and publication approved by the owner on 29 October 2026.** Commit, merge to main and deployment are authorized. Historic repository cleanup is outside this approval.

## 1. Original weaknesses and audit

The mandatory pre-implementation audit is [recruitment-audit.md](recruitment-audit.md), classified KEEP / IMPROVE / FIX. The live English and German pages were inspected at 390, 768 and 1440px before implementation. The static builder, reusable content, CVs, academic figures, encrypted-original/public-preview mechanism and existing responsive/keyboard behavior were inspected.

Verified weaknesses:

- The hero led with a general slogan rather than a professional role and recruitment focus.
- There were **zero direct CV-PDF links in the hero** and **no actual professional-profile switch**.
- The three major projects used only three broad descriptive sections, obscuring requirements, analysis and decisions.
- The NeSt card relied on a generic enclosure illustration rather than a concrete manufacturing decision.
- Research charts existed in the gallery but were not assembled into a readable comparison with explicit measurement/energy qualifications.
- The source's 34% space claim did not reconcile with the stated geometry/basis.
- The approved CVs were searchable but had no link annotations, language metadata or tagged reading structure.
- A rendering defect added an unwanted semicolon to some unescaped ampersand abbreviations, such as R&D.

Kept: confirmed career dates/grades, separate Brooks roles, portrait and existing theme symbol, ordinary scrolling header, one back-to-top arrow, project filtering, 96 academic figures, public preview/password-original workflow, local CAD viewer and NDA exclusions.

## 2. Exact implementation

### Professional positioning and recruitment paths

Four server-rendered routes now exist:

- `/en/mechanical/` and `/de/mechanical/`
- `/en/research/` and `/de/research/`

The default homepage uses mechanical positioning. Native profile links work without JavaScript. With JavaScript, profile/language switching preserves the current section or project anchor; navigation within a profile stays on its profile route.

Mechanical pages lead with machine design, manufacturing-ready documentation, sheet metal/welded structures and DFM/DFA. R&D pages lead with the Scientific Instrumentation MSc, semiconductor equipment, vacuum/thermal work, material absorption and measurements. Distinction comes from wording, project order and restrained copper versus blue-green accents, not fabricated background machinery.

Each hero includes an explicit role, concise technical proposition, four specialisms, suitable-role context, technical-project action, **one-click matching PDF CV**, LinkedIn, email and an HTML-CV alternative. The professional photo, frame and crop remain; no SK/01 overlay, sticky header or new animation was introduced.

### Three engineering case studies

Each major project now follows six labelled stages: problem; requirements/constraints; analysis; decision; implementation; result/limitations. The summaries expose the evidence category before expansion. Native disclosure keeps all content available without hover or JavaScript.

**NeSt:** the owner confirmed that bend-relief slits tore in an 8 mm steel-sheet part, leading to repair welding/rework. The revision used two parts with a planned welded joint. The confirmed outcome is removal of the repair operation, not removal of all welding. A representative before/after diagram explains the manufacturing choice without customer geometry, weld dimensions or invented savings. Broader CAD/assembly/drawing/BOM responsibilities remain available.

**PAU:** added requirements, heater-duty and pressure-loss reasoning, component/integration considerations and an accessible before/after table. The text distinguishes design comparisons from measured operating energy. The text-free process schematic remains; no employer CAD or equipment photograph was reintroduced.

**FOUP research:** added the research question, reported test conditions, FTIR/visible/NIR method, 940 nm LED selection, source/material comparison, post-cycle measurement method and engineering decision. Two approved source graphs are embedded alongside a table of selected observations. Nominal input power, approximate electrical P × t comparison, surface temperature and absorbed heat are explicitly separated.

### Skills and professional level

Four groups replace the previous three-card structure: mechanical engineering; CAD/tools; thermal/scientific methods; manufacturing/documentation. Tool experience is qualified by professional versus academic/training evidence. No arbitrary progress bars, simulation-specialist title, management seniority, optical-design expertise or blanket DIN/ISO certification was added.

### CVs and PDF usability

The six approved CVs were reused. No employment date, qualification, grade, experience bullet or page layout was changed. Each PDF now has **five working link annotations**, language metadata and two section bookmarks. All 12 pages render pixel-identically to the approved baseline, and extracted page text is identical. Repository aliases were synchronized and the existing CV manifest refreshed.

The PDFs remain **untagged**; the update does not claim PDF/UA or fully verified screen-reader reading order. Searchable text, appropriate language metadata, clickable links and the HTML CV are meaningful improvements, not a substitute for a future properly tagged export.

## 3. Files modified

The complete path-level list is [recruitment-files.json](recruitment-files.json). Main changes:

| Files | Purpose |
| --- | --- |
| `scripts/recruitment.py` | Bilingual positioning, profile navigation, skill groups, six-step cases, representative manufacturing diagram and research comparison |
| `scripts/build.py` | New profile routes, role-led hero/direct CVs, project priority, shared rendering and sitemap |
| `assets/site.css` | Profile controls, role accents, readable hero/skills, case-study steps, figures and tables |
| `assets/site.js` | Preserve section context across profile links |
| `scripts/ui.py` | Correct ampersand/entity rendering while retaining SVG controls |
| `scripts/pdf_links.py` | Annotation-only CV link/bookmark/language updates |
| `assets/cv/*.pdf`, `assets/cv/manifest.json` | Six approved-content CVs with usability metadata; updated hashes |
| `assets/docs/`, `cv/`, `public/cv/` PDF aliases | Synchronize the same approved-content CV variants |
| `scripts/check.py`, `scripts/recruitment-check.cjs`, `package.json` | Publication/content checks and recruitment-specific regression coverage |
| `index.html`, `README.md`, `review/recruitment-*` | Generated root page, maintenance notes, source ledger and review package |

No deployment workflow, password, private original, employer CAD or raw report was added or changed.

## 4. Before / after

| Area | Before | After |
| --- | --- | --- |
| First impression | General slogan | Explicit engineering role, technical focus and role fit |
| Profile choice | No control | Two static professional paths in both languages |
| Hero CV access | Navigate to generic CV page | One click to relevant approved PDF; HTML/all-variant alternative |
| NeSt | Generic responsibility description | Confirmed failure → analysis → two-part welded solution → qualified outcome |
| PAU | Narrative metrics | Requirements/decision plus source-qualified before/after table |
| Thesis | Overview and gallery links | Test method, two readable source plots, numeric table and measurement/energy boundaries |
| Skills | Three broad cards | Four engineering capability groups with proficiency context |
| PDFs | Searchable text, unlinked printed addresses | Identical pages/text, five links each, language metadata and bookmarks |

Local screenshots, deliberately excluded from publication:

- [English before, mobile](../qa/recruitment-before-en-390.png) / [English R&D after, mobile](../qa/recruitment-after-en-research-390.png)
- [German before, desktop](../qa/recruitment-before-de-1440.png) / [German Mechanical after, desktop](../qa/recruitment-after-de-mechanical-1440.png)
- [NeSt reasoning](../qa/recruitment-nest-case.png) / [Thesis observation table](../qa/recruitment-thesis-table.png)

## 5. Claims and source verification

The structured ledger is [recruitment-claims.json](recruitment-claims.json). Private source reports were reviewed; they are not published or linked as unrestricted documents.

| Claim | Source and status | Treatment |
| --- | --- | --- |
| NeSt 8 mm tear / two-part welded revision / repair rework removed | Owner's two explicit confirmations in this chat, 29 October 2026 | Published as an owner-confirmed account; employer reference does not independently verify the incident |
| PAU 48 → 18 kW | Internship report, printed p. 53 | Heater design capacity, not metered energy saving |
| PAU ≈ 500 → 50 mbar | Same report, printed p. 53 | Approximate report-based pressure-drop comparison |
| PAU ≈ €4,200 / ≈ 21% | Report cost comparison p. 52 and conclusion p. 53 | Rounded result; not lifecycle cost or audited cash saving. Source table has a one-cent arithmetic inconsistency, so cent precision is not repeated |
| Employer reference 20% | Issued Brooks internship reference | Kept distinct from the report's approximately 21% |
| PAU 34% space reduction | Report statement does not reconcile with geometry/basis | Withheld; proprietary underlying dimensions are not republished |
| Thesis test conditions and measurements | Thesis methodology, printed pp. 45–46 | Reported 20 °C ambient / 0.03 kPa condition, not independently logged chamber performance; post-cycle IR camera and irreversible strips |
| 940 nm LED/material response | Thesis methods and conclusion p. 76 | Tested material-dependent conclusion, not universal polymer compatibility |
| Temperature comparison | Thesis Fig. 5-1, p. 63 | Four series × three selected observations transcribed; no interpolated data or fabricated error bars |
| Approximate equivalent-input comparison | Thesis Fig. 5-2/discussion pp. 63–65 | Nominal 550 W / 150 W and rounded durations; P × t is not absorbed thermal energy or measured complete-system efficiency |
| Limitations and radiant-heater preference | Thesis pp. 73–76 | Retained vent/cooling, emissivity, LED heat rejection, material-range and duration limitations |
| Existing NeSt 8+ platforms / 200 drawings / 70% / 60% figures | Owner-provided profile, existing approved CVs | Remain explicitly self-reported; not promoted as independently verified headline achievements |

## 6. Missing evidence / input

The manufacturing incident and joining method are now clarified; no further input is needed to show that account accurately.

For stronger independent evidence later:

- A sanitized NeSt fabrication/change/acceptance record supporting the incident and separately any quantitative project results.
- Source time-series data, chamber logs and a measurement uncertainty budget if new analysis or stronger efficiency claims are desired.
- Actual AI/Text-to-CAD code, model files, solver output and benchmarks before promoting that exploratory project to a validated engineering result.
- A properly tagged CV source/export for verified PDF/UA and screen-reader reading order.

## 7. Accessibility and responsive results

Tested in available Playwright **Chromium**, at **320, 375, 390, 430, 768, 1024 and 1440px**. No real-device or Firefox/Safari result is claimed.

- **28** samples across the four role/language combinations passed: headings, role/CV match, project order, six-step cases, four skill groups and no horizontal overflow.
- Existing UX suite passed **98** bilingual route/viewport samples. Together: **126** relevant responsive samples, plus separate gallery/security checks.
- Body and role-accent text contrast tested at **at least 4.5:1** in both themes for every role/language combination. This is targeted contrast testing, not a full site-wide WCAG conformance claim.
- Keyboard/native disclosure, visible focus, mobile menu/Escape focus, reduced motion and no-JavaScript profile/case access passed.
- New engineering tables have semantic row/column headers, captions and focusable horizontal-scroll regions.
- Source graphs have meaningful alt text and the key source values also appear as readable HTML data.
- All 12 CV pages render identically to the approved baseline. PDF links/language/bookmarks were verified; full tagged-PDF accessibility remains unresolved.

## 8. Build, functional and security results

- `python scripts/build.py`: passed, **20 HTML pages**.
- `python scripts/check.py`: passed routes/links/anchors, IDs/languages, alt text, role/CV structure, career facts, CV hashes and publication boundaries.
- Python compilation / JavaScript syntax checks / `git diff --check`: passed.
- `scripts/recruitment-check.cjs`: passed 28 role/profile samples and context/contrast/semantic-case checks.
- Existing browser regression: passed project/evidence filters, theme, clipboard, mobile navigation, document viewer, no-JavaScript and print behavior.
- Existing gallery regression: passed 96 figures, filtering/pagination/zoom and valid/invalid local mesh formats without uploads.
- Existing security regression: passed public previews, password-only original downloads, correct/wrong password, tamper rejection, exact recovered-file comparison, no password transmission/storage, and viewer cleanup.
- Existing UX regression: passed 98 route/viewport samples, no third-party requests/cookies/errors, language context and responsive interactions.
- No new frontend dependency, external font/image source, tracking system or scroll animation was added.

The root HTML increased from about **55.5 kB to 65.7 kB** before the final minor copy refinement, primarily for source-qualified case content and inline schematic markup. Images remain reused/lazy-loaded; no chart framework or heavy background media was introduced. The live baseline included warm-cache navigation samples, so a speed-improvement percentage or Core Web Vitals certification would be misleading and is not asserted.

No password or private backup is in the publication artifact. Approved previews are intentionally public and saveable; encryption protects separate original files, not the information visible on screen. Raw confidential reports/CAD remain excluded. Historic public copies are a pre-existing issue requiring separate approved cleanup; no history rewrite was performed.

## 9. Remaining recommendations

1. Review the local role pages and source-qualified case text, then approve publication if accepted.
2. For a stronger evidence package, add one sanitized manufacturing change/acceptance record rather than more decorative images.
3. Obtain a genuinely tagged CV export and test with assistive technology; the available HTML CV already offers a more semantic reading path.
4. Test actual iOS/Android and Firefox/Safari before making cross-browser/device claims.
5. Consider a short timed recruiter/hiring-manager review; no actual 10-second comprehension study or hiring-conversion experiment was conducted.
6. Keep confidential source data in private storage. Password-encrypted static files are not individual accounts or access revocation.

## 10. Recruiter-style assessment and acceptance

A fresh reviewer-style reading of the final implementation supports a clearer shortlist decision for **Konstruktionsingenieur / mechanical development / equipment engineering** roles. The NeSt account now demonstrates a concrete fabrication trade-off rather than software use alone. The R&D path offers an applied equipment/thermal-research narrative with material response, measurement limits and a defensible technology choice. It does not imply simulation-specialist, optomechanical-expert or engineering-management seniority.

The most persuasive material is the manufacturing failure/revision and the PAU/thesis reasoning. Independent evidence for the self-reported employment metrics remains the main credibility limitation. AI/CAD remains exploration, not a leading verified achievement. This is a recruiter-style qualitative assessment by the assistant, not an external recruiter's validation or a promise of interviews.

| Acceptance criterion | Assessment |
| --- | --- |
| Role understood quickly | Explicit title/focus/CV structurally improved; timed human study not performed |
| Two differentiated profiles | Implemented and tested |
| Three reasoning-led cases | Implemented with six stages each |
| Quantitative evidence | Traceable to sources or clearly owner-reported; independent proof incomplete for self-reported metrics |
| Confidentiality | Current artifact exclusions retained; historic copies remain a separate risk |
| English/German consistency | Four combinations tested; issued degree/course titles preserved |
| Relevant CV access | One click from each hero; PDFs have working links; full PDF tagging still open |
| Mobile use | Seven widths tested in Chromium; physical-device validation pending |
| Functional regression | Existing and new suites passed |
| Practical engineering judgement | Manufacturing trade-off, PAU design choices and research limitations now visible |

A blanket “9/10 achieved” would exceed the evidence. The implementation is substantially more useful for recruitment, with remaining limitations explicitly recorded rather than hidden behind a score.
