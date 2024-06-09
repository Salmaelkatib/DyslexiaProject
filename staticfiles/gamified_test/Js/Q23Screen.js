import SpeechSynthesisModule from './speechSynthesisModule.js';
import sendPerformanceData from './AJAXModule.js';

const words = [
    {'some': "soame"},
    {'school': "schowol"},
    {'Awesome': "Aweasome"},
    {'good': "goaod"},
    {'icecream': "icekcream"},
    {'Happy': "Hapqpy"},
    {'box':"boax"},
    {'dessert':"desserft"},
    {'Handsome':"Handsoame"},
    {'doctor':"doctoer"},
    {'Beautiful':"Beaeutiful"},
    {'adventure':"advenbture"},
    {'train':"trayin"},
    {'computer':"comdputer"},
    {'shelves':"shelgves"},
    {'rainbow':"raeinbow"},
    {'house':"houise"},
    {'forrest':"forrrest"},
];

let randomKey,randomWord;
const wordContainer = document.querySelector(".word-container");
const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");
var exerciseNum = parseInt(document.getElementById("myScript").getAttribute( "data-exerciseNum" ));
let [timerOn , playedSound] = [false , false];

let duration = 25;
let timerCount = duration; 

function buildCharacter(text) {
    const character = document.createElement("div");
    character.classList.add("char");
    character.textContent = text;
    character.style.marginRight =  `3px`;

    character.addEventListener("click", () => {
        console.log(`Clicked letter: ${text} `);
        // Remove clicked character from the word
        randomWord = randomWord.replace(text, '');
        character.remove();
        clicks++;
        if(randomWord == randomKey) hits++;
        else misses++;
        console.log(`clicks: ${clicks} hits: ${hits} misses: ${misses}`);
        // save performance measures and generate a new word
        setTimeout(generateExercise, 300);
    });
    return character;
}
function generateExercise() {
    if(!playedSound) {SpeechSynthesisModule.speak('Choose the extra letter.'); playedSound=true;}
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
    // Randomly select a word and split it into characters
    const randomIndex = Math.floor(Math.random() * words.length);
    const randomMap = words[randomIndex];
    randomWord = Object.values(randomMap)[0];
    randomKey = Object.keys(randomMap)[0];
    var characters = randomWord.split('');
    
    wordContainer.innerHTML = '';
    characters.forEach(char => {
        const charElement = buildCharacter(char);
        wordContainer.appendChild(charElement);
    });
}
//performance metrics
let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];
generateExercise();
