from django.urls import path

from back_end_developer_q1 import views

urlpatterns = [
    path('last_points', views.last_points, name='last_points'),
    path('last_points2', views.get_last_points, name='last_points2'),
]
