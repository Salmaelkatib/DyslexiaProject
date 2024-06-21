from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import adaptation_GazeData
import json
from urllib.parse import urlparse
from eyeTracking.data_algorithms.ivt_algorithm import process_gaze_info

colors={
    '#ffffff':'White',
    '#edd1b0':'Peach',
    '#eddd6e':'Orange',
    '#f8fd89':'Yellow',
    '#fffdd0':'Cream',
}

feature_files = {
    #background color files
    'bg_base':'#ffffff',
    'bg_extension1': '#edd1b0',
    'bg_extension2': '#eddd6e',
    'bg_extension3': '#f8fd89',
    'bg_extension4': '#fffdd0',

    #font type files
    'font_type_base':'Arial',
    'font_type_extension1': 'OpenDyslexic',
    'font_type_extension2': 'CMU',
    'font_type_extension3': 'Courier',
    'font_type_extension4': 'Verdana',
    'font_type_extension5': 'Helvetica',
    'font_type_extension6': 'Times',
    'font_type_extension7': 'Comic',

    #character spacing files
    'char_spacing_base': '0.1em',
    'char_spacing_extension1': '0.04em',
    'char_spacing_extension2': '0.17em',

    #text color files
    'text_color_base':'Black',
    'text_color_extension': 'Blue',
}

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

def adaptation_result(request):
    # Assuming you want to retrieve the data for the currently logged-in user
    user = request.user
    try:
        variations = adaptation_GazeData.objects.get(user=user)
        result = {
            'min_bg_color': colors[variations.min_bg_color],
            'min_font_type': variations.min_font_type,
            'min_font_color': variations.min_font_color,
            'min_char_spacing': variations.min_char_spacing,
        }
    except adaptation_GazeData.DoesNotExist:
        result = {
            'min_bg_color': 'N/A',
            'min_font_type': 'N/A',
            'min_font_color': 'N/A',
            'min_char_spacing': 'N/A',
        }
    context = {
        'result': result,
    }
    return render(request, 'adaptation/adaptation_result.html', context)

@csrf_exempt  # Disable CSRF protection for this view (for simplicity)
def save_gaze_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            gaze_data_array = data.get('gazeData', [])
            features = process_gaze_info(gaze_data_array)
            AFD = features['Average Fixation Duration']
            user = request.user
 
            # Get or create GazeData object for the player
            gaze_data, created = adaptation_GazeData.objects.get_or_create(user=user)
 
            # Determine the setting variation from the URL
            current_url=data.get('currentUrl','')
            # Split the URL by '/' and get the last segment
            segments = current_url.split('/')
            variation = segments[-2]  # Get the second last segment
            print('Variation:', variation)
            
           
            if variation == 'adaptation':
                # Base page
                gaze_data.base_afd = AFD
                gaze_data.min_bg_color=feature_files['bg_base']
                gaze_data.min_bg_color_afd = AFD
                gaze_data.min_font_type =feature_files['font_type_base']
                gaze_data.min_font_type_afd = AFD
                gaze_data.min_font_color = feature_files['text_color_base']
                gaze_data.min_font_color_afd = AFD
                gaze_data.min_char_spacing = feature_files['char_spacing_base']
                gaze_data.min_char_spacing_afd = AFD
                print('Base AFD:',AFD)

            elif 'bg_extension' in variation:
                print('before check Bg Filename:',variation)
                print('before check Bg AFD:',AFD)
                if gaze_data.min_bg_color_afd is None or AFD < gaze_data.min_bg_color_afd:
                    gaze_data.min_bg_color = feature_files[variation]
                    gaze_data.min_bg_color_afd = AFD
                    print('Bg Filename:',variation)
                    print('Bg AFD:',AFD)
            elif 'font_type_extension' in variation:
                if gaze_data.min_font_type_afd is None or AFD < gaze_data.min_font_type_afd:
                    gaze_data.min_font_type = feature_files[variation]
                    gaze_data.min_font_type_afd = AFD
                    print('Font type Filename:',variation)
                    print('Font type AFD:',AFD)
            elif 'text_color_extension' in variation:
                if gaze_data.min_font_color_afd is None or AFD < gaze_data.min_font_color_afd:
                    gaze_data.min_font_color = feature_files[variation]
                    gaze_data.min_font_color_afd = AFD
                    print('Text color Filename:',variation)
                    print('Text color AFD:',AFD)
            elif 'char_spacing_extension' in variation:
                if gaze_data.min_char_spacing_afd is None or AFD < gaze_data.min_char_spacing_afd:
                    gaze_data.min_char_spacing = feature_files[variation]
                    gaze_data.min_char_spacing_afd = AFD
                    print('Character Spacing Filename:',variation)
                    print('Character Spacing AFD:',AFD)
 
            # Calculate overall gain
            gaze_data.overall_gain = gaze_data.calculate_overall_gain()
            print('Gain:',gaze_data.overall_gain)

            # Save the updated gaze data
            gaze_data.save()
 
            return JsonResponse({'status': 'success', 'avg_fix_duration': AFD}, status=200)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


    