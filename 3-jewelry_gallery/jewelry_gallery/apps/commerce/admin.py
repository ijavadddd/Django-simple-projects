from django.contrib import admin
from .models import ProductCategory,ProductProperty,Product,Attribute
# Register your models here.
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('CategoryTitle','CategoryStatus')
    search_fields = ('CategoryStatus',)
    prepopulated_fields = {'Slug':('CategoryTitle',)}

@admin.register(ProductProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    list_display = ('PropertyTitle','ProductPropertyStatus')
    search_fields = ('ProductPropertyStatus',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('ProductTitle','ProductBrand','ProductPrice','ProductDiscount','ProductStatus')
    search_fields = ('ProductStatus','ProductDiscount','ProductStar')
    prepopulated_fields = {'Slug':('ProductTitle','ProductBrand')}
