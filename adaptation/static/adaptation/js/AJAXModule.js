// AJAX request to send gaze data to Django view
export default function sendGazeData(gazeDataArray, currentUrl) {
    // Parse the URL and remove the calibrationData query parameter
    const urlParts = currentUrl.split('?');
    const baseUrl = urlParts[0];
    const data = JSON.stringify({ 
        gazeData: gazeDataArray,
        currentUrl:currentUrl,
    });
    $.ajax({
        type: "POST",
        url: `${baseUrl}save_gaze_data/`,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: data,
        success: function(response) {
            console.log("Gaze data sent successfully.");
        },
        error: function(xhr, status, error) {
            console.error("Error sending gaze data:", error);
        }
    });
}
