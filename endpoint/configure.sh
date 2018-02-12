#!/bin/sh

sed -i -e  "s|{FRONTEND_HOST}|${FRONTEND_SERVICE_HOST:-127.0.0.1}|g" /etc/nginx/nginx.conf && \
sed -i -e  "s|{FRONTEND_PORT}|${FRONTEND_SERVICE_PORT:-8080}|g" /etc/nginx/nginx.conf && \
sed -i -e  "s|{BACKEND_HOST}|${BACKEND_SERVICE_HOST:-127.0.0.1}|g" /etc/nginx/nginx.conf && \
sed -i -e  "s|{BACKEND_PORT}|${BACKEND_SERVICE_PORT:-8080}|g" /etc/nginx/nginx.conf
