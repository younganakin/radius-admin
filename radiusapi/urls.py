from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.radcheck_list, name='radcheck-list'),
    path('create-user/', views.radcheck_create, name='radcheck-create'),
    path('user-detail/<str:macAddress>/<str:ssid>',
         views.radcheck_detail,
         name='radcheck-detail'),
    path('nas-list/', views.nas_list, name='nas-list'),
    path('create-nas/', views.nas_create, name='nas-create'),
    path('nas-detail/<str:nasname>',
         views.nas_detail,
         name='nas-detail'),
]
