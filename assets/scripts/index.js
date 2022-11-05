import './navbar'
import './pmi_calculator'
import './charts'
import 'echarts'

const msgCloseButton = document.querySelector('button.delete');
const successMessage = document.querySelector('article.message');

msgCloseButton.addEventListener('click', () => {
    successMessage.classList.add('is-hidden');
});