import os
from collections import namedtuple

import requests
from behave import when, then, given

ServiceLocation = namedtuple('ServiceLocation', ['host', 'port'])


@given('a service')
def step_impl(context):
    context.service_location = ServiceLocation(
        host=os.getenv("BACKEND_SERVICE_HOST"),
        port=os.getenv("BACKEND_SERVICE_PORT")
    )

    assert context.service_location.host is not None, "BACKEND_SERVICE_HOST not set"
    assert context.service_location.port is not None, "BACKEND_SERVICE_PORT not set"


@when('we try to shorten {url}')
def step_impl(context, url):
    context.response = requests.get(
        'http://{}:{}/shorten?url={}'.format(context.service_location.host, context.service_location.port, url)
    )

    context.response.raise_for_status()

    context.response_json = context.response.json()


@then('key should be returned')
def step_impl(context):
    assert context.response_json['key'] is not None, "key was not returned: {}".format(context.response_json['error'])


@then('asking for key redirects to {url}')
def step_impl(context, url):
    key = context.response_json['key']
    response = requests.get(
        'http://{}:{}/{}'.format(context.service_location.host, context.service_location.port, key)
    )

    assert response.status_code == 301, "wrong response code {}".format(response.status_code)
    assert response.headers['Location'] == url, "wrong location '{}'".format(url)
