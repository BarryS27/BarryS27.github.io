# Barry Song | Personal Portfolio

![Website Status](https://img.shields.io/website?url=https%3A%2F%2Fbarrys27.github.io)
![License](https://img.shields.io/github/license/barrys27/barrys27.github.io)
![Top Language](https://img.shields.io/github/languages/top/barrys27/barrys27.github.io)

Welcome to the repository of my personal portfolio website. This site serves as a central hub to showcase my academic projects and technical skills. It is designed with a modern **Glassmorphism** aesthetic and hosted on **GitHub Pages**.

🔗 **Live Demo:** [https://barrys27.github.io/](https://barrys27.github.io/)

---

## 🎨 Design Philosophy: Glassmorphism

The visual identity is built around a modern **Glassmorphism** (frosted glass) aesthetic, focusing on clarity, depth, and a high-end digital feel.

* **Materials:** Multi-layered `backdrop-filter: blur()` effects combined with thin, translucent borders to mimic physical glass.
* **Typography:** **Inter** for primary UI readability; **Newsreader** for a refined, serif touch in specific contexts.
* **Responsiveness:** A mobile-first system utilizing a custom **Design Token**-based grid to ensure seamless adaptation across all devices.

## 🛠️ Technical Stack

This project balances backend logic with professional frontend engineering.

### Core technical stack
* **Python (Flask):** Handles the backend routing and dynamic data management.
* **Jinja2 Macros:** Utilized for a **Component-based Architecture**, allowing for reusable, clean, and DRY HTML structures.
* **SCSS (Sass):** A fully modular styling system using **Mixins** and **Nested Rules** for high maintainability.
* **Flask-Freeze:** Used to compile the dynamic Flask app into an optimized static site for GitHub Pages deployment.

## ✨ Key Features

* **Glass-Material Engine:** Custom SCSS mixins for consistent frosted-glass effects throughout the UI.
* **Componentized UI:** Navigation, cards, and buttons are all managed via Jinja2 macros.
* **Accessibility First:** Integrated `focus-visible` logic for keyboard navigation and `sr-only` support for screen readers.
* **Dynamic Metadata:** Automated year injection and professional copyright management.
* **Terminal-Style 404:** A custom error experience featuring a JS-powered typewriter animation.

## 📂 Project Structure

```text
/
/
├── app.py
├── freeze.py
├── templates/
    ├── layout.html
    ├── macros.html
    ├── index.html
    ├── 404.html
    └── work.html
└── static/
    ├── styles.scss
    ├── styles.css
    ├── script.js
    └── images/
```

## 👏 Credits

* **Background:** High-res photography from [Unsplash](https://unsplash.com/).
* **Icons:** [FontAwesome](https://fontawesome.com/).
* **Inspiration:** Various Glassmorphism UI kits and design communities.

---

*The code is available under the MIT License, but the text content and images are © Barry Song.*
