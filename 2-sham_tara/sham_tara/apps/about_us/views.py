from django.shortcuts import render
from django.conf import settings

# Create your views here.
def about_us(request):
    context={
        'media':settings.MEDIA_URL,
    }    
    return render(request,'about_us/about_us.html',context)