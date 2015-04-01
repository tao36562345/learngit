from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^investigate/', 'west.views.investigate'),
)
