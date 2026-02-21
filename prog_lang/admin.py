from django.contrib import admin
from .models import ProgLang

admin.site.register(ProgLang)

from . import models

admin.site.register(models.ProgLang)
