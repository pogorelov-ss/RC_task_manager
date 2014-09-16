from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from rest_framework import viewsets
from serializers import TaskSerializer, ProjectSerializer

from .models import Project, Task


class ProjectsListView(ListView):
    model = Project


class TasksListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task

    def get_success_url(self):
        return reverse('tasks-list')

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('task-new')

        return context


class TaskUpdateView(UpdateView):
    model = Task

    def get_success_url(self):
        return reverse('tasks-list')

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('task-edit', kwargs={'pk': self.get_object().id})

        return context


class TaskDeleteView(DeleteView):
    model = Task

    def get_success_url(self):
        return reverse('tasks-list')


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    model = Project
    # queryset = Project.objects.all()
    # serializer_class = ProjectSerializer