from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.wor_pad, name='wor_pad'),

]