from django.http import JsonResponse
from rest_framework.decorators import api_view

from utils import printer


@api_view(['GET'])
def root(request, format=None):
    printer.hello_world()
    return JsonResponse(status=200, data="Hello world", safe=False)
