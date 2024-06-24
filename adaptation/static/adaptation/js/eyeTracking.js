import EasySeeSo from './easy-seeso.js';
import showGaze from './showGaze.js';
import sendGazeData from './AJAXModule.js';

const licenseKey = 'dev_1t9m51mlw9xbhu3jycg8nxl1qi051qxtwaudhzww';
let seeSoInstance;
let gazeDataArray = [];

// In redirected page
function parseCalibrationDataInQueryString() {
    const href = window.location.href;
    const decodedURI = decodeURI(href);
    const queryString = decodedURI.split('?')[1];

    if (!queryString) return undefined;
    const jsonString = queryString.slice("calibrationData=".length, queryString.length);
    return jsonString;
}

// Open calibration once the page loads
function onClickCalibrationBtn() {
    const userId = 'YOUR_USER_ID'; 
    const redirectUrl = window.location.href;
    const calibrationPoint = 5;
    EasySeeSo.openCalibrationPage(licenseKey, userId, redirectUrl, calibrationPoint);
}

// Gaze callback
function onGaze(gazeInfo) {
    // Adjust timestamp to UTC format
    let timestamp = gazeInfo.timestamp;
    const date = new Date(timestamp);
    const minutes = date.getUTCMinutes();
    const seconds = date.getUTCSeconds();
    const milliseconds = date.getUTCMilliseconds().toString().padStart(3, '0');
    const totalSeconds = minutes * 60 + seconds;
    timestamp = parseFloat(`${totalSeconds}.${milliseconds}`);
    
    // Append gaze info to the array
    gazeDataArray.push({
        timestamp: gazeInfo.timestamp,  //in ms
        x: (gazeInfo.x),
        y: (gazeInfo.y),
        state: gazeInfo.eyemovementState
    });

    // To show gaze dot on screen
    showGaze(gazeInfo);
}
async function main() {
    // Check if calibration data is stored in localStorage
    let calibrationData = localStorage.getItem('calibrationData');
 
    if (!calibrationData) {
        // If not in localStorage, try to get it from the query string
        calibrationData = parseCalibrationDataInQueryString();
 
        if (calibrationData) {
            // Store calibration data in localStorage
            localStorage.setItem('calibrationData', calibrationData);
        }
    }
    if (calibrationData) {
        seeSoInstance = new EasySeeSo();
        await seeSoInstance.init(licenseKey,
            async () => {
                await seeSoInstance.setCalibrationData(calibrationData);
                await seeSoInstance.startTracking(onGaze);
                await seeSoInstance.setTrackingFps(100);
                console.log('Eye tracking started.');
            }, // Callback when init succeeded.
            () => console.log("callback when init failed.") // Callback when init failed.
        );
    }  else {
        console.log('No calibration data given.');
        const calibrationButton = document.getElementById('calibrationButton');
        calibrationButton.addEventListener('click', onClickCalibrationBtn);  
    }
}
export async function eyeTracking(url){
    await main();
    // set listener for stopTracking button
    const iframe = document.getElementById('embeddedPage');
    const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
    const stopTrackingButton = iframeDocument.getElementById('stopTrackingButton');
    stopTrackingButton.addEventListener('click', async () => {
        seeSoInstance.stopTracking();
        // send the gazeDataArray 
        console.log(gazeDataArray);
        sendGazeData(gazeDataArray , window.location.href);
        // to navigate to next screen
        window.location.href = url;
        });
}

(async () => {
    eyeTracking(document.getElementById("myScript").getAttribute("data-url")); 
    const calibrationButton = document.getElementById('calibrationButton');
    calibrationButton.addEventListener('click', onClickCalibrationBtn);
})()
