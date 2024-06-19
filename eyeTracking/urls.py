from django.urls import path
from . import views

app_name = 'eyeTracking'
urlpatterns = [
    path('', views.eyeTracking, name='eyeTracking'), #for startTracking
    path('stopTracking', views.stopTracking, name='stopTracking'),
    path('save_gaze_data/', views.save_gaze_data, name='save_gaze_data'),
    path('result/', views.result, name='result'),
]