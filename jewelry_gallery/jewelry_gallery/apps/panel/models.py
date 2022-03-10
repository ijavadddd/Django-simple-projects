from django.db import models

# Create your models here.
class AdminPanelItem(models.Model):
    Icon=models.CharField(max_length=25,default=None)
    Title=models.CharField(max_length=25)
    Slug=models.CharField(max_length=35)
    Status =models.BooleanField(default=True)

