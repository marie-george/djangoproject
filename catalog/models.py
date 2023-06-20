from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    author = models.CharField(max_length=150, verbose_name='автор')
    description = models.CharField(max_length=500, verbose_name='описание')
    category = models.CharField(max_length=150, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateField(verbose_name='дата создания')
    last_change_date = models.DateField(verbose_name='дата последнего изменения')
    preview = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=500, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URl')
    contents = models.CharField(max_length=500, verbose_name='описание')
    creation_date = models.DateField(verbose_name='дата создания')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_number = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('name',)