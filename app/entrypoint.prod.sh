#!/bin/sh

if ["$DATABASE" = "cotizate_db"]
then
    echo "WAITING FOR POSTGRES..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "POSTGESQL STARTED"
fi

python manage.py makemigrations
python manage.py migrate

exec "$@"
