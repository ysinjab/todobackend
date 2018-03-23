from base import *
import os

# Disable debug
if os.environ.get('DEBUG'):
  DEBUG = True
else:
  DEBUG = False

# Must be explicitly specified when Debug is disabled
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS', '*')]

# Database settings
DATABASES = {

        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('D_NAME','todobackend'),
        'USER': os.environ.get('D_USER','root'),
        'PASSWORD': os.environ.get('D_PASSWORD','123'),
        'HOST': os.environ.get('D_HOST','0.0.0.0'),
        'PORT': os.environ.get('D_PORT','5432'),
    }
}

STATIC_ROOT = os.environ.get('STATIC_ROOT', '/var/www/todobackend/static')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/var/www/todobackend/media')