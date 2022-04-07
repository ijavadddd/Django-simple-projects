from django.db import models

# Create your models here.
class Role(models.Model):
    Title = models.CharField(max_length=35)
    Status = models.BooleanField(default=True)

    def __str__(self):
        self.info=f'{self.Title}'
        return self.info
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
    Email = models.CharField(max_length=45,default=None,null=True,blank=True)
    Address= models.TextField(default=None,null=True,blank=True)
    Role= models.ForeignKey(Role, on_delete=models.CASCADE)
    Status = models.BooleanField(default=True)

    def __str__(self):
        self.info=f'{self.FirstName} {self.LastName} - {self.Role}'
        return self.info