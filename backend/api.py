from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def test_connection(request):
    return Response({"status": 200, "message": "OK", "description": "Connection to API is OK"})