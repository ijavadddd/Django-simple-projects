from django.urls import path
from apps.about_us import views
urlpatterns=[
    path('',views.about_us,name="about_us")
]

