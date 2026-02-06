from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

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


class Review(models.Model):
    MARKS = (
        ('1', '1'),
        ('2', '2'),
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