from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'brandon'  # Replace with a secure key in production

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'staticfiles'
