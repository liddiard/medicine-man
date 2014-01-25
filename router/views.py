from django.shortcuts import render
from .models import Domain

from location.views import FrontView as LocationFrontView
from content.views import FrontView as ContentFrontView

def route(request):
    url = request.META['HTTP_HOST']
    domain = Domain.objects.get(url=url)
    if domain.kind == 'lo':
        # send to location app
        return LocationFrontView.as_view()(request, domain.id)
    else: # domain is a content domain
        # send to content app
        return ContentFrontView.as_view()(request, domain.id)
