"""
David Alvarado
cis 218
09/25/24
"""

from django.apps import AppConfig


class TodosConfig(AppConfig):
    """Todos Config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "todos"
