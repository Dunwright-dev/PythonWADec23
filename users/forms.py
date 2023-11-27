"""django-htmx-demo project CustomUser Forms."""

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class AdminCustomUserCreationForm(UserCreationForm):
    """A basic custom user creation form."""

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "user_type",
            "department",
            "team",
        )

        error_messages = {
            "username": {
                "unique": _("That user name already exists, please choose another.")
            }
        }


class AdminCustomUserChangeForm(UserChangeForm):
    """A basic custom user change form."""

    class Meta(UserChangeForm.Meta):
        model = CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "user_type",
            "email",
            "department",
            "team",
            # "username",
        )
        # labels = {
        #     "name": _("Account Name:"),
        #     "broker": _("Broker:"),
        #     "platform_settings": _("Platform Settings:"),
        #     "currency": _("Account Currency:"),
        #     "leverage": _("Account Leverage:"),
        #     "number": _("Account Number:"),
        #     "risk_calculation_type": _("Risk Calculation Type:"),
        #     "account_type": _("Account Type:"),
        #     "comment": _("Comment:"),
        # }
