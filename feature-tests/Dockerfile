FROM python:3.6-alpine

ARG BUILD_KEY

ENV APP_PATH "/tests"

RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH
ADD sdk $APP_PATH/sdk
ADD feature-tests $APP_PATH/feature-tests

RUN python -m venv .venv && \
    .venv/bin/pip install ./sdk && \
    .venv/bin/pip install ./feature-tests

CMD exec .venv/bin/python $APP_PATH/feature-tests/feature_tests
