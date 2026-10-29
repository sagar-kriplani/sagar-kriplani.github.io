# Visual environment review — 29 October 2026

Local implementation only; not committed or published.

## Scope

Only `assets/site.css` and four new WebP background assets alter the site. No presentation markup was necessary. All 20 generated HTML pages, JavaScript and six CV PDFs match the pre-change SHA-256 snapshot byte for byte. Routes, IDs, section order, project descriptions, contact/CV links and data structures are unchanged.

## Visual changes

Mechanical: graphite, steel-blue, aluminium and restrained cyan with a generic precision-machine/CAD environment. Research: midnight navy, scientific teal/cyan, stainless vacuum-chamber imagery and a restrained warm heater glow. Light and dark palettes use the existing theme switch. Existing body profile attributes select the correct identity in both languages. Layered CSS masks protect hero text; other large surfaces use lower-intensity tonal treatments. Mobile uses smaller images and a stronger text overlay. No new animation, parallax, JavaScript or dependencies.

## Assets

Original concept artwork created with the built-in imagegen tool. These backgrounds are illustrative environments, not photographs or verified representations of Sagar's work, employer equipment or actual experiments. They must never be reused as technical evidence. No employer CAD/customer geometry was provided to the generator. Artwork was visually inspected for broad plausibility; it is not an engineering design or a scientific validation figure.

| Asset | Dimensions | Bytes |
|---|---|---|
| assets/images/mechanical-environment.webp | 1600 × 900 | 98120 |
| assets/images/mechanical-environment-mobile.webp | 800 × 450 | 33494 |
| assets/images/research-environment.webp | 1600 × 900 | 120534 |
| assets/images/research-environment-mobile.webp | 800 × 450 | 45464 |

Only the selected profile's background is requested. Responsive CSS selects the smaller source below 761 px. Image generation originals are retained outside the repository; project references use local WebP files. CSS backgrounds are decorative and add no screen-reader content.

## Checks

- Build and static validation: 20 pages, internal assets/links/IDs, languages and publishing boundaries passed.
- 32 combinations: DE/EN × Mechanical/Research × light/dark × 375/768/1074/1440 px. Background identity/source, primary and CV button contrast (at least 4.5:1), overflow and console/resource errors passed.
- Theme toggle/persistence and profile/language anchor context passed.
- Existing recruitment suite: 28 language/profile/viewport samples, CV paths, cases, skills, keyboard and no-JavaScript disclosure, public image viewer/protected-original controls, body and accent contrast passed.
- SHA-256 preservation: all generated HTML, JavaScript and six PDFs unchanged.
- Desktop and mobile screenshots reviewed. Reduced-motion mode tested; no new moving effects introduced.
- Chromium tested locally. No claim of complete WCAG certification, field performance measurements or real Safari/Firefox device testing.

Preview: http://127.0.0.1:4176/de/mechanical/ and http://127.0.0.1:4176/de/research/ . Both support EN and the existing theme control.

## Generation prompts (built-in tool)

### Mechanical

Use case: stylized-concept. Asset: wide cinematic photorealistic 3D background for a mechanical engineering portfolio, landscape 16:9. Original generic nonbranded precision machinery concept, NOT a real employer project. Main subject on right two thirds: sophisticated compact industrial machine with sheet-metal enclosure panels partially removed, welded frame, precision linear stages, spindle fixture, rails, bolted machined aluminium plates, plausible bearings and drives. Muted graphite #111820 and steel blue #172B3A, brushed aluminium, sparse cyan CAD edge overlays, subtle perspective engineering construction lines without text or dimensions. Left third calm dark negative space for web text. Studio-quality materials, controlled metallic reflections, restrained technical atmosphere, physically plausible machinery, no logos, no labels, no human, no futuristic holograms, no random gears, no neon. Elegant premium industrial CAD visualization, not an engineering evidence figure. Save usable generated image file and return its path.

### Research

Use case: stylized-concept. Asset type: landscape 16:9 cinematic realistic 3D background for scientific instrumentation R&D portfolio. Original illustrative laboratory concept, not evidence of an actual employer machine. High-vacuum stainless-steel chamber with physically plausible circular bolted flange, vacuum ports, restrained visible quartz radiant heating fixture behind a chamber viewport and separate experimental IR LED mounting array nearby (no exaggerated visible IR beams). Scientific metrology equipment and distant cleanroom engineer in proper cleanroom clothing provide depth. Subject mostly right two thirds; left third dark uncluttered negative space for website text. Premium realistic stainless materials, midnight blue #091724, scientific teal #167D91, restrained cyan #56D5E8 highlights; small warm amber #FF9D57 glow only at heating elements. Subtle technical construction lines, cleanroom background. No readouts, no graphs, no text, no logos, no holograms, no medical lab, no exposed electrical hazard, no invented machinery brand, no purple neon. Restrained technically credible scientific laboratory atmosphere.
