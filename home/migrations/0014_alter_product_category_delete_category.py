# Generated by Django 5.0.6 on 2024-09-06 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_category_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
