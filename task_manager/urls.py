from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from task_manager.views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
    path('users/', include('task_manager.users.urls'))
]
