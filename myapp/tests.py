from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


class PageViewTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Building the future")

    def test_about_page(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Technology meets")

    def test_contact_page(self):
        response = self.client.get(reverse("contact"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "GET IN TOUCH")

class APIHomeTests(APITestCase):

    def test_api_home_status_code(self):
        response = self.client.get('/api/')

        self.assertEqual(response.status_code, 200)

    def test_api_home_response_data(self):
        response = self.client.get('/api/')

        self.assertEqual(
            response.data['message'],
            'Welcome to my CSC325 Django API!'
        )
        self.assertEqual(
            response.data['project'],
            'CSC325 CI/CD Project'
        )
        self.assertEqual(response.data['status'], 'running')
        self.assertEqual(response.data['version'], '1.1')