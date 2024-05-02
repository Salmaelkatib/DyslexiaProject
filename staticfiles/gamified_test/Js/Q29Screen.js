const wordContainer = document.querySelector(".word-container");
const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");

const sentences = ["sheranupthehill", "wewantfreedom", "whattimeisit?", "todayisarainyday", "ican'tunderstandthis", "hetookthebus"];
// Required when calculating hits and misses
const spacesIndices = [
    [3, 6, 9, 13],
    [2, 6],
    [4, 8, 10],
    [5, 7, 8, 13],
    [1, 6, 16],
    [2, 7, 9]
];
let sentence;
let letters = [];
let timerCount = 25; 

const timerInterval = setInterval(() => {
    timerCount--;
    const progress = (25 - timerCount) / 25 * 100;
    progressBar.style.width = `${100 - progress}%`;
    timer.textContent = timerCount;

    if (timerCount <= 0) {
        clearInterval(timerInterval); 
        // Save data and navigate to the next question
        window.location.href = document.getElementById("myScript").getAttribute("data-url");
    }
}, 1000);

function buildCharacter(text, index) {
    const character = document.createElement("div");
    character.classList.add("char");
    character.textContent = text;
    character.style.marginRight =  `3px`;

    character.addEventListener("click", () => {
        separateWords(index); 
    });
    return character;
}

function separateWords(tapPosition) {
    const index = Math.round(tapPosition);
    if (index >= 0 && index <= letters.length) {
        letters.splice(index, 0, ' ');
        renderSentence();
    }
}

function generateRandomSentence() {
    // Randomly select a sentence and split it into characters
    sentence = sentences[Math.floor(Math.random() * sentences.length)];
    letters = sentence.split('');
    renderSentence();
}

function renderSentence() {
    wordContainer.innerHTML = '';
    letters.forEach((char, index) => {
        const charElement = buildCharacter(char, index);
        wordContainer.appendChild(charElement);
    });
}

generateRandomSentence();
