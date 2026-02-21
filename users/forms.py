from django import forms
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField
from .models import CustomUser

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)
=======
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )

>>>>>>> 88e1fbe6 (Классные работы)

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    photo = forms.ImageField(required=True)
    phone_number = forms.CharField(max_length=15, initial='+996', required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    city = forms.CharField(max_length=100, required=True)
<<<<<<< HEAD
    birthdate = forms.DateField(required=False)
    education = forms.CharField(max_length=200, required=False)
    experience = forms.CharField(max_length=200, required=False)
    skills = forms.CharField(widget=forms.Textarea, required=False)
    about = forms.CharField(widget=forms.Textarea, required=False)
=======
>>>>>>> 88e1fbe6 (Классные работы)

    class Meta:
        model = CustomUser
        fields = (
<<<<<<< HEAD
            'username', 'password1', 'password2',
            'first_name', 'last_name', 'email', 'photo',
            'phone_number', 'gender', 'city', 'birthdate',
            'education', 'experience', 'skills', 'about'
        )

class CustomLoginForm(AuthenticationForm):
    captcha = CaptchaField()
=======
            'username',
            'password1',
            'password2',
            'photo',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'gender',
            'city'
        )
    
    def save(self, commit = True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
>>>>>>> 88e1fbe6 (Классные работы)
