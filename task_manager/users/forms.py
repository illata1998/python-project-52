from django.contrib.auth.forms import UserCreationForm
from django import forms
from task_manager.users.models import User
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100, required=True, label=_("First name")
    )
    last_name = forms.CharField(
        max_length=100, required=True, label=_("Last name")
    )
    username = forms.CharField(
        max_length=150, required=True, label=_("Username")
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',)