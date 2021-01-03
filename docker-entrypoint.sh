#!/bin/sh
container_type=${CONTAINER_TYPE-DJANGO};
celery_loglevel=${CELERY_LOGLEVEL-INFO};
if [ $container_type = "CELERY" ]; then
  celery -A config.celery_app worker --concurrency 4 --loglevel=$celery_loglevel
else
  python manage.py migrate --noinput
  python manage.py runserver 0.0.0.0:8000
fi;
