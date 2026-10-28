# Sagar Kriplani — Engineering portfolio

Live: https://sagar-kriplani.github.io/

A responsive bilingual portfolio for mechanical design and development, with original conceptual technical diagrams and Sagar’s supplied CV portrait.

## Build and check

Requires Python 3.8+; no third-party build packages.

```
python scripts/build.py
python scripts/check.py
python -m http.server 4174 --directory dist
```

Open http://localhost:4174. Source copy and page templates live in `scripts/build.py`; reviewed evidence, new project copy and gallery rendering live in `scripts/evidence.py`; styles and interactions in `assets/site.css` and `assets/site.js`. Locally hosted fonts avoid third-party font requests.

## Routes

- `/` and `/en/`: English portfolio
- `/de/`: German portfolio
- `/en/cv/` and `/de/cv/`: corrected printable CVs, with browser Print / Save as PDF
- `/en/legal/` and `/de/legal/`: operator and privacy information
- `/en/gallery/` and `/de/gallery/`: 96 academic figures, project filters, progressive loading and image zoom
- `/en/cad/` and `/de/cad/`: local-only STL/OBJ mesh viewer; no file upload or storage
- `/en/evidence/` and `/de/evidence/`: searchable evidence gallery with 29 redacted document excerpts

The language selector preserves the CV/legal page type. Project filters, native case-study disclosure, mobile navigation, clipboard copy, theme persistence, and print styles enhance the static content. Content remains readable without JavaScript.

## Content evidence

Read `CONTENT_AUDIT.md` for corrections, evidence, and remaining limits. The PAU project report and submitted thesis support the featured research narrative. Other role details are identified as supplied-CV information. No unsupported Senior title, generalized energy-saving guarantee, or employment authorization claim is published. No raw confidential reports, identity documents or original scans ship. Selected project-report figure excerpts and privacy-redacted certificate/reference/transcript images are explicitly identified. The equipment-themed LinkedIn illustration/animation and Brooks PAU CAD have been removed at the user’s NDA request. A text-free process-flow diagram replaces the PAU model.

Older PDFs and previous assets remain in repository history/source for reference, but are excluded from the public artifact. The public CV pages replace the disputed downloads. `IMPLEMENTATION_BRIEF.md` records the structured task prompt.

## Deployment

Push to `main` triggers `.github/workflows/deploy.yml`: build, check, upload **only `dist/`**, then deploy to GitHub Pages. The existing user-site endpoint is preserved. Build failures stop deployment. No Sites hosting account or alternate endpoint is necessary.

## Optional browser QA

Install Playwright in your development environment and its browser runtime, then run `node scripts/browser-check.cjs`. An existing installation can be selected through `PLAYWRIGHT_MODULE` and `PLAYWRIGHT_BROWSERS_PATH`. The script expects the local preview on port 4174. It checks bilingual routes, asset responses, layouts at 320/390/768/1024/1440 pixels, filters, disclosure, theme persistence, clipboard, mobile navigation, evidence search and filters, document-viewer keyboard navigation, NDA imagery exclusions, and no-JavaScript content. QA artifacts are ignored by Git.

The new gallery data is in `assets/gallery/catalog.json`; page rendering is in `scripts/gallery.py`; the dependency-free local mesh viewer is in `assets/cad-viewer.js`. Native CAD files remain local.

Run `node scripts/gallery-check.cjs` with the same Playwright environment for academic-gallery and local mesh-viewer checks. The build recreates only its verified `dist/` output to prevent removed assets surviving a local rebuild.
