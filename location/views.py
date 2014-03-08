import json
import urllib
import urllib2

from django.http import HttpResponse
from django.views.generic import TemplateView

from router.models import Domain
from .models import Site, Artwork


# pages

class FrontView(TemplateView):

    template_name = "location/front.html"

    def get(self, request, **kwargs):
        domain = self.kwargs['domain']
        context = self.get_context_data()
        try:
            site = Site.objects.get(domain=domain)
        except Site.DoesNotExist:
            domain_name = Domain.objects.get(id=domain)
            return self.site_dne_error(domain_name)
        else:
            context['site'] = site
        context['gallery'] = Artwork.objects.order_by('?')
        coordinant = string_to_coordinant(site.area)
        coordinant_to_nearby(coordinant)
        return self.render_to_response(context)

    def site_dne_error(self, domain_name):
        error_msg = '''
            A location Site object matching this domain does not exist. If 
            you're the administrator of this site, you can fix this by adding 
            a location Site with "%s" as the domain.
        '''
        return HttpResponse(error_msg % domain_name, content_type='text/plain')


# utility functions

def string_to_coordinant(area):
    area_clean = urllib.quote_plus(area)
    q = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % area_clean
    response = urllib2.urlopen(q)
    data = json.load(response)
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    return latitude, longitude

def coordinant_to_nearby(coordinant):
    point = "%s,%s" % (coordinant[0], coordinant[1])
    kind = "art_gallery"
    q = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=50000&types=%s&sensor=false&key=AIzaSyB6R31HHidq6Dm6qf6g1-c8iAKiadHq33o" % (point, kind)
    response = urllib2.urlopen(q)
    data = json.load(response)
    print data

