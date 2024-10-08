from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomLoginView(LoginView):
    template_name='form.html'
    form_class = AuthenticationForm
    extra_context={
        'title': _('Log In'),
        'button_name': _('Log In')
    }
