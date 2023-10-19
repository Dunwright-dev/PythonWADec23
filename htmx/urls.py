"""htmx Url's file."""

from django.urls import include, path

from .views import (LandingView)

urlpatterns = [
    path("", LandingView.as_view(), name="landing")
]
