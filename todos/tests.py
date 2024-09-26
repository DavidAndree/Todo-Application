from django.test import TestCase
from django.urls import reverse
from .models import Todo


class TodoTests(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(name="Test Todo", due_date="2024-10-01")

    def test_todo_content(self):
        self.assertEqual(self.todo.name, "Test Todo")
        self.assertEqual(self.todo.due_date.strftime("%Y-%m-%d"), "2024-10-01")

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todos/home.html")
        self.assertContains(response, "Test Todo")
