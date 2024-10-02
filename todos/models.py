"""
David Alvarado
cis 218
09/25/24
"""

from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=150)  # Adjusted based on the ERD
    complete_by = models.DateTimeField()  # Changed to correct name

    def __str__(self):
        return self.name
