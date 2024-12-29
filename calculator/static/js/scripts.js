document.getElementById('clearButton').addEventListener('click', function() {
    // Clear form fields
    document.getElementById('amount').value = '';
    document.getElementById('term').value = '';
    document.getElementById('rate').value = '';

    // Hide results
    const resultsDiv = document.querySelector('.card.mt-4');
    if (resultsDiv) {
        resultsDiv.style.display = 'none';
    }
});
