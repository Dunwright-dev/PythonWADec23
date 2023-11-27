"""htmx Models file."""

from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser

# Create your htmx models here.


class Article(models.Model):
    exclude_fields_from_trigger_audit_log = []

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ["-publish_date"]

    author = models.CharField(
        verbose_name=_("Article Title"),
        max_length=255,
        null=True,
        blank=True,
        unique=False,
    )

    title = models.CharField(
        verbose_name=_("Article Title"),
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )

    image = models.ImageField(
        verbose_name=_("Article Banner"),
        null=True,
        blank=True,
    )

    publish_date = models.DateTimeField(
        verbose_name=_("Publish Date"),
        null=True,
        blank=True,
        help_text=_("Date that the article will be published"),
    )

    content = models.TextField(
        verbose_name=_("Article Content"),
        default="",
        blank=True,
        null=True,
        # null=False,
    )

    def __str__(self):
        return self.title
