// Contact Modal
const GAS_URL = "https://script.google.com/macros/s/AKfycbyoVKNhWd0fQZzjBhK9hT2t5VvNtMwxWXW5rl1YC7EZkyQEA0B8P4QfMO_AZCiBJYcZ/exec";

const modal = document.querySelector('div[role="dialog"]');
const form = modal.querySelector('form');
const textarea = modal.querySelector('textarea');

form.onsubmit = async (e) => {
    e.preventDefault();
    const content = textarea.value.trim();
    if (!content) return;

    const submitBtn = form.querySelector('button[type="submit"]');
    submitBtn.disabled = true;
    submitBtn.innerText = "Sending...";

    try {
        const response = await fetch(GAS_URL, {
            method: 'POST',
            mode: 'no-cors',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ comment: content })
        });

        alert('Message sent!');
        textarea.value = '';
        modal.style.display = 'none';
    } catch (error) {
        console.error('Error:', error);
        alert('Something went wrong.');
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerText = "Submit";
    }
};
