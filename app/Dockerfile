FROM python:3.6

ENV APP_USER "sandbox"
ENV APP_PATH "/app"

RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH
ADD sdk $APP_PATH/sdk
ADD app $APP_PATH/app

RUN adduser --disabled-password --gecos "" --system --no-create-home $APP_USER && \
    chown -R $APP_USER $APP_PATH
RUN python -m venv .venv && \
    .venv/bin/pip install ./sdk && \
    .venv/bin/pip install ./app

EXPOSE 8080

USER $APP_USER
CMD exec .venv/bin/python -m app
