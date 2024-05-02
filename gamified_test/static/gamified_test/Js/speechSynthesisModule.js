const SpeechSynthesisModule = {
  speak(text) {
    var timer = setInterval(function() {
    var voices = speechSynthesis.getVoices();
    console.log(voices);
    if (voices.length !== 0) {
        var msg = new SpeechSynthesisUtterance(text);
        msg.voice = voices[2];
        msg.rate = 0.7;
        speechSynthesis.speak(msg);
        msg.lang = 'en-US';
        clearInterval(timer);
        }
    }, 200);
},
  stop() {
    speechSynthesis.cancel();
  }
};

export default SpeechSynthesisModule;
