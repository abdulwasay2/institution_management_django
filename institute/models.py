from django.db import models
from ckeditor.fields import RichTextField 
from django.contrib.auth.models import User

from institution_management.models import BaseModel



class Institute(BaseModel):
    STATUS_CHOICES = [
        ("active", "Active"), 
        ("inactive", "Inactive")
        ]

    name = models.CharField(max_length=256, blank=True, null=True)
    description = RichTextField()
    address = models.TextField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True, upload_to="institutes/logs/")
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    official_email = models.EmailField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_institutes")
    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )


class CourseCategory(BaseModel):
    name = models.CharField(max_length=256, blank=True, null=True)
    description = RichTextField()


class Course(BaseModel):
    name = models.CharField(max_length=256, blank=True, null=True)
    description = RichTextField()
    institute = models.ForeignKey(
        Institute, on_delete=models.CASCADE, related_name="offered_courses")
    category = models.ForeignKey(
        CourseCategory, on_delete=models.CASCADE, related_name="courses")