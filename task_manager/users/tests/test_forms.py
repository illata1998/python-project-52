from django.test import TestCase
from task_manager.users.forms import CustomUserCreationForm


class RegistrationFormTest(TestCase):
    def test_is_invalid_missing_fields(self):
        form = CustomUserCreationForm(data={
            'username': 'Luke19',
            'password1': 'R2D2',
        })
        self.assertFalse(form.is_valid())

    def test_is_invalid_password(self):
        form = CustomUserCreationForm(data={
            'first_name': 'Luke',
            'last_name': 'Skywalker',
            'username': 'Luke19',
            'password1': '1',
            'password2': '1'
        })
        self.assertFalse(form.is_valid())

    def test_is_invalid_username(self):
        form = CustomUserCreationForm(data={
            'first_name': 'Luke',
            'last_name': 'Skywalker',
            'username': 'Luke19!',
            'password1': 'R2D2',
            'password2': 'R2D2'
        })
        self.assertFalse(form.is_valid())

    def test_is_valid(self):
        form = CustomUserCreationForm(data={
            'first_name': 'Luke',
            'last_name': 'Skywalker',
            'username': 'Luke19',
            'password1': 'R2D2',
            'password2': 'R2D2'
        })
        self.assertTrue(form.is_valid())