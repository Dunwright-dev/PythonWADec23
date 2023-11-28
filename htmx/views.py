"""htmx Views file."""
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
)
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from core.views.generic.base import HtmxTemplateView, HtmxTemplateResponseMixin
from core.views.generic.list import HtmxListView
from core.views.generic.edit import HtmxCreateView, HtmxDeleteView, HtmxUpdateView

from .models import Article
from users.forms import CustomUserForm
from users.models import CustomUser

# from .models import ()


# Create your htmx views here.


class LandingView(TemplateView):
    template_name = "htmx/1.html"


class TwoView(TemplateView):
    template_name = "htmx/2.html"


class ThreeView(TemplateView):
    template_name = "htmx/3.html"


class FourView(TemplateView):
    template_name = "htmx/4.html"


class FiveView(TemplateView):
    template_name = "htmx/5.html"


class SixView(TemplateView):
    template_name = "htmx/6.html"


class SevenView(TemplateView):
    template_name = "htmx/7.html"


class EightView(TemplateView):
    template_name = "htmx/8.html"


class NineView(HtmxTemplateView):
    template_name = "htmx/partials/9.html"
    htmx_template_name = "htmx/partials/9.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Paginator(Article.objects.all(), 9)
        context["articles"] = p.page(self.kwargs.get("page"))
        context["article_count"] = Article.objects.all().count()
        return context


class TenView(HtmxTemplateView):
    template_name = "htmx/partials/10.html"
    htmx_template_name = "htmx/partials/10.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Paginator(Article.objects.all(), 9)
        context["articles"] = p.page(self.kwargs.get("page"))
        context["article_count"] = Article.objects.all().count()
        return context


class ElevenView(HtmxTemplateView):
    template_name = "htmx/partials/11.html"
    htmx_template_name = "htmx/partials/11.html"

    def post(self, request, *args, **kwargs):
        q = request.POST["search"]
        context = self.get_context_data(**kwargs)

        if q:
            # Create a list of words with all spaces stripped.
            q_stripped = q.strip().split(" ")
            list_of_words = list(filter(lambda x: x != "", q_stripped))

            # This creates a chained Search, eg SearchQuery() and SearchQuery and SearchQuery()
            # Each word in the list has its own query.
            compound_query = SearchQuery(f"{list_of_words[0]}:*", search_type="raw")
            for word in list_of_words[1:]:
                compound_query = compound_query & SearchQuery(
                    f"{word}:*", search_type="raw"
                )

            vector = SearchVector(
                "title",
                "content",
                "author",
            )

            locations = (
                Article.objects.annotate(
                    search=vector, rank=SearchRank(vector, compound_query)
                )
                .filter(
                    search=compound_query,
                )
                .order_by("-rank")
            )

            context["articles"] = locations

        return render(request, "htmx/partials/11_results.html", context=context)


class TwelveView(HtmxTemplateView):
    template_name = "htmx/partials/12.html"
    htmx_template_name = "htmx/partials/12.html"


class TwelveListView(HtmxListView):
    template_name = "htmx/partials/12_list.html"
    htmx_template_name = "htmx/partials/12_list.html"
    model = CustomUser
    context_object_name = "users"


class TwelveCreateView(HtmxCreateView):
    template_name = "htmx/partials/12_create.html"
    htmx_template_name = "htmx/partials/12_create.html"
    model = CustomUser
    form_class = CustomUserForm
    success_url = reverse_lazy("landing")

    def form_valid(self, form):
        self.object = form.save()
        hx_trig = {
            "notify": {
                "type": "success",
                "content": "User Created Successfully",
            },
            "update": {},
        }
        return HttpResponse(
            status=204,
            headers={"HX-Trigger": json.dumps(hx_trig)},
        )


class TwelveCreateGroupDropdownView(HtmxTemplateView):
    template_name = "htmx/partials/12_group_dropdown.html"
    htmx_template_name = "htmx/partials/12_group_dropdown.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department = self.request.GET.get("department")
        options = []
        if department == "Corporate":
            options = ["Leadership", "Legal", "Accounting", "HR"]
        elif department == "Developer":
            options = ["Front End", "Back End"]
        elif department == "Sales":
            options = ["Metro", "Regional", "International"]
        context["options"] = options
        return context


class TwelveUpdateView(HtmxUpdateView):
    template_name = "htmx/partials/12_update.html"
    htmx_template_name = "htmx/partials/12_update.html"
    model = CustomUser
    form_class = CustomUserForm
    success_url = reverse_lazy("landing")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options = []
        print(self.kwargs["pk"])
        user = CustomUser.objects.get(id=self.kwargs["pk"])
        if user.department == "Corporate":
            options = ["Leadership", "Legal", "Accounting", "HR"]
        elif user.department == "Developer":
            options = ["Front End", "Back End"]
        elif user.department == "Sales":
            options = ["Metro", "Regional", "International"]
        context["options"] = options
        context["team"] = user.team
        context["user_id"] = user.id
        return context

    def form_valid(self, form):
        self.object = form.save()
        hx_trig = {
            "notify": {
                "type": "success",
                "content": "User Updated Successfully",
            },
            "update": {},
        }
        return HttpResponse(
            status=204,
            headers={"HX-Trigger": json.dumps(hx_trig)},
        )


class TwelveDeleteView(HtmxDeleteView):
    template_name = "htmx/partials/12_list.html"
    htmx_template_name = "htmx/partials/12_list.html"
    model = CustomUser
    context_object_name = "users"

    def delete(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=self.kwargs["pk"])
        user.delete()
        return HttpResponse(
            status=200,
            headers={"HX-Trigger": "update"},
        )



class ThirteenView(HtmxTemplateView):
    template_name = "htmx/partials/13.html"
    htmx_template_name = "htmx/partials/13.html"



class FourteenView(HtmxTemplateView):
    template_name = "htmx/14.html"
    htmx_template_name = "htmx/14.html"
