from django.urls import reverse_lazy

from task_manager.tasks.models import Task
from task_manager.tasks.tests.testcase import TaskTestCase


class TestTasksView(TaskTestCase):
    def test_tasks_unauthorized(self):
        response = self.client.get(reverse_lazy('tasks'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_tasks_authorized(self):
        user = self.user1
        self.client.force_login(user)
        response = self.client.get(reverse_lazy('tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks.html')
        self.assertEqual(Task.objects.count(), self.task_count)


class TaskFilterTest(TaskTestCase):
    def setUp(self):
        super().setUp()
        self.client.force_login(self.user1)

    def test_filter_by_status(self):
        response = self.client.get(
            reverse_lazy('tasks'), {'status': self.status1.id}
        )

        self.assertEqual(response.status_code, 200)
        tasks = set(response.context['tasks'])
        expected_tasks = set(Task.objects.filter(status=self.status1))
        self.assertEqual(tasks, expected_tasks)

    def test_filter_by_executor(self):
        response = self.client.get(
            reverse_lazy('tasks'), {'executor': self.user2.id}
        )

        self.assertEqual(response.status_code, 200)
        tasks = set(response.context['tasks'])
        expected_tasks = set(Task.objects.filter(executor=self.user2))
        self.assertEqual(tasks, expected_tasks)

    def test_filter_by_self_tasks(self):
        response = self.client.get(
            reverse_lazy('tasks'), {'users_tasks': 'on'}
        )

        self.assertEqual(response.status_code, 200)
        tasks = set(response.context['tasks'])
        expected_tasks = set(Task.objects.filter(author=self.user1))
        self.assertEqual(tasks, expected_tasks)


class TestTaskCreateView(TaskTestCase):
    def test_create_task_authorized(self):
        user1 = self.user1
        self.client.force_login(user1)
        creation_data = self.valid_task_data
        initial_count = Task.objects.count()
        response = self.client.get(reverse_lazy('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

        response = self.client.post(
            reverse_lazy('task_create'), data=creation_data
        )
        self.assertEqual(Task.objects.count(), initial_count + 1)
        self.assertEqual(response.status_code, 302)

    def test_create_task_unauthorized(self):
        creation_data = self.valid_task_data
        response = self.client.post(
            reverse_lazy('task_create'), data=creation_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestTaskDeleteView(TaskTestCase):
    def test_delete_task_unauthorized(self):
        task = self.task1
        response = self.client.get(
            reverse_lazy('task_delete', kwargs={'pk': task.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_delete_task_authorized(self):
        user = self.user1
        task = self.task1
        self.client.force_login(user)
        initial_count = Task.objects.count()
        response = self.client.post(
            reverse_lazy('task_delete', kwargs={'pk': task.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))
        self.assertEqual(Task.objects.count(), initial_count - 1)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task.id)

    def test_delete_other_users_task_authorized(self):
        user = self.user2
        task = self.task1
        self.client.force_login(user)
        initial_count = Task.objects.count()
        response = self.client.post(
            reverse_lazy('task_delete', kwargs={'pk': task.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))
        self.assertEqual(Task.objects.count(), initial_count)
        unchanged_task = Task.objects.get(id=task.id)
        self.assertEqual(unchanged_task.name, task.name)


class TestTaskUpdateView(TaskTestCase):
    def test_update_task_unauthorized(self):
        task = self.task1
        response = self.client.get(
            reverse_lazy('task_update', kwargs={'pk': task.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_task_authorized(self):
        user = self.user1
        task = self.task1
        self.client.force_login(user)
        update_data = self.valid_task_data.copy()
        update_data.update({
            'name': 'Absolutely new task'
        })
        response = self.client.post(
            reverse_lazy('task_update', kwargs={'pk': task.id}),
            data=update_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))
        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.name, update_data['name'])

    def test_update_other_users_task_authorized(self):
        user = self.user2
        task = self.task1
        self.client.force_login(user)

        update_data = self.valid_task_data.copy()
        update_data.update({
            'name': 'Absolutely new task'
        })

        response = self.client.post(
            reverse_lazy('task_update', kwargs={'pk': task.id}),
            data=update_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))

        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.name, update_data['name'])
