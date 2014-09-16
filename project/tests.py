from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory
from .views import TasksListView


class TasksListViewTests(TestCase):

    def test_tasks_in_the_context(self):

        client = Client()
        response = client.get('/tasks')

        self.assertEquals(list(response.context['object_list']), [])

        # Contact.objects.create(first_name=’foo’, last_name =’bar’)
        # response = client.get(’ / ’)
        # self.assertEquals(response.context[’object_list’].count(), 1)

    def test_tasks_in_the_request_factory(self):
        factory = RequestFactory()
        request = factory.get('/tasks')

        response = TasksListView.as_view()(request)

        self.assertEquals(list(response.context['object_list']), [])

        # Contact.objects.create(first_name=’foo’, last_name=’bar’)
        # response = ListContactView.as_view()(request)
        # self.assertEquals(response.context_data[’object_list’].count(), 1)