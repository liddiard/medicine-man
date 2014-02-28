import urllib2
import json

from django.http import HttpResponse
from django.views.generic import TemplateView

from router.models import Domain
from .models import Site, Artwork


class FrontView(TemplateView):

    template_name = "location/front.html"

    def get(self, request, **kwargs):
        domain = self.kwargs['domain']
        context = self.get_context_data()
        try:
            context['site'] = Site.objects.get(domain=domain)
        except Site.DoesNotExist:
            domain_name = Domain.objects.get(id=domain)
            return self.site_dne_error(domain_name)
        context['gallery'] = Artwork.objects.order_by('?')
        return self.render_to_response(context)

    def site_dne_error(self, domain_name):
        error_msg = '''
            A location Site object matching this domain does not exist. If 
            you're the administrator of this site, you can fix this by adding 
            a location Site with "%s" as the domain.
        '''
        return HttpResponse(error_msg % domain_name, content_type='text/plain')

def textToCoordinant(location):
    latitude = ""
    longitude = ""
    locationSearch = location
    locationUrl = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % locationSearch
    #print locationUrl
    response = urllib2.urlopen(locationUrl)
    data = json.load(response)
    latitude = data["results"][0]["geometry"]["location"]["lat"]
    longitude = data["results"][0]["geometry"]["location"]["lng"]
    return latitude, longitude

def coordinantToNearby(latitude, longitude):
    location = "%s,%s" %(latitude, longitude)
    types = 'art_gallery'
    nearbyUrl = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=50000&types=%s&sensor=false&key=AIzaSyB6R31HHidq6Dm6qf6g1-c8iAKiadHq33o' %(location, types)
    response = urllib2.urlopen(nearbyUrl)
    data = json.load(response)
    print data


#coordinantToNearby(textToCoordinant('Boston+MA')[0],textToCoordinant('Boston+MA')[1])
