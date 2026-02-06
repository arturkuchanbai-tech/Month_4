from django.db import models

class Proglang(models.Model):
    title = models.CharField(max_length=100, verbose_name='Укажите язык программирования')
    description = models.TextField(verbose_name='Укажите описание языка')
    image = models.ImageField(upload_to='prog_lang/', verbose_name='Загрузите фото')
    created_date_lang = models.PositiveBigIntegerField(verbose_name='Укажите год создания языка программирования', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'язык программирования'
        verbose_name_plural ='языки программирования'
