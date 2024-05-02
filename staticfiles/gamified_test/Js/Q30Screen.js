const letters = ["p g d j", "v h b z q", "m d j n p h", "i u e o", "b q l i", "h n w m"];
let selectedLetters;

// Function to hide the screen and start the test
function startTest() {
    document.getElementById('screen').style.display = 'none';

    // Randomly select a word from the array
    selectedLetters = letters[Math.floor(Math.random() * letters.length)];

    // Display the word for 5 seconds
    document.getElementById('wordDisplay').textContent = selectedLetters;
    setTimeout(() => {
        document.getElementById('wordDisplay').remove();
        document.getElementById('screen').style.display = 'flex'; // Reveal the screen again
    }, 5000);
}

document.getElementById('userInput').addEventListener('change', function() {
    const userInput = this.value.trim().toLowerCase().replace(/\s+/g, ''); // Remove white spaces from user input
    const selectedLettersString = selectedLetters.replace(/\s+/g, ''); // Remove white spaces from selected letters

    // Check if the user input matches the displayed word
    if (userInput === selectedLettersString) {
        alert('True');
    } else {
        alert('False');
    }

    // Clear the input field
    this.value = '';
});

window.onload = startTest;
