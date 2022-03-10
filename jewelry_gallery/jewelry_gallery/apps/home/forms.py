from django import forms
from .models import User

class RegisterForm(forms.Form):
    class Meta:
        model = User
        fields = ['FirstName','PhoneNumber']
