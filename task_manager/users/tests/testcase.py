from django.test import TestCase, Client
from task_manager.users.models import User

class UserTestCase(TestCase):
    fixtures = ['test_users.json']
    def setUp(self):
        self.user1 = User.objects.get(username='Luke19')
        self.user2 = User.objects.get(username='SpaceBuns')
        self.user3 = User.objects.get(username='Han.')
