# Generated by Django 4.2.1 on 2023-06-01 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_change_date',
            field=models.DateField(verbose_name='дата последнего изменения'),
        ),
    ]