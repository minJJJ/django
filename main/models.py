from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #쉘에서 필수값으로 지정했다


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='answer') #related_name 검색해보기
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
