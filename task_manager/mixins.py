from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, _('You are not authorized! Please, log in.'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UserPermissionMixin(UserPassesTestMixin):
    login_url = reverse_lazy('users')
    redirect_field_name = None
    def test_func(self):
        return self.get_object() == self.request.user

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            messages.add_message(request, messages.ERROR, _("You don't have rights to change another user."))
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)

