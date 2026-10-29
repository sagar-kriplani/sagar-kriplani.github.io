# Engineering slideshow review

## Scope and source

Implemented in the existing Python-generated static portfolio at `Profile-sagarkriplani/portfolio-redesign`, on local branch `codex/engineering-slideshow`. This checkout points to `sagar-kriplani/sagar-kriplani.github.io`. The implementation was first reviewed locally; the owner subsequently authorized production deployment in this chat. The earlier local modifications to `assets/site.css`, the four environment images and `review/visual-environments-review.md` were preserved.

The live website could not be fetched from this environment (DNS/access failure). Repository routes, build templates, public assets, published-artifact checks and local browser tests are the verification basis; live deployment parity cannot be independently confirmed.

## Audit

- Inspected all 144 image assets under `assets/`, including 96 gallery figures, project/evidence previews, portrait, backgrounds, legacy diagrams and favicon. See [complete inventory](engineering-asset-inventory.csv) for format, dimensions, aspect ratio, bytes and usage.
- Read the DE/EN home and profile content in `scripts/build.py`, `recruitment.py`, `mechanical_showcase.py`, `evidence.py`, `projects.py`, and the academic gallery catalog/rendering. Checked navigation, theme, project filters, detail disclosures, image viewer and language/profile links.
- Reviewed contact sheets of all 96 academic figures, with full-size checks for selected ANSYS outputs. Certificates, transcripts, generic diagrams and decorative backgrounds are not engineering-project slides.
- Employer CAD, hardware photography and raw models are deliberately excluded by the existing public-content review. No private originals, removed PAU geometry, stock assets or newly generated imagery were used. Existing illustrative profile backgrounds are reused only as decorative environments, never as project slides or evidence.
- Corrected 65 stale width/height pairs in the existing gallery catalog to match the already-optimized WebP files. This preserves one metadata source and avoids incorrect intrinsic image proportions; no image binary was changed.

## Selection and ranking

Subjective engineering/recruitment assessment on a 1–5 scale: complexity 30%, relevance to actual experience 25%, image clarity 20%, demonstrated competence 15%, recruiter engagement 10%. Ranking guides selection, while slide order tells the profile-specific story. Training scores lower for experience relevance than thesis evidence; component drawings score lower for complexity than complete mechanisms.

| Rank | Repository path | Dimensions / size | Scores C/R/Q/D/E | Weighted / 5 | Rationale |
|---|---|---|---|---|---|
| 1 | `assets/gallery/handling-27.webp` | 749 × 853 / 15.2 KiB | 5/4/4/5/5 | 4.55 | The clearest complete mechanism: coordinated base, column, rotary/vertical axes and gripper; strong lead image for practical mechanical design. |
| 2 | `assets/gallery/thesis-06.webp` | 1200 × 589 / 14.2 KiB | 4/5/4/5/4 | 4.40 | Directly relevant FOUP heating research: compares source-dependent temperature response. Lead R&D evidence without implying production readiness. |
| 3 | `assets/gallery/thesis-02.webp` | 1200 × 717 / 29.9 KiB | 4/5/4/4/4 | 4.25 | Material absorption provides a scientific reason for source selection, complementing temperature results rather than repeating them. |
| 4 | `assets/gallery/handling-09.webp` | 1004 × 893 / 20.2 KiB | 4/4/4/5/4 | 4.15 | Connects 3D guide geometry with dimensioned views. Adds integration and detailing evidence beyond the complete assembly. |
| 5 | `assets/gallery/thesis-01.webp` | 1200 × 462 / 23.6 KiB | 3/5/4/4/3 | 3.85 | Shows research structure: materials, experimental arrangement, heating procedure and evaluation. Complements measured results. |
| 6 | `assets/gallery/ansys-19.webp` | 1200 × 504 / 25.6 KiB | 4/3/4/4/4 | 3.75 | A clean, complex meshed frame with random-vibration output. Explicitly training, not an industrial validation claim. |
| 7 | `assets/gallery/frost-08.webp` | 1200 × 629 / 86.6 KiB | 4/3/4/4/4 | 3.75 | Legible three-dimensional numerical temperature output; extends R&D coverage beyond the thesis while identifying modelling rather than measurement. |
| 8 | `assets/gallery/handling-05.webp` | 977 × 690 / 11.8 KiB | 3/4/4/4/3 | 3.60 | A fabrication-oriented detail with a matching CAD view and drawing; grounds the gallery in manufacturable components. |
| 9 | `assets/gallery/ansys-25.webp` | 1200 × 641 / 58.6 KiB | 4/3/3/4/4 | 3.55 | A meshed finned component with static-structural deformation output. Deliberately not described as a thermal simulation. |

