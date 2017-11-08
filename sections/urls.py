from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

appname = "sections"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
