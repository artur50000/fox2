from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):  
        class Meta:  
            model = User  
            fields = ('email', 'password1', 'password2', 'username')


class ProfileForm(forms.Form):
    
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    bio = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
  

class ImageForm(forms.Form):
    
    image = forms.ImageField()