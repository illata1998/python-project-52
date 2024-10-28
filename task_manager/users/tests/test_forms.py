from django.test import TestCase
from task_manager.users.forms import CustomUserCreationForm


class SignUpFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'first_name': 'Luke',
            'last_name': 'Skywalker',
            'username': 'Luke19',
            'password1': 'R2D2pass123',
            'password2': 'R2D2pass123'
        }

    def test_valid_data(self):
        form = CustomUserCreationForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_missing_fields(self):
        form = CustomUserCreationForm(data={
            'username': self.valid_data['username'],
            'password1': self.valid_data['password1'],
        })
        self.assertFalse(form.is_valid())

    def test_password_too_short(self):
        invalid_data = self.valid_data.copy()
        invalid_data.update({
            'password1': '1',
            'password2': '1'
        })
        form = CustomUserCreationForm(data=invalid_data)
        self.assertFalse(form.is_valid())

    def test_invalid_username(self):
        invalid_data = self.valid_data.copy()
        invalid_data['username'] = 'Luke19!'
        form = CustomUserCreationForm(data=invalid_data)
        self.assertFalse(form.is_valid())

    def test_passwords_do_not_match(self):
        invalid_data = self.valid_data.copy()
        invalid_data['password2'] = 'C3POpass123'
        form = CustomUserCreationForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_empty_strings(self):
        invalid_data = self.valid_data.copy()
        invalid_data.update({
            'first_name': '',
            'last_name': ''
        })
        form = CustomUserCreationForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)

    def test_duplicate_username(self):
        form1 = CustomUserCreationForm(data=self.valid_data)
        form1.save()

        duplicate_data = self.valid_data.copy()
        duplicate_data.update({
            'first_name': 'Lucas',
            'last_name': 'Sky',
        })
        form2 = CustomUserCreationForm(data=duplicate_data)
        self.assertFalse(form2.is_valid())
        self.assertIn('username', form2.errors)
