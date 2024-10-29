from django.test import TestCase, Client
from task_manager.statuses.models import Status
from task_manager.users.models import User

class StatusTestCase(TestCase):
    fixtures = ['test_users.json', 'test_statuses.json']
    def setUp(self):
        self.client = Client()
        self.status1 = Status.objects.get(name='status1')
        self.status2 = Status.objects.get(name='status2')
        self.user1 = User.objects.get(username='Luke19')
        self.user2 = User.objects.get(username='SpaceBuns')
