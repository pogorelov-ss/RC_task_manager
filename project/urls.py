from django.conf.urls import patterns, include, url
from rest_framework import routers
import project.views

router = routers.DefaultRouter()
router.register(r'api/tasks', project.views.TaskViewSet)
router.register(r'api/projects', project.views.ProjectViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^projects/$', project.views.ProjectsListView.as_view(), name='projects-list'),
    url(r'^tasks/$', project.views.TasksListView.as_view(), name='tasks-list'),
    url(r'^new$', project.views.TaskCreateView.as_view(), name='task-new'),
    url(r'^edit/(?P<pk>\d+)/$', project.views.TaskUpdateView.as_view(), name='task-edit'),
    url(r'^delete/(?P<pk>\d+)/$', project.views.TaskDeleteView.as_view(), name='task-delete'),
    url(r'^detail/(?P<pk>\d+)/$', project.views.TaskDetailView.as_view(), name='task-detail'),
)
