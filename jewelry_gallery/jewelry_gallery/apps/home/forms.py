from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['FirstName','PhoneNumber','Password']
        widgets={
            'FirstName':forms.TextInput(attrs={'class':'form-input','placeholder':'First Name'}),
            'PhoneNumber':forms.TextInput(attrs={'class':'form-input','placeholder':'Mobile Number'}),
            'Password':forms.PasswordInput(attrs={'class':'form-input','placeholder':'Password'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['PhoneNumber','Password']
        widgets={
            'PhoneNumber':forms.TextInput(attrs={'class':'form-input','placeholder':'Mobile Number'}),
            'Password':forms.PasswordInput(attrs={'class':'form-input','placeholder':'Password'}),
        }
