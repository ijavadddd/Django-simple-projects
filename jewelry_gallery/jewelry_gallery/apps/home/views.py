from django.shortcuts import render
from django.conf import settings
from .forms import RegisterForm 

# Create your views here.
def home(request):
    registerForm=RegisterForm
    context={
        'media':settings.MEDIA_URL,
        'registerForm':registerForm
    }
    return render(request,'home/index.html', context) 