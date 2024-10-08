from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from task_manager.users.models import User
from task_manager.users.forms import CustomUserCreationForm
from django.utils.translation import gettext_lazy as _


class UsersView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/users.html', context={
            'users': users,
        })


class UserCreateView(CreateView):
    model = User
    template_name = 'form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    extra_context = {
        'title': _('Sign Up'),
        'button_name': _('Register')
    }
