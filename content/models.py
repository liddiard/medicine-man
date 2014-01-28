from django.db import models
from tinymce.models import HTMLField
from PIL import Image as PyImage


class Site(models.Model):
    domain = models.OneToOneField('router.Domain', related_name='content')
    body = HTMLField()

    def __unicode__(self):
        return self.domain.name


class Image(models.Model):
    image = models.ImageField(upload_to='content_images')
    image.help_text = '''
        For best results, images should be greater than or equal to 640  
        pixels wide. The image will be automatically resized on upload.
    '''
    caption = models.TextField(blank=True)

    __original_image = None

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        self.__original_image = self.image

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.image != self.__original_image:
            size = 640, 1280
            super(Image, self).save(force_insert, force_update, *args, **kwargs)
            image = PyImage.open(self.image)
            image.thumbnail(size, PyImage.ANTIALIAS)
            image.save(self.image.path)
        else:
            super(Image, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_image = self.image

    def __unicode__(self):
        return unicode(self.image)
