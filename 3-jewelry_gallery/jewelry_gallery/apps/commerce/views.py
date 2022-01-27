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
    category=product[0].Category
    categoryList=[]
    def GetCategory(category):
        if category.Parent != None:
            GetCategory(category.Parent)
        categoryList.append(category)
    GetCategory(category)
    
    context={
        'media':settings.MEDIA_URL,
        'product':product, 
        'categories':categoryList,
    }
    return render(request,'commerce/product.html',context)

def Category(request,category):
    products = Product.objects.all()
    aa=[]
    for product in products:
        if product.Category.Slug == category:
            aa.append(product)
        else:
            def GetCategory(productCategory):
                if productCategory.Slug == category:
                    aa.append(product)
                if productCategory.Parent != None:
                    GetCategory(productCategory.Parent)
            GetCategory(product.Category)
    context={
        'media':settings.MEDIA_URL,
        'product':products,
        'aa':aa,
    }
    print(aa)
    return render(request,'commerce/category.html',context)