from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    first_name = forms.EmailField(required=False)
    last_name = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
  
        
