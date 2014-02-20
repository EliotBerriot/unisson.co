from django.conf.urls import patterns, include, url
import views
from .views import ProjectListView, PracticeListView

urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<slug>[-\w]+)/$', views.ProjectDetailView.as_view(), name='project-detail'),
    url(r'^$', ProjectListView.as_view(), name='project-list'),                       
    url(r'^practice', PracticeListView.as_view(), name='practice-list'),                       
)