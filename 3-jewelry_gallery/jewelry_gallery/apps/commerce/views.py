from django.shortcuts import render
from django.conf import settings

# Create your views here.
def search(request):
    context={
        'media':settings.MEDIA_URL,
    }
    return render(request,'commerce/commerce.html',context)