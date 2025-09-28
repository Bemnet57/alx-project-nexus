from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from jobs.models import Job


User = get_user_model()

class JobPermissionTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

        # Create an employer user
        self.employer = User.objects.create_user(
            email="employer@test.com",
            password="strongpass123",
            first_name="Employer",
            last_name="User",
            role="employer"
        )
        self.client.force_authenticate(user=self.employer)

        # Create an applicant user
        self.applicant = User.objects.create_user(
            email="applicant@test.com",
            password="strongpass123",
            first_name="Applicant",
            last_name="User",
            role="applicant"
        )
        self.client.force_authenticate(user=self.employer)
        self.job_data = {
            "title": "Software Engineer",
            "description": "Develop and maintain applications",
            "location": "Remote",
            "category": "IT",
            
        }

        # Reverse assumes router registered JobViewSet as 'jobs'
        self.url = reverse("job-list")

    def test_employer_can_create_job(self):
        """Employers should be able to create a job posting"""
        self.client.force_authenticate(user=self.employer)
        response = self.client.post(self.url, self.job_data, format="json")
        print("Response Status Code:", response.status_code)
        if response.status_code != status.HTTP_201_CREATED:
            print("Validation Errors:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(Job.objects.count(), 1)

    def test_applicant_cannot_create_job(self):
        """Applicants should NOT be able to create a job posting"""
        self.client.force_authenticate(user=self.applicant)
        response = self.client.post(self.url, self.job_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)
        self.assertEqual(Job.objects.count(), 0)

    def test_unauthenticated_cannot_create_job(self):
        """Unauthenticated users should not be able to create a job"""
        self.client.logout()
        response = self.client.post(self.url, self.job_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.data)
        self.assertEqual(Job.objects.count(), 0)

    def test_search_jobs(self):
        Job.objects.create(title="Data Scientist", description="ML", location="Remote")
        Job.objects.create(title="UI Designer", description="Figma expert", location="Onsite")

        response = self.client.get(reverse("job-list") + "?search=Data")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Data Scientist")
    
    def test_retrieve_job(self):
        employer = User.objects.create_user(email="retriever@test.com", password="password123", role="employer")
        job = Job.objects.create(title="QA Engineer", description="Testing", location="Remote", employer = employer)
        response = self.client.get(reverse("job-detail", args=[job.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(response.data["title"], "QA Engineer")



# from django.test import TestCase

# # Create your tests here.
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status
# from users.models import CustomUser
# from .models import Job

# class JobTests(APITestCase):

#     def setUp(self):
#         self.employer = CustomUser.objects.create_user(email="emp@example.com", password="pass123", role="employer")
#         self.applicant = CustomUser.objects.create_user(email="app@example.com", password="pass123", role="applicant")

#     def test_employer_can_post_job(self):
#         self.client.login(email="emp@example.com", password="pass123")
#         response = self.client.post("/jobs/", {
#             "title": "Test Job",
#             "description": "Job desc",
#             "location": "Remote"
#         }, format="json")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Job.objects.count(), 1)

#     def test_applicant_cannot_post_job(self):
#         self.client.login(email="app@example.com", password="pass123")
#         response = self.client.post("/jobs/", {
#             "title": "Test Job",
#             "description": "Job desc",
#             "location": "Remote"
#         }, format="json")
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
