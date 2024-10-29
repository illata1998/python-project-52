import django_filters
from django.forms.widgets import CheckboxInput
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    users_tasks = django_filters.BooleanFilter(
        label=_("Only my own tasks"),
        widget=CheckboxInput,
        method='get_users_tasks',
    )

    def get_users_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor']
