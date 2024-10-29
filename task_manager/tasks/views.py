from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import CustomLoginRequiredMixin, AuthorPermissionMixin



class TasksView(CustomLoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.order_by('id').all()
        return render(request, 'tasks/tasks.html', context={
            'tasks': tasks,
            'button_name': _('Create Task')
        })


class TaskCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'form.html'
    form_class = TaskCreationForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task was created successfully')
    extra_context = {
        'title': _('Create Task'),
        'button_name': _('Create')
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskDeleteView(CustomLoginRequiredMixin, AuthorPermissionMixin, SuccessMessageMixin, DeleteView):
    template_name = 'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _('Task was deleted successfully')
    permission_denied_url = reverse_lazy('tasks')
    permission_denied_message = _("Only the task's author can delete it")
    extra_context = {'button_name': _('Yes, delete')}


class TaskUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = TaskCreationForm
    model = Task
    template_name = 'form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task was updated successfully')
    extra_context = {
        'button_name': _('Update'),
        'title': _('Update Task')
    }
