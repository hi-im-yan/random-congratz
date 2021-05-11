from django.urls import path

from . import api

urlpatterns = [
    path('', api.test_connection, name='routes'),
]