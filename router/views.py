from django.http import HttpResponse
from .models import Domain

from location.views import FrontView as LocationFrontView
from content.views import FrontView as ContentFrontView

domain_dne_msg = '''
    A Domain object matching this website does not exist. If you're the 
    administrator of this website, you can fix this by adding a Domain with
    the URL "%s".
'''

def route(request):
    host = request.META['HTTP_HOST']
    try:
        domain = Domain.objects.get(url=host)
    except Domain.DoesNotExist:
        return HttpResponse(domain_dne_msg % host, content_type='text/plain')
    if domain.kind == 'lo':
        # send to location app
        return LocationFrontView.as_view()(request, domain=domain.id)
    else: # domain is a content domain
        # send to content app
        return ContentFrontView.as_view()(request, domain=domain.id)
