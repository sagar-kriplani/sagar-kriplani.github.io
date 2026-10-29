# Portfolio maintenance agreement

Owner instructions from 29 October 2026 apply to this repository and future maintenance.

## Approved design

- The owner approved the deployed design at commit `ab199efacf4d6267faa0699cb0c14d7a99323c42` as the visual baseline.
- Preserve its layout, typography, light/dark themes, responsive backgrounds, slideshow, profile navigation, evidence strips and existing sections.
- Future supplied updates and images should be integrated into the existing design. Resolve ordinary implementation choices and fix bugs without repeatedly asking for permission.
- Do not proactively redesign or add a new visual system. Work with the owner on `develop` when a design change is requested. Preserve the baseline until that change is explicitly agreed.

## Branch and release workflow

- `main` is production. A push to `main` triggers the GitHub Pages deployment.
- `develop` is the ongoing integration branch for content, images, fixes and jointly reviewed design changes.
- Start maintenance from the current `develop`; inspect Git status and preserve existing user changes. Do not overwrite another contributor's work.
- Integrate supplied content and images on `develop`. Keep production unchanged until the owner explicitly requests a deployment/release.
- When deployment is requested, finish appropriate checks, integrate the reviewed version into `main` without force-pushing, monitor the Pages workflow, and verify the live site. Do not ask for the same approval again.

## Content and image updates

- Maintain both German and English content and both professional profiles. Place each update in its technically relevant existing section/profile.
- Use supplied facts and verified project material. Do not invent achievements, technical specifications, outcomes, dates, job titles or measured performance.
- Use existing or newly owner-supplied images for project evidence. Do not generate replacement images or download stock photography. Existing illustrative background scenes remain decorative, never evidence of actual project work.
- Keep image aspect ratios, useful alt text, lightweight WebP delivery and accurate catalog dimensions. Avoid duplicate image metadata.
- Confirm image click-throughs reach existing relevant cases. Preserve public/private boundaries and original-file protection.
- Keep the CVs and their reviewed manifest unchanged unless the owner supplies or requests a CV update.

## Repository conventions

- The source is the existing dependency-free Python static site. Edit the relevant source modules in `scripts/`, shared assets, and `assets/gallery/catalog.json`.
- `scripts/build.py` generates `dist/` and the root `index.html`. Rebuild instead of hand-editing generated HTML.
- `scripts/showcase.py` holds curated slide keys and DE/EN copy; `assets/showcase.js` and `assets/showcase.css` provide its interactions and presentation.
- `assets/site.css` holds the shared theme and technical-evidence styling. Reuse its theme tokens and established responsive breakpoints.
- Run `python scripts/build.py` and `python scripts/check.py` for relevant changes. Use existing browser checks when layout, themes, navigation or interactions change; limit testing to affected behavior. There is no configured lint or TypeScript check.
- Local preview: `python scripts/preview.py --port 4174`. Existing Playwright installations may be selected through `PLAYWRIGHT_MODULE` and `PLAYWRIGHT_BROWSERS_PATH`; do not add runtime dependencies just for QA.

## Protected-download credentials

- The password and original backups are outside the repository in the sibling `private-portfolio-access/` directory. The password file is `evidence-password.txt` inside that private directory.
- Never copy the password, unencrypted originals, private backups or credentials into repository files, documentation, commits, public assets or deployment output.
- Password-protected downloads use `assets/protected/*.skvault`; public previews are intentionally viewable.
- Do not rotate the password or regenerate encrypted packages unless the owner explicitly requests it. Provide the existing password privately to the owner when requested, and verify it without persisting decrypted copies.
