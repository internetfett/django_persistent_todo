from django.conf.urls import patterns, url

from django_persistent_todo.views import AddToDoView, DelToDoView

urlpatterns = patterns('',
    url(r'^add/$', AddToDoView.as_view(), name='add'),
    url(r'^delete/(?P<pk>\d+)$', DelToDoView.as_view(), name='delete'),
)
