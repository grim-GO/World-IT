from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.wor_pods, name='wor_pods'),

]