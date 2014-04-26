import csv
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from router.models import Domain
from content.models import Site


class Command(BaseCommand):
    args = "<domains.csv>"
    help = "Import content domains"

    def handle(self, *args, **options):
        try:
            filename = args[0]
        except IndexError:
            self.stderr.write('Requires path to a .csv file as an argument')
            return
        num_domains_added = 0
        with open(filename, 'rb') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                with transaction.atomic(): # make transaction succeed or 
                                           # fail as a whole
                    d = Domain(url=row[0], name=row[1], kind='ct')
                    d.save()
                    s = Site(domain=d, body='')
                    s.save()
                num_domains_added += 1
                self.stdout.write('added: %s' % d)
        return "%d domains added" % num_domains_added
