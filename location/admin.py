from django.contrib import admin
from .models import Site, Artwork


class SiteAdmin(admin.ModelAdmin):
    list_display = ('domain', 'area')
    search_fields = ['domain__name', 'domain__url']


admin.site.register(Site, SiteAdmin)


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'url')


admin.site.register(Artwork, ArtworkAdmin)
