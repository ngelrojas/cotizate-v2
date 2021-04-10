#!/bin/sh

# gunicorn --bind 0.0.0.0:16610 api.wsgi:application

docker-compose run api sh -c "celery -A api.celery worker -l INFO"
