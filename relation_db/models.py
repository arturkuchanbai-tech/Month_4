from django.db import models


<<<<<<< HEAD
=======
# Модель отношения many:many
>>>>>>> 88e1fbe6 (Классные работы)
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

<<<<<<< HEAD
class TouristCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Person(models.Model):
    toure = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, blank=True)
    categories = models.ManyToManyField(TouristCategory, blank=True)

    def __str__(self):
        return f"{self.toure}-----{', '.join(i.name for i in self.tags.all())}"


class Register(models.Model):
    person= models.CharField(max_length=100)
    tour = models.OneToOneField(Person ,on_delete=models.CASCADE, related_name='registration')
    
    def __str__(self):
        return f'{self.person} - {self.tour}'


=======


class NumberCar(models.Model):
    nameCar = models.CharField(max_length=100, default='Lexus GX 570')
    nummer_car = models.CharField(max_length=15, default="..KG....")
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return f'{self.nameCar}------{', '.join(i.name for i in self.tags.all() )}'



# Модель отношение 1:1  
class DocumentCar(models.Model):
    choice_car = models.OneToOneField(NumberCar, on_delete=models.CASCADE, related_name='car')
    document = models.CharField(max_length=100)

    def __str__(self):
        return self.document
    
# Модель 1:many
>>>>>>> 88e1fbe6 (Классные работы)
class Review(models.Model):
    MARKS = (
        ('1', '1'),
        ('2', '2'),
<<<<<<< HEAD
        ('3', '3'), 
        ('4', '4'),
        ('5', '5'),
    )
    chois_toure = models.ForeignKey(Person ,on_delete=models.CASCADE, related_name='review')
    text = models.CharField(max_length=100, default='good toure')
    marks = models.CharField(max_length=100, choices=MARKS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Название :{self.chois_toure} - Отценка:{self.marks}: Коммент:{self.text}'
=======
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    choice_car = models.ForeignKey(NumberCar, on_delete=models.CASCADE, related_name='review')
    marks = models.CharField(max_length=100, choices=MARKS, default='5')
    text = models.CharField(max_length=100, default='отличная машина')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Марка:{self.choice_car}-Оценка:{self.marks}-Коммент:{self.text}'
    







    




>>>>>>> 88e1fbe6 (Классные работы)
