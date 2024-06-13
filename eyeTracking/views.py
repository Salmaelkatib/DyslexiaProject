from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import GazeData
from django.http import JsonResponse
import json
from .data_algorithms.ivt_algorithm import process_gaze_info

def eyeTracking(request):
    return render(request , 'eyeTracking/eyeTracking.html')
def stopTracking(request):
    return render(request , 'eyeTracking/stopTracking.html')
@csrf_exempt  # Disable CSRF protection for this view (for simplicity)
def save_gaze_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            gaze_data_array = data.get('gazeData', [])
            ppi = data.get('ppi', 0)

            features = process_gaze_info(gaze_data_array , ppi)
            print(features)
            # Save each gaze data entry to the database
            for gaze_data in gaze_data_array:
                GazeData.objects.create(
                    timestamp=gaze_data['timestamp'],
                    x=gaze_data['x'],
                    y=gaze_data['y'],
                    state=gaze_data['state']
                )
            return JsonResponse({'status': 'success'}, status=200)
        except json.JSONDecodeError as e:
            print("JSON decode error:", e)
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)