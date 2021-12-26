from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.home.urls')),
    path('blog',include('apps.blog.urls')),
    path('login',include('apps.login.urls')),
]
