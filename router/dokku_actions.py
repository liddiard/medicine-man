import os
from subprocess import call

from django.conf import settings

def add_domain(name):
    """
    This is a dokku-specific function. It won't do anything in development.
    Requires dokku domains plugin: 
    https://github.com/wmluke/dokku-domains-plugin
    """
    if os.environ.get('LOCAL_ENV'):
        return
    from .models import Domain
    domains = " ".join([domain.url for domain in Domain.objects.all()])
    domains += " " + name
    cmd = "%s domains:set %s %s" % (settings.DOKKU_PATH, 
                                    settings.ADMINISTRATIVE_DOMAIN, domains)
    call(cmd, shell=True) 
