from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from accounts.models import User
from jobs.models import Job, Company, Location, Industry
from applications.models import ApplyJob


class ApplicationTests(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username="user1",
            password="UserPass123!",
        )

        login = self.client.post(
            reverse("login"),
            {"username": "user1", "password": "UserPass123!"}
        )
        self.token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        # Job metadata
        industry = Industry.objects.create(name="Tech")
        location = Location.objects.create(name="Remote")
        company = Company.objects.create(name="OpenAI")

        self.job = Job.objects.create(
            title="AI Researcher",
            description="ML research.",
            company=company,
            location=location,
            industry=industry,
            job_type="Full-time",
            posted_by=self.user,
        )

    def test_apply_for_job(self):
        """User can apply for a job."""
        url = reverse("applyjob-list")
        data = {"job": self.job.id, "cover_letter": "I am interested."}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(ApplyJob.objects.filter(job=self.job).exists())

    def test_list_applications(self):
        """Users can list their applications."""
        ApplyJob.objects.create(applicant=self.user, job=self.job)

        url = reverse("applyjob-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
