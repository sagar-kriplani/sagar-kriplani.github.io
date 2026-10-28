# Portfolio review and requested revisions

Review date: 29 October 2026 (Europe/Berlin). Baseline public commit: `b94b453`.

**Publication approved by the owner on 29 October 2026.** The reviewed version is authorized for commit, push and deployment. Historical repository cleanup is outside this approval.

## Requested revisions

| Request | Result | Verification |
| --- | --- | --- |
| Restore the original dark/light symbol | Restored the original `◐` glyph; retained theme behavior and keyboard label | Browser screenshot and theme persistence regression |
| Remove sticky header | Header scrolls normally; one back-to-top arrow remains | All seven viewport sizes; return-to-top and footer non-overlap checks |
| Align languages | Five consistent label/proficiency rows using a responsive definition-list grid | English/German, desktop/mobile, no overflow |
| Consistent project timelines | Every project has a semantic, consistently formatted project-period row | Eight project cards in both languages |
| Add missing projects | Added AI Integration in Mechanical CAD Workflows, 01/2024–Present, as self-reported ongoing work | No supplied code/results/benchmark treated as verified |
| Handling project | Already present; 08/2022 and module grade 1.3 retained; cylindrical mechanism described accurately | No unsupported measured ±50 µm positioning-accuracy claim |
| Heat-transfer project | Existing MATLAB frost project retained; user-supplied 01/2019–12/2020 period identified as self-reported | No unsupported project-specific 1.0 / AA grade or validated CFD/mass-transfer result |
| Password-controlled downloads | Public document and project previews restored; separate original-file downloads encrypted (132 files) | Correct password, wrong password, tampering, byte-identical download and no password transmission tests |

Original project/source documents remain outside public hosting. No employer CAD or confidential raw document was added to packages. The latest instruction restores public previews and requires a password only for official original-image downloads; CV PDFs remain public.

## Public viewing and password-controlled original downloads

Latest owner instruction: every approved document/project image and all public data must remain visible without a password. **Public previews are therefore intentionally saveable and capturable.** This is not copy prevention or protection of information displayed on screen.

Every file-based image viewer now opens a public preview immediately. Selecting **Download original** opens the password form. Successful local decryption enables **Save original file** for the separate byte-exact original. The visible preview is not replaced with the original. Closing/changing the viewer clears passwords and revokes the temporary download URL. The original must be unlocked again on reopening.

There are **132 encrypted originals**: 29 redacted certificate/reference/transcript images, 96 academic gallery images, 6 additional project diagram/figure files, and the portrait. Public raster previews are separate compressed display derivatives. The simplified public SVG remains directly readable/saveable by its nature; its official original-file download uses the same password flow. Inline conceptual diagrams and browser screenshots are public and cannot be made confidential by a download button. CVs remain freely downloadable.

AES-256-GCM authenticated encryption, random 16-byte salts and 12-byte IVs, and PBKDF2-HMAC-SHA256 with 600,000 iterations protect the separate original packages. The generated long password and source-image backups remain in the sibling `private-portfolio-access` directory outside Git. The password never enters page source, browser storage or network requests. Package ciphertext is public; plaintext originals are not separately served from the current artifact except for intentionally public SVG content. Earlier public copies remain in Git history.

The exact public-preview/package paths are in [review/security-inventory.json](review/security-inventory.json). Keep the local password in a password manager and share it privately. To rotate future package access, change the local password file and run `scripts/protect_evidence.py --rotate` with the bundled Python/cryptography/Pillow environment. Previously downloaded packages or decrypted files cannot be revoked. This is file encryption, not per-recipient accounts or server-side access control.

No raw employer CAD or unredacted source document was packaged or made public. The original NDA exclusions remain. The old Brooks equipment URLs are still excluded; no force-push/history cleanup was performed. Publication of the current preview/download behavior is approved.

## Content and date decisions

| Project | Displayed period | Evidence level |
| --- | --- | --- |
| PAU redesign | 01/2023–06/2023 | Issued internship reference and project report |
| NeSt machine design | 09/2025–09/2026 | Employer reference; quantitative project figures remain self-reported |
| Thesis research | 07/2023–01/2024 | Owner-confirmed company research period; formal academic submission remains 02/2025 |
| Academic handling mechanism | 08/2022 | Dated academic report; Advanced 3D Design module grade 1.3 |
| ANSYS exercises | 2020 | Training/workbook records; month-level project dates not invented |
| MATLAB frost-growth modelling | 01/2019–12/2020 | New owner-supplied period; report limitations preserved |
| Diploma manufacturing concept | 2016–2017 | Academic report period |
| AI/CAD workflow | 01/2024–Present | Owner-supplied description only; no provided source code, FEA output or timing benchmark |

