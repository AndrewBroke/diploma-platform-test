from django.db import models

# Create your models here.
class PupilPrefs(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    