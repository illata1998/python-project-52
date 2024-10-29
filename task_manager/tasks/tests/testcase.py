from django.test import TestCase, Client
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status


class TaskTestCase(TestCase):
    fixtures = ['test_users.json', 'test_statuses.json', 'test_tasks.json']

    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)

        self.status1 = Status.objects.get(pk=1)

        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)

        self.task_count = Task.objects.count()

        # Task creation data for testing
        self.valid_task_data = {
            'name': 'New Task',
            'description': 'New Description',
            'status': self.status1.id,
            'executor': self.user2.id
        }
