from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from location import views as location_views
from content import views as content_views


from router.views import route
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', route, name='main'),

    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
