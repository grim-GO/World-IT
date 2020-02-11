from django.conf.urls import url
from . import views
from .views import EmailView
urlpatterns = [

    url(r'^$', views.about, name='about'),
    url(r'^$', EmailView.as_view(), name='email_view'),
    
]