# Generated by Django 3.2.5 on 2022-01-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0010_auto_20220122_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProductImage',
            field=models.CharField(max_length=450),
        ),
    ]
