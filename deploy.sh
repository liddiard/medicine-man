yes "yes" | python manage.py collectstatic --settings=medman.settings.prod && git push heroku master
