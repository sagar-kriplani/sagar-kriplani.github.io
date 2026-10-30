# Shared colour reference — 30 October 2026

The owner requested that the gallery, CAD viewer, evidence pages and the entire site match the homepage in both themes. The approved layout, content and image assets are retained. Work is saved on `develop`; this update does not publish to production.

## Shared palette

All 20 built pages, both languages and both engineering profiles now inherit one root palette from `assets/site.css`. Profile rules choose the existing decorative scenes without overriding the shared colours.

| Token | Light | Dark |
|---|---|---|
| Background | `#f3f6f8` | `#111820` |
| Surface | `#e5edf2` | `#172b3a` |
| Text | `#172b3a` | `#f0f4f7` |
| Secondary text | `#465e70` | `#aebcc7` |
| Accent | `#12617f` | `#48bfe3` |
| Border | `#bdccd7` | `#3b5265` |
| Card | `#fbfdfe` | `#203c52` |
| Image/canvas stage | `#e1eaf0` | `#142c3d` |

Gallery/evidence frames, captions, filter controls, forms, image-viewer surrounds, header, footer, favicon and technical-evidence accents follow the shared identity. The CAD renderer reads the CSS background/accent colours and repaints on a theme toggle without resetting the model. Original source diagrams, photos and simulation results keep their original pixels and colours.

## Default appearance

New visitors start in light mode, including on devices configured for dark mode. Dark mode is enabled only by an explicit visitor choice, saved with the existing `portfolio-theme` key. The early `assets/theme.js` script restores a valid choice before the stylesheet paints; invalid/unavailable storage falls back to light. Without JavaScript, the default is also light. Device preference changes never override the website choice. Reset on the privacy page removes the saved choice and restores light. The DE/EN privacy copy and persisted maintenance instructions describe this behaviour.

## Verification

- Build and static validation: PASS, all 20 pages and existing publication boundaries.
- `node scripts/theme-check.cjs`: PASS, 120 combinations of 20 routes × light/dark × 375/782/1440 px. Every page/profile uses the exact same core colour tokens as the homepage; no horizontal overflow or console/HTTP errors. Main text, secondary text and accent contrast meet 4.5:1.
- Tests cover default light with dark OS settings, preference restoration before styles, persistence across reload/language navigation, reset, invalid/blocked storage, no-JavaScript default, gallery caption contrast, and live WebGL background/mesh colours.
- Existing browser regression suite: PASS, routes, responsive layouts, controls, theme persistence, image viewer, no-JavaScript and print. Width checks now wait for web fonts before measuring layout.
- Existing gallery/CAD regression suite: PASS, 96 figures, filtering/pagination, image zoom, STL/OBJ formats, error handling, local-only files and responsive layouts.
- JavaScript syntax checks and `git diff --check`: PASS. No runtime dependencies added, image generated, credentials changed or CV regenerated.
- Visually inspected screenshots for light desktop gallery, dark mobile gallery figure/caption, dark desktop CAD canvas and dark mobile evidence page. Additional screenshots and machine-readable results are under ignored `qa/`, named `theme-{light|dark}-{page}-{375|1440}.png` and `theme-results.json`.

## Review

Start the local preview with `python scripts/preview.py --port 4174`. Check `/en/`, `/en/gallery/`, `/en/cad/` and `/en/evidence/`, then switch to German and toggle the theme. `main` remains the live release until the owner explicitly requests deployment.
