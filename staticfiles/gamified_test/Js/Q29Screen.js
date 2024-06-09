import SpeechSynthesisModule from './speechSynthesisModule.js';
import sendPerformanceData from './AJAXModule.js';

const wordContainer = document.querySelector(".word-container");
const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");
var exerciseNum = parseInt(document.getElementById("myScript").getAttribute( "data-exerciseNum" ));

const sentences = ["sheranupthehill", "wewantfreedom", "whattimeisit?", "todayisarainyday", "ican'tunderstandthis", "hetookthebus"];
// Required when calculating hits and misses
let spacesIndices = [
    [3, 6, 9, 13],
    [2, 6],
    [4, 8, 10],
    [5, 7, 8, 13],
    [1, 6, 16],
    [2, 7, 9]
];
let sentence;
const randomIndex=Math.floor(Math.random() * sentences.length);
let letters = [];
let timerCount = 25; 

function buildCharacter(text, index) {
    const character = document.createElement("div");
    character.classList.add("char");
    character.textContent = text;
    character.style.marginRight =  `3px`;

    character.addEventListener("click", () => {
        clicks++;
        separateWords(index); 
    });
    return character;
}

function separateWords(tapPosition) {
    const index = Math.round(tapPosition);
    if (index >= 0 && index <= letters.length) {
        if(spacesIndices[randomIndex].includes(index)) hits++;
        else misses++;
        console.log(`clicks: ${clicks} hits: ${hits} misses: ${misses}`);
        
        // insert white space
        letters.splice(index, 0, ' ');
        // update spaces indices with every white space
        for(let i=0; i<spacesIndices[randomIndex].length;i++){
            spacesIndices[randomIndex][i]++;
        }
        renderSentence();
    }
}

function generateExercise() {
    // Randomly select a sentence and split it into characters
    sentence = sentences[randomIndex];
    letters = sentence.split('');
    // Play sound of the selected item then start timer
    SpeechSynthesisModule.speak('Seperate the words of this sentence.');
    setTimeout(() => {
        const timerInterval = setInterval(() => {
            timerCount--;
            const progress = (25 - timerCount) / 25 * 100;
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
        }, 1000);
    renderSentence();
}

function renderSentence() {
    wordContainer.innerHTML = '';
    letters.forEach((char, index) => {
        const charElement = buildCharacter(char, index);
        wordContainer.appendChild(charElement);
    });
}

//performance metrics
let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];
generateExercise();
