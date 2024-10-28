from django.urls import path, include
from task_manager.statuses.views import StatusesView, StatusCreateView, StatusDeleteView, StatusUpdateView
urlpatterns = [
    path('', StatusesView.as_view(), name='statuses'),
    path('create/', StatusCreateView.as_view(), name='statuses_create'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='statuses_delete'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='statuses_update')
]
