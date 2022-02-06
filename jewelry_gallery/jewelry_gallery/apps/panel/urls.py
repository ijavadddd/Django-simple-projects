from django.urls import path
from . import views

urlpatterns =[
    path('admin/dashboard',views.AdminDashboard,name='admin'),
    path('admin/education',views.AdminEducation),
    path('admin/media',views.AdminMedia),
]
