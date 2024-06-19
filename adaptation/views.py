from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from eyeTracking.data_algorithms.ivt_algorithm import process_gaze_info

# Create your views here.
def base(request):
    return render(request , 'adaptation/base.html')
def bg_extension1(request):
    return render(request , 'adaptation/bg_extension1.html')
def bg_extension2(request):
    return render(request , 'adaptation/bg_extension2.html')
def bg_extension3(request):
    return render(request , 'adaptation/bg_extension3.html')
def bg_extension4(request):
    return render(request , 'adaptation/bg_extension4.html')

def font_type_extension1(request):
    return render(request , 'adaptation/font_type_extension1.html')
def font_type_extension2(request):
    return render(request , 'adaptation/font_type_extension2.html')
def font_type_extension3(request):
    return render(request , 'adaptation/font_type_extension3.html')
def font_type_extension4(request):
    return render(request , 'adaptation/font_type_extension4.html')
def font_type_extension5(request):
    return render(request , 'adaptation/font_type_extension5.html')
def font_type_extension6(request):
    return render(request , 'adaptation/font_type_extension6.html')
def font_type_extension7(request):
    return render(request , 'adaptation/font_type_extension7.html')

def text_color_extension(request):
    return render(request , 'adaptation/text_color_extension.html')

def char_spacing_extension1(request):
    return render(request , 'adaptation/char_spacing_extension1.html')
def char_spacing_extension2(request):
    return render(request , 'adaptation/char_spacing_extension2.html')

def stopTracking(request):
    return render(request , 'adaptation/stopTracking.html')
@csrf_exempt  # Disable CSRF protection for this view (for simplicity)
def save_gaze_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            gaze_data_array = data.get('gazeData', [])
            features = process_gaze_info(gaze_data_array)
            print(features)
            # Save each gaze data entry to the database
            # for gaze_data in gaze_data_array:
            #     GazeData.objects.create(
            #         timestamp=gaze_data['timestamp'],
            #         x=gaze_data['x'],
            #         y=gaze_data['y'],
            #         state=gaze_data['state']
            #     )
            return JsonResponse({'status': 'success'}, status=200)
        except json.JSONDecodeError as e:
            print("JSON decode error:", e)
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)