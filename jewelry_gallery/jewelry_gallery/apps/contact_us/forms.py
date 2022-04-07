from django import forms
from . import models
class ContactUs(forms.ModelForm):
    class Meta:
        model=models.ContactUs
        fields='__all__'
        widgets={
            'Subject': forms.TextInput(attrs={'placeholder': 'Subject...','class':'contact-us-form--fields'}),
            'Email':forms.EmailInput(attrs={'class':'contact-us-form--fields','placeholder': 'Email...'}),
            'Message':forms.Textarea(attrs={'class':'contact-us-form--fields'}),
        }
