from django.test import TestCase
from task_manager.statuses.models import Status


class StatusTestCase(TestCase):
    def setUp(self):
        self.status = Status.objects.create(
            name='Test Status'
        )

    def test_status_creation(self):
        self.assertEqual(self.status.name, 'Test Status')

    def test_duplicate_status_name(self):
        with self.assertRaises(Exception):
            Status.objects.create(name='Test Status')
