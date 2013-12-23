from django.conf.urls import patterns, include, url
from django.contrib import admin

from location import views as location_views
from content import views as content_views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', location_views.FrontView.as_view(), name='front'),

    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
