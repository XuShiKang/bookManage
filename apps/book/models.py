from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField('书名', max_length=50)
    author = models.CharField('作者', max_length=50)
    publisher = models.CharField('出版社', max_length=50)
    date = models.DateField('年份')
    amount = models.IntegerField('藏书量', default=0)
    ISBN = models.CharField('ISBN', blank=True, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

