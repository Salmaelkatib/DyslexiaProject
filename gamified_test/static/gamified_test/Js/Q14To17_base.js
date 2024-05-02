import SpeechSynthesisModule from './speechSynthesisModule.js';
import sendPerformanceData from './AJAXModule.js';

const list = localStorage.getItem("listData") ? JSON.parse(localStorage.getItem("listData")) : { 
    "F": Array(12).fill('E').concat(['F'], Array(12).fill('E')),
    "E": Array(12).fill('F').concat(['E'], Array(12).fill('F')),
    "p": Array(12).fill('q').concat(['p'], Array(12).fill('q')),
    "b": Array(12).fill('p').concat(['b'], Array(12).fill('p')),
    "u": Array(12).fill('n').concat(['u'], Array(12).fill('n')),
    "n": Array(12).fill('u').concat(['n'], Array(12).fill('u')),
    "h": Array(12).fill('n').concat(['h'], Array(12).fill('n')),
    "d": Array(12).fill('b').concat(['d'], Array(12).fill('b')),
    "e": Array(12).fill('a').concat(['e'], Array(12).fill('a')),
    "i": Array(12).fill('j').concat(['i'], Array(12).fill('j')),
    "M": Array(12).fill('W').concat(['M'], Array(12).fill('W')),
    "q": Array(12).fill('g').concat(['q'], Array(12).fill('g')),
    "l": Array(12).fill('i').concat(['l'], Array(12).fill('i')),
    "K": Array(12).fill('X').concat(['K'], Array(12).fill('X')),
    "c": Array(12).fill('o').concat(['c'], Array(12).fill('o')),
    "j": Array(12).fill('i').concat(['j'], Array(12).fill('i')),
    "g": Array(12).fill('j').concat(['g'], Array(12).fill('j')),
    "a": Array(12).fill('e').concat(['a'], Array(12).fill('e')),
    "O": Array(12).fill('Q').concat(['O'], Array(12).fill('Q')),
    "t": Array(12).fill('f').concat(['t'], Array(12).fill('f')),
    "A": Array(12).fill('V').concat(['A'], Array(12).fill('V')),
};

let randomKey;
let [timerOn , playedSound] = [false , false];

function generateGridTiles(gridSize, list) {
    if(!playedSound) {SpeechSynthesisModule.speak('choose the different letter.'); playedSound=true;}
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
    const exerciseLetters = generateExercise(list);
    const gridContainer = document.getElementById('grid-container');

    // Clear existing grid tiles
    gridContainer.innerHTML = '';
    gridContainer.style.gridTemplateColumns = `repeat(${gridSize}, 1fr)`;

    // Generate and append new grid tiles
    exerciseLetters.forEach(letter => {
        const gridTile = buildGridTile(gridSize, letter);
        gridContainer.appendChild(gridTile);
    });
}

// Function to generate exercise letters based on grid size and list
function generateExercise(list) {
    const keys = Object.keys(list);
    randomKey = keys[Math.floor(Math.random() * keys.length)];
    console.log(`random key: ${randomKey}`);
    const exerciseLetters = list[randomKey];

    // shuffle list 
    for (let i = exerciseLetters.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [exerciseLetters[i], exerciseLetters[j]] = [exerciseLetters[j], exerciseLetters[i]];
    }
    return exerciseLetters;
}

// Function to build a grid tile
function buildGridTile(gridSize, letter) {
    const gridTile = document.createElement('div');
    gridTile.classList.add('grid-tile');
    gridTile.textContent = letter;
    gridTile.addEventListener('click', () => {
        console.log(`Clicked on letter: ${letter}`);
        // calculate performance measures and generate a new grid
        clicks++;
        if(letter == randomKey) hits++;
        else misses++;
        console.log(`clicks: ${clicks} hits: ${hits} misses: ${misses}`);
        delete list[randomKey];
        localStorage.setItem("listData", JSON.stringify(list)); // Update localStorage
        generateGridTiles(gridSize, list);
    });
    return gridTile;
}

const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");
const gridSize = parseInt(document.getElementById("myScript").getAttribute("data-gridSize"));
var exerciseNum = parseInt(document.getElementById("myScript").getAttribute( "data-exerciseNum" ));

let duration = 25;
let timerCount = duration;

//performance metrics
let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];
generateGridTiles(gridSize, list);
