from django.urls import path,include
from apps.login import views

urlpatterns=[
    path('',views.login,name="login"),
    path('-register',views.register,name="register"),
    path('-register/confirm-number',views.confirm_number,name="confirm_number"),
]
