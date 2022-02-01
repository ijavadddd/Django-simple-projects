from django.db import models

# Create your models here.

class UserRole(models.Model):
    Id = models.BigAutoField(primary_key=True ,auto_created=True)
    Title = models.CharField(max_length=20)
    
    def __str__(self):
        info=f'{self.Id}- {self.Title}'
        return info
#AdminSite
#Proffessor
#Student


class User(models.Model):
    ProfilePhoto = models.CharField(max_length=120,default=None)
    FirstName = models.CharField(max_length=22,default=None)
    LastName = models.CharField(max_length=22,default=None)
    DateOfBirth = models.DateField(default=None)
    PhoneNumber = models.CharField(max_length=11)
    Email = models.EmailField(max_length=35)
    Role =models.ForeignKey(UserRole,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        info=f'{self.FirstName} {self.LastName} -> {self.Role}'
        return info
    
class Category(models.Model):
    Title = models.CharField(max_length=30)
    Slug=models.SlugField(max_length=50)
    Parent = models.ForeignKey('self',on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        info=f'{self.Parent} > {self.Title}'
        return info

class Course(models.Model):
    def CountStudent(self):
        students=self.Students.objects.all()
        count=0
        for student in students:
            count+=1
        return count
    Picture = models.CharField(max_length=85)
    Title = models.CharField(max_length=50)
    Level = models.CharField(max_length=20,default=None)
    Slug =models.SlugField(max_length=100)
    Students = models.ManyToManyField(User)
    NumberOfStudents=CountStudent
    Category =models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        info=f'{self.Title} - {self.Level} ({self.NumberOfStudents})'
        return info

class Session(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Picture = models.CharField(max_length=85)
    Title = models.CharField(max_length=50)
    Slug =models.SlugField(max_length=100)
    Description = models.TextField()
    File = models.CharField(max_length=200)
    
    def __str__(self):
        info=f'{self.Course} - {self.Title}'
        return info