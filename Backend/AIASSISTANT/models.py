from django.db import models

# Create your models here.
class Question_Answer(models.Model):
    question = models.TextField()
    answer = models.TextField()

