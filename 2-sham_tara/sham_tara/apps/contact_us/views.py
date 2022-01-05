from django.shortcuts import render
from django.conf import settings
# Create your views here.
def contact_us(request):
    context={
        'media':settings.MEDIA_URL,
    }
    return render(request,'contact_us/contact_us.html',context)