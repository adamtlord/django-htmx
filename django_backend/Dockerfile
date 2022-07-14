FROM python:3.8-alpine3.12 AS base

LABEL authors="Michal Kopacki <michal.kopacki@tivix.com>, Michal Weinert <michal.weinert@tivix.com>"

ARG env
ENV ENV ${env:-dev}

RUN apk update
RUN apk add --upgrade --no-cache "postgresql-client" "postgresql-contrib" "postgresql-dev" bash curl
RUN apk add --upgrade --no-cache py-pip g++ linux-headers gcc make libffi-dev uwsgi-python uwsgi wget

RUN apk add --upgrade --no-cache python3 python3-dev openssl-dev cargo

ENV WAITFORIT_VERSION="v2.2.0"
RUN curl -o /usr/local/bin/waitforit -sSL https://github.com/maxcnunes/waitforit/releases/download/$WAITFORIT_VERSION/waitforit-linux_amd64 && \
    chmod +x /usr/local/bin/waitforit

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ADD . /code/

WORKDIR /code

# make poetry available in image && do not create a virtualEnv && install dependencies w/o user input
RUN source $HOME/.poetry/env && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

WORKDIR /

RUN mkdir -p /data/static

VOLUME /data

EXPOSE 8000

WORKDIR /code

## Dev image, for use during local development
FROM base AS dev
