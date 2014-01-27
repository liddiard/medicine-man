from django.db import models
from tinymce.models import HTMLField


class Site(models.Model):
    domain = models.OneToOneField('router.Domain', related_name='content')
    body = HTMLField()

    def __unicode__(self):
        return self.domain.name


class Image(models.Model):
    image = models.ImageField(upload_to='content_images')
    caption = models.TextField(blank=True)

    def __unicode__(self):
        return unicode(self.image)
