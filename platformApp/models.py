from django.db import models

# Create your models here.
class PupilPrefs(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    
class SimpleAnswer(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"{self.pk} - {self.text}"

class SimpleQuestion(models.Model):
    text = models.TextField()
    correct_answer = models.ForeignKey(
        "SimpleAnswer",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.pk} - {self.text}"
