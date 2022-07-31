const startBtn = document.querySelector("#start-btn");

const recognition = new webkitSpeechRecognition();
recognition.continuous = true;
recognition.lang = "en-US";
recognition.interimResults = false;
recognition.maxAlternatives = 1;

const synth = window.speechSynthesis;

startBtn.addEventListener("click", () => {
    recognition.start();
});


let utter = new SpeechSynthesisUtterance("Hi, how are you?");

recognition.onresult = (e) => {
    const transcript = e.results[e.results.length - 1][0].transcript.trim();
    console.log(transcript);
    if (transcript == "how do I know if I have received a scam email or phone call"){
        recognition.stop();
        utter = new SpeechSynthesisUtterance("You may receive an unsolicited phone call (from someone claiming to be from the Bank) requesting personal or financial information, or to participate in a bank survey. You may receive an e-mail advising that you have won or inherited a large amount of money (usually from overseas) and that you need to pay a fee to release the money from the Bank.");
        synth.speak(utter);
    }
    
    else if (transcript == "what should I do if I got scammed"){
        recognition.stop();
        utter = new SpeechSynthesisUtterance("Immediately stop contacting the scammer and report it.");
        synth.speak(utter);        
    }
    
    else if (transcript == "can I get my money back after I have been scammed"){
        recognition.stop();
        utter = new SpeechSynthesisUtterance("Unfortunately, it is very difficult to do as scammers are difficult to track. The best thing you can do is avoid providing information to scammers in the future.");
        synth.speak(utter);        
    }
    
    else if (transcript == "how can I prevent being scammed in the future"){
        recognition.stop();
        utter = new SpeechSynthesisUtterance("You should avoid providing information to scammers, or ignore them completely. If you are unsure whether a message is a scam or not, you can use our scam detector tool.");
        synth.speak(utter);        
    }
    
    else{
        recognition.stop();
        utter = new SpeechSynthesisUtterance("I don't know. Try google.");
        synth.speak(utter);        
    }
};