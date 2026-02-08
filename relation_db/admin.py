from django.contrib import admin
from . import  models
admin.site.register(models.Tag)
admin.site.register(models.TouristCategory)
admin.site.register(models.Person)
admin.site.register(models.Register)
admin.site.register(models.Review)