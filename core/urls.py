from django.urls import path

from core import views
from django.conf.urls import url

urlpatterns = [
    # url(r'^api/$', ''),
    url('^$', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),

]
