# Generated by Django 4.0.1 on 2022-02-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0010_rename_same_product_otherproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='OtherProduct',
            field=models.ManyToManyField(null=True, to='commerce.SameProduct'),
        ),
    ]
