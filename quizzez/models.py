from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db import models
from datetime import date
import datetime

class Question(models.Model):
    name = models.CharField(max_length=200)
    opt_1 = models.CharField(max_length=50)
    opt_2 = models.CharField(max_length=50)
    opt_3 = models.CharField(max_length=50)
    opt_4 = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={'pk': self.id})
    
  
class Quiz(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    questions = models.ManyToManyField(Question)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('quiz-detail', kwargs={'quiz_id': self.id})
    
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk': self.id})