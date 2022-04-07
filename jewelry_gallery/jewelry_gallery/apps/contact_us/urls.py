from django.urls import path
from . import views

urlpatterns =[
    path('',views.contact_us.as_view(),name='contact_us')
]