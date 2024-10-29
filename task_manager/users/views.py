from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from task_manager.mixins import CustomLoginRequiredMixin, UserPermissionMixin
from task_manager.users.forms import (CustomUserCreationForm,
                                      CustomUserChangeForm)
from task_manager.users.models import User


class UsersView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'
    ordering = ['id']


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    success_message = _('User was registered successfully')
    extra_context = {
        'title': _('Sign Up'),
        'button_name': _('Register')
    }


class UserDeleteView(CustomLoginRequiredMixin,
                     UserPermissionMixin,
                     SuccessMessageMixin,
                     DeleteView):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User was deleted successfully')
    permission_denied_url = reverse_lazy('users')
    permission_denied_message = _(
        "You don't have rights to change another user."
    )
    access_denied_message = _("You don't have rights to change another user.")
    extra_context = {'button_name': _('Yes, delete')}


class UserUpdateView(CustomLoginRequiredMixin,
                     UserPermissionMixin,
                     SuccessMessageMixin,
                     UpdateView):
    form_class = CustomUserChangeForm
    model = User
    template_name = 'form.html'
    success_url = reverse_lazy('users')
    success_message = _('User was updated successfully')
    permission_denied_url = reverse_lazy('users')
    permission_denied_message = _(
        "You don't have rights to change another user."
    )
    extra_context = {
        'button_name': _('Update'),
        'title': _('Update User')
    }
