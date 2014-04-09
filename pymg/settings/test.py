import os
from .common import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


########## INSTALLED APPS CONFIGURATION

INSTALLED_APPS += (
    'django_nose',
    'nose',
)

########## TEST SETTINGS
os.environ['REUSE_DB'] = "1"
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
TEST_DISCOVER_TOP_LEVEL = PROJECT_DIR
TEST_DISCOVER_ROOT = PROJECT_DIR
TEST_DISCOVER_PATTERN = "test_*"
NOSE_ARGS = [
    '--verbosity=2',
    '-x',
    '-d',
    '--with-specplugin',
    '--with-xtraceback',
    '--with-progressive',
]
########## END TEST SETTINGS
