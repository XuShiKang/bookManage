from django.db import models
from apps.book.models import Book
import pytz
from datetime import datetime
from bookManage.settings import TIME_ZONE

types = [
    (0, '学生'),
    (1, '老师')
]

# Create your models here.
class User(models.Model):
    name = models.CharField('姓名', max_length=50)
    # college = models.CharField('学院', max_length=50)
    major = models.CharField('专业', max_length=50)
    studentID = models.CharField('学号', max_length=20)
    createTime = models.DateField('注册时间', auto_created=True)
    type = models.IntegerField('身份', choices=types,default=0)
    phone = models.CharField('联系方式', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Borrow(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL,verbose_name='借阅人',null=True)
    borrowBook = models.ForeignKey(Book, on_delete=models.SET_NULL,verbose_name='借阅书名', null=True)
    createTime = models.DateTimeField('借阅时间',auto_created=True)
    returnTime = models.DateTimeField('归还时间', blank=True, null=True)
    limitTime = models.IntegerField('借阅时长',default=30)

    def __str__(self):
        return f"{self.borrower.name}=>{self.borrowBook.name}"

    def isOverdue(self):
        if self.returnTime:
            now = self.returnTime
        else:
            now = datetime.now()
        now = now.replace(tzinfo=pytz.timezone(TIME_ZONE))
        return (now - self.createTime).days > self.limitTime

    class Meta:
        verbose_name = '借阅表'
        verbose_name_plural = verbose_name