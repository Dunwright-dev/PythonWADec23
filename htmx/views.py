"""htmx Views file."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

# from .models import ()


# Create your htmx views here.

class LandingView(TemplateView):
    template_name = "htmx/_landing.html"