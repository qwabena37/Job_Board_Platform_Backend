from django.db import models
from django.conf import settings

class Industry(models.Model):
    name = models.CharField(max_length=120, unique=True)

class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Company(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True)

class Job(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True)
    job_type = models.CharField(max_length=20)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
