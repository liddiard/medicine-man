from .base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}

DEFAULT_FILE_STORAGE = 'medman.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'medman.s3utils.StaticRootS3BotoStorage'
S3_URL = "http://%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME

STATIC_URL = S3_URL + 'static/'
MEDIA_URL = S3_URL + 'media/'

DOKKU_PATH = "/usr/local/bin/dokku"
