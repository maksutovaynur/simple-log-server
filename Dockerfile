FROM python:3.8-slim-buster
RUN mkdir /src
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY src /src
WORKDIR /
