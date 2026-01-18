// Contact Modal
const modal = document.querySelector('div[role="dialog"]');
const trigger = document.querySelector('#contact-trigger');
const closeBtn = modal.querySelector('button[type="button"]');

trigger.onclick = () => { modal.style.display = 'flex'; };
closeBtn.onclick = () => { modal.style.display = 'none'; };

window.onclick = (e) => { if (e.target == modal) modal.style.display = 'none'; };