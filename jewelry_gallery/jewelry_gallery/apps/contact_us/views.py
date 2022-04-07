from django.shortcuts import render
from django.conf import settings
from django.views import View
from . import forms
# Create your views here.
class contact_us(View):
    def get(self,request):   
        contact_us_form=forms.ContactUs 
        context={
            'media':settings.MEDIA_URL,
            'contact_us_form':contact_us_form,
        }
        return render(request, 'contact_us/contact_us.html',context)