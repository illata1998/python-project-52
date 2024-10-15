from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from task_manager.users.models import User
from task_manager.users.forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import CustomLoginRequiredMixin, UserPermissionMixin



class UsersView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.order_by('id').all()
        return render(request, 'users/users.html', context={
            'users': users,
        })


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


class UserDeleteView(CustomLoginRequiredMixin, UserPermissionMixin, SuccessMessageMixin, DeleteView):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User was deleted successfully')
    extra_context = {'button_name': _('Yes, delete')}


class UserUpdateView(CustomLoginRequiredMixin, UserPermissionMixin, SuccessMessageMixin, UpdateView):
    form_class = CustomUserChangeForm
    model = User
    template_name = 'form.html'
    success_url = reverse_lazy('users')
    success_message = _('User was updated successfully')
    extra_context = {
        'button_name': _('Update'),
        'title': _('Update User')
    }
