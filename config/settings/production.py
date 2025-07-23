from .base import *

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com']

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'brandon')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'staticfiles'
