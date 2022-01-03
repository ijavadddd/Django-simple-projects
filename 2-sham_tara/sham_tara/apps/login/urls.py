from django.urls import path,include
from apps.login import views

urlpatterns=[
    path('',views.login,name="login"),
    path('-register',views.register,name="register"),
]
