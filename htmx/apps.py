"""htmx Apps file."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppNameConfig(AppConfig):
    """htmx App name config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "htmx"
    verbose_name = _("htmx")
    verbose_name_plural = _("htmxs")
