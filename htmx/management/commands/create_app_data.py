from htmx.factories import ArticleFactory
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(100):
            ArticleFactory()
