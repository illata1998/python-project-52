from django.urls import path, include
from django.views.generic import TemplateView
from task_manager.users.views import UsersView, UserCreateView

urlpatterns = [
    path('', UsersView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='users_create')
]