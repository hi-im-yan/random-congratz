from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import *

from . import utils as utils

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

@api_view(['POST'])
def generate_message(request):
    category = request.data['category']
    message = ''

    if category == 1:
        message = utils.get_random_message_by_category(category)

    elif category == 2:
        message = utils.get_random_message_by_category(category)

    elif category == 3:
        message = utils.get_random_message_by_category(category)



    if request.data['name'] == "":
        context = {
            "message": message.replace('{name}', '')
        }
    elif request.data['name'] != "":
        context = {
            "message": message.replace('{name}', request.data['name'])
        }

    return Response(context)

