const wordContainer = document.querySelector(".word-container");
const lettersContainer = document.getElementById("letters-container");
const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");

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
    'ti be au ful',
    'di mond a',
    'en em y',
    'com ter pu',
    'di sa ur no',
    'bi gra o y ph',
    'ste my ous ri'
];

let picked = [];
let syllables = [];
let randomIndex;
let selectedWord;
let duration = 25;
let timerCount = duration; 

const timerInterval = setInterval(() => {
    timerCount--;
    const progress = (duration - timerCount) / duration * 100;
    progressBar.style.width = `${100 - progress}%`;
    timer.textContent = timerCount;

    if (timerCount <= 0) {
        clearInterval(timerInterval); 
        // save data and navigate to next question
        window.location.href = document.getElementById("myScript").getAttribute("data-url");
    }
}, 1000);

function buildContainer(text) {
    const container = document.createElement("div");
    container.classList.add("letter");
    container.textContent = text;

    container.addEventListener("click", () => {
        console.log("clicked on:" ,text);
        wordContainer.textContent += text;
        container.remove();
        
        if (lettersContainer.children.length === 0) {
            wordContainer.textContent = ''; 
            const index = words.indexOf(selectedWord);
            words.splice(index, 1);
            wordSyllables.splice(index, 1);
            generateWordAndSyllables();
        }
    });
    return container;
}

function generateWordAndSyllables() {
    randomIndex = Math.floor(Math.random() * words.length);
    selectedWord = words[randomIndex];
    syllables = wordSyllables[randomIndex].split(' ');
    
    // Shuffle syllables list 
    for (let i = syllables.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [syllables[i], syllables[j]] = [syllables[j], syllables[i]];
    }

    lettersContainer.innerHTML = '';
    syllables.forEach(syllable => {
        const container = buildContainer(syllable);
        lettersContainer.appendChild(container);
    });
}

generateWordAndSyllables();
