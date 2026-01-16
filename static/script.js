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