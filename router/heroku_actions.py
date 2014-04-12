import os
from requests.exceptions import HTTPError
import heroku

from django.conf import settings


def add_domain(name):
    heroku_email = settings.HEROKU_EMAIL
    heroku_pass = settings.HEROKU_PASSWORD
    cloud = heroku.from_pass(heroku_email, heroku_pass)
    app = cloud.apps[settings.HEROKU_APP_NAME]
    domain = app.domains
    try:
        domain.add(name)
    except HTTPError:
        pass # NOTICE: silencing error
