from django.contrib import admin
from .models import Site, Artwork


class SiteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Site, SiteAdmin)


class ArtworkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artwork, ArtworkAdmin)
