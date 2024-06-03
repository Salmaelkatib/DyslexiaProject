from django.shortcuts import render
import json
import random
from django.http import JsonResponse
from .models import GameData
import numpy as np
import pickle
import os
from django.views.decorators.csrf import csrf_exempt

def signin(request):
    return render(request , 'signin.html')
def register(request):
    return render(request , 'register.html')
def q1Screen(request):
    return render(request , 'gamified_test/q1Screen.html')
def q2Screen(request):
    return render(request , 'gamified_test/q2Screen.html')
def q3Screen(request):
    return render(request , 'gamified_test/q3Screen.html')
def q4Screen(request):
    return render(request , 'gamified_test/q4Screen.html')
def q5Screen(request):
    list = [['ne','no','de','na','pu','qu','be','qe','da','pa','ba','pe','da']]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q5Screen.html',{'my_list': my_list})
def q6Screen(request):
    list = [['ne','no','de','na','pu','qu','be','qe','da','pa','ba','pe','da']]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q6Screen.html',{'my_list': my_list})
def q7Screen(request):
    list =  [['pra','par','gar','qar','are','gra','dar','qar','der','ger','gre','bar']]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q7Screen.html',{'my_list': my_list})
def q8Screen(request):
    list = [['pra','par','gar','qar','are','gra','dar','qar','der','ger','gre','bar']]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q8Screen.html',{'my_list': my_list})
def q9Screen(request):
    list = [['grel','glis','glil','gris','gerl']]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q9Screen.html',{'my_list': my_list})
def q10Screen(request):
    list = [
    [
    "create" , "great" , "gate" ,
    "greet" , "crate" , "great" ,
    "greet" , "grade" , "crate"
    ],
    [ "date" , "late" , "deer" ,
      "dear" , "gate" , "ate" ,
      "late" , "door" , "grade"
    ]]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q10Screen.html',{'my_list': my_list})
def q11Screen(request):
    list = [
    ["meet" , "greet" , "great" ,"sweet"
    "seat" , "meet" , "mate" , "neat",
    "sweet" , "grade" , "crate" , "greet",
    "greet" , "neat" , "seat" , "grade",
    ],
    ["blue" , "true" , "you" ,"view",
    "crew" , "you" , "glue" , "shoe",
    "glue" , "clue" , "crew" , "true",
    "true" , "blue" , "knew" , "glue"
    ]
  ]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q11Screen.html',{'my_list': my_list})
def q12Screen(request):
    list = [
    ["shade" , "sheet" , "seed" ,"clean" , "neat",
      "read" , "red" , "cheat" , "chase",  "meat",
      "neat" , "chase" , "chase" , "dress" , "shade",
      "red" , "check" , "read" , "chase" , "net",
      "neat" , "shade" , "red" , "cheat" , "shade"
    ],
    ["coat" , "cough" , "dough" ,"boat" , "gloat",
      "shoot" , "note" , "caught" , "chose",  "loose",
      "mose" , "rough" , "rogue" , "note" , "suit",
      "boot" , "road" , "taught" , "chose" , "nose",
      "note" , "cough" , "mose" , "rough" , "tough"
    ],
  ]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q12Screen.html',{'my_list': my_list})
def q13Screen(request):
    list = [["fly" , "dye" , "tie" ,"fight" , "flight" , "night",
      "rye" , "shy" , "cheat" , "chase",  "meat" ,"red",
      "yield" , "shed" , "sat" , "dress" , "dish","shred",
      "red" , "men" , "read" , "need" , "net", "note",
      "neat" , "meat" , "yield" , "deal" , "read" ,"shed",
      "night" , "dye" , "diet" , "deal" , "tight" , "shy"
    ]]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q13Screen.html',{'my_list': my_list})
def q14Screen(request):
    return render(request , 'gamified_test/q14Screen.html')
def q15Screen(request):
    return render(request , 'gamified_test/q15Screen.html')
def q16Screen(request):
    return render(request , 'gamified_test/q16Screen.html')
def q17Screen(request):
    return render(request , 'gamified_test/q17Screen.html')
