from django.db import models
from django.utils import timezone


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    # is_deleted = models.BooleanField(null=False, blank=False, default=False)
    # created_at = models.DateTimeField(default=timezone.now())
    # updated_at = models.DateTimeField(default=timezone.now())