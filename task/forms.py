
from django import forms 

from django.contrib.auth.models import User

class RegistrationForm(forms.Form):

    class Meta:
        model=User
        field=["first_name","last_name","username","email","password"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()        
