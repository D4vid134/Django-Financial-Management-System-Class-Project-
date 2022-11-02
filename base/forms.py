from django.forms import ModelForm
from .models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
        
class RegisterUserForm(UserCreationForm):
    first_name =  forms.CharField(max_length=40)
    last_name =  forms.CharField(max_length=40)
    age = forms.IntegerField()
    address = forms.CharField(max_length=255)
    sex = forms.CharField(max_length=10)
    occupation = forms.CharField(max_length=200)
    
    class Meta(UserCreationForm):
        model = User
        fields = ('username','first_name', 'last_name', 'age', 'address', 'sex', 'occupation', 'password1', 'password2')