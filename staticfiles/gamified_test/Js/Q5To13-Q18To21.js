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
    // Generate random letter only once throughout the entire exercise
    if (!randomElement) {
        randomElement =list[Math.floor(Math.random() * list.length)];
        console.log(`randomLetter: ${randomElement}`);
    }
    const exerciseLetters = [];
    exerciseLetters.push(randomElement);
    for (let i = 0; i < gridSize * gridSize-1; i++) {
        const randomIndex = Math.floor(Math.random() * list.length);
        exerciseLetters.push(list[randomIndex]);
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
list = JSON.parse( document.getElementById("myScript").getAttribute("data-list"));
gridSize = parseInt(document.getElementById("myScript").getAttribute("data-gridSize"));
let randomElement;

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
        window.location.href = document.getElementById("myScript").getAttribute("data-Url");
    }
}, 1000);

//performance metrics
let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];
generateGridTiles(gridSize, list);