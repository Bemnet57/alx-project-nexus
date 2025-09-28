from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager

# ENUM for roles
class UserRole(models.TextChoices):
    EMPLOYER = 'employer', 'Employer'
    APPLICANT = 'applicant', 'Applicant'
    ADMIN = 'admin', 'Admin'

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError('Password must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', UserRole.ADMIN)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)
   

class CustomUser(AbstractUser):  # Corrected
    username = None # Override the default username field and nullify it
    email = models.EmailField(unique=True) # Make email the primary identifier
    # Set the USERNAME_FIELD to email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','role']
    #password = models.CharField(max_length=128) since built-in password handling logic is secure with password hashing and authentication
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.APPLICANT)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    def __str__(self):
        return self.email