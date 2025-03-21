import SpeechSynthesisModule from './speechSynthesisModule.js';
import sendPerformanceData from './AJAXModule.js';

const wordContainer = document.getElementById("word-container");
const lettersContainer = document.getElementById("letters-container");
const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");
var exerciseNum = parseInt(document.getElementById("myScript").getAttribute( "data-exerciseNum" ));
let [timerOn , playedSound] = [false , false];

const listOfWords = [
    {'b': "webnesday"},
    {'e': "fridey"},
    {'w': "nuwber"},
    {'i': "iacket"},
    {'n': "npset"},
    {'e': "Triel"},
    {'E':"Elash"},
    {'e':"goel"},
    {'q':"aqventure"},
    {'p':"ropot"},
    {'l':"queslion"},
    {'e':"woed"},
    {'b':"elebhant"},
    {'a':"coconat"},
    {'a':"schaol"},
    {'t':"airoptane"},
    {'j':"wjndow"},
    {'m':"rainbom"},
    {'u':"chupter"},
    {'e':"tewn"},
    {'q':"qanda"},
];

const correctLetters = ["d", "a", "m", "j", "u", "a", "F", "a", "d", "b", "t", "o", "p", "u", "o", "l", "i", "w", "a", "o", "p"];

const possibleCorrectLetters = [
    "dbay", "daqp", "xmnu", "jegp","uaeo","uaeo","FTLI","aouh"
,"dbay","dbat","ftil","uaio","dbpq","nuho","uaio","tfli","uaio","unmw","uaio","gauo","dbpq"
];

let duration = 25;
let timerCount = duration; // Initial timer count in seconds 

function generateExercise() {
    // play sound then start timer
    if(!playedSound) {SpeechSynthesisModule.speak('Correct the wrong letter.'); playedSound=true;}
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
    const randomIndex = Math.floor(Math.random() * listOfWords.length);
    const wordObj = listOfWords[randomIndex];
    const wrongLetter = Object.keys(wordObj)[0];
    const word = wordObj[wrongLetter];

    // Generate list of letters including correct and distractors
    const lettersList = possibleCorrectLetters[randomIndex].split('');
    
    // Display word with wrong letter colored in blue
    let formattedWord = '';
    for (let i = 0; i < word.length; i++) {
        if (word[i] === wrongLetter) {
            formattedWord += `<span style="color: #00aaff;">${wrongLetter}</span>`;
        } else {
            formattedWord += word[i];
        }
    }
    wordContainer.innerHTML = formattedWord;

    lettersContainer.innerHTML = '';
    for (let i = 0; i < lettersList.length; i++) {
        const letterElement = document.createElement("div");
        letterElement.classList.add("letter");
        letterElement.textContent = lettersList[i];
        lettersContainer.appendChild(letterElement);

        // Attach click event listener after creating the letter element
        letterElement.addEventListener("click", () => {
            // Handle click event (e.g., update statistics, reload question)
            const pickedLetter = letterElement.textContent;
            const correctLetter = correctLetters[randomIndex];
            const isCorrect = pickedLetter === correctLetter;

            listOfWords.splice(randomIndex, 1);
            possibleCorrectLetters.splice(randomIndex, 1);
            correctLetters.splice(randomIndex, 1);

            // Reload question with new random letter
            generateExercise();

        //calculate performance metrics based on the clicked letter
        clicks++;
        if(isCorrect) hits++;
        else misses++;
});
}
}

//performance metrics
let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];
// Call the function to generate word and letters
generateExercise();

