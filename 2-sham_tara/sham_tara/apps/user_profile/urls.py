from apps.user_profile import views
from django.urls import path

urlpatterns = [
    path('',views.user_profile,name='user_profile'),
    path('car_rescuer/',views.car_rescuer,name="car_rescuer"),
    path('discount/',views.discount,name="discount"),
    path('credit/',views.credit,name="credit"),
    path('complaint/',views.complaint,name="complaint"),
    
]

