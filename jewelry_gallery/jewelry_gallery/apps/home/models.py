from django.db import models

# Create your models here.
class Role(models.Model):
    Title = models.CharField(max_length=35)
    Status = models.BooleanField(default=True)
##Subscriber
##Contributor
##Author
##Editor
##Administrator
## no role


class User(models.Model):
    FirstName = models.CharField(max_length=35)
    LastName = models.CharField(max_length=35,default="None")
    Password = models.CharField(max_length=35,)
    PhoneNumber = models.CharField(max_length=20)
    Email = models.EmailField(max_length=45,default=None)
    Address= models.TextField(default=None)
    Role= models.ForeignKey(Role, on_delete=models.CASCADE)
    Status = models.BooleanField(default=True)