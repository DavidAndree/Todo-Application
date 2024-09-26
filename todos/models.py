"""
David Alvarado
cis 218
09/25/24
"""

from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=200)
    due_date = models.DateField()

    def __str__(self):
        return self.name
