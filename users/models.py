from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='users/', blank=True)
    phone_number = models.CharField(max_length=15, default='+996')
    gender = models.CharField(max_length=10, choices=GENDER, default='MALE')
    city = models.CharField(max_length=100, default='Бишкек')
    

    birthdate  = models.DateField(null=True, blank=True)
    education  = models.CharField(max_length=200, blank=True)
    experience = models.CharField(max_length=200, blank=True)
    skills     = models.TextField(blank=True)
    about      = models.TextField(blank=True)


    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username
