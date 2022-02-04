from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.home.urls')),
    path('search/',include('apps.commerce.urls')),
    path('contact_us/',include('apps.contact_us.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)