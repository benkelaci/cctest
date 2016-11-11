from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mentor_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<opinion_id>[0-9]+)/vote/$', views.opinion, name='vote'),
]