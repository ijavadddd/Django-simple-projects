from django.urls import path
from apps.home import views

urlpatterns = [
    path('',views.home.as_view(),name='home'),
]
