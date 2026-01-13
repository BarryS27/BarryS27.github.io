function togglePin() {
    const island = document.getElementById('island');
    island.classList.toggle('pinned');
    
    const isPinned = island.classList.contains('pinned');
    localStorage.setItem('navPinned', isPinned);
}

document.addEventListener('DOMContentLoaded', () => {
    const island = document.getElementById('island');
    const isPinned = localStorage.getItem('navPinned') === 'true';
    if (isPinned) {
        island.classList.add('pinned');
    }
});

const backToTop = document.getElementById('backToTop');

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTop?.classList.add('visible');
    } else {
        backToTop?.classList.remove('visible');
    }
});

backToTop?.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});