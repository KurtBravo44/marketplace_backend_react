from django.conf import settings
from django.db import models
from django.utils import timezone

from users.models import NULLABLE, User


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=100, default='продаю', verbose_name='название')
    price = models.IntegerField(default=0, verbose_name='цена')
    image = models.ImageField(upload_to='ads/', verbose_name='изображение', **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)
    text = models.TextField(verbose_name='текст', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время', **NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='объявление', **NULLABLE)

    def __str__(self):
        return f'{self.author} #{self.pk}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'коммантарии'