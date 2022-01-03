from django.shortcuts import render
from django.conf import settings

# Create your views here.
def login(request):
    context={
        'media':settings.MEDIA_URL,
    }
    return render(request,'login/login.html',context)

def register(request):
    context={
        'media':settings.MEDIA_URL,
    }
    return render(request,'login/register.html',context)