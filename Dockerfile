FROM python:alpine3.7

RUN  apk add --update --no-cache make

RUN mkdir /work
WORKDIR /work
COPY requirements.txt /work
RUN pip install -r requirements.txt

RUN mkdir /doc
WORKDIR /doc
VOLUME /doc
