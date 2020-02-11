from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.wor_phone_pro, name='wor_phone_pro'),

]