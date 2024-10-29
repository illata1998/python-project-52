from django.urls import reverse_lazy

from task_manager.statuses.models import Status
from task_manager.statuses.tests.testcase import StatusTestCase


class TestStatusesView(StatusTestCase):
    def test_statuses_authorized(self):
        user1 = self.user1
        self.client.force_login(user1)
        response = self.client.get(reverse_lazy('statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/statuses.html')
        self.assertEqual(Status.objects.count(), self.status_count)

    def test_statuses_unauthorized(self):
        response = self.client.get(reverse_lazy('statuses'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestStatusCreateView(StatusTestCase):
    def test_create_status_authorized(self):
        user1 = self.user1
        self.client.force_login(user1)
        creation_data = self.valid_status_data
        initial_count = Status.objects.count()
        response = self.client.get(reverse_lazy('status_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')
        response = self.client.post(
            reverse_lazy('status_create'), data=creation_data
        )
        self.assertEqual(Status.objects.count(), initial_count + 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))

    def test_create_status_unauthorized(self):
        creation_data = self.valid_status_data
        response = self.client.post(
            reverse_lazy('status_create'), data=creation_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestStatusDeleteView(StatusTestCase):
    def test_delete_status_unauthorized(self):
        status = self.status1
        response = self.client.get(
            reverse_lazy('status_delete', kwargs={'pk': status.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_delete_status_authorized(self):
        user = self.user1
        status = self.status1
        self.client.force_login(user)
        initial_count = Status.objects.count()
        response = self.client.post(
            reverse_lazy('status_delete', kwargs={'pk': status.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))
        self.assertEqual(Status.objects.count(), initial_count - 1)
        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(id=status.id)


class TestStatusUpdateView(StatusTestCase):
    def test_update_status_unauthorized(self):
        status = self.status1
        response = self.client.get(
            reverse_lazy('status_update', kwargs={'pk': status.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_status_authorized(self):
        user = self.user1
        status = self.status1
        self.client.force_login(user)
        update_data = {'name': 'new'}
        response = self.client.post(
            reverse_lazy('status_update', kwargs={'pk': status.id}),
            data=update_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))
        updated_status = Status.objects.get(id=status.id)
        self.assertEqual(updated_status.name, update_data['name'])
