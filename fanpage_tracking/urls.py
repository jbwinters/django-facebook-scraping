from django.conf.urls import patterns, url

from fanpage_tracking import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

