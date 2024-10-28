from task_manager.users.tests.user_testcase import UserTestCase
from task_manager.users.models import User


class UserModelTestCase(UserTestCase):
    def test_user_creation(self):
        user = self.user1
        self.assertEqual(user.username, 'Luke19')
        self.assertEqual(user.first_name, 'Luke')
        self.assertEqual(user.last_name, 'Skywalker')

    def test_username_uniqueness(self):
        with self.assertRaises(Exception):
            User.objects.create(
                first_name='Another',
                last_name='Luke',
                username='Luke19',
                password='Force123',
                email='another@rebellion.com'
            )
