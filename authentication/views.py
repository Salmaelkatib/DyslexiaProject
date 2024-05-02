from django.shortcuts import render
from authentication.forms import PlayerForm,UserForm,Parent_TeacherForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    registered = request.GET.get('registered', False)  
    return render(request , 'authentication/home.html' ,{'registered': registered})

def signin(request):
    return render(request , 'authentication/signin.html')

def register(request):
    userForm = UserForm()
    playerForm = PlayerForm()
    parent_teacherForm = Parent_TeacherForm()

    return render(request , 'authentication/register.html' , {
        'userForm': userForm,
        'playerForm': playerForm,
        'parent_teacherForm': parent_teacherForm
    })

def register_player(request):
    if request.method == 'POST':  
        userForm = UserForm(data=request.POST)
        playerForm = PlayerForm(data=request.POST)
        
        if userForm.is_valid() and playerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            player = playerForm.save(commit=False)  # Get unsaved instance
            player.user = user  # Assign user to player
            player.save()  # Save player instance
            return HttpResponseRedirect(reverse('home'))
        else:
            print(userForm.errors, playerForm.errors)  
    else:
        userForm = UserForm()
        playerForm = PlayerForm()
        
    return render(request, 'authentication/register.html', {
        'userForm': userForm,
        'playerForm': playerForm,
    })
def register_parent_teacher(request):
    if request.method == 'POST':  
        userForm = UserForm(data=request.POST)
        parent_teacherForm = Parent_TeacherForm(data=request.POST)
        
        if userForm.is_valid() and parent_teacherForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            p = parent_teacherForm.save(commit=False)  # Get unsaved instance
            p.user = user  # Assign user to player
            p.save()  # Save player instance
            return HttpResponseRedirect(reverse('home'))
        else:
            print(userForm.errors, parent_teacherForm.errors)  
    else:
        userForm = UserForm()
        parent_teacherForm = Parent_TeacherForm()
        
    return render(request, 'authentication/register.html', {
        'userForm': userForm,
        'parent_teacherForm': parent_teacherForm,
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password = password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("inactive account")
        else:
            return HttpResponse("invalid data")
    else:
        return render(request, 'authentication/signin.html',{})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))