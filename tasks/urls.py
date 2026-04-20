from django.urls import path

from .views import (
    TaskDetailApiView,
    TaskListCreateApiView,
    task_detail_page,
    task_home_view,
    task_selector_view,
)

urlpatterns = [
    path("tasks/", task_home_view, name="task-home"),
    path("tasks/select/", task_selector_view, name="task-selector"),
    path("tasks/page/<int:pk>/", task_detail_page, name="task-detail-page"),
    path("tasks/api/", TaskListCreateApiView.as_view(), name="task-list-create-api"),
    path("tasks/<int:pk>/", TaskDetailApiView.as_view(), name="task-detail-api"),
]
