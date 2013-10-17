from django.conf.urls import patterns, url

from django_persistent_todo.views import AddToDoView

urlpatterns = patterns('',
    url(r'^add/$', AddToDoView.as_view(), name='add'),
)