def q18Screen(request):
    list = [['matapa','madata','mapaba','damata','pamama','mamata'],
    ['bapama','dapama','madapa','tapama']]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q18Screen.html',{'my_list': my_list})
def q19Screen(request):
    list = [['matapa','madata','mapaba','damata','pamama','mamata'],
    ['bapama','dapama','madapa','tapama']]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q19Screen.html',{'my_list': my_list})
def q20Screen(request):
    list = [['dabaqa','badaqa','dadapa','pabapa',
      'dadapa','dabapa','babada','dabada','pabapa','babapa'] ]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q20Screen.html',{'my_list': my_list})
def q21Screen(request):
    list = [['dabaqa','badaqa','dadapa','pabapa',
      'dadapa','dabapa','babada','dabada','pabapa','babapa'] ]
    selected_list = random.choice(list)
    my_list = json.dumps(selected_list)
    return render(request , 'gamified_test/q21Screen.html',{'my_list': my_list})
def q22Screen(request):
    return render(request , 'gamified_test/q22Screen.html')
def q23Screen(request):
    return render(request , 'gamified_test/q23Screen.html')
def q24Screen(request):
    my_dict = {
        "affect": ['The', 'affect', 'of', 'the', 'wind', 'was', 'to', 'cause', 'the', 'boat’s', 'sail', 'to', 'billow.'],
        "meet": ['The', 'restaurant', 'offers', 'a', 'delicious', 'meet', 'dish', 'for', 'dinner.'],
        "then": ['There', 'are', 'less', 'girls', 'in', 'our', 'class', 'then', 'boys.'],
        "net": ['You', 'must', 'get', 'your', 'neat', 'for', 'fishing.'],
    }
    selected_key = random.choice(list(my_dict.keys()))
    selected_list = my_dict[selected_key]
    my_list = json.dumps(selected_list)
    return render(request, 'gamified_test/q24Screen.html', 
                  {'my_list': my_list},
                  {'selected_key': selected_key} )
def q24Screen(request):
    my_dict = {
        "affect": ['The', 'affect', 'of', 'the', 'wind', 'was', 'to', 'cause', 'the', 'boat’s', 'sail', 'to', 'billow.'],
        "meet": ['The', 'restaurant', 'offers', 'a', 'delicious', 'meet', 'dish', 'for', 'dinner.'],
        "then": ['There', 'are', 'less', 'girls', 'in', 'our', 'class', 'then', 'boys.'],
        "neat": ['You', 'must', 'get', 'your', 'neat', 'for', 'fishing.'],
    }
    selected_key = random.choice(list(my_dict.keys()))
    selected_list = my_dict[selected_key]
    my_list = json.dumps(selected_list)
    return render(request, 'gamified_test/q24Screen.html',
                   {'my_list': my_list,
                   'selected_key': selected_key})
def q25Screen(request):
    my_dict = {
    "of": ['Smoking','is','prohibited','of','the','entire','craft.'],
    "them":  ['This','homework','is','so','easy','.  I','can','do','them' ,'in','five','minutes.'],
    "was": ['I','swim','in','the','sea','whenever','the','weather','was','fine.'],
    "were":['When','we','went','shopping','it','were','very','busy.'],
    }
    selected_key = random.choice(list(my_dict.keys()))
    selected_list = my_dict[selected_key]
    my_list = json.dumps(selected_list)
    return render(request, 'gamified_test/q25Screen.html',
                   {'my_list': my_list,
                   'selected_key': selected_key})
def q26Screen(request):
    return render(request , 'gamified_test/q26Screen.html')
def q27Screen(request):
    return render(request , 'gamified_test/q27Screen.html')
def q28Screen(request):
    return render(request , 'gamified_test/q28Screen.html')
def q29Screen(request):
    return render(request , 'gamified_test/q29Screen.html')
def q30Screen(request):
    return render(request , 'gamified_test/q30Screen.html')
