// =========================================
// Slide-In Effect
// =========================================

const initScrollObserver = () => {
    const observerOptions = {
        threshold: 0.12,
        rootMargin: "0px 0px -50px 0px"
    };

    const animationObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
                animationObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('section').forEach(section => {
        animationObserver.observe(section);
    });
};

// --- 3. UI Interaction: Smooth Anchor Scroll ---
const initSmoothScroll = () => {
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId.startsWith('#')) {
                e.preventDefault();
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
};



document.addEventListener('DOMContentLoaded', () => {
    initScrollObserver();
    initSmoothScroll();
});