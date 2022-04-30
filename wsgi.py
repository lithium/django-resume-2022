"""
WSGI config for mainsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application


BASE_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(BASE_DIR, 'src'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainsite.settings')

application = get_wsgi_application()
