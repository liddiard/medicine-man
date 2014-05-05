from django.contrib import admin
from .models import Site, Image


class SiteAdmin(admin.ModelAdmin):
    list_display = ('domain',)
    search_fields = ['domain__name', 'domain__url']


admin.site.register(Site, SiteAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'caption')
    list_display_links = ('id', 'image')
    readonly_fields = ('id',)


admin.site.register(Image, ImageAdmin)
