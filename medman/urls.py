from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from location import views as location_views
from content import views as content_views


from router.views import route
admin.autodiscover()

urlpatterns = patterns('',
    
    # pages
    url(r'^$', route, name='main'),

    # api
    url(r'^api/location/place_detail/$', 
        location_views.PlaceDetailView.as_view(), name='place_detail'),
    
    # django/third-party apps
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
