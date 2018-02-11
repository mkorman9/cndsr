import random

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

temp_store = {}


@api_view(['GET'])
def go_to(request, key, format=None):
    url = _retrieve_url_by_key(key)
    if not url:
        return JsonResponse(status=404, data={
            'error': 'Key not found'
        })

    return Response(status=301, headers={
        'Location': url
    })


@api_view(['GET'])
def shorten(request, format=None):
    url = request.GET['url']
    if not url:
        return JsonResponse(status=400, data={
            'error': 'Missing url parameter'
        })

    if not _is_url_valid(url):
        return JsonResponse(status=400, data={
            'error': 'Invalid URL'
        })

    key = _store_url_and_get_key(url)
    return JsonResponse(status=200, data={
        'key': key
    })


def _retrieve_url_by_key(key):
    return temp_store[key]  # TODO: retrieve from redis


def _is_url_valid(url):
    return True  # TODO: validate


def _store_url_and_get_key(url):
    key = _generate_key()
    _store_pair(key, url)
    return key


def _generate_key():
    return str(random.randint(0, 2000000))  # TODO: something better + check for collisions


def _store_pair(key, url):
    temp_store[key] = url
