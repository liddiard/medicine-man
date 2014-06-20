from tinymce.models import HTMLField
from PIL import Image as PyImage

from django.core.files.storage import default_storage as storage
from django.db import models

from router.models import ClearCacheOnSaveModel


class Site(ClearCacheOnSaveModel):
    domain = models.OneToOneField('router.Domain', related_name='content')
    body = HTMLField()
    body.help_text = '''
        To embed an image: <strong>[img{id}]</strong> (e.g. [img2]). By 
        default, images display full width. To float an image to the right
        or left of the text, add "left" or "right" (e.g. 
        [img35 <strong>right</strong>]).<br/>
        To embed a youtube video: 
        <strong>[youtube]{youtube share link}[/youtube]</strong> (e.g. 
        [youtube]http://youtu.be/VU_2R1rjbD8[/youtube]).
    '''

    def __unicode__(self):
        return self.domain.name


class Image(ClearCacheOnSaveModel):
    image = models.ImageField(upload_to='content_images')
    image.help_text = '''
        For best display, images should be greater than or equal to 640  
        pixels wide. Images are automatically resized on upload.
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
            file_storage = storage.open(self.image.name, 'w')
            image.save(file_storage, 'JPEG')
            file_storage.close()
        else:
            super(Image, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_image = self.image

    def __unicode__(self):
        return unicode(self.image)
