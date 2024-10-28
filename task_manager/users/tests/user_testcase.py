from django.test import TestCase, Client
from task_manager.users.models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(
            first_name='Luke',
            last_name='Skywalker',
            username='Luke19',
            password='R2D2'
        )
        User.objects.create(
            first_name='Leia',
            last_name='Organa',
            username='SpaceBuns',
            password='NewHope'
        )
        User.objects.create(
            first_name='Han',
            last_name='Solo',
            username='Han.',
            password='MillenniumFalcon'
        )
        self.user1 = User.objects.get(username='Luke19')
        self.user2 = User.objects.get(username='SpaceBuns')
        self.user3 = User.objects.get(username='Han.')
