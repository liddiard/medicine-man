from django.db import models
from django.core.cache import cache


class ClearCacheOnSaveModel(models.Model):
    
    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        cache.clear()
        super(ClearCacheOnSaveModel, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        cache.clear()
        super(ClearCacheOnSaveModel, self).save(*args, **kwargs)


class Domain(ClearCacheOnSaveModel):
    url = models.CharField(max_length=64, unique=True)
    url.help_text = "Actual name of this domain (e.g. bostonartgallery.com)"
    name = models.CharField(max_length=64)
    name.help_text = "Name to display on the site (e.g. Boston Art Gallery)"
    LOCATION = 'lo'
    CONTENT = 'ct'
    KIND_CHOICES = ((LOCATION, 'location'), (CONTENT, 'content'))
    kind = models.CharField(max_length=2, choices=KIND_CHOICES, 
                            default=LOCATION)
    kind.help_text = '''
        What type of site should this domain be? <br/>Be sure to create the 
        corresponding <a href="../../../location/site/add/">location site</a> 
        or <a href="../../../content/site/add/">content site</a>.
    '''
    
    def __unicode__(self):
        return "%s (%s)" % (self.name, self.url) 
