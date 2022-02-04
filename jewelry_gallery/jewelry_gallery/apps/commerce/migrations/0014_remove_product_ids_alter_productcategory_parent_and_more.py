# Generated by Django 4.0.1 on 2022-02-03 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0013_product_ids_alter_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Ids',
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='Parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='commerce.productcategory'),
        ),
        migrations.AlterField(
            model_name='sameproduct',
            name='Image',
            field=models.ManyToManyField(to='commerce.ProductImage'),
        ),
    ]
