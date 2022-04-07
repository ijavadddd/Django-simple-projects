from django import forms
from . import models




class Earrings_Filter_form(forms.ModelForm):
    class Meta:
        model=models.Earrings_Filter
        fields=('SelectBox','Title','Slug')
        widget={
            'SelectBox':forms.CheckboxInput()
        }
