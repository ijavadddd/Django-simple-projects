from django.shortcuts import render
from django.conf import settings
# Create your views here.
def user_profile(request):
    context = {
        'media' :settings.MEDIA_URL,
    }
    return render(request,'user_profile/user_profile.html',context)

def car_rescuer(request):
    context={
        'media':settings.MEDIA_URL,
    }
    return render(request,'user_profile/car_rescuer.html',context)