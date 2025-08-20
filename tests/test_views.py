from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from todo.models import Task, Tag


class TaskViewsTests(TestCase):
    def setUp(self):
        self.tag_work = Tag.objects.create(name="work")
        self.tag_home = Tag.objects.create(name="home")

        now = timezone.now()

        # done=False, older
        self.t1 = Task.objects.create(content="old undone", is_done=False)
        self.t1.created_at = now - timedelta(hours=2)
        self.t1.save(update_fields=["created_at"])

        # done=False, newer
        self.t2 = Task.objects.create(content="new undone", is_done=False)
        self.t2.created_at = now - timedelta(hours=1)
        self.t2.save(update_fields=["created_at"])
        self.t2.tags.add(self.tag_work)

        # done=True
        self.t3 = Task.objects.create(content="done task", is_done=True)
        self.t3.created_at = now - timedelta(hours=3)
        self.t3.save(update_fields=["created_at"])

    def test_home_uses_template_and_has_tags_link(self):
        url = reverse("todo:task-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "todo/task_list.html")
        # the sidebar should have a link to the tags page
        self.assertContains(resp, reverse("todo:tag-list"))

    def test_task_ordering_not_done_first_then_newest(self):
        resp = self.client.get(reverse("todo:task-list"))
        tasks = list(resp.context["tasks"])
        self.assertEqual([t.pk for t in tasks],
                         [self.t2.pk, self.t1.pk, self.t3.pk])

    def test_toggle_status(self):
        self.assertFalse(self.t1.is_done)
        resp = self.client.post(
            reverse("todo:task-toggle", args=[self.t1.pk]), follow=True
        )
        self.assertRedirects(resp, reverse("todo:task-list"))
        self.t1.refresh_from_db()
        self.assertTrue(self.t1.is_done)

    def test_create_task_with_tags(self):
        data = {
            "content": "created via post",
            "is_done": False,
            "tags": [self.tag_work.pk, self.tag_home.pk],
        }
        resp = self.client.post(reverse("todo:task-add"), data, follow=True)
        self.assertRedirects(resp, reverse("todo:task-list"))

        task = Task.objects.get(content="created via post")
        self.assertSetEqual(
            set(task.tags.values_list("name", flat=True)),
            {"work", "home"},
        )

    def test_update_task(self):
        resp = self.client.post(
            reverse("todo:task-update", args=[self.t1.pk]),
            {"content": "updated", "is_done": self.t1.is_done},
            follow=True,
        )
        self.assertRedirects(resp, reverse("todo:task-list"))
        self.t1.refresh_from_db()
        self.assertEqual(self.t1.content, "updated")

    def test_delete_task(self):
        count_before = Task.objects.count()
        resp = self.client.post(
            reverse("todo:task-delete", args=[self.t3.pk]), follow=True
        )
        self.assertRedirects(resp, reverse("todo:task-list"))
        self.assertEqual(Task.objects.count(), count_before - 1)


class TagViewsTests(TestCase):
    def setUp(self):
        self.t1 = Tag.objects.create(name="work")
        self.t2 = Tag.objects.create(name="home")

    def test_tag_list_uses_template_and_shows_rows(self):
        url = reverse("todo:tag-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "todo/tag_list.html")
        self.assertContains(resp, "#work")
        self.assertContains(resp, "#home")
