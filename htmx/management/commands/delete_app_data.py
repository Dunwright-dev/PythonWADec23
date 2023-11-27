from htmx.models import Article
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        models = [Article]
        for m in models:
            m.objects.all().delete()
