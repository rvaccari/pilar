FROM python:3.10.9-slim

RUN useradd -ms /bin/bash python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip 
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app/
