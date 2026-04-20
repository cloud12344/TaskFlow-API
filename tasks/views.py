from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import generics

from .models import Task
from .serializers import TaskSerializer


class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        input_formats=["%Y-%m-%dT%H:%M"],
    )

    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date"]


class TaskListCreateApiView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by("id")
    serializer_class = TaskSerializer


class TaskDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all().order_by("id")
    serializer_class = TaskSerializer


def task_home_view(request):
    tasks = Task.objects.all().order_by("id")

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("task-detail-page", pk=task.id)
    else:
        form = TaskForm(initial={"status": "pending", "priority": "medium"})

    return render(request, "tasks/task_home.html", {"tasks": tasks, "form": form})


def task_selector_view(request):
    tasks = Task.objects.all().order_by("id")
    return render(request, "tasks/task_selector.html", {"tasks": tasks})


def task_detail_page(request, pk):
    task = get_object_or_404(Task, pk=pk)
    tasks = list(Task.objects.all().order_by("id"))
    current_index = next((index for index, item in enumerate(tasks) if item.id == task.id), 0)
    previous_task = tasks[current_index - 1] if current_index > 0 else None
    next_task = tasks[current_index + 1] if current_index < len(tasks) - 1 else None

    return render(
        request,
        "tasks/task_detail_page.html",
        {
            "task": task,
            "tasks": tasks,
            "previous_task": previous_task,
            "next_task": next_task,
        },
    )
