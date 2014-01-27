import re

from django import template
from django.template.defaultfilters import stringfilter
from django.conf.settings import MEDIA_URL

from content.models import Image

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def shortcode(value):
    img = r'\[img(?P<pk>\d+)\s*(?P<display>\S+)?\]'
    return re.sub(img, imgHTML, value)

def imgHTML(match):
    try:
        image = Image.objects.get(pk=match.group('pk'))
    except Image.DoesNotExist:
        return "" # IDEA: don't fail silently?
    given_display = match.group('display')
    # IDEA: check if given_display is in a list of valid dispaly options.
    # If not, assign it to default value.
    # Would prevent users from assigning any css class they want.
    display = given_display if given_display is not None else "fullwidth"
    params = {'display': display,
              'MEDIA_URL': MEDIA_URL,
              'filename': image.image,
              'author': image.author,
              'caption': image.caption
    }
    organization = image.author.organization
    if organization:
        params['organization'] = " / %s" % organization
    else:
        params['organization'] = ""
    return '''
           <figure class="%(display)s">
               <img src="%(MEDIA_URL)s%(filename)s"/>
               <figcaption>%(caption)s</figcaption>
           </figure>
           ''' % params
