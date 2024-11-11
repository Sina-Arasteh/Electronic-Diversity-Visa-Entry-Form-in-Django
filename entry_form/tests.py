from django.test import TestCase, Client

# Create your tests here.

class BeginEntryViewTests(TestCase):

    def test_template(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, "entry_form/begin_entry.html")