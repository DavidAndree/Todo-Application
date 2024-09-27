"""
David Alvarado
cis 218
09/25/24
"""

from django.test import TestCase
from django.urls import reverse
from .models import Todo


class TodoTests(TestCase):
    """Todo Test"""

    def setUp(self):
        self.todo = Todo.objects.create(name="Test Todo", due_date="2024-10-02")

    def test_todo_content(self):
        """Todo Todo Content"""
        self.assertEqual(self.todo.name, "Test Todo")
        self.assertEqual(self.todo.due_date, "2024-10-02")

    def test_homepage(self):
        """Test Home Page"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Test Todo")
