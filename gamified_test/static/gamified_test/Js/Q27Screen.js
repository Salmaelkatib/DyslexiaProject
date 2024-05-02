import SpeechSynthesisModule from './speechSynthesisModule.js';
import sendPerformanceData from './AJAXModule.js';

const wordContainer = document.querySelector(".word-container");
const lettersContainer = document.getElementById("letters-container");
const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");
var exerciseNum = parseInt(document.getElementById("myScript").getAttribute( "data-exerciseNum" ));

const words = ['bird', 'potatoes', 'bread', 'vegetable', 'education', 'break'];
let selectedWord;
let pressedLetters = [];
let shuffledLetters;
let [timerOn , playedSound] = [false , false];

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

function buildContainer(text) {
    const container = document.createElement("div");
    container.classList.add("letter");
    container.textContent = text;

    container.addEventListener("click", () => {
        wordContainer.textContent += text;
        const index = pressedLetters.indexOf(text);
        pressedLetters.splice(index, 1);
        container.remove();
        clicks++;
        if (lettersContainer.children.length === 0) {
            for (let i = 0; i < wordContainer.textContent.length; i++) {
                // Compare each letter with the corresponding letter in the selected word
                if (wordContainer.textContent[i] === selectedWord[i]) {
                    hits++;
                } else {
                    misses++;
                }
            }
                console.log(`clicks: ${clicks} hits: ${hits} misses: ${misses}`);
                wordContainer.textContent = ''; 
                const index = words.indexOf(selectedWord);
                words.splice(index, 1);
                generateExercise();
            }
    });

    return container;
}

function generateExercise() {
    // play sound then start timer
    if(!playedSound) {SpeechSynthesisModule.speak('Rearrange to form a word.'); playedSound=true;}
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
                    window.location.href = document.getElementById("myScript").getAttribute("data-url");
                }
            }, 1000);
        }, 600);
        timerOn=true;
    }
    selectedWord = words[Math.floor(Math.random() * words.length)];
    shuffledLetters = selectedWord.split('').sort(() => Math.random() - 0.5);
    lettersContainer.innerHTML = '';
    shuffledLetters.forEach(letter => {
        const container = buildContainer(letter);
        lettersContainer.appendChild(container);
    });
}

//performance metrics
let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];
generateExercise();
