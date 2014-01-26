from django.db import models


class Site(models.Model):
    domain = models.OneToOneField('router.Domain', related_name='location')
    area = models.CharField(max_length=64)

    def __unicode__(self):
        return self.domain.name


class Artwork(models.Model):
    image = models.ImageField(upload_to='location_artwork')
    title = models.CharField(max_length=64)
    date = models.CharField(max_length=32, blank=True)
    artist = models.CharField(max_length=32, blank=True)
    location = models.CharField(max_length=32, blank=True)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.title
