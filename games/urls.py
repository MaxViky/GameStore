from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.GameView.as_view()),
]