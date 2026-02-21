from django.db import models

<<<<<<< HEAD
class ProgLang(models.Model):
    title = models.CharField(max_length=100, verbose_name='Укажите язык программирования')
    description = models.TextField(verbose_name='Укажите описание языка')
    image = models.ImageField(upload_to='prog_lang/', verbose_name='Загрузите фото')
    created_date_lang = models.PositiveBigIntegerField(verbose_name='Укажите год создания языка программирования', blank=True)
    views =models.PositiveIntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'язык программирования'
        verbose_name_plural ='языки программирования'
=======
created_date_lang = models.PositiveIntegerField(
    verbose_name='укажите год создания языка',
    blank=True,
    null=True  
)

class ProgLang(models.Model):
    #CharField - поле которое отвечает за кол-во символов в форме
    #verbose_name - нужен для пользовательского интерфейса 
    title = models.CharField(max_length=100, verbose_name='укажите язык программирования')
    #TextField - указывает неограничное кол-во символов
    description = models.TextField(verbose_name='укажите описания языка')
    #ImageField - поле для загрузки media картинок - примимает любые виды картинок
    image = models.ImageField(upload_to='proglang/', verbose_name='загрузите фото')
    #PostiveIntergerField - указывает на то что нужно загружать только положительные числа, атрибут blank=True указывает что поле не обязательное для заполнения 
    created_date_lang = models.DateTimeField(auto_now_add=True)
    
    file_python = models.FileField(upload_to='files/', verbose_name='загрузите какой нибудь файл', null=True)

    viki_url = models.URLField(verbose_name='вставьте ссылку с википедии', null=True)

    #DateTimeField - показывает дату и время  auto_now_add=True- подключает к системному времени
    created_at = models.DateTimeField(auto_now_add=True)

    #TODO - изучить поля самостоятельно FileField, URLField, EmailField и еще доп какие найдете
    #!!!! атрибут null=True - дома изучить

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'язык программирования'
        verbose_name_plural = 'языки программирования'
>>>>>>> 88e1fbe6 (Классные работы)
