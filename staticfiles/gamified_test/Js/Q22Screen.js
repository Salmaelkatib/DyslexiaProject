import SpeechSynthesisModule from './speechSynthesisModule.js';
import sendPerformanceData from './AJAXModule.js';

const wordContainer = document.querySelector(".word-container");
const lettersContainer = document.getElementById("letters-container");
const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");
var exerciseNum = parseInt(document.getElementById("myScript").getAttribute( "data-exerciseNum" ));
let [timerOn , playedSound] = [false , false];

const words = [
    {'w': "_ith"},
    {'b': "_oat"},
    {'a':"r_in"},
    {'p':"_lum"},
    {'e':"hous_"},
    {'o':"br_wn"},
    {'n':"_ature"},
    {'u':"lang_age"},
    {'d':"brea_"},
    {'i':"ja_l"},
    {'q':"e_ual"},
    {'f':"_armer"},
    {'c':"fa_e"},
];
const missingLetters = ["wnmx", "daeb", "adbr", "apeq","aeui","oeau","nuea","eaui","dbqp","uigj","eaqf","epdf","aeuc"];
let randomKey,randomIndex;

let duration = 25;
let timerCount = duration; 

function buildContainer(letter) {
    const container = document.createElement("div");
    container.classList.add("letter");
    container.textContent = letter;

    container.addEventListener("click", () => {
        words.splice(randomIndex, 1);
        missingLetters.splice(randomIndex, 1);
        // calculate performance measures then generate new word
        clicks++;
        console.log(`randomKey: ${randomKey}`);
        if(letter == randomKey) hits++;
        else misses++;
        console.log(`clicks: ${clicks} hits: ${hits} misses: ${misses}`);
        generateExercise();
    });
    return container;
}

function generateExercise() {
    if(!playedSound) {SpeechSynthesisModule.speak('Choose the missing letter.'); playedSound=true;}
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
        }, 700);
        timerOn=true;
    }
    randomIndex =Math.floor(Math.random() * words.length);
    var randomMap = words[randomIndex];
    var randomWord =  Object.values(randomMap)[0];
    randomKey = Object.keys(randomMap)[0];
    var letters = missingLetters[randomIndex].split('').sort(() => Math.random() - 0.5);
    
    wordContainer.textContent = randomWord;
    lettersContainer.innerHTML = '';
    letters.forEach(letter => {
        const container = buildContainer(letter);
        lettersContainer.appendChild(container);
    });
}
//performance metrics
let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];
generateExercise();
