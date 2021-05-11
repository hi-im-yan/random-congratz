from django.urls import path

from . import api

urlpatterns = [
    path('', api.test_connection, name='routes'),
    path('categorias', api.get_categorias, name='categoria'),
    path('mensagens', api.get_messages, name='mensagens'),
    path('generate_message', api.generate_message, name='generate_message'),
]