from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from task_manager.views import CustomLoginView, CustomLogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('users/', include('task_manager.users.urls'))
]
