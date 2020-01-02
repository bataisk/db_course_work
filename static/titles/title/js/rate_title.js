rateBlock = document.getElementById('user-rate-block');
rateForm = document.getElementById('user-rate-form');
rateTooltip = document.getElementById('rate-tooltip');


rateBlock.onclick = function () {
    rateForm.style.display = 'block';
    rateTooltip.style.display = 'none'
};