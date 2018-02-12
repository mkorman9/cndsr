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
    context.response = requests.post(
        'http://{}:{}/shorten'.format(context.service_location.host, context.service_location.port),
        json={
            "url": url
        }
    )


@then('key should be returned')
def step_impl(context):
    context.response.raise_for_status()
    context.response_json = context.response.json()

    assert context.response_json['key'] is not None, "key was not returned: {}".format(context.response_json['error'])


@then('request should be rejected')
def step_impl(context):
    assert context.response.status_code == 400, "wrong response code {}".format(context.response.status_code)


@then('asking for key redirects to {url}')
def step_impl(context, url):
    key = context.response_json['key']
    response = requests.get(
        'http://{}:{}/{}'.format(context.service_location.host, context.service_location.port, key),
        allow_redirects=False
    )

    assert response.status_code == 302, "wrong response code {}".format(response.status_code)
    assert response.headers['Location'] == url, "wrong location '{}'".format(url)


@then('asking for {key} gives 404')
def step_impl(context, key):
    response = requests.get(
        'http://{}:{}/{}'.format(context.service_location.host, context.service_location.port, key),
        allow_redirects=False
    )

    assert response.status_code == 404, "wrong response code {}".format(response.status_code)
