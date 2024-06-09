import SpeechSynthesisModule from './speechSynthesisModule.js';
import sendPerformanceData from './AJAXModule.js';

function generateGridTiles(gridSize, my_list) {
    const exerciseLetters = generateExercise(my_list, gridSize); 
    const gridContainer = document.getElementById('grid-container');
    
    // Clear existing grid tiles
    gridContainer.innerHTML = '';
    gridContainer.style.gridTemplateColumns = `repeat(${gridSize}, 1fr)`;

    // Generate and append new grid tiles
    exerciseLetters.forEach(letter => {
        const gridTile = buildGridTile(gridSize,letter);
        gridContainer.appendChild(gridTile);
    });
}

// Function to generate exercise letters based on grid size and list
function generateExercise(list, gridSize) {
    // Generate random word only once throughout the entire exercise
    if (!randomElement) {
        randomElement =list[Math.floor(Math.random() * list.length)];
        console.log(`randomLetter: ${randomElement}`);
    }
    if(!playedSound) {SpeechSynthesisModule.speak(`Choose ${randomElement}`); playedSound=true;}
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
        }, 600);
        timerOn=true;
    }
    const exerciseLetters = [];
    exerciseLetters.push(randomElement);
    for (let i = 0; i < gridSize * gridSize-1; i++) {
        const randomIndex = Math.floor(Math.random() * list.length);
        exerciseLetters.push(list[randomIndex]);
    }
     //shuffle list 
     for (let i = exerciseLetters.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [exerciseLetters[i], exerciseLetters[j]] = [exerciseLetters[j], exerciseLetters[i]];
    }
    return exerciseLetters;
}

// Function to build a grid tile
function buildGridTile(gridSize,letter) {
    const gridTile = document.createElement('div');
    gridTile.classList.add('grid-tile');
    gridTile.textContent = letter;
    gridTile.addEventListener('click', () => {
        console.log(`Clicked on letter: ${letter}`);
        // calculate performance measures and generate a new grid
        clicks++;
        if(letter == randomElement) hits++;
        else misses++;
        generateGridTiles(gridSize, list);
    });
    return gridTile;
}
const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");
const list = JSON.parse( document.getElementById("myScript").getAttribute("data-list"));
const gridSize = parseInt(document.getElementById("myScript").getAttribute("data-gridSize"));
var exerciseNum = parseInt(document.getElementById("myScript").getAttribute( "data-exerciseNum" ));
let randomElement;
let [timerOn , playedSound] = [false , false];

let duration = 25;
let timerCount = duration; 

//performance metrics
let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];
generateGridTiles(gridSize, list);