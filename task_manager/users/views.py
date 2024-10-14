from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView
from task_manager.users.models import User
from task_manager.users.forms import CustomUserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin



class UsersView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
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


class UserDeleteView(SuccessMessageMixin, DeleteView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    permission_denied_message = ''
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User was deleted successfully')
    extra_context = {'button_name': _('Yes, delete')}
