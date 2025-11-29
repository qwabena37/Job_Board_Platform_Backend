from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from accounts.models import User
from jobs.models import Job, Company, Location, Industry


class JobTests(APITestCase):

    def setUp(self):
        # Create admin
        self.admin = User.objects.create_user(
            username="admin",
            password="AdminPass123!",
            role="admin",
        )

        # Login admin
        response = self.client.post(
            reverse("login"),
            {"username": "admin", "password": "AdminPass123!"}
        )
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        # Job metadata
        self.industry = Industry.objects.create(name="Tech")
        self.location = Location.objects.create(name="Remote")
        self.company = Company.objects.create(name="OpenAI")

    def test_create_job(self):
        """Admin can create a job."""
        url = reverse("job-list")
        data = {
            "title": "Backend Developer",
            "description": "Django experience required.",
            "industry": self.industry.id,
            "location": self.location.id,
            "company": self.company.id,
            "job_type": "Full-time",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Job.objects.filter(title="Backend Developer").exists())

    def test_list_jobs(self):
        """Anyone can view job listings."""
        Job.objects.create(
            title="Frontend Dev",
            description="React job.",
            company=self.company,
            location=self.location,
            industry=self.industry,
            job_type="Contract",
        )

        url = reverse("job-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)
