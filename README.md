# Barry Song | Personal Portfolio

![Website Status](https://img.shields.io/website?url=https%3A%2F%2Fbarrys27.github.io)
![License](https://img.shields.io/github/license/barrys27/barrys27.github.io)
![Top Language](https://img.shields.io/github/languages/top/barrys27/barrys27.github.io)

This repository contains the source code for my personal portfolio website.  
I built this project to organize my work, practice frontend development, and explore how design and code can work together.

🔗 **Live Site:** https://barrys27.github.io/

---

## 🎯 Project Goals

This project started as a simple personal website, but gradually turned into a learning project focused on:

- Writing cleaner and more reusable HTML and CSS
- Avoiding repeated code by using components
- Making layouts easier to adjust and maintain
- Understanding how visual design choices affect usability

---

## 🎨 Visual Style

The website uses a **glass-style (Glassmorphism)** visual theme.

I was interested in how blur, transparency, and layering could create depth without making the interface distracting.

Some design choices include:

- Translucent surfaces with background blur
- Soft shadows to separate layers
- Rounded corners for a consistent visual language
- Simple motion feedback for interactive elements

---

## 🧱 Layout & Structure

The page is organized into three main visual layers:

1. **Hero section** at the top of the page
2. **Scrollable content area** with a rounded top edge
3. **Floating navigation buttons** that stay visible while scrolling

This structure helped me experiment with positioning, stacking contexts, and layout flow.

---

## 🧩 Reusable Components

To keep the code organized, I used **Jinja2 macros** to create reusable components.

Examples include:

- Navigation buttons
- Cards for projects and education
- Repeating content sections

Each component keeps the same layout and styling, while the content can be changed easily.  
This reduced duplication and made the site easier to update.

---

## 🛠️ Tools & Technologies

- **Python (Flask)** – routing and template rendering
- **Jinja2** – reusable HTML components (macros)
- **SCSS (Sass)** – organized and nested styling
- **Flask-Freeze** – generating a static site for GitHub Pages

---

## ✨ Features

- Reusable navigation and UI components
- Glass-style buttons and cards
- Keyboard-accessible navigation
- Automatically updated footer year
- Custom 404 page with a typing animation

---

## 📂 Project Structure

```text
/
├── app.py
├── freeze.py
├── templates/
│   ├── layout.html
│   ├── macros.html
│   ├── index.html
│   ├── work.html
│   └── 404.html
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
