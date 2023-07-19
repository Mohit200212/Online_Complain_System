from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
import pandas

class LoginForm(forms.Form):
   username=forms.CharField(max_length=20)
   password=forms.CharField(max_length=8,widget=forms.PasswordInput)

   
       


 
       























