import json
import urllib
import urllib2
from urlparse import urlparse

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View, TemplateView

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
        context['places'] = self.format_places(site.area)
        return self.render_to_response(context)

    def site_dne_error(self, domain_name):
        error_msg = '''
            A location Site object matching this domain does not exist. If 
            you're the administrator of this site, you can fix this by adding 
            a location Site with "%s" as the domain.
        '''
        return HttpResponse(error_msg % domain_name, content_type='text/plain')

    def format_places(self, area):
        limit = 4
        places_data = string_to_nearby(area)
        places_results = places_data['results']
        places = []
        for place in places_results[:limit]:
            photo = reference_to_photo(place['photos'][0]['photo_reference'])
            places.append({
                'reference': place['reference'],
                'name': place['name'],
                'address': place['vicinity'],
                'rating': place.get('rating'),
                'coordinates': (place['geometry']['location']['lat'], 
                                place['geometry']['location']['lng']),
                'photo': photo
            })
        return places


# abstract base classes

class AjaxView(View):

    def json_response(self, **kwargs):
        return HttpResponse(json.dumps(kwargs), content_type="application/json")

    def success(self, **kwargs):
        return self.json_response(result=0, **kwargs)

    def error(self, error, message):
        return self.json_response(result=1, error=error, message=message) 

    def key_error(self, message):
        return self.error("KeyError", message)


# api

class PlaceDetailView(AjaxView):

    def get(self, request):
        reference = request.GET.get('reference')
        if reference is None:
            return self.key_error('Required key "reference" not found in '
                                  'request.')
        q = ('https://maps.googleapis.com/maps/api/place/details/json?'
             'reference=%s&sensor=false&key=%s') % (reference, 
                                                    settings.GOOGLE_API_KEY)
        response = urllib2.urlopen(q).read()
        result = json.loads(response)['result']
        map_image = coordinant_to_map(result['geometry']['location']['lat'], 
                                      result['geometry']['location']['lng'])
        website = result.get('website')
        if website:
            host = urlparse(website).netloc
        else:
            host = None
        detail = {
            'address': result.get('vicinity'),
            'phone': result.get('formatted_phone_number'),
            'url': website,
            'host': host,
            'rating': result.get('rating'),
            'open_hours': result.get('open_hours'),
            'map': map_image
        }
        return self.success(detail=detail)


# utility functions

def string_to_coordinant(area):
    '''takes a location string and returns a lat/long tuple'''
    area_clean = urllib.quote_plus(area)
    q = ('http://maps.googleapis.com/maps/api/geocode/json?address=%s'
         '&sensor=false') % area_clean
    response = urllib2.urlopen(q)
    data = json.load(response)
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    return latitude, longitude

def coordinant_to_nearby(coordinant):
    '''takes a tuple of lat/long coords and returns a dict of nearby places'''
    point = "%s,%s" % coordinant
    kind = "art_gallery"
    q = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
         'location=%s&radius=50000&types=%s&sensor=false'
         '&key=%s') % (point, kind, settings.GOOGLE_API_KEY)
    response = urllib2.urlopen(q)
    data = json.load(response)
    return data

def string_to_nearby(area):
    return coordinant_to_nearby(string_to_coordinant(area))

def reference_to_photo(ref):
    q = ('https://maps.googleapis.com/maps/api/place/photo?maxwidth=200'
         '&photoreference=%s&sensor=false&key=%s') % (ref, 
                                                      settings.GOOGLE_API_KEY)
    return q

def coordinant_to_map(lat, lng):
    q = ('http://maps.googleapis.com/maps/api/staticmap?markers=%s,%s'
         '&size=268x179&zoom=13&sensor=false' % (lat, lng))
    return q
