from django.urls import path
from . import views

app_name ='authentication'

urlpatterns=[
    path('home/', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('register-player/', views.register_player, name='register-player'),
    path('register-parent-teacher/', views.register_parent_teacher, name='register-parent-teacher'),
    path('user_login/', views.user_login, name='user_login'),
]
