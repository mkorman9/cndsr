import os
from collections import namedtuple

import requests
from behave import when, then, given

ServiceLocation = namedtuple('ServiceLocation', ['host', 'port'])


@given('a service')
def step_impl(context):
    context.service_location = ServiceLocation(
        host=os.getenv("APP_SERVICE_HOST"),
        port=os.getenv("APP_SERVICE_PORT")
    )

    assert context.service_location.host is not None
    assert context.service_location.port is not None


@when('we request {endpoint} endpoint')
def step_impl(context, endpoint):
    context.response = requests.get(
        'http://{}:{}/'.format(context.service_location.host, context.service_location.port)
    )


@then('{result} should be returned')
def step_impl(context, result):
    context.response.raise_for_status()
    actual_result = context.response.json()['result']
    assert actual_result == result
