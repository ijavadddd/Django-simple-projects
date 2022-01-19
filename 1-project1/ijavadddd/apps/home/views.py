from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Autor



def index(request):
    Autors=Autor.objects.all()
    context={
        'media_url':settings.MEDIA_URL,
        'professor':Autors,
        'lenList':range(0 , len(Autors)),
    }
    return render(request,'home/index.html',context)