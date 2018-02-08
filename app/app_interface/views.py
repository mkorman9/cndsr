from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils import printer


@api_view(['GET'])
def root(request, format=None):
    printer.hello_world()
    return Response(status=200, data="Hello world")
