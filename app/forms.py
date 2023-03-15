from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class CustomerRegistrationForm(UserCreationForm):
    email=forms.EmailField(label='Email',required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

    class Meta:
        model=User
        fields=['email','username','password1','password2']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
        help_texts={
            'username':None
        }


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    
    
    class Meta:
        model=User
        fields=['email','password']
        