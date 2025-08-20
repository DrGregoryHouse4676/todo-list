from django.test import TestCase
from todo.models import Tag, Task


class ModelsStrTest(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="work")
        self.assertEqual(str(tag), "work")

    def test_task_str_truncated(self):
        long_text = "x" * 120
        task = Task.objects.create(content=long_text)
        # __str__ returns the first 50 characters
        self.assertEqual(str(task), long_text[:50])
