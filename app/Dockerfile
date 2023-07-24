FROM python:3.10.5-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /mysite

WORKDIR /mysite 

ADD . /mysite
COPY  requirments.txt requirments.txt

RUN pip install -r requirments.txt

COPY . .

EXPOSE 8000

CMD python manage.py runserver


