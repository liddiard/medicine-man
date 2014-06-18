from subprocess import call

from django.conf import settings

from .models import Domain


def add_domain(name):
    """
    This is a dokku-specific function. It won't do anything in development.
    """
    if settings.LOCAL_ENV:
        return
    domains = " ".join([domain.url for domain in Domain.objects.all()])
    domains += " " + name
    cmd = "dokku domains:set %s %s" % (settings.ADMINISTRATIVE_DOMAIN, domains)
    call([cmd]) 
