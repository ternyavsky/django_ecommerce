from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField, PasswordResetForm, SetPasswordForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "text",
        'id': "username",
        'placeholder':"Username",
        'name':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete": "current-password",
        'class':'form-control',
        'type': "password",
        'id': "password",
        'placeholder':"Password",
        'name':'password'}),
    ) 


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        
        max_length=254,
        widget=forms.EmailInput(attrs={
            "autocomplete": "email",
            'class':'form-control',
            'id':'email',
            'placeholder':'Email',
            'name':'email',
            'type':'email'})
    )

class ConfirmPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
       
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
            'class':'form-control',
            'id':'password',
            'placeholder':'Password',
            'name':'password',
            'type':'password'})
       
    )
    new_password2 = forms.CharField(
      
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
        'class':'form-control',
            'id':'password',
            'placeholder':'Password again',
            'name':'password',
            'type':'password'}))
    
    


class RegistrationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "email",
        'id': "floatingInput",
        'placeholder':"Email",
        'name':'email'}))
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "text",
        'id': "floatingInput",
        'placeholder':"Username",
        'name':'username'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "text",
        'id': "fname",
        'placeholder':"Firstname",
        'name':'email'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "text",
        'id': "lname",
        'placeholder':"Lastname",
        'name':'username'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete": "new-password",
        'class':'form-control',
        'type': "password",
        'id': "password",
        'placeholder':"Password",
        'name':'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete": "new-password",
        'class':'form-control',
        'type': "password",
        'id': "password",
        'placeholder':"Password again",
        'name':'password2'
    }))