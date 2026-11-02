# Brooks reference integration — 2 November 2026

Added the owner's supplied three-page employment reference, issued by Brooks Automation (Germany) GmbH on 28 October 2026, to the existing evidence presentation. Work remains on `develop`; production is unchanged until deployment is requested.

## Presentation and provenance

- One logical record, `brooks-thesis-reference`, with three public redacted page previews and a single encrypted original PDF. Both profiles feature the reference in their existing evidence cards. The older internship references remain available.
- Public previews: `assets/evidence/brooks-thesis-reference.webp`, `brooks-thesis-reference-2.webp`, `brooks-thesis-reference-3.webp`.
- The public metadata describes documented IR/quartz-heater/LED comparisons, spectroscopy, vacuum test-system development, experimental evaluation and CAD/PLM work. No new performance metrics or changes to career titles, employment dates or CV claims were introduced.
- Source PDF SHA-256: `7a07103d070d20ec6320b8fa0f464f8fe36bf5d70a792d694f4344774b6f868c`.

## Privacy and access

- Page 1: removed the birth-detail phrase with an irreversible raster redaction before resizing/encoding. The public name, employment information and technical duties remain readable.
- Page 3: cropped away the complete signatures, signatory names/roles and signing timestamp. The document text, issue date and issuer remain.
- Page 2: reviewed and retained; no additional private identification/contact block was present.
- Public pages are fresh RGB WebP images without PDF text layers, editable masks, document-author metadata, EXIF or XMP. Original private renders and the source PDF remain outside the repository.
- The unchanged original PDF is available only through `assets/protected/brooks-thesis-reference.skvault`, using the existing PBKDF2-SHA256/AES-256-GCM format, password and in-browser decryption flow. Every public page maps to this same package. The browser downloads it with `application/pdf`; it never substitutes the unredacted PDF into the public preview.
- The password was not rotated, printed or placed in source files. All 132 pre-existing encrypted packages and manifest entries are unchanged. The current manifest contains 133 originals; the evidence library has 30 records and 32 page links.

## Timeline discrepancy retained for owner review

The newly supplied reference states a thesis period of 1 July 2023–29 February 2024 and subsequent working-student employment of 1 March–30 June 2024. The approved portfolio/CV timeline currently uses July 2023–January 2024 and February–June 2024 respectively. This request adds documentary evidence; it does not reconcile these periods or regenerate the six reviewed CVs. The source pages retain the issuer's actual text.

## Verification

- Visually inspected all original pages and all three final redacted previews. Verified a solid raster redaction over the removed birth information and the permanent signature crop; public image metadata contains no EXIF/XMP/comment fields.
- `python scripts/build.py` and `python scripts/check.py`: PASS, all 20 pages, every public page asset, internal anchors, 133-package coverage/checksums and the unchanged six-public-CV boundary.
- Extended existing protected-download browser checks: PASS in DE and EN. Every new page opens without a password; all three page links share one encrypted package. Wrong passwords fail; the existing password downloads the exact private PDF byte-for-byte with the correct MIME type. No password transmission/storage, cookies, console errors or unprotected original URL.
- Existing WebP/SVG/portrait protected downloads, tamper rejection, close/reopen cleanup and PDF header validation also passed.
- Existing general browser regression suite: PASS, routes, responsive layouts, filters/search, 30 evidence records, six references, viewer navigation, no-JavaScript and print.
- New reference layout checked in 16 DE/EN × light/dark × 375/768/1440/1920 px combinations: PASS, three page controls, no horizontal overflow or console errors. Desktop/light and mobile/dark screenshots were visually reviewed.
- JavaScript syntax checks and `git diff --check`: PASS. No image generation, new runtime dependency, raw public PDF, changed career data or CV regeneration.

Local review: `/en/evidence/#brooks-thesis-reference` and `/de/evidence/#brooks-thesis-reference` on the existing port-4174 preview. Browser artifacts are ignored under `qa/`.
