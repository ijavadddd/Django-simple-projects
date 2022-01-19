from django.db import models


class Author(models.Model):
    SEX_LIST = [
        ('M','مرد'),
        ('F','زن'),
    ]
    FirstName = models.CharField(max_length=50,null=False,verbose_name='نام')
    LastName = models.CharField(max_length=50,null=False,verbose_name='نام خانوادگی')
    Slug = models.SlugField(max_length=110)
    Email = models.EmailField(max_length=120,verbose_name='ایمیل')
    PhoneNumber = models.CharField(max_length=15,null=True,blank=True,verbose_name='شماره تلفن')
    Sex = models.CharField(choices=SEX_LIST,null=False,max_length=10,verbose_name='جنسیت')
    Education = models.CharField(max_length=60,null=False,verbose_name='تحصیلات')
    DataOfBirth = models.DateField(null=True, blank=True,verbose_name='تاریخ تولد')
    Bio = models.TextField(null=True, blank=True,verbose_name='بیوگرافی')
    ProfilePhoto = models.CharField(max_length=300,null=True,blank=True,verbose_name='تصویر پروفایل')
    Status = models.BooleanField(default=True,verbose_name='وضعیت')
    
    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'
    
    def __str__(self):
        Field = f'{self.FirstName} {self.LastName}'
        return Field

class Article(models.Model):
    Title =models.CharField(null=False,max_length=85,verbose_name='عنوان')
    Slug = models.SlugField(max_length=85)
    Created_at = models.DateTimeField(null=False,auto_now_add=True,verbose_name='تاریخ ساخت')
    Text = models.TextField(null=False,verbose_name='متن مقاله')
    ReadPeriad = models.IntegerField(null=True,verbose_name='مدت زمان مطالعه')
    Tags = models.CharField(max_length=40,verbose_name='تگ های مربوط به مقاله',null=True)
    Refrence = models.CharField(max_length=500,verbose_name='منابع',null=True)
    Author = models.ManyToManyField(Author,verbose_name='نویسنده')
    Status = models.BooleanField(default=True,verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        Field = f'عنوان مقاله : {self.Title} , نویسنده : {self.Author}, وضعیت : {self.Status}'
        return Field
