from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import adaptation_GazeData
import json
from eyeTracking.data_algorithms.ivt_algorithm import process_gaze_info

# Create your views here.
def base(request):
    return render(request , 'adaptation/base.html')
def bg_extension1(request):
    AFD = adaptation_GazeData.objects.get(extention_no=1)
    return render(request , 'adaptation/bg_extension1.html',{'AFD': AFD})
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
            extention_no = data.get('extention_no', 0)

            features = process_gaze_info(gaze_data_array)
            print(features)
            # retrieves the Player object linked to the currently authenticated user.
            player = request.user.player
            # Get or create GazeData object for the player
            gaze_data, created = adaptation_GazeData.objects.get_or_create(player=player)

            # Set AFD
            gaze_data.avg_fix_duration = features['Average Fixation Duration']
            gaze_data.extention_no = extention_no

            # store data in model
            gaze_data.save()
            return JsonResponse({'status': 'success'}, status=200)
        except json.JSONDecodeError as e:
            print("JSON decode error:", e)
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


    