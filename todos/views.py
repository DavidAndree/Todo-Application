"""
David Alvarado
cis 218
09/25/24
"""

from django.views.generic import ListView
from .models import Todo


class TodoListView(ListView):
    """Todo List View"""

    model = Todo
    template_name = "home.html"
    context_object_name = "todos"
