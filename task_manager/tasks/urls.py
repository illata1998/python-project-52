from django.urls import path

from task_manager.tasks.views import (TasksView,
                                      TaskShowView,
                                      TaskCreateView,
                                      TaskDeleteView,
                                      TaskUpdateView)

urlpatterns = [
    path('', TasksView.as_view(), name='tasks'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/', TaskShowView.as_view(), name='task_show')
]
