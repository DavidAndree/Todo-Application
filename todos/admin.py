"""
David Alvarado
cis 218
09/25/24
"""

from django.contrib import admin
from .models import Todo

admin.site.register(Todo)  # For Admin Registration
