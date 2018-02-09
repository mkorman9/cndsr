FROM python:3.6-alpine

ARG BUILD_KEY

ENV APP_USER "app"
ENV APP_PATH "/app"

RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH
ADD sdk $APP_PATH/sdk
ADD app $APP_PATH/app
ADD app/nginx.conf /etc/nginx/nginx.conf

RUN addgroup -S $APP_USER && adduser -S -G $APP_USER $APP_USER && \
    python -m venv .venv && \
    .venv/bin/pip install ./sdk && \
    .venv/bin/pip install ./app && \
    chown -R $APP_USER:$APP_USER $APP_PATH
RUN apk add --update build-base linux-headers pcre-dev nginx && \
    .venv/bin/pip install uwsgi==2.0.15 && \
    apk del build-base linux-headers && rm -rf /var/cache/apk/*

EXPOSE 8080
USER $APP_USER

RUN sed -i -e  "s|DEBUG.*=.*True|DEBUG = False|g" app/app/settings.py && \
    sed -i -e  "s|SECRET_KEY.*=.*|SECRET_KEY = \"$BUILD_KEY\"|g" app/app/settings.py

CMD nginx -g 'daemon on;' && \
    exec .venv/bin/uwsgi \
    --socket $APP_PATH/uwsgi.sock \
    --chmod-socket=660 \
    --master \
    --processes 4 \
    --threads 2 \
    --wsgi-file app/app/wsgi.py
