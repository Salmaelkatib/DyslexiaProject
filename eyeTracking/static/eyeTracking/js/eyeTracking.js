import EasySeeSo from './easy-seeso.js';
import showGaze from './showGaze.js';
import sendGazeData from './AJAXModule.js';

const licenseKey = 'dev_1t9m51mlw9xbhu3jycg8nxl1qi051qxtwaudhzww';
export let seeSoInstance;
export let gazeDataArray = [];

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
    const milliseconds = date.getUTCMilliseconds().toString().padStart(3, '0');
    timestamp = parseInt(milliseconds);
    
    // Append gaze info to the array
    gazeDataArray.push({
        timestamp: timestamp,
        x: gazeInfo.x,
        y: gazeInfo.y,
        state: gazeInfo.eyemovementState
    });

    // To show gaze dot on screen
    showGaze(gazeInfo);
}

async function main() {
    const calibrationData = parseCalibrationDataInQueryString();

    if (calibrationData) {
        seeSoInstance = new EasySeeSo();
        await seeSoInstance.init(licenseKey,
            async () => {
                // Disable the calibration button
                document.getElementById('calibrationButton').disabled = true;
                await seeSoInstance.setCalibrationData(calibrationData);
                await seeSoInstance.startTracking(onGaze);
                console.log('Eye tracking started.');
            }, // Callback when init succeeded.
            () => console.log("callback when init failed.") // Callback when init failed.
        );
    } else {
        console.log('No calibration data given.');
        const calibrationButton = document.getElementById('calibrationButton');
        calibrationButton.addEventListener('click',onClickCalibrationBtn);
    }
}

(async () => {
    await main();
    // set listener for stopTracking button
    const iframe = document.getElementById('embeddedPage');
    const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
    const stopTrackingButton = iframeDocument.getElementById('stopTrackingButton');
    stopTrackingButton.addEventListener('click', async () => {
        seeSoInstance.stopTracking();
        // send the gazeDataArray 
        sendGazeData(gazeDataArray , window.location.href);
        });
  })()
