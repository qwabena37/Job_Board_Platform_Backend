from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from accounts.models import User


class AccountsAuthTests(APITestCase):

    def test_user_registration(self):
        """Test that a new user can register successfully."""
        url = reverse("register")
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "StrongPass123!",
            "first_name": "Test",
            "last_name": "User",
            "role": "user"
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_user_login(self):
        """Test JWT login works."""
        user = User.objects.create_user(
            username="tester",
            password="StrongPassword123!"
        )

        url = reverse("login")
        data = {"username": "tester", "password": "StrongPassword123!"}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)


class ProfileTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="tester",
            password="StrongPassword123!",
            email="t@t.com",
        )
        login_url = reverse("login")
        response = self.client.post(
            login_url, {"username": "tester", "password": "StrongPassword123!"}
        )
        self.token = response.data["access"]

    def test_get_profile(self):
        """User can view their profile when authenticated."""
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        url = reverse("me")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
