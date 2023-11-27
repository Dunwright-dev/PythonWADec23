import factory
from faker import Faker
import datetime
from .models import Article

fake = Faker()


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    author = factory.lazy_attribute(lambda x: fake.name())
    title = factory.lazy_attribute(lambda x: fake.sentence(nb_words=10))
    image = factory.lazy_attribute(lambda x: fake.image_url())
    publish_date = factory.lazy_attribute(lambda x: fake.date_this_century())
    content = factory.lazy_attribute(lambda x: fake.paragraphs(nb=2))
