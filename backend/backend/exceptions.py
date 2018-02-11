import logging

from django.http import JsonResponse

logger = logging.getLogger(__name__)


def handle_exception(exc, context):
    logger.error('unhandled exception: {}'.format(exc))

    return JsonResponse(status=500, data={
        'error': 'server error'
    })
