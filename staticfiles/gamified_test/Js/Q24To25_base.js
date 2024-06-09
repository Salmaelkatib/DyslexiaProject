import SpeechSynthesisModule from './speechSynthesisModule.js';
import sendPerformanceData from './AJAXModule.js';

document.addEventListener("DOMContentLoaded", function() {
    const wordContainer = document.getElementById("word-container");
    const progressBar = document.getElementById("progress-bar");
    const timer = document.querySelector("#progress-bar p");
    var exerciseNum = parseInt(document.getElementById("myScript").getAttribute( "data-exerciseNum" ));
    let [timerOn , playedSound] = [false , false];

    // Parse the list from JSON attribute
    const list = JSON.parse(document.getElementById("myScript").getAttribute("data-list"));
    const selectedKey = document.getElementById("myScript").getAttribute("data-key");
    //performance metrics
    let [clicks, hits, misses, missrate,score, accuracy] = [0, 0, 0, 0,0, 0];

    let duration = 25;
    let timerCount = duration;

    if(!playedSound) {SpeechSynthesisModule.speak('Choose the wrong word.'); playedSound=true;}
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

    function buildContainer(list) {
        list.forEach(word => {
            const wordElement = document.createElement("div");
            wordElement.classList.add("word");
            wordElement.textContent = word;
            wordElement.style.marginRight = `5px`;
            wordContainer.appendChild(wordElement); 

            wordElement.addEventListener("click", () => {
                wordElement.style.color = `#00aaff`; 
                console.log(`selectedkey: ${selectedKey}`);
                //calculate performance metrics
                clicks++;
                if(wordElement.textContent == selectedKey) hits++;
                else misses++;
                console.log(`clicks: ${clicks} hits: ${hits} misses: ${misses}`);
                // save performance measures and navigate to next question
                sendPerformanceData(exerciseNum, clicks, hits, misses, missrate, score, accuracy , window.location.href);
                setTimeout(() => {
                    window.location.href = document.getElementById("myScript").getAttribute("data-url");
                }, 1000);
            });
        });
    }

    buildContainer(list);
});
