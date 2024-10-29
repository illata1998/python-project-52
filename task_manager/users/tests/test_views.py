from django.urls import reverse_lazy
from django.test import TestCase
from task_manager.users.tests.testcase import UserTestCase
from task_manager.users.models import User


class TestUsersView(UserTestCase):
    def test_users(self):
        response = self.client.get(reverse_lazy('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users.html')
        self.assertEqual(User.objects.count(), 3)


class TestUserCreateView(TestCase):
    def test_create(self):
        registration_data = {
            'first_name': 'Isabella',
            'last_name': 'Swan',
            'username': 'JustBella',
            'password1': 'lamb',
            'password2': 'lamb'
        }
        initial_count = User.objects.count()
        response = self.client.get(reverse_lazy('users_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

        response = self.client.post(reverse_lazy('users_create'), data=registration_data)
        self.assertEqual(User.objects.count(), initial_count + 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestUserDeleteView(UserTestCase):
    def test_delete_without_authorization(self):
        response = self.client.get(reverse_lazy('users_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_self_delete(self):
        luke = self.user1
        self.client.force_login(luke)
        initial_count = User.objects.count()
        response = self.client.post(reverse_lazy('users_delete', kwargs={'pk': luke.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))
        self.assertEqual(User.objects.count(), initial_count - 1)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=luke.id)

    def test_delete_other_user(self):
        luke = self.user1
        leia = self.user2
        self.client.force_login(leia)
        response = self.client.post(reverse_lazy('users_delete', kwargs={'pk': luke.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))
        unchanged_user = User.objects.get(id=luke.id)
        self.assertEqual(unchanged_user.username, 'Luke19')


class TestUserUpdateView(UserTestCase):
    def test_update_without_authorization(self):
        luke = self.user1
        response = self.client.get(reverse_lazy('users_update', kwargs={'pk': luke.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_self_update(self):
        luke = self.user1
        self.client.force_login(luke)
        update_data = {
            'first_name': 'Luke',
            'last_name': 'Skywalker',
            'username': 'Jedi_Master',
            'password1': 'NewPassword123',
            'password2': 'NewPassword123'
        }
        response = self.client.post(reverse_lazy('users_update', kwargs={'pk': luke.id}), update_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))
        updated_user = User.objects.get(id=luke.id)
        self.assertEqual(updated_user.username, 'Jedi_Master')
        self.assertEqual(updated_user.first_name, 'Luke')
        self.assertEqual(updated_user.last_name, 'Skywalker')

    def test_update_other_user(self):
        luke = self.user1
        leia = self.user2
        self.client.force_login(leia)
        update_data = {
            'first_name': 'Modified',
            'last_name': 'User',
            'username': 'Hacked',
            'password1': 'Compromised',
            'password2': 'Compromised'
        }
        response = self.client.post(reverse_lazy('users_update', kwargs={'pk': luke.id}), update_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))
        unchanged_user = User.objects.get(id=luke.id)
        self.assertEqual(unchanged_user.username, 'Luke19')
