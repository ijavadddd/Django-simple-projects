from django.db import models

# Create your models here.
class Autor(models.Model):
    AutorId = models.AutoField( 
                                    unique=True,
                                    auto_created=True,
                                    primary_key=True,
                                    db_column="آیدی",
                                    verbose_name="ایدی اساتید",
                                    )
    FirstName = models.CharField(
                                    max_length=30,
                                    null=False,
                                    db_column ="نام",
                                    verbose_name="نام",
                                    )
    LastName = models.CharField(    
                                    max_length=30,
                                    null=False,
                                    db_column ="نام خانوادگی",
                                    verbose_name="نام خانوادگی",
                                    )
    # Slug = models.SlugField(max_length=60)
    Skill = models.CharField(
                                    max_length=120,
                                    help_text="مهارت هایتان را با , جدا کنید",
                                    db_column ="مهارت ها",
                                    verbose_name="مهارت ها",
                                    )
    Age = models.IntegerField(
                                    db_column="سن",
                                    verbose_name="سن",
                                    )
    ProfilePhoto = models.CharField(
                                    default='None',
                                    max_length=350,
                                    db_column ="عکس پروفایل",
                                    verbose_name="عکس پروفایل",
                                    )
    Status = models.BooleanField(
                                    default=True,
                                    null=False,
                                    db_column ="وضعیت",
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
                                    db_column="آیدی",
                                    verbose_name="ایدی آموزش",
                                    )
    TutorialTitle = models.CharField(
                                    max_length=30,
                                    null=False,
                                    db_column ="عنوان آموزش",
                                    verbose_name="عنوان آموزش",
                                    )
    Slug = models.SlugField(max_length=60)
    Tags = models.CharField(
                                    max_length=120,
                                    help_text="تگ های مربوط به آموزش را بنویسید",
                                    db_column ="تگ ها",
                                    verbose_name="تگ ها",
                                    )
    TutorialPeriod = models.IntegerField(
                                    db_column="مدت زمان",
                                    verbose_name="مدت زمان",
                                    )
    TutorialProfile = models.CharField(
                                    default='None',
                                    max_length=350,
                                    db_column ="تصویر آموزش",
                                    verbose_name="تصویر آموزش",
                                    )
    Status = models.BooleanField(
                                    default=True,
                                    null=False,
                                    db_column ="وضعیت",
                                    verbose_name="وضعیت",
                                    )
    Autor = models.ForeignKey(
                                    Autor,
                                    on_delete=models.SET_NULL,
                                    max_length=30,
                                    default=None,
                                    null=True,
                                    db_column ="استاد",
                                    verbose_name="استاد",
                                    )
    
    class Meta:
        verbose_name ='دوره'
        verbose_name_plural ='دوره ها'
    def __str__(self):
        Field = f'عنوان آموزش : {self.TutorialTitle} , استاد : {self.Autor}, وضعیت : {self.Status}'
        return Field