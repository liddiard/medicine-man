from django.db import models
from .heroku_actions import add_domain

class Domain(models.Model):
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

    def save(self, *args, **kwargs):
        if self.pk is None:
            add_domain(self.url)
        super(Domain, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return "%s (%s)" % (self.name, self.url) 
