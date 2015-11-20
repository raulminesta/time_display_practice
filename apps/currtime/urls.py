from django.conf.urls import patterns, url
from apps.currtime import views
urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
)