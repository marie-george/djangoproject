from django.db import models
from django.urls import reverse
from pytils.translit import slugify

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=500, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    author = models.CharField(max_length=150, verbose_name='автор')
    description = models.CharField(max_length=500, verbose_name='описание')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateField(verbose_name='дата создания')
    last_change_date = models.DateField(verbose_name='дата последнего изменения')
    preview = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URl')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.name} - {self.price}'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='продукт')
    version_number = models.CharField(max_length=50, verbose_name='номер версии')
    version_name = models.CharField(max_length=250, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='активная версия')

    def __str__(self):
        return f'{self.product} (версия {self.version_number})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('product',)


class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URl')
    contents = models.TextField(verbose_name='содержание')
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_number = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def increase_view_count(self):
        self.views_number += 1
        self.save()

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('name',)

