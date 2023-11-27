"""htmx Url's file."""

from django.urls import include, path

from .views import (
    LandingView,
    TwoView,
    ThreeView,
    FourView,
    FiveView,
    SixView,
    SevenView,
    EightView,
    NineView,
    TenView,
    ElevenView,
    TwelveView,
    TwelveCreateView,
    TwelveCreateGroupDropdownView,
    TwelveListView,
    TwelveUpdateView,
    TwelveDeleteView,
    ThirteenView,
    FourteenView,
)

urlpatterns = [
    path("", LandingView.as_view(), name="1"),
    path("2/", TwoView.as_view(), name="2"),
    path("3/", ThreeView.as_view(), name="3"),
    path("4/", FourView.as_view(), name="4"),
    path("5/", FiveView.as_view(), name="5"),
    path("6/", SixView.as_view(), name="6"),
    path("7/", SevenView.as_view(), name="7"),
    path("8/", EightView.as_view(), name="8"),
    path("9/<int:page>", NineView.as_view(), name="9"),
    path("10/<int:page>", TenView.as_view(), name="10"),
    path("11/", ElevenView.as_view(), name="11"),
    path("12/", TwelveView.as_view(), name="12"),
    path("12_l/", TwelveListView.as_view(), name="12_list"),
    path("12_c/", TwelveCreateView.as_view(), name="12_create"),
    path("12_gd/", TwelveCreateGroupDropdownView.as_view(), name="12_group_dropdown"),
    path("12_u/<pk>", TwelveUpdateView.as_view(), name="12_update"),
    path("12_d/<pk>", TwelveDeleteView.as_view(), name="12_delete"),
    path("13/", ThirteenView.as_view(), name="13"),
    path("14/", FourteenView.as_view(), name="14"),
]
