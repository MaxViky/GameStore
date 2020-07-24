from django.conf.urls import url
from . import views


urlpatterns = [
    url('^login/$', views.login),
    url('^registration/$', views.reg),
    url('^logout/$', views.logout),
]