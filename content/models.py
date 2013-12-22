from django.db import models


class Site(models.Model):
    domain = models.OneToOneField('router.Domain', related_name='content')
    body = models.TextField()


class Image(models.Model):
    image = models.ImageField(upload_to='img')
