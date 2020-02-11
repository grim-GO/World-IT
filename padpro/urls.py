from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.pad_pro, name='pad_pro'),

]