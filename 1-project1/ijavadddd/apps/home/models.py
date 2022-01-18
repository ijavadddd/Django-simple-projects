from django.db import models

# Create your models here.
class Professor(models.Model):
    ProfessorId = models.AutoField( 
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
                                    help_text="Skill seprate by , ",
                                    db_column ="مهارت ها",
                                    verbose_name="مهارت ها",
                                    )
    Age = models.IntegerField(
                                    db_column="سن",
                                    )
    ProfilePhoto = models.CharField(
                                    default='No7ne',
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
    def __str__(self):
        Field = f'First name : {self.FirstName} , Last name : {self.LastName} , Status : {self.Status}'
        return Field