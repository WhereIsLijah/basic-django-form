from django import forms

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    terms_condition = forms.CharField(required=True, widget=forms.CheckboxInput(attrs={'default': True}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)