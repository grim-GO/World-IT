from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.watch, name='watch'),

]