from django.urls import path

from task_manager.statuses.views import (StatusesView,
                                         StatusCreateView,
                                         StatusDeleteView,
                                         StatusUpdateView)

urlpatterns = [
    path('', StatusesView.as_view(), name='statuses'),
    path('create/', StatusCreateView.as_view(), name='status_create'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='status_update')
]