**Mechanical order (5):** `handling-27`, `handling-09`, `ansys-19`, `handling-05`, `ansys-25`. **R&D order (4):** `thesis-06`, `thesis-02`, `thesis-01`, `frost-08`. No image is repeated across profiles.

**Rejected/held back:** lower-resolution small gripper/support screenshots, handwritten force diagrams, repeated ANSYS exercise outputs, repeated thesis comparison charts and portrait-format shoe process tables. They either repeat a selected technical idea, lose clarity at showcase size, or add less profile relevance. Public equipment CAD/photos are unavailable, so the slides do not impersonate NeSt enclosures, the Brooks PAU, vacuum chambers or experimental hardware. Those existing text-led cases remain intact below.

## Placement and design

Immediately after the hero on `/`, `/en/`, `/de/`, and all four explicit profile pages, before the bridge, metrics, selected work and experience. Recruiters encounter visual evidence after reading the role introduction, with a direct path into the existing case studies. All eight project cards, evidence gallery, qualifications, CVs, contact information and SEO metadata remain.

The showcase follows the existing light/dark theme: pale steel-blue surfaces and dark text in light mode, graphite/navy surfaces and cyan accents in dark mode. It reuses the existing Inter/GeistMono fonts, icon helper, colour tokens and maximum-width token. Existing mechanical/research background images receive theme-specific scrims; smaller scene files load on mobile. The hero light-mode overlays were also refined for text contrast. Desktop uses a 72% central card and restrained adjacent previews; tablet uses 84%; mobile shows one complete image. Figures use `object-fit: contain`, never stretched or cropped. Text is below the image so captions cannot obscure axes or CAD features.

## Behaviour and accessibility

- Six-second automatic rotation, with wrapping previous/next arrows, numbered indicators, focused Left/Right keys and horizontal touch swipes. Vertical scrolling and pinch zoom remain available.
- Hover over the figure/caption temporarily pauses playback; moving away restarts a full reading interval. Pointer navigation and swipes resume the full six-second reading interval automatically. Anchor jumps and pointer focus do not disable rotation. Explicit Pause and actual keyboard exploration remain paused until Play is activated. Offscreen, inactive-tab and enlarged-view states suspend timers. The localized status explains the current playback state. No background interval loop.
- Reduced-motion preference defaults to paused and removes transitions/progress animation; a subsequent preference change pauses playback. Visitors can explicitly opt into playback.
- Only the active slide is exposed to accessibility APIs and keyboard focus; previews are inert. Manual changes produce localized status announcements; automatic changes are silent. Navigation does not move focus.
- Clicking either the main image or case-study link opens the matching existing case (`#handling`, `#ansys`, `#thesis`, `#frost`), resets an incompatible project filter if needed, and opens its disclosure.
- A separate enlarge link reuses the existing dialog, zoom controls, Escape and native focus return. Existing protected original downloads retain their prior behavior.
- Native language/profile links preserve the showcase hash. DE/EN headings, categories, alt text, captions, control names, playback text and status announcements are rendered through the existing Python localization approach.
- Without JavaScript, each route retains its linked first figure and full-gallery link; nonfunctional controls remain hidden.
- Existing WebP assets are already small (selected figures total about 285.6 KiB). First figure eager, others lazy; async decoding, correct intrinsic dimensions, fixed media stage. No new runtime/build package or image copy.

## Implementation files

- `scripts/showcase.py`: curated keys, bilingual captions, semantic static rendering; asset metadata comes from the existing catalog.
- `assets/showcase.css`: isolated responsive showcase styles and reduced-motion behavior.
- `assets/showcase.js`: progressive enhancement and autoplay lifecycle.
- `scripts/build.py`: insertion after hero, home-only CSS/JS inclusion, explicit build copy list.
- `assets/gallery/catalog.json`: corrected dimensions for optimized files.
- `scripts/showcase-check.cjs`, `package.json`: browser regression command `npm run test:showcase`.
- `index.html`: regenerated root fallback through the existing build.
- `README.md`: feature overview, review links and browser-test command.
- `review/engineering-showcase.md`, `review/engineering-asset-inventory.csv`: review and audit deliverables.

## Validation

