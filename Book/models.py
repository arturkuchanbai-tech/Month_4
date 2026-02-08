from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)               
    author = models.CharField(max_length=100)                  
    published_date = models.DateField(null=True, blank=True)     
    isbn = models.CharField(max_length=13, unique=True)          
    pages = models.IntegerField(null=True, blank=True)           
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)       
    file = models.FileField(upload_to='books_files/', null=True, blank=True)   
    description = models.TextField(null=True, blank=True)      
    publisher_email = models.EmailField(null=True, blank=True)  
    info_url = models.URLField(null=True, blank=True)           
