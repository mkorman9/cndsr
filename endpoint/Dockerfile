FROM nginx:stable-alpine

COPY ./endpoint/configure.sh .
COPY ./endpoint/nginx.conf /etc/nginx/nginx.conf

EXPOSE 8080

CMD sh ./configure.sh && nginx -g 'daemon off;'
