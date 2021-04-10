#!/bin/bash

docker-compose -f docker-compose.prod.yml run api sh -c "celery -A api.celery worker -l info"
