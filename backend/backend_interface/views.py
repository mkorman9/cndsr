import os
import random

import redis
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.decorators import api_view


@api_view(['GET'])
def go_to(request, key, format=None):
    url = _retrieve_url_by_key(key)
    if not url:
        return JsonResponse(status=404, data={
            'error': 'key not found'
        })

    return HttpResponseRedirect(redirect_to=url)


@api_view(['POST'])
def shorten(request, format=None):
    url = request.data.get('url')
    if not url:
        return JsonResponse(status=400, data={
            'error': 'missing url parameter'
        })

    if not _is_url_valid(url):
        return JsonResponse(status=400, data={
            'error': 'invalid URL'
        })

    key = _store_url_and_get_key(url)
    return JsonResponse(status=200, data={
        'key': key
    })


def _retrieve_url_by_key(key):
    connection = _get_redis_connection()
    return connection.get(key)


def _is_url_valid(url):
    return True  # TODO: validate


def _store_url_and_get_key(url):
    key = _generate_key()
    _store_pair(key, url)
    return key


def _generate_key():
    return str(random.randint(0, 2000000))  # TODO: something better + check for collisions


def _store_pair(key, url):
    connection = _get_redis_connection()
    connection.set(key, url)


def _get_redis_connection():
    host, port = os.getenv("REDIS_SERVICE_HOST"), os.getenv("REDIS_SERVICE_PORT")
    if not host or not port:
        raise Exception('REDIS_SERVICE_HOST or REDIS_SERVICE_PORT not set')

    return redis.StrictRedis(host=host, port=int(port), db=0)
