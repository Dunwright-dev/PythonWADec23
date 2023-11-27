# Generated by Django 4.2.5 on 2023-11-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Article Title"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="",
                        verbose_name="Article Banner",
                    ),
                ),
                (
                    "publish_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="Date that the article will be published",
                        null=True,
                        verbose_name="Publish Date",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True,
                        default="",
                        null=True,
                        verbose_name="Article Content",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
                "ordering": ["-publish_date"],
            },
        ),
    ]
