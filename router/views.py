from django.shortcuts import render
from .models import Domain

from location.views import FrontView as LocationFrontView
from content.views import FrontView as ContentFrontView
# Create your views here.

def route (request):
    url = request.META['HTTP_HOST']
    print url
    domain = Domain.objects.get(url=url)
    print domain.kind
    
    if domain.kind == 'lo':
        #send to location app
        return LocationFrontView.as_view()(request, domain.id)
    else: #domain.kind == 'ct'
        return ContentFrontView.as_view()(request, domain.id)
         #send to content app
