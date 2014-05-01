# the following method of dynamically updating settings at runtime
# is per the suggestion of http://stackoverflow.com/a/16111968/2487925

import os

from django.db import DatabaseError
from django.conf import settings

from .models import Domain

if not os.environ.get('LOCAL_ENV'):
    try:
        settings.ALLOWED_HOSTS = [domain.url for domain in Domain.objects.all()]
    except DatabaseError: # new project / database table doesn't exist yet
        settings.ALLOWED_HOSTS = []

    # make sure we could still access the admin domain even if the db were reset
    if settings.ADMINISTRATIVE_DOMAIN not in settings.ALLOWED_HOSTS:
        settings.ALLOWED_HOSTS.append(settings.ADMINISTRATIVE_DOMAIN)
