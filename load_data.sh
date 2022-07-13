#!/bin/bash

docker-compose exec api python manage.py country_city
docker-compose exec api python manage.py users
docker-compose exec api python manage.py profile_companies
docker-compose exec api python manage.py campaing_header_body
docker-compose exec api python manage.py phases
docker-compose exec api python manage.py rewards
docker-compose exec api python manage.py likes
docker-compose exec api python manage.py book_marked
