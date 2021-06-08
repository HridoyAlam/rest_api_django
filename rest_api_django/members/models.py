from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=20)
    major = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

    def __str__(self):
        return self.name