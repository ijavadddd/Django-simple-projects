from django.db import models

# Create your models here.
class ContactUs(models.Model):
    Subject= models.CharField(max_length=125)
    Email= models.EmailField()
    Message=models.TextField()