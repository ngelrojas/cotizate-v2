#!/bin/sh

gunicorn --bind 0.0.0.0:16610 api.wsgi:application
