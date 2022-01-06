from django.urls import path
import apps.contact_us.views as views

urlpatterns = [
    path('',views.contact_us,name='contact_us')
]




