import sendPerformanceData from './AJAXModule.js';

const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");
var exerciseNum = parseInt(document.getElementById("myScript").getAttribute( "data-exerciseNum" ));
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

        startTimer();
    }, 5000);
}

// Function to start the timer and progress bar
function startTimer() {
    let duration = 25;
    let timerCount = duration;

    const timerInterval = setInterval(() => {
        timerCount--;
        const progress = (duration - timerCount) / duration * 100;
        progressBar.style.width = `${100 - progress}%`;
        timer.textContent = timerCount;

        if (timerCount <= 0) {
            clearInterval(timerInterval); 
            // calculate missrate ,score, accuracy
            missrate = misses / clicks;
            accuracy = hits / clicks;
            score = hits;
             // save data and navigate to next question
             sendPerformanceData(exerciseNum, clicks, hits, misses, missrate, score, accuracy , window.location.href);
             setTimeout(() => {
                 window.location.href = document.getElementById("myScript").getAttribute("data-url");
             }, 1000);
        }
    }, 1000);
}

document.getElementById('userInput').addEventListener('change', function() {
    const userInput = this.value.trim().toLowerCase().replace(/\s+/g, ''); // Remove white spaces from user input
    const selectedLettersString = selectedLetters.replace(/\s+/g, ''); // Remove white spaces from selected letters
    
    clicks = userInput.length;
    // Check if the user input matches the displayed word
    if (userInput === selectedLettersString) {
       hits++;
    } else {
        misses++;
    }
    // Clear the input field
    this.value = '';
   // save data and navigate to next question
   sendPerformanceData(exerciseNum, clicks, hits, misses, missrate, score, accuracy , window.location.href);
   setTimeout(() => {
       window.location.href = document.getElementById("myScript").getAttribute("data-url");
   }, 1000);
});
//performance metrics
let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];
window.onload = startTest;
