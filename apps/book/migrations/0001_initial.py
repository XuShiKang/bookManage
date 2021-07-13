# Generated by Django 2.2.9 on 2020-05-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='书名')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('publisher', models.CharField(max_length=50, verbose_name='出版社')),
                ('date', models.DateField(verbose_name='年份')),
                ('amount', models.IntegerField(default=0, verbose_name='藏书量')),
                ('ISBN', models.CharField(blank=True, max_length=50, verbose_name='ISBN')),
            ],
            options={
                'verbose_name': '书籍',
                'verbose_name_plural': '书籍',
            },
        ),
    ]