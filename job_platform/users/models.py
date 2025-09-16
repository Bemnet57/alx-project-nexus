from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# ENUM for roles
class UserRole(models.TextChoices):
    EMPLOYER = 'employer', 'Employer'
    HOST = 'host', 'Host'
    ADMIN = 'admin', 'Admin'

class User(AbstractUser):
  username = None # Override the default username field
  email = models.EmailField(unique=True) # Make email the primary identifier
  # Set the USERNAME_FIELD to email
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']
  #password = models.CharField(max_length=128) since built-in password handling logic is secure with password hashing and authentication
  role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.EMPLOYER)
  date_joined = models.DateTimeField(default=timezone.now)

