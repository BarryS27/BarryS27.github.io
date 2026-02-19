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



// =========================================
// Easter Eggs
// =========================================

// Console Signature
const printSignature = () => {
    const brandColor = '#007AFF';
    const textColor = '#1C1C1E';

    const asciiArt = `
     ____  ____  ____  ____ ___  _
    /  __\\/  _ \\/  __\\/  __\\\\  \\//
    | | //| / \\||  \\/||  \\/| \\  / 
    | |_\\\\| |-|||    /|    / / /  
    \\____/\\_/ \\|\\_/\\_\\\\_/\\_\\/_/   
    `;

    const styles = [
        `color: ${brandColor}`,
        'font-size: 12px',
        'font-weight: bold',
        'font-family: monospace',
        'text-shadow: 2px 2px 4px rgba(0,0,0,0.1)'
    ].join(';');

    const subStyles = [
        `color: ${textColor}`,
        'font-size: 14px',
        'font-weight: 500',
        'font-family: -apple-system, system-ui, sans-serif'
    ].join(';');

    const linkStyles = 'color: #34C759; font-weight: bold; text-decoration: underline;';

    console.log(`%c${asciiArt}`, styles);
    console.log('%c🚀 High School Student | Data Enthusiast', subStyles);
    console.log('%cFind me on GitHub: %chttps://github.com/BarryS27', subStyles, linkStyles);
};



document.addEventListener('DOMContentLoaded', () => {
    printSignature();
    initScrollObserver();
    initSmoothScroll();
});