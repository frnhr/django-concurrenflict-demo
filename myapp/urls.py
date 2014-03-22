from django.conf.urls import patterns, url

from .views import Home, List, Create, Update

urlpatterns = patterns('',
    url(r'^list/', List.as_view(), name='list'),
    url(r'^create/', Create.as_view(), name='create'),
    url(r'^update/(?P<pk>[\d-]+)/', Update.as_view(), name='update'),
    url(r'', Home.as_view(), name='home'),
)
