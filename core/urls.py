from django.urls import path

from core import views
from django.urls import include, re_path

urlpatterns = [
    # url(r'^api/$', ''),
    re_path('^$', views.index, name='index'),
    path('createroom/', views.create_room, name='createroom'),
    path('room/<str:room_name>/', views.room, name='room'),


    ## Teste bruto
    path('template/<str:room_name>/<str:username>', views.room_template, name='room_template'),
    path('template/<str:room_name>/', views.index, name='room_no_username'),
    # path('createroom_template/', views.create_room_template, name='createroom_template'),

]


