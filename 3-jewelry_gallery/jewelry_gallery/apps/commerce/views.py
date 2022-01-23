from django.shortcuts import render
from django.conf import settings
from . models import Product
# Create your views here.
def search(request):
    products=Product.objects.all()
    context={
        'media':settings.MEDIA_URL,
        'products':products,
    }
    return render(request,'commerce/commerce.html',context)

def Product_Page(request,productId,productSlug):
    product = Product.objects.all().filter(Id=int(productId))
    context={
        'media':settings.MEDIA_URL,
        'product':product,
    }
    return render(request,'commerce/product.html',context)