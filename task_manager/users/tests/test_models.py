from django.test import TestCase
from task_manager.users.models import User


class UserTestCase(TestCase):
    def test_user_creation(self):
        User.objects.create(
            first_name='Luke',
            last_name='Skywalker',
            username='Luke19',
            password='R2D2'
        )
        user1 = User.objects.get(username='Luke19')
        self.assertEqual(user1.username, 'Luke19')
        self.assertEqual(user1.first_name, 'Luke')
        self.assertEqual(user1.last_name, 'Skywalker')