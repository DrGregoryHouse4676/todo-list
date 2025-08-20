from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "task/add/",
        views.TaskCreateView.as_view(),
        name="task-add"
    ),
    path(
        "task/<int:pk>/update",
        views.TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete",
        views.TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task/<int:pk>/toggle/",
        views.ToggleTaskStatusView.as_view(),
        name="task-toggle"
    ),
    path(
        "tags/",
        views.TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tag/add/",
        views.TagCreateView.as_view(),
        name="tag-add"
    ),
    path(
        "tag/<int:pk>/update",
        views.TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tag/<int:pk>/delete",
        views.TagDeleteView.as_view(),
        name="tag-delete"
    ),
]
