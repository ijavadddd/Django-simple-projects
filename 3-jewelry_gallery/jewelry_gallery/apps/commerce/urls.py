from django.urls import path
from apps.commerce import views

urlpatterns = [
    path('',views.search,name='search'),
    path('<int:productId>/<slug:productSlug>',views.Product_Page,name='product_page'),
]
