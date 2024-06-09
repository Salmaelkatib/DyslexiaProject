import EasySeeSo from './easy-seeso.js';

const licenseKey = 'dev_1t9m51mlw9xbhu3jycg8nxl1qi051qxtwaudhzww';

 // in redirected page
 function parseCalibrationDataInQueryString () {
    const href = window.location.href
    const decodedURI = decodeURI(href)
    const queryString = decodedURI.split('?')[1];

    if (!queryString) return undefined
    const jsonString = queryString.slice("calibrationData=".length, queryString.length)
    return jsonString
  }
  function onClickCalibrationBtn(){
    const userId = 'YOUR_USER_ID'; 
    const redirectUrl = document.getElementById("myScript").getAttribute("data-url");
    const calibrationPoint = 5;
    EasySeeSo.openCalibrationPage(licenseKey, userId, redirectUrl, calibrationPoint);
}
// gaze callback.
function onGaze(gazeInfo) {
    // do something with gaze info.
    console.log(`Timestamp: ${gazeInfo.timestamp}`);
    console.log(`Gaze position (x, y): (${gazeInfo.x}, ${gazeInfo.y})`);
    console.log(`Fixation position (x, y): (${gazeInfo.fixationX}, ${gazeInfo.fixationY})`);
    console.log(`Eye movement state: ${gazeInfo.eyemovementState}`);
 
    showGaze(gazeInfo);
}

  async function main() {
 
    const calibrationData = parseCalibrationDataInQueryString()
 
    if (calibrationData){
        const seeSo = new EasySeeSo();
        await seeSo.init(licenseKey,
            async () => {    
                await seeSo.startTracking(onGaze)              
                await seeSo.setCalibrationData(calibrationData)
                console.log("Finished Calibration")
            }, // callback when init succeeded.
            () => console.log("callback when init failed.") // callback when init failed.
        )
    } else {
        console.log('No calibration data given.')
        const calibrationButton = document.getElementById('calibrationButton')
        calibrationButton.addEventListener('click', onClickCalibrationBtn)
    }
}
 
(async () => {
  await main();
})()

