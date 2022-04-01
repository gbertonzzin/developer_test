from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    name =          models.CharField(max_length = 100)
    description =   models.CharField(max_length = 300)
    date =          models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name



class SurveyQuestion(models.Model):
    survey =    models.ForeignKey(Survey, related_name='questions', on_delete = models.CASCADE)
    text =      models.CharField(max_length = 300)
    date =      models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.text

class SurveyQuestionAlternative(models.Model):
    question =  models.ForeignKey(SurveyQuestion, related_name='alternatives', on_delete=models.CASCADE)
    text =      models.CharField(max_length = 300)


    def __str__(self):
        return self.text


class SurveyUserAnswer(models.Model):
    user =          models.ForeignKey(User, on_delete=models.CASCADE)
    alternative =   models.ForeignKey(SurveyQuestionAlternative, related_name='answers', on_delete=models.CASCADE)
    answer =        models.BooleanField(default= False)