from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import GazeData
from django.http import JsonResponse
import numpy as np
import json
import pickle
import os
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

            features = process_gaze_info(gaze_data_array)
            print(features)

            # retrieves the Player object linked to the currently authenticated user.
            player = request.user.player
            # Get or create GazeData object for the player
            gaze_data, created = GazeData.objects.get_or_create(player=player)

            # Set features
            gaze_data.avg_fix_duration = features['Average Fixation Duration']
            gaze_data.avg_saccade_duration = features['Average Saccade Duration']
            gaze_data.total_fixations = features['Total Fixations']
            gaze_data.total_saccades = features['Total Saccades']
            gaze_data.saccades_to_fixations = features['ratio']

            # store data in model
            gaze_data.save()

            return JsonResponse({'status': 'success'}, status=200)
        except json.JSONDecodeError as e:
            print("JSON decode error:", e)
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def getPredictions(data_array):
    # Load the ML model 
    current_directory = os.path.dirname(os.path.abspath(__file__))
    model_file_path = os.path.join(current_directory, 'ml_model', 'eyeTracking_model.sav')
    scaler_file_path = os.path.join(current_directory, 'ml_model', 'scaler.sav')
    
    with open(model_file_path, "rb") as model_file:
        model = pickle.load(model_file)
    
    with open(scaler_file_path, "rb") as scaler_file:
        scaler = pickle.load(scaler_file)
    
    # Scale the input data using the loaded scaler
    scaled_data = scaler.transform([data_array])  
    prediction_prob = model.predict_proba(scaled_data)[:, 1]
    
    # Use the threshold to determine the prediction
    threshold = 0.265
    prediction = (prediction_prob > threshold).astype(int)
    
    if prediction == 0:
        return "Low-Risk"  # Not dyslexic
    elif prediction == 1:
        return "High-Risk"  # Dyslexic
    else:
        return "error"
        
# result page view
def result(request):
    # Define the order of fields for feeding into the ML model
    field_order = [
        'Gender','Avg_Fix_Duration', 'Avg_Sacc_Duration', 'Total_Fix', 'Total_Sacc','Sacc_Fix_Ratio'
    ]
 
    data_dict = {}
    # Retrieve data of the current authenticated user from the GazeData table
    player = request.user.player
    gaze_data_instance = GazeData.objects.get(player=player)
    
    # Access data of player
    gender = gaze_data_instance.player.gender
    created_at = gaze_data_instance.created_at
    data_dict['Gender'] = 1 if gender.lower() == 'male' else 0
    data_dict['Avg_Fix_Duration'] = gaze_data_instance.avg_fix_duration
    data_dict['Avg_Sacc_Duration'] = gaze_data_instance.avg_saccade_duration
    data_dict['Total_Fix'] = gaze_data_instance.total_fixations
    data_dict['Total_Sacc'] = gaze_data_instance.total_saccades
    data_dict['Sacc_Fix_Ratio'] = gaze_data_instance.saccades_to_fixations
    
    # Arrange the data according to the specified order
    input_data = [data_dict[field] for field in field_order]
    data_array = np.array(input_data, dtype=float)  

    result = getPredictions(data_array)
    
    # Save result in database
    setattr(gaze_data_instance, 'result', result)
    gaze_data_instance.save()

    return render(request, 'eyeTracking/result.html', 
                  {'result': result ,
                   'date': created_at})