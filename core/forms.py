from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length = 250, widget=forms.TextInput(attrs={'class':'form-control input-lg w-full px-1 py-1 rounded-xl', 'placeholder':'Username'}))
    password = forms.CharField(max_length = 250, widget=forms.PasswordInput(attrs={'class':'form-control input-lg w-full px-1 py-1 rounded-xl', 'placeholder':'Password'}))

    

class SignupForm(UserCreationForm):
                             

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

    email = forms.EmailField(max_length = 250, widget=forms.TextInput(attrs={'class':'form-control input-lg w-full px-1 py-1 rounded-xl', 'placeholder':'Email'}))
    username = forms.CharField(max_length = 250, widget=forms.TextInput(attrs={'class':'form-control input-lg w-full px-1 py-1 rounded-xl', 'placeholder':'Username'}))
    password1 = forms.CharField(max_length = 250, widget=forms.PasswordInput(attrs={'class':'form-control input-lg w-full px-1 py-1 rounded-xl', 'placeholder':'Password'}))
    password2 = forms.CharField(max_length = 250, widget=forms.PasswordInput(attrs={'class':'form-control input-lg w-full px-1 py-1 rounded-xl', 'placeholder':'Confirm Password'}))