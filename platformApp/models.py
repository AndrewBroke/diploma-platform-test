from django.db import models
from django.contrib.auth.models import User

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

class Measure(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"{self.pk} - {self.text}" 

class Test2Relations(models.Model):
    question = models.ForeignKey(
        "SimpleQuestion",
        on_delete=models.CASCADE
    )
    measure = models.ForeignKey(
        "Measure",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Вопрос номер {self.question.pk}, мера - {self.measure.text}" 
    

class Theme(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.pk} - {self.name}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    grade = models.IntegerField()
    tests = models.JSONField(null=True)

    def __str__(self) -> str:
        return f"{self.pk} - {self.user.username}"