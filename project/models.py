from django.db import models
from django.core.urlresolvers import reverse


class Project(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    project = models.ForeignKey('Project')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.id})