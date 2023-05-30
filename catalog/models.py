from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=500, verbose_name='описание')
    category = models.CharField(max_length=150, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateTimeField(verbose_name='дата создания')
    last_change_date = models.DateTimeField(verbose_name='дата последнего изменения')
    preview = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)

