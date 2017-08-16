from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'medica_online',
      'USER': 'admin_medika',
      'PASSWORD':'12345',
      'HOST':'localhost',
      'PORT':'5432'
  }
}