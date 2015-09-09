# Dev: Rohan
# Date: 09/08/2015
# Desc: To create a URLconf in the polls directory, create a file called urls.py.

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
