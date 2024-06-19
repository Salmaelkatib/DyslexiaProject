from django.urls import path,re_path
from . import views

app_name = 'adaptation'
urlpatterns = [
    path('', views.base, name='base'), #for startTracking
    path('bg_extension1/',views.bg_extension1, name='bg_extension1'),
    path('bg_extension2/',views.bg_extension2, name='bg_extension2'),
    path('bg_extension3/',views.bg_extension3, name='bg_extension3'),
    path('bg_extension4/',views.bg_extension4, name='bg_extension4'),

    path('font_type_extension1/',views.font_type_extension1, name='font_type_extension1'),
    path('font_type_extension2/',views.font_type_extension2, name='font_type_extension2'),
    path('font_type_extension3/',views.font_type_extension3, name='font_type_extension3'),
    path('font_type_extension4/',views.font_type_extension4, name='font_type_extension4'),
    path('font_type_extension5/',views.font_type_extension5, name='font_type_extension5'),
    path('font_type_extension6/',views.font_type_extension6, name='font_type_extension6'),
    path('font_type_extension7/',views.font_type_extension7, name='font_type_extension7'),

    path('text_color_extension/',views.text_color_extension, name='text_color_extension'),

    path('char_spacing_extension1/',views.char_spacing_extension1, name='char_spacing_extension1'),
    path('char_spacing_extension2/',views.char_spacing_extension2, name='char_spacing_extension2'),

    path('stopTracking/',views.stopTracking, name='stopTracking'),
    re_path(r'.*save_gaze_data/$', views.save_gaze_data, name='save_gaze_data'),

]