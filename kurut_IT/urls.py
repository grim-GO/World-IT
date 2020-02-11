"""kurut_IT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from django.contrib import admin


urlpatterns = [
    url(r'^worpods/', include('worpods.urls')),
    url(r'^worphone/pro/', include('worphonepro.urls')),
    url(r'^worphone/', include('worphone.urls')),
    url(r'^worpad/', include('worpad.urls')),
    url(r'^watch/', include('watch.urls')),
    url(r'^worpad/pro/', include('padpro.urls')),
    url(r'^worbook/', include('worbook.urls')),
    url(r'^worbook/lite/', include('lite.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^admin/', admin.site.urls),
]
