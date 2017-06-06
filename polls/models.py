# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=150)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice_text


