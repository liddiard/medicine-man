# the following method of dynamically updating settings at runtime
# is per the suggestion of http://stackoverflow.com/a/16111968/2487925

from django.conf import settings
from .models import Domain

settings.ALLOWED_HOSTS = [domain.url for domain in Domain.objects.all()]

# make sure we could still access the admin domain even if the db were reset
if settings.ADMINISTRATIVE_DOMAIN not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS.append(settings.ADMINISTRATIVE_DOMAIN)
