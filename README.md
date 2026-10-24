# Sagar Kriplani — Bilingual Engineering Portfolio

[![Deploy to GitHub Pages](https://github.com/sagar-kriplani/Profile-sagarkriplani/actions/workflows/deploy.yml/badge.svg)](https://github.com/sagar-kriplani/Profile-sagarkriplani/actions/workflows/deploy.yml)

Live Website: **[https://sagar-kriplani.github.io/](https://sagar-kriplani.github.io/)**

## Overview

Professional engineering portfolio of **Sagar Kriplani (M.Sc. Scientific Instrumentation)**, featuring two differentiated professional profiles and instant bilingual German/English switching:

1. **Mechanical Design Engineer** (*Konstrukteur Maschinenbau & Sondermaschinen*)
   - Positioning: Special-purpose machinery, machine enclosures, precision mechanical systems, Trumpf sheet-metal unfolding, welded frames, DFM/DFA, DIN/ISO production drawings, GD&T (DIN EN ISO 1101), cost and weight reduction.
   - Core Experience: NeSt GmbH Sondermaschinenbau & Anlagenbau (Herbrechtingen), Ravi Brass Industries.

2. **R&D Engineer — M.Sc. Scientific Instrumentation** (*F&E Ingenieur*)
   - Positioning: Semiconductor equipment, high-vacuum systems (HV/UHV), thermal radiation systems, process air thermodynamics (EUV Pod / FOUP cleaning), optical metrology, coupled ANSYS FEA/CFD simulation, experimental test bench validation.
   - Core Experience: Brooks Automation (Deutschland) GmbH (Steißlingen), Ernst-Abbe-Hochschule Jena.

---

## Key Features

- **Instant Bilingual Switching (DE | EN):** German default with seamless toggling between German and English without full page reloads, maintaining active profile state.
- **Two Differentiated Profiles:** Dynamic switching between Mechanical Design and R&D views with customized hero, scope metrics, featured case studies, experience records, technical stack, and education.
- **4 Distinct CV Downloads:**
  - Mechanical Design Engineer — German CV (`assets/docs/mechanical-design-de.pdf`)
  - Mechanical Design Engineer — English CV (`assets/docs/mechanical-design-en.pdf`)
  - R&D Engineer — German CV (`assets/docs/rd-engineer-de.pdf`)
  - R&D Engineer — English CV (`assets/docs/rd-engineer-en.pdf`)
- **Contact & Profile Modal:** Interactive profile overlay with verified contact information, work authorization (EU Blue Card), social links, and direct access to all four CV documents.
- **Theme Switcher:** Dark mode and light mode with persistent storage (`localStorage`) and system preference support.
- **Responsive Architecture:** Mobile drawer menu, fluid grid layouts, tablet and phone optimization.
- **Production-Ready & Zero-Dependency:** Ultra-fast static architecture ready for direct GitHub Pages deployment.

---

## Repository Structure

```
├── .github/workflows/
│   └── deploy.yml              # GitHub Pages CI/CD workflow
├── assets/
│   ├── css/
│   │   └── style.css           # Core stylesheet (typography, themes, responsive layout)
│   ├── docs/                   # Public engineering CV variants (DE & EN)
│   ├── drawings/               # Technical SVG diagrams
│   └── profile-placeholder.svg # Monogram technical stamp
├── cv/                         # Mirrored CV directory
├── public/cv/                  # Public CV directory
├── index.html                  # Single-page bilingual application
└── README.md                   # Documentation
```

## Deployment

Pushed to GitHub branch `main`. Automatically deployed to GitHub Pages via `.github/workflows/deploy.yml`.

---
© 2026 Sagar Kriplani. All rights reserved.
