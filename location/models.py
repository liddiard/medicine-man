from django.db import models


class Site(models.Model):
    domain = models.OneToOneField('router.Domain', related_name='location')
    area = models.CharField(max_length=64)
    area.help_text = '''
        Should be in the form <strong>city, state</strong> (e.g. Santa Fe, NM) 
        or <strong>city, country</strong> (e.g. Vienna, Austria)
    '''

    def __unicode__(self):
        return self.domain.name


class Artwork(models.Model):
    image = models.ImageField(upload_to='location_artwork')
    image.help_text = '''
        For best display, artwork should be between 1280x720 and 1920x1080 
        pixels.
    '''
    title = models.CharField(max_length=64)
    date = models.CharField(max_length=32, blank=True)
    date.help_text = "Time period created (e.g. 1920, September 1888, circa 1250)"
    artist = models.CharField(max_length=32, blank=True)
    location = models.CharField(max_length=32, blank=True)
    location.help_text = "Current location of this piece (optional)"
    url = models.URLField(blank=True)
    url.help_text = "Page to which to link a 'View Item' button (optional)"

    def __unicode__(self):
        return self.title
