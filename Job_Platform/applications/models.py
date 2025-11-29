from django.db import models
from django.conf import settings
from jobs.models import Job

class ApplyJob(models.Model):
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cover_letter = models.TextField(blank=True)
    resume_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
        ordering = ['-created_at']  