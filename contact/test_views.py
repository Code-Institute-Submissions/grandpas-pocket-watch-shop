from django.test import TestCase


class TestContact(TestCase):
    def contact(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

