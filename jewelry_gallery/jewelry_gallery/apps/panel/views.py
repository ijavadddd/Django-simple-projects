from django.shortcuts import render
from django.conf import settings
from .models import AdminPanelItem

# Create your views here.
def AdminDashboard(request):
    sidebarItems=AdminPanelItem.objects.all()
    context ={
        'media':settings.MEDIA_URL,
        'sidebarItems':sidebarItems,
    }
    return render(request,'panel/admin-dashboard.html',context)

def AdminEducation(request):
    sidebarItems=AdminPanelItem.objects.all()
    context ={
        'media':settings.MEDIA_URL,
        'sidebarItems':sidebarItems,
    }
    return render(request,'panel/admin-education.html',context)

def AdminMedia(request):
    sidebarItems=AdminPanelItem.objects.all()
    context ={
        'media':settings.MEDIA_URL,
        'sidebarItems':sidebarItems,
    }
    return render(request,'panel/admin-media.html',context)

def AdminUsers(request):
    sidebarItems=AdminPanelItem.objects.all()
    context ={
        'media':settings.MEDIA_URL,
        'sidebarItems':sidebarItems,
    }
    return render(request,'panel/admin-users.html',context)