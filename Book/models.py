from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)                     # Название
    author = models.CharField(max_length=100)                    # Автор
    published_date = models.DateField(null=True, blank=True)     # Дата публикации
    isbn = models.CharField(max_length=13, unique=True)          # ISBN
    pages = models.IntegerField(null=True, blank=True)           # Количество страниц
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)       # Обложка
    file = models.FileField(upload_to='books_files/', null=True, blank=True)    # Файл книги
    description = models.TextField(null=True, blank=True)        # Описание
    publisher_email = models.EmailField(null=True, blank=True)    # Email издателя
    info_url = models.URLField(null=True, blank=True)            # Ссылка на сайт книги
