import logging

from django.http import JsonResponse
from rest_framework.exceptions import MethodNotAllowed, UnsupportedMediaType, NotFound, ParseError

logger = logging.getLogger(__name__)


def handle_exception(exc, context):
    logger.error('unhandled exception: {}'.format(exc))
    exc_type = type(exc)

    if exc_type == NotFound:
        return handle_not_found(None)
    elif exc_type == ParseError:
        return JsonResponse(status=400, data={
            'error': 'bad request'
        })
    elif exc_type == MethodNotAllowed:
        return JsonResponse(status=405, data={
            'error': 'method not allowed'
        })
    elif exc_type == UnsupportedMediaType:
        return JsonResponse(status=415, data={
            'error': 'unsupported media type'
        })

    return JsonResponse(status=500, data={
        'error': 'server error'
    })


def handle_not_found(_):
    return JsonResponse(status=404, data={
        'error': 'not found'
    })
