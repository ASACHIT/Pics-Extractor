from python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate