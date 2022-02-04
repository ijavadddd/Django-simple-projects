from django.shortcuts import render
from django.conf import settings
# Create your views here.
def home(request):
    context={
        'media':settings.MEDIA_URL,
    }
    return render(request,'home/index.html', context)