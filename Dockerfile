# syntax=docker/dockerfile:1
FROM python:3.11.1-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UWSGI_PROCESSES=1
ENV UWSGI_THREADS=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

# cambio a usuario no root
RUN useradd charly
RUN chown -R charly: /code
USER charly
RUN mkdir -p log
RUN mkdir -p static

COPY . /code/

#CMD bash -c "uwsgi --ini uwsgi.ini"
