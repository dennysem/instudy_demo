from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Task(models.Model):
    desc = models.TextField()
    assignee = models.ForeignKey(User)