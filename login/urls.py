from django.conf.urls import url
from . import views


urlpatterns = [
    url('^login/$', views.logIn),
    url('^registration/$', views.reg),
    url('^logout/$', views.logOut),
]