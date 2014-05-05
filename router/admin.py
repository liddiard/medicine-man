from django.contrib import admin
from .models import Domain


class DomainAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'kind')
    search_fields = ['name', 'url']


admin.site.register(Domain, DomainAdmin)
