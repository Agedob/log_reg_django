from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg$', views.regi),
    url(r'^done$', views.done),
    url(r'^logs$', views.login),
]