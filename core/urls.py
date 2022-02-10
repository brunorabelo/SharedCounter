from django.urls import path

from core import views
from django.urls import include, re_path

urlpatterns = [
    # url(r'^api/$', ''),
    re_path('^$', views.index, name='index'),
    path('createroom/', views.create_room, name='createroom'),
    path('room/<str:room_name>/', views.room),
    path('template/<str:room_name>/', views.room_template, name='room'),

]
