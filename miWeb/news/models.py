from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    description = models.TextField('Текст')
    author = models.CharField('Автор', max_length=20)
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/news'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'