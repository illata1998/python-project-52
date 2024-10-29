from django.urls import path

from task_manager.users.views import (UsersListView,
                                      UserCreateView,
                                      UserDeleteView,
                                      UserUpdateView)

urlpatterns = [
    path('', UsersListView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update')
]
