from apps.blog import views
from django.urls import path,include

urlpatterns = [
    path('',views.articles,name='blog'),
]

