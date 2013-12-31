from django.db import models

class Domain(models.Model):
    url = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    LOCATION = 'lo'
    CONTENT = 'ct'
    KIND_CHOICES = ((LOCATION, 'location'), (CONTENT, 'content'))
    kind = models.CharField(max_length=2, choices=KIND_CHOICES, 
                            default=LOCATION)
    
    def __unicode__(self):
        return "%s (%s)" % (self.name, self.url) 
