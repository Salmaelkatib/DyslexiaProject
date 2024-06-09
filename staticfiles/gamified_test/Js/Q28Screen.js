import SpeechSynthesisModule from './speechSynthesisModule.js';
import sendPerformanceData from './AJAXModule.js';

const wordContainer = document.querySelector(".word-container");
const lettersContainer = document.getElementById("letters-container");
const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");
var exerciseNum = parseInt(document.getElementById("myScript").getAttribute( "data-exerciseNum" ));
let [timerOn , playedSound] = [false , false];

const words = [
    'beautiful',
    'diamond',
    'enemy',
    'computer',
    'dinosaur',
    'biography',
    'mysterious'
];
const wordSyllables = [
    'be au ti ful',
    'di a mo nd',
    'en em y',
    'com pu ter',
    'di no saur',
    'bi o graph y',
    'my ste ri ous'
];
let syllables = [];
let randomIndex , i=0;
let selectedWord;
let duration = 25;
let timerCount = duration; 

function buildContainer(text) {
    const container = document.createElement("div");
    container.classList.add("letter");
    container.textContent = text;

    container.addEventListener("click", () => {
        clicks++;
        console.log("clicked on:" ,text);
        wordContainer.textContent += text;
        container.remove();

        if(text == syllables[i]) hits++;
        else misses++;
        i++;
        console.log(`clicks: ${clicks} hits: ${hits} misses: ${misses}`);
        
        if (lettersContainer.children.length === 0) {
            wordContainer.textContent = ''; 
            const index = words.indexOf(selectedWord);
            words.splice(index, 1);
            wordSyllables.splice(index, 1);
            generateExercise();
        }
    });
    return container;
}

function generateExercise() {
    // Play sound then start timer
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
                     sendPerformanceData(exerciseNum, clicks, hits, misses, missrate, score, accuracy , window.location.href);
                     setTimeout(() => {
                         window.location.href = document.getElementById("myScript").getAttribute("data-url");
                     }, 1000);
                }
            }, 1000);
        }, 600);
        timerOn=true;
    }
    randomIndex = Math.floor(Math.random() * words.length);
    selectedWord = words[randomIndex];
    syllables = wordSyllables[randomIndex].split(' ');
    
    const shuffledSyllables = [...syllables];
    // Shuffle the syllables list
    for (let i = shuffledSyllables.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffledSyllables[i], shuffledSyllables[j]] = [shuffledSyllables[j], shuffledSyllables[i]];
    }
    lettersContainer.innerHTML = '';
    shuffledSyllables.forEach(syllable => {
        const container = buildContainer(syllable);
        lettersContainer.appendChild(container);
    });
}

//performance metrics
let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];
generateExercise();
