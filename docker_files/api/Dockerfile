FROM python:3.6
ENV PYTHONUNBUFFERED 1

WORKDIR /code
ADD ./ /code

RUN apt-get update

RUN pip install -r ./requirements.txt
