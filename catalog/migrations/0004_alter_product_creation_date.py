# Generated by Django 4.2.1 on 2023-06-01 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='creation_date',
            field=models.DateField(verbose_name='дата создания'),
        ),
    ]