def q31Screen(request):
    list =["socks","hand","make" ,"room","spoon","vegetable", "science","house","elephant","read","shape","note","book","penguin","riddle","glass"]
    my_list = json.dumps(list)
    return render(request , 'gamified_test/q31Screen.html',{'my_list': my_list})
def q32Screen(request):
    list=["smay" ,"crench","qota","wabas","glis","glaba","nana"]
    my_list = json.dumps(list)
    return render(request , 'gamified_test/q32Screen.html',{'my_list': my_list})

@csrf_exempt  # Disable CSRF protection for this view (for simplicity)
def save_performance_data(request, exercise_num):
    if request.method == 'POST':
        # Retrieve performance data from AJAX request
        clicks = request.POST.get('clicks')
        hits = request.POST.get('hits')
        misses = request.POST.get('misses')
        missrate = request.POST.get('missrate')
        score = request.POST.get('score')
        accuracy = request.POST.get('accuracy')

        # retrieves the Player object linked to the currently authenticated user.
        player = request.user.player
        # Get or create GameData object for the player
        game_data, created = GameData.objects.get_or_create(player=player)
        
        # Update performance metrics for the specific exercise
        setattr(game_data, f'clicks{exercise_num}', clicks)
        setattr(game_data, f'hits{exercise_num}', hits)
        setattr(game_data, f'misses{exercise_num}', misses)
        setattr(game_data, f'missrate{exercise_num}', missrate)
        setattr(game_data, f'score{exercise_num}', score)
        setattr(game_data, f'accuracy{exercise_num}', accuracy)
        # store data in model
        game_data.save()
        
        return JsonResponse({'message': 'Performance data saved successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def getPredictions(data_array):
    # Load the ML model 
    current_directory = os.path.dirname(os.path.abspath(__file__))
    model_file_path = os.path.join(current_directory, 'ml_model', 'lr_model.sav')
    scaler_file_path = os.path.join(current_directory, 'ml_model', 'scaler.sav')
    
    with open(model_file_path, "rb") as model_file:
        model = pickle.load(model_file)
    
    with open(scaler_file_path, "rb") as scaler_file:
        scaler = pickle.load(scaler_file)
    
    # Scale the input data using the loaded scaler
    scaled_data = scaler.transform([data_array])  # Ensure data is in 2D array format
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
        'gender', 'isNative', 'otherlang', 'age'
    ]
    # Add performance metrics for each exercise to field_order
    for i in range(1, 33):
        field_order.extend([f'clicks_{i}', f'hits_{i}', f'misses_{i}', f'missrate_{i}', f'score_{i}', f'accuracy_{i}'])
    
    data_dict = {}
    # Retrieve data of the first row of the GameData table
    game_data_instance = GameData.objects.first()
    
    # Access demographic data of player
    gender = game_data_instance.player.gender
    created_at = game_data_instance.created_at
    data_dict['gender'] = 1.0 if gender.lower() == 'male' else 0.0
    data_dict['isNative'] = game_data_instance.player.isNative
    data_dict['otherlang'] = game_data_instance.player.failedLang
    data_dict['age'] = game_data_instance.player.age
    
    # Access performance metrics for each exercise
    for i in range(1, 33):
        data_dict[f'clicks_{i}'] = getattr(game_data_instance, f'clicks{i}')
        data_dict[f'hits_{i}'] = getattr(game_data_instance, f'hits{i}')
        data_dict[f'misses_{i}'] = getattr(game_data_instance, f'misses{i}')
        data_dict[f'missrate_{i}'] = getattr(game_data_instance, f'missrate{i}')
        data_dict[f'score_{i}'] = getattr(game_data_instance, f'score{i}')
        data_dict[f'accuracy_{i}'] = getattr(game_data_instance, f'accuracy{i}')
    
    # Arrange the data according to the specified order
    input_data = [data_dict[field] for field in field_order]
    data_array = np.array(input_data, dtype=float)  # Ensure the data array is of type float

    result = getPredictions(data_array)
    
    # Save result in database
    setattr(game_data_instance, 'result', result)
    game_data_instance.save()

    return render(request, 'gamified_test/result.html', 
                  {'result': result ,
                   'date': created_at})


