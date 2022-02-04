from django.contrib import admin
from .models import ProductCategory,ProductProperty,Product,Attribute,ProductImage,SameProduct
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

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('ProductProperty','Value','AttributeStatus')
    search_fields = ('AttributeStatus',)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('Image',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('Id',)
    list_display = ('Title','Brand','Id','Price','Discount','Status')
    search_fields = ('Status','Discount','Star')
    prepopulated_fields = {'Slug':('Title','Brand')}

@admin.register(SameProduct)
class SameProductAdmin(admin.ModelAdmin):
    list_display = ('ProductId','Status')
    search_fields = ('Status','Discount')
