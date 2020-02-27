from django.db import models
"""
# Create your models here.
class Info(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "user_info"
"""
class Quiz(models.Model):
    questionb = models.CharField(max_length=200, default=1)
    questiona = models.CharField(max_length=200, default=None,blank=True)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    ques_slug = models.CharField(max_length=100, default=1)
    
    def __str__(self):
        return self.questionb