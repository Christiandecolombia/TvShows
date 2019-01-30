from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^new$',views.new),
    url(r'^edit/(?P<id>[0-9]+)$',views.edit),
    url(r'^create$',views.create),
    url(r'^(?P<id>[0-9]+)$', views.view),
    url(r'^delete/(?P<id>[0-9]+)$',views.delete),
    url(r'^editshow/(?P<id>[0-9]+)$',views.editshow),
]