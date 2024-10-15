from django.urls import path, include
from django.views.generic import TemplateView
from task_manager.users.views import UsersView, UserCreateView, UserDeleteView, UserUpdateView

urlpatterns = [
    path('', UsersView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='users_create'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='users_delete'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='users_update')
]