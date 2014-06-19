from django.core.management.base import BaseCommand, CommandError

from router.models import Domain


class Command(BaseCommand):

    def handle(self, *args, **options):
        return " ".join([domain.url for domain in Domain.objects.all()])
