import dj_database_url
from .base import *
import os

#cambiar estos valores por los de abajo
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = dict()

DATABASES['default'] = dj_database_url.config()

STATIC_ROOT = os.path.join(os.getcwd(),'static')

#la base de datos como la tenemos en production
'''
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'good_db',
      'USER': 'admin_good',
      'PASSWORD':'12345',
      'HOST':'localhost',
      'PORT':'5432'
  }
}

'''