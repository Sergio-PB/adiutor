FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /adiutor

ADD requirements.txt /adiutor/
RUN pip install -r requirements.txt
ADD . /adiutor/
