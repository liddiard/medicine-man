from django.db import models
from tinymce.models import HTMLField


class Site(models.Model):
    domain = models.OneToOneField('router.Domain', related_name='content')
    body = HTMLField()


class Image(models.Model):
    image = models.ImageField(upload_to='img')
