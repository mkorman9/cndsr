from django.http import JsonResponse
from rest_framework.decorators import api_view

from sdk import calculator


@api_view(['GET'])
def hello_world(request, format=None):
    return JsonResponse(status=200, data={
        'result': "Hello world"
    })


@api_view(['GET'])
def add(request, x, y, format=None):
    return JsonResponse(status=200, data={
        'result': calculator.add(x, y)
    })
