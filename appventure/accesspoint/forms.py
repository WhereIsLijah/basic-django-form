from django import forms
from .models import UserInfo

class SignUpForm(forms.ModelForm): 
    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'email', 'password', 'password2', 'terms_condition']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
            'terms_condition': forms.CheckboxInput(attrs={'default': True})
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Type your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type your password'}), required=True)