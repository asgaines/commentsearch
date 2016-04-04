from __future__ import unicode_literals

from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length=100, null=False, help_text='Name of the person having made the comment')
    body = models.TextField(null=False, help_text='The body of the comment')

