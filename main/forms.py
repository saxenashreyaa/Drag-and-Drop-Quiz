
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    fullname = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("fullname","username","email" ,"password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,

        }
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.fullname = self.cleaned_data["fullname"]

        if commit:
            user.save()
        return user

"""from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Info


class RegistrationForm(forms.ModelForm):
    fullname = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter full name'}))
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    email = forms.CharField(max_length=50,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter emailID'}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))

    class Meta:
        model = Info
        fields = ("fullname","username","email","password")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]
        user.fullname = self.cleaned_data["fullname"]
        user.password = self.cleaned_data["password"]

        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))"""

