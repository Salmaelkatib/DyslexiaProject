list = JSON.parse( document.getElementById("myScript").getAttribute("data-list"));
const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");
let selected;


let duration = 25;
let timerCount = duration; 

const timerInterval = setInterval(() => {
    timerCount--;
    const progress = (duration - timerCount) / duration * 100;
    progressBar.style.width = `${100 - progress}%`;
    timer.textContent = timerCount;

    if (timerCount <= 0) {
        clearInterval(timerInterval); 
        // save data and navigate to next question
        window.location.href = document.getElementById("myScript").getAttribute( "data-url" );
    }
}, 1000);

function generateExercise(list) {
    selected = list[Math.floor(Math.random() * keys.length)];
    // play sound of selected item
}

document.getElementById('userInput').addEventListener('change', function() {
    const userInput = this.value.trim().toLowerCase().replace(/\s+/g, ''); // Remove white spaces from user input
    const selectedString = selected.replace(/\s+/g, ''); // Remove white spaces from selected item

    // Check if the user input matches the selected item
    if (userInput === selectedString) {
        alert('True');
    } else {
        alert('False');
    }

    // Clear the input field
    this.value = '';
});

window.onload = generateExercise();
