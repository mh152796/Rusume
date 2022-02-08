from distutils.command.upload import upload
import uuid
from django.db import models
from profiles.models import Profile

# Create your models here.

class ResumeModel(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)
    edu_qualification = models.TextField(blank=True, null=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to = 'cv_image/')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name