<<<<<<< HEAD
# main/wsgi.py
import os
=======
"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

>>>>>>> 88e1fbe6 (Классные работы)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_wsgi_application()
