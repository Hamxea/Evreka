from django.urls import path

from back_end_developer_q2 import views

urlpatterns = [
    path('collection_frequency_bin_operation', views.collection_frequency_bin_operation, name='collection_frequency_bin_operation'),
]
