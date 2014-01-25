from django.db import models


class Site(models.Model):
    domain = models.OneToOneField('router.Domain', related_name='location')
    area = models.CharField(max_length=64)

    def __unicode__(self):
        return self.domain


class Artwork(models.Model):
    image = models.ImageField(upload_to='/')
    title = models.CharField(max_length=64)
    date = models.CharField(max_length=32)
    artist = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    url = models.URLField()

    def __unicode__(self):
        return self.title
