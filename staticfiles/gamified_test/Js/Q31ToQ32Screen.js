import SpeechSynthesisModule from './speechSynthesisModule.js';
import sendPerformanceData from './AJAXModule.js';

// Retrieve the list data from the HTML attribute and parse it as JSON
const listData = document.getElementById("myScript").getAttribute("data-list");
const list = JSON.parse(listData);
var exerciseNum = parseInt(document.getElementById("myScript").getAttribute( "data-exerciseNum" ));

const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");
let randomIndex, selected, timerOn=false;

let duration = 25;
let timerCount = duration;

function generateExercise() {
    randomIndex = Math.floor(Math.random() * list.length);
    selected = list[randomIndex];
    // Play sound of the selected item then start timer
    SpeechSynthesisModule.speak(`Write ${selected}`);
    if(!timerOn){
        setTimeout(() => {
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
        }, 400);
        timerOn=true;
    }
}

document.getElementById('userInput').addEventListener('change', function() {
    const userInput = this.value.trim().toLowerCase().replace(/\s+/g, ''); // Remove white spaces from user input
    const selectedString = selected.replace(/\s+/g, ''); // Remove white spaces from selected item
    clicks =  userInput.length;
    console.log( `clicks: ${clicks}`);
    // Check if the user input matches the selected item
    if (userInput === selectedString) {
        hits++;
    } else {
        misses++;
    }
    // Clear the input field and play a new word
    this.value = '';
    list.slice(randomIndex,0);
    generateExercise();
});
//performance metrics
let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];
window.onload = generateExercise;
