from .base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': dj_database_url.config()
}

STATIC_URL = S3_URL + 'static/'
MEDIA_URL = S3_URL + 'media/'
