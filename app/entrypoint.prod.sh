#!/bin/sh

if ["$DATABASE" = "postgres"]
then
    echo "WAITING FOR POSTGRES..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "POSTGESQL STARTED"
fi

exec "$@"
