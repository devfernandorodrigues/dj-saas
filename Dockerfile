FROM python:3.11-slim-buster
LABEL maintainer="devfernandorodrigues@gmail.com"

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    && apt-get -y install build-essential libpq-dev gettext wget curl \
    && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash \
    && apt-get install -y nodejs \
    && apt-get clean

RUN mkdir -p /project
WORKDIR /project
COPY poetry.lock pyproject.toml /project/

RUN pip install --upgrade pip
RUN pip install poetry==1.4.2
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . /project

RUN addgroup --system user && adduser --system --group user
RUN chown -R user:user /project

USER user
