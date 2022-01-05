from django.shortcuts import render
from django.conf import settings
# Create your views here.
context={
        'media':settings.MEDIA_URL,
    }
def user_profile(request):
    return render(request,'user_profile/user_profile.html',context)

def car_rescuer(request):
    return render(request,'user_profile/car_rescuer.html',context)

def discount(request):
    return render(request,'user_profile/discount.html',context)

def credit(request):
    return render(request,'user_profile/credit.html',context)

def complaint(request):
    return render(request,'user_profile/complaint.html',context)