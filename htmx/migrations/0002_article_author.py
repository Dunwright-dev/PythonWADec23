# Generated by Django 4.2.5 on 2023-11-23 19:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("htmx", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="author",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Article Title"
            ),
        ),
    ]