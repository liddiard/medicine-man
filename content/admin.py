from django.contrib import admin
from .models import Site, Image


class SiteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Site, SiteAdmin)


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)
