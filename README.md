# Bairu (Barry) Song | Personal Portfolio

![Website Status](https://img.shields.io/website?url=https%3A%2F%2Fbarrys27.github.io)
![License](https://img.shields.io/github/license/barrys27/barrys27.github.io)
![Top Language](https://img.shields.io/github/languages/top/barrys27/barrys27.github.io)

This repository contains the source code for my personal portfolio website. I am a student at **Lexington High School** with a focus on data-driven decision making and modern web development.

🔗 **Live Site:** [barrys27.github.io](https://barrys27.github.io/)

---

## 🎨 Design Philosophy

The website implements a **Glassmorphism** visual language, drawing inspiration from modern iOS and macOS interfaces.

* **Standard Thin Material**: Utilizes a custom `std-thin` SCSS mixin for translucent surfaces with background blur and subtle high-light borders.
* **Tactile Feedback**: Interactive elements feature a `tap-effect` mixin that provides scale-based motion feedback and spring animations.
* **Visual Consistency**: A unified grid system is used for padding and margins to ensure a balanced, system-level layout.
* **Accessibility**: Color palettes are optimized for WCAG AA contrast standards to ensure readability across all devices.

---

## 🛠️ Technology Stack

* **Backend**: Python (Flask) for routing and site management.
* **Templating**: Jinja2 with custom macros to ensure modular and reusable UI components.
* **Styling**: Dart Sass Standalone + Lightning CSS binaries for modern SCSS support, autoprefixing, and minified output without Node runtime dependencies.
* **Deployment**: Flask-Freeze for generating the static site architecture for GitHub Pages.
* **Optimization**: GPU-accelerated animations using `will-change` and hardware-layering properties for smooth 120Hz performance.

---

## ✨ Key Features

* **Component-Based Architecture**: Reusable macros for badges and project cards reduce code duplication.
* **Dynamic Background**: A high-resolution mountain landscape background with ambient light gradients and a fixed parallax effect.
* **Hardware Acceleration**: Optimized scroll performance and slide-up entry animations for all sections.
* **Navigation**: A fixed, glass-material navigation bar with accessibility-focused ARIA labels.

---

## 📂 Featured Projects

* **Urban Scaling**: A data analysis project exploring the relationship between city size and various urban metrics.
* **uTerm-Lite**: A lightweight web application featuring a stock screener, heatmap, and advanced charting tools.
* **Nvidia Stock Analysis**: A project focused on analyzing financial performance and market trends for NVDA.

---

## 📂 Project Structure

```text
/
├── app.py                         # Flask app + JSON data loader
├── data.json                      # Portfolio content source of truth
├── scss.py                        # Python wrapper for standalone Sass + Lightning CSS
├── freeze.py                      # Flask-Frozen build + artifact verification
├── templates/
│   ├── index.html                 # Main page template
│   └── macros.html                # Reusable Jinja UI macros
└── static/
    ├── css/
    │   ├── styles.scss            # Main SCSS entrypoint
    │   └── _core.scss             # Shared design tokens and mixins
    ├── js/
    └── images/
```

Build flow uses `python scss.py` + `python freeze.py`; both scripts provision standalone binaries and run a Node-free pipeline.

Set `FLASK_ENV=development` for local debug mode, and optionally set `FREEZER_BASE_URL` (for example, `https://username.github.io/repo-name/`) to harden sub-path GitHub Pages builds.


## 🧱 Build Pipeline

- `python scss.py`: downloads/uses Dart Sass Standalone + Lightning CSS to compile, prefix, and minify `static/css/styles.scss`, with `vendor/ui` as an additional load path when present.
- `python freeze.py`: runs CSS build, optimizes images via Pillow, freezes the site, and verifies required artifacts.
- `.browserslistrc`: centralized browser support targets consumed by Lightning CSS.
- GitHub Actions runs weekly via cron and manually via `workflow_dispatch`, vendoring the latest `@barrys27/ui` tarball into `vendor/ui` without Node/npm.

## 📜 License

This project is available under the **MIT License**. Text content and personal images are © Bairu Song.

## 👏 Credits

* **Iconography**: [FontAwesome](https://fontawesome.com/).
* **Photography**: High-resolution backgrounds via [Unsplash](https://unsplash.com/).
* **Design Inspiration**: Apple's Human Interface Guidelines (HIG).
