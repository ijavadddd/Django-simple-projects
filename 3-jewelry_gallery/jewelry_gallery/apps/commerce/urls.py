from django.urls import path
from apps.commerce import views

urlpatterns = [
    path('',views.search,name='search'),
]
