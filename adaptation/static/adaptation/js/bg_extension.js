import { eyeTracking } from "./eyeTracking"

let setting = []

document.addEventListener("DOMContentLoaded", function() {
    eyeTracking(document.getElementById("myScript").getAttribute("data-url"),1);
    // compare AFD 
    const AFD =document.getElementById("myScript").getAttribute("AFD");
    


});






