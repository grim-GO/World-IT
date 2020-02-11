from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.wor_phone, name='wor_phone'),

]