The source report for frost modelling acknowledges limitations from excluding mass transfer in its final model. The handling report does not establish measured ±50 µm accuracy. The AI project uses a clearly labelled conceptual workflow illustration; no generated image is presented as delivered or validated hardware. Existing projects were not duplicated.

## Preserved UX improvements

The original portrait/crop/frame, project filters, evidence search, 96-image academic gallery, local-only CAD viewer, separate Brooks roles, education timeline and six public CVs remain. The photo's decorative SK / 01 overlay stays removed. SVG directional controls, bilingual footer/legal/privacy routes, readable secondary text, German wrapping, no-JavaScript navigation, reduced-motion behavior and saved-theme reset from the preceding local review remain in place. Language switching preserves the active section.

There is no professional-profile switch in the actual implementation: it has mechanical/R&D project categories and three CV variants. No fictitious switching system was added. Body text remains left aligned; paragraphs are not justified.

## Privacy and legal details

The site adds no analytics, tracking pixels, third-party media or consent banner. Only the explicitly chosen theme preference is stored locally. Passwords are never persisted. Fonts, public images and encrypted files load from the same origin. Privacy text now explains public/saveable previews, separate encrypted original downloads, local decryption and its limitations. The Legal Notice uses name/email only, as explicitly requested by the owner; no postal address was inferred from private documents.

This technical review does not certify legal completeness. [DDG section 5](https://www.gesetze-im-internet.de/ddg/BJNR0950B0024.html) includes name/address duties within its scope; applicability and the owner's email-only notice require independent review. The storage assessment follows the narrow consent/necessity framework in [TDDDG section 25](https://www.gesetze-im-internet.de/ttdsg/__25.html). Host processing is described separately in [GitHub's privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Web Crypto behavior follows the platform [encryption](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/encrypt) and [key-derivation](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/deriveKey) APIs.

## Files and validation

Changes are concentrated in existing build/content/style/interaction modules. New shared modules are `scripts/ui.py` and `scripts/projects.py`; encryption preparation is in `scripts/protect_evidence.py`. Tests use the existing Playwright runtime, with `scripts/ux-check.cjs` and `scripts/security-check.cjs`. No deployment configuration was changed and no frontend dependency was added.

- Build: 16 generated HTML pages.
- Publication checks: local assets, anchors, IDs, languages, alt text, shared career/CV hashes, eight project date rows, 132 encrypted original files, all public previews present, and no password files in the artifact.
- Existing browser regression: project filtering, theme persistence, clipboard, mobile menu, document navigation, evidence filtering and no-JavaScript/print behavior.
- Gallery regression: 96 figures, pagination/filtering/zoom, valid/invalid mesh formats, no mesh uploads.
- UX suite: English/German home/CV/legal/privacy/evidence/gallery/CAD routes at 320, 375, 390, 430, 768, 1024 and 1440px (98 responsive samples), keyboard interactions and no horizontal overflow.
- Security suite: wrong-password rejection, successful local decryption, download matching the original bytes, ciphertext-tamper rejection, input editing, close/reopen cleanup, no password transmission/storage and no cookies.
- Syntax and whitespace checks: plain JavaScript/Python and `git diff --check`.

Only Playwright Chromium is available. No Safari, Firefox, real iOS/Android device, exhaustive penetration-test or full WCAG conformance claim is made. The six CV PDFs have not changed during this UX review; the new self-reported AI project is added to the website only pending supporting source material.

Local screenshots/results remain in ignored `qa/`, including `protected-access.png`, updated education/language layouts and `security-results.json`. Local preview: http://127.0.0.1:4174/ .

## Required next decisions

1. Commit/push/deployment approved on 29 October 2026; verify the live artifact after the Pages workflow completes.
2. Share the generated access password only with authorized document recipients, preferably separately from file links.
3. Decide separately whether to undertake public Git-history/cache cleanup for previously published documents and employer media.
4. Supply AI project files or measured accuracy/grade evidence later if those claims should become documented results.
