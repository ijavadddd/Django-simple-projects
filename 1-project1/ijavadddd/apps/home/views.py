from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Professor
def index(request):
    professors=Professor.objects.all()
    for professor in professors:
        for skills in professor.Skill:
            skillList=skills.split()
            skills='ddsss'
    context={
        'media_url':settings.MEDIA_URL,
        'teacher':professors,
        'lenList':range(0 , len(professors)),
    }
    return render(request,'home/index.html',context)
