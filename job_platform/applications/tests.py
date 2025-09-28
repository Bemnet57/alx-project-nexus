from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from jobs.models import Job
from applications.models import Application

User = get_user_model()

class ApplicationTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

        # Create users
        self.applicant = User.objects.create_user(
            email="applicant@test.com",
            password="strongpass123",
            first_name="Applicant",
            last_name="User",
            role="applicant"
        )
        self.employer = User.objects.create_user(
            email="employer@test.com",
            password="strongpass123",
            first_name="Employer",
            last_name="User",
            role="employer"
        )

        # Create a job
        self.job = Job.objects.create(
            title="Backend Dev",
            description="Build APIs",
            location="Remote",
            category="IT",
            employer=self.employer
        )

        self.application_data = {
            "job": self.job.id,
            "cover_letter": "I am interested in this job.",
            "applicant": self.applicant.id
        }

        self.url = reverse("application-list")

    def test_applicant_can_apply(self):
        self.client.force_authenticate(user=self.applicant)
        response = self.client.post(self.url, self.application_data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Application.objects.count(), 1)

    def test_employer_cannot_apply(self):
        self.client.force_authenticate(user=self.employer)
        response = self.client.post(self.url, self.application_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Application.objects.count(), 0)

    def test_unauthenticated_cannot_apply(self):
        self.client.logout()
        response = self.client.post(self.url, self.application_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Application.objects.count(), 0)
