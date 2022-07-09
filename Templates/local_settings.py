DEBUG = "True"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio',
        'USER': 'jarvis',
        'PASSWORD': 'q#JX6zy#AxbhEid$',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
ALLOWED_HOSTS = ['*']

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = '/uploads'
