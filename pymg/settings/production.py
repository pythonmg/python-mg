from .common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pythonmg',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = '/home/deploy/www/pugmg/static/'
STATIC_URL = '/static/'

MEDIA_ROOT = '/home/deploy/www/pugmg/media/'
MEDIA_URL = '/media/'
