from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorId = models.AutoField( 
                                    unique=True,
                                    auto_created=True,
                                    primary_key=True,
                                    verbose_name="ایدی اساتید",
                                    )
    FirstName = models.CharField(
                                    max_length=30,
                                    null=False,
                                    verbose_name="نام",
                                    )
    LastName = models.CharField(    
                                    max_length=30,
                                    null=False,
                                    verbose_name="نام خانوادگی",
                                    )
    # Slug = models.SlugField(max_length=60)
    Skill = models.CharField(
                                    max_length=120,
                                    help_text="مهارت هایتان را با , جدا کنید",
                                    verbose_name="مهارت ها",
                                    )
    Age = models.IntegerField(
                                    verbose_name="سن",
                                    )
    ProfilePhoto = models.CharField(
                                    default='None',
                                    max_length=350,
                                    verbose_name="عکس پروفایل",
                                    )
    Status = models.BooleanField(
                                    default=True,
                                    null=False,
                                    verbose_name="وضعیت",
                                    )
    class Meta:
        verbose_name ='اساتید'
        verbose_name_plural ='استاد'
        
    def __str__(self):
        Field = f'نام : {self.FirstName} , نام خانوادگی : {self.LastName} , وضعیت : {self.Status}'
        return Field

class Tutorial(models.Model):
    TutorialId = models.AutoField( 
                                    unique=True,
                                    auto_created=True,
                                    primary_key=True,
                                    verbose_name="ایدی آموزش",
                                    )
    TutorialTitle = models.CharField(
                                    max_length=30,
                                    null=False,
                                    verbose_name="عنوان آموزش",
                                    )
    Slug = models.SlugField(max_length=60)
    Tags = models.CharField(
                                    max_length=120,
                                    help_text="تگ های مربوط به آموزش را بنویسید",
                                    verbose_name="تگ ها",
                                    )
    TutorialPeriod = models.IntegerField(
                                    verbose_name="مدت زمان",
                                    )
    TutorialProfile = models.CharField(
                                    default='None',
                                    max_length=350,
                                    verbose_name="تصویر آموزش",
                                    )
    Status = models.BooleanField(
                                    default=True,
                                    null=False,
                                    db_column ="وضعیت",
                                    verbose_name="وضعیت",
                                    )
    Author = models.ForeignKey(
                                    Author,
                                    on_delete=models.SET_NULL,
                                    max_length=30,
                                    default=None,
                                    null=True,
                                    verbose_name="استاد",
                                    )
    
    class Meta:
        verbose_name ='دوره'
        verbose_name_plural ='دوره ها'
    def __str__(self):
        Field = f'عنوان آموزش : {self.TutorialTitle} , استاد : {self.Author}, وضعیت : {self.Status}'
        return Field