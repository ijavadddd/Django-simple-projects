from django.urls import path
from apps.login import views

urlpatterns = [
    path('',views.login,name='login'),
    
]