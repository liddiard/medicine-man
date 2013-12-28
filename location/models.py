from django.db import models


class Site(models.Model):
    domain = models.OneToOneField('router.Domain', related_name='location')
    area = models.CharField(max_length=64)
