"""
David Alvarado
cis 218
09/25/24
"""

from django.urls import path
from .views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),  # Class based function param
]
