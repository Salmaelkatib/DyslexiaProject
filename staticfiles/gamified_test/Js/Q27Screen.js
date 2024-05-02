const wordContainer = document.querySelector(".word-container");
const lettersContainer = document.getElementById("letters-container");
const progressBar = document.getElementById("progress-bar");
const timer = document.querySelector("#progress-bar p");

const words = ['bird', 'potatoes', 'bread', 'vegetable', 'education', 'break'];
let selectedWord;
let pressedLetters = [];
let shuffledLetters;

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
        window.location.href = document.getElementById("myScript").getAttribute( "data-url" );
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
        
        if (lettersContainer.children.length === 0) {
                wordContainer.textContent = ''; 
                const index = words.indexOf(selectedWord);
                words.splice(index, 1);
                generateWordAndLetters();
            }
    });

    return container;
}

function generateWordAndLetters() {
    selectedWord = words[Math.floor(Math.random() * words.length)];
    shuffledLetters = selectedWord.split('').sort(() => Math.random() - 0.5);
    lettersContainer.innerHTML = '';
    shuffledLetters.forEach(letter => {
        const container = buildContainer(letter);
        lettersContainer.appendChild(container);
    });
}
generateWordAndLetters();
