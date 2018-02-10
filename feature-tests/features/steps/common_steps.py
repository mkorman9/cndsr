import os
from collections import namedtuple

import requests
import sys
from behave import when, then, given

ServiceLocation = namedtuple('ServiceLocation', ['host', 'port'])


@given('a service')
def step_impl(context):
    context.service_location = ServiceLocation(
        host=os.getenv("BACKEND_SERVICE_HOST"),
        port=os.getenv("BACKEND_SERVICE_PORT")
    )

    assert context.service_location.host is not None
    assert context.service_location.port is not None


@when('we request {endpoint} endpoint')
def step_impl(context, endpoint):
    context.response = requests.get(
        'http://{}:{}{}'.format(context.service_location.host, context.service_location.port, endpoint)
    )


@then('{result} should be returned')
def step_impl(context, result):
    context.response.raise_for_status()

    actual_result = context.response.json()['result']
    actual_result = str(actual_result)

    if actual_result != result:
        print("{} != {}".format(actual_result, result), file=sys.stderr)
        raise AssertionError()
