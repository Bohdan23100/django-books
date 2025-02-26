from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='static/img/authors/')
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    desc = models.TextField()
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Book(models.Model):
    name = models.CharField(max_length=100,null=False,unique=True)
    desc = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=False)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = False)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='static/img/books/')
    stock = models.PositiveIntegerField(default=0)
    total_sold = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


