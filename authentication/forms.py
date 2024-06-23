from django.contrib.auth.models import User
from authentication.models import Player,Parent_Teacher
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # Update attributes for username field separately
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'usernameInputId',
            'aria-describedby': 'usernameHelp',
        })
        # Update attributes for other fields
        for field in ['email', 'password']:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class PlayerForm(forms.ModelForm):
     YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]
     GENDER_CHOICES = [
        ("male", 'Male'),
        ("female", 'Female'),
    ]
     nationalId = forms.CharField(widget=forms.TextInput(attrs={'id': 'nationaId'}))
     age = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'age'}))
     gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'id': 'gender'}))
     isNative = forms.ChoiceField(choices=YES_NO_CHOICES,widget=forms.Select(attrs={'id': 'isNative'}))
     failedLang = forms.ChoiceField(choices=YES_NO_CHOICES,widget=forms.Select(attrs={'id': 'failedLang'}))

     def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

     class Meta():
        model = Player
        fields =('isNative' , 'failedLang' ,'nationalId' ,'gender' ,'age')
    
class Parent_TeacherForm(forms.ModelForm):
     nationalId = forms.CharField(widget=forms.TextInput(attrs={'id': 'nationaId'}))

     def __init__(self, *args, **kwargs):
        super(Parent_TeacherForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

     class Meta():
        model = Parent_Teacher
        fields =('nationalId',)
    