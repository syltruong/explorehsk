FROM nginx:alpine

ARG EXTERNAL_IP

COPY . /usr/share/nginx/html

RUN if [ ! -z "$EXTERNAL_IP" ]; then \
        sed -i -e "s/0\.0\.0\.0/$EXTERNAL_IP/g" /usr/share/nginx/html/index.js; \
    fi