from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
    context={
        'media':settings.MEDIA_URL,
    }
    return render(request, 'home/home.html',context)