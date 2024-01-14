from django.db import models
from django.contrib.auth.models import User

from institution_management.models import BaseModel
from institute.models import Course, Institute



class Student(BaseModel):
    STATUS_CHOICES = [
        ("active", "Active"), 
        ("inactive", "Inactive")
        ]
    GENDER_CHOICES = [
        ("male", "Male"), 
        ("female", "Female")
        ]

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )
    cnic_number = models.CharField(
        max_length=200, unique=True, blank=True, null=True)
    surname = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    date_of_birth = models.DateField(blank=True, null=True)
    institute = models.ForeignKey(
        Institute, on_delete=models.SET_NULL, blank=True, null=True
    )
    user = models.OneToOneField(User, models.CASCADE)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True)
    others = models.TextField(blank=True)
    passport_picture = models.ImageField(blank=True, upload_to="students/passports/")

    class Meta:
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.cnic_number})"

    # def get_absolute_url(self):
    #     return reverse("student-detail", kwargs={"pk": self.pk})


class StudentRollNumberSlip(BaseModel):
    course = models.ForeignKey(Course, models.CASCADE, related_name="student_rollnumber_slips")
    student = models.ForeignKey(Student, models.CASCADE, related_name="course_rollnumber_slips")
    doc_file = models.FileField(upload_to="Students/RollNumberSlips/")
