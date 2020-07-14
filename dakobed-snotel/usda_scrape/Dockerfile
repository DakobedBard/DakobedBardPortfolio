FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache bash coreutils grep sed

RUN apk update \
    && apk add  gcc python3-dev musl-dev
RUN apk update
RUN apk add vim

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY snotel.py /usr/src/app/snotel.py
COPY create_tables.py /usr/src/app/create_tables.py

