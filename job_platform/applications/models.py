from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

# ENUM for status
class StatusChoice(models.TextChoices):
    PENDING = 'pending', 'Pending'
    ACCEPTED = 'accepted', 'Accepted'
    REJECTED = 'rejected', 'Rejected'

class Application(models.Model):
  job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, related_name='applications') #, 
  applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications') #, limit_choices_to={'role': UserRole.EMPLOYER}, help_text='The user who posted this job, must have the role of EMPLOYER.')
  cover_letter = models.TextField(blank=True)
  status = models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.PENDING)
  applied_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return f"Application for {self.job.title} by {self.applicant.get_full_name()}"