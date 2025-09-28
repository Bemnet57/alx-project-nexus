from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Get the custom user model (which is expected to have a 'role' field)
User = get_user_model()

class Job(models.Model):
  title = models.CharField(max_length=255, db_index=True)
  description = models.TextField()
  location = models.CharField(max_length=200, db_index=True)
  category = models.CharField(max_length=100, db_index=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs_posted') # limit_choices_to={'role': UserRole.EMPLOYER}, help_text='The user who posted this job, must have the role of EMPLOYER.')
                                                               # role limiting of the employer is done in the views 

  def __str__(self):
        return self.title