- `python scripts/build.py`: PASS. Builds the existing 20-page bilingual artifact without third-party build packages.
- `python scripts/check.py`: PASS. All internal assets, anchors, languages, image alts, page semantics, reviewed CVs and publication boundaries verified.
- `node --check assets/showcase.js` and `node --check scripts/showcase-check.cjs`: PASS. No standalone lint/type-check task exists in this repository.
- `node scripts/showcase-check.cjs`: PASS. All 32 combinations of light/dark × DE/EN × mechanical/research × 375/768/1440/1920 px, including caption contrast of at least 4.5:1 and correct desktop/mobile background sources. Every selected image decodes and matches its catalog dimensions; all nine image links reach the correct existing case. No page overflow. Carousel height remains stable across every slide at these sizes.
- Feature tests also cover wrapping arrows, every indicator, scoped keyboard keys, real Chromium touch swipes, separate enlarged view, Escape and focus return, language/profile hash preservation, project-filter recovery, all case disclosures, and no-JavaScript content.
- Playback tests cover actual desktop and mobile six-second transitions, automatic resume after a real touch swipe, anchor-focus autoplay, silence of automatic accessibility announcements, hover pause, offscreen pause, explicit play/pause, persistent genuine keyboard-focus pause and live reduced-motion changes. Tab inactivity is checked with a synthetic `visibilitychange`/`document.hidden` transition in headless Chromium; manual testing of a real background tab remains a useful final review step.
- Existing `node scripts/browser-check.cjs`: PASS. Site routes, layouts, interactions, no-JavaScript and print behavior; zero console/network errors.
- Existing `node scripts/recruitment-check.cjs`: PASS. 28 role/language/viewport samples, matching CVs, case studies, skills, source context and contrast. Includes additional 320/390/430/1024 px widths.
- `git diff --check`: PASS. Existing user changes retained. No dependency added, image generated/downloaded, protected original exposed, or production ref changed.

Browser screenshots and machine-readable results live under ignored `qa/`: `showcase-results.json` and `showcase-{light|dark}-{en|de}-{mechanical|research}-{375|1440}.png` previews. These screenshots were visually inspected at desktop/mobile sizes; the full 32-combination browser matrix checks geometry and interactions. The local preview server remains available for the owner’s requested interactive review on port 4174.

## Review locally

```powershell
python scripts/build.py
python scripts/check.py
python scripts/preview.py --port 4174
```

Open `http://127.0.0.1:4174/en/mechanical/#engineering-showcase` or `/de/research/#engineering-showcase`. Use the existing Playwright runtime through `PLAYWRIGHT_MODULE` / `PLAYWRIGHT_BROWSERS_PATH` when running browser scripts. No standalone lint or type-check command is configured; the project is static Python/JavaScript rather than TypeScript.

Production deployment was authorized by the owner after the local previews and theme refinements. Publishing `main` triggers the existing Pages workflow, which rebuilds and checks the public artifact before deployment.

## Preview revision: autoplay, themes and mobile

The owner requested automatic playback and consistent dark/light, background-image and desktop/mobile design. The slideshow now distinguishes explicit/keyboard pauses from incidental pointer or anchor focus; mobile swipes resume automatically. Backgrounds follow the selected profile and responsive source. Both themes and all required viewport sizes passed browser QA. No new images, dependencies or production changes.

## Highlighted technical-evidence strip: light/dark correction

Addressed the owner's browser comments on `.metrics` in both profiles. The section previously combined a theme-aware surface with inherited dark-strip foreground colours and hard-coded pale source-note text. `assets/site.css` now applies matching theme tokens to the surface, values, labels, source notes and separators; the research accent has separate accessible light/dark colours. The strip aligns to the portfolio container. Desktop/tablet retain three columns; mobile at 600 px and below uses three readable rows with values beside their descriptions. No content, claims, interactions or project links changed.

Validation: build and all 20-page static checks passed. Chromium checked 56 DE/EN × mechanical/research × 320/375/600/768/782/1440/1920 px × light/dark combinations. Every value, label and source note exceeded 4.5:1 contrast (minimum 5.40:1), with no clipped text, horizontal overflow, changed content, browser errors or failed requests. Screenshots were visually reviewed at the owner's 782 px viewport and at 375 px mobile. Artifacts: `qa/metrics-theme-results.json`, `qa/metrics-{light|dark}-{mechanical|research}-{375|782}.png`. These checks were completed locally before the owner authorized deployment.
