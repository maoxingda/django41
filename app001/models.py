from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField('姓名', max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('书名', max_length=128)
    author = models.ForeignKey(Author, verbose_name='作者', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
