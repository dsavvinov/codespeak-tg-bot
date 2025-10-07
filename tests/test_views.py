import pytest
from django.test import TestCase, Client
from django.urls import reverse


class HelloWorldEndpointTest(TestCase):
    """Test cases for the hello_world endpoint."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    @pytest.mark.timeout(30)
    def test_hello_world_endpoint_returns_200(self):
        """
        Test kind: endpoint_tests
        Original method: hello_world

        Test that the hello_world endpoint returns HTTP 200 status code.
        """
        response = self.client.get(reverse('django_app:hello_world'))
        self.assertEqual(response.status_code, 200)

    @pytest.mark.timeout(30)
    def test_hello_world_endpoint_uses_correct_template(self):
        """
        Test kind: endpoint_tests
        Original method: hello_world

        Test that the hello_world endpoint uses the correct template.
        """
        response = self.client.get(reverse('django_app:hello_world'))
        self.assertTemplateUsed(response, 'django_app/hello_world.html')

    @pytest.mark.timeout(30)
    def test_hello_world_endpoint_contains_expected_content(self):
        """
        Test kind: endpoint_tests
        Original method: hello_world

        Test that the hello_world endpoint returns expected content in the response.
        """
        response = self.client.get(reverse('django_app:hello_world'))
        self.assertContains(response, "Hello from CodeSpeak!")
        self.assertContains(response, "Welcome to your Django web application")
        self.assertContains(response, "Ready to Go!")

    @pytest.mark.timeout(30)
    def test_hello_world_endpoint_root_path(self):
        """
        Test kind: endpoint_tests
        Original method: hello_world

        Test that the hello_world endpoint is accessible via root path.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello from CodeSpeak!")