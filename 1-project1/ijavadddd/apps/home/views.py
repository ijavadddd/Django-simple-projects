from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Author



def index(request):
    Authors=Author.objects.all()
    context={
        'media_url':settings.MEDIA_URL,
        'professor':Authors,
        'lenList':range(0 , len(Authors)),
    }
    return render(request,'home/index.html',context)