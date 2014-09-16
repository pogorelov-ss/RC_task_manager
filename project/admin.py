from django.contrib import admin
from .models import Project, Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'status')
    list_filter = ('project',)
    search_fields = ('name',)


class ProjectAdmin(admin.ModelAdmin):
    def task_count(self, obj):
        return Task.objects.filter(project=obj).count()

    task_count.short_description = 'Task count'
    list_display = ('name', 'task_count')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)