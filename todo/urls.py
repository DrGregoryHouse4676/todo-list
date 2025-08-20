from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path(
        "",
        views.TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "tasks/add/",
        views.TaskCreateView.as_view(),
        name="task-add"
    ),
    path(
        "tasks/<int:pk>/update/",
        views.TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        views.TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/toggle/",
        views.ToggleTaskStatusView.as_view(),
        name="task-toggle"
    ),
    path(
        "tags/",
        views.TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/add/",
        views.TagCreateView.as_view(),
        name="tag-add"
    ),
    path(
        "tags/<int:pk>/update/",
        views.TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        views.TagDeleteView.as_view(),
        name="tag-delete"
    ),
]
