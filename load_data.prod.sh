#!/bin/bash

docker-compose -f docker-compose.prod.yml exec api python manage.py country_city
docker-compose -f docker-compose.prod.yml exec api python manage.py users
docker-compose -f docker-compose.prod.yml exec api python manage.py profile_companies
docker-compose -f docker-compose.prod.yml exec api python manage.py campaing_header_body
docker-compose -f docker-compose.prod.yml exec api python manage.py rewards
docker-compose -f docker-compose.prod.yml exec api python manage.py phases
docker-compose -f docker-compose.prod.yml exec api python manage.py likes
docker-compose -f docker-compose.prod.yml exec api python manage.py comments
docker-compose -f docker-compose.prod.yml exec api python manage.py book_marked
docker-compose -f docker-compose.prod.yml run api sh -c "python manage.py collectstatic --no-input --clear"
