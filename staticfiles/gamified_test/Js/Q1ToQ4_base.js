function generateGridTiles(gridSize) {
    const exerciseLetters = generateExercise(gridSize); 
    const gridContainer = document.getElementById('grid-container');
    
    // Clear existing grid tiles
    gridContainer.innerHTML = '';
    gridContainer.style.gridTemplateColumns = `repeat(${gridSize}, 1fr)`;

    // Generate and append new grid tiles
    exerciseLetters.forEach(letter => {
        const gridTile = buildGridTile(letter);
        gridContainer.appendChild(gridTile);
    });
}

// Function to generate exercise letters based on grid size
function generateExercise(gridSize) {
     // Generate random letter only once throughout the entire exercise
     if (!randomLetter) {
        randomLetter = String.fromCharCode(Math.floor(Math.random() * 26) + 97);
        console.log(`randomLetter: ${randomLetter}`);
    }
    const exerciseLetters = [];
    exerciseLetters.push(randomLetter);
    for (let i = 0; i < gridSize * gridSize-1; i++) {
        exerciseLetters.push(String.fromCharCode(Math.floor(Math.random() * 26) + 97));
    }
    return exerciseLetters;
}

// Function to build a grid tile
function buildGridTile(letter) {
    const gridTile = document.createElement('div');
    gridTile.classList.add('grid-tile');
    gridTile.textContent = letter;
    gridTile.addEventListener('click', () => {
        // calculate performance measures and generate a new grid for each click
        clicks++;
        if(letter == randomLetter) hits++;
        else misses++;
        generateGridTiles(gridSize);
    });
    return gridTile;
}

// Get elements from the included template after the page has loaded
document.addEventListener("DOMContentLoaded", function() {

const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");

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
        window.location.href = document.getElementById("myScript").getAttribute( "data-Url" );
    }
}, 1000);
});

var gridSize = parseInt(document.getElementById("myScript").getAttribute( "data-gridSize" ));
var randomLetter;
//performance metrics
let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];
generateGridTiles(gridSize);