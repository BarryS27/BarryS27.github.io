/* =========================================
   Easter Egg: Console Signature
   Design System: Apple HIG / Glassmorphism
   ========================================= */

const printSignature = () => {
    const brandColor = '#007AFF';
    const textColor = '#1C1C1E';

    const asciiArt = `
    ██████╗  █████╗ ██████╗ ██████╗ ██╗   ██╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
    ██████╔╝███████║██████╔╝██████╔╝ ╚████╔╝ 
    ██╔══██╗██╔══██║██╔══██╗██╔══██╗  ╚██╔╝  
    ██████╔╝██║  ██║██║  ██║██║  ██║   ██║   
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
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
    console.log('%c🚀 High School Student | Data Enthusiast | Python Dev', subStyles);
    console.log('%cFind me on GitHub: %chttps://github.com/BarryS27', subStyles, linkStyles);
    console.log('%c"Precision meets Minimality."', 'color: #8E8E93; font-style: italic;');
};

document.addEventListener('DOMContentLoaded', printSignature);