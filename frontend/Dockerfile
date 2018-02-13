FROM node:9-alpine

ADD ./frontend .

RUN npm install -g serve

RUN npm run build --production

EXPOSE 8080
CMD serve --port=8080 build
