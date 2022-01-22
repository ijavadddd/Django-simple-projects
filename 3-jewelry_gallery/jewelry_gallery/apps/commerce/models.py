from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    CategoryTitle = models.CharField(max_length=80)
    Slug = models.SlugField(max_length=100)
    CategoryStatus = models.BooleanField(default=True)
    
    def __str__(self):
        self.values = f'{self.CategoryTitle}'
        return self.values

class ProductProperty(models.Model):
    PropertyTitle = models.CharField(max_length=35,primary_key=True)
    ProductPropertyStatus = models.BooleanField(default=True)

    
    def __str__(self):
        self.values = f'{self.PropertyTitle}'
        return self.values
    # Size      
    # Weight    
    # Colors    
    # Material  
    # Dimensions
    # Length    
    # Jewel     
    # Width     
    # LockType  
    # Shorten   
    # Stone     

class Attribute(models.Model):
    ProductProperty = models.ForeignKey(ProductProperty, on_delete=models.CASCADE)
    Value= models.CharField(max_length=50)
    AttributeStatus = models.BooleanField(default=True)
    
    def __str__(self):
        self.values = f'{self.ProductProperty} {self.Value}'
        return self.values

class Product(models.Model):
    ProductId= models.BigAutoField(primary_key=True ,auto_created=True)
    ProductImage = models.CharField(max_length=450)
    ProductTitle = models.CharField(max_length=250)
    ProductBrand = models.CharField(max_length=120 ,null=True, blank=True)
    Slug = models.SlugField(max_length=450)
    ProductPrice = models.CharField(max_length=35)
    ProductDiscount = models.IntegerField(default=0)
    ProductStar = models.FloatField()
    ProductStatus = models.BooleanField(default=True)
    ProductCategorys = models.ManyToManyField(ProductCategory)
    Attribute = models.ManyToManyField(Attribute)
    
    def __str__(self):
        self.values = f'{self.ProductTitle} {self.ProductBrand}'
        return self.values
