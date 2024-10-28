from task_manager.statuses.tests.statuses_testcase import StatusTestCase
from task_manager.statuses.forms import StatusCreationForm


class CreationFormTest(StatusTestCase):
    def test_missing_fields(self):
        form = StatusCreationForm(data={
            'name': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_duplicate(self):
        form = StatusCreationForm(data={
            'name': self.status1.name
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_valid_form(self):
        form = StatusCreationForm(data={
            'name': 'status3'
        })
        self.assertTrue(form.is_valid())