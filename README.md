# Barry Song | Personal Portfolio

![Website Status](https://img.shields.io/website?url=https%3A%2F%2Fbarrys27.github.io)
![License](https://img.shields.io/github/license/barrys27/barrys27.github.io)
![Top Language](https://img.shields.io/github/languages/top/barrys27/barrys27.github.io)

Welcome to the repository of my personal portfolio website. This site serves as a central hub to showcase my academic projects and technical skills. It is designed with a modern **Glassmorphism** aesthetic and hosted on **GitHub Pages**.

🔗 **Live Demo:** [https://barrys27.github.io/](https://barrys27.github.io/)

---

## 🎨 Design Philosophy: Glassmorphism

The visual identity of this website is built around the **Glassmorphism** (frosted glass) trend. The goal was to create a clean, modern, and depth-rich interface.

* **Visuals:** Utilization of semi-transparent backgrounds with `backdrop-filter: blur()`, subtle white borders, and soft shadows to mimic floating glass cards.
* **Typography:** [Inter](https://fonts.google.com/specimen/Inter) for clean readability and [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) for code-related elements.
* **Responsiveness:** A mobile-first approach ensuring the layout adapts seamlessly from desktops to smartphones using CSS Grid and Flexbox.

## 🛠️ Technical Stack

This project is built with pure web technologies without heavy frameworks, focusing on performance and animation control.

### Core
* **HTML5:** Semantic markup for better accessibility and SEO.
* **CSS3:** Custom styling featuring CSS Variables, Flexbox, Grid, and media queries.
* **JavaScript (ES6+):** Logic for DOM manipulation and animation triggering.

### Libraries & Tools
* **[GSAP (GreenSock)](https://greensock.com/gsap/):** Used for high-performance animations (Entrance effects, Staggered reveals).
    * *Plugins:* `ScrollTrigger` for scroll-based interactions.
* **FontAwesome 6:** For consistent and scalable vector icons.
* **Google Fonts:** Typography hosting.

## ✨ Key Features

* **Interactive "Now" Section:** A dynamic card on the homepage showcasing my current reading list and learning focus.
* **Project Showcase:** A dedicated `work.html` page detailing my technical projects (e.g., Student Academic Management System).
* **Custom 404 Page:** A terminal-inspired "Page Not Found" experience with a typewriter animation effect.
* **Smooth Navigation:** Floating sidebar navigation with hover effects and active state indicators.

## 📂 Project Structure

```text
/
├── index.html      # 🏠 Home: Introduction, "Now" section, Contact
├── work.html       # 💼 Work: Portfolio projects, Skills, Resume link
├── 404.html        # 🚫 Error: Custom terminal-style 404 page
├── style.css       # 🎨 Styles: Global styles, Glassmorphism classes, Responsive rules
├── script.js       # ⚡ Scripts: GSAP animation config
└── images/         # 🖼️ Assets: Profile pictures, project previews, favicon
```

## 🚀 How to Run Locally

If you want to view or modify this project on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/barrys27/barrys27.github.io.git](https://github.com/barrys27/barrys27.github.io.git)
    ```

2.  **Navigate to the folder:**
    ```bash
    cd barrys27.github.io
    ```

3.  **Open `index.html`:**
    You can simply double-click `index.html` to open it in your browser.
    > *Tip: For the best experience (to avoid CORS issues with local files), use a local server like Live Server in VS Code.*

## 👏 Credits

* **Background:** High-res photography from [Unsplash](https://unsplash.com/).
* **Icons:** [FontAwesome](https://fontawesome.com/).
* **Inspiration:** Various Glassmorphism UI kits and design communities.

---

*The code is available under the MIT License, but the text content and images are © Barry Song.*
