import os

import requests
import sys

if __name__ == '__main__':
    service_host = os.getenv("APP_SERVICE_HOST")
    service_port = os.getenv("APP_SERVICE_PORT")

    response = requests.get('http://{}:{}/'.format(service_host, service_port))
    response.raise_for_status()

    response_content = response.json()
    if response_content != "Hello world!":
        print("invalid content {}".format(response_content), file=sys.stderr)
        sys.exit(1)
    else:
        print("OK: {}".format(response_content), file=sys.stderr)
