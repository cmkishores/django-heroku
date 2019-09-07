from django.test import TestCase
from django.test import SimpleTestCase

class SimpleTest(SimpleTestCase):
	def test_homepage(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code,200)
		self.assertNotEqual(response.status_code,404)
		self.assertNotEqual(response.status_code,403)
		self.assertNotEqual(response.status_code,402)


# Create your tests here.
