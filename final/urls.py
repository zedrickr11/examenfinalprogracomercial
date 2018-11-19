from django.conf.urls import include, url
from . import views


urlpatterns = [
        url(r'^pensum/pens/$', views.pensum_index, name ='pensum_index'),
        url(r'^pensum/pens/new/$', views.pensum_new, name='pensum_new'),

    ]
