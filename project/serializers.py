__author__ = 'pss'
from rest_framework import serializers
from .models import Project, Task


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task

