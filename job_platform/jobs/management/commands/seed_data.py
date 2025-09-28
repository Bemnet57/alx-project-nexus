from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random

from users.models import CustomUser
from jobs.models import Job
from applications.models import Application


class Command(BaseCommand):
    help = "Seed database with sample users, jobs, and applications"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # --- Create Default Superuser (if not exists) ---
        admin_email = "admin@example.com"
        admin_password = "admin123"
        if not CustomUser.objects.filter(email=admin_email).exists():
            CustomUser.objects.create_superuser(
                email=admin_email,
                password=admin_password,
                first_name="Admin",
                last_name="User",
            )
            self.stdout.write(self.style.SUCCESS(f"✅ Created default superuser {admin_email} / {admin_password}"))
        else:
            self.stdout.write(self.style.WARNING(f"⚠️ Superuser {admin_email} already exists"))

        # --- Create Employers ---
        employers = []
        for _ in range(3):
            employer = CustomUser.objects.create_user(
                email=fake.unique.email(),
                password="password123",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                date_joined=timezone.now(),
            )
            employers.append(employer)
        self.stdout.write(self.style.SUCCESS(f"✅ Created {len(employers)} employers"))

        # --- Create Applicants ---
        applicants = []
        for _ in range(5):
            applicant = CustomUser.objects.create_user(
                email=fake.unique.email(),
                password="password123",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                date_joined=timezone.now(),
            )
            applicants.append(applicant)
        self.stdout.write(self.style.SUCCESS(f"✅ Created {len(applicants)} applicants"))

        # --- Create Jobs ---
        categories = ["Engineering", "Design", "Marketing", "Finance", "Healthcare"]
        jobs = []
        for employer in employers:
            for _ in range(2):  # 2 jobs per employer
                job = Job.objects.create(
                    title=fake.job(),
                    description=fake.text(max_nb_chars=300),
                    location=fake.city(),
                    category=random.choice(categories),
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    employer=employer,
                )
                jobs.append(job)
        self.stdout.write(self.style.SUCCESS(f"✅ Created {len(jobs)} jobs"))

        # --- Create Applications ---
        statuses = ["pending", "accepted", "rejected"]
        for applicant in applicants:
            job = random.choice(jobs)
            Application.objects.create(
                job=job,
                applicant=applicant,
                cover_letter=fake.paragraph(nb_sentences=5),
                status=random.choice(statuses),
                applied_at=timezone.now(),
            )
        self.stdout.write(self.style.SUCCESS("✅ Applications seeded successfully!"))
