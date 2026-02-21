from django.contrib import admin
<<<<<<< HEAD
from . import  models
admin.site.register(models.Tag)
admin.site.register(models.TouristCategory)
admin.site.register(models.Person)
admin.site.register(models.Register)
=======
from . import models

admin.site.register(models.Tag)
admin.site.register(models.NumberCar)
admin.site.register(models.DocumentCar)
>>>>>>> 88e1fbe6 (Классные работы)
admin.site.register(models.Review)