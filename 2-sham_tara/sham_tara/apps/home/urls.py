from django.urls import path
import apps.home.views as views

urlpatterns = [
    path('',views.index,name='home'),
]
