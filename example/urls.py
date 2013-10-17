from django.conf.urls import patterns, include, url
from django.contrib import admin

from example.views import ExampleView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ExampleView.as_view(), name='example'),
    url(r'^django_persistent_todo/', include('django_persistent_todo.urls')),
)
