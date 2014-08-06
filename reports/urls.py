from django.conf.urls import patterns, url

from reports import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^listUsers/$', views.listUsers, name='listUsers'),
    #url(r'^listProperty/$', views.listProperty, name='listProperty'),
    url(r'^(?P<user_id>\d+)/member/$', views.member, name='member'),
    url(r'^(?P<user_id>\d+)/memberView/$', views.memberView, name='memberView'),   
    
    )
