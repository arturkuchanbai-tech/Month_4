from django.db import models

class Proglang(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.name
