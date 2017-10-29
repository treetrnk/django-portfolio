from django.conf.urls import url
from . import views

appname = "sections"
urlpatterns = [
    url(r'^', views.index, name='index'),
]
