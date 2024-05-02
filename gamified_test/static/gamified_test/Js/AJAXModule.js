// AJAX request to send performance data to Django view
export default function sendPerformanceData(exerciseNum, clicks, hits, misses, missrate, score, accuracy , currentUrl) {
   // Construct the django view Url for save_performance_data using the exerciseNum parameter
   var urlParts = currentUrl.split('/');
    urlParts.splice(-2); 
    var url = urlParts.join('/');

    $.ajax({
        type: "POST",
        url: `${url}/save_performance_data/${exerciseNum}/`,
        data: {
            clicks: clicks,
            hits: hits,
            misses: misses,
            missrate: missrate,
            score: score,
            accuracy: accuracy
        },
        success: function(response) {
            console.log("Performance data sent successfully.");
        },
        error: function(xhr, status, error) {
            console.error("Error sending performance data:", error);
        }
    });
}

