# Generated by Django 4.2.1 on 2023-06-20 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_blog_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='contents',
            field=models.TextField(verbose_name='содержание'),
        ),
    ]
