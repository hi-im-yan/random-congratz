from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import *

# Create your views here.

@api_view(['GET'])
def test_connection(request):
    return Response({"status": 200, "message": "OK", "description": "Connection to API is OK"})

@api_view(['GET'])
def get_categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(instance=categorias, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(instance=messages, many=True)

    return Response(serializer.data)