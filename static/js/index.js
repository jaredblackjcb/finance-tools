const msgCloseButton = document.querySelector('button.delete');
const successMessage = document.querySelector('article.message');

msgCloseButton.addEventListener('click', () => {
    successMessage.classList.add('is-hidden');
});