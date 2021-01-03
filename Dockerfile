FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gettext libgettextpo-dev && apt-get install -y uwsgi

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENV STATIC_ROOT /static
ENV MEDIA_ROOT /media

WORKDIR /app

# Copy source code
COPY . /app

# Collect static
RUN python manage.py collectstatic --noinput

CMD ["/docker-entrypoint.sh"]